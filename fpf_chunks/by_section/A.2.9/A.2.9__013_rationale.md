---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__013_rationale.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:10 — Rationale"
line_start: 7125
line_end: 7133
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "U.Method"
  - "U.Work"
keywords:
  - "actual communicative occurrence"
  - "admitted speech-act Work kind"
  - "authority-grounding assignment"
  - "evidence carrier"
  - "institutional target and effect"
  - "optional SpeechActRecord"
  - "performing U.System"
  - "publication relation"
  - "utterance description"
---

### A.2.9:10 — Rationale

FPF already relies on communicative acts (approvals, notices, overrides) as operationally meaningful events. A.2.9 therefore admits `U.SpeechAct` as the Work kind, treats each actual act as a temporally bounded Work individual enacting an exact Method, and uses `SpeechActRecord` only for claim-bearing representation. That separation keeps performer, obtaining assignment, role and recognition taxonomies, effective schemes, any receiving claim scope, optional MethodDescription and channel, act interval, utterance descriptions, carriers, and separately governed effect intervals and deontic relations (`U.Commitment` or `GrantedPermissionRelation@Context`) inspectable without letting a record stand in for actuality.

This also improves modularity:

* **F.18** can remain a **lexical entry point** for naming (why “SpeechAct” and “utterance” are useful labels),
* while **A.2.9** carries the ontology and conformance discipline for the kind, its actual occurrences, their optional records, and their connections to commitments, granted permissions, and evidence.

