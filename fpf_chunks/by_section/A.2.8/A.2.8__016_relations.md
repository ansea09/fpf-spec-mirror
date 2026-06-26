---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Object)"
section_id: "A.2.8:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__016_relations.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Object)"
  - "A.2.8:12 — Relations"
line_start: 5611
line_end: 5630
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "E.8"
  - "U.PromiseContent"
  - "U.Work"
keywords:
  - ") but makes the structure explicit"
  - "BCP‑14 (RFC 2119/8174)"
  - "adjudication hooks"
  - "are cues for the modality field after the deontic relation is recovered"
  - "by themselves"
  - "commitment"
  - "deontics"
  - "evidenceRefs"
  - "modality normalization"
  - "obligation"
  - "permission"
  - "prohibition"
  - "scope+validity window"
  - "they are not the governed object of this pattern"
---

### A.2.8:12 - Relations

**Uses / builds on**

* A.2.1 for identifying accountable roles vs role-enactors (role assignments).
* A.2.6 for expressing scope and time/window (`U.ClaimScope`, qualification-window policy).
* A.7 for keeping source “binding” wording distinct from utterance descriptions and carriers.

**Used by**

* A.6.B (Quadrant D) as the canonical payload shape for deontic statements.
* A.6.C (Contract Unpacking) as the formal governing pattern for the “Commitment” component of the bundle.
* Part D governance/ethics patterns, when current, for expressing layered, conflicting, multi-authority commitments.

**Coordinates with**

* A.2.3 (`U.PromiseContent`): services are promise clauses; commitments assign accountable subjects to those clauses.
* **A.2.9 (`U.SpeechAct`)**: `U.Commitment.source.speechActRef` points to the instituting communicative work occurrence when provenance matters.
* A.15.1 (`U.Work`) and evidence patterns: adjudication hooks refer to evidence in work, not to text.

