---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Method-Family Registry, Dispatch and Selected-Set Result Declaration"
section_id: "G.5:11"
section_title: "SoTA-Echoing — return what the receiving use can actually select"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__018_sota-echoing-return-what-the-receiving-use-can-actually-select.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "G.5 — Method-Family Registry, Dispatch and Selected-Set Result Declaration"
  - "G.5:11 — SoTA-Echoing — return what the receiving use can actually select"
line_start: 113766
line_end: 113779
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "C.32.P2S"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
  - "E.4.PFR"
  - "G.0"
  - "G.11"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "JointUseSet"
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry and eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set result declaration"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:11 - SoTA-Echoing — return what the receiving use can actually select

**Practice question.** What should a dispatcher hand over when several candidates remain useful but the declared comparison does not justify one winner? The selected line returns the admissible alternatives with their ordering status and basis. A serious default chooses one best candidate under a declared objective and returns it ready for use. That default is efficient when the objective settles the choice; it loses a needed alternative when an undeclared scalar objective is substituted for an unresolved trade-off.

The [scikit-learn GridSearchCV documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), `refit` and `best_estimator_`, supplies the concrete default. It can choose one estimator by a scorer or a custom rule over the evaluation results; multi-metric evaluation still needs a specified refit choice. **Adopt** that explicit-choice requirement when G.5 emits an ordered result. **Reject** reading a single best-estimator interface as a warrant to invent the missing comparator. The library supports custom choices and exposes other candidate results; it does not require G.5 to discard them.

[PS-AAS, Kostovska et al. (2023)](https://proceedings.mlr.press/v224/kostovska23a.html) supplies a substantive alternative-selection line: form a complementary portfolio for later algorithm selection, balancing coverage with the cost of a larger choice problem. Its experiments concern specified CMA-ES variants and BBOB tasks, not arbitrary Methods. **Adapt** the distinction between forming an eligible pool and selecting a member to `Shortlist` and `RankedShortlist` in §4.4b, S3 and the pump case in §0.5. The selected line here is this result discipline, not a claim that PS-AAS is the best portfolio algorithm for every task.

A different receiving use combines members. [Split-Ensemble, Chen et al. (2024)](https://proceedings.mlr.press/v235/chen24aw.html) supplies a concrete counterexample to treating every retained set as alternatives: its submodels serve complementary subtasks in one ensemble. **Adapt** that use distinction to `JointUseSet` and `G.5-6 DeclareSetResult`. G.5 states all-member inclusion; the paper's trained ensemble does not establish compatibility or effective combined use for an arbitrary set of framework editions. Show 4 therefore keeps those claims with their own patterns.

In §0.5 both grounded pump Methods meet the task constraints, but no admitted comparator orders them. With the same candidate evidence, returning the pair as an unordered `Shortlist` preserves the receiving choice at the cost of one further decision. Naming the spectral Method “best” would require an additional criterion and its supporting comparison. If that criterion is supplied and actually orders the candidates, a ranked result is available. If the receiving use includes every exact member, declare that different membership meaning; a ranking does not establish it. These distinctions govern the outcome declarations and the positive, ranked, no-survivor and joint-use cases in §5.

Reopen when new evidence changes eligibility, a comparator supplies or defeats an ordering, the downstream use changes from alternatives to joint inclusion, or keeping the retained set costs more than the receiving decision can bear. A bounded handoff or abstain outcome remains available. None of these sources establishes actual selection Work, a Method's identity, public availability or assurance merely from the emitted result.

