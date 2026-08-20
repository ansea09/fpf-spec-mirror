---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:7"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__009_conformance-checklist.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:7 — Conformance checklist"
line_start: 38965
line_end: 38984
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

### B.3:7 - Conformance checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-B3.1** | The assurance result is a C.2.1 claim episteme stating `AssuranceResult(E_C, U_A &#124; RS_A, G_A, T_A)` for one exact target-claim episteme and use. | Prevent target, use, interpretation, scope, and time drift. |
| **CC-B3.2** | `F` is ordinal and uses thresholds or `min`; `G` is a USM scope value and uses membership, intersection along essential paths, and `SpanUnion` only across independent evidence lines; `R` is ratio and uses `min` plus conservative operations. | Preserve scale integrity (CHR and USM). |
| **CC-B3.3** | Each `CL` qualifies one exact admitted integration relation occurrence; `Φ(CL)` is monotone decreasing and bounded (`R_eff ≥ 0`). | Make integration quality first-class without letting a graph edge or label create it. |
| **CC-B3.4** | `R_eff = max(0, min_i R_i - Φ(CL_min))` for the relevant integration dependency paths, unless a stricter domain-specific rule is justified. | Enforce WLNK and penalize low-CL integrations. |
| **CC-B3.5** | For `G`, essential dependency paths compose by intersection; `SpanUnion` applies only across explicitly independent evidence lines to the same claim and only over evidenced slices. | Prevent over-generalization. |
| **CC-B3.6** | Any reusable assurance record cites target/input claims, value bearers, exact integration relations, assessment work/application refs, evidence-use/provenance refs, witnesses, scope/window, limitations, decay, and currentness refs; the record performs no work and creates no result. | Keep replay, result, work, evidence, and currentness distinct. |
| **CC-B3.7** | Agency-characteristic values under A.13 and the A.17/A.18/A.19/C.16/A.10 characterization-and-evidence stack do not override WLNK or `Φ(CL)` penalties; if agency grade change alters capabilities, model it as a Meta-Holon Transition. Planned C.9 may later consolidate the profile but supplies no current governing force. | Preserve safety; keep agency separate. |
| **CC-B3.8** | Design and run assurance uses have separate `T_A`, condition sets, scopes, evidence windows, assessments, and result claims; compare rather than merge them. | Avoid design/run chimeras. |
| **CC-B3.9** | If an assurance claim depends on a `C.28` causal-use verdict, it consumes `CausalUseSupportVerdict`, `CausalEvidenceSupportBasis`, and relevant profile refs from `C.28` or `A.10`; a causal-use claim whose C.28 verdict is unsupported degrades, blocks, or abstains rather than raising `R`. | Prevent assurance prose from certifying unsupported causal claims. |
| **CC-B3.10** | A local C.28 downgrade, redirected use, or abstention is not a new B.3 assessment/result trigger unless the exact claim is assurance-, publication-, release-bearing, or reused as an assurance input. | Keep cheap causal triage from becoming assurance ceremony. |
| **CC-B3.11** | A label, badge, dashboard, credential, provenance mark, model/data card, assurance document, attestation, or generated phrase raises no assurance unless exact `E_C`, `U_A`, assessment, input-result and A.2.4 evidence-use refs, A.10/G.6 path, argument, limitations, disposition, decay, and reopen condition support a typed assurance-result claim. | Block visible authority from supplying target truth or assurance. |
| **CC-B3.12** | When reliance may materially change behavior, safety, release, compliance, access, resources, people/team status use, operational action, or controlled-entity regulation, constitute the assurance-result claim or explicitly narrow, degrade, abstain, request evidence, reopen, or block; an optional `RelianceSafetyCase` record only cites that result and basis. | Keep consequential assurance concrete without turning the record into authority. |
| **CC-B3.13** | Target/world-side result, target-claim episteme, assessment work, input results, assurance-result episteme, witnesses, record, publication, and later reliance/status/gate/decision remain independently recoverable. | Prevent result and process collapse. |
| **CC-B3.14** | Evidence availability, provenance, or a successful check may alter warrant and assurance disposition but does not create target truth; absence of evidence is not a negative target result. | Preserve the world/claim/warrant boundary. |
| **CC-B3.15** | F.10 defines the status value and its use; cite any domain-specific status rule only for the concrete contribution it makes. Assurance does not define the target, approve a standard, satisfy a requirement, pass a gate, grant permission, or prove actual reliance. | Preserve the assurance/status/use boundary. |

