---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "EntityOfConcern, Description Episteme, and Specification-Use Discipline"
section_id: "E.10.D2:5"
section_title: "Naming discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__007_naming-discipline.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline"
  - "E.10.D2:5 — Naming discipline"
line_start: 75164
line_end: 75175
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.2.6"
  - "A.3.2"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "E.10"
  - "E.10.D1"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "Description episteme"
  - "DescriptionContext"
  - "EntityOfConcern"
  - "specification use"
  - "testable"
  - "verifiable"
---

### E.10.D2:5 - Naming discipline

**Default suffix.** Use `...Description` when naming a description episteme for a practitioner-facing use.

**Reserved suffix.** Use `...Spec` only when the specification-use conditions above obtain. Do not use it as a synonym for detailed, official, approved, formal-looking, or stored in a schema.

**Entity names.** Name the EntityOfConcern by its independently governed kind and identity: one exact local system-role kind, `Method`, `System`, `Architecture`, `Characteristic`, `PromiseContent`, `Work`, `Episteme`, or another exact kind. Append `Description`, `Spec`, `View`, `Publication`, `Form`, `Carrier`, or `Representation` only when that neighboring object is what the name actually designates.

**Relation language.** Prefer the direct governing verb: a description carries claims about an entity; a publication occurrence makes an edition available; a carrier bears a form; a representation corresponds under a scheme; evidence supports an assertion; an admitted system performs work. Do not turn those verbs into one generic description link.

**Ambiguous role language.** When source wording says that a description, source, standard, requirement, evidence item, publication, dashboard, or view “has a role,” recover its exact evidence-use, source-use, standard-use, requirement-use, publication-use, assurance-use, or gate-use relation. For a claimed Work use, name the exact premise, governed reference, decision-use relation, or A.6.1 operation-argument binding and its actual participants. If the claimed use needs another relation and no direct governor supplies its predicate and participants, return the exact `missing-governor` result rather than inferring a universal description-to-Work or episteme-to-Work relation. Open one exact occurrence of a directly declared `U.SystemRoleAssignment` species only when an independently admitted `U.System` is assigned to one exact local system-role kind for the bounded work; an acting holon is eligible only after that exact entity has independently passed `U.System` admission for this claim.

