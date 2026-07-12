---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "P2W Problem-to-Work Carry-Through"
section_id: "E.18.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__011_rationale.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "E.18.1 — P2W Problem-to-Work Carry-Through"
  - "E.18.1:10 — Rationale"
line_start: 79254
line_end: 79259
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.1"
  - "C.16"
  - "C.22.2"
  - "C.29"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.18"
  - "E.18.3"
  - "F.9"
  - "G.11"
  - "G.2"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### E.18.1:10 - Rationale

`E.18.1` is a child of `E.18` because a P2W relation can use transformation-flow structure as its setting when the carried claim spans several transformation-flow slices, typed positions, or returns. It does not define graph semantics or prescribe performed-work order. It helps a practitioner preserve an accepted problem-side claim while selecting and applying the next direct pattern; that pattern, not P2W, produces or amends the governed value.

The design puts the positive carry-through table first because repeated negative distinction sets can make a pattern whose primary EntityOfConcern is P2W behave like reference policing. P2W needs precision, but precision is useful here only when it leaves a surviving action: preserve the accepted claim, recover the exact direct relation and governing pattern, apply that pattern, obtain its governed value, materialize a compact note only under reliance, stop, split, or return locally.

