#!/usr/bin/env python3
"""
Checks every design spec in this repo against the template in README.md.

README.md is the source of truth: this script re-derives the required
section order, Constraints subsection order, and table headers straight
from it, so updating the template doesn't require updating this script.

Specs are any .md files under specs/, in any subfolder (e.g.
specs/Client Q3 2026/Feature-Spec.md).

Usage:
    python3 scripts/check_specs.py            # check all specs under specs/
    python3 scripts/check_specs.py file1.md    # check specific files

Exit code 0 if every spec matches the template, 1 otherwise.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
SPECS_ROOT = REPO_ROOT / "specs"

HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")
TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")
CHECKBOX_BULLET_RE = re.compile(r"^\s*-\s*\[[ xX]\]\s")
PLAIN_BULLET_RE = re.compile(r"^\s*-\s+(?!\[)")


def split_cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def find_section(lines, heading_text, level_prefix):
    """Return (start, end) line indices (exclusive end) for a heading's body,
    where body runs until the next heading of the same or higher level."""
    start = None
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m and m.group(1) == level_prefix and m.group(2) == heading_text:
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for i in range(start, len(lines)):
        m = HEADING_RE.match(lines[i])
        if m and len(m.group(1)) <= len(level_prefix):
            end = i
            break
    return start, end


def extract_tables(lines, start, end):
    """Within lines[start:end], return a list of tables, each a list of rows
    (each row a list of cell strings), including the header and alignment row."""
    tables = []
    current = []
    for i in range(start, end):
        if TABLE_ROW_RE.match(lines[i]):
            current.append(split_cells(lines[i]))
        else:
            if current:
                tables.append(current)
                current = []
    if current:
        tables.append(current)
    return tables


def headings_at(lines, level_prefix, start=0, end=None):
    end = len(lines) if end is None else end
    out = []
    for i in range(start, end):
        m = HEADING_RE.match(lines[i])
        if m and m.group(1) == level_prefix:
            out.append(m.group(2))
    return out


class Template:
    def __init__(self, readme_lines):
        tpl = find_section(readme_lines, "Template", "##")
        assert tpl, "Could not find '## Template' in README.md"
        self.start, self.end = tpl

        all_sections = headings_at(readme_lines, "###", self.start, self.end)
        self.required_sections = [s for s in all_sections if s != "Project Title"]

        pt = find_section(readme_lines, "Project Title", "###")
        tables = extract_tables(readme_lines, pt[0], pt[1])
        self.title_table_1_header = tables[0][0]
        self.title_table_1_fields = [row[0] for row in tables[0][2:]]
        self.title_table_2_header = tables[1][0]
        self.title_table_2_fields = [row[0] for row in tables[1][2:]]

        aud = find_section(readme_lines, "Audience", "###")
        aud_tables = extract_tables(readme_lines, aud[0], aud[1])
        self.audience_header = aud_tables[0][0]

        cons = find_section(readme_lines, "Constraints", "###")
        sub = headings_at(readme_lines, "####", cons[0], cons[1])
        self.constraints_order = [h for h in sub if h != "Category"]


def check_spec(path, tmpl):
    errors = []
    lines = path.read_text(encoding="utf-8").splitlines()

    # Required section order (## headings, minus the first title heading)
    sections = headings_at(lines, "##")
    if sections and sections[0] not in tmpl.required_sections:
        sections = sections[1:]  # drop the doc's own title heading
    if sections != tmpl.required_sections:
        errors.append(
            "Section order/presence mismatch.\n"
            f"    expected: {tmpl.required_sections}\n"
            f"    found:    {sections}"
        )

    # Project Title: first two tables in the doc, before Problem Statement
    ps = find_section(lines, "Problem Statement", "##")
    pre_end = ps[0] - 1 if ps else len(lines)
    pre_tables = extract_tables(lines, 0, pre_end)
    if len(pre_tables) < 2:
        errors.append(f"Expected 2 title tables before Problem Statement, found {len(pre_tables)}.")
    else:
        t1, t2 = pre_tables[0], pre_tables[1]
        if t1[0] != tmpl.title_table_1_header:
            errors.append(f"Title table 1 header is {t1[0]}, expected {tmpl.title_table_1_header}.")
        fields1 = [row[0] for row in t1[2:]]
        if fields1 != tmpl.title_table_1_fields:
            errors.append(
                "Title table 1 field order/presence mismatch.\n"
                f"    expected: {tmpl.title_table_1_fields}\n"
                f"    found:    {fields1}"
            )
        if t2[0] != tmpl.title_table_2_header:
            errors.append(f"Title table 2 header is {t2[0]}, expected {tmpl.title_table_2_header}.")
        fields2 = [row[0] for row in t2[2:]]
        if fields2 != tmpl.title_table_2_fields:
            errors.append(
                "Title table 2 field order/presence mismatch.\n"
                f"    expected: {tmpl.title_table_2_fields}\n"
                f"    found:    {fields2}"
            )

    # Audience table header
    aud = find_section(lines, "Audience", "##")
    if aud:
        aud_tables = extract_tables(lines, aud[0], aud[1])
        if aud_tables and aud_tables[0][0] != tmpl.audience_header:
            errors.append(f"Audience table header is {aud_tables[0][0]}, expected {tmpl.audience_header}.")

    # Constraints subsection order + checkbox syntax
    cons = find_section(lines, "Constraints", "##")
    if cons:
        sub = headings_at(lines, "####", cons[0], cons[1])
        if sub != tmpl.constraints_order:
            errors.append(
                "Constraints subsection order/presence mismatch.\n"
                f"    expected: {tmpl.constraints_order}\n"
                f"    found:    {sub}"
            )
        for i in range(cons[0], cons[1]):
            line = lines[i]
            if PLAIN_BULLET_RE.match(line) and not CHECKBOX_BULLET_RE.match(line):
                errors.append(f"Line {i + 1}: Constraints bullet missing checkbox syntax: {line.strip()!r}")

    # Every table in the doc should use left-align markers, not bare dashes
    for i, line in enumerate(lines):
        if re.match(r"^\s*\|[\s:|-]+\|\s*$", line) and "-" in line:
            if ":" not in line:
                errors.append(f"Line {i + 1}: table separator row not left-aligned (use ':----' not '----'): {line.strip()!r}")

    return errors


def main(argv):
    readme_lines = README.read_text(encoding="utf-8").splitlines()
    tmpl = Template(readme_lines)

    if argv:
        paths = [Path(p) for p in argv]
    else:
        paths = sorted(SPECS_ROOT.rglob("*.md"))

    ok = True
    for path in paths:
        errors = check_spec(path, tmpl)
        try:
            rel = path.resolve().relative_to(REPO_ROOT)
        except ValueError:
            rel = path
        if errors:
            ok = False
            print(f"\n✗ {rel}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"✓ {rel}")

    if not ok:
        print("\nSpecs don't match README.md's template. Fix the mismatches above.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
