---
chunk_kind: "child"
pattern_id: "C.2.7"
pattern_title: "U.LanguageStateRepresentationFactorBundle"
section_id: "C.2.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.7/C.2.7__005_solution.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.2.7 — U.LanguageStateRepresentationFactorBundle"
  - "C.2.7:4 — Solution"
line_start: 42816
line_end: 42849
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.18"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.6"
  - "C.2.LS"
  - "F.9"
  - "F.9.1"
keywords:
  - "factor bundle"
  - "locality"
  - "representation factors"
  - "representation organization"
  - "sparsity"
  - "symbolicity"
---

### C.2.7:4 - Solution
`U.LanguageStateRepresentationFactorBundle` is a factor bundle, not one scalar characteristic. The minimal core starter set is:

- `U.LocalityDistribution`
- `U.Sparsity`
- `U.Symbolicity`

A Context may publish a local alias such as `EncodingBasis`, but it shall dock back to the underlying factor bundle instead of replacing it.

#### C.2.7:4.0a - Kind and factor-bundle boundary

`U.LanguageStateRepresentationFactorBundle` is a dependent durable factor-bundle value under the declared `U.LanguageStateSpace` / `U.CharacteristicSpace` boundary, not a root U-kind. Its identity is the bundle of representation factors used for governed episteme publication positions. Individual factors, aliases, dashboards, model probes, or publication forms do not become separate U-kinds unless another governing pattern admits them.

#### C.2.7:4.1 - Minimal factor readings
| Factor | Question it answers | Typical values |
|---|---|---|
| `LocalityDistribution` | Is the representation concentrated in local units or distributed across many units? | local / mixed / distributed |
| `Sparsity` | How concentrated are activation, representation use, or descriptive marks? | sparse / mixed / dense |
| `Symbolicity` | How explicit are the symbolic structures and tokens? | symbolic / mixed / subsymbolic |

#### C.2.7:4.2 - Non-collapse rules

`LanguageStateRepresentationFactorBundle` is not:

- `LanguageStateAnchoringMode`;
- `ArticulationExplicitness`;
- `LanguageStateClosureDegree`;
- evidence, source-currentness, publication authority, work permission, or gate readiness.

A representation may be distributed yet have high trace anchoring; symbolic yet low-articulation; sparse yet low-closure. Those combinations shall remain visible. A model-state, embedding, vector-store relation, or operator-facing publication face may fill one or more representation factors, but the factor bundle does not decide the episteme, carrier, evidence, bridge, work, or gate relation by itself.

#### C.2.7:4.3 - Extension rule
Contexts may add extra representation factors only if the extension is published as a factor addition rather than as a new master factor that erases the core factor bundle.

