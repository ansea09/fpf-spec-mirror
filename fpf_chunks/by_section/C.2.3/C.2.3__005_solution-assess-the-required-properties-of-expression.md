---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:4"
section_title: "Solution - Assess the required properties of expression"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__005_solution-assess-the-required-properties-of-expression.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:4 — Solution - Assess the required properties of expression"
line_start: 52266
line_end: 52313
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

### C.2.3:4 - Solution - Assess the required properties of expression

Formality is assessed on a named expression of an episteme's content. Establish what its next use requires, recover the relevant interpretation and inferential relations, and inspect the actual expression against those requirements. Keep independent properties distinct. A shared profile makes their combination visible; a local summary is useful only when its declared criteria preserve the distinctions the receiving use needs.

#### C.2.3:4.1 - Subject and representation of the assessment

**F** names the formality assessment in an account that also uses G and R. It is not a globally ordered atomic `U.Characteristic`, and this pattern supplies no universal `U.Formality` value or `F0...F9` scale. The assessed subject is an exact claim, declaration, model or argument expressed by an episteme. State which parts and connecting inferences belong to that assessment.

An ordinary assessment can be a sentence: “The budget condition has declared units, a typed variable and an explicit predicate; no derivation of its adequacy for the project is supplied.” That is enough when it answers the receiving question. For comparison, automation or repeated use, describe the selected expression properties and their values as a profile. The description remains an episteme; a reference such as `formalityRef` points to that assessment and its basis. This introduces no new root U-kind.

If a `CharacteristicSpace` is used, each assessed Characteristic has its own declared Scale and slot under A.18 and A.19. A profile is not one Coordinate containing several unnamed characteristics. Record missing or unknown assessments separately from values; unknown precision is not evidence of low precision. Keep the relevant calculus, assumptions and interpretation recoverable alongside the property assessments.

#### C.2.3:4.2 - Place beside G and R

A named assurance argument may consume F alongside G or R under B.3. The notation `[F,G,R]` is a view of distinct assessments, not automatically a point in one numeric space.

- F concerns expression properties. G concerns applicability or claim scope.
- A derivation expressed in a calculus is part of the assessed content. Evidence that a particular checker accepted it supports that checking claim. Confidence in the checker, its assumptions and the resulting conclusion belongs to the relevant assurance argument.
- A fully expressed empirical claim can have weak or missing empirical support. Formal validity under stated premises and applicability to the world answer different questions.
- Mapping loss is assessed for the receiving use. Any effect on R needs its B.3/C.2.2 basis; an ordinal CL label supplies no automatic penalty.
- A notation, carrier or rendering change preserves the assessment only when it preserves the expression properties on which that assessment rests.

#### C.2.3:4.3 - Comparison and local ordered summaries

Compare profiles only after aligning the assessed properties, their meanings and relevant conditions. One expression can provide a formal predicate while another provides an executable procedure; neither fact alone makes one more formal for every use. A changed use may need both, or may need only one.

When an order is useful, declare its domain and comparison rule. For a fixed compatible basis of independently established requirements, an expression that satisfies all requirements satisfied by another and some additional ones can dominate it under that declared rule. This does not rank the entire languages or establish a preference for every use. Preserve incomparability when different requirements are satisfied; unresolved assessment is a separate result. Use A.19:5.1.3 for an order overlay when a CharacteristicSpace is involved.

A local ordinal summary is possible when its levels have nested criteria. For example, one team's specification-expression scale can require: named objects and stable terms; those conditions plus explicit acceptance predicates and their interpretation; those conditions plus expressed derivations for a specified set of obligations. The last level includes the earlier criteria by declaration. Its proof-checking evidence is still assessed separately. State the exact scale, mapping from the profile, domain and conditions before using its levels or a threshold. Another team's levels are not comparable merely because they use the same numbers.

Arithmetic, averages and numerical differences are not licensed by an ordinal scale. Where a change is described as an increase in formality, identify the strengthened property or the established order that makes that claim meaningful. A new logic, extra subsystem or larger toolchain is not such a property by itself.

#### C.2.3:4.4 - Requirements for a receiving use

Express a formality requirement through what the recipient needs to do. “The invariant has explicit types and semantics, and every inference needed for this proof is expressed in the selected calculus” is a recoverable condition. If checked validity is also required, name that separate evidence requirement. A local ordinal threshold can abbreviate the expression condition only when its named scale captures the required criteria.

Normative content must make the expression conditions needed for its intended use recoverable. A suitable ordinary explanation can do this without a separate score, profile document or formal proof. A richer assessment is required when a comparison, assurance argument or automated consumer actually relies on it. Neither a satisfactory formality assessment nor a threshold result grants permission to act.

Improving the expression changes the assessed content. Correcting an erroneous assessment can instead leave that content unchanged. When the receiving requirement changes, return to the property, formal apparatus, derivation or external support it actually needs; do not automatically raise every part of the expression.

#### C.2.3:4.5 - Assess and improve an expression

1. Identify the exact claim or argument and the next operation: interpretation, execution, combination or checking. Name the required result and any applicable binding requirement.
2. Recover the terms, domains, variable bindings, constraints, operation meanings and inferential connections needed for that operation. Section 13 supplies common distinctions, not a mandatory assessment form.
3. Inspect the expression. State which needed properties it provides and where interpretation, an operation or an inference remains unspecified. Keep a proposed derivation separate from the result of checking it.
4. Test the receiving condition. A sufficient expression ends this inquiry. If a missing property prevents the use, repair that part or obtain a suitable expression. Use C.19.2 to choose and configure formal apparatus when that is the actual question; use C.39 when a way to obtain the needed result still has to be developed.
5. After the change, repeat the affected use, including any connecting inference. Preserve unchanged scope and support assessments unless their own grounds changed. If the repaired expression reveals a different claim or assumption, assess that change explicitly rather than calling it a purely notational improvement.

