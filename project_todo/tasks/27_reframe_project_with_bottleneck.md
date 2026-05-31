# Task 27: 用 Bottleneck 重写项目定位与主叙事

## 目标

把当前项目从“OpenClaw 商科 OOD benchmark”重写为一个更强的研究叙事：

- 以 *The Ideation Bottleneck* 为上位框架
- 把本项目定位为对 `execution residual` 的细粒度拆解
- 明确说明本项目聚焦的是 causal-design / mechanism / econometric-awareness failures，而不是泛化的“科研能力”

本 task 的任务是 **改 framing**，不是重跑实验。

## 为什么现在需要做

当前项目的实证主链路已经完整：

- 10-case main set
- `level1 -> level2 -> level3`
- `perturbed`
- `no_solution`
- claim extraction / adjudication / metrics / failure analysis

但如果没有一个更强的外部理论锚点，这些结果在答辩或报告中仍容易被理解成：

- “做了一个课程 benchmark”
- “测了 OpenClaw 在商科任务上的表现”

而不是：

- “对 Bottleneck 所识别的 execution gap 做了 OOD causal-design 方向的细粒度诊断”

因此，这个 task 的价值在于 **提升项目的研究身份**。

## 输入

- `report/research_report.md`
- `README.md`
- `report/presentation_outline.md`
- `codex_project_guide.md`
- `report/bottleneck_ape_leverage_plan.md`
- `The Ideation Bottleneck.pdf`
- 现有 `results/metrics_summary.md`

## 需要做什么

1. 在项目总述中引入 Bottleneck 的 `idea vs execution` 分解。
2. 明确写出：本项目不重做 idea-quality 比较，而是继续拆 execution 侧的 causal-design failures。
3. 将当前 benchmark 的核心结果重写为：
   - information gradient
   - mechanical reuse
   - no-solution honesty
   - packet overreach / mechanism confounding
4. 明确解释为什么本项目聚焦 identification 和 mechanism，而不把 robustness/writing 作为主轴。
5. 在 README 和报告里统一术语，不再混用：
   - “科研能力”
   - “因果设计能力”
   - “execution weakness”

## 具体执行方法

1. 先抽一段固定定位话术，后续在多个文档中复用。
2. 在 `research_report.md` 的 introduction 或 problem definition 里新增一段：
   - Bottleneck 先发现总体 AI-human gap
   - Bottleneck 将其拆为 idea / execution
   - 本项目承接 execution side
3. 在 `README.md` 的 opening section 同步改写成更短版本。
4. 在 `presentation_outline.md` 的开场 1-2 页中加入同样逻辑。
5. 所有改写必须和已有实证结果一致，不得新增未测结论。

## 建议产物

- 更新后的：
  - `README.md`
  - `report/research_report.md`
  - `report/presentation_outline.md`
- 如有需要，可补一个：
  - `report/framing_notes.md`

## 推荐改写重点

### 应强化的句子

- 本项目是对 `execution residual` 的细粒度诊断。
- 商科/经济学 causal-design task 是对 research agent 的 OOD stress test。
- `perturbed` 和 `no_solution` 不只是 harder tasks，而是对 identification vigilance 和 claim calibration 的定向 probes。

### 应避免的句子

- “本项目全面评估了科研 agent 的研究能力”
- “本项目证明 OpenClaw 不适合做商科研究”
- “本 benchmark 覆盖了 execution 的全部方面”

## 验收标准

- [x] `README.md` 已明确引用 Bottleneck 的 `idea vs execution` 分解。
- [x] `research_report.md` 已把本项目定位为 execution-side diagnostic，而非泛化 benchmark。
- [x] `presentation_outline.md` 已反映新的开场叙事。
- [x] 所有文档对本项目的核心对象表述一致。
- [x] 新叙事没有超出现有实验结果可支持的范围。
- [x] 所有修改通过 `git diff --check`。

## 常见风险

- 只加 citation，不改整体叙事结构。
- 把 Bottleneck 写成 related work 点缀，而不是 framing backbone。
- 为了对齐 Bottleneck 而夸大本项目的外推范围。
- introduction、README、presentation 三处口径不一致。
