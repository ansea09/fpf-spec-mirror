---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__011_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 50248
line_end: 50260
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
| One TaskSignature mixes design-time traits, later run observations, and incompatible DesignRunTag positions. | Split the claims by their actual work and relation positions; retain only the traits current in this signature edition and use E.18 crossing relations when the receiving use relies on the crossing. |
| A new file, card, or database row is treated as a new TaskSignature. | Resolve SignatureId and edition and compare the four-row semantic content. Reuse the same identity when only the publication or serialization changed; issue a new edition only for a semantic row change. |
| A broad domain label is used as if it supplied scope, measurement, evidence, or selection rules. | Recover the exact bounded context, A.2.6 scope relation, `U.Discipline`, characteristic rules, and direct selector or policy relations that the use actually needs. |
| Data shift is assumed away because the old profile used `iid`. | State the current `ShiftClass` or `unknown`, cite its evidence and currentness relation, and let the acceptance or selector pattern decide the changed use. |
| A vendor, tool, or fashionable method label is treated as a normative selector input. | Keep it only as a Plain example or recover the exact method-description, capability, evidence, and selector relations on which comparison relies. |

