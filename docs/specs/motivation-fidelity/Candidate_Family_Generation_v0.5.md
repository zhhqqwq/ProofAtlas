# ProofAtlas 核心规范 01.3：Required Property → Candidate Family 生成规范 v0.5

> 所属项目：ProofAtlas  
> 所属总规范：Motivation Fidelity Standard  
> 当前主题：M3 Candidate Search Model — Candidate Family Generation  
> 当前版本：v0.5  
> 状态：面向 Skill 可执行规则的规范化阶段  
> 本规范只解决：
>
> \[
> \boxed{\text{Required Property}\rightarrow\text{Candidate Family}}
> \]
>
> 不进入 Candidate Selection、Construction Archaeology 或 Cognitive Proof Graph 的正式设计。

---

# 0. 本规范要解决的问题

前一阶段已经要求 ProofAtlas 在生成具体构造之前，先得到 Required Property：

\[
R=\{R_1,R_2,\ldots,R_m\}.
\]

但这仍然存在第二层后见泄漏风险：

> 模型虽然没有直接写出参考答案，却把“候选族”定义成了参考答案的同义改写。

例如参考答案使用：

\[
g(x)=f(x)-x.
\]

一个伪 Candidate Family 可能写成：

> “考虑形如 \(f(x)-x\) 的辅助函数。”

这并没有真正产生“族”。

它只是把答案包了一层类别名称。

因此本规范的核心目标是：

> **给定已经独立生成的 Required Property，怎样得到一个由功能、对象类型和允许操作共同定义的搜索区域，使参考答案只是该区域中的一个候选，而不是候选族的定义来源。**

---

# 1. Candidate Family 的正式定义

ProofAtlas 中的 Candidate Family 不是“几个候选的列表”。

它是：

\[
\boxed{
\mathcal F
=
\{C:\; C\text{ satisfies a specified functional interface and structural constraints}\}
}
\]

更直观地说：

> **Candidate Family 是由“这个对象必须做什么”定义出的候选搜索空间，而不是由“参考答案长什么样”定义出的近邻集合。**

Candidate Family 至少应包含以下信息：

1. **object type**：要寻找的是什么类型对象；
2. **functional role**：它需要承担什么功能；
3. **required interfaces**：它必须同时连接哪些已有条件、工具或目标；
4. **admissible operations**：当前知识状态允许怎样构造它；
5. **invariants / constraints**：哪些性质必须保留；
6. **degrees of freedom**：哪些部分仍未决定；
7. **family boundary**：什么对象属于这个族，什么对象不属于；
8. **generation provenance**：这个族如何从 Required Property 得到。

---

# 2. 核心原则：Family Before Instance

必须执行：

\[
\boxed{\text{Family Before Instance}}
\]

即：

> 在生成具体候选对象之前，先生成候选族。

禁止流程：

\[
R
\rightarrow
C^\*
\rightarrow
\text{把 }C^\*\text{包装成“候选族”}.
\]

正确流程：

\[
R
\rightarrow
\mathcal F
\rightarrow
\{C_1,C_2,\ldots\}
\rightarrow
C^\*.
\]

其中：

\[
C^\*\in\mathcal F.
\]

这条规则是防止 Candidate Family 阶段答案泄漏的第一道硬门。

---

# 3. Candidate Family 不是“形式相似集合”

错误例子：

参考答案：

\[
g(x)=f(x)-x.
\]

伪候选族：

\[
g(x)=f(x)-\lambda x.
\]

如果引入 \(\lambda\) 只是为了让答案看起来像一个族，而不是由 Required Property 导出，那么这仍然是答案拟合。

真正合格的候选族应该先写成：

> 寻找一个辅助量 \(g\)，使：
>
> 1. \(g(c)=0\) 与原目标 \(f(c)=c\) 等价；
> 2. \(g\) 继承已有连续性；
> 3. 可以从题设得到 \(g\) 在某些点的符号信息；
> 4. 从而能够接入零点存在性定理。

然后才问：

> 哪些构造满足这些接口？

这样：

\[
g=f-\mathrm{id}
\]

才作为候选出现。

---

# 4. Candidate Family 的生成输入

Candidate Family Generator 不允许看到无限制的完整参考答案。

允许输入：

\[
S_t=(G_t,A_t,K_t,C_t,R_t)
\]

其中：

- \(G_t\)：当前目标；
- \(A_t\)：当前已经建立的事实；
- \(K_t\)：当前学习者允许调用的知识与操作；
- \(C_t\)：当前约束；
- \(R_t\)：已经通过 Required Property 审计的需求集合。

默认禁止输入：

- 最终参考构造的具体形式；
- 后续才出现的常数；
- 后续 lemma；
- 后续成功路线；
- 完整参考证明的未来部分。

---

# 5. Candidate Family 生成的主流程

推荐固定成：

\[
\boxed{
R
\rightarrow
Object\ Type
\rightarrow
Interface\ Signature
\rightarrow
Mechanism
\rightarrow
Family\ Template
\rightarrow
Family
}
\]

展开如下。

---

# 6. Step 1 — Object Type Inference

首先判断：

> 为满足 Required Property，我们需要寻找什么“类型”的数学对象？

候选对象类型至少包括：

### CF-OBJ-1 Auxiliary Function
辅助函数。

### CF-OBJ-2 Bridge Term
桥接项 / 中间项。

### CF-OBJ-3 Parameter / Threshold
\(\delta,N,M,r,\lambda\) 等参数。

### CF-OBJ-4 Subsequence / Extracted Object
子列、子网、子族、子结构。

### CF-OBJ-5 Auxiliary Sequence
辅助数列或函数列。

### CF-OBJ-6 Set / Neighborhood / Partition
集合、邻域、覆盖、分割。

### CF-OBJ-7 Extremal Object
上确界、下确界、极值点、最小反例等。

### CF-OBJ-8 Approximation Object
多项式、简单函数、截断函数、光滑逼近等。

### CF-OBJ-9 Witness / Counterexample Object
反证中的坏对象、见证对象。

### CF-OBJ-10 Transformation / Representation
变量替换、归一化、对数化、积分因子、坐标变换等。

### CF-OBJ-11 Decomposition
误差拆分、正负部、主项/余项、有限/尾部拆分等。

### CF-OBJ-12 Theorem-Input Object
为了满足某定理输入格式而专门构造的对象。

第一步只决定：

\[
\text{需要哪类对象}
\]

不能决定：

\[
\text{这个对象具体是什么}.
\]

---

# 7. Step 2 — Interface Signature

对候选对象建立“接口签名”：

\[
\Sigma(C)=
(\text{inputs},\text{outputs},\text{compatibilities},\text{constraints})
\]

也就是：

> 它必须和哪些已有信息发生连接？

例如桥接项 \(B\) 的接口可能是：

\[
A-B
\]

能够由条件 1 控制，

同时：

\[
B-C
\]

能够由条件 2 控制。

这时 Candidate Family 应先定义为：

\[
\mathcal F_{\text{bridge}}
=
\{B:
A-B\text{ 可由条件1控制，且 }B-C\text{ 可由条件2控制}\}.
\]

而不是直接写：

\[
B=f(x_n).
\]

---

# 8. Step 3 — Mechanism Identification

Required Property 通常不能直接告诉我们具体对象，但会暴露一个“机制”。

ProofAtlas 应优先识别以下机制。

## MCH-1 Goal Re-expression
把目标改写成已有理论擅长处理的形式。

例如：

\[
f(c)=c
\rightarrow
f(c)-c=0.
\]

---

## MCH-2 Interface Bridging
寻找一个对象同时连接两套已有控制。

例如：

\[
f_n(x_n)
\quad\text{与}\quad
f(x)
\]

之间加入桥接项。

---

## MCH-3 Error Decomposition
把不可控总误差拆成若干可控误差。

---

## MCH-4 Localization
通过限制变量进入一个局部区域，使系数、函数或其它对象变得可控。

---

## MCH-5 Uniformization
把依赖点的局部控制转化为统一控制。

---

## MCH-6 Extraction
从复杂/无限对象中提取具有稳定性质的子对象。

---

## MCH-7 Extremalization
通过上确界、极值、最小反例等构造边界对象。

---

## MCH-8 Approximation
用结构更好的对象逼近原对象。

---

## MCH-9 Normalization
消除尺度、平移、常数等非本质自由度。

---

## MCH-10 Cancellation
构造新对象，使不希望出现的项发生抵消。

---

## MCH-11 Theorem Input Matching
把当前问题转换成某个定理所需要的输入结构。

---

## MCH-12 Contradiction Witnessing
把某个统一结论的失败转化为可操作的坏对象序列/族。

机制是在“功能”和“具体形式”之间的中层表示。

---

# 9. Step 4 — Family Template Retrieval

只有识别出机制以后，才允许调用 Proof Pattern Library 中的 Family Template。

例如：

### Bridge Template

```text
Find B such that:
- left(A,B) matches control source 1;
- right(B,C) matches control source 2.
```

### Localization Parameter Template

```text
Choose r small enough that:
- local condition L(r) holds;
- remaining target reduces to a simpler controllable bound.
```

### Auxiliary Function Template

```text
Construct g from available objects so that:
- target condition is equivalent to a simple property of g;
- g inherits required regularity;
- known data provide sign/size/monotonicity information about g.
```

注意：

> Family Template 必须是跨题可复用的结构模板，而不是某一道题的答案模板。

---

# 10. Step 5 — Candidate Family Materialization

把 Template 与当前 proof state 结合，得到当前题目的候选族。

形式上：

\[
\mathcal F
=
T(R,S_t,K_t).
\]

例如：

### 桥接项问题

目标：

\[
|f_n(x_n)-f(x)|.
\]

Required Property：

- 第一段要能由 \(f_n\to f\) 控制；
- 第二段要能由 \(f\) 的连续性控制。

Candidate Family：

\[
\mathcal F
=
\left\{
B_n:
|f_n(x_n)-B_n|
\text{ 可由函数列收敛控制},
\;
|B_n-f(x)|
\text{ 可由连续性控制}
\right\}.
\]

此时还没有指定：

\[
B_n=f(x_n).
\]

只有进入 Candidate Selection 才能进一步选择。

---

# 11. Candidate Family 的“非单例原则”

默认情况下，一个合格 Candidate Family 不应被直接定义成单例：

\[
\mathcal F=\{C^\*\}.
\]

否则极易发生答案泄漏。

因此引入：

\[
\boxed{\text{Non-Singleton-by-Default Principle}}
\]

默认要求：

- family 中存在至少两个结构上可能的成员；
- 或包含尚未确定的参数；
- 或存在明确的自由度；
- 或是一个由性质定义的集合，而不是具体表达式。

---

# 12. 单例例外：Forced Candidate

有时 Required Property 确实会把候选唯一逼出。

例如某些线性方程匹配会给出唯一的系数。

这种情况下允许：

\[
|\mathcal F|=1.
\]

但必须提供：

\[
\boxed{\text{Uniqueness Derivation}}
\]

即证明：

> 不是因为参考答案就是这个，而是因为 Required Property 联立以后只允许这个候选。

如果无法给出 uniqueness derivation，则单例 family 应被判为高风险。

---

# 13. Candidate Family 的“功能不变性原则”

如果参考答案换成另一个等价合法证明，Candidate Family 不应发生根本变化。

定义：

\[
\boxed{\text{Functional Invariance}}
\]

若参考证明 \(P_1,P_2\) 采用不同具体构造，但承担同一功能，则由问题状态生成的 Candidate Family 应保持相近。

例如误差预算：

参考答案 1：

\[
\varepsilon/3,\varepsilon/3,\varepsilon/3.
\]

参考答案 2：

\[
\varepsilon/4,\varepsilon/4,\varepsilon/2.
\]

Candidate Family 应是：

> 所有满足各子误差预算之和不超过 \(\varepsilon\) 的正预算分配。

而不应绑定：

\[
\varepsilon/3.
\]

---

# 14. Candidate Family 的“语法不变性原则”

如果把参考答案进行等价代数变形：

\[
g=f-x
\]

改写成：

\[
g=-(x-f),
\]

Candidate Family 不应随语法变化。

因此族应以：

- 功能；
- 接口；
- 约束；
- 机制；

定义，而不是以字符串/符号形式定义。

---

# 15. Candidate Family Leakage 类型

Candidate Family 阶段新增以下泄漏类型。

## CFL-1 Exact-Form Family

候选族直接包含参考答案具体结构。

例如：

> “考虑 \(f(x)-x\) 型函数。”

如果该结构尚未由 Required Property 推出，则违规。

---

## CFL-2 Parameterized Answer Disguise

把答案加一个无意义参数伪装成族。

例如参考答案：

\[
f-x,
\]

伪族：

\[
f-\lambda x.
\]

如果 \(\lambda\) 没有来源，只是为了形成 family，属于泄漏。

---

## CFL-3 Answer-Centered Neighborhood

族被定义为“与参考答案相近”的形式：

> 对参考构造作小扰动。

这不是独立生成的搜索空间。

---

## CFL-4 Future-Mechanism Leakage

Candidate Family 使用了后面才发现的成功机制。

例如在尚未识别需要 cancellation 前，就生成“积分因子族”。

---

## CFL-5 Theorem-Name Leakage

因为参考答案最后使用某定理，候选族直接围绕该定理构造，但当前 proof state 尚未暴露该定理的 trigger。

---

# 16. Candidate Family Anti-Leakage Audit

每个 family 至少通过以下测试。

---

## Test CF-A — Reference Removal Test

完全删除参考构造。

只保留：

\[
S_t+R_t.
\]

检查 family 是否仍可生成。

若不能：

> 高泄漏风险。

---

## Test CF-B — Family Definition Deletion Test

把 family 中所有具体候选表达式删除。

检查剩余的功能描述是否足够定义搜索区域。

若不够：

> family 很可能依赖答案形式。

---

## Test CF-C — Alternative Instance Test

要求至少生成一个：

\[
C'\neq C^\*
\]

但仍满足 family definition 的候选，或者说明为什么不存在。

如果既不能给出替代项，也不能证明唯一性：

> family 可信度不足。

---

## Test CF-D — Counterfactual Reference Test

假设参考答案换成另一个合法构造。

检查当前 family 是否仍然合理。

若 family 只适配原答案：

> 说明它可能是答案中心化定义。

---

## Test CF-E — Parameter Provenance Test

任何 family 参数：

\[
\lambda,r,C,\alpha,\ldots
\]

都必须回答：

> 为什么这个自由度存在？

不能为了制造“族”而人工加入。

---

## Test CF-F — Mechanism Provenance Test

必须能够追踪：

\[
Required\ Property
\rightarrow
Mechanism
\rightarrow
Family.
\]

如果机制只来自后续参考答案，则失败。

---

# 17. Candidate Family Generation 的四种来源

为与前面的 Motivation 分类兼容，族生成可分为四类。

---

## CFG-N — Natural Structural Family

直接来自当前问题结构与 Required Property。

例如：

> 需要一个同时连接两套控制的中间对象。

这是最高优先级来源。

---

## CFG-H — Heuristic Family

来自已掌握的证明经验/模式库。

例如：

> 看到“有界但无收敛”，可以考虑子列提取类方法。

这种 family 合法，但必须标记：

\[
[\text{HEURISTIC}]
\]

而不能伪装成纯演绎结果。

---

## CFG-B — Backward Family

从目标或某定理输入格式反推需要怎样的对象。

例如：

> 若希望利用介值定理，就需要构造一个连续函数，其零点对应目标。

合法。

但必须标记：

\[
[\text{BACKWARD}]
\]

---

## CFG-P — Probe Family

用于探索的试探性 family。

例如：

> 尝试线性组合族；
> 尝试乘法变换族；
> 尝试局部截断族。

这种 family 不要求一开始就有强结构必然性，但必须具有合理搜索成本和明确检验标准。

---

# 18. 四类 Candidate Family 的边界

## Natural ≠ “常见”

“自然”必须来自当前 proof state 的结构。

不能因为某构造在教材中常见，就直接称 natural。

---

## Heuristic ≠ 猜答案

Heuristic 来自可陈述的模式：

> “遇到 X 结构，过去常用 Y 类方法。”

必须能说明这个模式。

---

## Backward ≠ Hindsight Leakage

从当前目标反推合法。

从参考答案反推不合法。

关键区别：

\[
\boxed{
\text{Backward from Goal}
\neq
\text{Backward from Answer}
}
\]

---

## Probe ≠ Random

试探族必须满足至少一项：

- 结构简单；
- 计算成本低；
- 能快速验证；
- 能揭示约束；
- 与当前机制存在弱联系。

纯随机对象不属于合格 Probe Family。

---

# 19. Candidate Family 优先级

默认搜索顺序建议：

\[
\boxed{
CFG\text{-}N
\rightarrow
CFG\text{-}B
\rightarrow
CFG\text{-}H
\rightarrow
CFG\text{-}P
}
\]

解释：

1. 优先从结构本身产生候选族；
2. 若不足，尝试目标反推；
3. 再调用已有模式经验；
4. 最后进行低成本试探。

但这不是绝对顺序。

不同数学领域可以调整。

---

# 20. Candidate Family 不应一次无限扩张

需要：

\[
\boxed{\text{Search Economy Principle}}
\]

Skill 不应该产生几十个候选族。

默认建议：

- 1 个主要 structural family；
- 最多 1–2 个备选 family；
- 若主要 family 已高度匹配 Required Property，不继续无意义扩展。

目标：

> 保留真实搜索感，而不是制造组合爆炸。

---

# 21. Family Coverage 与 Family Specificity

Candidate Family 存在一个重要张力。

太宽：

\[
\mathcal F=\{\text{所有函数}\}
\]

没有指导意义。

太窄：

\[
\mathcal F=\{f-x\}
\]

容易答案泄漏。

因此需要平衡：

\[
\boxed{\text{Coverage–Specificity Balance}}
\]

好的 family 应：

- 足够宽，保留真实自由度；
- 足够窄，由 Required Property 显著减少搜索空间。

---

# 22. Candidate Family 的最低信息量要求

一个 family 必须至少使搜索空间相比 object type 明显缩小。

例如：

> “找一个辅助函数”

不够。

但：

> “找一个由当前已有连续对象构成的辅助函数，使其零点等价于原目标，并继承连续性”

已经形成有意义的 family。

---

# 23. Candidate Family 信息压缩指标（概念性）

未来可以定义：

\[
\Delta H
=
H(\text{object space})
-
H(\mathcal F)