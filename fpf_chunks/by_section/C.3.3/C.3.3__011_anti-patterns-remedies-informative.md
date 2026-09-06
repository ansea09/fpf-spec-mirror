---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
section_id: "C.3.3:10"
section_title: "Anti‑patterns & Remedies (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__011_anti-patterns-remedies-informative.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.3.3 — KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
  - "C.3.3:10 — Anti‑patterns & Remedies (informative)"
line_start: 46011
line_end: 46021
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
---

### C.3.3:10 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                 | Why it’s wrong                         | Remedy                                                                              |
| -------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------- |
| One interoperability score, or mandatory scope-plus-kind bridges | Blurs independent channels and invents unused relations | Open only the exact Scope, kind, and sense relations consumed by the receiving use; keep their losses and R consequences separate |
| Claiming preserved `⊑` while inverting order | Makes typed reasoning unsound          | Mark as **not preserved**; add **loss note**; consider adapter or subkind redesign  |
| Hiding collapses                             | Overstates coverage                    | List collapsed subkinds explicitly; plan the justified **R** penalty for lost granularity           |
| Implicit latest mapping | Non-deterministic and non-auditable | Pin both scheme editions and the mapping-rule edition in the bridge assertion; outside bridge definedness decline that bridge use without changing an independently obtained receiving result. |
| Using KindBridge to widen G                  | Conflates kind correspondence with claim-scope translation | Keep Scope edits in **USM** (ΔG±); KindBridge never widens Scope                    |
| Adjusting F/G for poor `CL^k`                 | Violates F–G–R & USM separation             | Route consequences to **R** only; consider narrowing Scope or adding adapters       |

