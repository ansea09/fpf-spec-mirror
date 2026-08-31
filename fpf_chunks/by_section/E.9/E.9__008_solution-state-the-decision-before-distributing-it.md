---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design‑Rationale Record (DRR) Method"
section_id: "E.9:4"
section_title: "Solution — state the decision before distributing it"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__008_solution-state-the-decision-before-distributing-it.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "E.9 — Design‑Rationale Record (DRR) Method"
  - "E.9:4 — Solution — state the decision before distributing it"
line_start: 73783
line_end: 73949
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.6.1"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.19"
  - "E.2"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.5.4"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.10"
  - "F.19"
  - "G.11"
  - "G.6"
keywords:
---

### E.9:4 - Solution — state the decision before distributing it

Write the `Decision` account first in ordinary precise language. Before a reader meets a DRR identity schema, method/work account, or catalogue of alternatives, they must be able to recover, in this order:

1. the working FPF problem and why it matters now;
2. the selected answer stated positively;
3. what changes in practitioner or authoring use;
4. the selected loci and the positive obligation each one carries;
5. the first substantive drafting action; and
6. the nearest boundary, honest blocker, or reopen condition.

That short account is the primary authoring source. Add exact method, work, application, episteme-identity, source-use, assessment, or authority distinctions only when the decision or a named later reliance depends on them.

A nontrivial DRR keeps four conceptual components recoverable. These are the minimum decision kernel; the lightweight editorial variant remains available under `CC-DRR.5`.

| Minimum-kernel component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Working problem, trigger, intended FPF use-value, scenario, or external change. |
| **Decision** | *What will we do?* | Selected answer, positive content distribution, practical change, first drafting action, and nearest boundary. |
| **Rationale** | *Why this answer?* | The material comparison, load-bearing Pillar or taxonomy-lens effects, architecture/usability/SoTA grounds, and uncertainty that could change the answer. |
| **Consequences** | *What follows?* | Benefits, trade-offs, affected loci and true direct consumers, practical gains/costs, validation obligation, and reopen condition. |

In this pattern, a **bounded coordinated change set** is one bounded group of mutually dependent content-decision questions whose enduring FPF expression is distributed across several patterns or selected non-pattern FPF kind-reference pairs.

The **selected answer** is what FPF should say, which selected loci carry it, what practical action changes, what stays outside, and which source-use, evidence, validation, or loss/recoverability conditions remain live.

A **selected non-pattern FPF kind-reference pair** is a content-distribution instruction, not a new kind. It names an admitted FPF kind and one exact reference by value—for example a `U.View`, source map, source-use note, evidence-path record, review-finding record, or architecture-decision record.

A **temporary convergence record** holds the selected answer while several selected carriers are still being updated. It is not a second permanent Core-law section or a process-state container.

Keep a rejected alternative only when it explains the selected answer, a live boundary, or a reopen condition. Pillars and taxonomy lenses may inform the decision, but the DRR records their load-bearing effects rather than rehearsing every lens or preserving the history of discussion.

Before selecting a broad language, ontology, or authoring rule for fanout, apply it to at least one dependency-aware actual predecessor/proposed host pair. At comparable effort, compare the recognizable entry, required inputs, first action, practitioner vocabulary, formality and assurance burden, first useful result, stop or return, preserved useful ideas, and true direct consumers. Proposed pattern wording must pass the E.8 first screen and the `F.19` kind-preserving plain-rewrite test. A schema, invented fact pack, unrelated lane test, checklist, or promised later review cannot substitute for this replay. If the pilot degrades use without a compensating semantic gain, repair or reject the rule before fanout.

A DRR records the selected answer; the record does not decide, authorize, perform drafting, or realize Core content. When exact identity or reliance makes the distinction material, separately identify the decision work and method, selected-answer result, C.2.1 DRR episteme, source-use relations, assessment and result, any acceptance or authority, and later realization work. An exact DRR episteme then follows C.2.1 identity by `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>`; ordinary use does not require materializing that whole account.

#### E.9:4.1 - Minimum decision-inspection content blocks

A conforming DRR must also make the following decision-inspection content blocks
recoverable. They may appear inside the four kernel components or inside one
dedicated `Decision grounds used` or decision-inspection block, but they are part of
substantive DRR adequacy rather than later review-only hardening.

| Decision-inspection content block | What must be recoverable by value | Usual location in the DRR |
|---|---|---|
| **Exact decision grounds and governing inheritance** | Exact source documents, accepted architecture records, accepted audit records, and inherited decisions that materially govern the decision, plus any remaining uncertainty not already closed by those grounds. | Header or `Decision grounds used`, with the Problem frame or Rationale carrying the decision-relevant source use. |
| **Purpose, utility, and scenario grounding** | Intended FPF use-value, first-minute working situation, minimum scenario/anti-case grounding, and compact utility/fitness reading. | Problem frame. |
| **Decision-relevant alternatives and current disposition** | The alternatives needed to explain the selected answer, a live boundary, or a reopen condition, with their current disposition. Discussion history and harmless options stay outside the current DRR; retain them in a separate historical source only when a named later use needs that history. | Decision and Rationale. |
| **Content-distribution and outside-boundary map** | For each load-bearing selected answer: the positive content obligation each selected pattern or selected non-pattern FPF kind-reference pair must carry, the first subject kind and action guidance expected in drafting when a pattern is selected, which decision-relevant related patterns or selected non-pattern FPF kind-reference pairs stay unamended under the current decision, and any agreement across selected patterns and selected non-pattern FPF kind-reference pairs that those selected patterns and selected non-pattern FPF kind-reference pairs must preserve. Outside-boundary and non-obligation material is secondary distribution control; it must be normalized, compact, and not pasteable as copied negative doctrine or precision-restoration debt for the selected pattern Solution. Ordinary `use/apply this pattern` wording remains valid action-guiding shorthand. In the distribution map, state the concrete claim, relation, boundary, or practitioner action that would change. Repeated content families, ordinary references, README/ToC/E.11/I.2 navigation, package-boundary rationale, split/defer rationale, architecture placement reasoning, and phrase-level boilerplate around simple claims stay in DRR, architecture documents, handoff, relation rows, README, ToC, `E.11`, `I.2`, or one compact local locus instead of the Solution. When proposed wording still needs precision restoration, the DRR names the selected restoration or governing pattern: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or another governing pattern. Named related patterns or selected non-pattern FPF kind-reference pairs must be classified now, not left as tentative `most likely` / `may need` / `if later touched` watch prose. | Decision. |
| **Existing-pattern sufficiency and new-pattern necessity** | For each load-bearing selected answer, whether one already-existing pattern is sufficient, one already-existing selected non-pattern FPF kind-reference pair is sufficient, or one newly selected pattern or selected non-pattern FPF kind-reference pair is necessary, and why rejected options would misplace, overload, or falsely split the pattern or selected non-pattern FPF kind-reference pair that governs the selected answer. | Decision and Rationale. |
| **Naming, ontology, and wrong-carrier-confusion account** | Head/branch/object/move/outside-work separation, tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment, and any load-bearing `F.18` naming obligation needed to keep the selected answer truthful by value. | Problem frame, Decision, and Rationale. |
| **Reusable content-disposition when triggered** | Whether a potentially reusable selected non-pattern FPF kind-reference pair remains local, is generalized now, is rejected, or is placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Decision and Rationale. |
| **Loss and recoverability template when source-loss or scope narrowing is declared** | Preserved distinctions, dropped distinctions, admissible use, non-admissible downstream use, recoverability class, and reopen/stop rule. | Decision and Consequences. |
| **Selected locus and related-pattern boundary account** | Why the selected patterns and selected non-pattern FPF kind-reference pairs carry the content, which tempting patterns or selected non-pattern FPF kind-reference pairs stay outside, and which governing patterns govern specific outside claims, relations, or boundaries. | Decision and Rationale. |
| **Convergence and overlap account when several content-decision branches touch the same carrier set** | Whether overlap is valid convergence or one reopened architecture smell, what agreement across selected patterns and selected non-pattern FPF kind-reference pairs must hold, and whether a new pattern or selected non-pattern FPF kind-reference pair is actually selected or refused now. | Decision and Consequences. |
| **Selected-answer stability boundary** | Which elements of the selected answer are fixed now for later FPF drafting, and which later elaborations may strengthen wording, examples, source-use rows, or validation evidence without reopening the selected answer. | Decision and Consequences. |
| **Impact, practical gains, and remaining validation evidence obligation** | Affected patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, authority or release consequences when they follow from the content decision, and the remaining validation evidence obligation that still constrains later authoring or landing. | Consequences. |
| **SoTA and competitive-positioning account when load-bearing** | Current best-known problem-solving source anchors and source-derived moves under E.8 that discipline the decision, what problem-owning domain or practice they answer to, which official, popular, or legacy alternatives they reject or bound when relevant, and what unresolved uncertainty would materially change the selected answer. | Problem frame, Rationale, and Consequences. |
| **Actual-host predecessor/proposed replay when a broad authoring rule is selected** | One dependency-aware real host comparison at comparable effort: recognizable entry, inputs, first action, vocabulary, formality and assurance burden, first useful result, stop or return, preserved useful ideas, and true direct consumers. The proposed wording passes E.8 and F.19; a proxy or promised later review does not substitute. | Decision and Rationale, with the selected rule and pilot effect carried into the locus obligations. |
| **Campaign problem-solution unfolding carry-through when triggered** | For campaigns changing README entries, path-shaped patterns, pattern families, DPF entries, or first-practical routes: the map from admitted problem-side record refs or cues, accepted starting records, current starting structures, and entry cues to selected solution architecture, affected unfolding families, loci added or changed, governing-pattern map, blocked overreads, and what must not remain only in DRR or README. | Decision, selected-locus map, and Consequences. |
These decision-inspection content blocks are not separate process paperwork. A DRR that keeps
only the four labels while leaving decision grounds, first-minute use question, naming,
selected content distribution, pattern or selected non-pattern FPF kind-reference pair sufficiency or necessity, overlap handling, impact,
or unresolved uncertainty implicit is structurally labeled but still
substantively immature.

Together these decision-inspection content blocks let the DRR act as one decision record
for one bounded coordinated change set: enough semantic closure that later
drafting distributes the selected answer into selected patterns and selected non-pattern FPF kind-reference pairs rather than
inventing it for the first time pattern by pattern.

When one bounded decision coordinates several patterns or selected non-pattern FPF kind-reference pairs, or one cluster of mutually dependent pattern edits and selected non-pattern FPF kind-reference pair edits, the DRR **MAY**
carry additional substantive sections beyond that minimum kernel. Typical substantive additions include obligations on selected patterns and selected non-pattern FPF kind-reference pairs, one explicit
new-pattern vs existing-pattern decision, one impact or non-goal map across selected patterns and selected non-pattern FPF kind-reference pairs, coverage or agreement maps across selected patterns and selected non-pattern FPF kind-reference pairs, convergence
classification, and one provisional decision-law account by value that
keeps the bounded change account semantically complete until enduring
Core text is distributed.

Such additions do not change the DRR’s kind. A DRR carrying them remains
conforming only when it stays about the FPF content decision: what FPF should
say, why, what is excluded, how selected patterns and selected non-pattern FPF kind-reference pairs are
affected, and what practical use or authoring action improves. A DRR carrying richer
convergence content **MUST NOT** become a campaign plan, process script,
baton carrier, packet checklist, staging log, or other development-process
brief.

When one selected answer could plausibly fit an existing pattern or selected non-pattern kind-reference pair, or require a new one, the selected-answer decision result recorded in the DRR must state that sufficiency/necessity disposition by value. A tentative carrier list is not a decision result; later drafting must not be asked to invent the selected locus.
When the accepted decision grounds or the DRR itself already names one pattern or
selected non-pattern FPF kind-reference pair as part of the distribution question, that
pattern or selected non-pattern FPF kind-reference pair is not a neutral future watch item. The DRR
must classify it now either as one selected pattern or selected non-pattern FPF kind-reference pair
with explicit obligation, one explicit boundary neighbor kept unchanged,
one inherited-unchanged neighbor, or one outside-current-decision item
with named pattern, selected non-pattern FPF kind-reference pair, or decision record. Conditional or
time-relative pattern prose or prose for one selected non-pattern FPF kind-reference pair such as `most likely`, `may need local
hardening`, `if later touched`, `watch later`, or one equivalent
placeholder is non-conforming there because it marks one unmade current
decision rather than one explicit current disposition.

When decision grounds expose a potentially reusable non-pattern carrier or neighboring source-use, evidence, assurance, validation, or architecture-decision mechanism, the selected-answer result must classify it as generalized now, kept local with reason, rejected, or outside the decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record. The DRR records that disposition; mere mention of an existing artifact is not the deciding work or result.
When one selected answer involves source-loss mode, simplification, redaction,
summarization, or other declared loss, the DRR must make the admissible-use template explicit by value. Explanation alone is not enough; the decision
must say what remains preserved, what is dropped, which branch reading is admissible and which selected non-pattern FPF kind-reference pair carries it, which uses lack an admissible carrier or evidence path, what recoverability class
applies, and what reopen or stop rule governs cases that exceed the
declared source-loss or scope-narrowing state.

A nontrivial DRR is mature enough for downstream authoring only when
material selected-answer branch choices about the EntityOfConcern, selected patterns and selected non-pattern FPF kind-reference pairs, outside-current-decision boundary, reusable-content disposition,
and loss/recoverability regime have already been selected, rejected,
inherited unchanged, or placed outside the current decision with a named pattern, selected non-pattern FPF kind-reference pair, or decision record. If those choices are still missing, the DRR is still decision-grounding work
rather than one accepted design-rationale record.

The DRR episteme lives **outside** normative Core. A separately governed acceptance, authority, or realization decision may rely on it, but the word *accepted*, a record status, review mark, or publication does not make its claims true or authorize change.

When the selected answer is separately authorized for realization, dated authoring work applies it to the selected patterns or selected non-pattern Core kind-reference pairs. The changed Core content, authoring work, result claims, checks, witnesses, publications, and any landing or release record remain distinct; apply the relevant pattern to each claim. The DRR remains external provenance and temporary convergence support; it must not remain the sole carrier of enduring semantics after those semantics are realized in Core.

Authors using a separately accepted selected answer may elaborate examples, SoTA-Echoing, recognition sections, local wording, and neighboring fit inside its declared stability boundary. A change to the selected answer, selected loci, outside boundary, reusable-content disposition, or loss/recoverability regime requires a successor decision result and DRR episteme rather than a silent edit to downstream prose.

Improvement work may apply E.23 to a DRR episteme. That work, its method applications, quality-result claims, and witnesses are separate from the DRR and do not turn the record into a pattern draft. When SoTA is load-bearing, the successor decision result must show what changed in the selected answer, locus obligation, boundary, example, validation obligation, or reopen condition; otherwise the source use remains rationale-only or lineage-only.
When a campaign creates or modifies route-shaped, unfolding-shaped, first-entry, DPF, or multi-pattern path material, add a compact `CampaignProblemSolutionUnfoldingCheck`:

```text
CampaignProblemSolutionUnfoldingCheck:
  campaignProblem:
  acceptedProblemSideRecordRefsOrCues:
  selectedSolutionArchitecture:
  affectedReadmeEntries:
  affectedUnfoldingFamilies:
  acceptedStartingRecordRefs[]:
  acceptedStartingStructureRefs[]:
  entryCueRefs[]:
  nextUseOrResultMap:
  unfoldingLociAddedOrChanged:
  governingPatternMapAddedOrChanged:
  patternPlacements:
  whatStayedOnlyInDRRAndMustMoveToPatternOrUnfoldingStructure:
  whatStayedOnlyInReadmeAndMustMoveToPatternOrUnfoldingStructure:
  blockedOverreads:
  rejectedUnfoldingAlternatives:
  unfoldingCarryThroughResidueAfterContentUpdate:
  refreshOrReopenTrigger:
```

The critical field is `whatStayedOnlyInDRRAndMustMoveToPatternOrUnfoldingStructure`. If it remains nonempty after host drafting, the selected answer has not been fully realized. The next authoring work moves the surviving content into the selected pattern body, unfolding block, README seed, E.11 expansion, or concrete relation locus; adding another record paragraph is not realization.

To preserve **P-2 Didactic Primacy** without duplicating meta-text, realization work using a separately accepted selected answer should distill stable Rationale, Consequences, SoTA-Echoing, Grounding, and other valid convergence content into the selected informative pattern loci under E.8. The DRR episteme remains external provenance; it is not itself landed or transformed into Core.
A substantive DRR is one claim-bearing episteme about one bounded current content-decision question/change set. It may carry selected obligations only in its Decision or Consequences, but no route, gate, handoff, packet, monolith, mutable status, or future-campaign state. Any undecided remainder is explicitly outside the decision with a named pattern, kind-reference pair, or successor decision record.

#### E.9:4.1a - Process-source method admission into FPF

When a DRR considers a stable method described in a process source, it decides the FPF-admission disposition by value. The DRR records that decision and any source-use relation that matters; neither the source passage nor the record performs admission or becomes a second canon.

The DRR names:

- the process-source passage or accepted source named by value process-source decision-ground item being considered;
- the reusable FPF method recovered from that passage;
- the current FPF pattern, section, or accepted `DRR` that already carries the method, if any;
- the remaining delta that current FPF does not yet carry;
- the selected FPF pattern chosen to carry that delta;
- process-control material excluded from FPF pattern prose, such as task dispatch, seam state, helper behavior, Git recovery, packet transport, review transport, chat cadence, and mutable release state;
- the source-use result for that passage or decision-ground item: quote named by value, narrowed scope, instantiated case, decision-bearing use, draft-guidance source, example-only use, or retired source use;
- any meaning loss or addition created by that source-use result: changed scope, relation, evidence path, admissible use, non-admissible use, reader use, or recoverability condition;
- the first improved FPF use that the admitted method gives to an author, reviewer, or downstream FPF user;
- the current disposition: selected now, inherited sufficient, rejected now, or outside the current decision with the named evaluation pattern, accepted `DRR`, or accepted decision-ground item named by value.

Reusable process-source method is not limited to semio wording or pattern-authoring language. It may enter FPF only when it is separable from local process mechanics, improves FPF use, and has one exact evaluation pattern. After the method lands in FPF, process documents should cite the selected FPF pattern instead of keeping a parallel long-form rule.

