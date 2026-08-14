---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:9"
section_title: "Anti-patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__011_anti-patterns-and-repairs.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:9 — Anti-patterns and Repairs"
line_start: 45729
line_end: 45739
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
  - "base KindSignature"
  - "candidate-feature constraint"
  - "correspondence declaration"
  - "kind-use adaptation declaration"
  - "three-valued judgment"
  - "vocabulary binding"
---

### C.3.4:9 - Anti-patterns and Repairs

| Anti-pattern | Why it is wrong | Repair |
| --- | --- | --- |
| Adaptation declaration treated as a new type | Duplicates the kind and hides the declaration episteme. | Keep the base kind; for a stable conceptual refinement identify another local kind and establish `U.SubkindOf` independently. |
| Scope hidden in an adaptation judgment | Conflates context with candidate features. | Move context predicates to A.2.6 Scope; keep only direct candidate-feature predicates in `J_kindUse`. |
| Unversioned declaration used by a guard | Makes evaluation non-deterministic and unauditable. | Give the declaration a durable designator, pin its edition and dependencies, and decline use when they cannot be recovered. |
| Cross-context use without exact Bridge and declaration objects | Silently reuses source truth. | Establish the `KindBridge` and Bridge assertion, target declarations, and any correspondence declaration; then evaluate the target judgment and apply only justified R penalties. |
| Many declarations with the same local meaning | Produces catalog entropy and inconsistent behavior. | Consolidate redundant declarations; for a stable conceptual distinction, separately identify a local kind and establish its obtaining `U.SubkindOf` relation. |
| Declaration name treated as a kind synonym | Hides constraints and invites misuse. | Designate the exact declaration edition and base kind separately in prose and guards. |

