#!/usr/bin/env python3
import io, sys, re, yaml, pandas as pd
from pathlib import Path

MARK_START = "<!-- DATASETS_TABLE_START -->"
MARK_END = "<!-- DATASETS_TABLE_END -->"

def build_table(data):
    rows = []
    for item in data:
        name = item.get("name","")
        task = item.get("task","")
        url = item.get("url",{}) or {}
        paper = url.get("paper") or ""
        github = url.get("primary") or ""
        rows.append({"Dataset": name, "Task": task, "Paper": paper, "GitHub": github})
    df = pd.DataFrame(rows, columns=["Dataset","Task","Paper","GitHub"])
    md = []
    md.append("| Dataset | Task | Paper | GitHub |")
    md.append("| --- | --- | --- | --- |")
    for _, r in df.iterrows():
        def linkify(text, url):
            if url and isinstance(url, str) and url.startswith(("http://","https://")):
                return f"[{text}]({url})"
            return "—"
        ds = r["Dataset"] or "—"
        task = r["Task"] or "—"
        paper = linkify("paper", r["Paper"])
        gh = linkify("github", r["GitHub"])
        md.append(f"| {ds} | {task} | {paper} | {gh} |")
    return "\n".join(md)

def main():
    root = Path(".")
    yaml_path = root / "datasets.yaml"
    if not yaml_path.exists():
        print("datasets.yaml not found", file=sys.stderr)
        sys.exit(1)
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

    snippet = f"""{MARK_START}
## Datasets (Task + Links)

> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。

{build_table(data)}
{MARK_END}
"""
    readme = root / "README.md"
    if not readme.exists():
        # create a minimal README with markers
        readme.write_text(f"# Awesome Science Datasets\n\n{snippet}\n", encoding="utf-8")
        print("README.md created with datasets table.")
        return

    content = readme.read_text(encoding="utf-8")
    if MARK_START in content and MARK_END in content:
        # replace between markers
        pattern = re.compile(re.escape(MARK_START) + r".*?" + re.escape(MARK_END), re.DOTALL)
        new_content = pattern.sub(snippet.strip(), content)
    else:
        # append at end
        new_content = content.rstrip() + "\n\n" + snippet + "\n"
    readme.write_text(new_content, encoding="utf-8")
    print("README.md updated with datasets table.")

if __name__ == "__main__":
    main()
