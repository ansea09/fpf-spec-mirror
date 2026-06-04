---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__003_problem.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:2 — Problem"
line_start: 57276
line_end: 57292
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
keywords:
---

### E.9.DA:2 - Problem

`E.9` defines the kind and content obligations of a `DRR`, but it is not itself a stop rule for improving one concrete `DRR`. In practice, weak `DRR`s often pass a shape check and still fail for the declared authoring use.

Recurring failures:

1. **Decision summarization.** The record describes source material but does not select what FPF should say.
2. **Disposition gaps.** Selected, rejected, inherited, and outside-decision alternatives are not closed by value.
3. **Neighbour drift.** Related patterns are mentioned but not assigned exact amendment, non-amendment, or receiving-locus obligations.
4. **Drafting inactionability.** Pattern authors cannot tell which sections, names, examples, checks, or relations to write.
5. **Lexical under-typing.** Words such as `basis`, `support`, `quality`, `architecture`, `profile`, `source`, `view`, `decision`, `adequacy`, or `readiness` carry load without recovered kind, relation, or admissible use.
6. **Scope fog.** The `DRR` leaves one content decision partly unmade while implying that pattern drafting may settle it.
7. **Source theatre.** Sources, reviews, audits, standards, benchmarks, or SoTA references are listed but do not change the selected answer, boundary, example, validation obligation, or reopen condition.
8. **Pattern-quality confusion.** Authors try to evaluate the `DRR` as if it were an `E.21` pattern-quality object under evaluation, or treat a passed `E.19` pattern review as proof that the upstream `DRR` was adequate.
9. **Architecture-by-addressing.** The `DRR` names exact receiving loci, but does not judge whether the selected FPF content architecture is adequate: existing pattern vs new pattern, split vs merge, pattern body vs selected non-pattern FPF kind-reference pair, or neighbour-governed vs local content.
10. **Hidden source loss.** The `DRR` compresses, extracts, summarizes, clusters, diagrams, graphs, or dashboard-renders source material without saying which distinctions were preserved, lost, non-admissible for downstream use, or recoverable only by returning to the fuller source.

