---
chunk_kind: "child"
pattern_id: "A.10.1"
pattern_title: "Revalidate Affected Uses When a Relied-on Source Changes"
section_id: "A.10.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10.1/A.10.1__002_problem-frame.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "A.10.1 — Revalidate Affected Uses When a Relied-on Source Changes"
  - "A.10.1:1 — Problem Frame"
line_start: 28211
line_end: 28239
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

Use this pattern when a claim-bearing source has been revised, replaced, refined, superseded, or challenged and the practical question is not merely whether the source is current, but which existing results or actions relied on the changed claim.

The primary `EntityOfConcern` is the bounded source-to-use structure: the changed claim and the direct use relations through which receiving results, decisions, specifications, plans, or actions depended on it. The practitioner is not asked to know every receiving use in advance. The first move is to state the source comparison and the question that determines which receiving uses count.

**First useful move.** Compare source episteme `S0` with later or replacement episteme `S1` for the present question `Q`. Identify what changed in the claim or its applicability for `Q`, or state what prevents that comparison.

When relevant meaning, applicability and access remain compatible, a repaired reference can be the completed result. It needs no multi-use search or additional subject-result record. A new URL, file, layout, revision label, carrier, or publication occurrence alone establishes no material claim change. Missing claim content or access leaves a scoped gap rather than establishing unchanged meaning.

When a material change warrants revalidating several uses or finding additional ones, state:

> The material claim change is `ΔC`. Uses count for question `Q` within search frame `F`; the first known coverage limits are `G`.

**What goes wrong if missed.** One team replays every analysis because a version changed. Another preserves every result because the represented world did not change. A third follows citations or graph edges and calls every reachable item affected while missing an undeclared use of the premise. All three replace actual reliance with a proxy.

**What this buys.** The practitioner can finish with a repaired reference, a qualified subject result, or a scoped limit. When a common receiving question needs an affected-use account, it remains local, replayable, and bounded by its coverage. Inspected unaffected uses remain usable for their stated conditions; unresolved reliance and inaccessible surfaces bound the conclusion. Apply the subject rule to uses classified as `depends`. Follow each branch through the last use whose conclusion, conditions, required checks or actions could change.

**Not this pattern when.**

- Use `A.10` when one already-known bounded reliance use is the whole question.
- Use `C.2.1`, `E.17`, or `E.24.PUB` when source identity, edition continuity, publication, carrier, form, audience, or availability is the live question and no revalidation across several uses is needed.
- Use `G.11` when currentness, decay, refresh planning, or refresh reporting is the live result.
- Use `E.15` when the changed object is one FPF pattern edition; it retains Delta-Class, predecessor-function continuity, pattern checks, and its own change result.
- Use the direct subject pattern for a world-side change with no source change; examples include a changed sensor, market, organization, configuration, or situation affecting a law's applicability.
- Use the direct subject pattern for the judgment or action needed after discovering an affected use. Section 4.5 identifies the governing contributions for those questions.

**What changes in practice.** The team compares the claims and identifies any missing evidence. If it needs to find affected uses, it states which uses count, searches for them, and checks reliance in the receiving content. It then applies the relevant subject guidance where the changed claim could alter a conclusion or action. A sufficient direct result closes its receiving question.

