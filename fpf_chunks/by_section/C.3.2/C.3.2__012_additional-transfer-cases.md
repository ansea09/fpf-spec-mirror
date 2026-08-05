---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:10"
section_title: "Additional Transfer Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__012_additional-transfer-cases.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:10 — Additional Transfer Cases"
line_start: 45058
line_end: 45065
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
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
---

### C.3.2:10 - Additional Transfer Cases

| Case | Repaired use |
| --- | --- |
| Vehicle and PassengerCar | Keep explicit VIN, axle, brake, standard-version, and time conditions in signature editions; test subkind monotonicity over candidate judgments. A registry query result is an extension representation, not `U.EntitySet`. |
| AuthenticatedRequest | Name `AuthStandard v2.3` and key-validity time as dependencies. If the standard is unavailable, the judgment is `unknown` and the receiving guard fails closed without treating the request as known unauthenticated. |
| AdultPatient | Pin jurisdictional threshold, measurement time, and candidate identity. Missing date-of-birth support yields `unknown`; it does not turn the person into a non-adult or make an EHR row the candidate. |

