---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__002_use-this-when.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:0 — Use This When"
line_start: 94789
line_end: 94821
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "admission before naming"
  - "alias"
  - "designation"
  - "durable naming"
  - "governed value or relation"
  - "local phrase"
  - "proposed naming use"
  - "row use"
  - "subject before name"
---

### F.8:0 - Use This When

**Plain name.** Keep, reuse, or strengthen a name.

Use F.8 after the subject is known and a project must decide the smallest naming treatment for one expression and one use. Start only when these four facts are available: the expression, the governed value or relation, its subject pattern, and the proposed naming use.

Typical triggers include:

- a familiar source word may be useful locally but would import the source ontology if promoted;
- a role-like word such as `ReviewerRole`, `AccessRole`, or `EvidenceRole` may name a system-role kind, another governed value or relation, or only ordinary wording;
- an alias, subject-pattern name, or F.17 row may already serve the use, but only within its stated meaning and scope;
- a governed value may need a durable name, public row, or policy identifier; and
- pressure for a new U-kind appears. That last case stops before naming until E.24.UK has returned a stable admission disposition.

**Primary working object.** One F.8 disposition for the expression and proposed use. Ordinary use creates no decision occurrence or result episteme. If a later claim must cite, replay, or assign accountability to the decision itself, use the separately triggered branch in §4.5.

**Primary working reader.** An engineer-manager, analyst, method author, pattern author, or terminology steward choosing whether an expression should stay local, reuse a name, or open a stronger naming path.

**First useful move.** Write the four starting facts. Then try, in order, a local phrase, an existing designation, an alias, the subject pattern's name, and an admitted F.17 row. Stop at the first sufficient result. Open a cell, NameCard, public row, or policy identifier only when the receiving use needs it.

**What goes wrong if missed.** A convenient expression is treated as the subject it merely names. Local or source wording becomes durable ontology; a row or alias gains uses it never admitted; a role-like word hides a kind, description, assignment, Work occurrence, or another governed relation; or a record is mistaken for the decision it describes.

**What this buys.** Teams get short usable names without creating duplicate kinds or naming records. Stronger names are harder to introduce but easier to trust because the governed subject and use remain visible.

**Not this pattern when.**

- For one-off wording repair, use the applicable wording rule—E.10, E.10.ARCH, or A.6.P—or the subject pattern.
- If the governed subject or relation is not yet known, recover it first. For an unsettled U-kind proposal, use E.24.CD when the object is unclear and E.24.UK for admission.
- To constitute a `SystemRoleKindDescription`, use F.4. To assign a system, use A.2.1. For precise performed Work, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated occurrence; add F.6 only when the naming case or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment.
- For an obtaining relation between different local-sense projections, use F.9. Use F.17 when a public, Core-facing, durable, or cross-local row is needed.
- For a status, evidence use, policy, Method, Work, publication, or any other governed subject, use its subject pattern before naming it.
- After F.8 has selected a name family, use F.5 for its naming discipline and F.18 only for a durable naming settlement.

