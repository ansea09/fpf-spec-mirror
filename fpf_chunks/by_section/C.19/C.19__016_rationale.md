---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore–Exploit Governor (E/E‑LOG)"
section_id: "C.19:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__016_rationale.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.19 — Explore–Exploit Governor (E/E‑LOG)"
  - "C.19:10 — Rationale"
line_start: 40888
line_end: 40895
dependencies:
  - "B.3"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.24"
  - "C.28"
  - "G.5"
  - "G.9"
keywords:
  - "DecisionSubject clarification"
  - "EmitterPolicy"
  - "InsertionPolicy"
  - "dominance default routing"
  - "explore-exploit"
  - "keep frontier"
  - "lens id"
  - "live candidate pool"
  - "narrow to subset"
  - "pool-policy result"
  - "reroute"
  - "sunset line"
  - "widen"
---

### C.19:10 - Rationale

`C.19` exists because pool governance is neither local choice nor execution. Once several candidate lines remain live, the key question is no longer which single option should survive now; it is how the pool should be governed next under one explicit lens or policy. That question needs its own explicit pool-policy result, otherwise frontier drift, silent scalarization, and policy amnesia return immediately.

- Post-2015 bandit and Bayesian-optimization practice treats explore/exploit posture as an explicit policy object, not as one hidden side effect of whichever candidate looked best first. The practical implication here is to emit one explicit pool treatment plus one change trigger, not one atmospheric frontier story.
- Contemporary frontier and quality-diversity practice also distinguishes the live frontier from any scalarized pick taken under one declared lens. The practical safeguard is to keep `keep frontier`, `narrow to subset`, and `sunset line` as visible alternatives rather than silently totalizing the pool.
- Modern pool-management and fairness-preserving lines keep coverage or heterogeneity pressures explicit until one declared reason justifies retirement or reroute. The practical implication is simple: sunset or reroute only when the current pool-policy result can already say why the pool no longer belongs to `C.19`.

