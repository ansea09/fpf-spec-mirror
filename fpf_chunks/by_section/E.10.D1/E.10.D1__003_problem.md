---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Recovering What “Context” Means in Use"
section_id: "E.10.D1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__003_problem.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.10.D1 — Recovering What “Context” Means in Use"
  - "E.10.D1:2 — Problem"
line_start: 74813
line_end: 74818
dependencies:
  - "A.1.1"
  - "A.2.6"
  - "C.30"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "F.0.1"
  - "F.17"
  - "F.19"
  - "F.9"
keywords:
  - "architecture"
  - "claim scope"
  - "context wording"
  - "environment"
  - "model use"
  - "positive wording repair"
  - "source-local meaning"
  - "viewpoint"
  - "working situation"
---

### E.10.D1:2 - Problem

The word *context* is useful because it points toward locality, but it does not say which locality matters. Terminology work uses source schemes and local senses. Domain-driven design uses a model boundary and relations among model uses. Claims use scopes and qualification windows. Architecture work distinguishes a described holon, actual subject relations, a selected structure, an obtaining `ArchitectureRelation`, and an `ArchitectureClaim`; viewpoint, environment, and operating-condition claims introduce further distinctions. A pattern's Problem frame describes a recognizable situation. A DPF has a domain subject, audience, source basis, and local qualification conditions.

Treating these uses as one `Context` participant, `ContextId`, or two-part `SenseCell(Context, LocalSense)` hides the distinctions supplied by `A.1.1`, `A.2.6`, `C.2.1`, `F.0.1`, `F.17`, and `F.9`. Replacing that proxy with another universal container preserves the failure under a new name.

