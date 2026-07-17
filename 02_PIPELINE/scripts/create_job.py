from __future__ import annotations

import argparse
import re
from datetime import date

from common import REPO_ROOT, load_json, write_json, write_text


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def next_number(today_code: str) -> int:
    highest = 0
    for path in (REPO_ROOT / "04_CONTENT" / "JOBS").glob("*/GENERATION_JOB.json"):
        try:
            job_id = load_json(path).get("job_id", "")
            if job_id.startswith(f"KAIA-{today_code}-"):
                highest = max(highest, int(job_id.rsplit("-", 1)[-1]))
        except Exception:
            continue
    return highest + 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Kaia content job.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--platform", default="instagram")
    parser.add_argument("--category", default="lifestyle")
    parser.add_argument("--aspect-ratio", default="9:16")
    parser.add_argument("--location", default="Miami waterfront")
    parser.add_argument("--time", default="early morning")
    parser.add_argument("--lighting", default="soft natural golden light")
    parser.add_argument("--action", default="walking naturally")
    parser.add_argument("--wardrobe", default="white fitted tank and relaxed linen trousers")
    parser.add_argument("--accessories", default="understated accessories")
    parser.add_argument("--hair", default="structured waves worn down")
    parser.add_argument("--expression", default="calm and self-possessed")
    parser.add_argument("--camera", default="iPhone 15 Pro RAW realism")
    args = parser.parse_args()

    slug = slugify(args.slug)
    if not slug:
        raise SystemExit("ERROR: invalid slug")

    folder = REPO_ROOT / "04_CONTENT" / "JOBS" / slug
    if folder.exists():
        raise SystemExit(f"ERROR: job already exists: {folder}")

    today_code = date.today().strftime("%Y%m%d")
    job = load_json(REPO_ROOT / "02_PIPELINE" / "TEMPLATES" / "GENERATION_JOB.template.json")
    job.update({
        "job_id": f"KAIA-{today_code}-{next_number(today_code):03d}",
        "status": "READY_FOR_PROMPT_ASSEMBLY",
        "platform": args.platform,
        "aspect_ratio": args.aspect_ratio,
        "content_category": args.category,
        "scene": {"location": args.location, "time": args.time, "lighting": args.lighting, "action": args.action},
        "wardrobe": {"description": args.wardrobe, "accessories": args.accessories},
        "hair_style": args.hair,
        "expression": args.expression,
        "camera_profile": args.camera
    })

    title = args.title or slug.replace("-", " ").title()
    brief = f"""# {title}\n\n## Objective\n\nCreate identity-consistent Kaia content for {args.platform}.\n\n## Scene\n\n- Location: {args.location}\n- Time: {args.time}\n- Lighting: {args.lighting}\n- Action: {args.action}\n\n## Styling\n\n- Wardrobe: {args.wardrobe}\n- Accessories: {args.accessories}\n- Hair: {args.hair}\n- Expression: {args.expression}\n\n## Technical\n\n- Category: {args.category}\n- Aspect ratio: {args.aspect_ratio}\n- Camera: {args.camera}\n\n## Identity rule\n\nThe scene and styling may change. Kaia's locked identity may not.\n"""

    qc = {
        "schema_version": "1.0.0",
        "job_id": job["job_id"],
        "asset_id": "",
        "identity_checks": {key: "PENDING" for key in ["face_match","eye_color","skin_tone","skin_texture","hair_color","hair_length","hair_density","beauty_mark","no_freckles","body_proportions"]},
        "conditional_checks": {"left_thumb_ring": "NOT_VISIBLE", "hand_anatomy": "NOT_VISIBLE"},
        "overall_result": "PENDING",
        "manual_approval": "PENDING",
        "failure_reasons": []
    }

    write_json(folder / "GENERATION_JOB.json", job)
    write_text(folder / "CONTENT_BRIEF.md", brief)
    write_json(folder / "QC_REPORT.json", qc)
    print(f"CREATED: {folder.relative_to(REPO_ROOT)}")
    print(f"JOB ID: {job['job_id']}")


if __name__ == "__main__":
    main()
