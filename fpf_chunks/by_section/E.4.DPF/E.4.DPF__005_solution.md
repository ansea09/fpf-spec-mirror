---
chunk_kind: "child"
pattern_id: "E.4.DPF"
pattern_title: "Domain Principle Framework Authoring and Local-Monolith Landing"
section_id: "E.4.DPF:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF/E.4.DPF__005_solution.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "E.4.DPF — Domain Principle Framework Authoring and Local-Monolith Landing"
  - "E.4.DPF:4 — Solution"
line_start: 64118
line_end: 64188
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.8"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.DPF:4 - Solution

Author the framework through a spine whose outputs are inspectable at each step:

First-hour route for a first framework:

1. Write a one-paragraph context note: domain or local context, intended reader, first use, and non-use boundary.
2. Create a source-pack stub: source traditions to inspect, rival traditions to avoid losing, first examples, and claim status.
3. Draft one PFAD question: what framework family is being created, what first pattern set is in scope, what depends on FPF Core, and what must not land in Core.
4. Mark public names provisional: use `Domain Principle Framework` or `Local Practice Framework` in prose, and send durable names or abbreviations to `F.18`.
5. Draft one to three first pattern candidates through `E.8`, each with a recognizable problem frame, positive solution, worked slice, and local anti-pattern.
6. Add relation and edition rows for those candidates: source reuse, specialization, publication, dependency, compatibility, or refresh as needed.
7. Pick the first-entry carrier: local readme, preface, table of contents, card set, or local monolith.
8. Name the first quality and refresh route: what will be evaluated, what can improve next, and what source, Core edition, or local-use change reopens the framework.

Stop the first hour when those outputs exist, even if every pattern body is still rough. A rough framework with context, source basis, decision question, provisional names, first pattern candidates, relation rows, publication carrier, quality route, and refresh trigger is inspectable. A long monolith without those outputs is not yet an FPF-grounded framework.

Prompt-shaped starter for SoTA harvesting and first candidate generation:

```text
Help draft a first FPF-grounded principle-framework candidate.

Bounded context:
Intended reader and first use:
Non-use boundary:
Source traditions to inspect:
Rival traditions or schools not to lose:
Local examples or internal sources:
Adopted source payload to carry into pattern solutions:
Rejected source payload and why rejected:
Candidate first patterns, each with problem frame, positive solution, worked slice, and local anti-pattern:
Candidate relation functions among the patterns:
Dependency on FPF Core or a domain framework edition:
Publication carrier for first entry:
Quality route: which first drafts should be evaluated and improved:
Refresh triggers: source change, Core edition change, local-use telemetry, or policy change:

Return the result as a draft source-pack summary, PFAD question, candidate pattern list, relation-record candidates, publication carrier note, quality-route note, and refresh-trigger note.
Do not present generated text as authoritative. State what must return to `G.2`, `C.35`, `E.4.PFAD`, `E.4.PFR`, `F.18`, `E.21`, and `G.11` before the framework can be relied on.
```

1. **Context declaration.** State the domain or local bounded context, intended reader, first use, and non-use boundary.
2. **Source pack.** Use `G.2` to gather SoTA traditions, claim sheets, examples, source-use decisions, rejected alternatives, and source-currentness notes.
3. **Architecture decision.** Use `E.9` and `E.4.PFAD` to decide purpose, framework family, pattern split, relation structure, publication unit, dependency boundary, and source-return obligations.
4. **Name preparation.** Use `E.10` for kind discipline and `F.18` for durable names before public pattern heads or abbreviations are stabilized.
5. **Carrier admission.** Use `C.33`, `C.34`, or `C.35` before relying on local monoliths, tables of contents, relation graphs, source summaries, search outputs, transformed views, or generated candidates as architecture evidence.
6. **Pattern drafting.** Draft patterns with `E.8`: recognition text, positive solution, worked cases, boundary, local anti-patterns, SoTA-Echoing, conformance checks, and relations.
7. **Relation and edition discipline.** Use `E.4.PFR` for relation functions, dependency direction, compatibility boundary, deprecation, supersession, and edition effects.
8. **Quality cycle.** Use `E.22` to frame the evaluation purpose, quality floor, trade-off question, and expected improvement proposal when that frame is not already scoped. Use `E.21` to evaluate pattern quality, `E.23` for repeated improvement, and `E.19` only when admission or profile gating is actually being claimed. If an evaluation result needs a carrier, publish or refresh that carrier through the direct publication or currentness owner rather than through `E.22`.
9. **Admission review.** Use `E.19` when the local process asks whether a pattern or framework slice is ready for admission.
10. **Local monolith landing.** Publish the framework in its own local monolith, readme, preface, table of contents, or equivalent first-entry carrier. Do not land domain or local frameworks into `FPF-Spec.md` by default.
11. **Currentness route.** Use `G.11` for refresh plans, edition pins, source decay, deprecation, and supersession conditions.

Starter evaluation characteristics for a principle-framework improvement loop:

| Characteristic question | Direct owner to use |
| --- | --- |
| Discoverability | Can the intended reader find the first useful entry and governing pattern? Use `E.11`, then evaluate the pattern or projection through the applicable quality owner. |
| Source fidelity | Are adopted and rejected source payloads recoverable in source packs, solutions, boundaries, and examples? Use `G.2`, `C.33`, `C.34`, and pattern-quality evaluation. |
| Ontology clarity | Are Core, domain, local, publication, source, decision, relation, quality, and refresh claims kept as different kinds? Use `E.10`, `F.18`, `F.19`, and the direct owner. |
| Relation typedness | Are pattern-use, specialization, dependency, publication, preservation, quality, and source-use relations separated? Use `E.4.PFR`. |
| Compatibility impact | Can maintainers see what breaks or must migrate when Core, domain, or local editions change? Use `E.4.PFR`, `E.5.3`, and `G.11`. |
| Refreshability | Are source decay, edition pins, local-use telemetry, and supersession conditions actionable? Use `G.11`. |
| Package navigability | Can the selected pattern set, relation records, source packs, decision records, quality evidence, and first-entry carrier be found without treating the package as runtime machinery? Use `G.5`, `E.4.PFR`, and `E.11`. |
| Adoption telemetry | Are repeated reader errors, skipped records, stale sources, and local-use failures routed to refresh or improvement? Use `G.11` and `E.23`. |
| Didactic first use | Can a first-time domain or local author write the first useful output without prior FPF developer knowledge? Use `E.11`, `E.12`, `E.21`, and `E.23`. |

These are evaluation characteristics for selecting and framing improvement work. They are not measurement programs by themselves. If the pass needs a measurement, eval, evidence, or adequacy record, create it through the pattern that owns that object, such as `E.21`, `E.9.DA`, `E.2.DA`, `C.16`, `A.10`, or the relevant architecture-characteristic pattern.

The spine is complete only when a reader can answer: what framework edition is being authored, which sources and decisions shaped it, which patterns and relations were selected, where it is published, how quality improves, and when it returns for refresh or repair.

