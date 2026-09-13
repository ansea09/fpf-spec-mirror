---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__012_sota-echoing.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:11 — SoTA-Echoing"
line_start: 64809
line_end: 64820
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:11 - SoTA-Echoing

For a constrained comparison, the selected approach is to construct feasible changes before interpreting their effect. Direct substitution is useful for small expressions; differential conditions and numerical optimization become useful as the candidate class or calculation grows. The choice depends on the result needed and the assumptions available.

[Boyd and Vandenberghe, *Convex Optimization*, §4.2.3](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=153) gives the differentiable convex case: the gradient's inner product with every feasible displacement characterizes optimality. Adopt its attention to the feasible set and the hypotheses that make a first-order condition sufficient. The Method above also admits nonconvex and discrete comparisons, where that sufficiency cannot be inherited. Specialized convex formulations and algorithms remain useful external constructions when their inputs fit.

[Tong, *Classical Dynamics*, §2.1](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) develops variations of a history with fixed endpoints and the resulting Euler-Lagrange equations. Adopt the explicit endpoint conditions and the distinction between stationary action and a minimum. This is an established classical source; it supplies neither an action for every new physical system nor its empirical justification.

C.29 supplies the mathematical interpretation and return, while C.29.2 supplies computational formulation and error-sensitive use. Here the reusable contribution is construction of the admissible family and the argument from its change. If those operations require a specialized variational, optimization or physical-modeling technique, recover that technique at the point where the needed result becomes specific.

Revisit the construction when constraints, regularity, candidate class or the required conclusion change. A newer solver can improve cost without changing the meaning of the admissibility and optimality claims.

