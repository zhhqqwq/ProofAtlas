# ProofAtlas 核心规范 01.4：Candidate Family → Candidate Selection 规范 v0.6

> 所属项目：ProofAtlas  
> 所属总规范：Motivation Fidelity Standard  
> 当前主题：M3 Candidate Search Model — Candidate Selection  
> 当前版本：v0.6  
> 状态：面向 Skill 可执行规则的规范化阶段  
> 本规范只解决：
>
> \[
> \boxed{\text{Candidate Family}\rightarrow\text{Candidate Selection}}
> \]
>
> 即：在 Candidate Family 已经独立、合法、冻结之后，Skill 如何生成少量具体候选、比较候选、选择或保留候选，并解释“为什么先试这个”，同时避免在这一阶段重新向参考答案泄漏。

---

# 0. 本规范要解决的问题

前一阶段已经完成：

\[
\text{Required Property}
\rightarrow
\text{Candidate Family}.
\]

但即使 Candidate Family 完全独立于参考答案，仍然存在第三层后见偏置：

> 模型可能在族内直接挑中参考答案，然后事后说它“最自然”“最简单”“最优”。

例如已经得到候选族：

\[
\mathcal F
=
\left\{
B_n:
A_n-B_n\text{ 可由条件 1 控制，}
B_n-C\text{ 可由条件 2 控制}
\right\}.
\]

参考答案选：

\[
B_n=f(x_n).
\]

一个未经约束的模型可能直接说：

> “显然最自然的是 \(f(x_n)\)。”

但“显然”并没有说明：

1. 族内还有哪些候选；
2. \(f(x_n)\) 为什么优先；
3. 它是唯一合理候选还是只是一个低成本候选；
4. 这个判断是否来自参考答案本身。

因此 Candidate Selection 必须成为独立、可审计的步骤。

---

# 1. Candidate Selection 的核心目标

Candidate Selection 不是：

\[
\boxed{\text{猜中参考答案}}
\]

而是：

\[
\boxed{
\text{从冻结的 Candidate Family 中，依据当前 proof state 独立产生少量高价值候选，并用答案无关的理由决定：优先尝试、并列保留、暂缓或淘汰。}
}
\]

参考答案的候选：

\[
C_{\mathrm{ref}}
\]

在这一阶段只应拥有普通候选身份。

它不能因为“出现在答案里”而获得额外优先级。

---

# 2. 第一原则：Reference Answer Is Not the Objective

必须锁定：

\[
\boxed{\text{Reference Answer Is Evidence, Not Objective}}
\]

ProofAtlas 的目标不是最大化：

\[
\Pr(C=C_{\mathrm{ref}}).
\]

而应最大化：

\[
\Pr(
C\text{ 是当前状态下合理、可操作、低成本且有学习价值的下一步}
).
\]

因此允许出现：

> ProofAtlas 的首选候选与参考答案不同，但一样合法、甚至更自然。

这种情况不应被视为系统失败。

相反，它可以成为极有价值的教学内容：

> “参考答案采用 A；从当前状态出发，B 也是一个非常自然的选择。两条路线的差异在于……”

---

# 3. 第二原则：Selection Before Reference Inspection

Candidate Family 已冻结后，进入 Candidate Selection。

推荐执行：

\[
\boxed{\text{Blind Selection First}}
\]

即在查看参考答案具体候选之前：

1. 从 family 内生成候选池；
2. 完成候选初筛；
3. 形成首选/并列首选；
4. 冻结 Selection Record；
5. 最后才与参考答案比较。

正确流程：

\[
\mathcal F
\rightarrow
P
\rightarrow
E
\rightarrow
S
\rightarrow
\text{freeze}
\rightarrow
C_{\mathrm{ref}}\text{ comparison}.
\]

其中：

- \(P\)：candidate pool；
- \(E\)：candidate evaluation；
- \(S\)：selection result。

---

# 4. Candidate Selection 不等于 Candidate Generation

必须区分两个动作。

## Candidate Generation

问题：

> Candidate Family 中有哪些值得实际检查的实例？

输出：

\[
P=\{C_1,C_2,\ldots,C_k\}.
\]

## Candidate Selection

问题：

> 这些候选中，当前最值得先尝试哪些？

输出可以是：

- 单个优先候选；
- 多个并列候选；
- 一个候选 + 一个备选；
- 暂无足够依据选优。

因此：

\[
\boxed{
\text{Generate}
\neq
\text{Select}
}
\]

---

# 5. Candidate Pool 的大小

不能：

- 只生成参考答案一个；
- 也不能产生几十个候选制造噪声。

默认建议：

\[
2\le k\le5
\]

对于结构非常明确的问题，可以：

\[
k=1
\]

但必须已有 uniqueness derivation 或非常强的 structural forcing。

对于探索性问题，可以：

\[
k\le7
\]

但只有在候选差异确实有教学价值时。

---

# 6. Candidate Pool 的来源

Candidate Pool 中的候选应至少来自以下一种明确来源。

---

## CP-N — Structurally Direct Candidate

直接由 Required Property 与 family interface 的最简单实例化得到。

例如：

> 需要一个对象同时匹配两个接口。

优先检查最直接复用已有对象的实例。

---

## CP-H — Heuristic Candidate

由已知 proof pattern 提供。

例如：

- 加减中间项；
- 取平均；
- 取最值；
- 取子列；
- 归一化；
- 截断。

必须标记经验来源。

---

## CP-B — Backward Candidate

从目标或定理输入反推得到。

合法前提：

\[
\text{backward from goal/tool interface}
\]

而不是：

\[
\text{backward from reference answer}.
\]

---

## CP-P — Probe Candidate

用于低成本试探。

特点：

- 简单；
- 易计算；
- 易验证；
- 即使失败也能提供信息。

---

## CP-U — Uniqueness-Forced Candidate

由接口方程、系数匹配或约束联立唯一逼出。

这种候选不需要与其它对象竞争，但需要保存 uniqueness derivation。

---

# 7. “自然候选”的正式定义

ProofAtlas 禁止将“自然”作为未解释形容词。

一个候选 \(C\) 的自然性必须相对于：

\[
(S_t,R,\mathcal F,K_u)
\]

定义。

也就是说：

\[
\boxed{
Naturalness(C)
=
Naturalness(C\mid S_t,R,\mathcal F,K_u)
}
\]

不是候选自身的绝对属性。

---

# 8. Natural Candidate 的六个来源

一个候选可以因为以下原因被称为“自然候选”。

## N1 — Direct Interface Match

它直接匹配 Required Property 中的多个接口。

---

## N2 — Reuse of Existing Objects

它主要由当前 proof state 已经存在的对象组成，不额外引入复杂结构。

---

## N3 — Minimal New Structure

它引入的新定义、参数、定理或复杂度较少。

---

## N4 — Standard Mechanism Realization

它是已识别机制的标准、低复杂度实例。

例如：

> 误差拆分机制下优先考虑已有量作为桥接点。

---

## N5 — Immediate Testability

它可以立即代入检查，而不需要长链推导。

---

## N6 — Learner Accessibility

它只使用学习者当前掌握的概念和操作。

只有能够明确指出一项或多项来源时，才允许写：

> “这是一个自然候选。”

否则只能写：

> “这是一个可能的候选。”

---

# 9. 自然 ≠ 最优

候选可能：

- 最自然但不最短；
- 最短但不最自然；
- 最强但证明成本最高；
- 最适合教材表达但发现难度较高。

因此严禁把：

\[
\text{natural}
\]

自动等同于：

\[
\text{best}.
\]

---

# 10. 四类“候选优点”必须分开

每个候选至少要区分：

### Discovery Simplicity
是否容易从当前状态想到。

### Proof Simplicity
采用它后证明是否短。

### Expression Simplicity
最终公式是否漂亮。

### Pedagogical Simplicity
是否容易让当前学习者理解。

这四者可能不一致。

---

# 11. 一个典型冲突

某个参考答案可能选择：

\[
C_{\mathrm{ref}}
\]

因为它让最终证明只有 3 行。

但另一个候选：

\[
C'
\]

虽然最终证明长 8 行，却可以更直接从当前 Required Property 推出。

那么：

\[
C'
\]

可能拥有更高的：

\[
\text{Discovery Simplicity}
\]

而：

\[
C_{\mathrm{ref}}
\]

拥有更高的：

\[
\text{Proof Compression}.
\]

ProofAtlas 应明确说明这种差异，而不是强行把参考答案包装成“最自然”。

---

# 12. Selection Criteria：先硬门，再偏好

本规范不建议对所有属性进行一个总分加权。

推荐：

\[
\boxed{\text{Hard Gates}+\text{Partial Order}+\text{Lexicographic Preferences}}
\]

原因：

> 数学候选的不同优点通常不可用一个可靠的线性分数统一。

---

# 13. Stage A — Hard Validity Gates

候选必须先通过硬门。

---

## GATE-1 Family Membership

候选确实属于冻结 family。

---

## GATE-2 Information Legality

候选生成只使用当前可用信息。

---

## GATE-3 Knowledge Legality

不依赖学习者尚未拥有的工具，除非明确作为高级路线。

---

## GATE-4 Required Property Coverage

候选至少满足核心 Hard Requirements。

---

## GATE-5 No Reference Dependency

候选不能因为参考答案形式而被生成。

---

## GATE-6 Mathematical Well-formedness

表达式、对象、域等必须合法。

任何硬门失败：

\[
C\rightarrow\text{reject}.
\]

---

# 14. Stage B — Functional Coverage

通过硬门后，首先比较：

\[
\boxed{\text{Requirement Coverage}}
\]

候选满足多少关键接口？

特别区分：

- Hard Requirement；
- Route-Enabling Requirement；
- Simplifying Requirement；
- Preference。

优先规则：

> 完整覆盖 Hard Requirements 的候选优先于只部分覆盖者。

---

# 15. Stage C — Tool Accessibility

接下来问：

> 采用这个候选后，是否立即让已有条件或定理变得可用？

定义：

\[
\boxed{\text{Tool Access Gain}}
\]

例如某个辅助函数一旦构造，便直接暴露：

- 连续性；
- 单调性；
- 零点；
- 紧致性；
- 某个已知估计。

这种候选具有较高选择优先级。

---

# 16. Stage D — Structural Economy

比较候选需要新增多少结构。

优先：

- 复用已有对象；
- 少引入新变量；
- 少增加额外假设；
- 少使用高阶工具。

可记作：

\[
\boxed{\text{Structural Cost}}
\]

这里不是单纯比较公式长度。

---

# 17. Stage E — Proof Cost

估计如果采用候选 \(C\)，后续证明需要：

- 多少新子目标；
- 多少额外 lemma；
- 多复杂的计算；
- 是否容易形成死路。

记作：

\[
\boxed{\text{Proof Cost}}
\]

Candidate Selection 可以使用粗粒度：

```text
low
medium
high
unknown
```

不需要一开始发明精确数值。

---

# 18. Stage F — Information Gain

对于试探性候选，即使暂时不能成功，也可能值得先试。

原因是它可能快速回答：

- 当前路线是否可行；
- 哪个 Required Property 还缺；
- 哪个系数需要调整；
- 是否需要换 family。

因此定义：

\[
\boxed{\text{Expected Information Gain}}
\]

这使 Candidate Selection 不只选择“最可能成功”的候选，

还可以选择：

> 最值得低成本试验的候选。

---

# 19. Stage G — Learner Value

面向 ProofAtlas，学习价值本身也是选择因素。

候选可能具有：

- 更高模式迁移价值；
- 更清楚体现核心思想；
- 更容易展示 Constraint Ledger；
- 更能说明定理角色。

因此可以定义：

\[
\boxed{\text{Pedagogical Value}}
\]

但它不能凌驾于数学合法性和发现真实性之上。

---

# 20. 推荐的词典式偏好顺序

默认可以采用：

\[
\boxed{
\text{Legality}
\succ
\text{Hard Requirement Coverage}
\succ
\text{Tool Access}
\succ
\text{Structural Economy}
\succ
\text{Proof Cost}
\succ
\text{Learner Value}
}
\]

对于 Probe Candidate：

\[
\text{Information Gain}
\]

可以提前。

重要：

> 这只是默认 policy，不应宣称是数学上的普适最优排序。

---

# 21. 不允许“为了对上参考答案”修改排序标准

一种危险行为：

1. 先看到参考答案；
2. 发现当前标准选不到它；
3. 临时增加一个偏好：
   > “更优雅”；
4. 于是参考答案胜出。

这属于：

\[
\boxed{\text{Selection Criterion Leakage}}
\]

因此 selection criteria 必须在：

\[
C_{\mathrm{ref}}
\]

可见之前冻结。

---

# 22. Selection Leakage 分类

---

## CSL-1 Reference Privilege

因为候选与参考答案相同而提高排序。

---

## CSL-2 Retroactive Criterion

看到答案后新增评判标准。

---

## CSL-3 Beauty Bias

把最终表达漂亮当成“事前自然”。

---

## CSL-4 Proof-Length Leakage

因为已经知道某候选最终证明最短，所以事前优先。

如果 proof cost 不能在当前状态合理预估，这属于后见偏置。

---

## CSL-5 Hidden Future Success

使用后续才知道的成功结果比较候选。

---

## CSL-6 Alternative Suppression

明明存在同样合理候选，却为了与答案一致而不展示。

---

# 23. Candidate Selection 的 Blind Audit

每个重要 selection 都应接受以下测试。

---

## CS-A — Reference Blind Test

不显示参考答案，独立生成 shortlist 与排序。

这是最基本测试。

---

## CS-B — Alternate Reference Test

将参考答案换成另一个合法证明。

selection policy 不应因此自动改变。

---

## CS-C — Candidate Label Shuffle

把候选顺序、变量名打乱。

排名不应受表面位置影响。

---

## CS-D — Syntax Perturbation

对等价候选进行代数改写。

排名应该基于功能，而不是表达式是否像教材。

---

## CS-E — Criterion Freeze Test

确认 selection criteria 在参考答案揭示前已记录。

---

## CS-F — Reference Loss Test

若参考答案候选没有进入 shortlist，系统是否仍能正常完成证明？

若能：

> 不得把这个差异当错误。

---

# 24. Candidate Selection 的结果不一定唯一

可能出现：

\[
C_1\sim C_2
\]

即没有足够依据区分。

此时正确输出：

> “当前状态下，\(C_1\) 与 \(C_2\) 都是合理首选；先尝试哪一个都可以。”

而不是强迫：

\[
C_1>C_2.
\]

这对防止答案偏置非常重要。

---

# 25. Pareto Frontier

可以把候选看成多个维度：

\[
v(C)=
(\text{coverage},
\text{tool access},
-\text{structural cost},
-\text{proof cost},
\text{learner value}).
\]

若一个候选在所有关键维度都不差，并在至少一维更好，则支配另一个候选。

被支配候选可以降低优先级。

剩余候选形成：

\[
\boxed{\text{Candidate Pareto Frontier}}
\]

ProofAtlas 不必强行在 frontier 内唯一排序。

---

# 26. Selection Outcome 类型

建议只允许以下几种主要输出。

### SO-1 Preferred Candidate

一个候选明显更符合当前偏好。

### SO-2 Co-Preferred Candidates

多个候选并列合理。

### SO-3 Probe First

尚不能选最终路线，先试一个高信息增益候选。

### SO-4 Forced Candidate

约束唯一决定。

### SO-5 Underdetermined

当前信息不足以合理偏好任何候选。

SO-5 必须是合法结果。

---

# 27. “自然候选、经验候选、逆向候选、试探候选”的边界

这里正式与上一阶段衔接。

---

## Natural Candidate

定义：

> 主要由当前结构、接口和 Required Property 直接产生，新增假设少，匹配直接。

允许依据：

- 目标结构；
- 已有对象；
- interface match；
- local algebraic structure。

不得依据：

- “参考答案就是它”。

---

## Heuristic Candidate

定义：

> 由已经掌握的 proof pattern 或领域经验提供。

例如：

> “遇到两个难以直接比较的量，可以尝试插入中间项。”

它不是严格演绎出的，

但不是随机的。

必须标明使用的 heuristic。

---

## Backward Candidate

定义：

> 从当前目标或已触发定理需要的输入结构反推。

例如：

> 想证明零点存在；
> 已识别 IVT trigger；
> 因此寻找连续且可得到符号信息的辅助函数。

合法。

---

## Probe Candidate

定义：

> 当前依据较弱，但试验成本低、失败有信息价值的候选。

例如先试：

- 最简单常数；
- 最简单线性组合；
- 已有对象之一；
- 对称分配。

Probe Candidate 不得被称为“自然必然选择”。

---

# 28. Candidate 类型可以重叠
