---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:10"
section_title: "Anti‑patterns & Remedies (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__011_anti-patterns-remedies-informative.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:10 — Anti‑patterns & Remedies (informative)"
line_start: 45541
line_end: 45551
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

### C.3.3:10 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                 | Why it’s wrong                         | Remedy                                                                              |
| -------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------- |
| One “interop score” for both kind & scope    | Blurs channels; corrupts penalties     | Use **two bridges**; apply **Φ(CL)** (Scope) and **Ψ(`CL^k`)** (Kind) **separately** |
| Claiming preserved `⊑` while inverting order | Makes typed reasoning unsound          | Mark as **not preserved**; add **loss note**; consider adapter or subkind redesign  |
| Hiding collapses                             | Overstates coverage                    | List collapsed subkinds explicitly; plan extra **R** for lost granularity           |
| Implicit latest mapping | Non-deterministic and non-auditable | Pin both scheme editions and the mapping-rule edition in the bridge assertion; outside bridge definedness decline the cross-context use without changing the target judgment. |
| Using KindBridge to widen G                  | Conflates entityOfConcern with applicability | Keep Scope edits in **USM** (ΔG±); KindBridge never widens Scope                    |
| Adjusting F/G for poor `CL^k`                 | Violates F–G–R & USM separation             | Route consequences to **R** only; consider narrowing Scope or adding adapters       |

