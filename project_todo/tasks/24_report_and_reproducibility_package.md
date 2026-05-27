# Task 24: 写研究报告与复现说明

## 目标

把 benchmark 设计、实验结果、失败分析和可复现材料整理成最终研究包。

## 输入

- benchmark cases
- raw logs
- annotations
- metrics
- failure cases
- figures

## 需要做什么

1. 写 research report。
2. 写 reproducibility README。
3. 整理 benchmark case package。
4. 整理 raw outputs 和 parsed claims。
5. 整理 annotations 和 adjudication notes。
6. 整理 metrics 和 figures。
7. 写 limitations 和 future work。
8. 如需展示，裁剪 slides/poster/demo script。

## 具体执行方法

1. 先写报告主论点，不要先堆材料。主论点应回答：Agent 在商科 OOD 因果设计中具体弱在哪里。
2. 方法部分说明 case construction、information gradient、variants、locally isolated but remote-tool-enabled benchmark condition、annotation protocol。
3. 结果部分先给总体指标，再给分组指标，最后给失败案例。
4. 每个失败案例都要引用 raw output 和 gold reference。
5. limitations 必须承认 case 数量、人工标注、locally isolated but remote-tool-enabled 设置、商科子领域覆盖等限制。
6. reproducibility README 按“如何复查一个 case”和“如何复现指标”两条路径写。

## reproducibility README 必须回答

```markdown
1. case 文件在哪里？
2. agent 输入在哪里？
3. raw output 在哪里？
4. claim 抽取表在哪里？
5. 人工标注在哪里？
6. 指标如何从标注表计算？
7. 失败案例对应哪些 run_id？
```

## 产出

```text
report/
  research_report.md
  reproducibility_readme.md
  presentation_outline.md
```

## 报告建议结构

1. Problem definition
2. Benchmark design
3. Case construction
4. Agent run setup
5. Annotation protocol
6. Metrics
7. Results
8. Failure cases
9. Limitations
10. Recommendations

## 验收标准

- [ ] 报告能清楚解释为什么商科因果设计是 OOD 压力测试。
- [ ] 结果基于 main-set 数据，不只基于单例。
- [ ] 至少包含 3 张核心图表。
- [ ] 至少包含 3 个失败案例。
- [ ] README 能让另一个人理解如何复查输入、输出、标注和指标。

## 常见风险

- 报告变成流水账，没有中心论点。
- 只展示失败，不展示评测协议如何保证公平。
- 没有说明局限性，例如 case 数量、人工标注主观性、locally isolated but remote-tool-enabled 设置。
