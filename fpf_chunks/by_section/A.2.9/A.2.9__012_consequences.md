---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
section_id: "A.2.9:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__012_consequences.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.2.9 — U.SpeechAct (Communicative Work Kind, Occurrences, and Records)"
  - "A.2.9:9 — Consequences"
line_start: 7730
line_end: 7744
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Method"
  - "U.SystemRoleAssignment"
  - "U.Work"
keywords:
  - "A.13-qualified actual performer"
  - "containment"
  - "enacted Method"
  - "evidence carrier"
  - "independently admitted speech-act Work"
  - "institutional target and effect"
  - "named receiving use"
  - "optional SpeechActRecord"
  - "publication relation"
  - "response versus achievement"
  - "same obtaining assignment"
  - "separate later performedUnderAssignment"
  - "smallest repair or stop"
  - "time"
  - "utterance description"
---

### A.2.9:9 — Consequences

**Benefits**

* Makes approvals/authorizations/notices **first-class and queryable**, enabling clean RSG checklists and guard rules.
* Provides stable provenance: commitments, granted permissions, and status transitions can cite the **instituting act** explicitly.
* Makes the actual performer recoverable in occurrence and institutional-provenance claims.
* Lets a practitioner judge one named receiving use and repair the smallest blocker without first building a complete occurrence record.
* Keeps observed response, achieved use, later action or change, causal contribution, and permission or admissibility as separately testable questions.

**Trade-offs / mitigations**

* A receiving-use judgement may remain conversational when no later claim must cite it. A reliance-bearing use requires a small structured `SpeechActRecord` plus adequate evidence only when the occurrence itself must remain addressable.
* Requires one exact recognition-taxonomy episteme and effective reference scheme for `SpeechActTypeRef`; mitigated by starting with a small set (Approve, Revoke, Publish, Notify, Authorize) and extending that taxonomy deliberately.

