---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Object)"
section_id: "A.2.8:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__016_relations.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Object)"
  - "A.2.8:12 — Relations"
line_start: 5762
line_end: 5782
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
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
  - "prohibition"
  - "recommendation-as-duty"
  - "scope and validity window"
  - "they are not the governed object of this pattern"
---

### A.2.8:12 - Relations

**Uses / builds on**

* A.2.1 for identifying accountable roles vs role-enactors (role assignments).
* A.2.6 for expressing scope and time/window (`U.ClaimScope`, qualification-window policy).
* A.7 for keeping source “binding” wording distinct from utterance descriptions and carriers.

**Used by**

* A.6.B (Quadrant D) as the canonical payload shape only for obligation, recommendation-as-duty, and prohibition statements; strong or weak permission, exercise, non-violation, and conflict claims cite the exact `A.2.8.PER` result instead.
* A.6.C (Contract Unpacking) as the formal governing pattern for the “Commitment” component of the bundle.
* Part D governance/ethics patterns, when current, for expressing layered, conflicting, multi-authority commitments.

**Coordinates with**

* A.2.3 (`U.PromiseContent`): services are promise clauses; commitments assign accountable subjects to those clauses.
* **A.2.9 (`U.SpeechAct`)**: `U.Commitment.source.speechActRef` points to the instituting communicative work occurrence when provenance matters.
* A.15.1 (`U.Work`) and evidence patterns: adjudication hooks refer to evidence in work, not to text.
* **A.2.8.PER:** strong grants, permission exercise, weak non-prohibition/non-violation findings, and permission conflicts remain separate from `U.Commitment`; a visible `MAY` or `OPTIONAL` token does not choose between those objects and an `A-*` entry predicate.

