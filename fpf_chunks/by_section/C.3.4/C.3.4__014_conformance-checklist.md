---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:12"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__014_conformance-checklist.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:12 — Conformance Checklist"
line_start: 46251
line_end: 46265
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
| **KUA-01** | The declaration is a C.2.1 episteme with base kind as EntityOfConcern, effective scheme, pinned editions, use, constraints/bindings, applicability, dependencies, and its own formality. |
| **KUA-02** | It creates no kind or subkind fact. |
| **KUA-03** | Admissibility precedes the three-valued judgment; guard refusal is separate. |
| **KUA-04** | Vocabulary preserves the base judgment; constraint/composite uses governed candidate conditions and the three-valued conjunction rule. |
| **KUA-05** | Claim-scope conditions remain under A.2.6 and are not folded into kind identity. |
| **KUA-06** | A guard designates exact editions, checks applicability, evaluates the exact candidate, and makes a separate use decision. |
| **KUA-07** | Stable refinement is independently identified and checked; declaration reuse does not promote it. |
| **KUA-08** | Guard-addressable adaptation and correspondence declarations resolve to their exact editions and all interpretation, dependency, definedness, direction, and loss values required by section 6.3; a catalog remains representation and does not merge kind identities. |
| **KUA-09** | Locality change triggers identity comparison. Same-kind reuse has no bridge and still gets a fresh receiving judgment; distinct-kind use requires an obtaining C.3.3 correspondence before bridge reliance. |
| **KUA-10** | Non-applicability forms no judgment; unavailable admissible dependencies yield `unknown`; correspondence failure blocks use without rewriting the receiving result. |

