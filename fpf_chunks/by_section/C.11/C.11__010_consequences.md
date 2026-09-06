---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__010_consequences.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:9 — Consequences"
line_start: 47481
line_end: 47492
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

### C.11:9 - Consequences

| Benefits | Trade-offs / Mitigations |
| --- | --- |
| Keeps decision doctrine distinct from search, candidate-pool policy, and planning. | The same working episode now needs an explicit question split across choice, pool policy, and planning rather than one blurred rationality account. |
| Makes evidential, causal, and subjunctive branches comparable in one place. | The pattern becomes more explicit about dependence language and therefore needs tighter lexical discipline. |
| Keeps bounded-resource probing inside the doctrine rather than as one afterthought. | Fast-path use now carries a slightly richer inventory before the doctrine feels natural under pressure. |
| Keeps active-inference and quantum-like repairs visible without letting them silently replace the whole core. | Those lines stay load-bearing only when they change the actual `ChoiceResult`, unfinished state, or reroute logic; heavier formal packages still remain outside this body. |
| Makes the choice result explicit through one `ChoiceResult` record instead of one general statement that the case is complex. | Each decision record has to show why `choose now`, `reject current set`, `probe again`, or `reroute` is lawful, which removes rhetorical room to sound informed without committing to one result. |
| Makes downstream work cleaner because search, pool policy, publication, and enactment can receive one explicit output instead of one blurred upstream "decision happened" claim. | Reroutes now require one named next subject pattern and one reusable part of the record instead of one vague upstream claim that deliberation happened somewhere. |
| Lets one comparison stay open honestly through one explicit tie-set or `probe again` result instead of forcing a fake winner. | Some outcomes will look less rhetorically decisive because the pattern refuses to hide unfinished comparison under elegant prose. |

