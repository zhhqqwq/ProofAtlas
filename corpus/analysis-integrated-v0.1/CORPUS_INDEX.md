# ProofAtlas Analysis Integrated Corpus v0.1

Corpus size: **40 complete analysis proof cases**

Purpose: batch-test Integrated ProofAtlas Skill v0.2 on real-analysis proof explanations, with both construction-heavy and low-archaeology cases.

## Cases

| ID | Proof | Difficulty | Mode | Depth |
|---|---|---:|---|---|
| AN-001 | 数列极限唯一性 | introductory | teach | L2 |
| AN-002 | 收敛数列必有界 | introductory | teach | L1 |
| AN-003 | 收敛数列的子列同极限 | introductory | expand | L1 |
| AN-004 | Cauchy 数列必有界 | introductory | teach | L2 |
| AN-005 | 单调有界数列收敛 | intermediate | teach | L2 |
| AN-006 | 夹逼定理 | introductory | expand | L1 |
| AN-007 | Bolzano–Weierstrass | advanced | construct | L3 |
| AN-008 | limsup 的逼近子列 | advanced | construct | L3 |
| AN-009 | liminf 的逼近子列 | advanced | construct | L3 |
| AN-010 | 闭集的序列判别 | intermediate | teach | L2 |
| AN-011 | x² 的 ε–δ 连续性 | introductory | trace-constant | L2 |
| AN-012 | 1/x 的连续性 | intermediate | trace-constant | L2 |
| AN-013 | 连续函数乘积仍连续 | introductory | teach | L2 |
| AN-014 | 复合函数连续 | introductory | theorem-role | L1 |
| AN-015 | 可微推出连续 | introductory | motivate | L1 |
| AN-016 | 连续性的序列判别 | intermediate | teach | L2 |
| AN-017 | 连续像保持紧性 | intermediate | theorem-role | L2 |
| AN-018 | 极值定理 EVT | intermediate | teach | L2 |
| AN-019 | 紧集上正连续函数有正下界 | intermediate | compare | L3 |
| AN-020 | Heine–Cantor 定理 | advanced | teach | L3 |
| AN-021 | 区间自映射固定点 | intermediate | motivate | L2 |
| AN-022 | 介值定理的符号版 | introductory | theorem-role | L1 |
| AN-023 | sqrt(x) 的连续性 | intermediate | teach | L2 |
| AN-024 | 严格单调连续函数的反函数连续 | advanced | teach | L3 |
| AN-025 | 一致极限保持连续 | intermediate | teach | L3 |
| AN-026 | 一致收敛保持有界性 | introductory | teach | L1 |
| AN-027 | 一致收敛与 Riemann 积分交换极限 | intermediate | theorem-role | L2 |
| AN-028 | 一致 Cauchy 判别 | advanced | teach | L3 |
| AN-029 | Weierstrass M-test | intermediate | theorem-role | L2 |
| AN-030 | 绝对收敛推出一致收敛的尾估计形式 | intermediate | expand | L2 |
| AN-031 | 导数一致收敛定理（锚点版） | advanced | teach | L3 |
| AN-032 | 绝对收敛推出收敛 | introductory | theorem-role | L1 |
| AN-033 | 比较判别法 | introductory | teach | L1 |
| AN-034 | 交错级数判别与误差估计 | intermediate | teach | L2 |
| AN-035 | Cauchy 凝聚判别 | advanced | construct | L2 |
| AN-036 | 积分判别法 | intermediate | theorem-role | L2 |
| AN-037 | Archimedean 性：存在 n 使 1/n<ε | introductory | expand | L1 |
| AN-038 | 有理数在实数中稠密 | intermediate | construct | L2 |
| AN-039 | 紧集必有界 | intermediate | construct | L2 |
| AN-040 | 紧集在 R 中闭 | advanced | teach | L2 |

## Distribution

- introductory: 14
- intermediate: 17
- advanced: 9

Recommended modes:

- teach: 18
- theorem-role: 7
- construct: 6
- expand: 4
- trace-constant: 2
- motivate: 2
- compare: 1

## Design notes

- Low-archaeology controls are deliberate.
- Canonical textbook proofs are normally calibrated `M3-provisional`, not automatically M3.
- Alternative routes are preserved.
- Constant provenance distinguishes problem data, existential witnesses, convenient specializations, and derived constants.
