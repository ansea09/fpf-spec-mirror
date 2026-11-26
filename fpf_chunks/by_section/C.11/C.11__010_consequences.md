---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__010_consequences.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:9 — Consequences"
line_start: 60061
line_end: 60072
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

### C.11:9 - Consequences

| Benefits | Trade-offs / Mitigations |
| --- | --- |
| Keeps decision doctrine distinct from search, candidate-pool policy, and planning. | The same working episode now needs an explicit question split across choice, pool policy, and planning rather than one blurred rationality account. |
| Makes evidential, causal, and subjunctive branches comparable in one place. | The pattern becomes more explicit about dependence language and therefore needs tighter lexical discipline. |
| Keeps bounded-resource probing inside the doctrine rather than as one afterthought. | Fast-path use now carries a slightly richer inventory before the doctrine feels natural under pressure. |
| Keeps active-inference and quantum-like repairs visible without letting them silently replace the whole core. | Those lines stay load-bearing only when they change the actual `ChoiceResult`, unfinished state, or reroute logic; heavier formal packages still remain outside this body. |
| Gives the recipient the choice and its basis. | A decision record must distinguish the reason to select an option from the reason to stop investigating it. |
| Makes downstream work cleaner because search, pool policy, publication, and enactment can receive one explicit output instead of one blurred upstream "decision happened" claim. | Reroutes now require one named next subject pattern and one reusable part of the record instead of one vague upstream claim that deliberation happened somewhere. |
| Keeps an unfinished comparison explicit through a tie-set or `probe again` result instead of forcing an unsupported winner. | Some outcomes will look less decisive because they state that the comparison is unfinished. |

