# ProofAtlas — M3 Search Protocol v1
## v0.3–v0.6 Integration Pass + Adversarial Test Report

> 所属项目：ProofAtlas  
> 所属核心规范：Motivation Fidelity Standard  
> 文档性质：第一部分集成规范 / Skill 实现前冻结候选  
> 版本：M3 Search Protocol v1.0-rc1  
> 上游规范：
>
> - M3 Candidate Search Model v0.3
> - Required Property Synthesis Specification v0.4
> - Candidate Family Generation Specification v0.5
> - Candidate Selection Specification v0.6
>
> 本文目标：
>
> 1. 将 v0.3–v0.6 压缩成一个真正可以写入 `SKILL.md` 的统一协议；
> 2. 删除重复 taxonomy，只保留直接影响 Skill 行为的规则；
> 3. 用 9 个典型分析证明做 adversarial test；
> 4. 根据测试暴露的问题修订协议；
> 5. 判断 Motivation Fidelity 第一部分是否已经达到“可开始实现 Skill”的状态。

---

# 1. M3 的最终任务定义

ProofAtlas 中的 M3 不是：

> 看到参考证明以后，给最终构造编一个合理故事。

M3 是：

> **冻结关键构造出现前的数学状态，在参考构造不参与搜索的情况下，从当前目标、障碍、可用事实、可用工具与学习者知识出发，先得到候选必须完成的功能，再建立候选族，再盲选少量候选并局部测试；只有这一过程冻结后，才允许与参考答案比较。**

核心链条：

\[
\boxed{
S_t
\rightarrow
G
\rightarrow
O
\rightarrow
I
\rightarrow
R
\rightarrow
\mathcal F
\rightarrow
P
\rightarrow
C
\rightarrow
T
\rightarrow
U
}
\]

其中：

- \(S_t\)：构造前冻结状态；
- \(G\)：Goal；
- \(O\)：Obstacle；
- \(I\)：Available Information；
- \(R\)：Required Property；
- \(\mathcal F\)：Candidate Family；
- \(P\)：Candidate Pool；
- \(C\)：Selected Candidate / co-preferred candidates；
- \(T\)：Local Test；
- \(U\)：Search State Update。

参考答案：

\[
C_{\mathrm{ref}}
\]

不属于以上搜索函数的输入。

只允许在搜索记录冻结以后进入：

\[
\boxed{\text{Reference Comparison}}
\]

---

# 2. M3 不要求复现参考答案

M3 的成功标准不是：

\[
C=C_{\mathrm{ref}}.
\]

而是：

\[
\boxed{
\text{得到与当前目标兼容、答案独立、可测试的功能候选路线}
}
\]

可能出现：

### Match

\[
C\equiv C_{\mathrm{ref}}.
\]

### Functional Match

具体形式不同，但承担相同功能。

### Alternative Valid Route

盲选路线与参考答案不同，但同样有效。

### Reference Unexplained

当前独立搜索无法合理恢复参考构造。

最后一种情况必须允许。

禁止为了“解释参考答案”而倒改搜索记录。

---

# 3. M3 的输入边界

每次处理一个重要构造前，建立：

\[
S_t=(G_t,O_t,A_t,K_t,C_t,P_u,H_t).
\]

## \(G_t\)：当前目标

不是整道题，而是当前真正要完成的局部目标。

## \(O_t\)：当前障碍

明确：

> 为什么当前已有信息不能直接完成目标？

## \(A_t\)：可用事实

只允许：

- 题设；
- 当前步骤之前已经证明的事实；
- 当前步骤之前合法推出的结论。

禁止未来 lemma。

## \(K_t\)：可用知识 / 工具

包括当前学习者允许使用的：

- 定义；
- 定理；
- 推论；
- 标准技巧；
- 合法计算工具。

## \(C_t\)：当前约束

已经明确产生的范围、接口、误差或参数要求。

## \(P_u\)：学习者模式库

已经掌握的证明模式。

## \(H_t\)：此前搜索历史

只记录结构化信息：

- 已尝试 family；
- 已尝试 candidate；
- 失败原因；
- 新增 obstacle / constraint / RP。

---

# 4. Reference Isolation

M3 的第一硬规则：

\[
\boxed{\text{Reference Answer Isolation}}
\]

在完成 Candidate Selection 冻结以前，搜索阶段不得使用：

- 参考构造的具体形式；
- 参考答案中的漂亮常数；
- 后续才出现的 lemma；
- 后续才暴露的成功优势；
- “因为标准答案用了 X”这一事实。

如果运行环境无法真正隐藏参考答案，则必须逻辑模拟隔离：

> 任何理由都必须能够标注为来自 \(S_t\)，而不能来自 reference。

---

# 5. Stage 0 — Freeze the Pre-Construction State

在解释关键构造之前先冻结：

```text
Current goal:
Current obstacle:
Available facts:
Available tools:
Current constraints:
Learner-available patterns:
Reference-specific information excluded:
```

如果无法确定构造前状态：

> 不得声称 M3。

可降级为 M1/M2。

---

# 6. Stage 1 — Normalize the Goal

允许进行不使用参考答案的目标处理：

### 等价改写

例如：

\[
f(c)=c
\iff
f(c)-c=0.
\]

### 目标拆分

把一个复合目标拆成若干子目标。

### 量词显式化

例如：

\[
\forall\varepsilon>0\ \exists\delta>0\ \cdots
\]

### 目标类型识别

例如：

- existence；
- inequality；
- convergence；
- zero finding；
- uniform control；
- compactness extraction；
- approximation。

Goal normalization 只能改变表示，不能偷偷引入最终构造。

---

# 7. Stage 2 — Diagnose the Obstacle

至少回答：

> 为什么当前不能直接完成目标？

常见 obstacle：

- representation mismatch；
- mixed sources of variation；
- unknown-dependent coefficient；
- local information cannot yet give global conclusion；
- existence without explicit witness；
- infinite complexity；
- missing sign / monotonicity / boundedness / compactness；
- quantifier-order obstruction；
- theorem interface mismatch。

如果没有明确 obstacle，后续 Required Property 极易变成答案改写。

---

# 8. Stage 3 — Inventory Available Information

必须区分：

### Facts
当前已经成立什么？

### Structures
连续、有界、单调、紧致、线性等。

### Tools
哪些定理现在合法可调用？

### Degrees of Freedom
现在到底允许“选”什么？

例如：

- 一个中间项；
- 一个辅助函数；
- 一个参数；
- 一个子列；
- 一组误差预算；
- 一个局部半径；
- 一个变换。

---

# 9. Stage 4 — Required Property Synthesis

核心原则：

\[
\boxed{\text{Functional Before Form}}
\]

先回答：

> 未知候选必须“做什么”？

而不是：

> 候选“长什么样”？

每条 RP 必须拥有 provenance：

- `RP-G`：Goal-derived；
- `RP-O`：Obstacle-derived；
- `RP-I`：Interface-derived；
- `RP-T`：Theorem-derived；
- `RP-C`：Constraint-derived；
- `RP-R`：Representation-derived。

并标记 necessity：

- `hard`
- `route_enabling`
- `simplifying`
- `preference`

---

# 10. Required Property Anti-Leakage Gate

每组 RP 至少满足：

### RP-G1 Provenance

每条性质都能指向 Goal / Obstacle / Interface / Tool / Constraint。

### RP-G2 Candidate-Agnostic

删除最终候选名称后仍有意义。

### RP-G3 Obstacle-Relevant

确实消除当前障碍。

### RP-G4 Necessity-Calibrated

方便条件不能伪装成必要条件。

### RP-G5 Answer-Masking Survival

隐藏答案后仍可提出。

### RP-G6 Family-Producing

能定义一个功能性搜索空间，而不是单纯重述参考答案。

如果失败：

> M3 不成立。

---

# 11. Required Property 停止条件

不要无限细化。

当 RP 已经：

1. 把 obstacle 转成可测试接口；
2. 明显缩小搜索空间；
3. 不依赖候选具体形式；
4. 再继续细化就开始等价于“直接解候选”；

立即停止，进入 Candidate Family。

---

# 12. Stage 5 — Candidate Family Generation

核心原则：

\[
\boxed{\text{Family Before Instance}}
\]

Candidate Family 是：

> **由功能接口、对象类型和合法机制定义的搜索区域。**

不是：

> 参考答案加一个参数。

---

# 13. Candidate Family 生成流程

按以下顺序：

\[
R
\rightarrow
\text{Object Type}
\rightarrow
\text{Interface Signature}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Family Template}
\rightarrow
\mathcal F
\]

## Object Type

例如：

- auxiliary function；
- bridge term；
- parameter / threshold；
- subsequence；
- auxiliary sequence；
- set / neighborhood / partition；
- extremal object；
- approximation object；
- contradiction witness；
- transformation；
- decomposition；
- theorem-input object。

## Mechanism

例如：

- goal re-expression；
- interface bridging；
- error decomposition；
- localization；
- uniformization；
- extraction；
- extremalization；
- approximation；
- normalization；
- cancellation；
- theorem input matching；
- contradiction witnessing。

---

# 14. Candidate Family 的最低要求

Family 必须：

1. 由 RP 和当前 state 产生；
2. 用功能定义，而不是答案语法定义；
3. 显著缩小搜索空间；
4. 默认保留真实自由度；
5. 对等价参考答案保持大体稳定；
6. 对等价语法保持大体稳定；
7. 参数必须有 provenance。

默认：

\[
|\mathcal F|>1.
\]

若 family 是单例，必须给出：

\[
\boxed{\text{Uniqueness Derivation}}
\]

证明是 RP 将其唯一逼出，而不是因为参考答案如此。

---

# 15. Candidate Family Anti-Leakage Gate

至少执行：

### CF-G1 Reference Removal
删除参考构造后 family 仍可生成。

### CF-G2 Functional Definition
删除所有具体实例后，family 定义仍完整。

### CF-G3 Alternative Instance
能给出另一成员，或证明单例唯一性。

### CF-G4 Counterfactual Reference
换一个合法参考证明，family 仍合理。

### CF-G5 Parameter Provenance
自由参数不是为了伪造“族”而添加。

### CF-G6 Mechanism Provenance
family 对应的 mechanism 在当前 state 中已经出现。

通过后：

\[
\boxed{\text{Freeze Family}}
\]

---

# 16. Stage 6 — Candidate Pool Generation

从冻结 family 中生成少量候选：

默认：

\[
2\le k\le5.
\]

候选来源必须标记：

- `natural`
- `heuristic`
- `backward`
- `probe`
- `uniqueness_forced`

类型可以重叠。

---

# 17. “自然候选”的可执行定义

禁止把“自然”当空洞评价。

只有候选具有以下至少一个明确来源时，才允许称为自然：

- 直接匹配多个 RP 接口；
- 主要复用已有对象；
- 引入新结构少；
- 是已识别 mechanism 的低复杂度实例；
- 可立即局部测试；
- 对当前 learner 可达。

更准确地记录：

```text
structural_fit:
extra_assumptions:
search_distance:
learner_pattern_available:
```

而不是使用神秘的 `naturalness = 0.87`。

---

# 18. Stage 7 — Candidate Hard Gates

每个候选先过硬门：

1. **Family Membership**
2. **Information Legality**
3. **Knowledge Legality**
4. **Hard RP Coverage**
5. **No Reference Dependency**
6. **Mathematical Well-formedness**

失败者直接淘汰。

---

# 19. Stage 8 — Candidate Comparison

通过硬门后，不使用单一总分。

采用：

\[
\boxed{
\text{Partial Order}
+
\text{Lexicographic Preferences}
}
\]

默认比较：

1. Hard / enabling RP coverage；
2. Tool access gain；
3. Structural economy；
4. Estimated proof cost；
5. Expected information gain；
6. Pedagogical value。

对于 Probe Candidate，可提高 information gain 权重。

---

# 20. 必须区分四种“简单”

不要把“最简单”写成一个词。

必须区分：

### Discovery Simplicity
事前容易想到。

### Proof Simplicity
采用后证明短。

### Expression Simplicity
最终表达漂亮。

### Pedagogical Simplicity
对当前学习者易懂。

后两者特别容易制造 hindsight bias。

---

# 21. Candidate Selection Outcome

允许：

- `preferred_candidate`
- `co_preferred_candidates`
- `probe_first`
- `forced_candidate`
- `underdetermined`

不得为了匹配参考答案强迫唯一排序。

---

# 22. Stage 9 — Freeze Selection

Candidate Selection 的 policy 与 outcome 必须在 reference comparison 之前冻结。

至少记录：

```text
shortlist:
selection criteria:
preferred / co-preferred:
selection reason:
reference visible: false
```

之后禁止：

> 因为参考答案不同，所以临时修改评价标准。

---

# 23. Stage 10 — Local Test

只进行当前候选的局部测试。

测试：

- 是否满足 RP；
- 是否让目标产生进展；
- 是否暴露新的可用 theorem interface；
- 是否引入隐藏条件；
- 是否造成不可接受 proof cost。

Local Test 不需要把整个证明全部完成。

---

# 24. Candidate 失败后的合法更新

失败只有在产生信息增益时才属于 Discovery Path。

最低形式：

\[
\boxed{
\text{Prior Justification}
+
\text{Local Test}
+
\text{Information Gain}
}
\]

失败至少产生一种：

- new obstacle；
- new constraint；
- new RP；
- family eliminated；
- parameter range reduced；
- tool mismatch；
- goal representation change。

否则属于噪声。

---

# 25. Search Result 分类

候选或路线可以标成：

- `incorrect`
- `insufficient`
- `too_strong`
- `valid_but_cumbersome`
- `valid_but_nontransparent`
- `requires_unavailable_tool`
- `accepted_discovery`
- `accepted_presentation`

特别重要：

\[
\boxed{
\text{accepted discovery}
\neq
\text{accepted presentation}
}
\]

一个路线可以最容易发现，但不是最终教材最漂亮的写法。

---

# 26. Stage 11 — State Update

若候选失败或部分成功：

\[
S_t\rightarrow S_{t+1}.
\]

新 state 可以加入：

- 新 obstacle；
- 新 constraint；
- 新 RP；
- 排除的 family；
- 候选失败原因。

然后允许再次执行局部 M3 search。

---

# 27. Nested M3 Search

Adversarial tests 表明，复杂分析证明往往不是一次搜索就得到整个证明。

因此 v1 正式加入：

\[
\boxed{\text{Nested M3 Search}}
\]

允许一个候选成功以后产生新的局部构造问题，再启动新的 M3 子搜索。

例如统一连续性极限定理中：

1. 先选择中间函数 \(f_N\)；
2. 再分配三个误差预算；
3. 再由 \(f_N\) 连续选择 \(\delta\)。

这三个选择不应该硬塞进同一个 Candidate Family。

每个子搜索都有独立的：

\[
S_t\rightarrow R\rightarrow\mathcal F\rightarrow C.
\]

---

# 28. Dependent Candidate Construction

Adversarial tests 还表明，有些 candidate 不是一次性公式，而是：

> 根据前一次选择继续递归地产生下一项。

典型：

- 子列；
- 嵌套区间；
- 对角线序列；
- 逐级 witness。

因此 Candidate 可以是：

\[
\boxed{\text{construction policy}}
\]

而不仅是静态数学对象。

例如：

```text
given previous index n_{k-1},
choose n_k > n_{k-1}
satisfying property P_k
```

只要每一步选择有当前信息支持，仍可达到 M3。

---

# 29. Existential Selection

若定理已经保证：

\[
\mathcal F\neq\varnothing,
\]

且目标不要求显式公式，可以：

> 任取 \(C\in\mathcal F\)。

不应为了“解释得具体”而虚构一个显式候选。

典型：

- 收敛子列；
- 有限子覆盖；
- 达到近似上确界的点。

---

# 30. Search Economy

M3 不认可暴力枚举。

优先：

\[
\text{semantic narrowing}
\rightarrow
\text{small family}
\rightarrow
\text{small shortlist}
\rightarrow
\text{local test}.
\]

不鼓励：

\[
\text{enumerate huge expression space}
\rightarrow
\text{hit answer}.
\]

默认预算：

- 主 family：1；
- 备选 family：最多 2；
- family 内候选：2–5；
- 若已有明确首选，不继续扩张。

---

# 31. Counterfactual / Memorization Audit

对于经典证明：

\[
\boxed{\text{Masked Recovery Alone Is Not Enough}}
\]

因为模型可能记住标准答案。

开发与 benchmark 阶段至少使用以下一种：

### Perturbation
改变常数、系数、目标形式。

### Isomorphic Novel Problem
保持结构，改变表面对象。

### Alternative Reference
换一个合法参考证明。

### Mechanism Evaluation
重点评估 RP / family / selection mechanism，而不是精确答案匹配。

---

# 32. Reference Comparison

只有 Selection Freeze 之后，才能查看参考答案。

分类：

- `reference_match`
- `family_match`
- `alternative_valid_route`
- `reference_superior_ex_post`
- `reference_unexplained`

如果参考答案只是在后续证明中表现更短：

> 标记为 ex-post advantage。

不能反过来说：

> 所以事前就“自然应该想到”。

---

# 33. M3 Eligibility Gate v1

只有下列核心 Gate 都通过，才允许把 Motivation 标成 M3。

### M3-1 Pre-answer snapshot
构造前状态可明确描述。

### M3-2 Obstacle explicit
当前困难明确。

### M3-3 RP independent
Required Property 通过 anti-paraphrase gate。

### M3-4 Family independent
Candidate Family 通过 anti-leakage gate。

### M3-5 Blind selection
候选生成与选择不使用 reference privilege。

### M3-6 Local test
候选接受当前状态下的局部测试。

### M3-7 Failure/update integrity
若有失败路线，其信息增益明确。

### M3-8 Counterfactual support
对经典/高记忆风险问题，至少有 perturbation / isomorphic / alternative-reference 支持之一；若没有，只能标记 `M3-provisional`。

### M3-9 Calibration
承认候选非唯一、路线非唯一、或无法重建时的真实不确定性。

---

# 34. M3 的降级

### M1
只能解释：

> why it works。

### M2
可以说明：

> 为什么该构造与当前结构相容，

但无法完成答案独立 family + selection。

### M3-provisional
完整搜索链成立，但经典题记忆风险尚未用反事实测试排除。

### M3
完整通过 M3 Eligibility Gate。

### M4 support
存在真实历史来源时单独记录。

M4 不覆盖 M3。

---
