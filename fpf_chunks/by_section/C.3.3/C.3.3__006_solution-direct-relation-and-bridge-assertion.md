---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:5"
section_title: "Solution — Direct relation and bridge assertion"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__006_solution-direct-relation-and-bridge-assertion.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:5 — Solution — Direct relation and bridge assertion"
line_start: 45171
line_end: 45186
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
  - "CL^k"
  - "KindBridge direct relation"
  - "R penalty"
  - "bridge assertion episteme"
  - "loss"
  - "target judgment"
---

### C.3.3:5 - Solution — Direct relation and bridge assertion

A `KindBridge` occurrence is an obtaining direct relation between one exact source local `U.Kind` and one exact target local `U.Kind`. The kinds remain independently identified in their source and target reference schemes. The bridge does not move, clone, or construct either kind. Its obtaining predicate states the exact mapping direction, source and target scheme editions, definedness, and the direct kind-intent correspondence required for that pair. Preservation, collapse, inversion, or non-preservation of a source `U.SubkindOf` fact is instead a separate assertion over the relevant pair of obtaining KindBridge relations and the exact source and target order facts. The paired `KindSignature` editions are declaration epistemes used to evaluate the correspondence predicate; they are not relation participants or occurrence-identity discriminators.

`KindBridge` is the direct relation kind governed here under the common `U.Relation` occurrence discipline of A.6.REL. This spelling does not by itself admit a durable dependent U-kind named `U.KindBridge`. An F.9 Bridge, Bridge Card, mapping row, or publication can serve as a bridge assertion or representation only when its exact content and EntityOfConcern support that use; its existence does not make a `KindBridge` relation obtain or identify an occurrence by record identity.

Keep the direct relation separate from the C.2.1 bridge-assertion episteme used to communicate or rely on it. That episteme designates the exact bridge occurrence when occurrence identity is needed and carries the mapping rule, order-preservation status, `CL^k`, loss notes, definedness area, evidence, and admitted receiving use. An assertion, bridge card, table row, or mapping expression neither makes the bridge relation obtain nor creates a target `KindSignature`. If a target declaration is needed, author and identify that separate C.3.2 declaration episteme first.

For every classified candidate, the target context performs its own exact judgment:

`J(candidate, targetKind, targetSignatureEdition, TargetSlice) ∈ {true, false, unknown}`

A source-context judgment may support the bridge or reliance assertion but is never reused as target truth. Missing target-side evidence, an unavailable target-declaration dependency, or a candidate outside the target evaluation domain yields `unknown` for the target C.3.2 judgment. An unavailable mapping dependency or a bridge use outside declared definedness instead leaves the required bridge reliance unsettled or inadmissible; a receiving guard declines that cross-context use without rewriting an independently evaluated target judgment.

When a receiving claim relies on an obtaining bridge and the target judgment, the bridge-assertion episteme supplies the assessed `CL^k` and loss basis. Apply the monotone `Ψ(CL^k)` consequence to R only. Do not change declaration formality F or Claim scope G.

