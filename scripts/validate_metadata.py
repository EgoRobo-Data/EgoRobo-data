import argparse
import json
import sys

REQUIRED_FIELDS = [
    "session_id",
    "task_id",
    "subject_id",
    "env_id",
    "camera_type",
    "fps",
    "resolution",
    "duration_sec",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to session metadata JSON")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    missing = [k for k in REQUIRED_FIELDS if k not in data]
    if missing:
        print("Missing required fields:", ", ".join(missing))
        sys.exit(1)

    print("Metadata validation passed.")


if __name__ == "__main__":
    main()
