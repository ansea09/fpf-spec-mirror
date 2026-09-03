---
chunk_kind: "child"
pattern_id: "A.11.OP"
pattern_title: "Decision-Relevant Least Action and Operational Parsimony"
section_id: "A.11.OP:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11.OP/A.11.OP__002_problem-frame.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.11.OP — Decision-Relevant Least Action and Operational Parsimony"
  - "A.11.OP:1 — Problem frame"
line_start: 23515
line_end: 23548
dependencies:
  - "A.11"
  - "A.11.OP"
  - "A.15.7"
  - "A.3.1"
  - "A.3.2"
  - "B.3"
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

The primary `EntityOfConcern` is one proposed mandatory requirement under one declared use and one substantive horizon. *Action*, *apparatus*, *requirement*, and *horizon* are ordinary working words here. This pattern introduces no generic `U.Apparatus`, `U.Move`, action kind, horizon kind, or result record.

**First useful result.** Return one of two short answers:

- retain the requirement for this use and horizon because it changes a named substantive branch, realizes an already selected result, or preserves a named assurance or recovery condition on which the use relies; or
- remove the requirement or leave it optional because none of those conditions changes when it is removed.

Ordinary use needs no score or separate record. Name the receiving decision, result, reliance, or recovery condition in the same sentence as the disposition.

**Three recognition cases.**

- A team has added a second status update before a repair decision. Every possible status leaves the same repair action, and no later user relies on the duplicate update.
- A laboratory considers a bounded probe that leaves today's setup unchanged but can determine which of two methods will be used next week.
- A release route contains both a deterministic build step that creates the selected publication and an assurance check whose evidence is consumed by the release decision.

These are one recurring problem across unlike situations: mandatory effort can be ceremonial, immediately productive, decision-relevant only later, or necessary because another use relies on the assurance or recovery condition it preserves.

**What goes wrong if missed.** Requirements accumulate because each sounds prudent in isolation, while their possible results change no substantive choice and produce no selected result. The opposite error removes exploration, deterministic realization, safety evidence, recovery support, or a small discriminating cue merely because it does not change the next administrative state.

**What this buys.** The practitioner can remove ceremony without treating the fewest steps as the goal. Useful exploration, realization work, assurance, option preservation, and recovery remain when their receiving use is named.

**Not this pattern when.**

- When a law, regulation, duty, permission, prohibition, safety floor, evidence rule, or gate condition is in question, use the pattern or authority that establishes that obligation. This pattern neither creates nor cancels it.
- When several already qualifying alternatives need comparison, use their direct choice, apparatus, architecture, or Method Engineering pattern.
- When the question is whether a new durable ontology value should exist, use `A.11`.
- When the question is how to use an already selected pattern, use `E.11.PUA` or `E.11.PUR`.
- When ongoing Work needs one next action chosen from current facts, use `A.15.7`.
- When an available direct-kind apparatus is already being configured for a declared use, use `C.19.2` for that application question.

