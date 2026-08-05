---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 66811
line_end: 66824
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.6"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.18.NET"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `ADRBeforeDecisionRelation` | The team starts from an ADR template and fills prose before the selected option, trade-off, and work consequences are recoverable. | Draft `ArchitectureDecisionRelation@Project` first; then use `C.32.ADR` only as publication projection. |
| `CandidateWinnerByMetric` | One score, benchmark, or eval reading is treated as the architecture decision. | Return to `C.32.ACS`, `C.32.ACE`, `C.16`, and `A.19.CPM`; decide only after trade-offs and accepted losses are recorded. |
| `StructureOnlyDecision` | The decision names a target structure but gives no method-use or work-split instruction for those who must realize it. | Add method-description or pattern-use refs, responsible roles, work boundary, readiness exit, and expected structure effect; use `A.15` for work claims. |
| `MethodOnlyDecision` | The decision says which style, pattern, or tool to use but not which target structures it is expected to produce or preserve. | Name the intended selected structures and architecture-characteristic trade-offs; return to `C.30`, `C.30.ASV`, or `C.32` if the structure is not recoverable. |
| `FrozenArchitectureDecision` | The decision has no source-return or reopen condition. | Add eval guardrails, source-currentness return, architecture-influence/transformed-side fit trigger, or supersession rule. |
| `LensOrQBundleAsDecisionAuthority` | A view, structural-information lens, measurement row, Q-Bundle, or eval reading is treated as if it selected the architecture. | Return the source to its owner: `C.29` for lens use, `C.25` for Q-Bundle, `C.16` for measurement, `C.32.ACE` for eval, and PAD for the actual decision relation. |
| `GovernanceByImplication` | Teams are expected to follow the decision, but no readiness, gate, evidence, assurance, or governance exit is named. | Add the exact receiving pattern refs; do not import those statuses into PAD. |
| `ProjectSelectionOrRoleByDecision` | A PAD field is treated as proof that a project selected a system, or the system gains `SystemOfInterestRole` or an assignment because the decision names it. | Keep the decision designation and every direct fact; apply A.15.6 and A.2/A.2.1 independently, and return `missing-substrate[project-selection-conjunction]` when the compound truth is needed. |
| `NetworkOrInfluenceByCitation` | A cited network record, C.32.CONWAY frame or pair row, or PAD decision is treated as a network member, cross-flow occurrence, architecture-influence occurrence, performer, or actual structure effect. | Restore the exact E.18.NET network and direct relation owners, use C.30.TFS-REL for architecture use, and keep expected structure effect modal until C.30 independently establishes the actual architecture relation. |

