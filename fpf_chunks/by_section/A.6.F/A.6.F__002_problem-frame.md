---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__002_problem-frame.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:1 — Problem frame"
line_start: 17568
line_end: 17600
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.8"
  - "A.6.9"
  - "A.6.B"
  - "A.6.C"
  - "A.6.M"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.18"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.6"
keywords:
  - "FunctionalStructure"
  - "actual transformation"
  - "capability"
  - "episteme/publication boundary"
  - "function wording"
  - "functional architecture"
  - "mathematical function"
  - "method-description membership"
  - "module allocation"
  - "required behavior or effect"
  - "work"
---

### A.6.F:1 - Problem frame

Use this pattern when `function`, `functional`, `functionality`, `effect`, or a similar function-like phrase carries an FPF-governed use beyond ordinary prose. The reading to inspect may concern architecture, work, method, capability, role, quality, mathematics, module allocation, an interface, or another claim named by value. These are recognition and dispatch possibilities, not one semantic kind.

The first useful move is small:

```text
FunctionUseRepair:
phrase:
sourceCueText?:
functionLikeReadingUnderRepair:
exactGovernedObjectOrClaim:
directRelationPredicateUse?:
relationalAssertionUse?:
obtainingRelationOccurrenceUse?:
reusableDeclarationUse?:
selectedClaimBearingEpistemeUse?:
representationUse?:
directGoverningPatternApplicationRefs?:
blockedLocalOverreadRefs:
nextAdmissibleUse:
stopCondition:
```
Stop when the source cue, exact governed entity, value, claim, or claim-bearing episteme, direct owner, the one local overread that would change this repair, and the next admissible use are clear. If the next step must test whether named participants stand in a relation, add its admitted direct predicate. If it must preserve an affirmative, negative, or modal claim about that predicate, identify the exact `C.2.1` relational-assertion episteme and its claim. If it must track one particular obtaining instance, apply the direct owner's identity rule and add the separately individuated occurrence. Otherwise leave those three branches empty. Add reusable declaration, other selected assertion, specification, or view episteme, or representation correspondence only when the next step needs it.

What goes wrong if A.6.F is missed: a function becomes a root kind; functional architecture becomes a peer ontology beside architecture; a capability becomes a function; a method or work occurrence becomes a function; a mathematical function becomes design ontology; a module allocation becomes functional truth; or a quality claim hides behind "functionality".

What A.6.F buys in practice: the practitioner can keep useful engineering language while naming the exact governed object or claim and going straight to its direct owner. Direct participation, reusable declaration, claim-bearing description, and representation remain separate instead of becoming one generic function record.

Not this pattern when the phrase is ordinary prose and carries no FPF claim being made. If the issue under repair is a general relation word, evaluative language, grounded architecture adequacy, or an architecture structural view, use `A.6.P`, `C.16.Q`, `C.30`, or `C.30.ASV` respectively.

**E.10.ARCH governing-pattern relation.** When `E.10` encounters function-like wording whose exact governed entity, value, claim, claim-bearing episteme, direct relation, or governing pattern is hidden, `E.10.ARCH` may apply `A.6.F` until that object and the remaining action are clear or the wording is lowered to ordinary prose, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. A direct relation names its actual participants; a reusable `RelationSignature` and declaration-local `SlotSpec`s, selected assertion, specification, or view episteme, and C.29 representation correspondence are added only for a current receiving use. After recovery, apply the direct governing pattern; `A.6.F` does not own architecture, mathematics, quality, work, evidence, assurance, gate, decision, or release claims by function wording alone.

