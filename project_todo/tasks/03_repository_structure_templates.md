# Task 03: 建立目录结构与文件模板

## 目标

把 benchmark 的文件结构固定下来，保证每个 case 产物一致、可复查、可复跑。

## 输入

- Task 01 `benchmark/scope.md`
- Task 02 `benchmark/case_taxonomy.md`

## 需要做什么

1. 创建 benchmark 目录结构。
2. 为单个 case 创建标准模板。
3. 为 outputs、annotations、results、report 创建目录。
4. 写一个 case 文件命名规范。
5. 明确哪些文件 agent-facing，哪些 evaluator-only。

## 具体执行方法

1. 先创建 `C000_template/`，所有真实 case 从这个模板复制。
2. 每个模板文件顶部写 visibility 注释，避免误把 gold reference 塞进 Agent 输入。
3. case 目录名使用匿名短名，例如 `C001_consumer_credit/`，不要用原论文标题。
4. `metadata.yaml` 放机器可读信息；markdown 文件放人类可读内容。
5. 所有 agent-facing 文件命名以 `agent_task_` 开头；所有隐藏评测文件明确写 `evaluator-only`。

## 文件头模板

```markdown
<!-- visibility: agent-facing -->
<!-- case_id: C001 -->
<!-- variant: level2 -->
```

```markdown
<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
```

## 产出

```text
benchmark/
  case_registry.csv
  case_taxonomy.md
  cases/
    C001_example/
      source_packet.md
      source_facts.md
      gold_reference.md
      agent_task_level1.md
      agent_task_level2.md
      agent_task_level3.md
      perturbed_variant.md
      no_solution_variant.md
      audit.md
      metadata.yaml
  prompts/
  run_configs/
outputs/
  raw_agent_logs/
  parsed_claims/
annotations/
  annotation_sheet.csv
  adjudicated_labels.csv
  annotation_guide.md
results/
  figures/
  failure_cases.md
report/
```

## 验收标准

- [x] 每个目录职责清楚。
- [x] 每个 case 的文件名固定，不随论文自由命名。
- [x] `agent_task_*` 文件不包含原论文题名、作者、真实地点或 gold reference。
- [x] `gold_reference.md`、`audit.md` 和 `metadata.yaml` 明确标记 evaluator-only。

## 常见风险

- 把隐藏答案和 agent 输入放在同一个文件里。
- 文件名包含原论文标题，导致匿名任务被泄漏。
- 缺少 metadata，后续统计需要人工补。
