---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__002_problem-frame.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:1 — Problem frame"
line_start: 13721
line_end: 13746
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

### A.6.F:1 - Problem frame

Use this pattern when `function`, `functional`, `functionality`, `effect`, or a similar function-like phrase carries an FPF claim being made beyond ordinary prose. The claim kind may be architecture, work, method, capability, role, quality, mathematical, module-allocation, interface, or another FPF claim named by value.

The first useful move is small:

```text
FunctionUseRepair:
phrase:
liveUse:
recoveredFpFKind:
recoveredFpFReference?:
falseFpFKindRefs:
nextAdmissibleMove:
stopCondition:
```
Stop when the recovered FPF kind, any needed FPF reference, false FPF kind references, and the next admissible move are clear.

What goes wrong if A.6.F is missed: a function becomes a root kind; functional architecture becomes a peer ontology beside architecture; a capability becomes a function; a method or work occurrence becomes a function; a mathematical function becomes design ontology; a module allocation becomes functional truth; or a quality claim hides behind "functionality".

What A.6.F buys in practice: the practitioner can keep useful engineering language while recovering the FPF kind or relation named by value and the governing pattern that carries any remaining claim kind.

Not this pattern when the phrase is ordinary prose and carries no live FPF claim. If the issue under repair is a general relation word, evaluative language, grounded architecture adequacy, or an architecture structural view, use `A.6.P`, `C.16.Q`, `C.30`, or `C.30.ASV` respectively.

**E.10.ARCH governing-pattern relation.** When `E.10` encounters function-like wording whose required transformation, capability, method, work, role, mathematical-function use, quality use, module allocation, interface relation, architecture use, FPF kind named by value, relation, claim record, governing pattern, or stop condition is hidden, `E.10.ARCH` sends the case to `A.6.F` only until those fields are recovered or the wording is lowered to ordinary prose, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. `A.6.F` then exits to the governing pattern; it does not own architecture, mathematics, quality, work, evidence, assurance, gate, decision, or release claims by function wording alone.

