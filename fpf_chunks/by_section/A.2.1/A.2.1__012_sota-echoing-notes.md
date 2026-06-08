---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment: Contextual Role Assignment"
section_id: "A.2.1:11"
section_title: "SoTA-Echoing (notes)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__012_sota-echoing-notes.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.2.1 — U.RoleAssignment: Contextual Role Assignment"
  - "A.2.1:11 — SoTA-Echoing (notes)"
line_start: 2433
line_end: 2443
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2"
  - "D.CTX"
  - "E.10.D1"
  - "E.10.D2"
  - "U.BoundedContext"
keywords:
  - "RCS/RSG"
  - "RoleEnactment"
  - "Standard"
  - "context"
  - "holder"
  - "role"
---

### A.2.1:11 - SoTA-Echoing (notes)

| Topic this pattern leans on | Post‑2015 anchor (example) | How A.2.1 uses it | Status |
| --- | --- | --- | --- |
| Context‑local meaning boundaries | Vernon (2016) *DDD Distilled*; Newman (2021) *Building Microservices* | `role ∈ Roles(context)`; no equivalence by label; cross‑Context reuse via Bridges | Adopt/Adapt |
| Roles as context‑dependent (anti‑rigid) types | Guizzardi et al. (2018–2022) work on roles in OntoUML/UFO | Separates holder identity from contextual function; prevents type explosion | Adopt |
| Separation of duties & traceable responsibility | NIST SP 800‑53 Rev. 5 (2020); ISO/IEC 27001:2022 | `⊥` incompatibilities; auditable windows; reviewer independence hooks | Adopt |
| Continuous authorisation / policy enforcement | NIST SP 800‑207 (2020) Zero Trust Architecture | Window + RSG state as explicit gates; “green gate” as a checkable condition | Adapt |
| Checklist‑based state progression | OMG Essence 1.2 (2019) | RSG states with explicit checklists and StateAssertions | Adapt |
| Requirements and standards as first-class normative epistemes | ISO/IEC/IEEE 29148:2018; ISO 26262:2018 | Epistemes hold Normative-Status/Requirement roles; Systems act; Work is evaluated against them | Adopt |

