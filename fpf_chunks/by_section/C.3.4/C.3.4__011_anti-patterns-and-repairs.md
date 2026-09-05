---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:9"
section_title: "Anti-patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__011_anti-patterns-and-repairs.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:9 — Anti-patterns and Repairs"
line_start: 46180
line_end: 46190
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
---

### C.3.4:9 - Anti-patterns and Repairs

| Anti-pattern | Why it is wrong | Repair |
| --- | --- | --- |
| Adaptation declaration treated as a new type | Duplicates the kind and hides the declaration episteme. | Keep the base kind; for a stable conceptual refinement identify another local kind and establish `U.SubkindOf` independently. |
| Claim- or Work-scope condition hidden in an adaptation judgment | Conflates the candidate with where a claim or Work applies. | Move the scope condition to A.2.6; keep candidate constraints and declaration applicability explicit. |
| Unversioned or applicability-free declaration used by a guard | Makes evaluation non-replayable. | Give the declaration a designator, pin its edition and dependencies, state applicability, and distinguish `not-applicable` from `unknown`. |
| Locality change treated as automatic bridge | Splits the same kind or transfers source truth. | Compare kind definitions first. Same-kind reuse needs no bridge and still gets a fresh receiving result; distinct-kind use needs an obtaining C.3.3 correspondence. |
| Many declarations with the same local meaning | Produces catalog entropy and inconsistent behavior. | Consolidate redundant declarations; for a stable conceptual distinction, separately identify a local kind and establish its obtaining `U.SubkindOf` relation. |
| Declaration name treated as a kind synonym | Hides constraints and invites misuse. | Designate the exact declaration edition and base kind separately in prose and guards. |

