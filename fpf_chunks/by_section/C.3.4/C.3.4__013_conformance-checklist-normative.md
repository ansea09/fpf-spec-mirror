---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:12"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__013_conformance-checklist-normative.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:12 — Conformance Checklist (normative)"
line_start: 45075
line_end: 45089
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

### C.3.4:12 - Conformance Checklist (normative)

| ID | Requirement |
| --- | --- |
| **RM-01** | RoleMask is a C.2.1 declaration episteme with exact base kind, pinned `KindSignature` edition, declaration edition, intended use, constraint/binding content, definedness, and its own formality when current. |
| **RM-02** | It creates no new kind or `U.SubkindOf` relation; any stable refinement is independently identified and governed by C.3.1. |
| **RM-03** | `J_mask(candidate, kind, kindSignatureEdition, roleMaskEdition, slice)` is reproducible and returns `true`, `false`, or `unknown`; guard refusal is separate. |
| **RM-04** | Vocabulary masks preserve the base judgment; constraint/composite masks use only direct candidate-feature predicates and apply false-if-any-false, true-if-all-true, otherwise-unknown conjunction. |
| **RM-05** | Context conditions remain USM Scope predicates and are not folded into classification. |
| **RM-06** | A guard designates exact declaration editions, evaluates the exact candidate, and does not treat a mask name as a kind synonym. |
| **RM-07** | Broad stable reuse triggers review for a separately identified local kind and an obtaining subkind relation; a declaration or catalog row does not perform promotion. |
| **RM-08** | Every guard-addressable RoleMask resolves durably to its exact declaration and dependency editions; an optional catalog represents those references and may consolidate redundant declarations without becoming ontology. |
| **RM-09** | Cross-context use establishes the exact KindBridge relation, target declarations, and any separate MaskAdapter episteme before evaluating the target masked judgment. |
| **RM-10** | RoleMask non-settlement yields target `unknown`; MaskAdapter non-settlement blocks the cross-context use without rewriting an independent target masked judgment; fail-closed is never `false`. |

