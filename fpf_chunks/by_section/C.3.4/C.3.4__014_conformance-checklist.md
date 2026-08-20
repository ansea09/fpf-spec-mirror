---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:12"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__014_conformance-checklist.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:12 — Conformance Checklist"
line_start: 45470
line_end: 45484
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

### C.3.4:12 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| **KUA-01** | `KindUseAdaptationDeclaration` is a C.2.1 declaration episteme with exact base kind, pinned `KindSignature` edition, declaration edition, intended use, constraint or binding content, definedness, and its own formality when current. |
| **KUA-02** | It creates no new kind or `U.SubkindOf`; any stable refinement is independently identified and checked under C.3.1. |
| **KUA-03** | `J_kindUse(candidate, kind, kindSignatureEdition, adaptationDeclarationEdition, slice)` is reproducible and returns `true`, `false`, or `unknown`; guard refusal is separate. |
| **KUA-04** | Vocabulary declarations preserve the base judgment; constraint and composite declarations use direct candidate-feature predicates and apply false-if-any-false, true-if-all-true, otherwise-unknown conjunction. |
| **KUA-05** | Context conditions remain A.2.6 Scope predicates and are not folded into classification. |
| **KUA-06** | A guard designates exact declaration editions, evaluates the exact candidate, and does not treat a declaration name as a kind synonym. |
| **KUA-07** | Broad stable reuse triggers review for a separately identified local kind and an obtaining subkind relation; a declaration or catalog row does not perform promotion. |
| **KUA-08** | Every guard-addressable declaration resolves durably to its exact edition and dependency editions; a catalog represents those references without becoming ontology. |
| **KUA-09** | Cross-context use establishes the exact `KindBridge`, target declarations, and any separate `KindUseAdaptationCorrespondenceDeclaration` before evaluating the target judgment. |
| **KUA-10** | Adaptation non-settlement yields target `unknown`; correspondence non-settlement blocks the cross-context use without rewriting an independent target judgment; fail-closed is never `false`. |

