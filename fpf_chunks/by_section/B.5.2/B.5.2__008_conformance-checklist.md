---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__008_conformance-checklist.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:7 — Conformance Checklist"
line_start: 32644
line_end: 32652
dependencies:
  - "A.10"
  - "A.16"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:7 - Conformance Checklist

- `CC-B.5.2-1` Every abductive run **SHALL** begin from a declared `U.AbductivePrompt`; arbitrary prose fragments are not sufficient prompt-entry forms.
- `CC-B.5.2-2` A conforming abductive run **SHALL** record at least one rival candidate alongside any selected prime hypothesis, unless the author explicitly justifies why no rival candidate was available.
- `CC-B.5.2-3` Selection of a prime hypothesis **SHALL** cite at least two explicit plausibility filters.
- `CC-B.5.2-4` The selected prime hypothesis **SHALL** be published as a new `U.Episteme` with `AssuranceLevel:L0`.
- `CC-B.5.2-5` The prime hypothesis record **SHALL** preserve a link to the initiating prompt and to the filtering rationale that justified selection.
- `CC-B.5.2-6` A hypothesis that cannot support any downstream deduction, probe design, or evidence path **SHALL NOT** be presented as a conforming abductive result.

