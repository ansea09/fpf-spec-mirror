---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set"
section_id: "C.32.ACS:7"
section_title: "Conformance requirements"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__008_conformance-requirements.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set"
  - "C.32.ACS:7 — Conformance requirements"
line_start: 76928
line_end: 76945
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "architecture criteria"
  - "attainable observation"
  - "protected qualities"
  - "proxy risk"
  - "required result"
  - "structural alternatives"
---

### C.32.ACS:7 - Conformance requirements

| Requirement | Required result |
|---|---|
| `CC-ACS-1` | The criteria set names the described holon, architecture use, and receiving use; every admitted row names its exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, and qualification or evaluation window. |
| `CC-ACS-2` | Source catalogue, HCS starter pack, draft project criteria rows, optimization indicators, monitored guardrails, and context-only rows remain distinct. |
| `CC-ACS-3` | The optimization core is small enough to guide the current work. Three to five rows is a heuristic, not a minimum; a larger core needs a use reason, and all binding constraints remain. |
| `CC-ACS-4` | Each admitted row names a bearer or selected structure. A draft with an unresolved bearer remains a question and cannot guide the dependent architecture choice. |
| `CC-ACS-5` | User function, architecture characteristic, Q-Bundle, scale row, reading, eval program, and eval result remain separate. |
| `CC-ACS-6` | Any composite quality family belongs to `C.25`; ACS may reference the Q-Bundle or one declared slot. |
| `CC-ACS-7` | Before an optimization row guides a change or evaluation, examine its material proxy risk and retain the constraints and counter-characteristics needing protection. If no material proxy loss is found, retain the basis of that judgment rather than inventing a loss. |
| `CC-ACS-8` | Eval-program construction belongs to `C.32.ACE`; eval programs are not used as criteria rows. |
| `CC-ACS-9` | The criteria set does not compare, select, publish, decide, certify, or carry an architecture-adequacy claim by itself. |
| `CC-ACS-10` | A project-local criteria set or improvement row names both `projectWorkOccurrenceRef` and the obtaining `architectureCriteriaProjectUseRelationRef` for that exact record; the suffix or either reference alone asserts no locality. |
| `CC-ACS-11` | A criteria row remains distinct from its referenced characteristic or Q-Bundle slot, scale, predicate, measurement result, eval program, eval result, and receiving decision object. |
| `CC-ACS-12` | `modelUseStructureRef` appears only when an independently selected `BoundedModelUseStructure` changes the row interpretation; it never replaces row claim scope or context-slice membership. |
| `CC-ACS-13` | A scale-sensitive ACS row names the exact characteristic or Q-Bundle slot, bearer, scale form, and use class; any preference between alternatives over a scale window is separately governed by `C.31.ASAP`. |

