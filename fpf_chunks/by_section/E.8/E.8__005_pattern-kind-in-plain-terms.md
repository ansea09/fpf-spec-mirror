---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:0.3"
section_title: "Pattern Kind In Plain Terms"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__005_pattern-kind-in-plain-terms.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:0.3 — Pattern Kind In Plain Terms"
line_start: 56232
line_end: 56243
dependencies:
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.8.ECSPF"
  - "E.9"
  - "E.9.DA"
  - "F.18"
keywords:
  - "). The key words MUST"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT appear inside Definition:/Invariant:/Well-formedness constraint: blocks. When enforceable"
  - "Prevents ambiguity between obligation language and model validity"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SHALL"
  - "SHALL NOT"
  - "SHOULD"
  - "SHOULD NOT"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:0.3 - Pattern Kind In Plain Terms

An FPF pattern is an action-guiding method description for a recurring working situation. It is applied by an intended FPF user who recognizes the situation, understands the problem and forces, and then uses the `Solution` to decide what to do, what to stabilize, what to avoid, and what practical change should follow.

A pattern is not a procedure, function, API, workflow engine, parameterized call, or checklist bundle. Its `Problem frame`, `Problem`, `Forces`, `Solution`, `Consequences`, worked slices, and anti-patterns carry the guidance. Its `Conformance Checklist` checks whether that guidance has been applied and authored correctly; it must not replace the `Solution` or turn the pattern into a control form.

The primary content-bearing job is constructive method guidance: the pattern must say what the user should do so the recurring error does not arise. Error prevention, auditability, and conformance checks are evidence that the guidance is usable; they are not the pattern's center.

When an action-adjacent pattern classifies wording, a name, a publication face, an explanation class, a comparison unit, or another semio-facing object, that classification is only useful if it returns to action guidance. The pattern must say what use or action is admissible now, what neighboring use or action is not admissible under the current pattern, and which exact neighboring FPF pattern governs the case when the live claim has become work, evidence, gate, decision, assurance, engineering justification, release, or reliance.

`Semio-Echoing` is admissible only as a trigger-controlled auxiliary placement. Use it when `E.10`, `C.2.P`, or `E.10.ARCH` has exposed a live wording-use overread whose EntityOfConcern, episteme/publication stack, alignment path, and remaining admissible reader move are recoverable by value. Do not add it as a generic warning block. In non-semio patterns the primary content remains the pattern's own `EntityOfConcern` and admissible move; semio material stays as a thin cue, exact neighboring-pattern exit, local recovery line, or named description and publication-use boundary section unless it changes that move or blocks a live overread. If the material mainly says that a description, view, publication, record, card, diagram, source, or file is not a permission, promise, prescription, evidence item, assurance verdict, decision, gate passage, release, work occurrence, or authority source, keep it out of the subject Solution and put it in that boundary section or in the exact description-publication pattern.

