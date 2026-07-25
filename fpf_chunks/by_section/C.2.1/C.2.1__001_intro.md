---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__001_intro.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:intro — Intro"
line_start: 40371
line_end: 40408
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

## C.2.1 - `U.Episteme`: Constitution, Empirical Grounding, and Edition Relations

> **Type:** Pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly marked informative

**Plain name.** Episteme constitution.

**Mint or reuse.** This pattern reuses `U.Episteme`, `U.ClaimGraph`, `U.Entity`, `U.ReferenceScheme`, `U.Holon`, `U.Signature`, `RelationSignature`, and `SlotSpec`. It introduces the direct relation names `EpistemeConstitutionRelation`, `EpistemeEmpiricalGroundingRelation`, and `EpistemeEditionRelation`; it introduces no U-kind. Each named `...RelationSignature` below is the relation-facing use of one declaration episteme for which the `A.6.0` membership predicate obtains; `A.6.0` therefore recognizes that same individual as a `U.Signature`, not as another identity. The signature-local SlotKinds named below identify participant meanings only inside their stated signatures. An episteme itself has no slots, and repeated slot spelling in another signature establishes no shared SlotKind by spelling alone.

**One-line summary.** A `U.Episteme` is a knowledge holon identified by exact claim content, one exact EntityOfConcern, and the effective `U.ReferenceScheme` that makes those claims interpretable as claims about that entity. `EpistemeConstitutionRelation` is the core direct relation of the episteme ontic. Empirical grounding, viewpoint, view, scope, model use, edition succession, description, publication, carrier, and mathematical representation remain neighboring objects and relations.

**Use this pattern when.** Use C.2.1 when one body of claims about one exact subject, interpreted under one effective reference scheme, must be identified or compared. In ordinary words, identify what this body of knowledge says, what it says about, and which shared rules make that saying interpretable.

Changed claims, a changed subject, or a changed interpretation identify another episteme. Changed empirical grounding, viewpoint or view use, publication, form, carrier, or representation can leave the episteme unchanged; update the neighboring object or relation that actually changed.

A theory, model, specification, proof, or diagnosis can therefore be an episteme when the selected object is that claim-bearing whole. A diagram or dashboard has two branches: use C.2.1 when the selected claim-bearing whole satisfies the constitution test above; when the current object is instead its layout, file, display, or correspondence to something else, treat it as a publication form, carrier, or C.29 representation rather than as the episteme.

**Primary working reader.** An engineer or researcher who needs to identify a knowledge object and use it without mistaking its subject, file, view, evidence, or publication for that knowledge object.

**Primary working concern.** Keep one claim-bearing object reidentifiable through empirical grounding, viewing, revision, and publication, and detect when changed claims, subject, or interpretation identify another episteme.

**Primary viewpoint.** The practitioner using, comparing, revising, or publishing that knowledge object while keeping its identity and neighboring relations distinct.

**Primary governed object.** One `U.Episteme`: the claim-bearing knowledge holon being identified or compared.

**Architecture in scope.** C.2.1 also governs that episteme's `EpistemeConstitutionRelation`, `EpistemeEmpiricalGroundingRelation`, and `EpistemeEditionRelation`; it coordinates with the direct owners of viewpoint, view, scope, model use, description, publication, form, carrier, and representation.

**Terminology guard.** The EntityOfConcern **of an episteme** is the exact entity its claims concern. It is not the same field as the primary governed object **of this pattern**.

**First useful move.** Ask three ordinary questions: what is claimed, what exact entity are the claims about, and what designation and interpretation rules make those claims readable about that entity? Where the claims use measurement, comparison, or evaluation rules, name those applicable rules too. Those answers identify the episteme. If identity is all the task needs, stop there. Otherwise name the concrete receiving use—such as comparison, preservation, teaching, publication, inquiry, or decision—and add only the neighboring object or direct relation needed for its next visible sentence or action. Name an unresolved uncertainty or choice only when a real inquiry or decision has one.

**What goes wrong if missed.** A file or diagram becomes "the model"; a subject label drifts while the same episteme name is retained; the holon through which claims are empirically inspected, or the viewpoint from which claims are selected, is copied into episteme identity without justification; or a revised publication is mistaken for a changed knowledge object.

**What this buys.** Epistemes can be compared, revised, grounded, viewed, published, and used recursively while ordinary prose stays short. The complete distinction among the episteme, its direct relations, and their assertion, publication, and representation objects remains recoverable without making users restate every object for every claim.

**Not this pattern when.** Use the direct subject pattern when the current question concerns the system, work, method, relation occurrence, or other entity described by an episteme. Use `A.1` for constructive recognition of a candidate under an admitted holon kind, `C.3.2` for a local-kind membership judgment, and `E.24.UK` for FPF U-kind admission. Use `E.17` and `E.24.PUB` for publication, `A.10` and `B.3` for evidence or assurance, `C.29` for a mathematical representation, and `E.10`, `C.2.P`, or `F.18` for precision restoration or naming. C.2.1 governs episteme identity, including the identity of a separately current classification assertion.

