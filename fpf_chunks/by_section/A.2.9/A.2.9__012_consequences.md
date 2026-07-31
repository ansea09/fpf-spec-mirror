---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__012_consequences.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:9 — Consequences"
line_start: 7037
line_end: 7049
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

### A.2.9:9 — Consequences

**Benefits**

* Makes approvals/authorizations/notices **first-class and queryable**, enabling clean RSG checklists and guard rules.
* Provides stable provenance: commitments, granted permissions, and status transitions can cite the **instituting act** explicitly.
* Prevents recurring category errors: “documents promise”, “interfaces commit”, “logs prove”.

**Trade-offs / mitigations**

* Reliance-bearing uses require a small structured `SpeechActRecord` plus adequate evidence; ordinary occurrence talk needs no record when no later claim must cite it.
* Requires context-local `SpeechActTypeRef` registration; mitigated by starting with a small set (Approve, Revoke, Publish, Notify, Authorize) and extending as needed.

