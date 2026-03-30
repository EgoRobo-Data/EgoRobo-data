import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.root)
    files = []
    for p in root.rglob("*"):
        if p.is_file():
            files.append({
                "path": str(p.relative_to(root)),
                "suffix": p.suffix,
                "size_bytes": p.stat().st_size,
            })

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({"files": files}, f, ensure_ascii=False, indent=2)

    print(f"Dataset index written to {args.output}")


if __name__ == "__main__":
    main()
