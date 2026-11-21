---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__008_conformance-checklist.md"
commit_sha: "dba39812b83cac74dd2a3251c134cdc23dfaec86"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:7 — Conformance Checklist"
line_start: 59837
line_end: 59856
dependencies:
  - "A.10"
  - "A.13"
  - "A.18"
  - "A.19"
  - "A.6.5"
  - "A.6.P"
  - "C.11.CRC"
  - "C.11.DUA"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.38"
  - "C.39"
  - "C.40"
  - "C.9"
  - "E.10.LRN"
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
| `CC-C11.1` | A comparison **SHALL** use already-available options; when complete ways or new candidates still need construction, use their governing pattern first. | Keeps candidate construction and development outside local choice. |
| `CC-C11.2` | Identify who makes the choice and whether it is attributed to an individual or to an organized whole. A precise agency claim **SHALL** be governed by `A.13`. Measured characteristic and evidence claims retain their `A.17`–`A.19`, `C.16` and `A.10` grounds. | Makes the attribution of the choice inspectable. |
| `CC-C11.3` | When the question leaves local choice, the result **SHALL** identify the receiving question under §4.4, including candidate construction/development, pool policy, enactment or selector-facing result declaration when applicable. | Separates choice from candidate construction and development, the generation or archive/front account, pool policy, planning, and selector-facing result declaration. |
| `CC-C11.4` | A completed comparison **SHALL** identify the chooser, options, comparison basis, applicable dependence assumptions, any live probe decision, `ChoiceRule` and the `ChoiceResult` it supports. An open comparison identifies what the holder can use now and what still prevents closure (§4.2.4). | The recipient can use the result at the strength the available grounds support. |
| `CC-C11.5` | The comparison **SHALL** identify the applicable objects in §4.5.1, preserving its always-required versus conditionally activated distinction. | Keeps the objects of the calculus explicit. |
| `CC-C11.6` | Load-bearing terms in a decision record **SHALL** have recoverable meanings, using the local glosses or an explicit equivalent interpretation. | Prevents the core terminology from remaining implicit or displaced into outside basis carriers. |
| `CC-C11.7` | When a relation predicate or participant remains unclear, use `A.6.P`; when argument or slot structure remains unclear, use `A.6.5`. An already clear relation uses its governing rule directly. | Keeps dependence language inspectable and deconflicted. |
| `CC-C11.8` | An active-inference or quantum-like branch **SHALL** address a stated limitation of the current comparison; the branch name alone supplies no support. | Preserves practical meaning and avoids branch-name citation without operational load. |
| `CC-C11.9` | A local choice result **SHALL** remain distinct from any separately needed quantum-like, aggregation or multilevel formal support. | Keeps the pattern usable now while leaving heavier support work typed and explicit. |
| `CC-C11.10` | Use `ProbeBudget` for inquiry while the choice or reliance on it can still change. Apply the relevant information or computation value. Once the choice and its use are settled, resources for performing the chosen work belong to execution planning. | Identifies which decision the inquiry informs. |
| `CC-C11.11` | When the question shifts to declaring selector-facing set content, use `G.5`. For presentation or availability of an existing result, use `E.17` for its publication face and source return, and `E.24.PUB` for the publication occurrence and availability. | Preserves the boundary among local choice, selector-result declaration, and publication availability. |
| `CC-C11.12` | When a further dependence layer or neighboring family is used, the comparison **SHALL** state the limitation it addresses and the resulting change in the comparison. | Prevents branch-name citation from replacing use-time doctrine. |
| `CC-C11.13` | The result **SHALL** justify `choose now`, `reject current set`, `probe again` or `reroute` under the closure conditions; an unresolved comparison **SHALL** remain explicit. | Prevents the decision record from ending without a justified choice result. |
| `CC-C11.14` | The decision record **SHALL** make the chooser, option set, comparison basis, `ChoiceRule`, conditionally required inquiry content and `ChoiceResult` recoverable. Each result branch **SHALL** retain the content specified in §4.2.3. An inactive inquiry item creates no placeholder or omission record. | Keeps the pattern usable as one working decision record rather than one doctrinal memo. |
| `CC-C11.15` | If a `ChoiceResult` is supported by a causal effect, counterfactual comparison, causal policy, or off-policy causal evaluation claim, it **SHALL** carry `ChoiceResult.causalUseSpec?` with the target rung, claim kind, relevant support-component refs, support-result ref when consumed, supported use, and unsupported use. | Prevents decision-theory vocabulary from certifying causal-use support. |

