---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:12"
section_title: "Archetypal Grounding - worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__014_archetypal-grounding-worked-cases.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:12 — Archetypal Grounding - worked cases"
line_start: 86773
line_end: 86792
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:12 - Archetypal Grounding - worked cases

#### F.17:12.1 - Role name becomes public across two project contexts

A project has `ReviewerRole@DesignReview` and `ReviewerRole@ExternalAudit`. The local expressions both say "reviewer", but one concerns a system-in-role performing design review work and the other concerns an assurance actor producing an audit report.

The UTS row does not declare one universal reviewer. It either creates two rows or one row with an explicit `F.9` bridge and loss note. Each row cites the direct role pattern, the RoleDescription when current, and the `F.18` NameCardRef. If evidence or assurance is current, `A.10` or `B.3` governs that separate row or note.

#### F.17:12.2 - Status label looks like a role name

A team proposes `BlockedReviewer` as a public label. F.17 does not accept it as a row until the direct patterns are separated. `Reviewer` is a role value; `blocked` is a status-family value or status-window value. The sheet may publish `Reviewer` as a role row and `Blocked` as a status row, with a note that a local UI may render them together. The table does not create a role called "blocked reviewer".

#### F.17:12.3 - Relation and slot names become reusable

An architecture pattern needs public names for `interfaceSlot`, `providedPort`, and `requiredPort`. The UTS row cites `A.6.5` for slot discipline, `A.6.RSIR` when the relation-signature-interface boundary is current, and `F.18` for durable names. The row does not treat a slot name as a component, role, or capability. If a project context uses `port` differently, the UTS row keeps the local sense and bridge explicit.

#### F.17:12.4 - Misleading evidence-role row

A sheet has a row labelled `Evidence role`. F.17 repairs the row by recovering the governed object instead of treating that label as a U-kind. If the claim is that an episteme is being used as evidence for another claim, `A.10`, `B.3`, or `A.2.4` governs the evidence relation. If the claim is that a system performs evidence-producing work, `A.2.1`, `F.6`, and `A.15.1` govern role assignment and performed work. The UTS may publish names for these values, but it must not keep a generic evidence-role row that fuses them.

