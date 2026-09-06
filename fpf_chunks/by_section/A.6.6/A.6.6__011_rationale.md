---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__011_rationale.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:10 — Rationale"
line_start: 19978
line_end: 19994
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.24.UK"
  - "E.8"
  - "F.0.1"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.9"
  - "U.KindBridge"
  - "U.Transfer"
keywords:
---

### A.6.6:10 - Rationale

**Why focus on base declaration rather than a metaphor.**
The recurring ambiguity is not “how to attach”, but which direct relation is being asserted between which participants. A readable relation-specific sentence exposes that answer; an optional declaration can then preserve it for a named reuse.

**Why keep the direct relation, assertion, and evidence separate.** The relation's predicate determines whether the world-side fact obtains. A C.2.1 episteme may assert it, and A.2.4/A.10 may support reliance on that assertion. Conflating these objects lets a record or carrier stand in for truth.
A base is a participant in the selected direct relation. Evidence or other supporting material justifies an assertion only through its own direct relations. Conflating the two makes both reasoning and audit unreliable.

**Why add scope and `Gamma_time` conditionally.** They are required when the direct predicate or receiving use changes across extent or time. Adding them everywhere hides the ordinary relation behind a universal qualifier form.
A declaration is never “everywhere forever” by default in FPF. Scope makes applicability explicit; `Γ_time` prevents hidden time dependence (“recent”, “current”, “latest”).

**Why prohibit kind edits.**
Changing the relation kind changes meaning; treating it as an update erases history and breaks continuity discipline.

**Why retain a local declaration-change lexicon.** When a named receiver tracks assertion or declaration history, the labels distinguish which episteme field changed. They are optional and do not describe actual relation change without the direct relation's own predicate.
Without explicit change classes, prose collapses distinct edits (rebase vs retime vs rescope vs witness refresh) and recreates the same ambiguity A.6.5 removed at the slot layer.

