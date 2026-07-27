---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__001_intro.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:intro — Intro"
line_start: 51028
line_end: 51049
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.22"
  - "C.22.1"
  - "C.22.PFR"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.MOVE"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.18.1"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "actual PFR versus non-actual or solvability claim"
  - "assertion polarity"
  - "current reliance"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card episteme"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "validation boundary"
---

## C.22.2 - ProblemCard@Context

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Context-bound problem card.

**Intent.** Give a practitioner one compact problem-side record that turns a messy problem signal into a reviewable problem-side record before downstream Principles-to-Work (P2W) or selector use, while leaving claims outside the card to the governing FPF patterns that govern those claims.

**Use this when.** Use this pattern when work starts from a signal, anomaly, drift, risk, hypothesis, stakeholder demand or concern, set-derived candidate, underused capability, new constraint, new environment, opportunity-like cue, or solution-shaped request, and downstream task typing, method-family selection, work planning, evidence use, gate passage, autonomy control, or P2W requires a reviewable problem-side record. Also use it when P2W would otherwise use a slogan, wish, ticket-shaped task, preselected work request, or solution-shaped task as if it were reviewable problem-side output.

**Do not use this when.** Use another pattern directly when the question under repair is already work planning, method selection, evidence, provenance, assurance, gate decision, autonomy, archive, selected-set governance, mathematical-lens use, or ordinary discussion with no project-side move.

**Builds on.** `E.2`, `E.9`, `E.10`, `C.2.P`, `A.6.P`, `C.16.Q`, `C.16`, `A.19`, `C.22`, `C.25`, `C.29`, `G.5`, `G.9`, `A.6.3.RT`, and `A.6.4`.

**Coordinates with.** `C.11`, `C.18`, `C.19`, `C.22.1`, `C.22.PFR`, `C.24`, `C.27`, `C.28`, `A.15`, `A.15.5`, `A.21`, `E.16`, `G.6`, `G.11`, `A.10`, `B.3`, `E.17`, `E.17.ID.CR`, `A.6.3`, `F.9`, `E.18`, `C.32.P2S`, and `E.10.MOVE`.

**Boundary summary.** `C.22.2` use starts from messy problem-side signals and yields one reviewable `ProblemCard@Context`, a `P2W-ready` problem-side input for downstream `C.22`, or a stop with a governing-pattern cue for the claim being made, relation, or boundary outside the card.

**Claim-family, actuality, and solvability boundary.** A `ProblemCard@Context` is an episteme and may carry several distinct claims without creating or ending an actual Problem. An actual-problem assertion states affirmative or negative polarity for the exact `ProblematicForRelation` obtaining predicate. An affirmative assertion may designate an already individuated current occurrence only when `C.22.PFR` independently establishes it. Negative polarity neither creates, erases, nor reidentifies an occurrence; any reference to an independently established occurrence retains its exact temporal and contextual qualification under its direct governor. The card, its acceptance, and its publication do not make the relation obtain. Only when an explicit reliance judgment is current for the declared use does `A.10` or the receiving evaluation separately state supported, refuted, or unresolved reliance; that result does not make the relation obtain. A forecast, scenario, counterfactual, or anticipated-condition claim keeps its exact assumptions, horizon, evidence, and direct governor under `C.2.1`, `C.27`, `C.28`, or the more specific claim pattern and does not assert a current PFR merely by affirmative polarity. A claim that no supported method is currently known concerns method availability, evidence, constraints, and the intended use; selecting a method changes that solvability claim but does not end an obtaining `ProblematicForRelation`. The actual Problem ceases only when its actual-condition relation, criterion-applicability relation, or adverse predicate truth ceases under `C.22.PFR`.

