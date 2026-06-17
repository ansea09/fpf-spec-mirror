---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__003_problem-frame.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:2 — Problem frame"
line_start: 67594
line_end: 67607
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:2 - Problem frame

Teams can produce many **well-typed flow valuations** for transformations of the same context holon under `VP.Functional`, for example for a declared `U.Capability` or transformation claim. The holon is the described/context object; the E.18 `EntityOfConcern` remains the selected `TransformationFlowStructure` over transformations and adjacent governed loci. The P2W reference path is:
`U.Signature(profile=FormalSubstrate) -> U.PrincipleFrame -> U.Mechanism -> U.ContextNormalization (UNM) -> SelectionAndTuning locus (G.5/selector relation) <-> WorkPlanning locus (A.15.2 U.WorkPlan or plan-item relation) -> U.Work -> EvaluatingAndRefreshing locus (G.11/refresh relation)`
is one **path** among many possible domain-specific transformation-flow paths. Without a common **structure discipline**:

* flows look ad-hoc and **non-comparable**;
* cross‑Context **crossings** (plane/Context changes) are undocumented;
* MVPK faces carry **hidden arithmetic** or restate I/O;
* set‑returning selection is silently replaced by **single scores**;
* cycles lack **budget** discipline; refresh is **out‑of‑band**.

MVPK already fixes publication drift at the **single-arrow** scope; E.18 lifts those **publication and comparability laws** to the **selected transformation-flow structure as a whole**.

