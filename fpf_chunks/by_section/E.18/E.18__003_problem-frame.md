---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__003_problem-frame.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:2 — Problem frame"
line_start: 66209
line_end: 66222
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:2 - Problem frame

Teams can produce many **valid flow valuations** for the same holon under `VP.Functional`, for example for a declared `U.Capability` or transduction claim. The P2W reference path is:
`U.Signature(profile=FormalSubstrate) → U.PrincipleFrame → U.Mechanism → U.ContextNormalization (UNM) → U.SelectionAndTuning ↔ U.WorkPlanning → U.Work → U.EvaluatingAndRefreshing`
is one **path** among many possible domain paths. Without a common **graph architecture**:

* flows look ad‑hoc and **non‑comparable**;
* cross‑Context **crossings** (plane/Context changes) are undocumented;
* MVPK faces carry **hidden arithmetic** or restate I/O;
* set‑returning selection is silently replaced by **single scores**;
* cycles lack **budget** discipline; refresh is **out‑of‑band**.

MVPK already fixes publication drift at the **single-arrow** scope; E.TGA lifts those **publication and comparability laws** to the **graph as a whole**.

