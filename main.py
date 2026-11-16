#!/usr/bin/env python3
"""Validate common Progressive Web App manifest fields."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse


DISPLAY_MODES = {"fullscreen", "standalone", "minimal-ui", "browser"}


def lint(manifest):
    if not isinstance(manifest, dict):
        raise ValueError("manifest root must be a JSON object")
    issues = []
    if not (manifest.get("name") or manifest.get("short_name")):
        issues.append(("error", "provide name or short_name"))
    if not manifest.get("start_url"):
        issues.append(("warning", "start_url is missing; browsers may use a default"))
    display = manifest.get("display")
    if display and display not in DISPLAY_MODES:
        issues.append(("error", f"unsupported display mode: {display}"))
    icons = manifest.get("icons", [])
    if not isinstance(icons, list):
        issues.append(("error", "icons must be an array"))
        icons = []
    for index, icon in enumerate(icons):
        if not isinstance(icon, dict):
            issues.append(("error", f"icons[{index}] must be an object"))
            continue
        if not icon.get("src"):
            issues.append(("error", f"icons[{index}] is missing src"))
        sizes = icon.get("sizes")
        if sizes and sizes != "any":
            for size in sizes.split():
                if not re.fullmatch(r"\d+x\d+", size):
                    issues.append(("warning", f"icons[{index}] has an invalid size: {size}"))
    start = manifest.get("start_url")
    scope = manifest.get("scope")
    for field, value in (("start_url", start), ("scope", scope)):
        if value:
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc:
                issues.append(("warning", f"{field} is absolute; verify it matches the deployed origin"))
    if start and scope:
        start_path = urlparse(urljoin("/", start)).path
        scope_path = urlparse(urljoin("/", scope)).path
        if not start_path.startswith(scope_path):
            issues.append(("error", "start_url is outside the declared scope path"))
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="path to manifest.webmanifest or JSON file")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        issues = lint(manifest)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps([{"severity": s, "message": m} for s, m in issues], indent=2))
    elif not issues:
        print("Manifest looks good.")
    else:
        for severity, message in issues:
            print(f"{severity}: {message}")
    return 1 if any(s == "error" for s, _ in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
