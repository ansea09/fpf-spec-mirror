---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__012_sota-echoing.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:11 — SoTA-Echoing"
line_start: 52481
line_end: 52489
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "source return"
  - "structure kind"
---

### C.30.ILC:11 - SoTA-Echoing

| SoTA/practice anchor | What it supports | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Scenario-based architecture trade-off practice, with ATAM-like reasoning used here as lineage and practice basis for concern, scenario, sensitivity point, and trade-off recognition rather than as a decision or evidence method. | Architecture work often starts from cross-concern and cross-scope trade-offs rather than one local measurement result. | Adopt and adapt: use the conflict cue for triage, require declared scopes and structure kinds, and keep final selection, evidence, assurance, and gate passage in exact governing patterns. | A residual can start an architecture move without becoming a decision, proof, or safety case. |
| Complex systems and multi-scale modeling practice. | Local interactions can produce residuals or constraints at wider declared scopes. | Adapt: use scale and scope language only after the FPF record declares the relevant scope or scale window. | `Interlevel`, conflict, and frustration language remains a cue until fields recover the scopes and residual carrier. |
| Control and cyber-physical systems practice. | Local autonomy, feedback, supervisor relations, and rate separation can create cross-scope conflict. | Reuse through `C.30.LCA`, `B.2.5`, `C.27`, and `A.3.3`; do not let ILC carry control proof. | A control conflict opens control-structure or dynamics support only when live. |
| FPF source-return and semantic-coarsening discipline. | Compressed views and reusable records can hide distinctions that matter in a wider scope. | Adopt: add `sourceReturnCondition?` when hidden distinctions carry the residual. | A bounded exception or source-return trigger may be the correct first move. |

