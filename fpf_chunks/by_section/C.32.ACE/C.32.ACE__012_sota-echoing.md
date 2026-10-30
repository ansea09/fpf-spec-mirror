---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__012_sota-echoing.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:11 — SoTA-Echoing"
line_start: 77578
line_end: 77592
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
  - "architecture fitness-function source wording"
  - "architecture-characteristic eval program"
  - "comparison input"
  - "current-architecture evaluation"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "monitoring"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:11 - SoTA-Echoing

These rows document how source practice contributes to eval-program fields, result-use boundaries, and refresh conditions in C.32.ACE.

| Source to inspect | Why this source is load-bearing here | Transfer into ACE | Blocked overread |
|---|---|---|---|
| FPF source presentation `ТриПрототипаТриОшибки` (2022-03-26) | Separates variant, prototype, candidate, stake, solution, error, eval as variant comparison, and testing as error checking; also requires fair comparison and indicator selection. | Make eval a typed architecture evaluation over declared candidates and criteria. | A pass-fail result alone does not identify the evaluation question, criterion or receiving decision. One test can be sufficient when it answers the whole stated evaluation question. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Practitioner source for incremental architecture governance and feedback under source-side fitness-function terminology. | Recover the source meaning, then frame the architecture evaluation over the relevant ACS rows, Q-Bundle slots or structures, with parity when the inference requires it. | The source term alone establishes neither an FPF object kind nor an architecture characteristic. |
| `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`) | Practitioner source for metric categories and governance practice after quality goals are named. | Carry metric-cadence distinctions as eval-program fields, not as criteria rows. | A metric, dashboard, rank, or score is not a project criterion, selected architecture, or architecture decision. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Mature practitioner source for objective definitions, trade-off analysis, and least-worst choices under competing characteristics. | Require declared criteria and the protection needed for material counter-losses before synthesis, comparison or selection relies on eval results. | A better reading or rank does not authorize comparison, selection, choice, G.5 selected-set result declaration, actual publication, or decision by itself. |
| Goodhart and proxy-risk line, plus current FPF `E.13` | Optimized proxies can detach from the declared architecture concern. | Keep proxy repair in E.13 while ACE records the risk before result use. | An eval result cannot replace the declared architecture concern. |
| Current FPF `C.16`, `C.25`, `E.23`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `E.17`, `E.24.PUB`, and `C.11` | Existing patterns for the next questions for measurement, Q-Bundles, repeated improvement, comparison, selection, selected-set result declaration, publication, and local choice. | Keep ACE as the eval-program framing and typed-result dispatch boundary. | ACE does not validate measurement, define every eval result, define Q-Bundles, compare, select, declare a selected-set result under G.5, publish it to an audience, choose, or decide. |

**Source-currentness boundary.** Use each source row only for the ACE eval-program field, result-use boundary, or refresh condition named in that row. Recheck the row when a named book edition, source presentation, FPF pattern for the next question, metric practice, or evolutionary-architecture practice changes the transferred move. If the project wants criteria-row admission, measurement validity, Q-Bundle structure, explicit comparison, selection, selected-set result declaration, actual publication, local choice, evidence, assurance, or decision use, leave ACE and open the pattern for the next question.

