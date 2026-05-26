---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__002_problem-frame.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:1 — Problem frame"
line_start: 14266
line_end: 14289
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

### A.6.F:1 - Problem frame

Use this pattern when `function`, `functional`, `functionality`, `effect`, or a similar function-like phrase carries a live FPF claim beyond ordinary prose. The claim kind may be architecture, work, method, capability, role, quality, mathematical, module-allocation, interface, decision, evidence, or gate.

The first useful move is small:

```text
FunctionUseRepair:
phrase:
liveUse:
recoveredCarrierKind:
recoveredCarrierRef?:
falseCarrierKindRefs:
nextAdmissibleMove:
stopCondition:
```
Stop when the recovered carrier kind, any needed carrier ref, false carrier kinds, and the next admissible move are clear.

What goes wrong if A.6.F is missed: a function becomes a root kind; functional architecture becomes a peer ontology beside architecture; a capability becomes a function; a method or work occurrence becomes a function; a mathematical function becomes design ontology; a module allocation becomes functional truth; or a quality claim hides behind "functionality".

What A.6.F buys in practice: the practitioner can keep useful engineering language while recovering the exact carrier and the neighboring pattern that carries any remaining claim kind.

Not this pattern when the phrase is ordinary prose and carries no live FPF claim. If the live issue is a general relation word rather than function-like wording, use A.6.P. If the live issue is evaluative language, use A.6.Q. If the live issue is architecture-description adequacy, use C.30. If the live issue is an architecture structural view, use C.30.ASV.

