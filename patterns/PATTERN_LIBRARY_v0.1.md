# ProofAtlas Pattern Library v0.1 — Corpus-Derived

本库不是按教材章节预先设计，而是从 40 个 Integrated Skill 输出中按**重复出现频率 + 跨题迁移价值 + failure pressure**抽取。

纳入原则：重复出现，或虽频率较低但对高价值构造（递归、anchor、route）具有独立机制意义。

## PL-01 — Bridge / Intermediate Object
**Trigger signal.** 目标把两个难直接比较的对象连在一起，而已有控制分别落在某个中间对象两侧。  
**Mechanism.** 插入一个能被两侧工具分别控制的中间对象，把 mixed variation 拆开。  
**Corpus anchors.** AN-001, AN-013, AN-025  
**Common failures.** 把任何加减中间项都误判为 bridge；只解释三角不等式，不解释为何选这个中间对象。

## PL-02 — Localization / Local Stabilization
**Trigger signal.** 某个系数、分母或非线性量仍依赖未知变量。  
**Mechanism.** 先把变量限制在基点附近，把危险量换成只依赖固定数据的 bound。  
**Corpus anchors.** AN-011, AN-012, AN-023  
**Common failures.** 把方便半径说成必要；忘记说明 localization 的功能。

## PL-03 — Error Budget Allocation
**Trigger signal.** 目标误差被拆成多个可分别控制的项。  
**Mechanism.** 先定义总预算，再给每项分配局部预算；对称 ε/m 只是 specialization。  
**Corpus anchors.** AN-001, AN-013, AN-025  
**Common failures.** 把 ε/2、ε/3 说成唯一选择；先看到教材常数再倒推预算。

## PL-04 — Constraint Merge by min/max
**Trigger signal.** 多个参数约束必须同时成立。  
**Mechanism.** 多个“足够小”约束用 min 合并；多个“足够大”阈值用 max 合并。  
**Corpus anchors.** AN-001, AN-002, AN-006, AN-011, AN-039  
**Common failures.** 只给最终 min/max 不给父约束；把 presentation order 当 search order。

## PL-05 — Tail Control + Finite Prefix
**Trigger signal.** 结论是全局的，但已有极限/Cauchy 信息只控制尾部。  
**Mechanism.** 先统一控制尾部，再把有限前缀作为有限例外单独合并。  
**Corpus anchors.** AN-002, AN-004, AN-029, AN-030, AN-032  
**Common failures.** 把有限前缀省略到 learner 无法补全；对简单尾部证明过度建模。

## PL-06 — Compactness Extraction
**Trigger signal.** 有界/紧对象中存在无限复杂行为，需要提取稳定子结构。  
**Mechanism.** 把问题编码成序列/候选后，用紧性提取收敛子列，再把局部性质传到极限。  
**Corpus anchors.** AN-007, AN-017, AN-019, AN-020, AN-024  
**Common failures.** 把 compactness 当“魔法收敛按钮”；忽略提取后 returned artifact 的作用。

## PL-07 — Recursive Selection Policy
**Trigger signal.** 需要构造子列、嵌套对象或逐步 witness，且每一步依赖前一步状态。  
**Mechanism.** 显式维护 state、admissible choices、selection rule、invariant 和 progress measure。  
**Corpus anchors.** AN-007, AN-008, AN-009  
**Common failures.** 只展示最终序列，不展示 policy；忘记 strict-increase / nesting invariant。

## PL-08 — Near-Extremal Witness
**Trigger signal.** sup/inf 给出抽象极值，但目标需要真实序列项/可行点。  
**Mechanism.** 用 ε-近极值元素把抽象 extremum 拉回原集合，再令 tolerance→0。  
**Corpus anchors.** AN-005, AN-008, AN-018  
**Common failures.** 把 supremum 当成已经达到的 maximum；没有说明近极值元素为何存在。

## PL-09 — Bad Object / Bad Sequence from Negation
**Trigger signal.** 否定连续性、一致性或正下界后，得到“每个尺度都有坏 witness”。  
**Mechanism.** 选一个趋零尺度，把每个尺度的局部失败串成坏序列/坏点对。  
**Corpus anchors.** AN-010, AN-016, AN-020  
**Common failures.** 量词否定错误；把 existential witness 与 chosen scale 混淆。

## PL-10 — Theorem-Input Manufacturing
**Trigger signal.** 想用强定理，但当前对象还不满足其标准输入格式。  
**Mechanism.** 构造 residual、cover、preimage、bundle 或 representation，使 theorem interface 被激活。  
**Corpus anchors.** AN-017, AN-021, AN-031, AN-039, AN-040  
**Common failures.** 只说“由定理”；把 theorem invocation 与 theorem preparation 混为一谈。

## PL-11 — Domination / Scalarization
**Trigger signal.** 对象级误差难直接控制，但可被更简单、与空间变量无关的标量对象压住。  
**Mechanism.** 建立 deterministic domination，再把问题降维到标量序列/尾和。  
**Corpus anchors.** AN-029, AN-030, AN-032, AN-033  
**Common failures.** 忽略 uniformity 来源；只记判别法名字，不理解 majorant 机制。

## PL-12 — Representation Alignment / Residualization
**Trigger signal.** 目标形式与已知定义/定理接口不匹配。  
**Mechanism.** 重写目标，暴露 derivative quotient、zero residual、partial sums、norm 等已有接口。  
**Corpus anchors.** AN-015, AN-021, AN-033, AN-037  
**Common failures.** 把经典 trick 当不可解释灵感；用最终漂亮形式反向制造唯一动机。

## PL-13 — Anchor Condition
**Trigger signal.** 已有控制只确定相对变化，存在平移/基准自由度。  
**Mechanism.** 固定一个基准点/基准项，把相对控制转成绝对控制。  
**Corpus anchors.** AN-004, AN-031  
**Common failures.** 不解释为什么需要 anchor；把 anchor 误当任意技术细节。

## PL-14 — Periodic/Subsequence Decomposition
**Trigger signal.** 整体对象因振荡或混合行为缺少单调结构。  
**Mechanism.** 按周期或结构类别拆成子序列，在子序列上恢复单调/夹逼，再重新组合。  
**Corpus anchors.** AN-034, AN-024  
**Common failures.** 机械拆分无结构收益；省略为何选该分解。

## Library design rule

Patterns are **mechanisms**, not chapter labels. New patterns should enter only when repeated corpus failures show that an existing mechanism cannot describe the construction without distortion.
