---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__008_conformance-checklist.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:7 — Conformance Checklist"
line_start: 45525
line_end: 45544
dependencies:
  - "A.13"
  - "A.18"
  - "A.19"
  - "A.6.5"
  - "A.6.P"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.9"
  - "G.5"
keywords:
  - "ChoiceResult"
  - "ChoiceRule"
  - "DecisionSubject"
  - "OptionSet"
  - "ValueOfComputation"
  - "ValueOfInformation"
  - "choose now"
  - "comparison basis"
  - "decision theory"
  - "non-shared comparison frame"
  - "probe again"
  - "probe-worthiness"
  - "question order"
  - "reject current set"
  - "reroute"
---

### C.11:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| `CC-C11.1` | The pattern **SHALL** state that `C.11` governs choice among already-available options rather than candidate generation. | Keeps `C.18` outside and prevents search takeover. |
| `CC-C11.2` | The pattern **SHALL** keep `DecisionSubject` as the default chooser term, and **SHALL NOT** use `Agent` as the generic chooser term unless one explicit agency claim is governed by `A.13`; measured characteristic and evidence claims use the A.17/A.18/A.19/C.16/A.10 stack, and planned `C.9` supplies no current governing force. | Prevents unwanted narrowing of the chooser. |
| `CC-C11.3` | The pattern **SHALL** state the boundary among `C.11`, `C.18`, `C.19`, `C.24`, and `G.5` explicitly in the body. | Prevents collapse of choice doctrine, candidate generation, candidate-pool policy, planning, and selector-facing result declaration. |
| `CC-C11.4` | `Solution` **SHALL** state one inspectable decision procedure from `DecisionSubject` and `OptionSet` through comparison basis, dependence layer, probe-worthiness test, one explicit `ChoiceRule`, and one emitted `ChoiceResult`. | Keeps `C.11` as one operational answer to the choice question rather than one survey of schools. |
| `CC-C11.5` | The pattern **SHALL** name one minimal decision inventory including `DecisionSubject`, `DecisionSubjectGranularity`, `OptionSet`, `PreferenceOrder`, `EvaluativeMeasure`, `BeliefState`, `OutcomeModel`, `ChoiceRule`, `ChoiceResult`, `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation`. | Keeps the calculus objectual rather than slogan-like. |
| `CC-C11.6` | Load-bearing inventory terms used in the pattern text **SHALL** receive local plain glosses or equivalent operational clarification inside the body. | Prevents the core terminology from remaining implicit or displaced into outside basis carriers. |
| `CC-C11.7` | Relation-heavy terms such as `PreferenceOrder`, `CounterfactualModel`, and `SubjunctiveDependenceRelation` **SHALL** remain answerable to `A.6.P` together with `A.6.5`. | Keeps dependence language inspectable and deconflicted. |
| `CC-C11.8` | Active-inference and quantum-like lines **SHALL** be introduced through the limitations they repair, not as prestige branch names. | Preserves practical meaning and avoids branch-name citation without operational load. |
| `CC-C11.9` | The pattern **SHALL** expose one minimal mathematical floor without overclaiming one full quantum-like or geometry-heavy formal package. | Keeps the pattern usable now while leaving heavier support work typed and explicit. |
| `CC-C11.10` | `ProbeBudget` **SHALL** stay in `C.11` while it means the budget for further probing before choice, and `ValueOfInformation` / `ValueOfComputation` **SHALL** stay theory-side comparative criteria even when `C.19` or `C.24` later consume their outputs. | Preserves the bounded-resource bridge without letting neighboring patterns steal the doctrine. |
| `CC-C11.11` | Shortlist or other selector-facing set-result declaration **SHALL NOT** be treated as part of `C.11`; if the question shifts to declaring or naming that result, the text **SHALL** apply `G.5`. Actual presentation or availability **SHALL** remain separate: use `E.17` for the publication face and return to source and `E.24.PUB` for the publication occurrence and availability. | Preserves the boundary among local choice, selector-result declaration, and publication availability. |
| `CC-C11.12` | When one heavier dependence layer or neighboring family line is activated, the text **SHALL** state what limitation of the simpler comparison it repairs and what changes in the actual comparison once that line is in play. | Prevents branch-name citation from replacing use-time doctrine. |
| `CC-C11.13` | The text **SHALL** make the closure rule explicit enough to justify why the lawful result is `choose now`, `reject current set`, `probe again`, or `reroute` rather than some softer holding-pattern output, and **SHALL** treat vaguer endings as unfinished rather than as lawful results. | Prevents the decision record from ending in one sophisticated but operationally empty result. |
| `CC-C11.14` | The decision record **SHALL** make one minimal decision-record shape explicit: chooser, option set, comparison basis, one explicit `ChoiceRule`, probe decision value, and one emitted `ChoiceResult`; `choose now`, `reject current set`, `probe again`, and `reroute` outputs **SHALL** each state their mandatory fields explicitly enough to determine the lawful choice result without reopening surrounding rationale. | Keeps the pattern usable as one working decision record rather than one doctrinal memo. |
| `CC-C11.15` | If a `ChoiceResult` is supported by a causal effect, counterfactual comparison, causal policy, or off-policy causal evaluation claim, it **SHALL** carry `ChoiceResult.causalUseSpec?` with the target rung, claim kind, relevant support-component refs, support-result ref when consumed, supported use, and unsupported use. | Prevents decision-theory vocabulary from certifying causal-use support. |

