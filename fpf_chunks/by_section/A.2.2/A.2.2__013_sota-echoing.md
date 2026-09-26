---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__013_sota-echoing.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:12 — SoTA-Echoing"
line_start: 4395
line_end: 4408
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

### A.2.2:12 - SoTA-Echoing

**Practice question.** When can measured performance support a new job, and which change calls for reconsidering the holder's ability, the qualification of its assertion, or its fit to that job?

For repeatable production, the strongest answer in this comparison is to retain a condition-bound description of performance and compare it with the receiving specification. The NIST/SEMATECH *e-Handbook of Statistical Methods*, [§3.4.5](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc45.htm), requires stability before this process-capability use. Its [§6.1.6](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm) compares specification limits with the process distribution, distinguishes spread-only `Cp` from centering-sensitive `Cpk`, and treats estimation uncertainty and non-normal data separately. These sections supply the substantive practice answer and its limits, not an FPF classification of a capability holder.

The serious alternative is a `Cp` width screen: it usefully answers whether the process spread could fit the tolerance if centered. For an actual job, however, the same available mean, spread and limits permit a `Cpk` comparison without another production run. Retaining the mean removes the extra centering assumption. **Adopt** that condition-sensitive comparison; **reject** a spread-only score as sufficient evidence of actual fit when centering is unresolved. This choice costs one additional comparison, while preserving the width screen's useful information.

In a constructed drilling case, take a stable normal diameter distribution with known mean `10.04 mm` and standard deviation `0.02 mm`, and demand `9.90–10.10 mm`. Then `Cp = 1.67`, but `Cpk = 1.00`. A local rule requiring an index of at least `1.33` therefore gives different answers: the width screen passes, while the centering-sensitive fit fails. The threshold is this example's demand, not a universal NIST rule. Real sample estimates would also need the uncertainty treatment required by that rule.

**Adapt** this separation in §§2–3: state the holder's attained performance and conditions, retain its support, and compare the particular demand separately. Tightening the diameter tolerance changes fit without physically changing the drill. Changed calibration can change attained performance; an expired qualification assessment instead changes warranted reliance. Those differences determine which §7 question to reopen. This adaptation does not impose normal distributions, statistical stability or capability indices on every human, software or organizational ability.

Reopen this selection when instability or a changed distribution defeats the retained measurement model, when the decision needs a different loss or uncertainty criterion, or when a rival method distinguishes the same relevant failures with less required evidence. A changed job specification alone calls for a new fit comparison, not a new ability claim or a new method survey.

