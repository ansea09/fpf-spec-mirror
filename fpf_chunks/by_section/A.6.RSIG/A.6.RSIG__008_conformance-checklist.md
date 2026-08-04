---
chunk_kind: "child"
pattern_id: "A.6.RSIG"
pattern_title: "Recognition Signatures for Descriptions"
section_id: "A.6.RSIG:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIG/A.6.RSIG__008_conformance-checklist.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.6.RSIG — Recognition Signatures for Descriptions"
  - "A.6.RSIG:7 — Conformance checklist"
line_start: 10200
line_end: 10221
dependencies:
  - "A.6"
  - "A.6.P"
  - "E.10"
  - "F.18"
keywords:
---

### A.6.RSIG:7 - Conformance checklist

- **CC-RSIG-1 First-contact only.** The pattern governs recognition of the
  right description, not the full semantics of that description.
- **CC-RSIG-2 Carrier/definition-episteme split.** A conforming description-recognition signature
  distinguishes `description_seen`, encountered carrier or projection,
  defining `U.Episteme`, and projection role when those distinctions are
  load-bearing. The encountered carrier or projection may help recognition,
  but it does not become authoritative merely by being encountered.
- **CC-RSIG-3 Neighbor boundaries explicit.** The text states when entry loads go
  to `A.6.B`, `E.17`, `E.10 / F.18 / A.6.P`, `C.25 / C.16.Q`, or the relevant
  authoritative pattern body.
- **CC-RSIG-4 No kind inflation.** Recognition signatures are not silently
  promoted into `U.Signature`, Signature Stack objects, publication face kinds, publication form kinds, carrier kinds,
  graph objects, workflow objects, or new `U.*` kinds.
- **CC-RSIG-5 Recoverable cue shape.** For load-bearing cases, description,
  viewpoint, cue, applicability, exclusion, defining `U.Episteme`, false neighbor,
  and admissible entry stop remain recoverable.
- **CC-RSIG-6 No alias minting.** Query cues and ordinary phrasing do not become
  aliases, bridges, semantic twins, or lexical authority without applying the relevant
  naming pattern or `authoritySourceRef` target.

