#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 datasets.yaml 生成 README 中的精简表格（Dataset | Task | Paper | GitHub）
- 支持按 Task / 名称过滤
- 兼容 Python 3.8+
"""
import re
import yaml
from pathlib import Path
from typing import Optional, Iterable

MARK_START = "<!-- DATASETS_TABLE_START -->"
MARK_END   = "<!-- DATASETS_TABLE_END -->"

# ===== 过滤规则（可按需修改）=====
EXCLUDE_TASKS = {
    "Pretraining",
    "Multi-Task Instruction",
}
EXCLUDE_DATASETS = set()
SHOW_ONLY_WITH_LINKS = False   # True=只展示有 paper 或 primary 链接的条目
# =================================

def _link(text: str, url: Optional[str]) -> str:
    if url and isinstance(url, str) and url.startswith(("http://", "https://")):
        return f"[{text}]({url})"
    return "—"

def build_table(items: Iterable[dict]) -> str:
    rows = []
    for it in items:
        name = it.get("name", "")
        task = it.get("task", "")
        url  = it.get("url", {}) or {}
        paper = url.get("paper")
        primary = url.get("primary")

        if task in EXCLUDE_TASKS:
            continue
        if name in EXCLUDE_DATASETS:
            continue
        if SHOW_ONLY_WITH_LINKS and not (paper or primary):
            continue

        rows.append((name or "—", task or "—", _link("paper", paper), _link("github", primary)))

    md = [
        "| Dataset | Task | Paper | GitHub |",
        "| --- | --- | --- | --- |",
    ]
    for ds, task, paper, gh in rows:
        md.append(f"| {ds} | {task} | {paper} | {gh} |")
    return "\n".join(md)

def main():
    root = Path(".")
    yml = root / "datasets.yaml"
    readme = root / "README.md"

    data = yaml.safe_load(yml.read_text(encoding="utf-8"))

    snippet = f"""{MARK_START}
## Datasets (Task + Links)

> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。
> 说明：当前已隐藏 **{', '.join(sorted(EXCLUDE_TASKS))}** 类别（仍保留在 YAML 中）。

{build_table(data)}
{MARK_END}
"""

    if not readme.exists():
        readme.write_text(f"# Awesome Science Datasets\n\n{snippet}\n", encoding="utf-8")
        print("README.md created with datasets table.")
        return

    content = readme.read_text(encoding="utf-8")
    if MARK_START in content and MARK_END in content:
        pattern = re.compile(re.escape(MARK_START) + r".*?" + re.escape(MARK_END), re.DOTALL)
        new_content = pattern.sub(snippet.strip(), content)
    else:
        new_content = content.rstrip() + "\n\n" + snippet + "\n"

    readme.write_text(new_content, encoding="utf-8")
    print("README.md updated with datasets table.")

if __name__ == "__main__":
    main()
