#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: commit_hidden_predictions.py PREDICTIONS_JSON RUN_MANIFEST_JSON")
    raise SystemExit(2)

prediction_path = Path(sys.argv[1])
manifest_path = Path(sys.argv[2])

data = json.loads(prediction_path.read_text(encoding="utf-8"))
digest = hashlib.sha256(prediction_path.read_bytes()).hexdigest()

manifest = {
    "run_id": data["run_id"],
    "evaluation_provenance": data["evaluation_provenance"],
    "skill_version": data["skill_version"],
    "prediction_file": prediction_path.name,
    "prediction_sha256": digest,
    "gold_opened_before_commit": False,
    "prediction_frozen": True
}

manifest_path.write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print(json.dumps(manifest, indent=2, ensure_ascii=False))
