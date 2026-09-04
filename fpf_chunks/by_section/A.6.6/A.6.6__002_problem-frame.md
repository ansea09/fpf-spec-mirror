---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__002_problem-frame.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:1 — Problem frame"
line_start: 19584
line_end: 19613
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.24.UK"
  - "E.8"
  - "F.0.1"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.9"
  - "U.KindBridge"
  - "U.Transfer"
keywords:
---

### A.6.6:1 - Problem frame

FPF repeatedly needs to express a family of situations of the form:

> **A dependent content is admissible, usable, or interpretable only relative to an explicit base.**

Examples occur across several disciplines:

* reference selection and identification (IDs, handles, pointers, registries),
* scale/datums/calibration (measurement traceability, baselines, normalisation),
* grounding of properties and abstractions to objects (attribution; “this property is about that thing”),
* admissibility/assurance (claims linked to evidence, checks, or proofs),
* publication discipline (what a statement is fit to be used for, where, and when).

In drafts, authors often reach for a single umbrella metaphor (frequently “anchor/anchoring”). That metaphor collapses **different ontological situations** and **different operation classes**, blocking precise invariants and making perspective-flips inevitable.

Like A.6.5, this family can expose **typing conflicts across viewpoints**: an endpoint may be named by its self-kind while the selected direct relation expects another participant kind or reference mode. Make that mismatch explicit only when it is current; do not hide it by renaming ends or flipping direction. Use SlotSpecs only when a reusable relation declaration actually needs them.

The structural problem is smaller than the old record shape suggested. Every ordinary basedness assertion first needs only:

1. the actual **dependent**;
2. the actual **base**; and
3. the direct relation and its obtaining test.

Scope, time, evidence, continuity, or a reusable declaration is added only when the direct predicate or one named receiving use depends on it. Until the direct relation is named, umbrella words such as *anchor*, *ground*, *attach*, *support*, or *based on* usually mean only:

> “There is an under-described relation here.”

The repair is therefore progressive: recover and test the direct relation, stop if the assertion is enough, and materialize declaration or assertion machinery only for a concrete later use.

