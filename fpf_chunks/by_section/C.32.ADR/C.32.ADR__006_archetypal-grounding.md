---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__006_archetypal-grounding.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:5 — Archetypal Grounding"
line_start: 61084
line_end: 61093
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.ADA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
keywords:
  - "ADR projection"
  - "ArchitectureDecisionDescription@Project"
  - "ArchitectureDecisionRecordProjection@Project"
  - "architecture decision record"
  - "consequences"
  - "method-use instruction"
  - "publication boundary"
  - "rationale"
  - "section function"
  - "supersession"
---

### C.32.ADR:5 - Archetypal Grounding

**Software ADR.** A team publishes an ADR for event-carried integration. The record uses local headings, but the function rows recover context, options, selected outcome, rationale, consequences, method-use instruction for event schema work, confirmation eval, and supersession. Developers can see what to implement and when the decision reopens.

**Manufacturing trade-study record.** A fixture decision is published as an engineering trade-study memo rather than a Markdown ADR. The memo carries candidate fixture variants, selected universal-fixture scope, accepted setup-time loss, cell-design method instruction, evidence links, and reopen threshold. C.32.ADR admits the memo because it projects the decision description for the intended reader.

**Certification rationale.** A regulated product records a safety-architecture decision in a certification rationale. The record carries the decision outcome, rationale, evidence refs, architecture-description refs, and confirmation path, while evidence and assurance claims stay in `A.10` and `B.3`.

**Method-governance record.** A method family decides that reviewers must use an evidence handoff pattern before final review. The ADR-like record cites the method description and expected evidence-structure effect; it does not become the method itself or the performed review work.

