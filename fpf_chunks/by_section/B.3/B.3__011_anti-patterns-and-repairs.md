---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust & Assurance Calculus (F–G–R with Congruence)"
section_id: "B.3:8"
section_title: "Anti‑patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__011_anti-patterns-and-repairs.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "B.3 — Trust & Assurance Calculus (F–G–R with Congruence)"
  - "B.3:8 — Anti‑patterns and repairs"
line_start: 31330
line_end: 31343
dependencies:
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "B.1"
  - "B.1.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.3"
  - "B.3.5"
  - "B.3.x"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "D.4"
  - "E.14"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

### B.3:8 - Anti‑patterns and repairs

| Anti‑pattern             | Symptom                                                    | Repair                                                                                                         |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Averaging assurance**  | Mean of `R_i` reported as system reliability               | Use `min R_i` on the cutset, then apply `Φ(CL_min)`.                                                           |
| **Ordinal arithmetic**   | Averaging `F` or `CL` to produce “2.3”                     | Use `min`/`max` or thresholds; never average ordinals.                                                         |
| **Coverage as centroid** | Replacing `G` union with a single “typical point”          | Keep `G` as set/coverage; if a numeric proxy is needed, derive it from the set.                                |
| **Ignoring congruence**  | No penalty for low-CL mappings or interfaces                    | Assign `CL` to integration edges and apply `Φ(CL_min)`.                                                           |
| **DesignRunTag chimera**   | “One score” mixing blueprint and telemetry                 | Split into `S=design` and `S=run` tuples; compare explicitly.                                                  |
| **Agency override**      | Claiming higher assurance because a controller is “clever” | Agency may justify *how* improvements are achieved; it cannot remove WLNK or `Φ`.                              |
| **MemberOf as stock**    | Using `MemberOf` to sum reliabilities                      | Keep `MemberOf` for collections; reliability comes from the relevant **Γ** composition (e.g., Γ\_sys cutset). |
| **False assurance support** | Badge, dashboard color, credential display, compliance mark, provenance label, model card, datasheet, data card, assurance document, attestation label, or generated confidence phrase is used as an assurance claim. | Keep it as orientation or source pointer unless a typed assurance claim and `A.10` evidence path support the intended assurance use. |
| **Minimum reliance safety support record inflation** | Ordinary evidence, source-finding explanation, local CV, documentation, or reversible local calibration use is forced into a safety support record; or the support record is used as approval, release permission, gate passage, safety acceptance, or compliance proof. | State the trigger that makes B.3 live. If the trigger is absent, return to `A.10`, `E.17.EFP`, `A.20`, `A.21`, `E.19`, or the local relation. If the trigger is live, write only the minimum support record and contest/redress path needed for the named reliance use. |

