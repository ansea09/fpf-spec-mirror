---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Is This Claim Supported for This Use? — Trust and Assurance Calculus"
section_id: "B.3:6"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__007_worked-cases.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "B.3 — Is This Claim Supported for This Use? — Trust and Assurance Calculus"
  - "B.3:6 — Worked cases"
line_start: 47062
line_end: 47103
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

On the independence assumption, treating `min(0.9, 0.9) = 0.9` as the joint probability would overstate it. Even with unknown dependence, joint success cannot be more likely than either necessary event. On these marginal estimates its probability is at most `0.9`. For a more demanding decision, establish the dependence or obtain other sufficient bounds.

Return to the protection function. Success requires both events, so its probability is at most `0.81` under the stated model and estimates. This rules out a required minimum above `0.81`. For a minimum of `0.80`, the assessor needs to bound the remaining failures. If the probability that both events occur and the function still fails is at most `0.01`, the model gives a lower bound of `0.80` for success. With no such bound, the upper bound alone leaves that acceptance open. To claim equality with `0.81`, establish zero probability of failure with both conditions present. For a decision about the actual design, establish how well the estimates and the dependence assumption apply to its demand class, including uncertainty that could change the decision.

#### B.3:6.2 - Routed-away case: dashboard status

Starting sentence: “The dashboard approves launch.”

Suppose the dashboard displays `GateDecision GD-17`, which records that a named gate passed for release candidate R. The repaired sentence is: “The dashboard shows GateDecision GD-17 for release candidate R; the decision, not the display, records that the gate passed.”

Use A.21 and the release or permission pattern that consumes the gate decision. No assurance claim is present, so B.3 stops. If the dashboard does not resolve a gate decision, it is only a cue and launch approval remains unresolved.

#### B.3:6.3 - Episteme credibility with a compact result

Target claim: “Model edition M predicts response Y within the declared operating region.” Assurance use: whether an engineer may use that prediction as one input to a reversible design comparison.

The engineer cites the model claim, its empirical-validation result, A.2.4 first-use classification and the direct support relation used, the A.10 provenance path, the operating region, and the expiry condition. No combination of unlike characteristics is needed. The compact disposition is `supported-for-use`, limited to the reversible comparison; release, safety, and operation are not carried. No dated assessment Work or reusable record is added because the use does not depend on who performed the already cited validation.

The engineer states the supporting inference: “The validation compared M's predictions with observations over the region needed for this comparison, and its stated error bounds meet the comparison's tolerance. Those predictions are therefore supported as one input to the reversible comparison within that region and the stated validity window.”

These are premises of this worked case. If the validation does not establish that coverage or tolerance, narrow the use or return an unresolved disposition. Keep the argument beside the compact result or accessible through `basisRefs`. A later correction to the validation reopens the conclusions that depended on the corrected result.

If the engineer is asked to design the assessment for later comparisons, start with the choice those comparisons must support. Suppose the task is to rank two proposed settings by response. A common offset can leave their ranking unchanged. Error in the predicted difference can reverse it. Choose conditions and evidence that bound the error in that difference over the uses promised. For a strict ranking, a predicted advantage greater than the bound on the absolute error in the difference establishes its sign. To decide whether one setting clears an absolute limit, the offset can matter again. The existing validation can supply either bound if its result covers that quantity and range.

#### B.3:6.4 - Order-sensitive Method case

An assurance argument relies on a manufacturing sequence whose result can change when two steps are reversed. To establish what a specified order would achieve, recover the order, any applicable joins and the rule that gives their consequence. For a claim about an actual batch, an applicable final inspection may answer directly. To establish how the batch was produced, use A.15.1 to identify the relevant work, its order and its contribution. To establish which steps are constituents of one reusable Method, use B.1.5.

Use A.22 only if a separately selected organization contributes another needed premise; then identify its constituents, obtaining relations, applied constraints and use frame. The assurance result cites only the results and structure it relies on.

