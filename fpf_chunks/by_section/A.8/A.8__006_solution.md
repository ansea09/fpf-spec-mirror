---
chunk_kind: "child"
pattern_id: "A.8"
pattern_title: "Universal Core Principle: Test a U-Kind Across Domains"
section_id: "A.8:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.8/A.8__006_solution.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.8 — Universal Core Principle: Test a U-Kind Across Domains"
  - "A.8:3 — Solution"
line_start: 26284
line_end: 26310
dependencies:
  - "A.11"
  - "C.3"
  - "C.3.1"
  - "E.24.UK"
  - "F.17"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "domain-agnostic"
  - "kernel-level U-kind admission"
  - "transdisciplinary"
  - "universality"
---

### A.8:3 - Solution

Use the three-domain falsification test only after `E.24.UK` has admitted the candidate as a durable U-kind candidate.

The candidate passes A.8 only when all four conditions hold:

1. **Distinct domain families.** At least three projections come from foundationally different domain families.
2. **Same abstract contribution.** Each projection shows the same kernel contribution, not merely a similar word.
3. **Non-trivial diversity.** Each projection supplies a distinct test of the contribution, with facts or correspondence evidence not subsumed by the other projections.
4. **Recorded losses.** Differences, losses and comparison risks are visible enough to distinguish the shared contribution from local conditions. An F.9 Bridge is needed only for the semantic-correspondence claim governed by that pattern.

Use the following fields to make each projection inspectable. Equivalent prose or a shared table is sufficient when it preserves these values:

```text
UniversalCoreProjection:
  CandidateUKind:
  UKindAdmissionResultRef: exact accepted E.24.UK output; follow it to the shared decision only when common inputs or decision mode are needed.
  DomainFamily:
  DomainTerm:
  LocalEoC:
  SameAbstractContribution:
  DifferenceOrLoss:
  EvidenceRef:
```

At least three supported projections are required. Try to defeat the proposed universal-core claim: a supported counterexample within its claimed scope refutes that form of the claim. A misidentified local object or invalid projection first needs correction. Three successful cases support this admission test; they do not prove universality over every future case.

