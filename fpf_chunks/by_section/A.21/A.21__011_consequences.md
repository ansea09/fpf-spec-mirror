---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__011_consequences.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:9 — Consequences"
line_start: 34612
line_end: 34617
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:9 - Consequences

The gate result is smaller and more truthful. It preserves repair information, prevents unknown or unrun required checks from disappearing, and makes profile change auditable without turning a path boundary into authority. Ordinary gates stop after one result and short rationale; publication, replay, crossing, safety, regulation, and assurance add cost only when their claims are current.

The cost is explicit identity. A practitioner must name the decision subject, profile application, and each required check application instead of relying on labels such as “green”, “Core”, or “regulated”.

