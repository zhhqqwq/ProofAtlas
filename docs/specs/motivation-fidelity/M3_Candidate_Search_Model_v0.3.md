# ProofAtlas 核心规范 01-A：M3 Candidate Search Model v0.3

> 所属项目：ProofAtlas  
> 上位规范：Motivation Fidelity Standard v0.2  
> 文档性质：核心可执行规范草案 / 后续新对话交接文件  
> 当前阶段：只打磨“为什么想到”的真实性，不进入 Construction Archaeology 与 Cognitive Proof Graph 正式设计  
> 核心问题：**怎样判断一个数学构造或证明步骤，是否真的能够从“当时可获得的信息”中被合理发现，而不是 AI 看过答案后的事后解释？**

---

## 0. 本文的目标

Motivation Fidelity Standard v0.2 已经规定：ProofAtlas 的高质量“为什么想到”解释，应尽量达到 **M3 — Forward-Reconstructible Motivation**。

但 M3 仍然缺少一个真正可执行的候选生成模型。

本文将 M3 具体化为：

\[
\boxed{
\text{Goal}
\rightarrow
\text{Obstacle}
\rightarrow
\text{Available Information}
\rightarrow
\text{Required Property}
\rightarrow
\text{Candidate Family}
\rightarrow
\text{Candidate Selection}
\rightarrow
\text{Local Test}
}
\]

并正式回答以下问题：

1. 什么叫“当前 proof state 下合理可发现的候选”？
2. 候选应该怎样从目标与障碍中产生，而不是从参考答案中反推？
3. “自然候选、经验候选、逆向候选、试探候选”的边界在哪里？
4. 哪些逆向推理是合法数学规划，哪些属于答案泄漏？
5. 哪些试探属于真实数学搜索，哪些只是随机猜答案？
6. 多个候选同时合理时如何选择？
7. 失败候选如何更新当前搜索状态？
8. 怎样把整个过程编码为可供 Skill、Agent、Benchmark 和未来 Engine 使用的结构化记录？

本文不试图还原模型的隐藏思维链，也不要求保存无限详细的内部推理。需要保存的是**可审计的数学状态、候选来源、选择依据和测试结果**。

---

# 1. M3 的正式目标

设关键构造出现前的状态为：

\[
S_t.
\]

参考答案中的目标构造为：

\[
C^*.
\]

M3 不要求证明：

\[
S_t\Rightarrow C^*
\]

是逻辑上唯一可能的路径。

M3 真正要求的是：

> 隐藏参考答案之后，只利用构造出现前已经可获得的数学信息、允许使用的知识和合理搜索操作，能够产生一个**具有相同功能的候选族**，并从其中找到参考构造或功能等价构造。

因此 M3 的中心对象不是单一答案：

\[
C^*
\]

而是：

\[
\boxed{\mathcal F_t=\text{Candidate Family at state }S_t}
\]

即：

> **在当前状态下，哪些对象具有我们真正需要的性质？**

参考答案只是：

\[
C^*\in\mathcal F_t
\]

的一种可能实现。

---

# 2. M3 的核心哲学：先得到“需要什么”，再问“取什么”

数学学习中最容易制造后见之明的形式是：

> 参考答案取了 \(g(x)=\cdots\)，于是我们围绕 \(g\) 编一个解释。

ProofAtlas 必须尽可能反过来：

> 在不知道 \(g\) 的情况下，先确定一个新对象需要具有什么性质。

即：

\[
\boxed{
\text{Object Name Last, Required Property First}
}
\]

例如不要首先问：

> “为什么取 \(f(x_n)\)？”

而应先问：

> “我们需要一个中间量 \(B_n\)，使第一段差能够由 \(f_n\to f\) 控制，同时第二段差能够由 \(x_n\to x\) 与 \(f\) 连续控制。什么对象满足这两个接口？”

随后才发现：

\[
B_n=f(x_n).
\]

因此 M3 的关键不在于“解释最终对象”，而在于：

\[
\boxed{
\text{先独立产生 Required Property，再生成 Candidate Family}
}
\]

---

# 3. M3 Search State：候选生成时允许知道什么

为了可执行审计，定义搜索状态：

\[
S_t=(G_t,A_t,K_t,C_t,P_u,H_t).
\]

其中：

## 3.1 \(G_t\)：Goal State

当前真正需要完成的目标及子目标。

例如：

```text
Goal:
prove |f_n(x_n)-f(x)| -> 0
```

或者：

```text
Goal:
find c such that f(c)=c
```

目标不能只是把整道题原封不动复制进来，而应允许经过合法的目标规范化。

---

## 3.2 \(A_t\)：Available Mathematical Facts

构造出现以前已经得到或题设直接给出的事实。

例如：

- \(f_n\to f\)；
- \(x_n\to x\)；
- \(f\) 连续；
- \((x_n)\) 有界；
- 某个误差已经小于 \(\varepsilon/2\)。

后续才证明的事实不得提前进入 \(A_t\)。

---

## 3.3 \(K_t\)：Available Knowledge / Tools

当前学习者允许使用的：

- 定义；
- 定理；
- 推论；
- 标准恒等式；
- 已学证明模式；
- 合法计算工具。

这是 learner-relative 的。

对于不同学习者：

\[
K_t^{(u_1)}\neq K_t^{(u_2)}.
\]

因此一个研究生水平的 M3 路径，未必是大一学生水平的 M3 路径。

---

## 3.4 \(C_t\)：Constraint Set

当前已经明确产生的要求。

例如：

\[
\delta<1,
\qquad
6\delta<\varepsilon.
\]

或者对一个未知中间项 \(B\)：

\[
A-B \text{ 应由定理 }T_1\text{ 控制},
\]

\[
B-C \text{ 应由定理 }T_2\text{ 控制}.
\]

Constraint 不等于最终构造。

它只是限制候选空间。

---

## 3.5 \(P_u\)：Learner Pattern Repertoire

学习者已经掌握的证明模式，例如：

- 加一项减一项；
- 固定点转零点；
- \(\min\) 合并“小量”条件；
- \(\max\) 合并“大 \(N\)”条件；
- 反证失败统一控制后构造坏序列；
- 有界序列考虑抽取子列。

这个字段对于区分“自然候选”和“专家经验候选”非常重要。

---

## 3.6 \(H_t\)：Search History

当前搜索过程中已经：

- 尝试过哪些候选；
- 为什么拒绝；
- 新暴露了什么障碍；
- 新增了什么约束。

但 \(H_t\) 只能记录真实发生在当前重建流程中的合法搜索。

不能把参考答案后半部分偷偷写回搜索历史。

---

# 4. M3 Candidate Search 的标准流水线

正式定义：

\[
\boxed{
G
\rightarrow O
\rightarrow I
\rightarrow R
\rightarrow F
\rightarrow C
\rightarrow T
\rightarrow U
}
\]

分别表示：

- \(G\)：Goal；
- \(O\)：Obstacle；
- \(I\)：Available Information；
- \(R\)：Required Property；
- \(F\)：Candidate Family；
- \(C\)：Candidate；
- \(T\)：Local Test；
- \(U\)：State Update。

以下逐一正式定义。

---

# 5. Stage G — Goal Normalization

第一步不是找技巧，而是问：

> **当前真正需要得到什么数学对象或关系？**

允许的 Goal Normalization 包括：

## G1. 等价改写

例如：

\[
f(c)=c
\iff
f(c)-c=0.
\]

---

## G2. 目标拆分

例如：

\[
E<\varepsilon
\]

拆成若干可分别控制的误差项。

---

## G3. 量词显式化

例如：

“连续”展开为：

\[
\forall \varepsilon>0,
\exists \delta>0,
\forall x,
\cdots
\]

这通常直接暴露构造对象是 \(\delta\)。

---

## G4. 目标类型识别

识别当前属于：

- existence；
- uniqueness；
- equality；
- inequality；
- convergence；
- uniform control；
- compactness extraction；
- approximation；
- contradiction；
- representation。

这一步的目标不是自动选定定理，而是缩小后续结构搜索空间。

---

# 6. Stage O — Obstacle Diagnosis

M3 不能只有 Goal，还必须知道：

> **为什么现在不能直接完成 Goal？**

Obstacle 是候选构造的真正来源之一。

建议第一版至少识别以下障碍类型。

## O1. Representation Mismatch

目标的形式与已知工具不匹配。

例如：

固定点问题不能直接套零点定理。

---

## O2. Mixed Sources of Variation

一个表达式混合多个独立变化来源。

例如：

\[
f_n(x_n)-f(x)
\]

同时存在函数变化和输入变化。

---

## O3. Coefficient Depends on the Unknown Control Parameter

例如：

\[
(4+2\delta)\delta.
\]

希望控制 \(\delta\)，但系数本身仍依赖 \(\delta\)。

---

## O4. Local Information Cannot Yet Produce Global Conclusion

例如逐点连续性无法直接产生统一控制。

---

## O5. Existence Without Explicit Candidate

需要证明对象存在，但无法直接构造。

---

## O6. Infinite Complexity

存在无限多个条件，需要抽取、对角化、紧致性或统一化。

---

## O7. Lack of Sign / Monotonicity / Boundedness / Compactness

某个定理需要的结构尚未建立。

---

## O8. Quantifier Order Obstruction

例如希望：

\[
\exists N\ \forall x
\]

但现有信息只有：

\[
\forall x\ \exists N_x.
\]

这往往提示 uniformization / compactness 类型策略。

---

# 7. Stage I — Available Information Inventory

在生成候选前，系统必须显式登记：

> **我们现在到底有什么？**

建议分为四类：

## I1. Facts

已建立事实。

## I2. Structure

例如：

- continuity；
- boundedness；
- monotonicity；
- compactness；
- convexity；
- linearity。

## I3. Tools

可调用定理与证明模式。

## I4. Degrees of Freedom

当前有哪些东西可以自由选择？

例如：

- \(\delta\)；
- \(N\)；
- 子列；
- 辅助函数；
- 中间项；
- 分割点；
- 权重；
- 参数 \(\lambda\)。

**Degrees of Freedom 非常重要。**

很多构造不是凭空出现，而是因为证明中存在一个“可以自由选择的对象”，我们的任务是让它满足若干 Required Properties。

---

# 8. Stage R — Required Property Synthesis

这是 M3 Candidate Search Model 的核心。

系统不能从：

> “参考答案用了什么？”

生成构造。

而应从：

> “什么性质一旦成立，当前障碍就会消失？”

生成 Required Property。

形式上：

\[
\boxed{
R_t=\{r_1,r_2,\ldots,r_m\}
}
\]

其中每个 \(r_i\) 都必须可以追溯到：

- Goal；
- Obstacle；
- Available Fact；
- Theorem requirement；
- 已产生 constraint。

---

## 8.1 Required Property 的来源

### RP-G：Goal-derived

从目标直接反推。

例如需要零点：

> 希望构造一个函数，其零点与原目标等价。

---

### RP-O：Obstacle-derived

为了消除障碍。

例如混合两类变化：

> 需要一个桥接项把二者拆开。

---

### RP-T：Theorem-derived

为了让某个已知定理可使用。

例如想使用 IVT：

> 需要连续性 + 两端跨越目标值。

---

### RP-C：Constraint-derived

已有约束直接限制对象。

例如：

\[
0<\delta\le1,
\qquad
6\delta<\varepsilon.
\]

---

## 8.2 Required Property 必须早于候选具体形式

不允许：

```text
Required property:
the candidate should be exactly f(x_n).
```

这只是把答案重新命名。

合格写法是：

```text
Required properties:
1. A-B must be controllable by f_n -> f.
2. B-C must be controllable by continuity of f.
```

再由接口匹配得到：

\[
B=f(x_n).
\]

---

# 9. Stage F — Candidate Family Generation

定义：

\[
\mathcal F_t
=
\{C:\ C\text{ satisfies enough of }R_t\}.
\]

M3 的关键要求之一是：

> **Candidate Family 必须能够在不知道参考答案具体形式的情况下被描述。**

如果所谓候选族只是：

> “和参考答案长得类似的东西”，

则不合格。

---

# 10. Candidate Family 的推荐类型

第一版可以支持以下候选族。

## F1. Representation Transformations

目标等价改写产生的候选。

例如：

\[
f(c)=c
\rightarrow
f(c)-c=0.
\]

产生零点型辅助函数族。

---

## F2. Bridge Objects

寻找同时连接两个可控制关系的中间对象。

例如：

\[
f_n(x_n)	o f(x_n)	o f(x).
\]

---

## F3. Theorem-Enabling Objects

构造一个对象，使已有定理的前提能够被验证。

---

## F4. Parameterized Auxiliary Objects

不要直接猜最终函数，而先设：

\[
g=\mu f
\]

或：

\[
g=f+\lambda h.
\]

然后由 Required Property 解出参数或函数 \(\mu,\lambda\)。

这是防止“神奇构造后见解释”的重要技术。

---

## F5. Sufficient-Condition Families

不求最优解，只寻找容易满足的充分条件。

例如：

\[
(4+2\delta)\delta<\varepsilon
\]

转而要求：

\[
\delta\le r,
\]

先把 \(4+2\delta\) 控制成常数。

---

## F6. Extraction Families

- 子列；
- 极值点列；
- 最大项；
- 对角序列；
- 反例序列。

---

## F7. Localization / Decomposition Families

- 分区间；
- 截断；
- 分解误差；
- 分解集合；
- 局部化。

---

## F8. Comparison / Majorant Families

寻找更简单对象 \(M\)，使：

\[
|A|\le M
\]

而 \(M\) 已知可控制。

---

# 11. 候选生成允许使用的基本 Search Operators

未来 Engine 不应该依赖无限自由文本搜索，可以优先实现有限的一组操作符。

## OP1 `rewrite_goal`

把 Goal 改写成等价或更适合工具匹配的形式。

## OP2 `decompose`

将一个复杂量拆成多个可控制部分。

## OP3 `introduce_bridge`

寻找同时连接两个已知关系的中间对象。

## OP4 `backchain_theorem`

从某个定理的 conclusion / hypotheses 反向寻找所需结构。

## OP5 `parameterize_unknown`

先设未知辅助对象的一般形式，而非直接猜最终答案。

## OP6 `solve_required_property`

把“希望对象满足什么”转化成方程、不等式或结构要求，并求解。

## OP7 `relax_to_sufficient_condition`

放弃最优性，用更简单但足够的条件替代原条件。

## OP8 `bound_variable_coefficient`

先人为限制参数范围，使复杂系数变为固定上界。

## OP9 `match_known_pattern`

调用学习者已掌握的证明模式。

## OP10 `analogy_transfer`

从结构类似问题迁移候选族。

## OP11 `structured_trial`

在一个已经被 Required Property 限定的小候选族中进行试探。

## OP12 `reject_and_update`

根据失败原因更新 Obstacle 或 Constraint。

---

# 12. Stage C — Candidate Instantiation

有了候选族以后，才允许生成具体候选：

\[
C_1,C_2,\ldots,C_k\in\mathcal F_t.
\]

重要原则：

> M3 不要求一次命中参考答案。

允许：

- 多候选；
- 等价候选；
- 更丑候选；
- 更宽松候选；
- 最终未被参考答案采用的合法候选。

这正是减少 hindsight bias 的关键。

---

# 13. Stage T — Local Candidate Test

候选生成后，只进行**当前状态允许的局部测试**。

禁止使用后续证明整体成功作为候选合理性的唯一依据。

局部测试至少回答：

1. 是否满足 Required Properties？
2. 是否减少当前 Obstacle？
3. 是否引入当前无法满足的新条件？
4. 是否需要 learner 尚未拥有的工具？
5. 是否保留目标等价性或足够性？

候选测试结果建议使用：

```text
accepted
informative_rejection
neutral_rejection
valid_but_cumbersome
valid_but_too_strong
requires_unavailable_tool
```

而不是只有 success / fail。

---

# 14. Stage U — Search State Update

候选测试后，更新：

\[
S_t\rightarrow S_{t+1}.
\]

失败如果有价值，应产生至少一种变化：

- 新 Obstacle；
- 新 Constraint；
- 排除一个 Candidate Family；
- 缩小参数范围；
- 识别需要的新工具；
- 改变 Goal representation。

如果一个失败没有造成任何状态更新，它通常没有必要进入教学型 Search Path。

---

# 15. 四类候选的正式边界

用户要求重点区分：

- 自然候选；
- 经验候选；
- 逆向候选；
- 试探候选。

v0.3 不把它们看成互斥类别，而看成**候选来源标签**。

一个候选可以同时拥有多个标签。

---

# 16. N — Natural / Structural Candidate

定义：

> 候选的核心性质可以直接从 Goal、Obstacle 和 Available Information 中导出，并且候选与这些性质存在明显结构匹配。

形式上：

\[
S_t
\rightarrow
R_t
\rightarrow
\mathcal F_t
\]

过程中不需要调用参考答案。

典型情况：

### 例 1：固定点转零点

\[
f(c)=c
\iff
f(c)-c=0.
\]

因此：

\[
g=f-\operatorname{id}
\]

属于结构自然候选。

### 例 2：桥接项

若需要一个中间项同时连接：

\[
f_n(x_n)	o ?
\]

和：

\[
?\to f(x),
\]

而已有两个控制恰好分别作用于：

\[
f_n(x_n)-f(x_n)
\]

和：

\[
f(x_n)-f(x),
\]

则 \(f(x_n)\) 是结构自然候选。

---

# 17. “自然”不是“唯一”

Natural Candidate 只意味着：

> 它与当前结构存在低额外假设、低搜索距离的匹配。

不意味着：

- 唯一；
- 必然；
- 所有学生都应该立即想到；
- 作者历史上就是这样想到。

因此 ProofAtlas 应避免：

> “唯一自然的选择是……”

除非可以证明候选被接口条件唯一确定。

---

# 18. E — Experience / Pattern Candidate

定义：

> 候选不是由当前条件几乎直接逼出，而是来自已掌握的数学经验、模式库、类比或领域惯例。

例如：

- 看到有界序列想到“抽取收敛子列”；
- 看到两个误差源想到“加一项减一项”；
- 看到多个小量要求想到 \(\min\)；
- 看到积分中奇异点想到分区间；
- 看到线性一阶 ODE 想到积分因子。

经验候选是合法的数学发现方式。

但必须标明：

> 这是 repertoire-based heuristic，而不是当前题面逻辑必然推出。

---