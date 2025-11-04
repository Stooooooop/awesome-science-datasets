# -*- coding: utf-8 -*-
"""
Update README.md table from data/datasets_from_latex.csv
Python 3.8+ compatible
"""
import csv
import io
import os
import sys
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "datasets_from_latex.csv")
README_PATH = os.path.join(ROOT, "README.md")

START = "<!-- DATASETS_MATRIX_START -->"
END = "<!-- DATASETS_MATRIX_END -->"

# 列顺序（与 CSV 表头一致）
COLUMNS = [
    "name","release_year","modality","task","is_multi_doc",
    "is_only_eval","label_method","domain","size"
]

def load_csv(path):
    with io.open(path, "r", encoding="utf-8") as f:
        # 自动识别逗号内含逗号的字段
        reader = csv.DictReader(f)
        rows = []
        for r in reader:
            # 确保所有列都有
            row = {k: (r.get(k) or "").strip() for k in COLUMNS}
            rows.append(row)
        return rows

def esc_md(s):
    # 保护竖线，避免破坏 Markdown 表格
    return (s or "").replace("|", r"\|")

def build_table(rows):
    head = "| " + " | ".join(COLUMNS) + " |"
    sep = "|" + "|".join(["---"] * len(COLUMNS)) + "|"
    body_lines = []
    for r in rows:
        vals = [esc_md(r.get(c, "")) for c in COLUMNS]
        body_lines.append("| " + " | ".join(vals) + " |")
    table = "\n".join([head, sep] + body_lines)
    return table

def inject_table_into_readme(readme_text, table_md):
    block = (
        f"{START}\n"
        "## Full Dataset Matrix (from CSV)\n\n"
        "> 字段：`name, release_year, modality, task, is_multi_doc, is_only_eval, label_method, domain, size`\n\n"
        f"{table_md}\n"
        f"{END}"
    )
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        flags=re.DOTALL
    )
    if pattern.search(readme_text):
        return pattern.sub(block, readme_text)
    else:
        # 没有标记时，默认附加到 README 末尾
        return readme_text.rstrip() + "\n\n" + block + "\n"

def main():
    if not os.path.exists(CSV_PATH):
        print(f"[ERROR] CSV not found: {CSV_PATH}", file=sys.stderr)
        sys.exit(1)
    rows = load_csv(CSV_PATH)
    if not rows:
        print("[WARN] CSV has no rows; table will contain only header.")
    table_md = build_table(rows)
    with io.open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()
    updated = inject_table_into_readme(readme, table_md)
    if updated != readme:
        with io.open(README_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated)
        print("[OK] README.md updated from CSV.")
    else:
        print("[OK] README.md already up-to-date.")

if __name__ == "__main__":
    main()
