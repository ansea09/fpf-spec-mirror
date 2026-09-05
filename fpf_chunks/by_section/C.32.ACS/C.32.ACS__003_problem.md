---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__003_problem.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:2 — Problem"
line_start: 64447
line_end: 64456
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "anti-Goodhart guard"
  - "architecture characteristic criteria set"
  - "criteria row"
  - "improvement cycle"
  - "protected counter-characteristic"
  - "proxy risk"
---

### C.32.ACS:2 - Problem

Architecture synthesis needs criteria. A multi-criteria or multilevel optimization phrase is empty until the criteria are named. In C.32-family work, those criteria are admitted architecture-characteristic rows or declared C.25 Q-Bundle slots of the described holon, each bound to its exact bearer, `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, qualification or evaluation window, and receiving use. A broad domain or bounded-context label supplies none of those bindings.

Architecture characteristics are not the same as user functions. Functional demand says what the holon must do. An architecture characteristic says whether the selected structures make that demand maintainable, controllable, replaceable, observable, evolvable, scalable, affordable, safe enough, or otherwise acceptable.

Source catalogues and textbooks can offer hundreds of possible quality or architecture terms. A project may inspect dozens. The actual optimization loop should normally use only a few indicatorized rows, often three to five. Other important rows remain monitored guardrails or context-only rows so that optimizing one visible measure does not damage functional adequacy, safety, evidence, maintainability, or another protected architecture concern.

C.32.ACS supplies the project criteria set and scale rows. It does not create the holon-family starter pack, define a Q-Bundle, validate a measurement method, run an eval, compare candidates, choose an architecture, or decide the project architecture.

