---
chunk_kind: "child"
pattern_id: "A.6.F"
pattern_title: "Function and Functional Precision Restoration (RPR-FUNCTION)"
section_id: "A.6.F:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.F/A.6.F__002_problem-frame.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.6.F — Function and Functional Precision Restoration (RPR-FUNCTION)"
  - "A.6.F:1 — Problem frame"
line_start: 23458
line_end: 23473
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

Use this pattern when `function`, `functional`, `functionality`, `effect`, or similar wording leaves an action-changing object, claim, or applicable rule unresolved. The reading may concern architecture, work, method, capability, a system-role kind or assignment, participation, actual functioning, responsibility, quality, mathematics, module allocation, or an interface. These are possible meanings to distinguish, not one semantic kind.

First recover the question the recipient needs to answer. An approved design can settle what it assigns a part to do. To explain a capability of the whole, show how the part and its partners can produce or maintain the required condition together. To explain an occurrence, use the conditions and interactions that actually obtained. Give the repaired claim and the next useful action. The optional `FunctionUseRepair` note in §4.2 serves uses that need inspectable detail.

Stop when the source cue, entity, value, claim, or claim-bearing episteme, subject pattern, and the next admissible use are clear. If the next step must test whether named participants stand in a relation, add its admitted direct predicate. If it must preserve an affirmative, negative, or modal claim about that predicate, identify the `C.2.1` relational-assertion episteme and its claim. If it must track one particular obtaining instance, apply the subject pattern's identity rule and add the separately individuated occurrence. Otherwise leave those three branches empty. Add reusable declaration, other selected assertion, specification, or view episteme, or representation correspondence only when the next step needs it.

Misreadings to repair: a function becomes a root kind; functional architecture becomes a peer ontology beside architecture; a capability becomes a function; a method or work occurrence becomes a function; a mathematical function becomes design ontology; a module allocation becomes functional truth; or a quality claim hides behind "functionality".

What A.6.F buys in practice: the practitioner can keep useful engineering language while naming the object or claim and going straight to its subject pattern. Direct participation, reusable declaration, claim-bearing description, and representation remain separate instead of becoming one generic function record.

Keep already clear wording, including an FPF claim whose object, meaning and applicable rule are recoverable. For a general relation question, evaluative language, grounded architecture adequacy, or an architecture structural view, use `A.6.P`, `C.16.Q`, `C.30`, or `C.30.ASV` respectively.

**E.10.ARCH subject-pattern relation.** When `E.10` encounters function-like wording whose entity, value, claim, claim-bearing episteme, direct relation, or subject pattern is hidden, `E.10.ARCH` may apply `A.6.F` until that object and the remaining action are clear or the wording is lowered to ordinary prose, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite. A direct relation names its actual participants; a reusable `RelationSignature` and declaration-local `SlotSpec`s, selected assertion, specification, or view episteme, and representation correspondence are added only for a current receiving use. After recovery, apply the subject pattern; `A.6.F` alone establishes no architecture, mathematics, quality, work, evidence, assurance, gate, decision, or release claim.

