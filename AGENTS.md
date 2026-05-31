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

截至 `2026-05-31`，仓库状态如下：

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
- `task26` 已完成：
  - 10 条 `level1` main runs 已追加到正式矩阵
  - claims / annotations / adjudication / metrics 已重算
  - `results/perturbed_mechanical_reuse.csv` 与 `results/perturbed_pair_audit.md` 已生成
  - README 与 report 中的过强措辞已收口
- 主线 benchmark 到此冻结：
  - 若按正式 benchmark 主线口径，完成点仍是 `task26`
  - 主 headline 仍以 baseline `benchmark_isolated` 结果为准
- `task27` 已完成：
  - Bottleneck framing 已写入 `README.md`、`report/research_report.md`、`report/presentation_outline.md`
- `task28` 已完成：
  - `results/bottleneck_crosswalk.md` 已生成并接入 report / metrics summary
- `task29` 已完成：
  - APE-style pairwise design-memo extension 已生成
  - 但该层结果仍应视为 exploratory extension，而不是主结论 headline
- `task30` 已完成到首轮 intervention study：
  - 已实现 `research_agent_v1` 三阶段外部编排：
    - `Stage 3` candidate generation
    - `Stage 4` independent critique
    - `Stage 5` final reconcile memo
  - 已完成 `10` 条 `perturbed` case 的正式 batch rerun
  - 已生成：
    - `results/perturbed_mechanical_reuse_v1.csv`
    - `results/perturbed_pair_audit_v1.md`
    - `results/metrics_summary_research_agent_v1.csv`
    - `results/metrics_summary_research_agent_v1.md`
    - `results/research_agent_v1_vs_baseline.md`
  - 当前最重要的 intervention 结果是：
    - baseline `perturbed mechanical reuse = 9/10`
    - `research_agent_v1 perturbed mechanical reuse = 2/10`
  - 解释上应把这视为 `task30` 的主结果
  - 但 `research_agent_v1` 的一般 claim-level headline metrics 仍应暂作 provisional，因为现有 override 体系主要是围绕 baseline 冻结 run IDs 构建
- `task31` 已完成：
  - 已新增轻量 threat-recognition audit：
    - `results/threat_recognition_audit.csv`
    - `results/threat_recognition_summary.md`
  - 范围限定为 baseline `level2` 主集 `10` 条输出
  - 结果为：
    - average threat hits per case = `1.9/2`
    - overall threat hit rate = `19/20 = 95.0%`
    - `9/10` case 为 `2/2`
    - `1/10` case 为 `1/2`
  - 解释上，这意味着 baseline `level2` 的主要问题更像是后续 claim calibration / overreach，而不是简单 threat blindness
- `task32` 尚未开始。

当前最重要的主结论是：

- `level1 -> level2` 有明显提升，而 `level2 -> level3` 基本持平
- `perturbed` 的配对审计显示 `9/10` case 存在 broken-identification 下的 mechanical reuse
- `no_solution` 结果应限定表述为 `4/4 tested runs`，而不是无条件 headline rate
- `task30` 的扩展性结论是：
  - critic-and-reconcile intervention 在 `10` 条 `perturbed` case 上把 mechanical reuse 从 `9/10` 降到了 `2/10`
- `task31` 的扩展性结论是：
  - baseline `level2` threat-recognition audit 为 `19/20`
  - 因而主线弱点更像是 threat-to-claim alignment，而不是 threat recognition 缺失

目前已经在全部 agent-facing task packet 的 `Task Rule` 中加入 anti-reconstruction 约束，并完成了主矩阵、level1 补跑、paired perturbed audit、首轮 `research_agent_v1` intervention study，以及 baseline `level2` threat-recognition audit。后续若继续推进，应转向：

- 课程展示版裁剪或论文写作润色
- `task32` no-solution 扩展
- 或进一步扩展新的 agent arm / 新 case

## 后续扩展方向参考

当前仓库的正式 benchmark 配置与主线结论已基本冻结；以下内容仅作为后续扩展与改版时的方向性参考，而不是立即执行的结构调整要求。

可将 ETH / UZH 的 `Project APE` 与 `The Ideation Bottleneck` 论文视为方法论参照。对本项目最有启发的，不是“自动生成论文”本身，而是把研究设计过程拆解为可审计、可比较、可复核的多个环节：尽量基于真实外部证据而非闭门补全；强调输出后的 review、复现与错误筛查；并尽量避免让同一生成过程承担自评职责。若未来扩展 benchmark，可更多考虑把“提出研究想法”“选择识别策略”“执行设计细化”“反思局限与稳健性”区分为可观察的不同能力维度。

`The Ideation Bottleneck` 的核心启发是，AI 经济学研究与人类研究之间的主要差距更可能出现在 `idea quality`，而不只是执行细节。因此，本项目后续若新增 case、评分维度或 review 规则，应优先增强对以下能力的识别：是否真正提出了新颖且合适的问题设定；是否避免对熟悉模板或标准识别设计的机械复用；是否能在证据受限条件下给出有判断力的 research design，而不是仅复述常见 econometrics recipe。当前已观察到的 `perturbed` mechanical reuse 问题，可继续沿这一方向深化为后续版本的重要设计抓手。

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

另外，后续每次完成一个实际任务阶段或形成新的可引用结果时，都应同步更新 `RUN_LOG.md`。不要把日志记录留到多个任务之后再补写；`RUN_LOG.md` 应始终近似反映仓库的最新真实状态。
