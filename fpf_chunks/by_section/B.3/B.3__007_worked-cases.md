---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Is This Claim Supported for This Use? — Trust and Assurance Calculus"
section_id: "B.3:6"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__007_worked-cases.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.3 — Is This Claim Supported for This Use? — Trust and Assurance Calculus"
  - "B.3:6 — Worked cases"
line_start: 46901
line_end: 46942
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "B.1.5"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
---

### B.3:6 - Worked cases

#### B.3:6.1 - Calculated case: two necessary independent conditions

Target claim: “The protection function succeeds on a demand.” Assurance use: a bounded reliability argument for a named design decision.

The domain model says that both independently tested conditions must succeed: sensor detection and actuator response. Each has estimated probability `0.9` under the same stated demand class and qualification window. Under the declared independence assumption, the joint probability is:

```text
0.9 × 0.9 = 0.81
```

Using `min(0.9, 0.9) = 0.9` would overstate this conjunction. If the conditions are dependent, the product is not justified; the result must use the applicable conditional model or remain unresolved.

The B.3 result therefore cites the two domain results, the series dependency structure, independence basis, product calculation, `0.81` conclusion, limitations, and the observation that reopens the independence assumption.

What changes in practice: the design decision is evaluated against `0.81`, not a falsely “conservative” `0.9`. No universal B.3 reliability formula is created.

#### B.3:6.2 - Routed-away case: dashboard status

Starting sentence: “The dashboard approves launch.”

The dashboard is a publication face. Suppose it displays `GateDecision GD-17`, which records that a named gate passed for release candidate R. The repaired sentence is: “The dashboard shows GateDecision GD-17 for release candidate R; the decision, not the display, records that the gate passed.”

Use A.21 and the release or permission pattern that consumes the gate decision. No assurance claim is present, so B.3 stops. If the dashboard does not resolve a gate decision, it is only a cue and launch approval remains unresolved.

#### B.3:6.3 - Episteme credibility with a compact result

Target claim: “Model edition M predicts response Y within the declared operating region.” Assurance use: whether an engineer may use that prediction as one input to a reversible design comparison.

The engineer cites the model claim, its empirical-validation result, A.2.4 first-use classification and the direct support relation used, the A.10 provenance path, the operating region, and the expiry condition. No combination of unlike characteristics is needed. The compact disposition is `supported-for-use`, limited to the reversible comparison; release, safety, and operation are not carried. No dated assessment Work or reusable record is added because the use does not depend on who performed the already cited validation.

The engineer states the supporting inference: “The validation compared M's predictions with observations over the region needed for this comparison, and its stated error bounds meet the comparison's tolerance. Those predictions are therefore supported as one input to the reversible comparison within that region and the stated validity window.”

These are premises of this worked case. If the validation does not establish that coverage or tolerance, narrow the use or return an unresolved disposition. Keep the argument beside the compact result or accessible through `basisRefs`. A later correction to the validation reopens the conclusions that depended on the corrected result.

#### B.3:6.4 - Order-sensitive Method case

An assurance argument relies on a manufacturing sequence whose result changes when two steps are reversed. Recover the B.1.5 composition, order and join conditions and any A.15.1 Work the argument consumes. Those results may answer the assurance question.

Use A.22 only if a separately selected organization contributes another needed premise; then identify its constituents, obtaining relations, applied constraints and use frame. The assurance result cites only the results and structure it relies on.

