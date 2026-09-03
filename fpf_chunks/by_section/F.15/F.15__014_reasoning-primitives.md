---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:12"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__014_reasoning-primitives.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:12 — Reasoning primitives"
line_start: 98042
line_end: 98072
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:12 - Reasoning primitives

```text
triggeredStaticResults(scopeVersion, receivingUse)
  = exact C.2.1 result-claim refs for every SCR triggered by that finite scope.
```

`staticSliceOK(...)` may be asserted only as a C.2.1 summary claim over those exact positive results. Scope membership, a filled record, or an absent failure row does not establish it.

```text
changedMemberResult(priorRef, laterRef, rscrRef, continuityOrChangeClaim, losses, receivingUse)
  = one exact C.2.1 result claim after the rule application and its evidence are recoverable.
```

`changedSliceOK(...)` may summarize only the exact changed-member results. Unchanged members reuse prior results after a direct contradiction check; one changed member does not trigger a full-slice rerun unless its dependencies invalidate the other results.

```text
failedRule(ruleRef, subjectClaimRef)
  -> use the defining or testing rule for subjectClaimRef before the receiving use.
```

An F.15 result may report the failed check. Writing another record field neither repairs nor decides the subject claim.

```text
bridgeSuitableForUse(bridgeOccurrenceRef, useClaimRef)
  only if the Bridge obtains, the separate C.2.1 claim is affirmative for exact <use,direction,rule,tolerance>,
  and current A.10 or B.3 reliance supports that claim for the same use.
```

The Bridge, use claim, evidence/reliance, authorization, and any receiving occurrence remain separate. `CL`, a Card, or record membership is not a use result.

