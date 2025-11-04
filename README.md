# Awesome Science Datasets & Benchmarks <!-- omit in toc -->

> 面向科技文献的公开数据集列表。  
> 欢迎 PR 补充与修正（见下方贡献指南）。

[![Link Check](https://img.shields.io/github/actions/workflow/status/<yourname>/awesome-science-datasets/link-check.yml?branch=main)](./.github/workflows/link-check.yml)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## 目录
- [目录](#目录)
- [使用方法](#使用方法)
- [Datasets (Task + Links)](#datasets-task--links)
- [数据清单（结构化索引）](#数据清单结构化索引)
- [快速浏览（按类别）](#快速浏览按类别)
  - [Summarization](#summarization)
- [贡献指南](#贡献指南)

## 使用方法
- 所有条目的“权威地址（primary）”指向项目官方 GitHub 或主页；若有论文与镜像地址一并给出。
- 结构化索引见 `datasets.yaml`（或 `datasets.json`），便于二次开发与程序化检索。

<!-- ## Datasets (CSV Viewer)
参见：[datasets_from_latex.csv](./data/datasets_from_latex.csv)  
> 点击链接后，GitHub 会以可滚动表格展示 CSV。 -->


## Datasets (Task + Links)

> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。请在 `datasets.yaml` 的 `url.paper` 与 `url.primary` 补齐官方链接后，表格会自动更新。

| Dataset | Task | Paper | GitHub |
| --- | --- | --- | --- |
| …自动生成… |



## 数据清单（结构化索引）
- 统一字段：`name / task / domain / modality / url.primary / url.paper / url.home / license / size / notes`
- 完整示例：见 [`datasets.yaml`](./datasets.yaml)

## 快速浏览（按类别）
>可在 `categories/` 下维护专题页。

### Summarization
- **WikiHow** — 抽象风格的多步说明文本；[GitHub](https://github.com/mahnazkoupaee/WikiHow-Dataset)
- **arXiv/PubMed** — 长文科学摘要生成；[Paper](https://aclanthology.org/N18-2097/)
- **SciSummNet** — 科学文献引用驱动摘要；[GitHub](https://github.com/WING-NUS/scisumm-corpus)

> 其余分类示例：`vision.md`, `biomedical.md` 等。

## 贡献指南
见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

<!-- DATASETS_TABLE_START -->
## Datasets (Task + Links)

> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。

| Dataset | Task | Paper | GitHub |
| --- | --- | --- | --- |
| WikiHow | summarization | [paper](https://arxiv.org/abs/1810.09305) | [github](https://github.com/mahnazkoupaee/WikiHow-Dataset) |
| arXiv/PubMed | summarization | [paper](https://aclanthology.org/N18-2097/) | — |
| SciSummNet | summarization | [paper](https://aclanthology.org/W19-8660/) | [github](https://github.com/WING-NUS/scisumm-corpus) |
<!-- DATASETS_TABLE_END -->

