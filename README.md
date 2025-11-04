# Datasets for Scientific Literature Understanding and Reasoning: A Survey <!-- omit in toc -->

> 面向科技文献的公开数据集综述。  
> 欢迎 PR 补充与修正（见下方贡献指南）。

<!-- [![Link Check](https://img.shields.io/github/actions/workflow/status/Stooooooop/awesome-science-datasets/link-check.yml?branch=main)](./.github/workflows/link-check.yml) -->
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/github/license/Stooooooop/awesome-science-datasets)](./LICENSE)
[![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-brightgreen)](./CONTRIBUTING.md)


## 目录
- [目录](#目录)
- [使用方法](#使用方法)
- [项目介绍](#项目介绍)
- [数据清单（结构化索引）](#数据清单结构化索引)
- [贡献指南](#贡献指南)
- [Datasets (Task + Links)](#datasets-task--links)

## 使用方法
- 指向数据集项目官方 GitHub 或主页；若有论文与镜像地址一并给出。
- 结构化索引见 `datasets.yaml`，便于二次开发与程序化检索。

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

<!-- DATASETS_MATRIX_START -->
## Full Dataset Matrix (from CSV)

> 字段：`name, release_year, modality, task, is_multi_doc, is_only_eval, label_method, domain, size`

| name | release_year | modality | task | is_multi_doc | is_only_eval | label_method | domain | size |
|---|---|---|---|---|---|---|---|---|
| PubLayNet | 2019 | Image&Text | Layout&OCR | No | No | Auto | Biomedical | 360k pages |
| DocBank | 2020 | Image&Text | Layout&OCR&Formula Recognition | No | No | Auto | Computer | 500k pages |
| DocLayNet | 2022 | Image&Text | Layout&OCR | No | No | Manual | Multi-domain | 80k pages |
| OmniDocBench | 2024 | Image&Text | Layout&OCR | No | No | Manual | Multi-domain | 981 pages |
| M6Doc | 2022 | Image&Text | Layout&OCR | No | No | Manual | Multi-domain | 237k instances |
| IBEM | 2022 | Image&Text | Layout&OCR | No | No | Manual | Multi-domain | - |
| TabLeX | 2020 | Image&Text | Layout&OCR | No | No | Auto | Scientific | - |
| ICDAR 2021 | 2021 | Image&Text | Layout&OCR | No | Yes | Manual | Scientific | - |
| PRImA | 2009 | Image&Text | Layout&OCR | No | No | Manual | Multi-domain | - |
| Nougat | 2023 | Image&Text | Layout&OCR&Table/Formula Recognition | No | No | Auto | - | - |
| AceParse | 2023 | Image&Text | Layout&OCR&Table/Formula Recognition | No | No | Auto | - | 500k parsed pairs |
| TableBank | 2020 | Image&Text | Table Recognition | No | No | Auto | Multi-domain | 417k tables |
| TabRecSet | 2023 | Image&Text | Table Recognition | No | No | Auto | Multi-domain | 38.1k tables |
| PubTables-1M | 2021 | Image&Text | Table Recognition | No | No | Auto | Scientific | 1M tables |
| ChemTable | 2025 | Image&Text | Table Recognition | No | No | Manual | Chemistry | - |
| Nougat For Formula | 2024 | Image&Text | Formula Recognition | No | No | Auto | Scientific | - |
| CROHME | 2023 | Image&Text | Formula Recognition | No | Yes | Manual | - | 11k images |
| HME100K | 2024 | Image&Text | Formula Recognition | No | No | Manual | - | 100k images |
| MathWriting | 2024 | Image&Text | Formula Recognition | No | No | Manual | - | 230k images |
| PEaCE | 2024 | Image&Text | Chemical Recognition | No | No | Manual | Chemistry | - |
| DECIMER.ai | 2023 | Image&Text | Chemical Recognition | No | No | Auto | Chemistry | - |
| MoIScribe | 2023 | Image&Text | Chemical Recognition | No | No | Manual | Chemistry | - |
| ReactionDataExtractor | 2023 | Image&Text | Chemical Recognition | No | No | Manual | Chemistry | - |
| S2abEL | 2023 | Text | Information Extraction | No | No | Manual | Biomedical | - |
| Wiki-TabNER | 2024 | Text | Information Extraction | No | No | Manual | - | - |
| AxCell | 2020 | Text | Information Extraction | No | No | Auto | - | - |
| Symlink | 2022 | Text | Information Extraction | No | No | Manual | - | - |
| SymDef | 2022 | Text | Information Extraction | No | No | Manual | - | - |
| GENIA | 2003 | Text | IE | No | No | Manual | Biomedical | - |
| BC2GM | 2008 | Text | IE | No | No | Manual | Biomedical | - |
| NCBI Disease | 2014 | Text | IE | No | No | Manual | Biomedical | 800 abstracts |
| CHEMDNER | 2015 | Text | IE | No | No | Manual | Biomedical | 10k abstracts |
| BC5CDR | 2016 | Text | IE | No | No | Manual | Biomedical | 1.5k abstracts |
| BioRED | 2022 | Text | IE | No | No | Manual | Biomedical | 600 abstracts |
| SCITLDR | 2020 | Text | Summarization | No | No | Manual | - | 5.4k full-text papers |
| WikiHow | 2018 | Text | Summarization | No | No | Manual | - | 230k articles |
| PubMed Summarization | 2018 | Text | Summarization | No | No | Auto | Biomedical | - |
| FacetSum | 2021 | Text | Summarization | No | No | Manual | - | 60k full-text papers |
| CS-PaperSum | 2025 | Text | Summarization | No | No | Auto | Computer Science | 91.9k full-text papers |
| Multi-XScience | 2020 | Text | Summarization | Yes | No | Auto | - | 30k instances |
| MS² | 2021 | Text | Summarization | Yes | No | Manual | Biomedical | 20k reviews |
| BigSurvey | 2022 | Text | Summarization | Yes | No | Auto | - | 7k full-text surveys |
| SURVEYSUM | 2024 | Text | Summarization | Yes | No | Manual | - | 79 sections |
| LEGOBench | 2023 | Text | Summarization | No | No | Auto | Scientific | - |
| SciCap+ | 2024 | Image&Text | Captioning | No | No | Manual | Scientific | - |
| MMSci | 2023 | Image&Text | Captioning | No | No | Manual | Scientific | - |
| ArXivCap | 2024 | Image&Text | Captioning | No | No | Auto | Scientific | 6.4M images & 3.9M captions |
| ACL-FIG | 2023 | Image | Classification | No | No | Manual | - | 112k figures |
| LitSearch | 2024 | Text | Retrieval | Yes | No | Manual | - | 597 queries |
| SciMMIR | 2024 | Image&Text | Retrieval | No | No | Manual&Auto | Scientific | 530k image-text pairs |
| ARQMath | 2020 | Text | QA | No | No | Manual | Math | - |
| SciTSR | 2019 | Table&Text | QA | No | No | Auto | - | - |
| PubTabNet | 2020 | Table&Text | QA | No | No | Auto | - | - |
| TableVQA-Bench | 2024 | Table&Text | QA | No | No | Auto | - | - |
| DocVQA | 2021 | Image&Text | QA | No | No | Manual | - | - |
| PlotQA | 2020 | Chart&Text | QA | No | No | Manual&Auto | - | 224k QA pairs |
| ChartQA | 2022 | Chart&Text | QA | No | No | Manual&Auto | - | 33k QA pairs |
| OpenCQA | 2022 | Chart&Text | QA | No | No | Manual | - | - |
| SciGraphQA | 2023 | Chart&Text | QA | No | No | Auto | - | 295k QA pairs |
| CharXiv |  | Chart&Text | QA | No | Yes | Manual | - | 2.3k QA pairs |
| ChartLlama | 2023 | Chart&Text | QA | No | No | Auto | - | - |
| SimChart9K | 2023 | Chart&Text | QA | No | No | Auto | - | 9k QA pairs |
| ReachQA | 2024 | Chart&Text | QA | No | No | Auto | - | - |
| ECD | 2025 | Chart&Text | QA | No | No | Auto | - | - |
| ChartBench | 2023 | Chart&Text | QA | No | Yes | Auto | - | 66.6k QA pairs |
| ChartX | 2024 | Chart&Text | QA | No | Yes | Manual | - | - |
| MMC | 2023 | Chart&Text | QA | No | No | Manual | - | - |
| BioRead | 2018 | Text | QA | No | No | Manual&Auto | Biomedical | 10k QA pairs |
| PubMedQA | 2019 | Text | QA | No | No | Manual&Auto | Biomedical | 273k QA pairs |
| BioMRC | 2020 | Text | QA | No | No | Auto | Biomedical | 1M QA pairs |
| ScholarlyRead | 2020 | Text | QA | No | No | Manual | - | 10k QA pairs |
| ChemLLMBench | 2023 | Text | QA | No | Yes | Manual | Chemistry | - |
| ScholarChemQA | 2025 | Text | QA | No | No | Manual&Auto | Chemistry | 40k QA pairs |
| QASPER | 2021 | Text | QA | Yes | No | Manual | NLP | 5k QA pairs |
| QASA | 2023 | Text | QA | Yes | No | Manual | - | 1.8k QA pairs |
| LitQA | 2023 | Text | QA | Yes | No | Manual | Biology | 50 QA pairs |
| SCIBENCH |  | Text | QA | No | Yes | Manual | - | - |
| SciEval | 2024 | Text | QA | No | Yes | Manual | - | 18k QA pairs |
| ScholarQABench | 2024 | Text | QA | Yes | Yes | Manual | - | 2.9k QA pairs |
| SCIDQA | 2024 | Text | QA | Yes | No | Manual | - | 2.9k QA pairs |
| SciQAG-24D | 2024 | Text | QA | Yes | No | Auto | - | 188k QA pairs |
| Xiezhi | 2024 | Text | QA | No | Yes | Manual | - | 249k QA pairs |
| SciKnowEval | 2024 | Text | QA | No | Yes | Manual | - | 70k QA pairs |
| PeerQA | 2025 | Text | QA | Yes | No | Manual | - | 579 QA pairs |
| COVID-QA | 2020 | Text | QA | Yes | No | Manual | COVID-19 | - |
| BioASQ-TaskB | 2013-2025 | Text | QA | Yes | No | Manual | Biomedical | - |
| SciFIBench | 2024 | Image&Text | QA | No | Yes | Manual | Scientific | 2k QA pairs |
| SCI-CQA | 2024 | Image&Text | QA | No | No | Manual | Scientific | 10k QA pairs |
| ArXivQA | 2024 | Image&Text | QA | No | No | Auto | Scientific | - |
| LLM4Mat-Bench | 2024 | Image&Text | QA | No | Yes | Auto | Materials Science | 1.97M samples |
| SPIQA | 2024 | Image&Text | QA | No | Yes | Manual | Scientific | - |
| SciAssess | 2024 | Text | QA | No | Yes | Manual | Scientific | 6,888 QA pairs |
| MMMU | 2023 | Image&Text | QA | No | No | Manual | - | 11.5k QA pairs |
| LAB-Bench | 2024 | Image&Text | QA | No | No | Manual | Biology | 2.4k |
| MMCR | 2025 | Image&Text | QA | No | No | Manual&Auto | Scientific | 310k |
| arXiv | 1991 | Text | Pretraining | No | No | Auto | Multi-domain | 2.6M full-text papers |
| S2ORC | 2020 | Text | Pretraining | No | No | Auto | Multi-domain | 81M full-text papers |
| PubMed Central | 2000 | Text | Pretraining | No | No | Auto | Biomedical | 10M full-text papers |
| PubMed | 1966 | Text | Pretraining | No | No | Auto | Biomedical | 35M paper metadata |
| CSL | 2022 | Text | Pretraining | No | No | Auto | Chinese | 396k paper metadata |
| The Pile | 2020 | Text | Pretraining | No | No | Auto | Multi-domain | 800GB raw text |
| RedPajama | 2024 | Text | Pretraining | No | No | Auto | General | - |
| Dolma | 2024 | Text | Pretraining | No | No | Auto | General | 3T tokens |
| CORD-19 | 2020 | Text | Pretraining | No | No | Auto | COVID-19 | 1M full-text papers |
| SciInstruct | 2024 | Text | Multi-Task Instruction | No | No | Manual | Scientific | 100k examples |
| SciRIFF |  | Text | Multi-Task Instruction | No | No | Manual | Scientific | 3.1k abstracts |
| SMoIlnstruct |  | Text | Multi-Task Instruction | No | No | Auto | Molecular | 340k instructions |
| HoneyBee | 2023 | Text | Multi-Task Instruction | No | No | Manual&Auto | Materials Science | 52k instructions |
| IDL |  | Text | Multi-Task Instruction | No | No | Manual | Industry | 15M documents |
<!-- DATASETS_MATRIX_END -->
