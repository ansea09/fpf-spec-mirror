---
chunk_kind: "child"
pattern_id: "E.9"
pattern_title: "Design-Rationale Record (DRR) for FPF Content Decisions"
section_id: "E.9:4"
section_title: "Solution — state the decision before distributing it"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9/E.9__006_solution-state-the-decision-before-distributing-it.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.9 — Design-Rationale Record (DRR) for FPF Content Decisions"
  - "E.9:4 — Solution — state the decision before distributing it"
line_start: 103740
line_end: 103890
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

Present the `Decision` account first in plain, precise language. Before a reader meets a DRR identity schema, a Method or Work account, or a catalogue of alternatives, they must be able to recover, in this order:

1. the working FPF problem and why it matters now;
2. the selected answer stated positively;
3. what changes in practitioner or authoring use;
4. the selected loci and the positive obligation each one carries;
5. the first substantive drafting action; and
6. the nearest boundary, blocker, or reopen condition.

If the answer is unsettled, develop it through a working expression under §4.2. The order above is for readers of the resulting decision; inquiry can start with an open question.

Once supported, the short decision account is the primary source for drafting. Add exact Method, Work, application, episteme identity, source use, assessment, or authority only when the decision or a named later reliance depends on that distinction.

A nontrivial DRR must make the four components below recoverable. They form the minimum decision kernel. `CC-DRR.5` gives the lightweight editorial variant.

| Minimum-kernel component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Working problem, trigger, intended FPF use-value, scenario, or external change. |
| **Decision** | *What will we do?* | Selected answer, positive content distribution, practical change, first drafting action, and nearest boundary. |
| **Rationale** | *Why this answer?* | The material comparison, load-bearing Pillar or taxonomy-lens effects, architecture/usability/SoTA grounds, and uncertainty that could change the answer. |
| **Consequences** | *What follows?* | Benefits, trade-offs, affected loci and direct consumers, practical gains/costs, validation obligation, and reopen condition. |

In this pattern, a **bounded coordinated change set** brings together mutually dependent content-decision questions within one decision boundary. Several patterns or selected non-pattern FPF kind-reference pairs carry the enduring FPF expression of that decision.

The **selected answer** is what FPF should say, which selected loci carry it, what practical action changes, what stays outside, and which source-use, evidence, validation, or loss/recoverability conditions remain live.

A **selected non-pattern FPF kind-reference pair** is a content-distribution instruction, not a new kind. It names an admitted FPF kind and one exact reference by value—for example a `U.View`, source map, source-use note, evidence-path record, review-finding record, or architecture-decision record. The selected patterns and such non-pattern items are the **selected loci** of the decision.

A **temporary convergence record** holds the selected answer while authors update several selected loci. Enduring normative rules belong in Core, and process state belongs outside the DRR.

Keep a rejected alternative only when it explains the selected answer, a live boundary, or a reopen condition. Pillars and taxonomy lenses may inform the decision, but the DRR records their load-bearing effects rather than rehearsing every lens or preserving the history of discussion.

Before adopting a language, ontology, or authoring rule for wider use, apply it to at least one real host and its proposed replacement, including their dependencies. At comparable effort, compare the recognizable entry, required inputs, first action, practitioner vocabulary, formality and assurance burden, first useful result, stop or return, preserved useful ideas, and direct consumers.

The proposed wording must pass the E.8 first screen and the `F.19` kind-preserving plain-rewrite test. A schema, invented fact pack, unrelated lane test, checklist, or promised review cannot replace this comparison. If the pilot makes the host harder to use without a compensating semantic gain, repair or reject the rule before applying it elsewhere.

A DRR records the selected answer. When exact identity or reliance makes the distinction material, separately identify the decision work and method, selected-answer result, C.2.1 DRR episteme, source-use relations, assessment and result, any acceptance or authority, and later realization work. An exact DRR episteme then follows C.2.1 identity by `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>`; ordinary use does not require materializing that whole account.

#### E.9:4.1 - Minimum decision-inspection content blocks

A nontrivial DRR must also make the following parts of the decision available for inspection. Authors may present them within the four kernel components or in a dedicated `Decision grounds used` or decision-inspection block. They are part of an adequate decision before it reaches a later review.

| Decision-inspection content block | What must be recoverable by value | Usual location in the DRR |
|---|---|---|
| **Exact decision grounds and governing inheritance** | The exact source documents, accepted architecture and audit records, and inherited decisions that govern this choice, plus any uncertainty those grounds leave open. | Header or `Decision grounds used`, with the Problem frame or Rationale carrying the decision-relevant source use. |
| **Purpose, utility, and scenario grounding** | Intended FPF use-value, first-minute working situation, minimum scenario/anti-case grounding, and compact utility/fitness reading. | Problem frame. |
| **Decision-relevant alternatives and current disposition** | The alternatives needed to explain the selected answer, a live boundary, or a reopen condition, with their current disposition. Discussion history and harmless options stay outside the current DRR; retain them in a separate historical source only when a named later use needs that history. | Decision and Rationale. |
| **Content-distribution and outside-boundary map** | For each consequential part of the answer, state what each selected locus must say, which related loci stay unchanged and what must agree across them. For a selected pattern, name the first subject kind and the action to explain. Use a consistent, compact account of exclusions and non-obligations to guide distribution. Do not paste it into the pattern Solution as negative doctrine or leave its distinctions for a later wording repair. Ordinary `use/apply this pattern` remains valid shorthand. In the distribution map, state the concrete claim, relation, boundary, or practitioner action that would change. Repeated content-family and reference catalogues, README/ToC/E.11 navigation, current development's package-boundary, split/defer, and architecture-placement correspondence, and phrase-level boilerplate around simple claims stay in DRR, architecture documents, handoff, relation rows, README, ToC, `E.11`, or one compact local locus instead of the Solution. Publish use-changing architectural reasons under `E.8:4.2.3`. When proposed wording still needs precision restoration, name the pattern that supplies it: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or another governing pattern. Classify each named related locus now. Phrases such as `most likely` / `may need` / `if later touched` leave its disposition undecided. | Decision. |
| **Existing-pattern sufficiency and new-pattern necessity** | For each load-bearing selected answer, whether an existing pattern suffices, an existing non-pattern FPF kind-reference pair suffices, or a new locus is needed. Explain why the rejected options would put the content in the wrong place, overload its governing locus, or split it unnecessarily. | Decision and Rationale. |
| **Naming, ontology, and wrong-carrier-confusion account** | Head/branch/object/move/outside-work separation, tempting wrong-pattern assignment or wrong non-pattern FPF kind-reference assignment, and any load-bearing `F.18` naming obligation needed to keep the selected answer truthful by value. | Problem frame, Decision, and Rationale. |
| **Reusable content-disposition when triggered** | Whether a potentially reusable selected non-pattern FPF kind-reference pair remains local, is generalized now, is rejected, or is placed outside the current decision with named pattern, selected non-pattern FPF kind-reference pair, or decision record. | Decision and Rationale. |
| **Loss and recoverability template when source-loss or scope narrowing is declared** | Preserved distinctions, dropped distinctions, admissible use, non-admissible downstream use, recoverability class, and reopen/stop rule. | Decision and Consequences. |
| **Selected locus and related-pattern boundary account** | Why the selected loci carry the content, which tempting selected loci stay outside, and which patterns govern the claims, relations, or boundaries left outside. | Decision and Rationale. |
| **Convergence and overlap account when several content-decision branches touch the same carrier set** | Whether overlap is valid convergence or an architecture problem requiring reconsideration, what agreement across selected loci must hold, and whether the decision selects or refuses a new pattern or selected non-pattern FPF kind-reference pair. | Decision and Consequences. |
| **Selected-answer stability boundary** | Which elements of the selected answer are fixed now for later FPF drafting, and which later elaborations may strengthen wording, examples, source-use rows, or validation evidence without reopening the selected answer. | Decision and Consequences. |
| **Impact, practical gains, and remaining validation evidence obligation** | Affected patterns and selected non-pattern FPF kind-reference pairs, practical gains/costs, authority or release consequences when they follow from the content decision, and the remaining validation evidence obligation that constrains later authoring or landing. | Consequences. |
| **SoTA and competitive-positioning account when load-bearing** | Current best-known problem-solving source anchors and source-derived moves under E.8 that discipline the decision, what problem-owning domain or practice they answer to, which official, popular, or legacy alternatives they reject or bound when relevant, and what unresolved uncertainty would materially change the selected answer. | Problem frame, Rationale, and Consequences. |
| **Actual-host predecessor/proposed replay when a broad authoring rule is selected** | One dependency-aware real host comparison at comparable effort: recognizable entry, inputs, first action, vocabulary, formality and assurance burden, first useful result, stop or return, preserved useful ideas, and direct consumers. The proposed wording passes E.8 and F.19; a proxy or promised later review does not substitute. | Decision and Rationale, with the selected rule and pilot effect carried into the locus obligations. |
| **Campaign problem-solution unfolding carry-through when triggered** | For campaigns changing README entries, path-shaped patterns, pattern families, DPF entries, or first-practical routes: the map from admitted problem-side record refs or cues, accepted starting records, current starting structures, and entry cues to selected solution architecture, affected unfolding families, loci added or changed, governing-pattern map, content assigned from DRR or README into patterns or unfolding structures, and any independently grounded overread that a plausible intended reader could make. | Decision, selected-locus map, and Consequences. |

These blocks supply the content of the decision. Four headings cannot tell a later author the grounds, first-minute working situation, naming choice, distribution, sufficiency or necessity of a pattern or non-pattern FPF kind-reference pair, treatment of overlap, impact, or remaining uncertainty. Make those answers recoverable in the DRR without creating separate process paperwork.

For a coordinated change, settle the common answer in the DRR before drafting. Each author can then express that answer at the selected locus without having to decide it again.

When a decision connects several selected loci or mutually dependent edits to patterns and non-pattern FPF kind-reference pairs, its DRR **MAY** include more than the minimum kernel. It can state obligations at each locus, the choice between a new and an existing pattern, how impacts or non-goals map across the selected loci, coverage or agreement across them, and whether overlapping changes converge. A provisional account of the decision rule can hold the full bounded answer until its enduring content is distributed in Core.

These additions leave the DRR's kind unchanged. It conforms only while it records what FPF should say and why, what is excluded, how the selected loci are affected, and what improves in practice or authoring. A record with richer coordination content **MUST NOT** become a campaign plan, process script, baton carrier, packet checklist, staging log, or other development-process brief.

If an existing pattern or selected non-pattern kind-reference pair might suffice, or a new locus might be needed, the DRR must settle that choice. A tentative list leaves the choice to the next author.

Classify each pattern or non-pattern kind-reference pair that the accepted grounds or the DRR bring into the distribution question. State its obligation if selected. Otherwise identify it as an unchanged boundary neighbour, inherited unchanged, or outside the current decision with a named pattern, kind-reference pair, or decision record. Saying it `may need local hardening` leaves that choice open.

If the grounds reveal a potentially reusable non-pattern carrier or a related source-use, evidence, assurance, validation, or architecture-decision mechanism, the decision must classify it as generalized now, kept local with a reason, rejected, or outside with a named locus or decision record. The DRR records the choice; mentioning an artifact does not decide its use.

For source loss, simplification, redaction, summarization, or other declared loss, the DRR must state which distinctions survive and which are lost. Identify each admissible branch reading and its selected non-pattern FPF kind-reference pair, the uses without an admissible carrier or evidence path, the recoverability class, and the stop or reopen rule when the use exceeds the declared loss or narrower scope.

Before another author can use a nontrivial DRR to draft the selected changes, it must settle the material choices about its EntityOfConcern, selected loci, outside boundary, reusable content, and loss or recoverability regime. Each is selected, rejected, inherited unchanged, or placed outside with a named locus or decision record. While any of these choices is missing, the work is still establishing the decision grounds; it has not produced an accepted DRR.

The DRR episteme lives **outside** normative Core. A separately governed acceptance, authority, or realization decision may rely on it, but the word *accepted*, a record status, review mark, or publication does not make its claims true or authorize change.

Once realization is separately authorized, authors apply the selected answer to its loci in dated authoring work. The changed Core content, authoring work, result claims, checks, witnesses, publications, and any landing or release record remain distinct; apply the relevant pattern to each claim. The DRR remains external provenance and temporary convergence support; after realization, the enduring semantics must be available in Core.

Authors using a separately accepted selected answer may elaborate examples, SoTA-Echoing, recognition sections, local wording, and neighboring fit inside its declared stability boundary. A change to the selected answer, selected loci, outside boundary, reusable-content disposition, or loss/recoverability regime requires a successor decision result and DRR episteme rather than a silent edit to downstream prose.

Improvement work may apply E.23 to a DRR episteme. That work, its method applications, quality-result claims, and witnesses are separate from the DRR and do not turn the record into a pattern draft. When a successor decision relies on SoTA, its result must show what changed in the selected answer, locus obligation, boundary, example, validation obligation, or reopen condition; otherwise the source use remains rationale-only or lineage-only.

When a campaign changes route-shaped, unfolding-shaped, first-entry, DPF or multi-pattern path material, make the connection from its actual starting situation to the selected solution and next use recoverable. The following optional form can carry those contents; include only fields that describe the current decision:

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
  blockedOverreads?: [only exact readings admitted by `F.19`'s grounded-contribution test]
  rejectedUnfoldingAlternatives?: <only those needed to explain the selected answer, boundary, or reopen condition>
  unfoldingCarryThroughResidueAfterContentUpdate:
  refreshOrReopenTrigger:
```

After host drafting, identify any enduring selected content that remains available only in the DRR. Move it into the selected pattern body, unfolding block, README seed, E.11 expansion or concrete relation locus so that the public reader can obtain and use the solution.

To preserve **P-2 Didactic Primacy** without duplicating meta-text, realization work using a separately accepted selected answer should distill stable Rationale, Consequences, SoTA-Echoing, Grounding, and other valid convergence content into the selected informative pattern loci under E.8. The DRR episteme remains external provenance; it is not itself landed or transformed into Core.

A substantive DRR is one claim-bearing episteme about one bounded current content-decision question/change set. It may carry selected obligations only in its Decision or Consequences, but no route, gate, handoff, packet, monolith, mutable status, or future-campaign state. Any undecided remainder is explicitly outside the decision with a named pattern, kind-reference pair, or successor decision record.

#### E.9:4.1a - Process-source method admission into FPF

When an author considers a stable method described in a process source, the author decides the FPF-admission disposition by value. The DRR records that decision and any source-use relation that matters; neither the source passage nor the record becomes a second canon.

Record the following when deciding whether to admit the method:

- the content of the passage or accepted decision ground being considered from the process source;
- the reusable FPF method recovered from that passage;
- the current FPF pattern, section, or accepted `DRR` that already carries the method, if any;
- the contribution still missing from FPF;
- the FPF pattern selected to carry that contribution;
- process-control material excluded from FPF pattern prose, such as task dispatch, seam state, helper behavior, Git recovery, packet transport, review transport, chat cadence, and mutable release state;
- how the passage or decision-ground item was used: quoted by value, narrowed in scope, instantiated as a case, used as decision grounds or drafting guidance, retained only as an example, or retired;
- any meaning loss or addition created by that source-use result: changed scope, relation, evidence path, admissible use, non-admissible use, reader use, or recoverability condition;
- the first improved FPF use that the admitted method gives to an author, reviewer, or downstream FPF user;
- the disposition: selected now, inherited and sufficient, rejected now, or outside this decision. For an outside item, name the evaluation pattern or accepted `DRR` that carries it, or state the content of the accepted decision ground that does so.

Reusable process-source methods may contribute beyond semio wording or pattern-authoring language. Admit the contribution when it is separable from local process mechanics, improves the selected FPF use, and has adequate grounds for the claims being made. Apply E.19 to pattern admission and E.21 when a pattern-quality conclusion is required. After the method lands in FPF, process documents should cite the selected FPF pattern instead of keeping a parallel long-form rule.

#### E.9:4.2 - Develop an unsettled decision through a working expression

If the answer is unknown, start with the difficulty and the material available. Use §4's order to present the answer once selected. Filling the Decision block in advance would require the author to guess what the inquiry is meant to establish.

Use a provisional expression to bring a consequential relation into view: juxtapose two cases, arrange competing explanations, trace a dependency, or compare an intended use with the result currently available. E.8:4.2.1.2 and A.6.3.RT.OE supply the expression construction. Identify what the arrangement lets you infer and what remains unsupported. A question mark can make an unresolved interpretation visible; it supplies no premise for choosing one answer.

Let the result change the decision question when it reveals that the original question conflated different work. Retain live alternatives only for the comparison they support. Replace a classification by format, tool or package name when the deciding difference concerns the operation or conditions of use. A working table can therefore be revised or discarded after it has produced the useful distinction.

Before another author relies on the selected answer, resolve each premise that can change its selected obligation, or bound the result so that the remaining uncertainty does not defeat that obligation. If neither is possible, state where the decision must stop. Use the four kernel components and the applicable inspection content in §4.1 to inspect that closure. Material already recoverable in the account need not be copied into another answer column. A source pointer without the needed substantive contribution is not recoverable decision content.

Keep this difference visible in the writing. “The source order for this row is unknown” can be a valid investigation result. “Convert this row using day/month/year” would require the missing premise. Conversely, a settled decision to stop such rows and request their interpretation can be supported even while their dates remain unknown. What remains open must be compared with the decision being made.

The record carries the resulting problem, selection, reasons and consequences, not every discarded worksheet or the chronology of deciding. Retain a working expression when a later use needs its reasoning or recoverability; otherwise carry its useful result and source return into the decision.

