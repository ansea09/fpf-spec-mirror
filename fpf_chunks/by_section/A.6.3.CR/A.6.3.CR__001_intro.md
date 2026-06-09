---
chunk_kind: "child"
pattern_id: "A.6.3.CR"
pattern_title: "ConservativeRetextualization — entityOfConcernRef-preserving textual re-expression"
section_id: "A.6.3.CR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CR/A.6.3.CR__001_intro.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.6.3.CR — ConservativeRetextualization — entityOfConcernRef-preserving textual re-expression"
  - "A.6.3.CR:intro — Intro"
line_start: 10782
line_end: 10824
dependencies:
  - "A.15"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.7"
  - "B.5.2"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
---

## A.6.3.CR - ConservativeRetextualization — entityOfConcernRef-preserving textual re-expression
> **Status:** Stable

**Placement.** Specialization under `A.6.3 U.EpistemicViewing` for entityOfConcernRef-preserving textual re-expression.
**Builds on.** `A.6.3 U.EpistemicViewing`; `A.6.2 U.EffectFreeEpistemicMorphing`; `A.7`; `E.10.D2`; `E.17.0`; `E.17`; `F.9`; `F.18`; `E.10`.
**Coordinates with.** `ExplanationFaithfulnessProfile`; `RepresentationTransduction`; `E.17.ID.CR ComparativeReading`; `A.6.4 U.EpistemicRetargeting`; `B.5.2`; `A.15`.

**One-line summary.** `ConservativeRetextualization` is an entityOfConcernRef-preserving textual re-expression of an episteme that stays inside `A.6.3 U.EpistemicViewing`: it may shorten, reorder, filter, translate, or restate claims, but it does **not** silently change `entityOfConcernRef`, add new claims about that entity, or hide bridge work.
**EntityOfConcern preservation discipline.** In this specialization, entityOfConcernRef-preserving textual re-expression means the C.2.1 `entityOfConcernRef` stays stable; wording changes cannot carry hidden retargeting, bridge, work, evidence, gate, or assurance force.

**Primary EntityOfConcern in plain terms.** One published textual rendering over the same EntityOfConcern; not the whole source corpus, not an explanation face, and not a downstream decision or publication with named authority-reference relation.
**Admissible move in plain terms.** Restate already available content textually while preserving `entityOfConcernRef`, keeping source tether visible, and making loss or omission inspectable.

**Use this when.** Use this pattern when one already available source line about the same EntityOfConcern needs a second textual form such as a report rewrite, summary, translation, or declared filtered restatement, and the real job is still same-entity textual re-expression rather than explanation, representation change, or retargeting.

**Start here when.** Your first honest publication unit is still a text over the same EntityOfConcern, and the main review question is whether omissions, softening, or foregrounding remain conservative and source-tethered.

**What goes wrong if missed.** A summary, translation, or manager-readable rewrite gets treated as harmless editing even after it has started hiding explanation work, bridge work, changed authority relation, or a separate narrower-use card.

**What this buys.** One honest same-entity textual rewrite with visible source tether, visible omission or loss notes, and an explicit handoff when the case stops being only conservative retextualization.

**Working action spine.** Same EntityOfConcern needs a second textual form -> separate source slice, published slice, omission or source-loss note, and admissible use -> use the rewrite for readable restatement, source-finding, review, comparison, or planning preparation -> output one source-slice to published-slice sentence or mini-card -> hand off if coarsened rendering, explanation, representation change, retargeting, work, evidence, gate, release, policy, assurance, adjudication, or bridge use is attempted.

**Ordinary use.** If the rewrite is admissible only for orientation, source-finding, review, comparison, or planning preparation, one source-slice to published-slice sentence or mini-card with the admissible use and visible omission or source-loss note is enough.

**Cheap stop before CSC.** If the rewrite is local, source-visible, non-reliance-bearing, and does not change admissible use, stay in `ConservativeRetextualization` without opening a `Controlled Semantic Coarsening` card.

**Work-planning boundary.** A rewritten method-selection note, work-planning note, or result-measurement note may improve readability and source-finding, but selected-method justification, intended `U.WorkPlan`, actual `U.Work`, and work-result measurement remain governed by `A.15` plus the source `U.Episteme`, source `U.EpistemePublication`, or project-side FPF kind and reference named by value for that work.

**Reliance-facing use.** Open the fuller rewrite-admissibility record only when the rewritten text will be externally relied on, disputed, cited as a source-relation reason, used across context, or read as release/gate/work preparation, engineering justification, approval, or evidence justification.

**Multi-source boundary.** A textual rendering over several source slices stays in this pattern only when every receiving claim can be recovered from either one already available entityOfConcernRef-preserving source line or declared entityOfConcernRef-preserving correspondence witness. The rewrite may align wording, shorten, translate, filter, or foreground with visible loss notes; it may not add comparative claims, hypotheses, rankings, recommendations, bridge/substitution licence, causal linkage, or a new connective theory. Those claims leave `ConservativeRetextualization` for `E.17.ID.CR`, `B.5.2` or an abductive prompt, `A.6.4`, `F.9` or `F.9.1`, or `A.6.3.CSC` as applicable.

**Stop condition.** Stop once the rewrite changes no next interpretation, review, comparison, source-finding, or planning-preparation move and blocks no concrete overclaim about source relation, omission, work, gate, approval, or evidence.

**Admissible-use examples.**

| Admissible project-side use | Source-finding or reversible probe | Non-admissible downstream use |
| --- | --- | --- |
| A summary or translation restates the same source claim with visible source slice, published slice, and omission/loss note. | A generated or manager-readable summary helps the team find/check the source before relying on an approval, evidence, gate, work, or engineering-justification claim. | A summary silently adds modality, reliability, approval, evidence, gate admissibility, or work authority that the source slice does not carry. |

**Not this pattern when.** Not this pattern when the case is primarily explanatory rendering (`ExplanationFaithfulnessProfile`), representation-scheme change (`RepresentationTransduction`), changed EntityOfConcern (`A.6.4`), or a deliberately coarsened rendering whose narrower admissible use, non-admissible downstream use, and source-bearing reopen card has become primary. In that last case, use `A.6.3.CSC Controlled Semantic Coarsening` instead of resolving it as ordinary `ConservativeRetextualization`.

