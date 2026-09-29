# ProofAtlas 核心规范 01-B：Required Property Synthesis Specification v0.4

> 所属项目：ProofAtlas  
> 上位规范：Motivation Fidelity Standard v0.2；M3 Candidate Search Model v0.3  
> 文档性质：Skill 可执行规范 / Motivation Fidelity 子规范  
> 当前范围：只解决 **Required Property 如何自动生成，并防止它只是把参考答案换一种说法**  
> 明确不进入：Construction Archaeology 正式规则、Cognitive Proof Graph 正式数据结构  

---

## 0. 本规范要解决什么问题

M3 Candidate Search 的核心链条是：

\[
\text{Goal}
\rightarrow
\text{Obstacle}
\rightarrow
\text{Available Information}
\rightarrow
\boxed{\text{Required Property}}
\rightarrow
\text{Candidate Family}
\rightarrow
\text{Candidate Selection}.
\]

其中最危险的一环是 `Required Property`。

如果系统已经看到了参考答案，它非常容易生成下面这种伪分析：

> 最终答案取 \(B=f(x_n)\)，所以我们需要一个“等于 \(f(x_n)\)”的中间项。

或者：

> 最终答案取 \(\delta\le 1\)，所以我们需要性质 \(\delta\le 1\)。

这种写法虽然形式上拥有一个 `Required Property` 字段，但并没有真正完成候选生成。它只是：

\[
\boxed{\text{Answer}\rightarrow\text{Paraphrased Answer}}
\]

ProofAtlas 必须阻止这种退化。

本规范的任务是定义：

> **什么样的 Required Property 才能被认为是在不知道候选具体形式时，从 Goal、Obstacle、Available Information 与合法工具中独立产生的。**

---

# 1. Required Property 的正式定义

设当前冻结的搜索状态为：

\[
S_t=(G_t,O_t,A_t,K_t,C_t,P_u,H_t),
\]

其中：

- \(G_t\)：当前目标；
- \(O_t\)：当前障碍；
- \(A_t\)：构造前已经可用的数学事实；
- \(K_t\)：允许使用的知识、定理与技术；
- \(C_t\)：已产生的约束；
- \(P_u\)：学习者已经掌握的模式；
- \(H_t\)：此前合法搜索历史。

假设当前存在一个尚未确定的自由对象：

\[
X\in\mathcal X.
\]

这个对象可能是：

- 中间项；
- 辅助函数；
- \(\delta\)、\(N\)、\(M\)；
- 子列；
- 分割点；
- 权重；
- 参数；
- 集合；
- 新表示方式。

则一个 **Required Property** 是施加在 \(X\) 或当前 proof state 上的谓词/约束：

\[
r(X;S_t),
\]

并且满足：

> 如果某个候选 \(X\) 满足这一性质，它就会消除至少一个已经明确识别的障碍、完成一个明确子目标、满足一个合法工具的输入接口，或使搜索空间产生可解释的缩减。

因此 Required Property 描述的是：

\[
\boxed{\text{候选必须“做什么”}}
\]

而不是：

\[
\boxed{\text{候选“长什么样”}}
\]

这是本规范最重要的区分。

---

# 2. Functional Before Form 原则

Required Property 必须尽量采用**功能语言**而不是**答案形式语言**。

例如目标是控制：

\[
|f_n(x_n)-f(x)|.
\]

不合格：

> 找一个中间项 \(B=f(x_n)\)。

合格：

> 找一个中间量 \(B\)，使：
>
> 1. \(|f_n(x_n)-B|\) 能由已知的 \(f_n\to f\) 控制；
> 2. \(|B-f(x)|\) 能由 \(x_n\to x\) 与 \(f\) 的连续性控制。

前者描述答案。

后者描述接口。

因此规定：

\[
\boxed{\text{Interface First, Representation Later}}
\]

---

# 3. Required Property 与“真正必要”必须区分

`Required Property` 这个名称容易让模型把所有后续选择都说成“必须”。

因此 ProofAtlas 内部必须进一步区分四个层级。

## RP-H：Hard Requirement

不满足该条件，当前路线无法成立。

例如桥接项 \(B\) 必须使两个误差项分别进入已有控制机制。

---

## RP-E：Enabling Requirement

不是逻辑上唯一必要，但为了启用当前选择的工具或策略必须满足。

例如若决定调用介值定理，则需要构造连续函数并建立跨越目标值的条件。

这属于：

> **route-relative necessity**。

---

## RP-S：Simplifying Requirement

为了把复杂条件化成容易操作的充分条件而主动加入。

例如：

\[
(4+2\delta)\delta<\varepsilon
\]

中主动要求：

\[
\delta\le 1.
\]

它不是原目标逻辑上必须要求的，而是一种简化策略。

---

## RP-P：Preference

不是 required property，而只是候选选择偏好：

- 简单；
- 对称；
- 易计算；
- 符合标准写法；
- 常数漂亮；
- 易于教学。

例如在三个误差项中取：

\[
\varepsilon/3,\varepsilon/3,\varepsilon/3
\]

通常首先属于方便偏好，而不是数学必须。

### 强制规则

ProofAtlas 不得把 `RP-S` 或 `RP-P` 错报成 `RP-H`。

这直接防止：

> “因为答案取了 1，所以 \(\delta\le1\) 是必要条件。”

这种后见式过度解释。

---

# 4. Required Property 的六类来源

每个 Required Property 必须至少拥有一个合法 provenance。

## RP-G：Goal-derived

从当前目标的逻辑形式直接反推。

例如：

\[
f(c)=c
\iff
f(c)-c=0.
\]

由此产生：

> 需要一个对象，其零点与原固定点目标等价。

---

## RP-O：Obstacle-derived

为消除已明确识别的障碍而产生。

例如：

> 一个差中混合了函数变化与输入变化。

产生：

> 需要把两种变化拆成可分别控制的部分。

---

## RP-I：Interface-derived

这是 v0.4 新增且建议作为最重要类型之一。

现有事实或工具只对某种“输入接口”起作用，于是新对象需要和这些接口兼容。

例如：

- \(f_n\to f\) 控制的是 \(f_n(y)-f(y)\)；
- \(f\) 连续控制的是 \(f(y)-f(x)\)。

因此桥接对象应同时能够进入这两个接口。

这会自然逼近：

\[
y=x_n,
\qquad
B=f(x_n).
\]

`RP-I` 特别适合解释分析中的桥接项、辅助函数和中间对象。

---

## RP-T：Theorem-derived

如果某个定理已经由当前结构合法触发，则可以反向读取其输入要求。

例如希望使用介值定理，则产生：

- 连续性；
- 跨越目标值。

注意：

> `RP-T` 只有在定理本身是从当前结构合法进入候选工具集之后才允许产生。

禁止先看到参考答案使用 IVT，再倒推“我们需要 IVT 的条件”。

否则属于 theorem fixation / answer leakage。

---

## RP-C：Constraint-derived

来自已经建立的数学约束。

例如同时需要：

\[
\delta<r,
\qquad
C\delta<\varepsilon.
\]

这些是直接限制自由参数的 Required Properties。

---

## RP-R：Representation-derived

通过合法的目标重写，产生新的结构要求。

例如：

\[
f(c)=c
\]

重写成：

\[
f(c)-c=0.
\]

这时不是直接说“构造 \(f-x\)”；而是先产生：

> 需要一个零点条件与原目标等价的表示。

---

# 5. Required Property 自动生成算法 v0.4

建议 Skill/Agent 按以下顺序执行。

---

## Step R0 — Freeze the State

在生成 Required Property 之前冻结：

```text
current_goal
known_facts
available_tools
current_constraints
learner_patterns
search_history
```

同时遮蔽：

```text
reference_candidate
later_steps
polished_constants
later_lemmas
```

若无法真正技术遮蔽，也必须在逻辑上将这些信息标记为：

```text
FORBIDDEN_FOR_GENERATION
```

---

## Step R1 — Normalize the Goal

把目标写成当前可工作的数学义务。

例如不要停在：

> 证明极限成立。

而转换为：

> 对任意 \(\varepsilon>0\)，需要找到一个控制参数，使最终误差小于 \(\varepsilon\)。

或者：

> 需要证明存在某个 \(c\) 满足 \(f(c)=c\)。

但 Goal normalization 不能提前包含最终构造。

---

## Step R2 — State the Obstacle

必须用**失败接口**描述当前为什么卡住。

例如：

> 当前目标中的一个表达式同时包含两个不同变化来源，而已有假设分别只能控制其中一种。

而不是：

> 当前缺少 \(f(x_n)\)。

后者已经泄漏候选。

---

## Step R3 — Identify Degrees of Freedom

问：

> 当前有哪些对象是可以主动选择的？

例如：

- 中间项 \(B\)；
- 辅助函数 \(g\)；
- \(\delta\)；
- 子列 \((x_{n_k})\)；
- 分割点 \(a\)；
- 参数 \(\lambda\)。

如果没有自由对象，就不应该强行制造 Construction-style Required Property。

---

## Step R4 — Derive Minimal Functional Requirements

对每个自由对象问：

> **这个对象至少需要完成什么功能，才能让当前障碍减少？**

使用模板：

```text
We need an object X such that ...
```

但省略任何参考答案中的具体表达式。

例如：

```text
We need B such that:
- the first difference matches convergence information;
- the second difference matches continuity information.
```

---

## Step R5 — Attach Provenance

每条 Required Property 必须标记：

```text
RP-G / RP-O / RP-I / RP-T / RP-C / RP-R
```

以及它来自哪一个具体 Goal、Obstacle、Fact 或 Tool。

没有 provenance 的 property 不能进入 M3 核心集合。

---

## Step R6 — Calibrate Necessity

将每条 property 标记为：

```text
hard
route_enabling
simplifying
preference
```

防止把参考答案中的方便设计误称为必要条件。

---

## Step R7 — Candidate-Agnostic Rewrite

尝试删除所有具体候选名称、特殊常数和最终表达式。

例如：

原句：

> 需要 \(B=f(x_n)\)，使两边可控。

改写：

> 需要一个中间量，使左段能进入函数列收敛的控制接口，右段能进入 \(f\) 连续性的控制接口。

如果删掉候选名称后 property 失去意义，则高度怀疑它只是 answer paraphrase。

---

## Step R8 — Minimality Reduction

检查 property 是否包含比解决当前障碍更多的信息。

例如只需要：

> \(g\) 的零点等价于原目标。

却生成：

> \(g(x)=f(x)-x\)、连续、端点异号、且只有一个零点。

这已经把未来证明和候选形式一起塞进 Required Property。

应拆成多个阶段，并删除尚未必要的信息。

---

## Step R9 — Candidate Family Test

真正合格的 Required Property 应该能定义一个**候选集合**，而不是只留下一个字面答案。

形式上：

\[
\mathcal F_R
=
\{X\in\mathcal X: r_1(X),\ldots,r_m(X)\}.
\]

如果：

\[
|\mathcal F_R|=1
\]

并且唯一元素恰好是参考答案，系统必须额外审计：

> 这是数学结构真正唯一逼出的，还是 property 已经过度具体？

唯一候选不是自动违规，但属于高风险状态。

---

## Step R10 — Only Then Generate Candidates

只有 Required Property 集合通过前面检查后，才能进入：

\[
R_t\rightarrow\mathcal F_t\rightarrow C_1,C_2,\ldots
\]

也就是说：


timestamp(`required_properties`) < timestamp(`concrete_candidate_generation`)

应成为概念上的硬规则。

---

# 6. Anti-Paraphrase Audit：防止“答案换一种说法”

这是本规范的核心审计部分。

---

## AP-1 Candidate Name Deletion Test

删除所有候选的名称和具体表达式。

问题：

> 剩余 property 是否仍然能够独立表达？

若否：

```text
status = answer_paraphrase_risk
```

---

## AP-2 Form-to-Function Test

检查 property 描述的是：

### Form

> “取指数函数乘子”；

还是：

### Function

> “寻找一个乘子，使原表达式能够合并成一个乘积导数”。

M3 Required Property 优先要求 Function 层。

---

## AP-3 Substitute Candidate Test

尝试寻找另一个不等于参考答案、但满足 property 的候选。

如果存在：

> 说明 property 很可能确实描述的是功能。

如果不存在：

> 不一定违规，但必须进入唯一性审计。

---

## AP-4 Reference Answer Removal Test

从上下文中完全删除参考候选。

仅给：

- Goal；
- Obstacle；
- Available facts；
- Allowed tools。

重新生成 Required Property。

如果核心 property 在语义上保持稳定，则支持独立性。

如果 property 完全改变，说明原分析可能强依赖答案。

---

## AP-5 Counterfactual Candidate Test

人为替换参考答案为另一个同样合法的候选。

真正功能性的 Required Property 应仍然基本成立。

例如误差预算从：

\[
\varepsilon/3,\varepsilon/3,\varepsilon/3
\]

换成：

\[
\varepsilon/4,\varepsilon/4,\varepsilon/2.
\]

Required Property 应仍是：

> 各误差预算总和不超过 \(\varepsilon\)。

如果 property 变成：

> 每项必须小于 \(\varepsilon/3\)，

则暴露了 answer-specific overfitting。

---

## AP-6 Syntax Invariance Test

把参考答案作等价代数改写。

如果 Required Property 随答案表面形式大幅变化，说明系统可能在模仿 syntax，而不是抓 mechanism。

---

## AP-7 Perturbation Test

轻微改变题目参数、常数或符号，但保持证明机制不变。

高质量 Required Property 应随数学结构变化，而不是死守原答案数字。

例如：

\[
(4+2\delta)\delta<\varepsilon
\]

改成：

\[
(5+3\delta)\delta<\varepsilon.
\]

Required Property 应仍能产生：

> 先给 \(\delta\) 一个简单上界，使系数被固定常数控制。

而不是继续机械地产生 \(\delta\le1, 6\delta<\varepsilon\)。

---

# 7. Required Property 的七项合格标准

一组 Required Properties 若要进入 M3，至少应满足以下标准。

## Q1 — Source Grounded

每条性质都能追溯到冻结状态中的合法来源。

---

## Q2 — Candidate Agnostic

无需写出参考候选，也能独立表达。

---

## Q3 — Obstacle Relevant

至少消除一个明确障碍或推进一个明确子目标。

---

## Q4 — Testable

可以判断某个候选是否满足它。

例如：

> “这个构造应该很巧妙。”

不是 property。

---

## Q5 — Minimal Enough

不提前塞入未来步骤、漂亮形式或不必要性质。

---

## Q6 — Necessity Calibrated

明确：hard / route-enabling / simplifying / preference。

---

## Q7 — Family Producing

能够帮助限定一个功能候选族，而不是直接重命名唯一答案。

---

# 8. Required Property 的失败状态

Skill 不应该强行输出合格结果。

建议允许：

```text
VALID
TOO_SPECIFIC
ANSWER_PARAPHRASE
UNSUPPORTED
OVERCONSTRAINED
UNDERDETERMINED
POST_HOC
THEOREM_FIXATED
LEARNER_ILLEGAL
```

含义：

## TOO_SPECIFIC

性质包含不必要的具体形式。

## ANSWER_PARAPHRASE

基本只是参考答案改写。

## UNSUPPORTED

找不到合法 provenance。

## OVERCONSTRAINED

加入了过多未来条件，把候选族人为压缩成参考答案。

## UNDERDETERMINED

性质太弱，无法形成有意义的候选族。

## POST_HOC

只能解释答案为何成功，不能从构造前状态产生。

## THEOREM_FIXATED

先锁定参考答案使用的定理，再硬凑输入条件。

## LEARNER_ILLEGAL

依赖学习者当前没有的工具或模式。

---

# 9. Obstacle → Required Property 的生成模板

为了可编码，第一版 Skill 可使用以下有限模板。

---

## Template A — Mixed Sources of Variation

Obstacle：

> 一个目标表达式混合多个变化来源，而已有工具分别只控制其中一部分。

Generate：

> 需要引入中间表示，使每一部分分别匹配一个已有控制接口。

典型模式：桥接项、加一项减一项、误差分解。

---

## Template B — Target Has Wrong Representation

Obstacle：

> 当前目标形式无法直接匹配已知工具。

Generate：

> 需要一个与原目标等价、但具有可调用工具所需结构的新表示。

典型模式：固定点转零点、等式转符号、积分转导数等。

---

## Template C — Coefficient Depends on Free Parameter

Obstacle：

> 希望控制一个小参数，但它同时出现在系数中，使条件难以直接解。

Generate：

> 需要先给自由参数增加一个简单局部上界，使相关系数被一个固定常数控制。

典型模式：\(\delta\le 1\)、局部有界化。

---

## Template D — Need Existence from Sequential Data

Obstacle：

> 有无限对象，但缺少稳定/收敛结构。

Generate：

> 需要从当前对象中抽取具有所需稳定性质的子结构。

可能进入：子列、紧致性、单调子列等候选族。

---

## Template E — Want to Apply a Legitimately Triggered Theorem

Obstacle：

> 某定理能够完成当前子目标，但缺少其一个或多个输入条件。

Generate：

> 新对象或前置步骤需要补齐这些输入条件。

重要：定理必须先通过 theorem-trigger 合法性检查。

---

## Template F — Multiple Simultaneous Bounds

Obstacle：

> 同一个自由参数必须同时满足多项条件。

Generate：

> 需要构造一个选择规则，使全部约束同时成立。

典型模式：min / max，但 property 本身先表达“同时满足”，不能直接预写 `min` 或 `max`。

---

# 10. 示例一：桥接项 \(f(x_n)\)

已知：

\[
f_n\to f,
\qquad
x_n\to x,
\qquad
f\text{ 连续}.
\]

目标：

\[
f_n(x_n)\to f(x).
\]

## Freeze State

可用控制接口：

\[
f_n(y)-f(y),
\]

以及：

\[
f(y)-f(x).
\]

## Obstacle

目标差：

\[
f_n(x_n)-f(x)
\]

同时改变函数索引和输入点。

## Bad Required Property

> 需要加入 \(f(x_n)\)。

这是答案重述。

## Good Required Properties

令未知桥接项为 \(B_n\)。

需要：

1. \(f_n(x_n)-B_n\) 能进入 \(f_n\to f\) 的控制接口；
2. \(B_n-f(x)\) 能进入 \(f\) 连续性的控制接口。

这两个性质在不知道答案时就能表达。

## Candidate Family

寻找同时与：

\[
f_n(x_n)
\]

和

\[
f(x)
\]

通过现有控制关系相连的中间量。

得到自然候选：

\[
B_n=f(x_n).
\]

因此这里的 Required Property 通过独立性测试。

---

# 11. 示例二：\(\delta=\min\{1,\varepsilon/6\}\)

已有条件：

\[
(4+2\delta)\delta<\varepsilon.
\]

## Obstacle

需要控制 \(\delta\)，但系数：

\[
4+2\delta
\]

仍依赖 \(\delta\)。