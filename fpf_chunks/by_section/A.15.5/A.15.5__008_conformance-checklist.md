---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__008_conformance-checklist.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:7 — Conformance Checklist"
line_start: 25618
line_end: 25631
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.2.8.PER"
  - "A.20"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.18"
  - "E.18.1"
  - "E.24"
keywords:
  - "WIP and flow policy"
  - "blocked readiness overread"
  - "commitment disposition"
  - "full-kit condition"
  - "launch gate"
  - "planned slot fillings"
  - "prospective permission inputs"
  - "readiness before work entry"
  - "resource-readiness refs"
  - "retrospective exercise evidence"
  - "work-entry readiness"
---

### A.15.5:7 - Conformance Checklist

| ID | A conforming readiness use... | Check |
| --- | --- | --- |
| `CC-A15.5-1` | names the exact WorkPlan, PlanItem, intended performance, criterion, and evaluation time. | The readiness result cannot float free of the plan content and bounded entry question it judges. |
| `CC-A15.5-2` | separates readiness from performed work. | No target `U.Work` occurrence is asserted unless dated work evidence is current. |
| `CC-A15.5-3` | separates full-kit inputs from preparation and checking Work. | Cite preparation or checking as actual only through one exact dated `U.Work`, performer system, obtaining assignment, enacted Method, extent, and required actual bindings. |
| `CC-A15.5-4` | cites planned baselines without rewriting them. | A.15.3 planned-filling rows remain declaration-local content inside the exact WorkPlan. |
| `CC-A15.5-5` | keeps gate decisions in A.21. | Readiness labels do not create `GateDecision` without A.21 fields. |
| `CC-A15.5-6` | keeps resource readiness and resource aggregation distinct. | Planned reservations and actual consumption are not merged. |
| `CC-A15.5-7` | states stop, degraded-use, or recheck condition. | The reader can tell whether to stop, probe, commit, launch, or name a missing value under its subject pattern. |
| `CC-A15.5-8` | keeps prospective and retrospective permission inputs temporally typed and non-productive. | A current grant uses its `validityWindow`; non-prohibition uses its `evaluationWindow`; conflict uses its `overlapWindow` and any subject-pattern resolution `effectiveWindow`. Exercise and non-violation appear only for different dated Work or an explicit post-launch recheck, with their own intervals. None proves another permission value, readiness, gate passage, capability, or target-work performance. |
| `CC-A15.5-9` | keeps the readiness result, domain-local inputs, provenance, assurance, and any inception claim under their subject patterns. | C.2.1 identifies the readiness-result episteme; each measurement, evaluation, resource, permission, gate, or other input keeps its own result algebra; use A.10 for provenance and state any assurance result separately under B.3, and A.15.PROD is opened only for a separately current local entity-identity inception claim. |

