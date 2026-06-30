---
chunk_kind: "child"
pattern_id: "E.4.DPF"
pattern_title: "Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly"
section_id: "E.4.DPF:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF/E.4.DPF__005_solution.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.4.DPF — Domain Principle Framework Authoring and Publication-or-Access Carrier Assembly"
  - "E.4.DPF:4 — Solution"
line_start: 64766
line_end: 64860
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
  - "E.4.DPF.DA"
  - "E.4.FPF"
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
3. Draft one PFAD question: what framework family is being created, which domain or local problem-situation architecture and solution-move architecture the first pattern set will render, what depends on FPF Core, and what must not land in Core.
4. Mark public names provisional: use `Domain Principle Framework` or `Local Practice Framework` in prose, and send durable names or abbreviations to `F.18`.
5. Draft one to three first pattern candidates through `E.8`, each with a recognizable problem frame, known failure mode or local anti-pattern, positive SoTA-informed solution move, worked slice, and boundary. In the first hour these are pattern seeds unless they already pass the declared `E.21` pattern-quality use.
6. Add relation and edition rows for those candidates: source reuse, specialization, publication, dependency, compatibility, or refresh as needed.
7. Pick the first-entry and publication or access carrier: readme, preface, table of contents, card set, all-in-one local carrier, split document set, skill pack, MCP-backed access service, or another access face.
8. Name the first quality and refresh route: what will be evaluated, what can improve next, and what source, Core edition, or local-use change reopens the framework.

Stop the first hour when those outputs exist, even if every pattern body is still rough. A rough framework with context, source basis, decision question, provisional names, first pattern candidates, relation rows, publication carrier, quality route, and refresh trigger is inspectable. A long all-in-one carrier without those outputs is not yet an FPF-grounded framework. Do not promote this rough output to a reliance-bearing DPF publication carrier until the DRR or decision carrier is checked for the intended authoring use, the pattern bodies are hardened as normal FPF patterns, and the package is evaluated through `E.4.DPF.DA`.

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
Recurring domain or local problem situations and forces:
Reusable solution moves and consequences:
Candidate first patterns, each with problem frame, positive solution, worked slice, and local anti-pattern:
Candidate relation functions among the patterns:
Dependency on FPF Core or a domain framework edition:
Publication or access carrier for first entry:
Quality route: which first drafts should be evaluated and improved:
Refresh triggers: source change, Core edition change, local-use telemetry, or policy change:

Return the result as a draft source-pack summary, PFAD question, candidate pattern list, relation-record candidates, publication or access carrier note, quality-route note, and refresh-trigger note. If the requester wants a ready DPF rather than a seed, return the developer DRR or decision carrier and the user DPF publication or access carrier as separate artifacts or clearly separated sections, then name which `E.21`, `E.4.DPF.DA`, and refresh checks remain before reliance.
Do not present generated text as authoritative. State what must return to `G.2`, `C.35`, `E.4.PFAD`, `E.4.PFR`, `F.18`, `E.21`, and `G.11` before the framework can be relied on.
```

1. **Context declaration.** State the domain or local bounded context, intended reader, first use, and non-use boundary.
2. **Source pack.** Use `G.2` to gather SoTA traditions, claim sheets, examples, source-use decisions, rejected alternatives, and source-currentness notes.
3. **Architecture decision.** Use `E.9` and `E.4.PFAD` to decide purpose, framework family, domain or local problem-and-solution architecture, pattern split, relation structure, publication carrier, access carrier, dependency boundary, and source-return obligations.
4. **Name preparation.** Use `E.10` for kind discipline and `F.18` for durable names before public pattern heads or abbreviations are stabilized.
5. **Carrier admission.** Use `C.33`, `C.34`, or `C.35` before relying on all-in-one carriers, tables of contents, relation graphs, source summaries, search outputs, transformed views, or generated candidates as architecture evidence.
6. **Pattern drafting.** Draft patterns with `E.8`: recognition text, positive solution, worked cases, boundary, local anti-patterns, SoTA-Echoing, conformance checks, and relations. In a DPF, those pattern bodies are the pattern-language rendering of selected domain or local problem-situation architecture and solution-move architecture. `E.8` means a normal action-guiding pattern body, not only a section skeleton. A thin skeleton, prompt seed, or compressed design note remains a pattern seed until `E.21` says it is adequate for the declared DPF use.
7. **Relation and edition discipline.** Use `E.4.PFR` for relation functions, dependency direction, compatibility boundary, deprecation, supersession, and edition effects.
8. **Quality cycle.** Use `E.22` to frame the evaluation purpose, quality floor, trade-off question, and expected improvement proposal when that frame is not already scoped. Use `E.4.DPF.DA` to evaluate the package as a DPF or local-framework package, `E.21` to evaluate individual pattern quality, `E.23` for repeated improvement, and `E.19` only when admission or profile gating is actually being claimed. If an evaluation result needs a carrier, publish or refresh that carrier through the direct publication or currentness owner rather than through `E.22`.
9. **Admission review.** Use `E.19` when the local process asks whether a pattern or framework slice is ready for admission.
10. **Framework publication-or-access carrier assembly.** Publish or expose the framework in its own DPF or local-framework carrier: all-in-one local carrier, split readme, preface, and pattern files, table of contents, cards, skill pack, MCP-backed access service, retrieval route, or another first-entry form. Do not land domain or local frameworks into `FPF-Spec.md` by default.
11. **Currentness route.** Use `G.11` for refresh plans, edition pins, source decay, deprecation, and supersession conditions.

For an all-in-one DPF publication carrier, assemble the content in a reproducible order. This order is a publication shape, not a new framework kind:

1. Public framework title and package edition ref: use a domain- or practice-specific framework name such as `<DomainOrPractice> Principles Framework`; `Principles Framework` alone is only the head or kind phrase, not an individual framework name. Do not put `local monolith`, `draft`, process status, or file-layout slang in the public title.
2. Dependency declaration: FPF Core edition, depended-on DPF or local-framework editions, and blocked reverse dependency.
3. Table of contents: pattern bodies first as the main language of use; support maps and relation records reachable but not front-loaded as required reading.
4. Readme or first practical entries: intended reader, first use, non-use boundary, first outputs, and a short statement of which selected domain or local structures this carrier exposes for that reader.
5. Preface or framework context: cross-cutting ideas that make the pattern set cohere, plus the selected structure families the carrier foregrounds, deliberately coarsens, defers, or sends back to sources and pattern bodies.
6. Package carrier structure-account: intended reader and use, selected source-structure denominator, recurring problem-situation structures, reusable solution-move structures, captured structure, deliberately coarsened, abstracted, omitted, or lost structure, source-return condition, and quality or epiplexity route. This may be a short subsection in the readme or preface when the carrier is compact.
7. Package boundary and owner routing: Core owners reused, local terms bounded, and source, evidence, assurance, publication, and refresh exits named.
8. Pattern index: pattern ids, titles, first use, and any local prefix discipline.
9. Pattern bodies: each drafted through `E.8`, with recognition text, positive solution, worked cases, local anti-patterns, SoTA-Echoing, conformance checks, and relations, and each evaluated or explicitly marked as a seed under `E.21` before the package is claimed for public, teaching, enterprise, or reliance-bearing use.
10. Heterogeneous acceptance cases or transfer probes: examples that force the pattern set to work across unlike uses rather than only repeating the motivating case.
11. Support maps or appendices: architecture bridge, source-use map, precision map, package-name route, or other reference material placed after pattern bodies unless a short front-door trigger table is needed.
12. Source use and refresh map: source rows with adopted payload, rejected or bounded readings, currentness triggers, and `G.2`/`G.11` return conditions.
13. Pattern-framework relation and edition records: `E.4.PFR` rows for dependency, specialization, publication, source reuse, evaluation, generated-carrier, teaching publication-carrier, ethics, deprecation, or supersession relations.
14. Refresh route: what returns to source, pattern quality, package adequacy, edition dependency, or publication carrier when source, Core edition, local use, telemetry, or evaluation changes.
Every DPF publication or access carrier bears or serves a publication/access expression that makes selected domain or local structures available for a declared reader and use; the carrier is not itself the framework edition, the domain, or a narrative by type. In an all-in-one publication carrier, the readme and preface usually carry the first explanatory route, and sometimes a narrative rendering, through the domain. They must therefore say what they are telling, for whom, which structures they foreground, which structures are deliberately coarsened, abstracted, omitted, or left to source return, and where a reader returns for fuller pattern, source, evidence, or relation detail. This is not only text-to-text summarization: the source-bearing side may be actual or possible holon structure, an architecture description, a view, a source pack, a model, a graph, or a pattern set. In architecture-mediated narrative-rendering use, read the return chain as `narrative rendering carried by a publication or access carrier -> architecture description or view -> architecture as selected structures in context -> wider source structures`. When no narrative rendering is present, read the first step as `framework publication or access carrier -> selected source structures`. Each step has selected structure, captured structure, coarsening, abstraction, omission, loss, and return conditions. An architecture description is often already a coarsened representation of selected real, expected, candidate, or actual structures, so the DPF carrier must not hide that second-step loss. This does not make every DPF a literary narrative or make every carrier a narrative; it makes the publication/access representation relation inspectable. When a sequential narrative rendering is load-bearing, use `A.6.3.NAR`; when the publication expression deliberately keeps only a narrower-use coarsened rendering, use `A.6.3.CSC`; for structure capture and loss, use `C.33`; for same-enough or preservation claims, use `C.34`; for first-entry publication, use `E.11` and `E.17`; for package adequacy, use `E.4.DPF.DA`.

Keep process state out of the carrier. DRR text, handoff notes, ledger rows, review status, helper state, admission blockers, and landing evidence may shape the package, but the publication carrier should contain only durable user-facing package content, source-use boundaries, relation records, quality routes, and refresh conditions. A short source-use or relation record may appear in the user carrier when it helps readers and maintainers use the DPF; a DRR argument, review transcript, or quality proof does not.

For skill packs and MCP-backed access, keep the same framework edition identity and relation records visible. A skill or endpoint may help a user find, select, retrieve, render, or apply DPF patterns, but it is an access carrier until another governing pattern makes a stronger claim. If the carrier generates candidate text, use `C.35`; if it performs work or triggers tools, use `A.15` and the local tool or work owner; if it claims currentness, evidence, assurance, or decision authority, use `G.11`, `A.10`, `B.3`, `E.9`, or the direct owner. Do not read a skill manifest, MCP tool name, endpoint schema, or protocol route as the DPF architecture.

Starter evaluation characteristics for a principle-framework improvement loop:

| Characteristic question | Direct owner to use |
| --- | --- |
| Discoverability | Can the intended reader find the first useful entry and governing pattern? Use `E.11`, then evaluate the pattern or projection through the applicable quality owner. |
| Source fidelity | Are adopted and rejected source payloads recoverable in source packs, solutions, boundaries, and examples? Use `G.2`, `C.33`, `C.34`, and pattern-quality evaluation. |
| Ontology clarity | Are Core, domain, local, publication, source, decision, relation, quality, and refresh claims kept as different kinds? Use `E.10`, `F.18`, `F.19`, and the direct owner. |
| Relation typedness | Are pattern-use, specialization, dependency, publication, preservation, quality, and source-use relations separated? Use `E.4.PFR`. |
| Compatibility impact | Can maintainers see what breaks or must migrate when Core, domain, or local editions change? Use `E.4.PFR`, `E.5.3`, and `G.11`. |
| Refreshability | Are source decay, edition pins, local-use telemetry, and supersession conditions actionable? Use `G.11`. |
| Package navigability | Can the selected pattern set, relation records, source packs, decision records, quality evidence, and first-entry or access carrier be found without treating the package as runtime machinery? Use `G.5`, `E.4.PFR`, and `E.11`. |
| Adoption telemetry | Are repeated reader errors, skipped records, stale sources, and local-use failures routed to refresh or improvement? Use `G.11` and `E.23`. |
| Didactic first use | Can a first-time domain or local author write the first useful output without prior FPF developer knowledge? Use `E.11`, `E.12`, `E.21`, and `E.23`. |

These are evaluation characteristics for selecting and framing improvement work. They are not measurement programs by themselves. If the pass needs a DPF package adequacy result, use `E.4.DPF.DA`; if it needs individual pattern quality, use `E.21`; if it needs DRR adequacy, FPF-level Pillar adequacy, measurement, evidence, or architecture-characteristic evaluation, use the pattern that owns that object, such as `E.9.DA`, `E.2.DA`, `C.16`, `A.10`, or the relevant architecture-characteristic pattern.

The spine is complete only when a reader can answer: what framework edition is being authored, what problem-and-solution architecture it renders, which sources and decisions shaped it, which patterns and relations were selected, where it is published, how quality improves, and when it returns for refresh or repair.

