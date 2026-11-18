#!/usr/bin/env python3
"""Check upload copy locally; never upload, call APIs, or echo the note."""
import argparse
import json
from pathlib import Path
import re

URL = re.compile(r"https?://|www\.", re.IGNORECASE)

def validate_text(text):
    errors = []
    if not text.strip():
        errors.append("empty_upload_copy")
    if len(text) > 500:
        errors.append("upload_copy_over_500_characters")
    if URL.search(text):
        errors.append("external_url_in_upload_copy")
    return {"ok": not errors, "characters": len(text), "errors": errors,
            "scope": "text only; images, factual accuracy and platform review remain separate"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text_file", type=Path, help="UTF-8 upload copy only; exclude source manifests")
    args = parser.parse_args()
    result = validate_text(args.text_file.read_text(encoding="utf-8"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
