---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:10"
section_title: "Anti‑patterns & Remedies (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__011_anti-patterns-remedies-informative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:10 — Anti‑patterns & Remedies (informative)"
line_start: 37062
line_end: 37073
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
keywords:
  - "CL^k"
  - "KindBridge"
  - "R penalty"
  - "cross-context mapping"
  - "type-congruence"
---

### C.3.3:10 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                 | Why it’s wrong                         | Remedy                                                                              |
| -------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------- |
| One “interop score” for both kind & scope    | Blurs channels; corrupts penalties     | Use **two bridges**; apply **Φ(CL)** (Scope) and **Ψ(`CL^k`)** (Kind) **separately** |
| Claiming preserved `⊑` while inverting order | Makes typed reasoning unsound          | Mark as **not preserved**; add **loss note**; consider adapter or subkind redesign  |
| Hiding collapses                             | Overstates coverage                    | List collapsed subkinds explicitly; plan extra **R** for lost granularity           |
| “Latest mapping”                             | Non‑deterministic; non‑auditable       | Version bridges; bind to Standards/versions; **fail closed** outside definedness    |
| Using KindBridge to widen G                  | Conflates describedEntity with applicability | Keep Scope edits in **USM** (ΔG±); KindBridge never widens Scope                    |
| Adjusting F/G for poor `CL^k`                 | Violates F–G–R & USM separation             | Route consequences to **R** only; consider narrowing Scope or adding adapters       |


