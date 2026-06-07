---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 13697
line_end: 13709
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

### A.6.F:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Root function kind** | The text treats function as a new universal FPF kind. | Use `FunctionUseRepair` and assign the use to an existing FPF kind, relation, claim record, view, or governing-pattern application. |
| **Functional architecture exception** | Functional architecture is treated as a peer architecture ontology. | Expand to `FunctionalStructure` under `ArchitectureOf@Context` and C.30.ASV. |
| **Capability collapse** | What the holon can do is treated as a functional dependency or vice versa. | Split capability claim from functional relation or effect claim. |
| **Work collapse** | Work occurrence or result is described as a function. | Assign occurrence or result claims to A.15 and P2W and keep functional wording design-side unless work evidence is live. |
| **Mathematical-function import** | A mathematical function, loss, objective, or value functional becomes design ontology. | Use C.29 and state preserved and lost structure plus stop condition. |
| **Module allocation shortcut** | A function is considered implemented because a module is named. | Add correspondence, allocation, interface-signature boundary, or `A.6.M` module-relation repair. |
| **Functionality as quality proxy** | "Functionality" carries adequacy or quality claim without bearer and exact governing pattern. | Recover bearer and exact governing pattern through `C.25`, `C.16`, C.16.Q, or an admitted characteristic or measurement governing pattern. |
| **Sterile exact-kind repair** | The wording is typed but no useful move remains. | Restore the exact-kind or relation assignment, functional view, alignment note, or exact governing pattern application. |

