---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 34248
line_end: 34261
dependencies:
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
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

### B.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Averaging assurance** | Mean of `R_i` reported as system reliability | Use `min R_i` on the cutset, then apply `Φ(CL_min)`. |
| **Ordinal arithmetic** | Averaging `F` or `CL` to produce “2.3” | Use `min` or `max` or thresholds; never average ordinals. |
| **Coverage as centroid** | Replacing `G` union with a single “typical point” | Keep `G` as set and coverage; if a numeric proxy is needed, derive it from the set. |
| **Ignoring congruence** | No penalty for low-CL mappings or interfaces | Assign `CL` to integration edges and apply `Φ(CL_min)`. |
| **DesignRunTag chimera** | “One score” mixing blueprint and telemetry | Split into `S=design` and `S=run` tuples; compare explicitly. |
| **Agency override** | Claiming higher assurance because a controller is “clever” | Agency may justify how improvements are achieved; it cannot remove WLNK or `Φ`. |
| **MemberOf as stock** | Using `MemberOf` to sum reliabilities | Keep `MemberOf` for collections; reliability comes from the relevant Γ composition, such as the Γ_sys cutset. |
| **False assurance relation** | Badge, dashboard color, credential display, compliance mark, provenance label, model card, datasheet, data card, assurance document, attestation label, or generated confidence phrase is used as an assurance claim. | Keep it as orientation or source pointer unless a typed assurance claim and `A.10` evidence-provenance path make the intended assurance use bounded and evidenced. |
| **Minimum reliance safety assurance record inflation** | Ordinary evidence, source-finding explanation, local CV, documentation, or reversible local calibration use is forced into a safety assurance record; or the assurance record is used as approval, release permission, gate passage, safety acceptance, or compliance proof. | State the trigger that meets the B.3 material-reliance threshold. If the trigger is absent, use `A.10`, `E.17.EFP`, `A.20`, `A.21`, `E.19`, or the local relation that actually governs the use. If the threshold is met, write only the minimum assurance record and contest and redress relation needed for the named reliance use. |

