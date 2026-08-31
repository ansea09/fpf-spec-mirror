---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 47190
line_end: 47208
dependencies:
  - "A.10"
  - "A.13"
  - "A.18"
  - "A.19"
  - "A.6.5"
  - "A.6.P"
  - "C.11.CRC"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.26"
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

### C.11:8 - Common Anti-Patterns and How to Avoid Them

One quick usability test helps here: if the closing line does not state one lawful choice result for the working chooser or team, the current result is still unfinished even if the doctrine survey looks polished.

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| --- | --- | --- | --- |
| Candidate-formation or search takeover | The text starts constructing complete ways or generating options as if that work were already part of decision doctrine. | `C.11` loses its decision-theory EntityOfConcern and silently absorbs `C.38` or `C.18`. | State the option set as already existing; use `C.38` for same-result way formation and `C.18` for open-ended generation. |
| Policy collapse | Exploration or exploitation governance over a candidate pool is written as if it were identical with choosing among current options. | Choice doctrine and candidate-pool policy become indistinguishable. | `C.19` remains explicit as the neighboring pattern for selection policy and exploration governance. |
| Planning collapse | Sequencing, replanning, and enactment budgeting are written as if they were already part of the choice calculus. | Planning-side question moves out of `C.24` by accident. | Execution order and operational budgeting remain in `C.24`, even when `C.11` says more probing is rational. |
| Inventory without decision rule | The current comparison names many objects and schools but never shows how to move from a live option set through one `ChoiceRule` to one `ChoiceResult`. | The pattern becomes one cleaned-up survey rather than one decision discipline. | State one explicit decision-record shape: chooser, option set, comparison basis, dependence layer, probe-worthiness test, one explicit doctrine, and one emitted result. |
| Hidden basis shift | Different options are compared under different belief states, outcome models, or dependence layers without one explicit statement that the basis changed. | The comparison only looks precise; in fact the choice rule cannot be audited. | Keep one shared comparison basis until one named probe or model change updates it, and state explicitly when the dependence layer changes. |
| No closure rule | The text sounds careful but never says what makes `choose now`, `reject current set`, `probe again`, or `reroute` lawful. | The record never closes into one explicit decision result. | State the closure conditions explicitly and show why the current case satisfies exactly one of them. |
| Undefined load-bearing terms | Terms such as `PreferenceOrder`, `BeliefState`, or `OutcomeModel` appear without local operational clarification. | Core comparison objects stay implicit and the decision question depends on outside theory or undocumented assumptions. | Give one local plain gloss or equivalent operational clarification for each load-bearing term used in the pattern text. |
| Bounded-resource bridge loss | `ProbeBudget`, `ValueOfInformation`, or `ValueOfComputation` are mentioned, but the text silently lets `C.19` or `C.24` own them. | The theory-side doctrine disappears into neighboring policy or planning prose. | Keep those objects theory-side in `C.11`; let neighboring patterns consume their outputs without minting the concepts. |
| Result-boundary collapse | The text treats declaring selector-facing set content, or later making it available, as if either were identical with deciding. | Choice doctrine silently absorbs the `G.5` result question or the publication question. | Keep both outside `C.11`: use `G.5` to declare the selector-facing result, `E.17` for its publication face and return to source, and `E.24.PUB` for the publication occurrence and availability. |
| Agent-default narrowing | Every chooser is described as one `Agent` even when the subject is really one team, organization, or other collectivity-bearing system. | The governed chooser is narrowed before the doctrine even starts. | `DecisionSubject` remains the default, and `DecisionSubjectGranularity` types the chooser-bearing level. |
| Prestige-branch citation | Active inference or quantum-like work is cited only as one fashionable name. | The text sounds current without stating what limitation is being repaired. | The repaired limitation is stated directly: embodied online updating for active inference, and context or order effects for quantum-like lines. |
| Cost-free deliberation | The text speaks as if probing and computation are free. | Bounded-resource doctrine disappears behind one idealized choice moment. | `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` stay visible in the calculus. |

