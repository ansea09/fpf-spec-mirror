---
chunk_kind: "child"
pattern_id: "A.8"
pattern_title: "Universal Core Principle: Test a U-Kind Across Domains"
section_id: "A.8:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.8/A.8__006_solution.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.8 — Universal Core Principle: Test a U-Kind Across Domains"
  - "A.8:3 — Solution"
line_start: 26302
line_end: 26335
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

Recover the basis for the three-domain falsification test through `E.24.UK`:

- **Already admitted kind.** Use its applicable accepted admission result and the candidate facts it establishes. Reconsider kernel placement at the claimed scope; an unchanged, still-applicable admission does not need to be repeated.
- **New admission proposal.** Use the independent candidate inputs of the shared decision in `E.24:4.0a`: governed individuals, proposed membership or identity rule, intended extent, nearest non-member and receiving use. Complete the A.8 test alongside the other applicable admission tests, before E.24.UK closes the decision. The projections provide evidence for the core-placement claim; the complete E.24.UK test decides admission.

In either case, the candidate description and the domain evidence must support the comparison independently of the conclusion being sought.

The candidate passes A.8 only when all four conditions hold:

1. **Distinct domain families.** At least three projections come from foundationally different domain families.
2. **Same abstract contribution.** Each projection shows the same kernel contribution, not merely a similar word.
3. **Non-trivial diversity.** Each projection supplies a distinct test of the contribution, with facts or correspondence evidence not subsumed by the other projections.
4. **Recorded losses.** Differences, losses and comparison risks are visible enough to distinguish the shared contribution from local conditions. An F.9 Bridge is needed only for the semantic-correspondence claim governed by that pattern.

Use the following fields to make each projection inspectable. Equivalent prose or a shared table is sufficient when it preserves these values:

```text
UniversalCoreProjection:
  CandidateUKind:
  UKindAdmissionResultRef: exact accepted E.24.UK output, when available; follow it to the shared decision only when common inputs or decision mode are needed.
  DomainFamily:
  DomainTerm:
  LocalEoC:
  SameAbstractContribution:
  DifferenceOrLoss:
  EvidenceRef:
```

For a new proposal, `CandidateUKind` identifies the candidate under consideration. Keep its projection findings with the shared decision's ClaimGraph. Supply `UKindAdmissionResultRef` when an applicable accepted result exists; a pending decision reference is not an accepted-result reference. The other projection values can be supplied and tested before that result exists.

At least three supported projections are required. Try to defeat the proposed universal-core claim: a supported counterexample within its claimed scope refutes that form of the claim. A misidentified local object or invalid projection first needs correction. Three successful cases support this admission test; they do not prove universality over every future case.

