---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection"
section_id: "E.24.CD:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__002_use-this-when.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.24.CD — Ontic Candidate Detection"
  - "E.24.CD:0 — Use This When"
line_start: 82693
line_end: 82719
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.2.DA"
  - "E.21"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:0 - Use This When

Use this pattern when a recurring FPF construct is an ontic candidate, but the current source material is still a tangle of names, fields, cards, records, tables, schemas, diagrams, views, examples, or nearby pattern fragments.

Typical moments:

- one word such as "process", "source", "quality", "architecture", "problem", "view", "role", "function", "mechanism", or "method" keeps pointing to several FPF values at once;
- several patterns repeat a similar slot list, field list, boundary formula, or generic semio warning;
- a project data structure looks concept-shaped, but it may only be a publication form or local record;
- a draft ToC row or older source label names a family that no current pattern yet governs;
- a proposed new `U.*` kind feels useful, but it might duplicate existing governing patterns.

**First useful move.** Recover the recognizable project concern first, then list the typed FPF values and relation positions that the source material compresses. Only then classify the case as durable ontic candidate, local use frame, direct governing-pattern use, publication-form-only case, or source wording to keep quote-only or reduced-use.

**What goes wrong if missed.** FPF grows a hidden ontology. A table becomes a kind, a card becomes a subject, a draft label becomes authority, and a convenient word creates a second ontology over values that already have governing patterns.

**What this buys.** The author gets a compact candidate cluster and a sufficiency rationale before opening `E.24`. This keeps E.24 small and keeps candidate discovery from becoming a registry, score form, or warning catalogue.

**Not this pattern when.**

- If the durable ontic is already selected and its identity and slot relation must be governed, use `E.24`.
- If the current question is whether a `U.*` spelling in a heading, title, filename, ToC row, table, or source passage should be retained, demoted, or repaired, recover the concern and use `E.24.UK`.
- If the current problem is only confusion between an ontic, its description, and publication forms, use `E.24.PUB`.
- If an existing subject pattern already governs the claim, use that pattern directly.
- If the issue is one wording-use repair, use `E.10`, `E.10.ARCH`, or the relevant precision-restoration pattern.
- If the contested question is how to compare pattern-set architecture alternatives, construct the evaluation `CharacteristicSpace` through `A.19.ECS`.

