---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
section_id: "A.6.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__002_problem-frame.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.6 — U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
  - "A.6.6:1 — Problem frame"
line_start: 15052
line_end: 15087
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.18"
  - "F.9"
  - "U.RelationSlotDiscipline"
keywords:
  - "SWBD"
  - "anchoring"
  - "base declaration"
  - "baseRelation"
  - "basedness"
  - "rebase"
  - "rescope"
  - "retime"
  - "scope"
  - "witnesses"
  - "Γ_time"
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

> **Deconfliction note (lexical).** This pattern is about *base-dependence in content* (“X is usable relative to B”). It is not about E.10’s **Domain Anchoring** (MG-DA), where “anchoring” is a *lexical* primitive for binding token morphology to the term’s described entity. When you see `anchor*` in a basedness sentence, treat it as a defect unless an explicit baseRelation token is present.
>
> **Deconfliction note (context/meaning).** This pattern is also not a license to reintroduce “anchor” as a surrogate for **Context**, **SenseCell**, or “where meaning lives”. Any such use is an *anchor‑relapse* and SHALL be rewritten into explicit Context/SenseCell/ConceptSet lane constructs (E.10 D.CTX), not into SWBD.

Like A.6.5, this family also triggers **typing conflicts across viewpoints**: an endpoint may be spoken about in its self-kind while the baseRelation declaration expects a different ValueKind (or a different `refMode`). If that mismatch is not made explicit (SlotSpec + relation-specific constraints), authors “solve” it by renaming ends or flipping direction, and the ontological obligation (bridge / narrowing / retargeting) is lost.

The structural reason for the collapse is consistent: what looks like “one anchoring” in prose is, in fact, a *based declaration* with at least five components:

1) **Dependent** — what is being made admissible/usable/meaningful,
2) **Base** — what it is relative to: reference frame, evidence carrier, standard, policy, or declared entity,
3) **BaseRelation** — the specific relation kind that states *how* dependent depends on base,
4) **Scope/Time** — where/when the declaration holds (`scope` plus explicit `Γ_time` when time matters),
5) **Witnesses / pins** — what justifies or enforces the declaration when it is used for decisions.

Until **BaseRelation** is named, umbrella words (“anchor”, “ground”, “attach”, “based on”) nearly always mean:

> “There is an under-described type of dependence here.”

This pattern introduces a single stable lens — **the based declaration** — and couples it with a strict lexical discipline and an operation lexicon, so that base-dependence can be expressed precisely across domains without collapsing back into metaphor.

