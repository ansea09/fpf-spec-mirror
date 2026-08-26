---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:4"
section_title: "Core Objects"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__006_core-objects.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:4 — Core Objects"
line_start: 44031
line_end: 44050
dependencies:
  - "A.1"
  - "A.11"
  - "A.2"
  - "A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "U.SubkindOf direct relation"
  - "classification equivalence"
  - "closed finite domain"
  - "continuity"
  - "criterion entailment"
  - "kind identity"
  - "membership criterion"
  - "participant-determined occurrence"
  - "preorder"
---

### C.3.1:4 - Core Objects

| Object | Meaning | Boundary |
| --- | --- | --- |
| `U.Kind` | The admitted meta-kind whose individuals are reusable intensional classification distinctions. One individual is recovered through its candidate domain, operative membership condition, intended member/non-member distinction, and continuity rule. | A `KindSignature`, label, source boundary, reference scheme, current extension, or receiving use is not the kind. |
| `U.SubkindOf` | The admitted direct relation kind whose occurrences relate exact narrower and broader `U.Kind` participants within declared applicability. Its obtaining facts form a preorder. | It is not a predicate expression, assertion episteme, dependency, part-whole relation, construction, system-role assignment, or admission relation. |
| `SubkindOfObtains(k1, k2)` | The relation-obtaining condition. It holds either because the exact membership criterion for `k1` entails the criterion for `k2` under an aligned interpretation and applicability, or because every candidate in a deliberately closed finite domain has been evaluated and every admissible `true` result for `k1` is also `true` for `k2`. | The first branch is criterion-based. The second is explicitly domain-bounded. Non-exhaustive observations support a separate assertion but do not make the relation obtain. |
| `R_sub : U.SubkindOf` | One obtaining relation occurrence between exact narrower kind `k1` and broader kind `k2`. | Use a designator only when a receiver needs it. The ordered kind participants determine occurrence identity; schemes, signatures, evidence, assertions, and publications do not. |
| subkind assertion episteme | A C.2.1 episteme that affirms, denies, or leaves unresolved the obtaining condition and cites its interpretation, applicability, branch, and support. | The assertion does not make the relation obtain; a negative or unresolved assertion designates no obtaining occurrence. |
| classification equivalence for an alignment | Mutual obtaining `U.SubkindOf` facts between two kinds within the same declared applicability. | It says that the two membership distinctions classify alike there. It does not identify the kinds. A consumer that needs a partial order may order these equivalence groups. |
| `KindSignature` edition | The C.3.2 declaration episteme used to interpret and evaluate one kind. | It is neither the kind nor the subkind relation. |

#### C.3.1:4.1 - Direct U.SubkindOf Relation Boundary

A readable sentence such as `CoolingPumpKind is a subkind of PumpKind for this declared plant use` states that the direct relation obtains. It needs no occurrence identifier when no receiver distinguishes or refers to the occurrence.

The criterion-entailment branch obtains when the exact narrower membership condition entails the broader one under the aligned interpretation and applicability. The closed-domain branch obtains only when the candidate domain is deliberately finite and closed, every candidate's admissibility has been checked, and exhaustive evaluation leaves no narrower `true` without a broader `true`. A counterexample refutes either proposal. A missing dependency or `unknown` judgment cannot establish either branch; a `not-applicable` request is outside the comparison.

When a receiver needs one occurrence, `R_sub` is participant-determined by the ordered pair of kind identities. The effective scheme, aligned signatures, and applicability qualify how obtaining is tested and asserted. A scheme-edition change therefore prompts an alignment and renewed test; it does not create another relation occurrence. If the same participants still satisfy the condition, the same relation continues to obtain. If they no longer do, the prior obtaining claim is no longer current; another assertion may record that change without inventing a scheme-keyed occurrence.

