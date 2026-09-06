---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:7"
section_title: "Conformance and counterexample replay"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__008_conformance-and-counterexample-replay.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:7 — Conformance and counterexample replay"
line_start: 15675
line_end: 15705
dependencies:
  - "A.10"
  - "A.22.CGUS"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "B.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "D.1"
  - "D.5"
  - "E.11"
  - "E.17"
  - "E.17.0"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.24.PUB"
  - "E.6"
  - "F.19"
  - "G.11"
  - "G.2"
keywords:
---

### A.6.3.NAR:7 - Conformance and counterexample replay

| Check | Pass condition |
| --- | --- |
| `CC-NAR-1` | An ordinary user can produce a readable narrative before supplying exact endpoint identities or assurance fields. |
| `CC-NAR-2` | Reader/listener use, source material, selected structures, and the reason for selecting them are clear. |
| `CC-NAR-3` | The ordering and connective account are explicit enough to distinguish source relations from narrative links added for readability. |
| `CC-NAR-4` | The narrative has been compared with its source for preservation, foregrounding, omission, weakening, rearrangement, and unsupported strengthening. |
| `CC-NAR-5` | Admissible use and a usable return trigger and destination are present; any optional non-admissible use passes F.19:4's plausible-reader test. |
| `CC-NAR-6` | Temporal posture, mediation, event-model support, viewpoint, engagement, and worker history appear only when each changes use or blocks a likely overread. |
| `CC-NAR-7` | Evidence, assurance, ethics, policy, publication, decision, and Work claims use the patterns that define or test those exact claims. |
| `CC-NAR-8` | The exact branch is opened only when an identified receiving use makes claim identity material, such as independent travel, citation, dispute, material cross-scheme reuse, identity-bearing admission, consequential reliance, or an explicit named-receiver requirement; publicness alone is not a trigger. |
| `CC-NAR-9` | In that branch, exact `X` and `Y` are independently identified by claim content, exact EntityOfConcern, and effective `U.ReferenceScheme`; source objects, forms, carriers, and readable prose do not substitute for them. |
| `CC-NAR-10` | Exact `n : X -> Y` states same EntityOfConcern, claim construction, endpoint scheme relation, ordering, preservation, loss, prohibited strengthening, applicability, and return. |
| `CC-NAR-11` | Additional source epistemes and correspondence dependencies are exact when used; actual Work, system, system-role kind or assignment, method, publication, carrier, evidence, assurance, and `U.View` membership remain separately identified and must satisfy their own definitions or tests. Completing the exact record does not itself authorize reliance. |
| `CC-NAR-12` | Reuse is lowered or locally repaired when the source, selected structure, order, loss, use, exact identity, depended-on relation, or return changes. |

Counterexample replay:

| Case | Required result |
| --- | --- |
| Ordinary entry | A team can turn an architecture trade-off structure into a useful explanatory sequence and loss note without first inventing `X`, `Y`, `n`, Work, or assurance records. |
| Preserve vs retarget | Exact NAR requires the same exact EntityOfConcern; a different narrated concern requires A.6.4 even when derived from `X`. |
| Same vs different scheme | Narrative order may be primary in either case. A material scheme change additionally opens RT, but scheme difference alone establishes neither `n` nor correspondence. |
| Candidate vs `U.View` | A valid narrative episteme and NAR construction can fail E.17.0 viewpoint conformance and remain a non-View candidate. |
| Source publication/form/carrier | A publication can make `X` available and a form or carrier can express it; none becomes `X`, and a narrative page or audio file is not `Y`. |
| Narrative order | Chronology, tension, or didactic order is a declared construction rule, not automatically world-side event order, proof order, performed-Work order, or an obtaining relation. |
| Controlled loss | If `Y` is usable only under declared loss, narrower use, and source return, coordinate CSC; NAR ordering alone does not make the loss admissible. |
| Grounded source, ungrounded narrative | Grounding of `X` or a designated evidence set does not ground `Y`; recover a separate exact `EpistemeEmpiricalGroundingRelation` for `Y` only when its own claims satisfy that rule. |
| Selected structure overread | An A.22 structure designated by source claims may be ordered by NAR; it is not the source or receiving episteme, worker, viewpoint, `U.View`, representation, publication, or narrative Work. |

