---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Recovering What “Context” Means in Use"
section_id: "E.10.D1:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__013_relations.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "E.10.D1 — Recovering What “Context” Means in Use"
  - "E.10.D1:12 — Relations"
line_start: 77603
line_end: 77616
dependencies:
  - "A.1.1"
  - "A.2.6"
  - "C.30"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "F.0.1"
  - "F.17"
  - "F.19"
  - "F.9"
keywords:
  - "architecture"
  - "claim scope"
  - "context wording"
  - "environment"
  - "model use"
  - "positive wording repair"
  - "source-local meaning"
  - "viewpoint"
  - "working situation"
---

### E.10.D1:12 - Relations

- Apply `E.10` to recognize a local wording problem and make the smallest local repair. Apply `E.10.D1` when *context* hides content that changes the statement or next action.
- Apply `E.10.ARCH` when the same consequential wording problem recurs across framework contributions. That pattern supplies the shared restoration method; `E.10.D1` supplies this word-specific branch.
- `A.1.1` defines the direct model-use relations and the decision condition for selecting `BoundedModelUseStructure`.
- `A.2.6` defines claim scopes, context slices, and their membership facts. `C.2.1` identifies claim-bearing epistemes and their effective schemes.
- `F.0.1` supplies the source-local recovery method, exact F.17 cell and basis-relation result, reuse rule, and stop. `E.10.D1` recognizes the wording use and returns the repaired sentence; it does not repeat that recovery method.
- `F.1` is used only when source selection is live. `F.0.2` is used only when several source ontologies must be compared for one receiving claim. Neither follows automatically from a source-local wording repair.
- `F.17` defines `SchemeSenseCell`, `SenseCellAddressRef`, and `LocalSenseBasisRelation`. `F.9` defines semantic-context projection, direct Bridge truth, separate bounded-use claims, and reliance boundaries; use `F.9` only when the receiving claim needs that cross-local relation.
- `C.30` defines the obtaining `ArchitectureRelation` and the separate `ArchitectureClaim` form. Use the actual relation only when its predicate holds; use claim content for a negative, unresolved, candidate, or expected architecture statement.
- `E.17.0` defines viewpoint identity, the direct `EpistemeViewpointConformanceRelation`, its readable positive, negative, and unresolved results, and the resulting same-episteme `U.View` membership.
- For environment, operating-region, and operating-condition wording, use the pattern that defines or constrains the subject claim. When the affecting fact or condition cannot be recovered, keep the wording result unresolved rather than inferring architecture or viewpoint content.
- Apply `F.19` only for final phrase repair after the ontology and practical use are recovered. Apply `F.18` only when the repair creates a durable reusable designation.

