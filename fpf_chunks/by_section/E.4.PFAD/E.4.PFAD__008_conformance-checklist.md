---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__008_conformance-checklist.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:7 — Conformance Checklist"
line_start: 70740
line_end: 70752
dependencies:
  - "A.6.RCD"
  - "A.6.REL"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFAD.1 Opening discriminator | A later-use edition, dependency, pattern-placement or relation, or publication/access boundary makes the architecture question live. |
| CC-PFAD.2 Cheap exit | A route or stop that settles no such boundary closes without PFAD or a DRR. |
| CC-PFAD.3 One decision record | Every selected DPF, access-only, or stop answer after the question opens is recorded in one ordinary `E.9` DRR. |
| CC-PFAD.4 Compact payload | The DRR carries the seven framework-specific content groups in `E.4.PFAD:4.2` and ordinary E.9 rationale. |
| CC-PFAD.5 Direct relation assertions | Relations among initial patterns are stated directly under their actual relation functions; no PFR row is required. |
| CC-PFAD.6 Object boundaries | Answer, acceptance, DRR, authoring, edition, and publication remain distinct. |
| CC-PFAD.7 Conditional apparatus | Proposal, source-return, naming, quality, admission, currentness, and package details appear only when they change the answer or serve a named later use. |
| CC-PFAD.8 Reopen condition | The DRR states what change in framework boundary or receiving use requires reconsideration. |

