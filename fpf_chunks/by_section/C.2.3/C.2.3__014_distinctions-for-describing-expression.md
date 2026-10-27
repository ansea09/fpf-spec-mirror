---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:13"
section_title: "Distinctions for describing expression"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__014_distinctions-for-describing-expression.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:13 — Distinctions for describing expression"
line_start: 52521
line_end: 52568
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.7"
  - "C.2.LS"
  - "C.39"
  - "F.9"
keywords:
  - "Formality assessment"
  - "expression properties"
  - "language-state separation"
  - "local ordinal scale"
  - "partial order"
  - "proof"
  - "specification"
---

### C.2.3:13 - Distinctions for describing expression

The following descriptions identify common contributions. They are neither mutually exclusive classes nor consecutive levels. Select only distinctions needed by the receiving operation.

#### C.2.3:13.1 - Unstructured prose

Free natural language may leave vocabulary, assumptions and connections unstable. It can still preserve an observation or start an inquiry. Identify the ambiguity that obstructs the next use before requiring a more elaborate form.

#### C.2.3:13.2 - Scoped notes

A note can identify its topic and use terms consistently while leaving criteria informal. Naming the subject helps interpretation; it does not by itself formalize a predicate or narrow claim scope. Assess scope separately.

#### C.2.3:13.3 - Structured outline

A coherent section structure helps readers find claims and their grounds. Placeholder criteria can remain inside a complete outline. Editorial organization is useful, but inspect what the filled content actually defines.

#### C.2.3:13.4 - Controlled narrative

Constrained prose can stabilize interpretation and state acceptance or refusal conditions. This may be sufficient for a competent reader's decision. Automatic interpretation needs an additional mapping or semantics when the prose itself does not supply one.

#### C.2.3:13.5 - Explicit predicates and constraints

Typed entities, bound variables, units, domains and an interpretation make a predicate recoverable. The claim's consistency or consequence can then be examined under the declared semantics. A written formula with undefined symbols does not supply this contribution; an explicit predicate need not be executable or proved.

#### C.2.3:13.6 - Executable semantics

An expression can define how an interpreter or procedure produces results. Declare the relevant input meanings, operation and output interpretation. This enables a run under those conditions; it does not establish a separate invariant or substitute for its specification. A non-executable formal statement can remain sufficient for a mathematical argument.

#### C.2.3:13.7 - Coupled formalisms

A hybrid controller model can relate discrete transitions to continuous evolution; another account can connect several formal subsystems. State their shared meanings and interconnection obligations. Additional formalisms introduce relations to establish, not an automatic increase in rigor. Assess whether the whole preserves the properties its intended use needs.

#### C.2.3:13.8 - Formally expressed derivation

A derivation states how its conclusion follows from declared premises under an identified calculus. Inspect the essential inferential steps, including their connection to the stated conclusion. A checked derivation in higher-order logic can satisfy this need without translation into dependent type theory.

#### C.2.3:13.9 - Properties expressed in types and proof terms

A dependent type can express a property of a program or mathematical object; a term can carry a derivation of that property under the calculus. Recover the exact proposition, assumptions and term. Distinguish that expression from evidence that the required checker accepted it. Its usefulness may include preventing a particular invalid construction or connecting a program to its specification.

#### C.2.3:13.10 - Higher equalities and univalent foundations

When a question needs relationships among equalities or a particular treatment of equivalence, name those structures and the foundation used to express them. This can change the available construction or proof. It does not strengthen every unrelated invariant or make simpler formal foundations inadequate.

#### C.2.3:13.11 - Keeping the distinctions together

A useful assessment explains which of these contributions cooperate. A controlled requirement can be related to a formal invariant and an executable model, with a derivation connecting the model to the invariant. The links carry claims of their own. Check the required link when its meaning or assumptions change; do not infer the whole connection from the presence of all three documents.

