---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__002_problem-frame.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:1 — Problem frame"
line_start: 18972
line_end: 19007
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "C.2.1"
  - "E.10"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.6.6:1 - Problem frame

FPF repeatedly needs to express a family of situations of the form:

> **A dependent content is admissible, usable, or interpretable only relative to an explicit base.**

This family appears across disciplines:

* reference selection and identification (IDs, handles, pointers, registries),
* scale/datums/calibration (measurement traceability, baselines, normalisation),
* grounding of properties and abstractions to objects (attribution; “this property is about that thing”),
* admissibility/assurance (claims linked to evidence, checks, or proofs),
* publication discipline (what a statement is fit to be used for, where, and when).

In drafts, authors often reach for a single umbrella metaphor (frequently “anchor/anchoring”). That metaphor collapses **different ontological situations** and **different operation classes**, blocking precise invariants and making perspective-flips inevitable.

> **Deconfliction note (lexical).** This pattern is about *base-dependence in content* (“X is usable relative to B”). It is not about E.10’s **Domain Anchoring** (MG-DA), where “anchoring” is a lexical primitive. In a basedness sentence, `anchor*` is a defect until the actual participants, relation-specific verb, and direct predicate are recoverable.
>
> **Deconfliction note (source-local meaning).** This pattern is not a license to use “anchor” for a source, meaning, or the thing that supposedly makes a word mean something. Recover the exact source and edition, effective `ReferenceScheme`, local expression, local-sense claim, and exact supporting passage under F.0.1. Create an F.17 `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` only when a later use needs that durable address or support claim. A small source note or Card may represent an already constituted episteme; its form supplies no meaning and is not a special base-declaration object.
>
> **Deconfliction note (support wording).** This pattern constrains *support* only when the claim is base-dependence: one identified dependent is usable, admissible, interpretable, comparable, publishable, or actionable relative to one identified base through a named direct relation. Ordinary help, source discovery, reader navigation, work enablement, evidence use, assurance, causal use, mathematical-lens use, and publication companionship keep their own direct accounts. A support phrase that cannot select one reading remains a cue, not a declaration.

Like A.6.5, this family can expose **typing conflicts across viewpoints**: an endpoint may be named by its self-kind while the selected direct relation expects another participant kind or reference mode. Make that mismatch explicit only when it is current; do not hide it by renaming ends or flipping direction. Use SlotSpecs only when a reusable relation declaration actually needs them.

The structural problem is smaller than the old record shape suggested. Every ordinary basedness assertion first needs only:

1. the actual **dependent**;
2. the actual **base**; and
3. the direct relation and its obtaining test.

Scope, time, evidence, continuity, or a reusable declaration is added only when the direct predicate or one named receiving use depends on it. Until the direct relation is named, umbrella words such as *anchor*, *ground*, *attach*, *support*, or *based on* usually mean only:

> “There is an under-described relation here.”

The repair is therefore progressive: recover and test the direct relation, stop if the assertion is enough, and materialize declaration or assertion machinery only for a concrete later use.

