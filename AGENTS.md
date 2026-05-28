# 仓库指南

## 项目结构与模块组织

本仓库是一个面向 OOD 商业与经济学研究设计任务的 benchmark 构建工作区。核心材料位于 `benchmark/`，包括 `scope.md`、`case_taxonomy.md`、`case_registry.csv`，以及 `benchmark/cases/` 下按 case 划分的子目录。新建 case 时一律从 `benchmark/cases/C000_template/` 复制。标注材料放在 `annotations/`，运行输出放在 `outputs/`，汇总指标与图表放在 `results/`，报告相关内容放在 `report/`。源 PDF 保留在 `downloads/`，不得出现在 agent-facing 任务文件中。

## 构建、测试与开发命令

本仓库没有正式的构建系统，日常工作主要是新增或修订 benchmark 资产。

- `cp -R benchmark/cases/C000_template benchmark/cases/C015_new_case`：从模板创建新 case。
- `rg --files benchmark/cases/C001_charitable_giving`：检查某个 case 是否具备预期文件集。
- `rg '^<!-- visibility:' benchmark/cases/C*/agent_task_*.md`：验证 agent-facing 文件是否包含可见性头。
- `git diff --check`：在提交前检查空白字符和 patch 格式问题。

## 编码风格与命名约定

优先使用简短、明确的 Markdown 和 YAML。Markdown 使用 ATX 标题（`##`），正文保持陈述式写法；YAML 列表使用两个空格缩进。Case 目录必须遵循 `benchmark/cases/C###_anonymous_short_name/` 格式。文件名应与 `C000_template` 保持一致。Agent-facing 文件统一使用 `agent_task_*.md` 命名；evaluator-only 文件保留现有文件名和元数据块。Agent-facing 内容中不得出现论文标题、作者姓名、精确地点或源 PDF 路径。

## 测试指南

本仓库的验证以结构检查和内容审校为主，而不是自动化测试。提交 PR 前，请确认每个 case 都包含模板中的完整文件集，且只有 `agent_task_*.md` 可进入 agent 上下文，evaluator-only 文件必须被排除。匿名化检查应对照 `benchmark/repository_structure.md` 手动完成，并抽查 YAML 中的 `agent_context_allowlist` 与 `agent_context_blocklist`。

## Benchmark 运行纪律

当前 benchmark 的正式运行目标是以 task packet 为主要证据来源、同时允许远程检索辅助的研究设计推理，而不是单纯比拼本地文件访问、论文记忆或工具炫技。默认运行要求如下：

- 使用本地 OpenClaw `benchmark_isolated` agent。
- 工具设置必须如实记录；是否开放 web/search 不再由任务包文本硬编码。
- 仅允许输入 `benchmark/cases/*/agent_task_*.md`。
- 正式评测遵循 `one run = one case = one variant = one agent-facing packet`。不要把同一 case 的多个 level 或 variant 一起喂给 agent。
- 每次运行都必须记录到 `outputs/run_manifest.csv`。
- 原始输出必须保存到 `outputs/raw_agent_logs/{pilot,main}/`。
- 不允许把 `metadata.yaml`、`gold_reference.md`、`audit.md`、`source_packet.md` 或 variant note 注入 agent 上下文。

当前正式运行 agent 为 `benchmark_isolated`。它的用途是复用固定 sandbox workspace，同时禁止本地文件工具，并通过外部脚本把单个 `agent_task_*.md` 作为纯文本消息送入 agent。该模式默认允许远程联网与文献工具，但本地 hidden benchmark files 必须始终不可见。

`benchmark_isolated` 的当前边界如下：

- workspace 固定为 `/Users/jiangcanxiang/OpenClawBenchmarkIsolated`
- workspace 位于 benchmark 仓库之外
- `AGENTS.md` 之外的 bootstrap 文件已清空，避免注入额外上下文
- agent 不暴露本地文件读取或写入工具
- 默认允许远程工具，包括 `web_search`、`web_fetch`、`deepxiv`、`semantic-scholar`，以及未来新增的非本地文件型远程 MCP
- 推荐通过 `scripts/run_isolated_packet.sh` 启动，以 fresh session id 运行
- `scripts/run_isolated_packet.sh` 默认超时为 `86400` 秒，可按需显式传更小值
- `deepxiv` 与 `semantic-scholar` 的 MCP 握手超时当前均已放宽到 `300000ms`
- 经验上，`deepxiv` 可稳定使用；`semantic-scholar` 已不再因握手超时而缺席，但仍可能遇到上游 API rate limit
- `semantic-scholar` 当前还加了一层本地保守限速 wrapper；匿名默认按 `0.5 req/s`、`burst=1` 运行
- 即便如此，无 API key 时仍可能因匿名共享池被上游 `429`；这属于外部配额限制，不是本地 OpenClaw 启动问题

当前推荐的实际执行 pipeline 如下：

1. 选择一个单独的 `agent_task_*.md` 文件作为本次 run 的唯一输入。
2. 由仓库外部脚本读取该文件文本，而不是让 OpenClaw 自己去文件系统中打开 benchmark 文件。
3. 通过 `scripts/run_isolated_packet.sh` 把这段纯文本作为 `--message` 发送给 `benchmark_isolated`。
4. 每次运行使用 fresh session id，避免不同 case 或 variant 之间串上下文。
5. agent 基于这段文本生成输出；后续再由外部流程记录 raw log、manifest 和 review 结果。

因此，当前 pipeline 不是“手动复制粘贴整组文件”，也不是“让 agent 自己浏览 case 目录”，而是“外部脚本读取单个 task packet，再把纯文本送入 agent”。

当前还新增了一个 batch 入口：

- `scripts/run_batch_isolated.sh`

推荐用途：

- `run_isolated_packet.sh`
  - 单条 run / smoke test / focused rerun
- `run_batch_isolated.sh`
  - 多条 case 的串行 batch run
  - 自动保存原始 JSON
  - 自动生成规范化 raw log
  - 自动追加 `run_manifest.csv`

若模型输出引用了任务包中未明确给出的关键设计细节，或明显反推出源论文式结构，即使没有调用工具，也不能自动记为 `clean`，而应按 `suspected` 或 `contaminated` 处理。

## 当前阶段状态

截至 `2026-05-28`，仓库状态如下：

- `task16` 已完成，OpenClaw benchmark 运行配置已冻结。
- `task17` 的首轮 5-case Level 2 pilot batch 已执行并完成首轮 review。
- `task17` 的 `benchmark_isolated` rerun 已完成。
- 已新增 `benchmark/pilot_review.md`，并将 5 条 pilot run 回写到 `outputs/run_manifest.csv`。
- 已在 `annotations/annotation_sheet.csv` 中加入每个 pilot output 的 quick spot-check claims。
- isolated rerun 显示 5/5 runs 均未实际调用工具；`C001`、`C002` 仍有问题，`C005`、`C008`、`C014` 明显改善。
- 已对 `C001`、`C002` 做 focused rerun；两条 trajectory 仍均为 `actual tool use = none`。
- `C002` 的中文输出问题在 focused rerun 中未再出现，但 `C001` 与 `C002` 仍都因为 packet-overreach 保持 `suspected`。
- `benchmark_retrieval` 不再单独设立；正式 benchmark 条件统一为 `benchmark_isolated`。
- `task18` main run 已完成，正式主矩阵的成功输出现已齐备。
- `task19` claim extraction 已完成，`outputs/parsed_claims/claims_to_annotate.csv` 已生成。
- `task20` first-pass annotation 已完成，`annotations/annotation_sheet.csv` 与 `annotations/annotation_guide.md` 已更新。
- `task21` second-label adjudication 已完成，`annotations/second_labels.csv`、`annotations/adjudication_notes.md` 与 `annotations/adjudicated_labels.csv` 已生成。
- `annotations/adjudicated_labels.csv` 现为后续统计与分析的唯一标签来源。
- `task22` metrics 与 figures 已完成，`results/metrics_summary.csv`、`results/grouped_metrics.csv` 与 `results/figures/*.svg` 已生成。
- `task23` failure-case analysis 已完成，`results/failure_cases.md` 已生成。
- `task24` final report package 已完成，`report/research_report.md`、`report/reproducibility_readme.md` 与 `report/presentation_outline.md` 已生成。
- 当前主线任务已全部完成。

当前的主要问题已经收缩为两类：

- 如何根据课程或论文用途裁剪现有交付物
- benchmark 运行时是否继续保留带噪声的 `semantic-scholar` MCP

目前已经在全部 agent-facing task packet 的 `Task Rule` 中加入 anti-reconstruction 约束，并完成了 focused rerun；主线 benchmark pipeline 已完成。后续若继续推进，应转向课程展示版裁剪、论文写作润色，或追加新 case / 新 agent 的扩展实验。

## 阶段顺序

后续工作默认遵循以下顺序，不跳步：

1. smoke test
2. anonymization / leakage revision if needed
3. 5-case pilot batch
4. pilot review and schema revision
5. claim extraction
6. annotation and adjudication
7. metrics and report

只有当 smoke test 和 pilot review 都通过后，才进入正式模型评测阶段。

## 提交与 Pull Request 规范

现有提交历史以简短的祈使句为主，例如 `Build pilot benchmark task packets`、`Add high-level case construction workflow`。后续也保持这一风格，例如 `Add C015 retail pricing case` 或 `Refine annotation guide labels`。PR 需要说明受影响的 case ID，概述 schema 或任务包的改动，标明是否做过 leakage risk 审查，并在目录结构变化时附上关键路径示例。
