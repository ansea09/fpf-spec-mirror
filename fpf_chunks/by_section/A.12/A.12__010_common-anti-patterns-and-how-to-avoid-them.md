---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split: Identify Who Acts on What"
section_id: "A.12:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split: Identify Who Acts on What"
  - "A.12:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 27977
line_end: 27987
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
keywords:
---

### A.12:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Self-action literalism | "The system fixed itself" is accepted as one undivided claim. | Identify the acting and changed participants. Use `ReflexiveSplit@Context` only when §4.2’s two-entity-part and one-holon conditions hold. |
| Transformer kind inflation | The acting side is modeled as `U.Transformer`, as a special system kind, or as a provisional phrase placed in a `U.System` slot. | When System recognition is needed, retain the `U.Entity` and A.1 disposition or blocker until `actingSystemRef` can identify that same entity as a System. Add a local `TransformerSystemRole` classification only after A.2/C.3 establishes the system-role kind from its system-candidate domain, work-facing membership distinction, member/non-member boundary and continuity rule. Add participation or assignment only when that relation is claimed. |
| Boundary as object by word | Boundary or interaction words become durable root objects. | Identify the relation actually claimed: holon delimitation, boundary crossing, transformation, signaling, evidence, source use or publication use. Apply its defining or testing rule; §4.1 gives the condition for recovering an identity-bearing ClaimGraph. |
| Work success by action | Because a system acted, the work is treated as successful. | Use A.15.1 and evidence-use patterns for performed work and success. |
| Evidence by producer | The acting system’s own output is accepted as enough evidence. | Use §4.5 to identify which claim the output supports under A.10. |
| Manufacturing as containment | A tool or teacher changing another holon is treated as its containing whole. | Keep transformation and part-whole claims separate. |

