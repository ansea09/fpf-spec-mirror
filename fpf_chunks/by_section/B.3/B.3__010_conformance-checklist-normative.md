---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust & Assurance Calculus (F–G–R with Congruence)"
section_id: "B.3:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__010_conformance-checklist-normative.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "B.3 — Trust & Assurance Calculus (F–G–R with Congruence)"
  - "B.3:7 — Conformance Checklist (normative)"
line_start: 31838
line_end: 31854
dependencies:
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.7"
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

### B.3:7 - Conformance Checklist (normative)

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-B3.1** | An assurance result **SHALL** be a typed claim `Assurance(H, C &#124; K, S)` with `S ∈ {design, run}`. | Prevent scope drift and chimeras. |
| **CC-B3.2** | `F` **SHALL** be treated as **ordinal** (`min`/thresholds only); `G` as **coverage** (set/measure union constrained by evidence relation); `R` as **ratio** (`min` + conservative operations). | Preserve scale integrity (CHR). |
| **CC-B3.3** | The **Congruence Level** `CL` **SHALL** live on **edges**; the penalty `Φ(CL)` **SHALL** be **monotone decreasing** and **bounded** (`R_eff ≥ 0`). | Make integration quality first-class. |
| **CC-B3.4** | `R_eff` **SHALL** be computed as `R_eff = max(0, min_i R_i - Φ(CL_min))` for the relevant integration paths, unless a stricter domain-specific rule is justified. | Enforce WLNK and penalize low-CL integrations. |
| **CC-B3.5** | `F_eff = min_i F_i`; `G_eff = SpanUnion({G_i})` constrained by evidence relation. | Prevent over-generalization. |
| **CC-B3.6** | An **Assurance SCR** **SHALL** be produced, listing node/edge values, Evidence Graph Ref, and any OrderSpec/TimeWindow identifiers, and **SHALL also display** the `describe(EntityOfConcernRef->GroundingHolonRef)` binding for the claim, the declared **CHR:ReferencePlane ∈ {world\|concept\|episteme}**, a separable **TA/VA/LA** evidence breakdown per **CC-KD-08**, decay/valid-until indicators on empirical bindings, and the **Epistemic-Debt** tally from **B.3.4**. | Provide auditability through A.10 without collapsing evidence families. |
| **CC-B3.7** | **Agency-CHR** values (A.13) **SHALL NOT** override WLNK or `Φ(CL)` penalties; if agency grade change alters capabilities, model it as a **Meta-Holon Transition**. | Preserve safety; keep agency separate. |
| **CC-B3.8** | Design-time and run-time assurance **SHALL NOT** be mixed in one tuple; compare them side by side if needed. | Avoid design-time and run-time mixing. |
| **CC-B3.9** | If an assurance claim depends on a `C.28` causal-use verdict, it **SHALL** consume `CausalUseSupportVerdict`, `CausalEvidenceSupportBasis`, and relevant profile refs from `C.28`/`A.10`; unsupported `CausalityLadderRung` climb **SHALL** degrade, block, or abstain rather than raising `R`. | Prevents assurance prose from certifying unsupported causal claims. |
| **CC-B3.10** | A local `C.28` downgrade, reroute, or abstain **SHALL NOT** be treated as a new assurance tuple trigger unless the claim is assurance-bearing, publication-bearing, release-bearing, or reused as an assurance input. | Keeps cheap causal triage from becoming assurance ceremony. |
| **CC-B3.11** | A conforming `B.3` use **SHALL NOT** treat a label, badge, dashboard tile, credential display, provenance mark, compliance-looking mark, model card, datasheet, data card, assurance document, attestation label, or generated confidence phrase as raising `F`, `G`, `R`, `CL`, readiness, safety, compliance, trust, release confidence, or assurance unless a typed `Assurance(H, C &#124; K, S)` claim and `A.10` evidence path name the claim, assurance use carried by the assurance tuple or relying context, scope, evaluation condition, evidence carriers, argument and assurance rationale, limitations, decay condition, reopen condition, and relying context. | Blocks visible authority-looking labels from supplying false assurance relation. |
| **CC-B3.12** | When reliance on a source may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people/team status, operational action, or controlled-object regulation, the B.3 result **SHALL** provide a minimum reliance safety assurance record or explicitly reject, narrow, degrade, abstain, or reopen the attempted assurance use. The local Tech label `RelianceSafetyCase` **SHALL NOT** be used as a certificate, approval, gate, policy source, Core kind, release permission, or general safety-case ontology. | Keeps safety-bearing reliance relation concrete without turning every source-looking item into a dossier or a new authority system. |

