# Datasets for Scientific Literature Understanding and Reasoning: A Survey <!-- omit in toc -->

> 面向科技文献的公开数据集综述。  
> 欢迎 PR 补充与修正（见下方贡献指南）。

<!-- [![Link Check](https://img.shields.io/github/actions/workflow/status/Stooooooop/awesome-science-datasets/link-check.yml?branch=main)](./.github/workflows/link-check.yml) -->
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## 目录
- [目录](#目录)
- [使用方法](#使用方法)
- [项目介绍](#项目介绍)
- [数据清单（结构化索引）](#数据清单结构化索引)
- [贡献指南](#贡献指南)
- [Datasets (Task + Links)](#datasets-task--links)

## 使用方法
- 所有条目的“权威地址（primary）”指向项目官方 GitHub 或主页；若有论文与镜像地址一并给出。
- 结构化索引见 `datasets.yaml`（或 `datasets.json`），便于二次开发与程序化检索。

## 项目介绍

本项目聚焦“科技文献理解与推理”数据集综述。面对文献激增与复杂推理需求，我们按四类系统梳理：光学层面理解、文本理解与推理、多模态理解与推理、预训练与对齐语料；概述各类数据集的动机、设计要点、组织方式与影响。结合大语言模型与多模态技术的迅速发展，呈现数据集演进脉络，帮助研究者高效选用资源，支撑 AI4S 中的自动理解、知识整合与创新研究。


## 数据清单（结构化索引）
> 结构化索引见 `datasets.yaml`；思维导图如下：

<p align="center">
  <img src="./assets/datasets_tree.svg" width="95%" alt="Mind map of datasets for scientific literature understanding" />
</p>

<!-- 
## 快速浏览（按类别）
>可在 `categories/` 下维护专题页。

### Summarization
- **WikiHow** — 抽象风格的多步说明文本；[GitHub](https://github.com/mahnazkoupaee/WikiHow-Dataset)
- **arXiv/PubMed** — 长文科学摘要生成；[Paper](https://aclanthology.org/N18-2097/)
- **SciSummNet** — 科学文献引用驱动摘要；[GitHub](https://github.com/WING-NUS/scisumm-corpus)

> 其余分类示例：`vision.md`, `biomedical.md` 等。 -->

## 贡献指南
见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

<!-- DATASETS_TABLE_START -->
## Datasets (Task + Links)

> 下表仅展示 **Task、Paper、GitHub** 三列；其余字段维护在 `datasets.yaml`。
> 说明：当前已隐藏 **Multi-Task Instruction, Pretraining** 类别（仍保留在 YAML 中）。

| Dataset | Task | Paper | GitHub |
| --- | --- | --- | --- |
| PubLayNet | Layout&OCR | [paper](https://arxiv.org/abs/1908.07836) | [github](https://ar5iv.labs.arxiv.org/html/1908.07836) |
| DocBank | Layout&OCR&Formula Recognition | [paper](https://doc-analysis.github.io/docbank-page/) | [github](https://github.com/doc-analysis/DocBank) |
| DocLayNet | Layout&OCR | [paper](https://arxiv.org/abs/2210.06155) | [github](https://github.com/DS4SD/DocLayNet) |
| OmniDocBench | Layout&OCR | [paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.pdf) | [github](https://github.com/opendatalab/OmniDocBench) |
| M6Doc | Layout&OCR | [paper](https://arxiv.org/abs/2305.08719) | [github](https://github.com/HCIILAB/M6Doc) |
| IBEM | Layout&OCR (Formula detection) | [paper](https://dl.acm.org/doi/10.1016/j.patrec.2023.05.033) | — |
| TabLeX | Table Recognition | [paper](https://arxiv.org/abs/2105.06400) | — |
| ICDAR 2021 DocVQA | Document VQA | [paper](https://arxiv.org/abs/2111.05547) | — |
| PRImA Layout Analysis | Layout&OCR | — | — |
| Nougat | Layout&OCR&Table/Formula Recognition | [paper](https://facebookresearch.github.io/nougat/) | [github](https://github.com/facebookresearch/nougat) |
| AceParse | Layout&OCR&Table/Formula Recognition | [paper](https://arxiv.org/abs/2402.18903) | — |
| TableBank | Table Recognition | [paper](https://aclanthology.org/2020.lrec-1.236/) | [github](https://github.com/doc-analysis/TableBank) |
| TabRecSet | Table Recognition (end-to-end) | [paper](https://www.researchgate.net/publication/368754251) | [github](https://github.com/MaxKinny/TabRecSet) |
| PubTables-1M | Table Recognition | [paper](https://openaccess.thecvf.com/content/CVPR2022/html/Smock_PubTables-1M_Towards_Comprehensive_Table_Extraction_From_Unstructured_Documents_CVPR_2022_paper.html) | [github](https://github.com/microsoft/table-transformer) |
| DECIMER.ai | Chemical Recognition | [paper](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00505-8) | [github](https://github.com/Kohulan/DECIMER-Image_Transformer) |
| CROHME | Formula Recognition (online HME) | — | — |
| HME100K | Formula Recognition (offline HME) | [paper](https://arxiv.org/pdf/2203.01601) | [github](https://github.com/Phymond/HME100K) |
| MathWriting | Formula Recognition (online/offline) | [paper](https://arxiv.org/abs/2404.10690) | [github](https://github.com/google-research/google-research/tree/master/mathwriting) |
| PEaCE | Chemical OCR | [paper](https://aclanthology.org/2024.lrec-main.1110.pdf) | [github](https://github.com/ZN1010/PEaCE) |
| DocVQA (WACV 2021 dataset) | Document VQA | [paper](https://openaccess.thecvf.com/content/WACV2021/papers/Mathew_DocVQA_A_Dataset_for_VQA_on_Document_Images_WACV_2021_paper.pdf) | — |
| GENIA | IE | — | — |
| BC5CDR | IE (Chem/Disease, relations) | [paper](https://biocreative.bioinformatics.udel.edu/media/store/files/2016/CDR_Task.pdf) | [github](https://github.com/JHnlp/BioCreative-V-CDR-Corpus) |
| NCBI Disease | IE (Disease) | — | — |
| CHEMDNER | IE (Chemical NER) | [paper](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-7-S1-S2) | — |
| BioRED | IE (Doc-level RE) | [paper](https://academic.oup.com/bib/article/23/5/bbac282/6645993) | — |
| SCITLDR | Summarization | — | [github](https://github.com/allenai/scitldr) |
| Multi-XScience | Summarization (multi-doc) | [paper](https://yaolu.github.io/upload/multixscience/Multi_XScience_Appendix.pdf) | [github](https://github.com/yaolu/Multi-XScience) |
| MS^2 | Summarization (multi-doc, biomedical) | [paper](https://arxiv.org/abs/2104.06486) | [github](https://github.com/allenai/ms2) |
| PubMedQA | QA (biomedical) | — | [github](https://github.com/pubmedqa/pubmedqa) |
| BioMRC | QA / MRC (biomedical) | [paper](https://arxiv.org/abs/2005.06376) | — |
| LitSearch | Retrieval benchmark | [paper](https://aclanthology.org/2024.emnlp-main.840.pdf) | [github](https://github.com/princeton-nlp/LitSearch) |
| SciMMIR | Image&Text Retrieval (scientific) | [paper](https://aclanthology.org/2024.findings-acl.746.pdf) | [github](https://github.com/Wusiwei0410/SciMMIR) |
<!-- DATASETS_TABLE_END -->

