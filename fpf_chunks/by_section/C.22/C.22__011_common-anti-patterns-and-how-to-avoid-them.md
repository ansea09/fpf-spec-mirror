---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Task Typing and TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__011_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.22 — Task Typing and TaskSignature Assignment (Problem-CHR)"
  - "C.22:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 51950
line_end: 51962
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

### C.22:8 - Common Anti-Patterns and How to Avoid Them

| Countercase | Repair |
| --- | --- |
| A preferred method or strategy name is inserted into S2 before eligibility is tested. | Remove the method value, restore the exact problem traits, and let A.19, C.23, G.4, and G.5 govern later comparison and selection. |
| A live unknown is encoded as `false`, `0`, or an empty value. | Restore `unknown`, name the direct basis relation and receiving-use policy, and let the downstream pattern produce the result governed by that policy. |
| Ordinal values or values with unlike units are averaged into one score. | Recover scale, unit, polarity, reference plane, and admitted order for every head; use only a directly governed admissible comparison or leave the candidate set partially ordered. |
| One TaskSignature mixes design-time traits, later run observations, and incompatible DesignRunTag positions. | Split the claims by their actual Work and relation positions; retain only the traits current in this signature edition. Use E.18 only when a selected transformation-flow relation is current, F.9 only when exact local meanings differ and its Bridge predicate is true, and the Work pattern for the actual run. |
| A new file, card, or database row is treated as a new TaskSignature. | Compare the declaration content, exact task or work target, and effective reference scheme. Reuse the same identity when only publication, carrier, serialization, or designator changed; identify another episteme when an identity component changed, then apply C.22:5.2's signature-membership and edition-continuity checks. |
| A broad domain, organization, or location label is used as if it supplied scope, measurement, evidence, or selection rules. | Recover the exact EntityOfConcern, effective ReferenceScheme, A.2.6 ClaimScope relation, `U.Discipline` when current, characteristic rules, and direct selector or policy relations that the use actually needs. |
| Data shift is assumed away because the old profile used `iid`. | State the current `ShiftClass` or `unknown`, cite its evidence and currentness relation, and state the changed-use result under the exact acceptance or selector predicate. |
| A vendor, tool, or fashionable method label is treated as a normative selector input. | Keep it only as a Plain example or recover the exact method-description, capability, evidence, and selector relations on which comparison relies. |

