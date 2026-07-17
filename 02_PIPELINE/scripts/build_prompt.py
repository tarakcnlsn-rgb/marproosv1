from __future__ import annotations

import argparse

from common import REPO_ROOT, load_json, resolve_repo_path, write_json, write_text


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a final Kaia image prompt.")
    parser.add_argument("job_path")
    args = parser.parse_args()

    job_path = resolve_repo_path(args.job_path)
    job = load_json(job_path)
    identity = load_json(REPO_ROOT / "01_IDENTITY" / "IDENTITY_KERNEL.json")
    registry = load_json(REPO_ROOT / "01_IDENTITY" / "ANCHOR_REGISTRY.json")
    anchor_lookup = {item["id"]: item for item in registry["anchors"]}
    selected = [anchor_lookup[item] for item in job["anchor_ids"]]

    exclusions = list(identity["global_exclusions"])
    for group in ("eyes","skin","hair"):
        exclusions.extend(identity[group].get("forbidden", []))
    exclusions.extend(identity["body"].get("forbidden", []))
    exclusions.extend(identity["hands"].get("forbidden", []))
    exclusions = list(dict.fromkeys(exclusions))

    anchor_lines = "\n".join(f"- {item['id']}: {item['role']} (recommended weight {item['default_weight']})" for item in selected)
    scene = job["scene"]
    wardrobe = job["wardrobe"]

    prompt = f"""# Final Kaia Generation Prompt\n\n## Character Identity\n\nCreate a photorealistic image of {identity['public_name']}, age {identity['age']}, preserving the exact recognizable face identity from the approved Kaia anchor.\n\n- Eyes: {identity['eyes']['color']}\n- Skin: {identity['skin']['tone']} with a {identity['skin']['undertone']} undertone; {identity['skin']['texture']}\n- Hair: {identity['hair']['length']}, {identity['hair']['density']}, {identity['hair']['base_color']} with {identity['hair']['highlight_color']}; {identity['hair']['ends']}\n- Body: {identity['body']['frame']}; {identity['body']['build']}; {identity['body']['proportions']}\n- Beauty mark: exactly one, {identity['face']['beauty_mark']['location']}\n- Hands: {identity['hands']['manicure']}; silver band on the left thumb whenever visible\n\n## Current Shoot\n\n- Platform: {job['platform']}\n- Aspect ratio: {job['aspect_ratio']}\n- Category: {job['content_category']}\n- Location: {scene['location']}\n- Time: {scene['time']}\n- Lighting: {scene['lighting']}\n- Action: {scene['action']}\n- Wardrobe: {wardrobe['description']}\n- Accessories: {wardrobe['accessories']}\n- Hair styling: {job['hair_style']}\n- Expression: {job['expression']}\n- Camera: {job['camera_profile']}\n\n## Approved Reference Strategy\n\n{anchor_lines}\n\n## Negative Constraints\n\nDo not generate: {'; '.join(exclusions)}.\n\n## Output Requirement\n\nPreserve Kaia's exact identity. The scene and styling may vary. Locked identity may not change.\n"""

    output = job_path.parent / "FINAL_PROMPT.md"
    write_text(output, prompt)
    job["status"] = "PROMPT_READY"
    write_json(job_path, job)
    print(f"PROMPT BUILT: {output.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
