---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__012_sota-echoing.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:11 — SoTA-Echoing"
line_start: 65545
line_end: 65559
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ACE. Keep a source citation only when the draft uses it to set or revise an eval-program field, result-use boundary, or refresh condition.

| Source to inspect | Why this source is load-bearing here | Transfer into ACE | Concrete ACE mutation | Blocked overread |
|---|---|---|---|---|
| FPF source presentation `ТриПрототипаТриОшибки` (2022-03-26) | Separates variant, prototype, candidate, stake, solution, error, eval as variant comparison, and testing as error checking; also requires fair comparison and indicator selection. | Make eval a typed architecture evaluation over declared candidates and criteria. | `test` is admitted only as one `evalOperation` when expectation failure or hard-constraint checking is current; parity frame and result form are mandatory. | A test, check, or pass-fail result is not the whole eval program, not the criterion, and not the decision. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner source for incremental architecture governance and feedback under source-side fitness-function terminology. | Restore the source term to FPF eval programs over ACS rows, Q-Bundle slots, candidate structures, and parity frames. | ACE record names evaluated rows, purpose, scope, eval operation, trigger mode, result form, run context, receiving use, and refresh or retire condition. | Fitness-function wording is not imported as the FPF object name or as a new architecture characteristic kind. |
| `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`) | Current practitioner source for metric categories and governance practice after quality goals are named. | Carry metric-cadence distinctions as eval-program fields, not as criteria rows. | ACE distinguishes scope, trigger mode, result form, run context, method refs, and refresh or retire condition. | A metric, dashboard, rank, or score is not a project criterion, selected architecture, or architecture decision. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Mature practitioner source for objective definitions, trade-off analysis, and least-worst choices under competing characteristics. | Require declared criteria rows and protected counter-characteristics before synthesis, comparison, or selection uses eval results. | ACE rows carry proxy risk, protected counter-characteristics, and receiving use before result-driven action. | A better reading or rank does not authorize comparison, selection, choice, G.5 publication of a selected set, or decision by itself. |
| Goodhart and proxy-risk line, plus current FPF `E.13` | Optimized proxies can detach from the declared architecture concern. | Keep proxy repair in E.13 while ACE records the risk before result use. | ACE requires proxy risk and protected counter-characteristics; proxy drift exits to `E.13`. | An eval result cannot replace the declared architecture concern. |
| Current FPF `C.16`, `C.25`, `E.23`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, and `C.11` | Existing receiving patterns for measurement, Q-Bundles, repeated improvement, comparison, selection, publication of selected sets, and local choice. | Keep ACE as the eval-program framing and typed-result dispatch boundary. | The relation table names C.16 for measurement validity and readings, C.25 for composite quality, E.23 for improvement feedback, A.19.CPM for comparison, A.19.SelectorMechanism for set-returning selection, G.5 for publication of selected sets, and C.11 for local choice; each actual typed result stays with its selected direct owner. | ACE does not validate measurement, own every eval result, define Q-Bundles, compare, select, publish a selected set under G.5, choose, or decide. |

**Source-currentness boundary.** Use each source row only for the ACE eval-program field, result-use boundary, or refresh condition named in that row. Recheck the row when a named book edition, source presentation, FPF receiving pattern, metric practice, or evolutionary-architecture practice changes the transferred move. If the project wants criteria-row admission, measurement validity, Q-Bundle structure, explicit comparison, selection, publication of a selected set, local choice, evidence, assurance, or decision use, leave ACE and open the receiving pattern.

