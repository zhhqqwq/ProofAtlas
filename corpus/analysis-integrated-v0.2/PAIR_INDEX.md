# Analysis Corpus v0.2 — Transfer Pair Index

Pairs: **18**  
Public transfer cases: **36**

| Pair | Canonical anchor | Perturbation | Isomorphic transfer |
|---|---|---|---|
| TP-01 | AN-001 | Use ε/3 and 2ε/3 instead of ε/2+ε/2. | Prove uniqueness of a function limit as x→a; bridge through f(x), using min for delta constraints. |
| TP-02 | AN-004 | Use Cauchy tolerance 7 and anchor m=N+3 instead of ε=1,m=N. | For a sup-norm Cauchy function sequence, show a tail has a common sup-norm bound by anchoring at one f_N. |
| TP-03 | AN-005 | Replace increasing/bounded-above by decreasing/bounded-below; use inf. | For a bounded increasing f:(0,1)→R, prove lim_{x→1^-}f(x) exists via sup and monotonicity. |
| TP-04 | AN-007 | Use trisection instead of bisection in the Bolzano–Weierstrass nested-interval proof. | Prove an infinite subset of [a,b] has an accumulation point by nested localization preserving infinitely many points. |
| TP-05 | AN-008 | Use η_k=2^{-k} and m_k=max{k,n_{k-1}+1}. | For nonempty bounded-above A⊂R, construct x_k∈A with x_k→sup A. |
| TP-06 | AN-010 | Use radius 2^{-n} instead of 1/n in the closure witness construction. | Prove x∈cl(F) iff there exists a sequence x_n∈F with x_n→x. |
| TP-07 | AN-011 | Prove x² continuity using localization radius 2 instead of 1. | Give a direct ε–δ proof that x³ is continuous at a, using localization of x²+ax+a². |
| TP-08 | AN-012 | Use θ=1/3 rather than θ=1/2 in the proof for 1/x. | Prove 1/(x+c) is continuous at a when a+c≠0; localize relative to the shifted singularity. |
| TP-09 | AN-013 | Use bridge f(a)g(x) rather than f(x)g(a), with an asymmetric error budget. | If u_n→u and v_n→v, prove u_nv_n→uv using the analogous mixed-term bridge. |
| TP-10 | AN-017 | Make preimage nonuniqueness explicit: for each y_n∈f(K), choose any x_n with f(x_n)=y_n. | In metric spaces, prove continuous images of sequentially compact sets are sequentially compact. |
| TP-11 | AN-019 | Give only the EVT route as reference and test whether the bad-sequence route is still preserved. | If f is continuous and nonzero on compact K, prove \\|f\\| has a positive lower bound. |
| TP-12 | AN-020 | Use d(x_n,y_n)<2^{-n} instead of <1/n. | Prove the sequential criterion for uniform continuity using pairs with d(x_n,y_n)→0. |
| TP-13 | AN-021 | Generalize self-map fixed point from [0,1] to [a,b]. | If continuous f,h have (f-h)(a)(f-h)(b)≤0, prove f(c)=h(c) for some c. |
| TP-14 | AN-025 | Use ε/4, ε/2, ε/4 rather than ε/3 in the uniform-limit continuity proof. | If all f_n are L-Lipschitz and f_n→f uniformly, prove f is L-Lipschitz. |
| TP-15 | AN-031 | Move the anchor point from x0 to an arbitrary fixed x1∈[a,b]. | If f_n(x0)→c and \\|\\|f_n'\\|\\|∞→0, prove f_n→c uniformly. |
| TP-16 | AN-035 | Use base-3 geometric blocks rather than dyadic blocks. | Use geometric blocking, not the integral test, to determine p-series convergence/divergence. |
| TP-17 | AN-038 | Require n(b-a)>2 and use a ceiling/floor witness instead of the minimal >1 slack. | Prove dyadic rationals {m/2^k} are dense in R by scale-insert-rescale. |
| TP-18 | AN-040 | Use safe radius d/3 instead of d/2 in the compact-set-closed proof. | If K,F are disjoint nonempty compact subsets of R, prove dist(K,F)>0. |
