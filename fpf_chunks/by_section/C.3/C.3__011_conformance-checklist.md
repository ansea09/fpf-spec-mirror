---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__011_conformance-checklist.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:9 — Conformance Checklist"
line_start: 43472
line_end: 43486
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.6.0"
  - "A.7.1"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "KindSignature"
  - "SubkindOf preorder"
  - "admissibility"
  - "admitted U.Kind individual"
  - "distinct-kind KindBridge"
  - "membership distinction"
  - "optional extension"
  - "true/false/unknown judgment"
---

### C.3:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | `U.Kind` and `U.SubkindOf` rely on exact accepted E.24.UK results; another public kind name still requires its own admission. |
| `CC-C3-2` | Kind, `KindSignature`, admissibility result, admissible three-valued judgment, and optional extension remain distinct; scheme and locality are not stored on the kind. |
| `CC-C3-3` | Kind identity is tested through candidate domain, membership distinction, intended member/non-member boundary, and continuity rule. A practice/source change is a comparison cue, not proof. |
| `CC-C3-4` | Candidate and slice applicability is checked before judgment; `not-applicable` is distinct from admissible `unknown`. |
| `CC-C3-5` | The governed condition named by the criterion decides membership. Evidentiary use alone does not constitute an independent condition, while directly criterion-bearing epistemes, statuses, and relations keep their own governors. |
| `CC-C3-6` | Subkind facts follow C.3.1's criterion-entailment or exhaustive closed-domain branch and form a preorder; classification equivalence does not merge kind identities. |
| `CC-C3-7` | Kind scope is absent; declaration and assertion scopes remain on their epistemes, and the slice remains an evaluation input. |
| `CC-C3-8` | An extension is a representation of admissible true candidates, not `U.EntitySet`, a world-side collection-belonging claim, a collection holon, or a direct relation occurrence. |
| `CC-C3-9` | C.3.3 is used only after distinct kinds and a proposed correspondence are independently established; same-kind reuse still gets a fresh receiving judgment. |
| `CC-C3-10` | `U.Work`, exact `W : U.Work`, and any episteme about W remain distinct. |

