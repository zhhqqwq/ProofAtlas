#!/usr/bin/env python3
import json, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

try:
    import jsonschema
except ImportError:
    jsonschema = None

def load_data(path):
    p=Path(path)
    txt=p.read_text(encoding="utf-8")
    if p.suffix.lower() in {".yaml",".yml"}:
        if yaml is None:
            raise RuntimeError("PyYAML is required for YAML validation")
        return yaml.safe_load(txt)
    return json.loads(txt)

def build_indexes(g):
    entities={x["id"]:x for x in g["entities"]}
    scopes={x["id"]:x for x in g["scopes"]}
    relations={x["id"]:x for x in g["relations"]}
    mentions={x["id"]:x for x in g["mentions"]}
    return entities,scopes,relations,mentions

def scope_ancestors(scopes, sid):
    out=[]
    seen=set()
    cur=sid
    while cur is not None:
        if cur in seen:
            raise ValueError(f"scope cycle at {cur}")
        seen.add(cur); out.append(cur)
        s=scopes.get(cur)
        if s is None:
            break
        cur=s.get("parent_scope")
    return out

def reasoning_visible(obj, scope_id, scopes):
    home=obj.get("home_scope")
    if home is None:
        return False
    ancestors=scope_ancestors(scopes,scope_id)
    if home in ancestors:
        return True
    scope=scopes.get(scope_id,{})
    return obj.get("id") in scope.get("imports",[]) or obj.get("id") in scope.get("exports",[])

def validate_graph(g, schema=None, signatures=None):
    errors=[]
    if schema is not None and jsonschema is not None:
        try:
            jsonschema.Draft202012Validator(schema).validate(g)
        except jsonschema.ValidationError as e:
            errors.append("JSON_SCHEMA: "+e.message)
            return errors

    entities,scopes,relations,mentions=build_indexes(g)
    all_ids=set(entities)|set(scopes)|set(relations)|set(mentions)

    lists=[g["entities"],g["scopes"],g["relations"],g["mentions"]]
    flat=[x["id"] for arr in lists for x in arr]
    if len(flat)!=len(set(flat)):
        errors.append("ID_UNIQUENESS: IDs must be globally unique")

    root=g["graph"]["root_scope"]
    if root not in scopes:
        errors.append(f"ROOT_SCOPE: {root} missing")

    for s in scopes.values():
        p=s.get("parent_scope")
        if p is not None and p not in scopes:
            errors.append(f"SCOPE_PARENT: {s['id']} -> missing {p}")
        try: scope_ancestors(scopes,s["id"])
        except ValueError as e: errors.append("SCOPE_CYCLE: "+str(e))

    for e in entities.values():
        if e["home_scope"] not in scopes:
            errors.append(f"ENTITY_SCOPE: {e['id']} home_scope missing")
        for r in e.get("references",[]):
            if r not in entities:
                errors.append(f"ENTITY_REFERENCE: {e['id']} -> missing {r}")

    sigs=(signatures or {}).get("signatures",{})
    for r in relations.values():
        typ=r["relation_type"]
        sig=sigs.get(typ)
        if sig is None:
            errors.append(f"RELATION_SIGNATURE: {r['id']} unknown type {typ}")
            continue
        if r["semantic_mode"]!=sig["semantic_mode"]:
            errors.append(f"RELATION_MODE: {r['id']} expected {sig['semantic_mode']}")
        if r["layer"]!=sig["layer"]:
            errors.append(f"RELATION_LAYER: {r['id']} expected {sig['layer']}")
        if r["scope"] not in scopes:
            errors.append(f"RELATION_SCOPE: {r['id']} missing scope {r['scope']}")
            continue
        by_role={}
        for p in r["participants"]:
            by_role.setdefault(p["role"],[]).append(p["ref"])
            if p["ref"] not in all_ids:
                errors.append(f"PARTICIPANT_REF: {r['id']} missing {p['ref']}")
        for role,rspec in sig["roles"].items():
            vals=by_role.get(role,[])
            if len(vals)<rspec.get("min",0):
                errors.append(f"CARDINALITY: {r['id']} role {role} min {rspec.get('min',0)}")
            if "max" in rspec and len(vals)>rspec["max"]:
                errors.append(f"CARDINALITY: {r['id']} role {role} max {rspec['max']}")
            for ref in vals:
                if ref in entities:
                    actual=entities[ref]["kind"]
                elif ref in relations:
                    actual="RelationEvent"
                elif ref in scopes:
                    actual="Scope"
                elif ref in mentions:
                    actual="Mention"
                else:
                    continue
                if actual not in rspec["allowed"]:
                    errors.append(f"ENDPOINT_TYPE: {r['id']} role {role}: {actual} not in {rspec['allowed']}")
        extra_roles=set(by_role)-set(sig["roles"])
        if extra_roles:
            errors.append(f"ROLE_UNKNOWN: {r['id']} roles {sorted(extra_roles)}")
        if sig.get("requires_fidelity") and not r.get("fidelity"):
            errors.append(f"FIDELITY_REQUIRED: {r['id']}")
        if sig.get("requires_loss_profile") and not r.get("loss_profile"):
            errors.append(f"LOSS_PROFILE_REQUIRED: {r['id']}")
        policy=sig.get("scope_policy")
        if policy in {"reasoning_visible","reasoning_visible_or_created_here"}:
            for p in r["participants"]:
                ref=p["ref"]
                if ref in entities:
                    obj=entities[ref]
                    if not reasoning_visible(obj,r["scope"],scopes):
                        if policy=="reasoning_visible_or_created_here" and p["role"]=="output":
                            continue
                        errors.append(f"SCOPE_VISIBILITY: {r['id']} cannot reason over {ref} from {r['scope']}")
        if r["semantic_mode"]=="event":
            for cp in r.get("event",{}).get("causal_parents",[]):
                if cp not in relations:
                    errors.append(f"CAUSAL_PARENT: {r['id']} missing {cp}")
                elif relations[cp]["semantic_mode"]!="event":
                    errors.append(f"CAUSAL_PARENT_MODE: {r['id']} parent {cp} not event")

        if typ == "export":
            exported = by_role.get("exported", [])
            srcs = by_role.get("source_scope", [])
            tgts = by_role.get("target_scope", [])
            if len(srcs)==1 and len(tgts)==1 and srcs[0] in scopes and tgts[0] in scopes:
                src, tgt = srcs[0], tgts[0]
                if tgt not in scope_ancestors(scopes, src):
                    errors.append(f"EXPORT_TARGET: {r['id']} target {tgt} must be an ancestor of {src}")
                for ref in exported:
                    if ref in entities and not reasoning_visible(entities[ref], src, scopes):
                        errors.append(f"EXPORT_SOURCE_VISIBILITY: {r['id']} cannot export {ref} from {src}")
                    if ref not in scopes[src].get("exports", []):
                        errors.append(f"EXPORT_CACHE_SOURCE: {r['id']} {ref} missing from {src}.exports")
                    if ref not in scopes[tgt].get("imports", []):
                        errors.append(f"EXPORT_CACHE_TARGET: {r['id']} {ref} missing from {tgt}.imports")

    event_ids={rid for rid,r in relations.items() if r["semantic_mode"]=="event"}
    adj={rid:[] for rid in event_ids}
    for rid in event_ids:
        for p in relations[rid].get("event",{}).get("causal_parents",[]):
            if p in event_ids:
                adj[p].append(rid)
    state={}
    def dfs(n):
        state[n]=1
        for m in adj.get(n,[]):
            if state.get(m)==1:
                return False
            if state.get(m,0)==0 and not dfs(m):
                return False
        state[n]=2
        return True
    for n in event_ids:
        if state.get(n,0)==0 and not dfs(n):
            errors.append("CAUSAL_CYCLE: event causal graph must be acyclic")
            break

    for m in mentions.values():
        if m["entity_id"] not in entities:
            errors.append(f"MENTION_ENTITY: {m['id']} missing {m['entity_id']}")
        if m["scope"] not in scopes:
            errors.append(f"MENTION_SCOPE: {m['id']} missing scope")
        sp=m["source_span"]
        if sp not in entities or entities[sp]["kind"]!="PresentationSpan":
            errors.append(f"MENTION_SPAN: {m['id']} source_span must be PresentationSpan")

    for seq in g["presentation_sequences"]:
        for sp in seq["ordered_spans"]:
            if sp not in entities or entities[sp]["kind"]!="PresentationSpan":
                errors.append(f"PRESENTATION_SEQUENCE: {seq['id']} contains non-span {sp}")

    return errors

def main(argv):
    if len(argv)<4:
        print("usage: validate_cpg.py GRAPH SCHEMA SIGNATURES", file=sys.stderr); return 2
    graph=load_data(argv[1]); schema=load_data(argv[2]); sig=load_data(argv[3])
    errs=validate_graph(graph,schema,sig)
    if errs:
        print("INVALID")
        for e in errs: print("- "+e)
        return 1
    print("VALID")
    return 0

if __name__=="__main__":
    raise SystemExit(main(sys.argv))
