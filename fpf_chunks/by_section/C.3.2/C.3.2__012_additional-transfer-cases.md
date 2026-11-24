---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:10"
section_title: "Additional Transfer Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__012_additional-transfer-cases.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:10 — Additional Transfer Cases"
line_start: 58222
line_end: 58229
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "E.24.UK"
keywords:
---

### C.3.2:10 - Additional Transfer Cases

| Case | Repaired use |
| --- | --- |
| Vehicle and PassengerCar | Check candidate admissibility and use C.3.1's obtaining branch; a registry result is an extension representation, not `U.EntitySet`. |
| AuthenticatedRequest | Name the standard and key-validity dependency. If the remaining facts do not settle authentication, an admissible request with unavailable key support yields `unknown`; a non-request value is `not-applicable`. |
| AdultPatient | Pin the applicable age threshold, date and candidate identity. With an inclusive minimum age, a supported lower bound at or above the cutoff establishes that condition. An upper bound below the cutoff rules it out. If the available evidence leaves both answers possible, its value is `unknown`. A non-person value rejected by ValueKind is `not-applicable`. |

