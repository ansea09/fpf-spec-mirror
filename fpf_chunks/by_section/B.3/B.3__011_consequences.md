---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__011_consequences.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:9 — Consequences"
line_start: 39787
line_end: 39802
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

### B.3:9 - Consequences

**Benefits**

- Assurance remains explicit without forcing one cross-domain score.
- A small local claim can stop after six fields.
- Calculations become more trustworthy because assumptions and dependency structure are visible.
- Domain safety, access, responsibility, status, and decision rules retain their own meaning.
- Visible artifacts can contribute useful provenance or evidence without becoming authority.

**Trade-offs**

- B.3 no longer supplies a convenient universal number. A project must use the domain model that gives its inputs meaning.
- Some assurance questions return `unresolved` until a dependency model, calibrated mapping, or direct domain requirement is supplied.
- Reusable replay records cost more than a compact result and therefore require an actual receiver.

