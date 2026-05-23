# Task 05: 为单篇论文准备 Source Packet

## 目标

为每个 case 准备可追溯的源材料包，作为强模型和人工抽取 source facts 的输入。

注意：Task 05 不是构建给 Agent 看的匿名任务包。它只负责准备 evaluator-only 的 `source_packet.md`，并在需要时同步更新 `metadata.yaml`。`agent_task_level1.md`、`agent_task_level2.md`、`agent_task_level3.md`、`agent_task_perturbed.md`、`agent_task_no_solution.md` 仍保持模板占位，直到 Task 09-13 再构建。

## 输入

- 入选论文 PDF
- `benchmark/case_registry.csv`
- 原论文来源链接或本地路径

## 需要做什么

1. 为每个 case 创建目录，例如 `benchmark/cases/C001_consumer_credit/`。
2. 写 `source_packet.md`。
3. 记录论文 metadata：题名、作者、年份、领域、PDF 路径、来源 URL。
4. 明确写出 `Research Question And Objective`，区分原论文研究问题和未来匿名 benchmark 任务目标。
5. 抽取论文中和研究问题、数据、实验设计、识别策略、结果、局限相关的片段。
6. 给每个片段编号，例如 `[P001]`、`[P002]`。
7. 如果使用 PDF 页码，记录页码。

## 具体执行方法

1. 先定位论文中的 abstract、introduction、data/experimental design、empirical strategy、robustness、limitations。
2. 在 `Paper Metadata` 后添加 `Research Question And Objective`，至少包含 `source_research_question`、`benchmark_research_objective`、`target_mechanism_or_estimand`、`why_this_case_tests_agent_weakness`。
3. 每个部分只摘和 benchmark 构建有关的段落，不复制整篇论文。
4. 每个 passage 使用稳定编号：`[P001]`、`[P002]`。
5. 每个 passage 后写 `source_page`、`section`、`why_included`。
6. 如果信息来自表格、附录或脚注，要单独作为 passage 记录。
7. 对不确定信息不要补全，写进 `extraction_uncertainties`。

## 非目标

- 不填 `agent_task_*` 文件。
- 不匿名化生成最终任务包。
- 不写隐藏 gold reference。
- 不评分 Agent 输出。

## Passage 模板

```markdown
[P001]
source_page:
section:
why_included:
text:
```

## 产出

- `benchmark/cases/<case_id>/source_packet.md`

## 建议结构

```markdown
# Source Packet: C001

## Paper Metadata

## Research Question And Objective

- source_research_question:
- benchmark_research_objective:
- target_mechanism_or_estimand:
- why_this_case_tests_agent_weakness:

## Source Locations

## Extracted Passages
[P1] ...

## Human Notes
- suspected_linchpin:
- known_risks:
- extraction_uncertainties:
```

## 完成范围

本轮已完成 frozen pilot set：`C001`、`C002`、`C005`、`C008`、`C014`。Main set 其余 case 可在 pilot 流程验证后按同一模板扩展。

## 验收标准

- [x] 每个关键事实都能追溯到 passage id 或页码。
- [x] source packet 可以独立支持后续 gold reference 编写。
- [x] 不要求全文复制论文，只抽取和 benchmark 构建有关的内容。
- [x] 对不确定的片段要标记 `extraction_uncertainties`。

## 常见风险

- 直接让模型读整篇 PDF，不保留引用位置。
- 只摘摘要，导致数据结构和识别命门缺失。
- source packet 过长，后续模型输入噪声太大。
