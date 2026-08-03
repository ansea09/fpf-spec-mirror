---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:14"
section_title: "Detail Map"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__016_detail-map.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:14 — Detail Map"
line_start: 44735
line_end: 44748
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
  - "KindBridge"
  - "SubkindOf"
  - "bounded-context local kind"
  - "effective ReferenceScheme"
  - "intent-bearing KindSignature"
  - "optional slice-indexed extension"
  - "three-valued candidate judgment"
---

### C.3:14 - Detail Map
C.3 is the head pattern for typed reasoning. It leaves each detailed mechanism at its direct neighboring pattern while preserving a discoverable route to that mechanism.

| Needed detail | Governing locus | Content carried there |
| --- | --- | --- |
| Local kind order and continuity | `C.3.1` | `U.Kind`, `U.SubkindOf`, partial-order law, judgment monotonicity, and continuity across signature editions. |
| Declaration, candidate judgment, and extension | `C.3.2` | `KindSignature`, exact four-key judgment, `true`/`false`/`unknown`, optional `KindExtension`, and scope/formality/evidence boundaries. |
| Cross-context kind use | `C.3.3` | The direct `KindBridge` relation between exact source and target local kinds, its separate bridge-assertion episteme, declared preservation and loss, and target-context reevaluation under the exact target `KindSignature` edition. |
| Local adaptation without cloning a kind | `C.3.4` | A `RoleMask` declaration episteme, its pinned base-kind judgment and additional candidate-feature constraints, the exact three-valued masked judgment, and any separately declared cross-context adapter. |
| Abstraction facet | `C.3.5` | `KindAT` as an editorial planning facet on one exact local kind, with no effect on the kind, declaration, judgment, extension, bridge assessment, guard, or F–G–R. |
| Typed guards and applied examples | `C.3.A` | Declaration-level kind compatibility and exact candidate-use judgments kept separate across regulatory, assurance, ESG, and Method–Work uses, including the independently grounded actual `W : U.Work` boundary. |

Do not treat this compact head pattern as the whole C.3 discipline when a case needs declaration, classification, extension, bridge, mask, abstraction, or applied-guard detail. Use the neighboring C.3 pattern that governs the live detail.

