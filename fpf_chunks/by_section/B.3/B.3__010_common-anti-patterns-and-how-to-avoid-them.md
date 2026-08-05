---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 38994
line_end: 39010
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.4"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "C.29"
  - "D.4"
  - "E.14"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.6"
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
| **False assurance by display** | A badge, dashboard color, credential, provenance label, model/data card, assurance document, attestation, or phrase is used as assurance. | Keep it as orientation/source material unless an exact assessment and typed assurance-result claim cite the necessary input-result, A.2.4 evidence-use, and A.10/G.6 provenance refs. |
| **Minimum reliance safety assurance record inflation** | Ordinary evidence, source-finding explanation, local CV, documentation, or reversible local calibration use is forced into a safety assurance record; or the record is used as approval, release permission, gate passage, safety acceptance, or compliance proof. | State the material-reliance trigger. If absent, return the case to the exact evidence, source, status, gate, comparison, or local-use rule that answers it. If met, constitute only the assurance-result claim and minimum record/contest-redress support needed for `U_A`. |
| **Evidence creates truth** | Evidence arrival is said to make the target result obtain, or evidence loss is called falsity. | Keep target facts and direct result with their governor; revise only evidence use, warrant, assurance disposition, or reliance unless the subject facts changed. |
| **Assessment-record collapse** | A checklist, calculation, record, witness, or publication is treated as assessment work or its result. | Name dated work/application, result-claim episteme, witness, record, and publication separately. |
| **Status as assurance** | Approved/current/ready/compliant status defines the target, satisfies a requirement, or proves assurance and release. | Use F.10 for the status value and its use; cite another domain-specific status rule only for its concrete contribution, and constitute a separate B.3 result only when assurance is actually assessed. |

