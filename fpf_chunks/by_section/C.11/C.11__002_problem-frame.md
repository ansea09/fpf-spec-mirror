---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__002_problem-frame.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:1 — Problem frame"
line_start: 59381
line_end: 59407
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

### C.11:1 - Problem frame

**When ongoing Work still needs a next action.** If admissible actions still have to be recovered from ongoing Work, its domain Method, and current facts, use `A.15.7` first. Return here only when a current chooser and `OptionSet` exist and comparison can change the result; a mandatory response or one familiar cue need not be expanded into an option set.


**Use this when.** Use this pattern when one `DecisionSubject` already has an `OptionSet` in hand and the question is how to choose among those already-available options under uncertainty, preference, causal or subjunctive dependence, and bounded probing or computation.

**First useful result.** Identify who makes this choice, the alternatives, what each could lead to, and the rule used to compare them. State which option or options the rule supports, why all fail, what further inquiry is worth doing, or where the remaining question belongs. When another party decides, that comparison can serve as advice. To report an actual decision, establish who made it or which authorized procedure put its result into effect.

When a choice is still open, give the recipient the comparison available now, the missing grounds and who can settle it. A supported recommendation or an unfinished comparison can be delivered before the holder decides.

**First-minute questions.**

- Who or what makes this choice? If several participants contributed, to whom is the decision attributed?
- What options are already on the table now?
- What current basis is being used to compare them?
- What could a further observation or calculation change about the choice or what the recipient can rely on?
- Is this still local choice, or has the question moved to a neighboring problem—for example, search, pool policy, selector-result declaration, publication availability, or enactment?

**When advice still hides the decision.** Use `C.11.DUA` when a recommendation or evidence demand still needs its receiving question, demanded work or requirement merits recovered. Return here when a current chooser and options support a local choice. An already adequate choice uses this pattern directly.

**Typical reroutes.** For candidate construction or development, use `C.38`–`C.40` as specified in §4.4; that section also distinguishes pool policy, selected-set publication and enactment. Use `A.13` when agency itself is at issue, or `A.18`/`A.19` when Scale bindings or a declared CharacteristicSpace or reusable predicate are the unresolved question.

**What the chooser gets.** The same options can yield different recommendations if they indicate an outcome, bring it about, or depend on what another chooser will do. Identify the dependence that matters, then check which alternatives the current facts support and what further inquiry could change.

**Not this pattern when.** Do not start here when the current question is still generating candidate options, setting exploration or exploitation policy over a candidate pool, declaring selector-facing set-result content, making that result available to an audience, or sequencing execution under an operational plan.

