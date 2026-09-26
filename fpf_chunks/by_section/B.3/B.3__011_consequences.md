---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Is This Claim Supported for This Use? — Trust and Assurance Calculus"
section_id: "B.3:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__011_consequences.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "B.3 — Is This Claim Supported for This Use? — Trust and Assurance Calculus"
  - "B.3:9 — Consequences"
line_start: 42128
line_end: 42143
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "B.1.5"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.5"
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

- B.3 supplies no convenient universal number. A project must use the domain model that gives its inputs meaning.
- Some assurance questions remain unresolved until a dependency model, calibrated mapping, or direct domain requirement is supplied.
- Reusable replay records cost more than a compact result and therefore require an actual receiver.

