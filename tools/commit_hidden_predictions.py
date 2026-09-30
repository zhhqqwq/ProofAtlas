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

if data.get("evaluation_provenance") != "sealed-hidden":
    raise SystemExit("Refusing commitment: evaluation_provenance must be sealed-hidden")

att = data.get("evaluator_context_attestation", {})
if att.get("gold_visible_before_commit") is not False:
    raise SystemExit("Refusing commitment: gold_visible_before_commit must be false")
if att.get("prior_gold_transcript_available") is not False:
    raise SystemExit("Refusing commitment: prior_gold_transcript_available must be false")

fresh_slice = data.get("fresh_slice") or {}
for key in ("slice_id", "statement_sha256", "gold_commitment_sha256"):
    if not fresh_slice.get(key):
        raise SystemExit(f"Refusing commitment: fresh_slice.{key} is required")

predictions = data.get("predictions")
if not isinstance(predictions, list) or not predictions:
    raise SystemExit("Refusing commitment: predictions must be a non-empty list")

digest = hashlib.sha256(prediction_path.read_bytes()).hexdigest()

manifest = {
    "run_id": data["run_id"],
    "evaluation_provenance": data["evaluation_provenance"],
    "skill_version": data["skill_version"],
    "fresh_slice": fresh_slice,
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
