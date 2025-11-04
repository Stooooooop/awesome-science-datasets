#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 datasets.yaml 生成 README 中的精简表格（Dataset | Task | Paper | GitHub）
- 支持按 Task / 按数据集名称过滤（排除或仅保留）
- 仅在 README 的标记之间替换内容
"""

import re, yaml, pandas as pd
from pathlib import Path
from typing import Iterable

MARK_START = "<!-- DATASETS_TABLE_START -->"
MARK_END   = "<!-- DATASETS_TABLE_END -->"

# ===== 可配置过滤规则 =====
# 1) 不想在 README 表格展示的 Task（仍在 datasets.yaml 中保留）
EXCLUDE_TASKS: set[str] = {
    "Pretraining",
    "Multi-Task Instruction",
}

# 2) 如需按名字排除（可选）
EXCLUDE_DATASETS: set[str] = set()

# 3) 仅展示“有链接”的条目（paper 或 primary 有一个即可）。不需要就设为 False
SHOW_ONLY_WITH_LINKS = False
# =======================

def _link(text: str, url: str | None) -> str:
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

        # 过滤逻辑
        if task in EXCLUDE_TASKS:               # 按 Task 排除
            continue
        if name in EXCLUDE_DATASETS:            # 按名称排除
            continue
        if SHOW_ONLY_WITH_LINKS and not (paper or primary):
            continue

        rows.append((name or "—", task or "—", _link("paper", paper), _link("github", primary)))

    # 生成 Markdown 表格
    md = ["| Dataset | Task | Paper | GitHub |",
          "| --- | --- | --- | --- |"]
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
