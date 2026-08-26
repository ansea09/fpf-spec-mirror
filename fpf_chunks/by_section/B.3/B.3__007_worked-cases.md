---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:6"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__007_worked-cases.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:6 — Worked cases"
line_start: 38245
line_end: 38278
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

### B.3:6 - Worked cases

#### B.3:6.1 - Fully calculated case: two necessary independent conditions

Target claim: “The protection function succeeds on a demand.” Assurance use: a bounded reliability argument for a named design decision.

The domain model says that both independently tested conditions must succeed: sensor detection and actuator response. Each has estimated probability `0.9` under the same stated demand class and qualification window. Under the declared independence assumption, the joint probability is:

```text
0.9 × 0.9 = 0.81
```

Using `min(0.9, 0.9) = 0.9` would overstate this conjunction. If the conditions are dependent, even the product is not justified; the result must use the applicable conditional model or remain unresolved. The B.3 result therefore cites the two domain results, the series dependency structure, independence basis, product calculation, `0.81` conclusion, limitations, and the observation that reopens the independence assumption.

What changes in practice: the design decision is evaluated against `0.81`, not a falsely “conservative” `0.9`. No universal B.3 reliability formula is created.

#### B.3:6.2 - Routed-away case: dashboard status

Starting sentence: “The dashboard approves launch.”

The dashboard is a publication face. Suppose it displays `GateDecision GD-17`, which records that a named gate passed for release candidate R. The repaired sentence is: “The dashboard shows GateDecision GD-17 for release candidate R; the decision, not the display, records that the gate passed.”

Use A.21 and the release or permission pattern that consumes the gate decision. No assurance claim is present, so B.3 stops. If the dashboard does not resolve an exact gate decision, it is only a cue and launch approval remains unresolved.

#### B.3:6.3 - Episteme credibility with a compact result

Target claim: “Model edition M predicts response Y within the declared operating region.” Assurance use: whether an engineer may use that prediction as one input to a reversible design comparison.

The engineer cites the exact model claim, its empirical-validation result, the A.2.4 evidence-use relation, the A.10 provenance path, the operating region, and the expiry condition. No combination of unlike characteristics is needed. The compact disposition is `supported-for-use`, limited to the reversible comparison; release, safety, and operation are expressly not carried. No dated assessment Work or reusable record is added because the use does not depend on who performed the already cited validation.

#### B.3:6.4 - Order-sensitive Method case

An assurance argument relies on a manufacturing sequence whose result changes when two steps are reversed. The practitioner uses the direct Method and Work patterns for the sequence and, only because organization among several Methods affects the argument, uses A.22 to select a `MethodRelationStructure` for that exact question. The assurance result cites the sequence result and selected structure; B.3 creates neither the Methods nor their order.

