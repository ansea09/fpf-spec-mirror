---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__011_conformance-checklist.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:9 — Conformance Checklist"
line_start: 44551
line_end: 44565
dependencies:
  - "A.1"
  - "A.11"
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
  - "assertion episteme"
  - "local kind"
  - "partial order"
  - "relation occurrence"
  - "relation-obtaining predicate"
---

### C.3.1:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C31-1` | Each `U.Kind` and `U.SubkindOf` use names the exact effective local reference-scheme edition; cross-context use goes through C.3.3. |
| `CC-C31-2` | `U.SubkindOf` is an admitted direct relation kind with narrower-kind and broader-kind participants, a recoverable obtaining predicate and applicability, and participant-plus-reference-scheme occurrence identity. |
| `CC-C31-2a` | A predicate expression, C.2.1 assertion episteme, evidence item, representation edge, and optional `R_sub` occurrence designator are kept distinct; none makes the relation obtain. |
| `CC-C31-2b` | Reflexivity, transitivity, and antisymmetry constrain obtaining relation facts and are not overloaded with dependency, construction, role, slot, or admission relations. |
| `CC-C31-3` | The judgment-level monotonicity implication is checked for the same candidate and slice under explicit compatible signature editions; `unknown` neither refutes nor establishes the universal relation predicate. |
| `CC-C31-4` | A monotonicity counterexample diagnoses a non-obtaining link, incompatible editions, or missing bridge; no extension row is silently changed. |
| `CC-C31-5` | Signature-edition identity and kind continuity are decided separately, and old judgments retain their cited edition. |
| `CC-C31-6` | Candidate-state or slice-driven extension change does not by itself change the signature, kind, or a still-obtaining subkind relation. |
| `CC-C31-7` | Scope is absent from the kind; a context slice is an evaluation input rather than a third subkind participant; durable public U-kind admission remains with `E.24.UK`. |
| `CC-C31-8` | `U.Work`, one `W : U.Work`, and any episteme about W remain distinct in every typed example. |

