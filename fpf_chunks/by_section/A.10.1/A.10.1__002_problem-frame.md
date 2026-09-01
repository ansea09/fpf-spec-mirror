---
chunk_kind: "child"
pattern_id: "A.10.1"
pattern_title: "Revalidate Affected Uses When a Relied-on Source Changes"
section_id: "A.10.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10.1/A.10.1__002_problem-frame.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.10.1 — Revalidate Affected Uses When a Relied-on Source Changes"
  - "A.10.1:1 — Problem Frame"
line_start: 23016
line_end: 23042
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.11"
  - "B.3"
  - "C.2.1"
  - "E.15"
  - "G.11"
  - "G.6"
keywords:
---

### A.10.1:1 - Problem Frame

Use this pattern when a claim-bearing source has been revised, replaced, refined, superseded, or challenged and the practical question is not merely whether the source is current, but which existing results or actions actually relied on the changed claim.

The primary `EntityOfConcern` is the bounded source-to-use structure: the changed claim and the exact direct use relations through which receiving results, decisions, specifications, plans, or actions depended on it. The practitioner is not asked to know every receiver in advance. The first move is to state the source comparison and the present decision that bounds where a receiving use would count.

**First useful move.** Write:

> Source episteme `S0` is being compared with later or replacement episteme `S1` for question `Q`. The potentially material claim change is `ΔC`. Uses will be sought only within search frame `F`; the first known coverage limits are `G`.

If no action-relevant claim change is established, stop before opening a multi-use search. A new URL, file, layout, revision label, carrier, or publication occurrence is not by itself a material claim change.

**What goes wrong if missed.** One team replays every analysis because a version changed. Another preserves every result because the represented world did not change. A third follows citations or graph edges and calls every reachable item affected while missing an undeclared receiver that actually used the premise. All three replace actual reliance with a proxy.

**What this buys.** The practitioner gets an affected-use revalidation account that is local, replayable, and honest about coverage. They preserve inspected unaffected uses for their stated conditions, prepare only `depends` branches for application of their direct subject-pattern guidance, record unresolved reliance and inaccessible search surfaces, and stop at the last receiving action that can change.

**Not this pattern when.**

- Use `A.10` when one already-known bounded reliance use is the whole question.
- Use `C.2.1`, `E.17`, or `E.24.PUB` when source identity, edition continuity, publication, carrier, form, audience, or availability is the live question and no several-use revalidation is needed.
- Use `G.11` when currentness, decay, refresh planning, or refresh reporting is the live result.
- Use `E.15` when the changed object is one FPF pattern edition; it retains Delta-Class, predecessor-function continuity, pattern checks, and its own change result.
- Use the direct subject pattern when the source is unchanged and a sensor, market, organization, law-applicability situation, configuration, or other world-side condition changed.
- Do not use A.10.1 to decide truth, evidence sufficiency, causality, choice, assurance, authority, permission, release, planning, or performed Work. Take those questions directly to their governing patterns.

**What changes in practice.** A source change no longer means “redo everything” or “update the link.” The team first establishes whether claim content changed or names the missing fact, states where receivers could count and how that area was searched, confirms reliance in the receiving content, and revalidates only the smallest action-changing branch.

