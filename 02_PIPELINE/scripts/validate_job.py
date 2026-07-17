from __future__ import annotations

import argparse
import re

from common import REPO_ROOT, flatten_strings, load_json, resolve_repo_path

REQUIRED = {"schema_version","job_id","character_id","status","platform","aspect_ratio","content_category","scene","wardrobe","hair_style","expression","camera_profile","anchor_ids","required_outputs","manual_approval_required"}
ALLOWED_STATUS = {"DRAFT","READY_FOR_PROMPT_ASSEMBLY","PROMPT_READY","GENERATED","QC_PENDING","APPROVED","REJECTED"}
ALLOWED_RATIOS = {"9:16","4:5","1:1","16:9"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a Kaia generation job.")
    parser.add_argument("job_path")
    args = parser.parse_args()

    path = resolve_repo_path(args.job_path)
    job = load_json(path)
    identity = load_json(REPO_ROOT / "01_IDENTITY" / "IDENTITY_KERNEL.json")
    anchors = load_json(REPO_ROOT / "01_IDENTITY" / "ANCHOR_REGISTRY.json")
    qc = load_json(REPO_ROOT / "01_IDENTITY" / "QC_RULES.json")
    errors: list[str] = []

    for field in sorted(REQUIRED - set(job)):
        errors.append(f"Missing required field: {field}")
    if job.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    if not re.fullmatch(r"KAIA-\d{8}-\d{3}", str(job.get("job_id", ""))):
        errors.append("job_id must match KAIA-YYYYMMDD-###")
    if job.get("character_id") != identity["character_id"]:
        errors.append("character_id does not match locked identity")
    if job.get("status") not in ALLOWED_STATUS:
        errors.append("invalid status")
    if job.get("aspect_ratio") not in ALLOWED_RATIOS:
        errors.append("invalid aspect ratio")
    if job.get("manual_approval_required") is not True:
        errors.append("manual approval must be required")

    for key in ("location","time","lighting","action"):
        if not str(job.get("scene", {}).get(key, "")).strip():
            errors.append(f"scene.{key} is required")
    for key in ("description","accessories"):
        if not str(job.get("wardrobe", {}).get(key, "")).strip():
            errors.append(f"wardrobe.{key} is required")

    known = {item["id"] for item in anchors["anchors"]}
    selected = job.get("anchor_ids", [])
    if not isinstance(selected, list) or not 1 <= len(selected) <= 2:
        errors.append("anchor_ids must contain one or two values")
    else:
        for item in selected:
            if item not in known:
                errors.append(f"unknown anchor: {item}")

    all_text = " ".join(flatten_strings(job)).lower()
    forbidden = set(qc["automatic_fail_terms"])
    forbidden.update(identity["global_exclusions"])
    forbidden.discard("identity drift")
    for term in sorted(forbidden):
        if term.lower() in all_text:
            errors.append(f"forbidden identity term found: {term}")

    if errors:
        print("JOB VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("JOB VALIDATION PASSED")
    print(path.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
