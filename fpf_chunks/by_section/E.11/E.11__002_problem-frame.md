---
chunk_kind: "child"
pattern_id: "E.11"
pattern_title: "Practical-Use Guidance and Pattern Discovery"
section_id: "E.11:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11/E.11__002_problem-frame.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.11 — Practical-Use Guidance and Pattern Discovery"
  - "E.11:1 — Problem frame"
line_start: 75370
line_end: 75387
dependencies:
  - "A.22.CGUS"
  - "C.2.1"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.17.AUD"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.18"
  - "G.11"
keywords:
---

### E.11:1 - Problem frame

#### E.11:1.1 - Use this when

Use `E.11` when an FPF author or maintainer publishes or refreshes the public practical-use cards that help a practitioner, manager, or assisting agent find which direct pattern to inspect first.

The practitioner, manager, or assisting agent is the reader of that publication, not the performer of E.11's publication method. Their first move is to compare the current README cards by working situation and first result or blocker, then open the direct pattern from the card that best fits the work.

Public guidance answers three questions quickly: "Is this my situation? What useful result could I obtain first? Which direct pattern should I open?" A public example remains a template; it is not a project instance, applicability finding, recommendation, plan, decision, or work occurrence.

**Primary EntityOfConcern.** One context-free public practical-use guidance episteme and its expansion, published through an E.17-conforming public card unit.

**Conditional support object.** A `PracticalUseCardShortlist@Context` is current only when a named receiving use relies on addressable comparison history. It records that bounded comparison; it is not a second public guidance form or the primary `EntityOfConcern`.

**What this buys.** A cold reader can move from an ordinary project question to one or a few inspectable direct patterns. A wrong first choice remains recoverable, while ordinary comparison stays conversational.

**Not this pattern when.** After one direct pattern has been selected, use `E.11.PUA` to follow its conditional `Solution`: identify the first independently governed result and the direct basis for calling it this use's result, or stop when that basis is missing. Use `E.11.PUR` when local applicability, recommendation, coordination, or ordering among candidate pattern uses is current. Use the direct subject pattern for the actual result, plan, work, evidence, decision, or publication claim.

