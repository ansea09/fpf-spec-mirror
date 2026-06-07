---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__008_conformance-checklist.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:7 — Conformance Checklist"
line_start: 13682
line_end: 13696
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
  - "A.6.M"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.2.P"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
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
| **CC-A6F-1 Exact FPF-kind or relation recovery.** | Every function-like phrase that carries a live FPF claim names the recovered FPF kind, relation, claim record, view, or governing-pattern application and, when the claim points to a specific source, the recovered FPF reference. | Add `FunctionUseRepair` or demote the phrase to Plain prose. |
| **CC-A6F-2 No `U.Function`.** | The use does not mint or rely on `U.Function` as a new root kind. | Assign the use to functional view, capability, method, work, role, mathematical lens, quality or characteristic, module allocation, or exact governing pattern. |
| **CC-A6F-3 Functional architecture expansion.** | Functional architecture expands to `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and C.30.ASV when it carries a live architecture claim. | Add the expansion or keep the phrase as ordinary recognition wording. |
| **CC-A6F-4 Function and capability split.** | Capability claims and function or effect claims remain distinct. | Assign capability claims to the exact capability-governing pattern or project record named by the live claim and keep function or effect wording in the functional view or effect record. |
| **CC-A6F-5 Function, work, and method split.** | Method, work occurrence, and work result claims do not hide inside function wording. | Assign the claim to `U.Method`, `MethodDescription`, `U.Work`, Work record, or A.15 and P2W as live. |
| **CC-A6F-6 Function and role split.** | Responsibility or role expectation wording uses `VP.RoleEnactor` and role and enactor relations when live. | Add the role and enactor relation or remove the role claim from the function phrase. |
| **CC-A6F-7 Mathematical function boundary.** | Mathematical function or relation wording used to justify reasoning names C.29 lens fields and stop condition. | Add C.29 lens-use admissibility value, preserved and lost structure, and stop condition, or mark mathematical use as ordinary. |
| **CC-A6F-8 Quality and functionality boundary.** | Quality, fitness, characteristic, score, or "functionality" wording recovers bearer and exact governing pattern. | Assign the claim to `C.25`, `C.16`, C.16.Q, `A.17`, `A.18`, or an admitted characteristic or measurement governing pattern as live. |
| **CC-A6F-9 Module-interface boundary.** | Functional relation, module allocation, interface, signature, port, API, protocol, flow, and mechanism wording remain separated. | Add `FunctionFlowModuleAlignmentNote`, `InterfaceSignatureBoundaryNote`, declared correspondence or allocation, or `A.6.M` module-relation repair. |
| **CC-A6F-10 Useful action.** | The repair leaves a surviving admissible move: assign exact FPF kind or relation, open functional view, add alignment note, assign the live claim to C.29, C.30, C.30.ASV, A.15, C.25, C.16, A.10, B.3, A.20, A.21, or C.11, or stop. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

