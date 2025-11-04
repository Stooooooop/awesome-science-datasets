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

## Datasets (Task + Links)

> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。

| Dataset | Task | Paper | GitHub |
| --- | --- | --- | --- |
| WikiHow | summarization | [paper](https://arxiv.org/abs/1810.09305) | [github](https://github.com/mahnazkoupaee/WikiHow-Dataset) |
| arXiv/PubMed | summarization | [paper](https://aclanthology.org/N18-2097/) | — |
| SciSummNet | summarization | [paper](https://aclanthology.org/W19-8660/) | [github](https://github.com/WING-NUS/scisumm-corpus) |


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


<<<<<<< HEAD
> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。

| Dataset | Task | Paper | GitHub |
| --- | --- | --- | --- |
| PubLayNet | Layout&OCR | — | — |
| DocBank | Layout&OCR&Formula Recognition | — | — |
| DocLayNet | Layout&OCR | — | — |
| OmniDocBench | Layout&OCR | — | — |
| M6Doc | Layout&OCR | — | — |
| IBEM | Layout&OCR | — | — |
| TabLeX | Layout&OCR | — | — |
| ICDAR 2021 | Layout&OCR | — | — |
| PRImA | Layout&OCR | — | — |
| Nougat | Layout&OCR&Table/Formula Recognition | — | — |
| AceParse | Layout&OCR&Table/Formula Recognition | — | — |
| TableBank | Table Recognition | — | — |
| TabRecSet | Table Recognition | — | — |
| PubTables-1M | Table Recognition | — | — |
| ChemTable | Table Recognition | — | — |
| Nougat For Formula | Formula Recognition | — | — |
| CROHME | Formula Recognition | — | — |
| HME100K | Formula Recognition | — | — |
| MathWriting | Formula Recognition | — | — |
| PEaCE | Chemical Recognition | — | — |
| DECIMER.ai | Chemical Recognition | — | — |
| MoIScribe | Chemical Recognition | — | — |
| ReactionDataExtractor | Chemical Recognition | — | — |
| S2abEL | Information Extraction | — | — |
| Wiki-TabNER | Information Extraction | — | — |
| AxCell | Information Extraction | — | — |
| Symlink | Information Extraction | — | — |
| SymDef | Information Extraction | — | — |
| GENIA | IE | — | — |
| BC2GM | IE | — | — |
| NCBI Disease | IE | — | — |
| CHEMDNER | IE | — | — |
| BC5CDR | IE | — | — |
| BioRED | IE | — | — |
| SCITLDR | Summarization | — | — |
| WikiHow | Summarization | — | — |
| PubMed Summarization | Summarization | — | — |
| FacetSum | Summarization | — | — |
| CS-PaperSum | Summarization | — | — |
| Multi-XScience | Summarization | — | — |
| MS² | Summarization | — | — |
| BigSurvey | Summarization | — | — |
| SURVEYSUM | Summarization | — | — |
| LEGOBench | Summarization | — | — |
| SciCap+ | Captioning | — | — |
| MMSci | Captioning | — | — |
| ArXivCap | Captioning | — | — |
| ACL-FIG | Classification | — | — |
| LitSearch | Retrieval | — | — |
| SciMMIR | Retrieval | — | — |
| ARQMath | QA | — | — |
| SciTSR | QA | — | — |
| PubTabNet | QA | — | — |
| TableVQA-Bench | QA | — | — |
| DocVQA | QA | — | — |
| PlotQA | QA | — | — |
| ChartQA | QA | — | — |
| OpenCQA | QA | — | — |
| SciGraphQA | QA | — | — |
| CharXiv | QA | — | — |
| ChartLlama | QA | — | — |
| SimChart9K | QA | — | — |
| ReachQA | QA | — | — |
| ECD | QA | — | — |
| ChartBench | QA | — | — |
| ChartX | QA | — | — |
| MMC | QA | — | — |
| BioRead | QA | — | — |
| PubMedQA | QA | — | — |
| BioMRC | QA | — | — |
| ScholarlyRead | QA | — | — |
| ChemLLMBench | QA | — | — |
| ScholarChemQA | QA | — | — |
| QASPER | QA | — | — |
| QASA | QA | — | — |
| LitQA | QA | — | — |
| SCIBENCH | QA | — | — |
| SciEval | QA | — | — |
| ScholarQABench | QA | — | — |
| SCIDQA | QA | — | — |
| SciQAG-24D | QA | — | — |
| Xiezhi | QA | — | — |
| SciKnowEval | QA | — | — |
| PeerQA | QA | — | — |
| COVID-QA | QA | — | — |
| BioASQ-TaskB | QA | — | — |
| SciFIBench | QA | — | — |
| SCI-CQA | QA | — | — |
| ArXivQA | QA | — | — |
| LLM4Mat-Bench | QA | — | — |
| SPIQA | QA | — | — |
| SciAssess | QA | — | — |
| MMMU | QA | — | — |
| LAB-Bench | QA | — | — |
| MMCR | QA | — | — |
| arXiv | Pretraining | — | — |
| S2ORC | Pretraining | — | — |
| PubMed Central | Pretraining | — | — |
| PubMed | Pretraining | — | — |
| CSL | Pretraining | — | — |
| The Pile | Pretraining | — | — |
| RedPajama | Pretraining | — | — |
| Dolma | Pretraining | — | — |
| CORD-19 | Pretraining | — | — |
| SciInstruct | Multi-Task Instruction | — | — |
| SciRIFF | Multi-Task Instruction | — | — |
| SMoIlnstruct | Multi-Task Instruction | — | — |
| HoneyBee | Multi-Task Instruction | — | — |
| IDL | Multi-Task Instruction | — | — |
<!-- DATASETS_TABLE_END -->
=======
>>>>>>> 291574f (更新数据清单)

