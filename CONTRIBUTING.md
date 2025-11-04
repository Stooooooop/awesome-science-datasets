# 贡献指南

感谢你的贡献！为保持清单高质量，请遵循：

## 条目规范
- **必要字段**：`name / task / domain / modality / url.primary|paper|home / license / size / notes`
- **权威链接优先**：优先使用官方 GitHub 或官网为 `url.primary`。
- **最小噪音**：避免博客转载/二手仓库，必要时作为 `notes` 补充。
- 每个 PR 通过 `Link Check` 工作流（自动执行）。

## 提交流程
1. Fork 仓库，创建分支：`feat/add-xxx-dataset`
2. 更新 `datasets.yaml`（或 `datasets.json`）；如需可读列表，更新 `categories/*.md`
3. `scripts/check_links.py` 本地自检（可选）
4. 发起 PR，说明变更与来源

## 风格/格式
- 英文名称统一首字母大写；数字用半角。
- `notes` 简洁具体（≤ 100 字），避免营销描述。
