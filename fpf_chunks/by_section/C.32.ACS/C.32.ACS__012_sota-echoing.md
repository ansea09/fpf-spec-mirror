---
chunk_kind: "child"
pattern_id: "C.32.ACS"
pattern_title: "Architecture Characteristic Criteria Set for Improvement Cycles"
section_id: "C.32.ACS:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACS/C.32.ACS__012_sota-echoing.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.32.ACS — Architecture Characteristic Criteria Set for Improvement Cycles"
  - "C.32.ACS:11 — SoTA-Echoing"
line_start: 65396
line_end: 65411
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.30"
  - "C.30.P"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.HCS"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "Q-Bundle"
  - "anti-Goodhart guard"
  - "architecture characteristic criteria set"
  - "criteria row"
  - "improvement cycle"
  - "protected counter-characteristic"
  - "proxy risk"
---

### C.32.ACS:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ACS. Keep a source citation only when the draft uses it to set or revise a criteria-row field, use-class rule, or receiving-pattern boundary.

| Source to inspect | Why this source is load-bearing here | Transfer into ACS | Concrete ACS mutation | Blocked overread |
|---|---|---|---|---|
| FPF source presentation `ТриПрототипаТриОшибки` (2022-03-26) | The presentation distinguishes eval from test and requires characteristic cards, scale procedures, fair comparison, explicit indicatorization, hard constraints, optimization goals, and risk signals. | Put characteristic rows and use classes before any ACE eval program or explicit comparison. | ACS row shape carries use class, scale form, current reading or no-reading reason, proxy risk, protected counter-characteristics, receiving use, and source-return condition. | An eval, test, dashboard, score, or hard constraint is not the architecture characteristic or project criterion by itself. |
| ISO/IEC 25010:2023 (`https://www.iso.org/standard/78176.html`) and SQuaRE quality-model practice | Current standard source for product quality vocabulary and measurement context. | Use standards as source catalogue material that must be rebound to the described holon, bearer, scale, and use class. | ACS separates source catalogue, HCS starter pack, draft project criteria rows, optimization indicators, monitored guardrails, and context-only rows. | A standard quality-model characteristic is not automatically an FPF project criterion, scale row, eval program, or holon ontology. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) | Current practitioner line treats architecture characteristics as criteria for success, trade-off analysis, scope, and governance. | Criteria rows must be admitted and typed before synthesis, residual optimization, measurement, or governance claims. | ACS rows supply the criteria consumed by `C.32`, `C.32.MLAO`, and later receiving patterns. | A broad architecture-characteristic list is not a project criteria set. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Mature practitioner line for least-worst trade-offs among competing architecture characteristics. | Keep explicit protected losses; explicit comparison belongs to `A.19.CPM` when comparison is being made. | ACS requires use class, proxy risk, protected counter-characteristics, and downstream comparison boundary. | No single criterion or local gain may dominate without naming the losses it can hide. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`), `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`), and `C.32.ACE` | Current practitioner line for guided change and repeatable eval over architecture characteristics. | Restore source-side fitness-function wording as eval programs over declared ACS rows. | Row shape has `evalProgramRefs?` and names ACE as the eval-program governing pattern after the row exists. | An eval program or metric is not a characteristic kind, project criterion, selected architecture, or decision. |
| Current FPF `C.25` and `E.13` | Local receiving law for composite quality families and proxy-for-value drift. | Keep Q-Bundle structure and proxy repair outside ACS while carrying the needed links. | Row shape includes `endpointShape`, `qBundleRef?`, `proxyRisk`, and `protectedCounterCharacteristicRefs`; proxy drift exits to `E.13`. | A composite quality family is not one scalar row, and a convenient indicator is not the declared architecture concern. |
| ATAM lineage and ATRAF 2025 (`https://arxiv.org/abs/2505.00688`) | Mature and current architecture-evaluation practice binds quality attributes to scenarios, trade-offs, sensitivity points, risks, and repeated refinement. | Admit a quality word as a project row with bearer, scale, polarity, counter-characteristics, and receiving use before it affects synthesis. | Explicit comparison belongs to `A.19.CPM`; composite quality bundles belong to `C.25`; ACS retains row preparation. | Scenario analysis and trade-off vocabulary do not compare or choose candidates until the receiving comparison, selection, choice, or decision pattern is being used. |

**Source-currentness boundary.** Use each source row only for the ACS field, use-class rule, or receiving-pattern boundary named in that row. Recheck the row when a named standard, book edition, source presentation, FPF receiving pattern, or current architecture-evaluation line changes the transferred move. If the project wants measurement, eval-program design, comparison, selection, publication of a selected set, local choice, evidence, assurance, or decision use, leave ACS and open the receiving pattern.

