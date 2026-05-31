---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust & Assurance Calculus (F–G–R with Congruence)"
section_id: "B.3:4.9"
section_title: "Assurance consequence for unsupported CausalityLadderRung climb"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__007_assurance-consequence-for-unsupported-causalityladderrung-climb.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "B.3 — Trust & Assurance Calculus (F–G–R with Congruence)"
  - "B.3:4.9 — Assurance consequence for unsupported CausalityLadderRung climb"
line_start: 31170
line_end: 31194
dependencies:
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
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

### B.3:4.9 - Assurance consequence for unsupported `CausalityLadderRung` climb

`B.3` consumes `CausalUseSupportVerdict` from `C.28` when an assurance claim depends on causal-use support:

```text
CausalUseSupportVerdict = supported | bounded | unsupported | abstain
```

`CausalAssuranceTupleTrigger` is narrower than local causal-use repair. A local `C.28` downgrade, redirection to a named receiving relation, or abstain disposition does not require a new `B.3` assurance tuple by itself. Create or update a `B.3` tuple only when the causal-use claim is assurance-bearing, publication-bearing, release-bearing, or reused as an input to assurance, trust, certification, risk acceptance, or downstream selection. Exploratory causal wording, local causal wording repair, or a `C.28` cheap stop remains outside `B.3` until it changes assurance or publication posture.

Unsupported `CausalityLadderRung` climb lowers, blocks, or abstains from `R` for the affected causal-use claim. If `CounterfactualSamplingRealizabilityProfile.verdict = nonrealizable`, `B.3` lowers or blocks `R` for claims that require direct counterfactual-comparison sampling evidence. If `CounterfactualSamplingRealizabilityProfile.verdict = unknown`, direct-realization claims are unsupported, but identified, bounded, or simulation-only supported use may still be admissible when `C.28` declares the supported use and unsupported use.

Verdict consequences:

| `CausalUseSupportVerdict` | Assurance consequence | Admissible assurance wording |
| --- | --- | --- |
| `supported` | The causal-use claim contributes to `R` only inside the named `CausalUseSupportStatement`, scope `G`, evidence support basis, and cited profile refs. | "Supported only for the declared causal use under the cited support basis, profile refs, and scope." |
| `bounded` | `R` is bounded to the declared admissible-use limit; assurance prose must name the bound, the `CausalUseSupportStatement`, and the `CausalUseUnsupportedStatement`, and must not imply unqualified causal support outside them. | "Bounded causal support for the declared regime, population, policy, model, or window; unsupported outside that bound." |
| `unsupported` | The causal-use claim cannot raise `R`; it becomes `CausalUseUnsupportedStatement`, is downgraded, removed, or blocks the assurance claim when the causal use is necessary. | "Causal use unsupported for this assurance claim; use association/metric/simulation-only wording or block the causal assurance claim." |
| `abstain` | No causal-use conclusion contributes to `R`; the assurance tuple either proceeds only on named non-causal grounds or abstains from the affected causal claim. | "No causal-use conclusion is used; assurance proceeds only on named non-causal grounds or abstains from this causal claim." |

What changes in practice: assurance prose cannot say "high confidence that the policy caused improvement" when the evidence path only supports association or simulation-only counterfactual output; the unsupported causal step must degrade, abstain, or block the causal-use claim.

What this does not authorize: `B.3` does not determine the `CausalityLadderRung`, estimand, causal identification, evidence design, or realizability profile; it applies assurance consequences to the support verdict supplied by `C.28` and the evidence path supplied by `A.10`.

