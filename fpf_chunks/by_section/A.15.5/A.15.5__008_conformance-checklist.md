---
chunk_kind: "child"
pattern_id: "A.15.5"
pattern_title: "Work-Entry Readiness and Full-Kit Preparation"
section_id: "A.15.5:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.5/A.15.5__008_conformance-checklist.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.15.5 — Work-Entry Readiness and Full-Kit Preparation"
  - "A.15.5:7 — Conformance Checklist"
line_start: 26147
line_end: 26159
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
| `CC-A15.5-1` | names the target intended work or work-boundary concern. | The readiness relation is not floating without a target concern. |
| `CC-A15.5-2` | separates readiness from performed work. | No target `U.Work` occurrence is asserted unless dated work evidence is current. |
| `CC-A15.5-3` | separates full-kit condition from preparation work. | `PreparationWorkRef` is used only when preparation was performed. |
| `CC-A15.5-4` | cites planned baselines without rewriting them. | `SlotFillingsPlanItem` remains a plan-item baseline under A.15.3. |
| `CC-A15.5-5` | keeps gate decisions in A.21. | Readiness labels do not create `GateDecision` without A.21 fields. |
| `CC-A15.5-6` | keeps resource readiness and resource aggregation distinct. | Planned reservations and actual consumption are not merged. |
| `CC-A15.5-7` | states stop, degraded-use, or recheck condition. | The reader can tell whether to stop, probe, commit, launch, or return to a missing governing pattern value. |
| `CC-A15.5-8` | keeps prospective and retrospective permission inputs temporally typed and non-productive. | A current grant, non-prohibition finding, or conflict finding may be a prospective direct input; exercise/non-violation appears only in `PriorWorkEvidenceRefs` for different dated work or in an explicit post-launch recheck after the target work is actual. Neither prior result proves current grant, capability, future exercise/non-violation, readiness, gate passage, or target-work performance; unresolved current conflict blocks or degrades reliance under `A.2.8.PER`. |

