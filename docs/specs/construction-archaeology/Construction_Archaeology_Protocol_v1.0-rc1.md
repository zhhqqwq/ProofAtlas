# ProofAtlas — Construction Archaeology Protocol v1.0-rc1

> 文档性质：Construction Archaeology v0.1–v0.6 Integration Pass  
> 状态：release candidate / 已完成 9 个 end-to-end adversarial tests  
> 上游依赖：Motivation Fidelity / M3 Search Protocol v1.0-rc1  
> 目标：把分散规范压缩成可执行、可审计、可直接进入 `SKILL.md` 的统一协议  
> 原则：不再为术语完整性扩 taxonomy；只保留改变 Skill 行为的结构

---

# 1. 核心任务

Construction Archaeology（CA）不是把证明讲得更长，也不是猜作者真实心理历史。

它的任务是：

> **恢复 polished proof 中被压缩掉的构造形成结构：局部选择、策略阶段、约束演化、常数来源、失败/替代路线，以及这些 discovery structures 最终怎样被写成短证明。**

核心闭环：

\[
\boxed{
\text{Polished Proof}
\rightleftarrows
\text{Discovery Structure}
}
\]

其中 discovery structure 的最小统一链为：

\[
\boxed{
\text{Hotspots}
\rightarrow
\text{Units}
\rightarrow
\text{Episodes}
\rightarrow
\text{Constraint Events}
\rightarrow
\text{Constant Provenance}
\rightarrow
\text{Presentation Map}
}
\]

CA 默认恢复的是：

- structural reconstruction；
- pedagogical reconstruction；

不是 historical reconstruction。

---

# 2. 与 M3 的边界

M3 回答：

> 在某一个关键状态下，为什么某个候选可以答案独立地产生、选择并测试？

CA 回答：

> 多个局部搜索事件怎样共同形成一个完整构造，并最终被压成 polished proof？

因此：

\[
\boxed{
\text{M3}=\text{local discovery fidelity}
}
\]

\[
\boxed{
\text{CA}=\text{multi-event construction history}
}
\]

CA 不得重新发明 M3，也不得提高 M3 fidelity。

若某 Unit 只有 M1/M2：

> CA 可以记录其功能与 provenance，但不能包装成 M3 discovery。

---

# 3. No Fidelity Inflation

对任意 CA reconstruction：

\[
\boxed{
F_{\mathrm{CA}}
\le
\min_i F(U_i)
}
\]

这里不是要求数值化评分，而是表达：

> 完整故事的可信度不能超过其关键局部动机中最弱的一环。

允许：

- `M1`
- `M2`
- `M3-provisional`
- `M3`

历史支持另记：

- `none`
- `source_grounded`

---

# 4. Construction Hotspot Gate

CA 不是全文逐步解释器。

只有遇到真正的 construction hotspot 才进入深度 archaeology：

- auxiliary object；
- bridge term；
- nontrivial parameter / threshold；
- subsequence / diagonal / nested selection；
- error decomposition；
- error budget；
- theorem-input manufacturing；
- bad-object / contradiction witness；
- localization；
- `min/max` merge；
- salient “magic” constant；
- normalization；
- major representation change；
- informative branch / retry。

普通：

- algebra；
- substitution；
- standard inequality chain；
- routine theorem application；

默认不触发 CA。

核心防线：

\[
\boxed{\text{No new choice, no new Construction Unit}}
\]

---

# 5. Surface Atoms

先把 polished proof 解析为 Surface Atoms：

- claim；
- formula；
- choice phrase；
- theorem invocation；
- parameter choice；
- witness construction；
- transition phrase；
- compression marker。

但：

\[
\boxed{
\text{Surface Atom}
\neq
\text{Construction Unit}
}
\]

一个 Unit 可覆盖多 atoms；
一个 atom 也可能压缩多个 latent events。

---

# 6. Construction Unit

定义：

\[
\boxed{
\text{Construction Unit}
=
\text{one locally coherent search obligation}
}
\]

一个 Unit 主要回答：

> 在当前状态下，为跨越当前 obstacle，我现在需要选择/构造/限制什么？

最小字段：

```yaml
unit:
  id:
  local_goal:
  obstacle:
  available_information:
  degree_of_freedom:
  required_properties:
  candidate_family:
  selected_candidate:
  local_test:
  state_update:
  fidelity:
```

---

# 7. Unit Boundary

新 Unit 的最强信号：

1. 新 degree of freedom；
2. local goal 改变；
3. obstacle 改变；
4. 新独立约束选择；
5. candidate family 改变；
6. branch / retry；
7. nested construction begins。

不因以下事项自动拆：

- 新公式行；
- 新等号；
- routine derivation；
- 一个候选的多项验证；
- jointly quantified witness tuple。

---

# 8. Counterfactual Separability Test

对两个相邻选择 \(A,B\) 问：

> 保持 \(A\) 不变，能否把 \(B\) 换成另一合法选择，且局部 proof structure 仍有意义？

若是：

> 倾向拆为不同 Units。

若 \(B\) 只是 \(A\) 的 deterministic consequence：

> 合并。

依赖不等于合并。

例如 \(N\) 选定后 \(\delta\) 依赖 \(N\)，但若二者解决不同 local goals，仍应拆。

---

# 9. Unit Closure

一个 Unit 在以下时刻关闭：

1. 当前 degree of freedom 已产生候选；
2. Required Properties 已局部测试；
3. proof state 有明确 update；
4. 下一步若继续，需要新的 search obligation，或只剩 deterministic derivation。

---

# 10. Construction Episode

定义：

\[
\boxed{
\text{Construction Episode}
=
\text{one coherent strategy phase}
}
\]

Episode identity 核心：

\[
\boxed{
ID(E)
=
(\text{High-level Goal},
\text{Strategy Commitment},
\text{Exit Condition})
}
\]

Episode 不是“几个相邻 Units 的文件夹”。

---

# 11. Episode Signature

```yaml
episode:
  high_level_goal:
  entry_obstacle:
  strategy_commitment:
  mechanism:
  working_representation:
  invariant:
  success_condition:
  returned_artifact:
```

相同 Episode 的强证据：

- shared goal；
- shared strategy；
- shared artifact flow；
- shared invariant；
- shared exit condition。

---

# 12. Peer Episode vs Child Episode

## Peer Episode

真正发生高层策略阶段变化：

- goal 改变；
- strategy 被放弃；
- previous exit condition 已完成；
- proof regime 从此切换且不返回。

## Child Episode

满足：

\[
\boxed{
\text{Call}
\rightarrow
\text{Subproblem}
\rightarrow
\text{Return Artifact}
\rightarrow
\text{Resume Parent}
}
\]

父 strategy 在 child 执行时仍然有效。

---

# 13. Episode Substance Gate — Integration Patch A

v0.3 容易把很小的局部选择升级为 child Episode。

Integration Pass 增加：

\[
\boxed{\text{Episode Substance Gate}}
\]

一个局部 subproblem 只有在至少满足以下之一时才升级成 child Episode：

1. 内部包含两个及以上 meaningful Units；
2. 有独立 strategy commitment；
3. 有自己的 invariant；
4. 有非平凡 call–return contract；
5. 可以合理作为独立 proof module。

否则：

> 保留为 parent Episode 内的 Unit。

例如：

- 单次对称 error-budget choice 通常只是 Unit；
- “选 \(\delta\)”通常只是 Unit；
- 递归子列构造可能是真正 child Episode。

这防止：

\[
\boxed{\text{Hierarchy Inflation}}
\]

---

# 14. Strategy Switch vs Local Repair

以下通常仍在同 Episode：

- 改参数；
- 换 candidate；
- family 内 retry；
- 改误差预算；
- strengthening / relaxation。

只有当高层 mechanism 本身被放弃时才换 peer Episode。

例如：

\[
\text{direct estimate}
\rightarrow
\text{missing uniform control}
\rightarrow
\text{compactness contradiction}
\]

才是 strategy switch。

---

# 15. Artifact 是跨 Unit/Episode 的接口

CA 中的重要对象需要作为 Artifact 被明确追踪。

Artifact 包括：

- auxiliary function；
- bridge term；
- subsequence；
- witness；
- bound；
- parameter；
- theorem-ready bundle；
- normalized representation；
- contradiction witness；
- returned guarantee。

统一最小记录：

```yaml
artifact:
  id:
  kind:
  created_by:
  consumed_by:
  scope:
  status:
```

这一对象在 v0.x 中分散出现，Integration Pass 将其提升为显式接口。

---

# 16. Constraint Ledger

Constraint Ledger 是：

\[
\boxed{\text{event-sourced constraint state machine}}
\]

不是最终约束列表。

它记录：

\[
\mathcal L_0
\rightarrow
\mathcal L_1
\rightarrow
\cdots
\]

每条 search-significant constraint 至少有：

- provenance；
- role；
- scope；
- lifecycle；
- dependency。

---

# 17. Search-Significant Constraint

只记录会影响以下任一事项的约束：

- candidate space；
- theorem activation；
- invariant；
- parameter choice；
- branch rejection；
- constant provenance；
- merge / replace。

普通 intermediate inequality 不进入 Ledger。

---

# 18. Constraint Roles

分开记录：

## Search role
- `hard`
- `route_enabling`
- `simplifying`
- `preference`
- `presentation_only`

## Logical relation
- `exact`
- `equivalent`
- `stronger`
- `weaker`
- `sufficient`
- `necessary`
- `incomparable`
- `unknown`

禁止把 convenience 误说成 necessity。

---

# 19. Constraint Events

统一只保留真正影响实现的事件：

- `introduce`
- `strengthen`
- `specialize`
- `relax`
- `replace`
- `merge`
- `mark_redundant`
- `discharge`
- `abandon`
- `scope_exit`
- `conflict_detect`
- `presentation_hide`

关键区别：

\[
\text{redundant}
\neq
\text{discharged}
\neq
\text{abandoned}
\neq
\text{out-of-scope}
\]

---

# 20. Causal Order — Integration Patch B

v0.4 使用：

\[
C_0\rightarrow C_1\rightarrow C_2
\]

容易被误解为存在唯一真实线性发现顺序。

完整证明测试前先加入候选修订：

\[
\boxed{
\text{Event Order}
=
\text{causal partial order}
}
\]

记录：

- `depends_on`
- `must_precede`
- `independent_of`
- `presentation_before/after`

只有有证据时才建立 total order。

因此多个独立约束：

\[
c_1,\quad c_2
\]

可以只记录：

\[
c_1\parallel c_2
\]

随后共同：

\[
\text{merge}(c_1,c_2).
\]

这样不会伪造“先想到哪一个”。

---

# 21. Feasibility Gate

每次：

- introduce；
- strengthen；
- specialize；
- merge；

后检查 active constraint bundle 是否仍可满足。

若冲突：

\[
\boxed{\text{search state = blocked}}
\]

随后必须：

- relax；
- replace；
- abandon candidate；
- abandon Episode。

---

# 22. Scope-Safe Return

child Episode 只能向 parent 导出：

```yaml
returned_artifact:
  object:
  guarantees:
```

内部 temporary constraints 默认：

`out_of_scope`

不能泄漏成全局 assumptions。

---

# 23. Constant Archaeology

CA 不把常数当孤立数字，而恢复：

\[
\boxed{\text{Constant Provenance Chain}}
\]

核心原则：

\[
\boxed{\text{Need Before Number}}
\]

先问：

> 为什么需要一个承担这种功能的量？

再追：

\[
\text{Need}
\rightarrow
\text{Family}
\rightarrow
\text{Constraint}
\rightarrow
\text{Specialization}
\rightarrow
\text{Coarsening}
\rightarrow
\text{Derived Constant}
\rightarrow
\text{Merge/Normalize}
\rightarrow
\text{Polished Form}.
\]

---

# 24. Salient Constant Gate

只追踪会影响理解或搜索的：

- magic number；
- threshold；
- \(\varepsilon/m\)；
- localization ratio；
- recursion scale；
- normalization factor；
- merge-generated threshold；
- coarsened coefficient。

不要追踪普通代数中每一个 `2`。

---

# 25. Constant-Producing Events

Integration Pass 保留：

- `parameter_introduce`
- `parameter_specialize`
- `derive_constant`
- `coarsen`
- `budget_split`
- `normalize`
- `optimize`
- `merge_generate`
- `canonicalize`

---

# 26. Constant Necessity

对 salient constant 分开回答：

- Value Necessity；
- Role Necessity；
- Route Necessity。

例如 \(r=1\) 可：

- value necessary: no；
- role necessary: yes；
- route necessary: yes。

---

# 27. Optimality Calibration

允许：

- `not_applicable`
- `unknown`
- `feasible`
- `nonoptimal_but_simple`
- `locally_optimal`
- `globally_optimal`
- `exact`

禁止：

\[
\text{feasible}
\Rightarrow
\text{optimal}.
\]

---

# 28. Hidden Parameter Recovery

可以从 polished constant 恢复 general family，但必须存在真正 semantic degree of freedom。

合法：

\[
r>0
\rightarrow
r=1.
\]

非法 fake family：

\[
6+\lambda-\lambda.
\]

---

# 29. Provenance ≠ Motivation

Constant Archaeology 允许从 final constant 向后查询 provenance。

但：

\[
\boxed{
\text{backward provenance}
\not\Rightarrow
\text{forward discoverability}
}
\]

声称“为什么会想到这个常数”仍需 M3。

---

# 30. Search-to-Presentation Map

Polished proof 被视为：

\[
\boxed{
\Pi_{\mathrm{pres}}:
\mathcal D
\rightarrow
\mathcal P
}
\]

其中 \(\mathcal D\) 是 discovery structure，\(\mathcal P\) 是 polished proof structure。

Map 必须允许：

- many-to-one；
- one-to-many；
- hidden；
- reordered；
- presentation-only。

---

# 31. Presentation Spans

高价值 span：

- sentence；
- formula；
- formula subexpression；
- “取/令/不妨设”；
- theorem call；
- `min/max`；
- “显然/易知”；
- omitted block。

不做 token-level alignment。

---

# 32. Presentation Mapping Operations

Integration Pass 压缩为：

- `preserve`
- `compress`
- `inline`
- `hide`
- `merge`
- `canonicalize`
- `normalize`
- `symmetrize`
- `coarsen`
- `reorder`
- `collapse_verification`
- `collapse_theorem_preparation`
- `delete_branch`
- `delete_search_commentary`
- `presentation_only_insert`

---

# 33. Compression Markers

以下只作为 inspection trigger：

- “取”
- “令”
- “不妨设”
- “显然”
- “易知”
- “由某定理”
- “充分大/充分小”
- `min/max`
- sudden constant
- \(\varepsilon/m\)

不能根据词面直接断定 hidden history。

---

# 34. Forward Projection 与 Reverse Archaeology

分开：

\[
F:
D\rightarrow P
\]

与：

\[
R:
P\rightarrow\{D_1,D_2,\ldots\}.
\]

Reverse map 是集合值恢复。

核心：

\[
\boxed{
\text{Polished Proof}
\not\Rightarrow
\text{Unique Discovery History}
}
\]

---

# 35. Reverse Recovery Evidence

按证据强度使用：

1. explicit text；
2. logical necessity；
3. Constraint Ledger provenance；
4. Constant provenance；
5. interface separation；
6. independent M3 reconstruction；
7. pedagogical generalization。

confidence：

- `forced`
- `strong`
- `plausible`
- `speculative`

默认只把 `forced/strong` 放进核心 archaeology。

---

# 36. Compression Loss Profile

对重要 polished span，记录它丢失了什么：

- motivation；
- alternatives；
- constraint provenance；
- constant provenance；
- branch history；
- theorem role；
- scope；
- optimization status；
- dependency information。

这用于识别：

\[
\boxed{\text{Cognitive Compression Hotspots}}
\]

---

# 37. Informative Branches

失败 branch 进入 CA 的条件：

\[
\boxed{
\text{prior justification}
+
\text{local test}
+
\text{information gain}
}
\]

允许：

- `accepted`
- `rejected_incorrect`
- `rejected_insufficient`
- `rejected_too_strong`
- `rejected_unavailable_tool`
- `valid_but_not_selected`
- `valid_discovery_not_presentation`

禁止 decorative failure。

---

# 38. Route — Integration Patch C

完整 proof 测试需要区分：

> 同一个证明目标的不同高层合法策略。

因此增加轻量级 Route：

```yaml
route:
  id:
  goal:
  status:
    accepted_reference
    accepted_alternative
    abandoned
  root_episode:
  fidelity:
```

Route 不取代 Episode。

它只解决：

- reference route；
- blind-preferred alternative；
- strategy-level abandoned route；

不能被强行混成同一 Episode tree。

---

# 38A. Witness Origin — Test-Driven Patch D

完整 proof 中的固定量并不都来自“选择”。

例如 Heine–Cantor 的否定给出：

\[
\exists\varepsilon_0>0.
\]

这里 \(\varepsilon_0\) 是逻辑量词提供的 existential witness，不是为了方便而挑选的 magic constant。

因此所有 salient constant / threshold / witness entity 增加：

```yaml
origin_mode:
  chosen
  derived
  existential_witness
  theorem_supplied
  inherited
  normalized
```

解释规则：

- `chosen`：存在自由度并由 search 选择；
- `derived`：由已有约束/表达式推出；
- `existential_witness`：由逻辑假设/否定/存在量词保证；
- `theorem_supplied`：由定理输出；
- `inherited`：题设/外层 scope 已固定；
- `normalized`：利用无关自由度选 canonical representative。

禁止把 `existential_witness` 讲成“为什么聪明地取这个数”。

---

# 38B. Construction Policy — Test-Driven Patch E

对子列、嵌套区间、对角化、逐步逼近等，candidate 不是静态公式，而是递归选择策略。

CA 必须保留：

```yaml
construction_policy:
  id:
  episode:
  state:
  admissible_choices:
  selection_rule:
  invariant:
  progress_measure:
  generated_artifact:
  fidelity:
```

例如 limsup 子列：

- state：上一索引 \(n_{k-1}\)；
- admissible choices：tail 中满足 approximation requirement 的 indices；
- selection rule：选 \(n_k>n_{k-1}\) 且 \(a_{n_k}>s_{m_k}-\eta_k\)；
- invariant：strictly increasing indices；
- progress：\(m_k\to\infty,\eta_k\to0\)；
- artifact：subsequence \((a_{n_k})\)。

Construction Policy 可以是 Unit 的 candidate type，也可以在通过 Episode Substance Gate 时成为 substantive child module。

---

# 39. Discovery Causality vs Presentation Order

CA 必须至少区分三种 order：

1. logical dependency；
2. reconstructed search causality；
3. presentation order。

禁止：

\[
\boxed{
\text{presentation order}
=
\text{discovery order}
}
\]

尤其教材经常先宣布最终 \(\delta\)，再验证。

---

# 40. Unified CA Record

```yaml
construction_archaeology:
  proof:
    goal:
    reference_route:

  routes:
    - id:
      status:
      root_episode:

  episodes:
    - id:
      route:
      parent:
      signature:
      units:
      children:
      inputs:
      outputs:
      status:
      fidelity:

  units:
    - id:
      episode:
      goal:
      obstacle:
      degree_of_freedom:
      required_properties:
      candidate_family:
      selected_candidate:
      local_test:
      state_update:
      fidelity:

  artifacts:
    - id:
      kind:
      created_by:
      consumed_by:
      scope:

  construction_policies:
    - id:
      episode:
      state:
      admissible_choices:
      selection_rule:
      invariant:
      progress_measure:
      generated_artifact:

  constraint_events:
    - id:
      type:
      inputs:
      outputs:
      depends_on:
      scope:
      role:
      confidence:

  constants:
    - id:
      expression:
      semantic_role:
      origin_mode:
      parents:
      generating_event:
      alternatives:
      necessity:
      optimality:
      scope:

  presentation_spans:
    - id:
      content:
      type:

  presentation_mappings:
    - discovery_sources:
      presentation_targets:
      map_types:
      lost_information:
      discovery_order:
      presentation_order:
      confidence:

  unresolved:
    - issue:
      confidence:

  archaeology_status:
    fidelity_floor:
    coverage:
    historical_support:
```

这是逻辑 record，不是 Cognitive Proof Graph schema。

---

# 41. Unified Execution Pipeline

\[
\boxed{
P
\rightarrow
H
\rightarrow
U
\rightarrow
E
\rightarrow
L
\rightarrow
K
\rightarrow
M
\rightarrow
X
}
\]

其中：

- \(P\)：Polished Proof；
- \(H\)：Hotspots；
- \(U\)：Units；
- \(E\)：Episodes / Routes；
- \(L\)：Constraint Ledger；
- \(K\)：Constant Provenance；
- \(M\)：Presentation Map；
- \(X\)：Learner-facing explanation。

具体：

1. Parse proof only to the granularity needed for hotspots.
2. Detect construction hotspots.
3. Segment each hotspot into Units.
4. Run/reuse M3 on nontrivial Unit choices.
5. Group Units into Episodes.
6. Separate alternative Routes.
7. Register Artifacts and scope.
8. Replay search-significant Constraint Events.
9. Trace salient Constants through Ledger.
10. Build Search-to-Presentation Map.
11. Audit fidelity, scope, causality, alternatives, and over-analysis.
12. Produce progressive student view.

---

# 42. Student-Facing Output

默认不 dump schema。

推荐：

## 1. Proof Map
证明整体分几阶段。

## 2. Construction Hotspot
真正难想到的位置。

## 3. Why It Works
数学有效性。

## 4. Why One Might Try It
M3 支持时给 discovery reconstruction。

## 5. Construction Lineage
目标 → obstacle → choice → constraint → result。

## 6. Constants & Constraints
哪些必须，哪些方便。

## 7. What the Textbook Compressed
展示 1–3 个高价值 compression hotspots。

## 8. Transfer Pattern
以后哪里能复用。

---

# 43. Archaeology Depth

### CA-L1 Quick
只给主 strategy、hotspot、constant origin。

### CA-L2 Teaching — default
Units + main Episode + constraints/constants + presentation compression。

### CA-L3 Research
Routes + branches + alternative preimages + full fidelity audit。

---

# 44. Core Audits

最终只保留 12 个综合 audit：

1. **Hotspot Audit** — 是否只深挖真正构造点？
2. **Segmentation Audit** — Units 是否按 search obligation 而非公式行？
3. **Episode Audit** — strategy grouping 是否过粗/过细？
4. **Hierarchy Audit** — child Episode 是否通过 Substance Gate？
5. **Fidelity Audit** — 是否提高 M-level？
6. **Branch Audit** — 是否虚构失败或抹掉 valid alternative？
7. **Constraint Audit** — provenance / role / lifecycle / scope 是否完整？
8. **Feasibility Audit** — active constraint bundle 是否可满足？
9. **Constant Audit** — provenance / alternatives / optimality 是否校准？
10. **Causality Audit** — 是否伪造唯一线性 discovery order？
11. **Presentation Audit** — discovery/presentation 是否分离？
12. **Over-analysis Audit** — 是否让 archaeology 淹没 proof idea？

---

# 45. Stop Rules

CA 应停止继续展开，当：

- 剩余步骤只是 routine derivation；
- 不再出现新的 search-significant constraint；
- salient constants 已追溯；
- theorem preparation 已解释；
- presentation compression 已足够解释 learner hotspot；
- 进一步展开不增加 transfer value。

---

# 46. rc1 冻结标准

只有在完整 end-to-end adversarial tests 后，且满足：

1. 至少 8 个不同 proof constructions；
2. 至少一个负例不触发 CA；
3. 至少一个 alternative valid route；
4. 至少一个 recursive policy；
5. 至少一个 nested/child Episode；
6. 至少一个 salient constant chain；
7. 至少一个 presentation reorder；
8. 没有发现必须新增核心层级对象；

才可冻结为：

\[
\boxed{\text{Construction Archaeology Protocol v1.0-rc1}}
\]

---

# 47. Integration Pass 当前三项候选 Patch

在 full-proof tests 前，Integration Pass 已识别三项值得重点验证的结构：

### Patch A — Episode Substance Gate
防止每个局部子问题都变 child Episode。

### Patch B — Causal Partial Order
Constraint / discovery events 不强迫唯一线性时间顺序。

### Patch C — Route Object
显式分开 reference route、valid alternative route、abandoned strategy route。

是否正式锁定，由 end-to-end tests 决定。

---

# 48. Integration Pass 的设计结论

Construction Archaeology 的最小稳定内核不需要更多 taxonomy。

真正需要稳定的是：

\[
\boxed{
\text{Unit}
+
\text{Episode}
+
\text{Route}
+
\text{Artifact}
+
\text{Constraint Event}
+
\text{Constant Provenance}
+
\text{Presentation Mapping}
}
\]

如果 end-to-end tests 不要求新的一级对象：

> 第三部分 Cognitive Proof Graph 应直接以这些对象和它们之间的关系作为 schema 需求来源。

---

# 49. End-to-End Validation Result

本 rc1 已用 9 个完整证明验证：

1. \(x^2\) continuity；
2. \(1/x\) continuity；
3. differentiable \(\Rightarrow\) continuous；
4. uniform limit preserves continuity；
5. Heine–Cantor；
6. limsup approximating subsequence；
7. positive continuous function on compact set has positive lower bound；
8. interval self-map fixed point via IVT；
9. uniqueness of sequence limits。

测试覆盖：

- localization；
- bridge construction；
- error budgeting；
- recursive selection；
- contradiction witness；
- compactness extraction；
- alternative routes；
- theorem preparation；
- min/max merge；
- low-archaeology negative pressure；
- causal independence。

结论：

\[
\boxed{
\text{Construction Archaeology Protocol v1.0-rc1}
}
\]

可作为 Part II 的第一个实现冻结候选。

除非真实 Skill/corpus eval 暴露新的结构性失败，否则不再继续扩充核心 taxonomy。
