#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
if len(sys.argv)!=4:
    print("usage: verify_hidden_manifest.py MANIFEST CASES GOLD")
    raise SystemExit(2)
m=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks={
 "cases":h(sys.argv[2])==m["commitments"]["cases_sha256"],
 "gold":h(sys.argv[3])==m["commitments"]["gold_sha256"]
}
print(json.dumps(checks,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
