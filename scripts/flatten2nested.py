#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 datasets.yaml 中的扁平 URL 字段（paper_url / code_url / homepage_url）
统一迁移到嵌套结构：
  url:
    paper:   ...
    primary: ...
    home:    ...
并清理旧字段；兼容根元素为 list 或单个 dict 的情况。
会生成备份文件 datasets.yaml.bak
"""

from pathlib import Path
import sys, shutil, yaml

YAML_PATH = Path("datasets.yaml")
BACKUP_PATH = Path("datasets.yaml.bak")

def http_ok(x):
    return isinstance(x, str) and x.startswith(("http://", "https://"))

def normalize_item(it: dict) -> dict:
    # 可能存在旧字段
    paper_url = it.pop("paper_url", None)
    code_url  = it.pop("code_url", None)
    home_url  = it.pop("homepage_url", None)
    # notes 统一
    if "note" in it and "notes" not in it:
        it["notes"] = it.pop("note")

    # 嵌套 url 字段
    url = dict(it.get("url") or {})
    # 优先级：已有嵌套保留，扁平字段作为补充
    if http_ok(paper_url) and not http_ok(url.get("paper")):
        url["paper"] = paper_url
    if http_ok(code_url) and not http_ok(url.get("primary")):
        url["primary"] = code_url
    # 没有 primary 时用 home 占位
    if not http_ok(url.get("primary")):
        if http_ok(home_url) and not http_ok(url.get("home")):
            url["home"] = home_url
        elif http_ok(url.get("home")):
            pass
        elif http_ok(paper_url):
            # 有些项目只有论文主页，可不设 primary
            pass

    # 为空就不写 url；否则写回
    if any(http_ok(v) for v in url.values()):
        it["url"] = {k: v for k, v in url.items() if http_ok(v)}
    else:
        it.pop("url", None)

    return it

def main():
    if not YAML_PATH.exists():
        print("datasets.yaml 不存在", file=sys.stderr)
        sys.exit(1)

    # 备份
    shutil.copy2(YAML_PATH, BACKUP_PATH)

    data = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    # 允许顶层是 dict 或 list
    if isinstance(data, dict):
        items = [data]
        root_is_list = False
    elif isinstance(data, list):
        items = data
        root_is_list = True
    else:
        print("datasets.yaml 顶层应为 list 或 dict", file=sys.stderr)
        sys.exit(2)

    new_items = [normalize_item(dict(it)) for it in items]

    # 保持原有结构（一般是 list）
    out_data = new_items if root_is_list else new_items[0]
    YAML_PATH.write_text(yaml.dump(out_data, allow_unicode=True, sort_keys=False), encoding="utf-8")

    print("完成：已将扁平 URL 字段迁移为嵌套结构。备份文件：datasets.yaml.bak")

if __name__ == "__main__":
    main()
