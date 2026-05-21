---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Object)"
section_id: "A.2.9:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__011_rationale.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Object)"
  - "A.2.9:10 — Rationale"
line_start: 5545
line_end: 5553
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Work"
keywords:
  - "act≠utterance≠carrier"
  - "approval/authorization/publication/revocation"
  - "communicative work"
  - "institutes"
  - "judgement context"
  - "provenance"
  - "speech act"
  - "window/freshness"
---

### A.2.9:10 — Rationale

FPF already relies on communicative acts (approvals, notices, overrides) as operationally meaningful events, but without a kernel object they blur into examples, naming choices, or prose. A.2.9 anchors speech acts where they belong: as a **Work-kind** with explicit performer, scope, and time, and with disciplined links to utterance surfaces, carriers, and deontic bindings (`U.Commitment`).

This also improves modularity:

* **F.18** can remain a **lexical anchor** for naming (why “SpeechAct/utterance” as a label family is useful),
* while **A.2.9** carries the ontology and conformance discipline for how speech acts behave as objects and how they connect to commitments and evidence.

