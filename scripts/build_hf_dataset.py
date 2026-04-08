from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".webp"}
PAPER_TAXONOMY = {
    ("Perception", "01_Miniature_Text"): ("Perceptual Blindness", "Tiny Text"),
    ("Perception", "02_Occlusion & Interference_text"): ("Perceptual Blindness", "Occluded Text"),
    ("Perception", "03_Handwritten_Text"): ("Perceptual Blindness", "Handwritten Style"),
    ("Perception", "04_Stylized & Composed_Text"): ("Perceptual Blindness", "Artistic/Distorted"),
    ("Perception", "05_Low_Contrast_Text"): ("Perceptual Blindness", "Low Contrast"),
    ("AIGC", "01_Blended_Background"): ("Perceptual Blindness", "AI Illusions"),
    ("AIGC", "02_Multi-Picture Camouflage"): ("Perceptual Blindness", "AI Illusions"),
    ("Reasoning", "01_Textual Steganography"): ("Reasoning Blockade", "Dense Text Masking"),
    ("Reasoning", "02_Contextual Camouflage"): ("Reasoning Blockade", "Semantic Camouflage"),
    ("Reasoning", "03_Cryptic Substitution"): ("Reasoning Blockade", "Visual Puzzles"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a Hugging Face-ready SmuggleBench dataset package.")
    parser.add_argument("--annotations-root", type=Path, default=Path("annotations"))
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--images-root", type=Path, help="Optional local image root for copying image files.")
    parser.add_argument("--split-name", default="test")
    parser.add_argument("--copy-images", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def iter_positive_rows(annotations_root: Path):
    for manifest in sorted(annotations_root.rglob("*.jsonl")):
        if "/positive/" not in manifest.as_posix():
            continue
        family = manifest.parent.parent.parent.name
        subcategory = manifest.parent.parent.name
        pathway, technique = PAPER_TAXONOMY[(family, subcategory)]
        with manifest.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                item = json.loads(line)
                filename = item["filename"]
                yield {
                    "file_name": f"{family}/{subcategory}/{filename}",
                    "family": family,
                    "subcategory": subcategory,
                    "pathway": pathway,
                    "paper_technique": technique,
                    "is_violating": True,
                    "ocr_text": item.get("ocr_text", ""),
                    "core_violation_items": item.get("core_violation_items", ""),
                    "_source_path": Path(item.get("image_path", "")),
                }


def source_image_path(images_root: Path, row: dict) -> Path:
    return images_root / row["family"] / row["subcategory"] / "positive" / Path(row["file_name"]).name


def main() -> None:
    args = parse_args()
    if not args.annotations_root.exists():
        raise SystemExit(f"Annotations root does not exist: {args.annotations_root}")
    if args.copy_images and not args.images_root:
        raise SystemExit("--images-root is required when --copy-images is set.")
    if args.copy_images and not args.images_root.exists():
        raise SystemExit(f"Images root does not exist: {args.images_root}")

    split_dir = args.output_root / args.split_name
    if split_dir.exists() and args.overwrite:
        shutil.rmtree(split_dir)
    split_dir.mkdir(parents=True, exist_ok=True)

    metadata_path = split_dir / "metadata.jsonl"
    count = 0
    with metadata_path.open("w", encoding="utf-8") as metadata_file:
        for row in iter_positive_rows(args.annotations_root):
            metadata_file.write(
                json.dumps(
                    {
                        "file_name": row["file_name"],
                        "family": row["family"],
                        "subcategory": row["subcategory"],
                        "pathway": row["pathway"],
                        "paper_technique": row["paper_technique"],
                        "is_violating": row["is_violating"],
                        "ocr_text": row["ocr_text"],
                        "core_violation_items": row["core_violation_items"],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

            if args.copy_images:
                src = source_image_path(args.images_root, row)
                if src.suffix.lower() not in IMAGE_EXTENSIONS:
                    raise SystemExit(f"Unsupported image extension: {src}")
                if not src.exists():
                    raise SystemExit(f"Missing image: {src}")
                dst = split_dir / row["file_name"]
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            count += 1

    print(f"Wrote {count} rows to {metadata_path}")
    if args.copy_images:
        print(f"Copied images into {split_dir}")


if __name__ == "__main__":
    main()
