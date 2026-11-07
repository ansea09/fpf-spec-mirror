---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:0"
section_title: "At a glance — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__002_at-a-glance-informative.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:0 — At a glance — informative"
line_start: 37423
line_end: 37449
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:0 - At a glance — informative

**Intent.** Declare how coordinate values in a `DeclaredCharacteristicSpace` are normalized for a chosen comparison or characterization, including the transformation, admissibility conditions and preserved or lost distinctions.

**Where it sits.**
- **CN-Spec:** `normalization` and `comparability.mode` select the normalization and whether comparison is `coordinatewise` or `normalization-based`.
- **CHR suite role:** stage `normalize` (first-stage, when enabled by the suite protocol / comparability routing).

**Key outputs.**
- `NCV` (NormalizedCharacteristicValue) values for coordinates.
- When requested for a function `n:D→N`, the equality-of-output relation `x ≡_UNM y` iff `n(x)=n(y)` on its actual domain D. Its classes form a set quotient; preserving further operations or answers needs the additional tests below.
- An inverse only on the stated image of an invertible transformation; an operational quotient only for compatible operations and recoverable queries; a `NormalizationFixSpec` only when a representative of an established class is needed.

**Declaration and configured-method identifiers.**
- `UNM_id?` identifies the selected UNM declaration episteme and its edition under A.6.1; it is distinct from the configured method and from an operation application.
- `NormalizationMethodInstanceId` selects the **normalization method instance** applied to specific coordinate(s), with its validity window and evidence pins (configured-method level).

**Minimum declaration set.**
- In `CN_Spec.comparability`: set `mode`, and (when UNM participates in acceptance/comparison) set `minimal_evidence`.
- In `CN_Spec.normalization`: declare `UNM_id?`, `methods`, `instances`, `method_descriptions`, `invariants`, and (if representatives are required) `fix`.
- For the actual normalization or eligibility evaluation, recover the available inputs, selected method and specification editions, preservation conditions and result or reason for abstaining under Audit below. Retain a separate record when the receiving use requires one.

**Non-goals.**
- Not indicator selection (that is **UINDM**).
- Not scoring, aggregation, comparison, selection (USCM / ULSAM / CPM / SelectorMechanism).


