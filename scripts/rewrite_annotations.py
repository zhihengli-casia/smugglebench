from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rewrite SmuggleBench annotation paths to portable relative paths.")
    parser.add_argument("--annotations-root", type=Path, default=Path("annotations"))
    parser.add_argument("--images-prefix", default="images")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()
def rewrite_manifest(manifest_path: Path, images_prefix: str, dry_run: bool) -> bool:
    label = manifest_path.parent.name
    subcategory = manifest_path.parent.parent.name
    category = manifest_path.parent.parent.parent.name

    updated_lines: list[str] = []
    changed = False
    with manifest_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            filename = item.get("filename") or Path(item.get("image_path", "")).name
            portable_path = (Path(images_prefix) / category / subcategory / label / filename).as_posix()
            if item.get("image_path") != portable_path:
                item["image_path"] = portable_path
                changed = True
            updated_lines.append(json.dumps(item, ensure_ascii=False))

    if changed and not dry_run:
        manifest_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    args = parse_args()
    if not args.annotations_root.exists():
        raise SystemExit(f"Annotations root does not exist: {args.annotations_root}")

    changed_files = 0
    for manifest_path in sorted(args.annotations_root.rglob("*.jsonl")):
        if rewrite_manifest(manifest_path, args.images_prefix, args.dry_run):
            changed_files += 1
            print(f"updated {manifest_path}")

    print(f"done. changed files: {changed_files}")


if __name__ == "__main__":
    main()
