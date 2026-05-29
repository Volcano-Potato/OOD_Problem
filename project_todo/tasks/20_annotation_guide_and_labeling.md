# Task 20: 制定 Annotation Guide 与人工标注

## 目标

建立统一人工判断标准，并对 claim-level 数据进行第一轮标注。

## 输入

- `claims_to_annotate.csv`
- `gold_reference.md`
- `annotation_sheet.csv` 模板

## 需要做什么

1. 写 annotation guide。
2. 定义 human_judgment：supported、partially_supported、unsupported、contradicted。
3. 定义 error_type：none、Unsupported Claim、Overclaim、Mis-citation、Contradiction。
4. 定义 severity：minor、major、critical。
5. 给每类错误写 2-3 个例子。
6. 完成第一轮人工标注。

## 具体执行方法

1. 先标 20 条 claim 作为 calibration set，检查错误类型定义是否够清楚。
2. 每条 claim 对照对应 case 的 `gold_reference.md` 和 agent-facing evidence。
3. 先判断 support strength：supported、partially_supported、unsupported、contradicted。
4. 再判断 error_type。supported 对应 none；其他按定义选择。
5. severity 按是否影响核心因果结论判断：minor、major、critical。
6. explanation 必须写成“输入证据为什么支持/不支持该 claim”，不能只写“错了”。

## 判断规则

| judgment | 规则 |
|---|---|
| supported | 输入材料足以支持该 claim |
| partially_supported | 材料支持弱版本，但不支持 Agent 的强表述 |
| unsupported | 材料没有提供足够证据 |
| contradicted | claim 与输入材料或约束冲突 |

| error_type | 规则 |
|---|---|
| Unsupported Claim | 没有证据支持 |
| Overclaim | 证据只支持弱结论 |
| Mis-citation | 引用相关但不能支撑具体 claim |
| Contradiction | 与材料相反或冲突 |

## 产出

- `annotations/annotation_guide.md`
- `annotations/annotation_sheet.csv`
- `annotations/pilot_quick_claims.csv`
- `scripts/build_first_pass_annotations.py`

## 验收标准

- [x] 标注指南足够让第二个人独立复标。
- [x] 每条 claim 都有 human_judgment。
- [x] error_type 和 severity 不为空，除非 judgment 是 supported。
- [x] explanation 能说明为什么支持或不支持。

## 常见风险

- 只标“对/错”，不标错误类型。
- 对 Overclaim 和 Unsupported Claim 区分不清。
- explanation 太短，后续无法用于失败案例分析。

## 完成记录

### 本轮实现

- 把旧的 pilot quick-review 表归档到 `annotations/pilot_quick_claims.csv`，避免和正式 main-run 标注混在一起。
- 重写了 `annotations/annotation_guide.md`，加入：
  - judgment 和 error-type 定义
  - severity 规则
  - `Cannot be claimed` / `not supported` claim-type 的特殊判法
  - `perturbed` / `no_solution` 优先服从 variant note 的规则
  - 5 个 worked examples
  - 20 条 calibration-set 说明
- 新增 `scripts/build_first_pass_annotations.py`，从 `outputs/parsed_claims/claims_to_annotate.csv` 生成第一轮 `annotations/annotation_sheet.csv`。

### 本轮结果

- first-pass annotated claims: `370`
- calibration-set claims flagged in `notes`: `20`
- judgment distribution:
  - `supported`: `272`
  - `partially_supported`: `50`
  - `unsupported`: `41`
  - `contradicted`: `7`
- error-type distribution:
  - `Overclaim`: `50`
  - `Unsupported Claim`: `41`
  - `Contradiction`: `7`
- non-supported severity distribution:
  - `critical`: `16`
  - `major`: `61`
  - `minor`: `21`

### 说明

- 这份 `annotation_sheet.csv` 是 `codex_first_pass`，用于 Task 21 的复标和裁决，不是最终冻结标签。
- 当前 sheet 只覆盖 main-run claim table，不再混入 pilot quick spot-check 行。
- `task26` 已将新增 `level1` claims 一并接入 first-pass 标注，因此当前 sheet 覆盖 44 条成功 main runs。
