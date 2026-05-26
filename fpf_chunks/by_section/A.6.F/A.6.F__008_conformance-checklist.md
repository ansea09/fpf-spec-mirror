---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__008_conformance-checklist.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:7 — Conformance Checklist"
line_start: 14514
line_end: 14529
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.5"
  - "A.6.8"
  - "A.6.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.6.Q"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.SEMIO"
  - "E.18"
  - "E.8"
  - "F.18"
  - "G.6"
  - "U.Function"
keywords:
  - "FunctionalStructure"
  - "capability/effect"
  - "function wording"
  - "function-use repair"
  - "functional architecture"
  - "mathematical function"
  - "module allocation"
  - "work/method boundary"
---

### A.6.F:7 - Conformance Checklist


| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A6F-1 Carrier-kind recovery.** | Every function-like phrase that carries a live FPF claim names the recovered carrier kind and, when the claim points to a specific object, the recovered carrier ref. | Add `FunctionUseRepair` or demote the phrase to Plain prose. |
| **CC-A6F-2 No `U.Function`.** | The use does not mint or rely on `U.Function` as a new root kind. | Assign the use to functional view, capability, method, work, role, mathematical lens, quality/characteristic, module allocation, or neighboring pattern. |
| **CC-A6F-3 Functional architecture expansion.** | Functional architecture expands to `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and C.30.ASV when it carries a live architecture claim. | Add the expansion or keep the phrase as ordinary recognition wording. |
| **CC-A6F-4 Function/capability split.** | Capability claims and function/effect claims remain distinct. | Assign capability claims to the current capability-support locus and keep function/effect wording in the functional view or effect record. |
| **CC-A6F-5 Function/work/method split.** | Method, work occurrence, and work result claims do not hide inside function wording. | Assign the claim to `U.Method`, `MethodDescription`, `U.Work`, Work record, or A.15/P2W as live. |
| **CC-A6F-6 Function/role split.** | Responsibility or role expectation wording uses `VP.RoleEnactor` and role/enactor relations when live. | Add the role carrier or remove the role claim from the function phrase. |
| **CC-A6F-7 Mathematical function boundary.** | Mathematical function or relation wording used for support names C.29 lens fields and stop condition. | Add C.29 support posture, preserved/lost structure, and stop condition, or mark mathematical use as ordinary. |
| **CC-A6F-8 Quality/functionality boundary.** | Quality, fitness, characteristic, score, or "functionality" wording recovers bearer and support. | Assign the claim to `C.25`, `C.16`, A.6.Q, `A.17`, `A.18`, or an admitted characteristic-support receiving pattern as live. |
| **CC-A6F-9 Module/interface boundary.** | Functional relation, module allocation, interface, signature, port, API, protocol, flow, and mechanism wording remain separated. | Add `FunctionFlowModuleAlignmentNote`, `InterfaceSignatureBoundaryNote`, declared correspondence/allocation, or exact module/interface repair. |
| **CC-A6F-10 Useful action.** | The repair leaves a surviving admissible move: assign carrier, open functional view, add alignment note, assign the live claim to C.29/C.30/C.30.ASV/A.15/C.25/C.16/A.10/B.3/A.20/A.21/C.11, or stop. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

