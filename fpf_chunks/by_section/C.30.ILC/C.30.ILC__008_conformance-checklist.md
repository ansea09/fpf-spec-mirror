---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__008_conformance-checklist.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:7 — Conformance Checklist"
line_start: 52004
line_end: 52017
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

### C.30.ILC:7 - Conformance Checklist


| ID | Check | Why it matters |
|---|---|---|
| CC-ILC-1 | A conforming use names `describedHolonRef`, `boundedContextRef`, and the live architecture concern. | Keeps the triage grounded. |
| CC-ILC-2 | A conforming use names declared scopes, not only `level`, `layer`, `scope`, or `scale` prose. | Prevents pseudo-scope reasoning. |
| CC-ILC-3 | A conforming use names the architecture structure kinds affected by the residual. | Keeps the residual architectural rather than generic. |
| CC-ILC-4 | A conforming use records local repair attempted and why local repair was insufficient when a local repair is claimed. | Prevents premature synthesis and repeated local fixes. |
| CC-ILC-5 | A conforming use states one first admissible architecture move or `noArchitectureMove`. | Makes the output action-guiding without opening candidate generation. |
| CC-ILC-6 | Evidence, assurance, measurement, causal, ethical, selection, scale, and mathematical-lens claim kinds exit to their governing patterns. | Prevents triage from becoming proof or synthesis. |
| CC-ILC-7 | If a source-return condition is live, the record states what hidden or lost distinction triggers return to the source. | Protects compressed and extracted views. |
| CC-ILC-8 | The stop condition is visible. | Prevents the triage pattern from expanding into a hidden prescribed sequence. |

