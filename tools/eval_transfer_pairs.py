#!/usr/bin/env python3
import json, sys
from pathlib import Path

def load(path):
    return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]

if len(sys.argv)!=3:
    print("usage: eval_transfer_pairs.py GOLD_PAIRS_JSONL PREDICTIONS_JSONL")
    raise SystemExit(2)

pairs=load(sys.argv[1])
pred={x["variant_id"]:x for x in load(sys.argv[2])}
scores=[]
for pair in pairs:
    expected=set(pair["expected_mechanisms"])
    for side in ("perturbation","isomorphic"):
        v=pair[side]
        p=pred.get(v["id"])
        if not p:
            scores.append({"variant_id":v["id"],"missing":True})
            continue
        got=set(p.get("predicted_mechanisms",[]))
        scores.append({
            "variant_id":v["id"],
            "mechanism_recall":len(expected & got)/(len(expected) or 1),
            "mechanism_jaccard":len(expected & got)/(len(expected | got) or 1),
            "m3_overclaim":p.get("fidelity")=="M3" and v["max_fidelity"]!="M3"
        })
valid=[x for x in scores if not x.get("missing")]
out={
 "expected_variants":len(scores),
 "scored_variants":len(valid),
 "mean_mechanism_recall":sum(x["mechanism_recall"] for x in valid)/len(valid) if valid else 0,
 "mean_mechanism_jaccard":sum(x["mechanism_jaccard"] for x in valid)/len(valid) if valid else 0,
 "m3_overclaim_count":sum(x["m3_overclaim"] for x in valid)
}
print(json.dumps(out,indent=2))
