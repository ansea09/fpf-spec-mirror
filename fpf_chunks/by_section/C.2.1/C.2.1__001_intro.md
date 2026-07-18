---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__001_intro.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:intro — Intro"
line_start: 38167
line_end: 38196
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15.PROD"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
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

**Use this pattern when.** Use C.2.1 when a theory, model, specification, standard, proof, algorithm description, diagnosis, lesson, diagram, dashboard, or other claim-bearing object needs to remain identifiable while its subject, interpretation, empirical grounding, view, edition, or publication changes.

**Primary working reader.** An engineer or researcher who needs to identify a knowledge object and use it without mistaking its subject, file, view, evidence, or publication for that knowledge object.

**Primary working concern.** Keep one claim-bearing object reidentifiable through empirical grounding, viewing, revision, and publication, and detect when changed claims, subject, or interpretation identify another episteme.

**Primary viewpoint.** The practitioner using, comparing, revising, or publishing that knowledge object while keeping its identity and neighboring relations distinct.

**Primary EntityOfConcern.** The `U.Episteme` ontic: the knowledge holon, its identity-bearing constitution relation, and the neighboring relations needed for empirical grounding, use, change, description, and publication.

**First useful move.** Name the exact work or decision that will rely on the episteme and the uncertainty or choice the episteme is expected to resolve. Then name the claim content, the identified entity those claims concern, and the effective reference scheme that makes the claims interpretable as claims about that entity. If the named work or decision also depends on empirical grounding, classification, viewpoint, view, claim scope, bounded model use, edition succession, description, or publication, add only the neighboring object or direct relation on which it depends, then apply the pattern governing that object or relation.

**What goes wrong if missed.** A file or diagram becomes "the model"; a subject label drifts while the same episteme name is retained; the holon through which claims are empirically inspected, or the viewpoint from which claims are selected, is copied into episteme identity without justification; or a revised publication is mistaken for a changed knowledge object.

**What this buys.** Epistemes can be compared, revised, grounded, viewed, published, and used recursively while ordinary prose stays short. The complete distinction among the episteme, its direct relations, and their assertion, publication, and representation objects remains recoverable without making users restate every object for every claim.

**Not this pattern when.** Use the direct subject pattern when the current question concerns the system, work, method, relation occurrence, or other entity described by an episteme. Use `A.1` for constructive recognition of a candidate under an admitted holon kind, `C.3.2` for a local-kind membership judgment, and `E.24.UK` for FPF U-kind admission. Use `E.17` and `E.24.PUB` for publication, `A.10` and `B.3` for evidence or assurance, `C.29` for a mathematical representation, and `E.10`, `C.2.P`, or `F.18` for precision restoration or naming. C.2.1 governs episteme identity, including the identity of a separately current classification assertion.

