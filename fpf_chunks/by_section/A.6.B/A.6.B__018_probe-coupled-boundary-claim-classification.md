---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:15a"
section_title: "Probe-coupled boundary claim classification"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__018_probe-coupled-boundary-claim-classification.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:15a — Probe-coupled boundary claim classification"
line_start: 11916
line_end: 11972
dependencies:
  - "A.10"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.8"
  - "U.Commitment"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
  - "U.SpeechAct"
keywords:
  - "(MUST"
  - "(ii) claim that evidence carriers exist (that is E-)"
  - "(ii) encode runtime entry predicates (those are A-)"
  - "Keeps normative content"
  - "MAY"
  - "MUST"
  - "MUST NOT"
  - "MUST NOT hide a gate predicate (that is A-)"
  - "SHALL"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "accountable norms and grants"
  - "actual exercise"
  - "an individual-duty D- claim MUST name its actual bearer and exact separately obtaining U.Commitment"
  - "and MAY"
  - "and MUST NOT cite D-*"
  - "and SHALL are to be interpreted as in RFC 2119/8174. Lower-case must"
  - "and evaluated results distinct"
  - "and should in explanatory prose is descriptive"
  - "as if it were an agent obligation"
  - "as if it were an agent obligation. (It is a gate predicate"
  - "as operators"
  - "atomic L/A/D/E claims"
  - "conflict claims"
  - "direct obtaining conditions"
  - "entry predicates"
  - "evaluated findings"
  - "evaluation"
  - "individual institution"
  - "laws"
  - "may"
  - "not a duty.)"
  - "not normative"
  - "observable effects and evidence"
  - "or (iii) assert evidence existence or measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility or enforcement (that is D-*)"
  - "or MAY) as operators inside the law or definition itself"
  - "or observation that settles it and any evidence used for reliance"
  - "responsibility"
  - "they report adjudicable results rather than obligations"
  - "“commits to”)"
  - "“is admissible”"
  - "“is blocked”"
  - "”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
---

### A.6.B:15a - Probe-coupled boundary claim classification

When boundary text says that an interaction changes the state represented by its
output, identify the interaction, the changed state, and the receiving use, then
classify the atomic claims through the same L/A/D/E square. Such interactions may
include asking a question, measuring or intervening through a metric, reading a
dashboard, conducting a workshop, exporting through a Bridge, or making an API
read. Probe-coupled boundary language does not create a fifth quadrant.

Action classification:

1. Copy the boundary sentence being used for a decision.
2. Split it into its atomic claims before judging it, retaining only the classes
   present in the source: definition or law, runtime admissibility, generic
   prescription or individual duty, work effect or evaluated result, and any
   separate evidence-support claim.
3. Give each atomic claim its quadrant and any identifier required by a later reference.
4. Put the state, probe, update, or export part in the quadrant where it belongs rather than treating "quantum-like boundary" as one claim.
5. Apply `A.6.P` to reusable relation words; use `F.18` only when recovered terms
   need durable names. Use `A.10` for needed evidence support, `B.3` for a named
   assurance question, `C.16` for measurement, and `F.9` for a Bridge question.
   Use `C.26.1` for the residual probe-coupled question only when the interaction
   participates in the represented state and its output is being used as a
   passive read or export despite that decision-relevant effect.
6. Use a Claim Register row set only when the classified claim set is
   decision-bearing, reusable, contested, assurance-facing, or likely to be cited
   across faces; otherwise keep the atomic prose.

For a local working note, atomize the sentence mentally and write one or more
atomic L/A/D/E-classified sentences, preserving every source claim. One sentence
suffices only when one logical job remains. Use the Claim Register when the claim
set must survive reuse or dispute; the phrase "quantum-like boundary" is not a
substitute for its separate claims.

| Quantum-like boundary phrase hides | Claim class | What the user writes |
| --- | --- | --- |
| The term, variable, state, frame, or relation being defined | `L-*` law or definition claim | Definition or invariant, without agent obligation language |
| When a mechanism admits use of a probe, metric, question, or bridge at the decision point; declaration-level intended-use scope remains in `Signature.Applicability` | `A-*` runtime-admissibility claim | Entry predicate, required current inputs, non-admitted outcome, and neighboring-pattern continuation |
| What exact policy prescribes about applying, retaining, exposing, or avoiding overuse of the probe result; or which actual bearer has that individually instituted duty; and, if separately claimed, who bears responsibility | generic `D-*` prescription or individual `D-*` claim about one exact `U.Commitment`; separate direct responsibility claim or missing governor | Exact normative source and rule content for the generic branch; actual duty bearer and referenced L/A/E claim IDs or canonical locations for the individual branch; responsibility predicate and participants only when that relation independently obtains |
| The actual work effect or observed before-state or after-state, plus any separate evidence relation or carrier used for reliance | `E-*` work-effect or evaluated-result claim; separate evidence-support claim when current | Exact predicate and object, actual Work, evaluation, or observation, conditions and window, and result; add an A.10 evidence relation and exact carrier only when a receiving use relies on that support |

Useful outputs:

- a Claim Register row set when decision, reuse, contest, assurance, or cross-face
  citation needs it;
- one or more atomic L/A/D/E-classified sentences preserving every source claim
  for a local working note;
- an ordinary A.6.B L/A/D/E-classified claim set when no probe-coupled
  state-reading question remains;
- the `C.26.1:4.2` decision and finish result for a residual probe-coupled question
  that meets the activation condition above;
- the evidence-support, assurance, measurement, or Bridge result or continuation
  required by `A.10`, `B.3`, `C.16`, or `F.9` for the corresponding current question.

Do not write "the boundary is quantum-like" as one claim without L/A/D/E classification. Identify the interaction and its receiving use, split and classify the claims,
then apply the `C.26.1` activation condition above to any remaining question.

