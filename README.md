# Awesome Science Datasets & Benchmarks <!-- omit in toc -->

> 面向【你的综述主题】的公开数据集 / 基准与工具清单。专注高质量链接与最少噪音。  
> 欢迎 PR 补充与修正（见下方贡献指南）。

[![Link Check](https://img.shields.io/github/actions/workflow/status/<yourname>/awesome-science-datasets/link-check.yml?branch=main)](./.github/workflows/link-check.yml)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## 目录
- [目录](#目录)
- [使用方法](#使用方法)
- [数据清单（结构化索引）](#数据清单结构化索引)
- [快速浏览（按类别）](#快速浏览按类别)
  - [Summarization](#summarization)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 使用方法
- 所有条目的“权威地址（primary）”指向项目官方 GitHub 或主页；若有论文与镜像地址一并给出。
- 结构化索引见 `datasets.yaml`（或 `datasets.json`），便于二次开发与程序化检索。

## 数据清单（结构化索引）
- 统一字段：`name / task / domain / modality / url.primary / url.paper / url.home / license / size / notes`
- 完整示例：见 [`datasets.yaml`](./datasets.yaml)

## 快速浏览（按类别）
> 若喜欢人类可读的清单，可在 `categories/` 下维护专题页。

### Summarization
- **WikiHow** — 抽象风格的多步说明文本；[GitHub](https://github.com/mahnazkoupaee/WikiHow-Dataset)
- **arXiv/PubMed** — 长文科学摘要生成；[Paper](https://aclanthology.org/N18-2097/)
- **SciSummNet** — 科学文献引用驱动摘要；[GitHub](https://github.com/WING-NUS/scisumm-corpus)

> 其余分类示例：`vision.md`, `biomedical.md` 等。

## 贡献指南
见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

## 许可证
本清单与元数据：MIT（推荐）。  
外部链接各自遵循其原始许可证。
