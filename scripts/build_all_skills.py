#!/usr/bin/env python3
"""Build all skills in skills/ into packaged .skill files under dist/.

For each folder in skills/:
  - validates SKILL.md exists and has valid YAML frontmatter with `name` + `description`
  - zips the folder into dist/<folder-name>.skill
Prints a summary table at the end.

No external dependencies — uses only the Python standard library.
"""

import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
DIST_DIR = REPO_ROOT / "dist"


def parse_frontmatter(text):
    """Return the frontmatter block as a dict of top-level scalar keys.

    Minimal parser: handles a leading `---` ... `---` block with `key: value`
    pairs. Values may span multiple lines if continuation lines are indented.
    Good enough to validate `name` and `description` are present and non-empty.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None

    fields = {}
    current_key = None
    for raw in lines[1:end]:
        if raw and not raw[0].isspace() and ":" in raw:
            key, _, value = raw.partition(":")
            current_key = key.strip()
            fields[current_key] = value.strip()
        elif current_key is not None and raw.strip():
            # continuation of a multi-line value
            fields[current_key] = (fields[current_key] + " " + raw.strip()).strip()
    return fields


def validate_skill(skill_dir):
    """Validate a skill folder. Return (ok, message, line_count)."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return False, "missing SKILL.md", 0

    text = skill_md.read_text(encoding="utf-8")
    line_count = len(text.splitlines())

    fm = parse_frontmatter(text)
    if fm is None:
        return False, "invalid or missing YAML frontmatter", line_count
    if not fm.get("name"):
        return False, "frontmatter missing `name`", line_count
    if not fm.get("description"):
        return False, "frontmatter missing `description`", line_count
    if line_count > 500:
        return False, f"SKILL.md is {line_count} lines (limit 500)", line_count

    return True, "ok", line_count


def zip_skill(skill_dir, dest):
    """Zip every file in skill_dir into dest, paths prefixed with the folder name."""
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                arcname = Path(skill_dir.name) / path.relative_to(skill_dir)
                zf.write(path, arcname.as_posix())


def human_size(num_bytes):
    size = float(num_bytes)
    for unit in ("B", "KB", "MB"):
        if size < 1024 or unit == "MB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024


def main():
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: skills directory not found: {SKILLS_DIR}")
        return 1

    DIST_DIR.mkdir(exist_ok=True)

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skill_dirs:
        print(f"ERROR: no skill folders found in {SKILLS_DIR}")
        return 1

    rows = []
    failures = 0

    for skill_dir in skill_dirs:
        ok, message, line_count = validate_skill(skill_dir)
        if not ok:
            print(f"  FAIL  {skill_dir.name}: {message}")
            failures += 1
            rows.append((skill_dir.name, "—", line_count, f"FAIL: {message}"))
            continue

        dest = DIST_DIR / f"{skill_dir.name}.skill"
        zip_skill(skill_dir, dest)
        size = human_size(dest.stat().st_size)
        print(f"  OK    {skill_dir.name} -> dist/{dest.name} ({size})")
        rows.append((skill_dir.name, size, line_count, "built"))

    # Summary table
    name_w = max(len("Skill"), *(len(r[0]) for r in rows))
    print()
    print(f"  {'Skill':<{name_w}}  {'Size':>9}  {'Lines':>6}  Status")
    print(f"  {'-' * name_w}  {'-' * 9}  {'-' * 6}  {'-' * 16}")
    for name, size, lines, status in rows:
        print(f"  {name:<{name_w}}  {size:>9}  {lines:>6}  {status}")
    print()

    built = len(rows) - failures
    print(f"  {built} skill(s) packaged into dist/, {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
