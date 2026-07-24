---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__008_conformance-checklist.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:7 — Conformance Checklist"
line_start: 17972
line_end: 17986
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
  - "A.6.RSIR"
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
  - "C.30.TFS-REL"
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
| **CC-A6F-1 FPF recovery named by value.** | Every function-like phrase that carries an FPF claim being made names the recovered FPF value kind, relation record, slot reference, claim record, view record, or governing-pattern application and, when the claim points to a specific source, the recovered FPF reference. | Add `FunctionUseRepair` or demote the phrase to Plain prose. |
| **CC-A6F-2 No `U.Function`.** | The use does not mint or rely on `U.Function` as a new root kind. | Assign the use to functional view, capability, method, work, role, mathematical lens, quality or characteristic, module allocation, or governing pattern. |
| **CC-A6F-3 Functional architecture expansion.** | Functional architecture expands to `ArchitectureOf@Context` with `structureKindRef = FunctionalStructure` and C.30.ASV when it carries a architecture claim being made. | Add the expansion or keep the phrase as ordinary recognition wording. |
| **CC-A6F-4 Function and capability split.** | Capability claims and function or effect claims remain distinct. | Assign capability claims to the capability-governing pattern or project record named by the claim being made and keep function or effect wording in the functional view or effect record. |
| **CC-A6F-5 Function, work, and method split.** | Method, work occurrence, and work result claims do not hide inside function wording. | Assign the claim to `U.Method`, `MethodDescription`, `U.Work`, Work record, `A.15`, or `E.18.1` according to the asserted method, work, work-result, or P2W carry-through claim. |
| **CC-A6F-6 Function and role split.** | Responsibility or role expectation wording uses `VP.AllocationResponsibility` and role-assignment or responsibility relations when a role claim is being made. | Add the role-assignment or responsibility relation or remove the role claim from the function phrase. |
| **CC-A6F-7 Mathematical function boundary.** | Mathematical function or relation wording used to justify reasoning names C.29 lens fields and stop condition. | Add C.29 lens-use admissibility value, preserved and lost structure, and stop condition, or mark mathematical use as ordinary. |
| **CC-A6F-8 Quality and functionality boundary.** | Quality, fitness, characteristic, score, or "functionality" wording recovers bearer and governing pattern. | Assign the claim to `C.25`, `C.16`, `C.16.Q`, `A.17`, `A.18`, or the characteristic named by value or measurement governing pattern according to the asserted quality, characteristic, measurement, or comparison claim. |
| **CC-A6F-9 Module-interface boundary.** | Functional relation, module allocation, interface, signature, port, API, protocol, flow, and mechanism wording remain separated. | Add `A.6.RSIR` interface-cue recovery, `FunctionFlowModuleAlignmentNote`, a module-interface boundary note governed by `A.6.M`, signature-discipline note governed by `A.6.0` and `A.6.5`, declared correspondence, declared allocation, or `A.6.M` module-relation repair. |
| **CC-A6F-10 Useful action.** | The repair leaves a remaining admissible use: assign the FPF value kind, relation record, slot reference, view record, or governing pattern named by value; open functional view; add alignment note; assign the claim being made to C.29, C.30, C.30.ASV, A.15, C.25, C.16, A.10, B.3, A.20, A.21, or C.11; or stop. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

