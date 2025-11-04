# -*- coding: utf-8 -*-
import csv, io, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "datasets_from_latex.csv")
README_PATH = os.path.join(ROOT, "README.md")
START, END = "<!-- DATASETS_MATRIX_START -->", "<!-- DATASETS_MATRIX_END -->"

COLUMNS = ["name","release_year","modality","task",
           "is_multi_doc","is_only_eval","label_method","domain","size"]

def esc(s): return (s or "").replace("|", r"\|")
def load_rows():
    if not os.path.exists(CSV_PATH):
        print(f"[ERROR] missing {CSV_PATH}", file=sys.stderr); sys.exit(1)
    with io.open(CSV_PATH, "r", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        return [{c: (r.get(c) or "").strip() for c in COLUMNS} for r in rdr]

def build_table(rows):
    head = "| " + " | ".join(COLUMNS) + " |"
    sep  = "|" + "|".join(["---"] * len(COLUMNS)) + "|"
    body = ["| " + " | ".join(esc(r[c]) for c in COLUMNS) + " |" for r in rows]
    return "\n".join([head, sep] + body)

def inject(md, table):
    block = (f"{START}\n## 完整的数据集表格 (from CSV)\n\n"
             "> 字段：`name, release_year, modality, task, is_multi_doc, is_only_eval, label_method, domain, size`\n\n"
             f"{table}\n{END}")
    pat = re.compile(re.escape(START)+r".*?"+re.escape(END), re.DOTALL)
    return pat.sub(block, md) if pat.search(md) else md.rstrip()+"\n\n"+block+"\n"

def main():
    rows = load_rows()
    table = build_table(rows)
    with io.open(README_PATH, "r", encoding="utf-8") as f: md = f.read()
    new = inject(md, table)
    if new != md:
        with io.open(README_PATH, "w", encoding="utf-8", newline="\n") as f: f.write(new)
        print("[OK] README updated.")
    else:
        print("[OK] README already up-to-date.")

if __name__ == "__main__": main()
