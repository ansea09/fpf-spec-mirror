---
chunk_kind: "child"
pattern_id: "I.2"
pattern_title: "Expanded Entry Disambiguation Cases"
section_id: "I.2"
section_title: ".8 - Causal-use and counterfactual-support repair"
source_path: "FPF-Spec.md"
output_path: "by_section/I.2/I.2__009_8-causal-use-and-counterfactual-support-repair.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "I.2 — Expanded Entry Disambiguation Cases"
  - "I.2 — .8 - Causal-use and counterfactual-support repair"
line_start: 92467
line_end: 92478
dependencies:
keywords:
---

### I.2.8 - Causal-use and counterfactual-support repair

- **Case signal:** "This policy would have prevented harm", "this intervention caused the improvement", "this fairness result is causal", "this method is better on counterfactual outcomes", or "these simulated counterfactuals prove the decision".
- **Initial uncertainty:** the reader may be seeing association, a metric disparity, temporal change, method execution, work-plan use, work occurrence, simulation output, deontic boundary language, or a real causal-use claim.
- **Plausible candidate patterns:** `C.28`, `A.10`, `B.3`, `C.11`, `C.19`, `C.24`, `C.26`, `C.27`, `D.5`, `G.5`, `G.9`, `A.15`, `A.3.2`, `A.6`, `C.16`.
- **Tempting wrong pattern:** use `D.5` to treat metric fairness as causal fairness; use `G.9` to compare methods across different causal rungs; use `C.26` to hide causal under quantum-like wording; use `C.27` to treat rate change as causal effect; use `A.15` or `A.3.2` to treat a sampling method, intervention procedure, or target-trial recipe as causal support by itself; use `A.6` to turn causal evidence into a duty or release gate.
- **Disambiguating fact:** the decisive question is not whether a causal-looking word appears. The decisive question is whether the claim is used to publish, choose, deploy, assure, audit, benchmark, or dispatch a causal use governed by `C.28`: effect, intervention success, counterfactual comparison, causal fairness, policy optimality, causal evidence support, off-policy/causal-RL evaluation, or causal method superiority.
- **Recognition repair or question reclassification:** if only a measured value is live, repair in `C.16`; if only rate, trend, or temporal adequacy is live, repair in `C.27`; if only method, work, or work-plan structure is live, repair in `A.15` and `A.3.2`; if only boundary duty or agreement language is live, split with `A.6`; if only residual QL modeling language is live, use `C.26` only after ordinary measurement, temporal, work, benchmark, proxy, and dynamics readings are exhausted.
- **Actual governing FPF pattern body or projection role:** `C.28` carries causal-use question, causality-ladder rung, claim kind, causal estimand, identification, counterfactual sampling realizability, causal evidence support basis, support record and verdict, supported use, and unsupported use. `A.10` carries evidence/provenance path, `B.3` carries assurance consequence, `D.5` carries ethical/fairness audit, `G.5` carries method dispatch, and `G.9` carries benchmark parity only as consumers of `C.28` support.
- **Admissible entry stop:** a cheap downgrade sentence, a local `CausalUseTriageRecord`, a local or durable `CausalUseEvidenceDesignRecord`, a `CausalUseSupportVerdict`, or a named neighbor-pattern use that cites `C.28` without claiming broader authority.
- **What not to infer:** a randomized procedure is not automatically counterfactual support; a simulation is not realized counterfactual data; a target-trial phrase is not proof of identification; a fairness metric is not causal fairness; a method benchmark is not comparable if methods sit on different causal rungs or estimands; and a causal support record does not by itself create a duty, promise, commitment, release gate, or admissibility predicate.

