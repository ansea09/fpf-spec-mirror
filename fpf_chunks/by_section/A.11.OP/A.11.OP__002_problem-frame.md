---
chunk_kind: "child"
pattern_id: "A.11.OP"
pattern_title: "Decision-Relevant Least Action and Operational Parsimony"
section_id: "A.11.OP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11.OP/A.11.OP__002_problem-frame.md"
commit_sha: "f6ee315e560a523f6381f264c03f46bcd3c7bdc0"
heading_path:
  - "A.11.OP — Decision-Relevant Least Action and Operational Parsimony"
  - "A.11.OP:1 — Problem frame"
line_start: 23575
line_end: 23610
dependencies:
  - "A.10"
  - "A.11"
  - "A.11.OP"
  - "A.15.1"
  - "A.15.7"
  - "A.19"
  - "A.3.1"
  - "A.3.2"
  - "B.3"
  - "C.11"
  - "C.11.DUA"
  - "C.19.2"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.13"
  - "E.23"
  - "E.5"
keywords:
---

### A.11.OP:1 - Problem frame

**Use this when.** Use this pattern when someone proposes making an action or apparatus mandatory and a plausible question remains: does this requirement change the subject work, or does it only make the route look controlled?

The primary `EntityOfConcern` is one proposed mandatory requirement under one declared use and one substantive horizon. The pattern screens the requirement for a substantive contribution. A contribution is necessary, but does not alone make the work obtainable, worthwhile or obligatory; *action*, *apparatus*, *requirement*, and *horizon* keep their ordinary meanings.

**First useful result.** Return one of two short answers:

- retain the requirement for this use and horizon because it has a named substantive contribution and its direct choice, realization, assurance or authority basis justifies requiring the work; or
- remove the requirement or leave it optional because it has no such contribution, or because a contribution does not justify its burden for this use.

For a proposed inquiry whose worth is still open, use `C.11.DUA` to compare what can be gained with feasible effort, delay, opportunity cost and downside; use `C.11` when a current chooser and options need a local choice. Finish with the supported answer and feasible continuation, which may retain the current action, narrow a claim or decline an unsupported use.

Ordinary use needs no score or separate record. Name the receiving decision, result, reliance, or recovery condition in the same sentence as the disposition.

**Three recognition cases.**

- A team has added a second status update before a repair decision. Every possible status leaves the same repair action, and no later user relies on the duplicate update.
- A laboratory considers a bounded probe that leaves today's setup unchanged but can determine which of two methods will be used next week.
- A release route contains both a deterministic build step that creates the selected publication and an assurance check whose evidence is consumed by the release decision.

These are one recurring problem across unlike situations: mandatory effort can be ceremonial, immediately productive, decision-relevant only later, or necessary because another use relies on the assurance or recovery condition it preserves.

**What goes wrong if missed.** Requirements accumulate because each sounds prudent in isolation, while their possible results change no substantive choice and produce no selected result. The opposite error removes exploration, deterministic realization, safety evidence, recovery support, or a small discriminating cue merely because it does not change the next administrative state.

**What this buys.** The practitioner can remove ceremony without treating the fewest steps as the goal. Useful exploration, realization work, assurance, option preservation, and recovery remain when their receiving use is named.

**Not this pattern when.**

- When the question is the force or applicability of an instituted obligation, use its direct authority. Apply A.11.OP only to discretionary apparatus inside the space it leaves. If the present question concerns the obligation's merits, use `C.11.DUA` to examine its protective contribution, burden and feasible amendment; that appraisal does not cancel its current force.
- When several already qualifying alternatives need comparison, use their direct choice, apparatus, architecture, or Method Engineering pattern.
- When the question is whether a new durable ontology value should exist, use `A.11`.
- When the question is how to use an already selected pattern, use `E.11.PUA` or `E.11.PUR`.
- When ongoing Work needs one next action chosen from current facts, use `A.15.7`.
- When an available direct-kind apparatus is already being configured for a declared use, use `C.19.2` for that application question.

