---
chunk_kind: "child"
pattern_id: "F.1"
pattern_title: "Find and Select Sources for a Current Question"
section_id: "F.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.1/F.1__006_archetypal-grounding.md"
commit_sha: "94b6c708eadc1a572f7db7788ed2e74df4053b2d"
heading_path:
  - "F.1 — Find and Select Sources for a Current Question"
  - "F.1:5 — Archetypal Grounding"
line_start: 106177
line_end: 106304
dependencies:
  - "A.10"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "E.11.PUR"
  - "F.0.1"
  - "F.0.2"
  - "F.17"
  - "F.9"
keywords:
  - "SourceCutNote"
  - "answer-changing role"
  - "exact source and edition"
  - "inspectable candidate material"
  - "search and access limits"
  - "source cut"
  - "unfamiliar terminology"
---

### F.1:5 - Archetypal Grounding

#### F.1:5.1 - Three heterogeneous source cuts

##### F.1:5.1.1 - Role assignment, performed work, sensing, and execution

Candidate sources include BPMN 2.0 (designed workflow structures), PROV-O (performed activities and provenance), ITIL 4 (service vocabulary), ODRL 2.2 (permissions, prohibitions, and duties), SOSA/SSN (observations and results), and IEC 61131-3 (control-program execution). Retain only those whose exact claims change the receiving question.

The cut keeps false friends visible: a BPMN participant is not an RBAC role; a PROV activity is not a BPMN process; an SOSA observation is an act, not a status; an ITIL incident is not automatically a plant fault. F.1 exposes these source roles but does not settle their relations.

##### F.1:5.1.2 - Methods, types, and measurement

SPEM 2.0 or ISO 24744 may change the reading of Method and MethodDescription; OWL 2 and formal concept analysis may change kind reasoning; SOSA/SSN and ISO 80000-1 may change measurement and quantity claims. The cut preserves the source-fixed differences rather than making *method*, *concept*, or *measurement* globally uniform.

##### F.1:5.1.3 - Control, actuation, and services

Control-theory sources, IEC 61131-3, ISA-95, ITIL 4, and SOSA/SSN can contribute different claims about controller design, program execution, integration, service commitments, and observations. A current question may need only a subset. *Actuation* is not a service promise, and *incident* is not a plant fault merely because the words occur near operational work.

#### F.1:5.2 - Minimal worked source cut

The project brief already identifies this receiving question: **Can one contribution use “process” for both a workflow description and a performed occurrence?** The exact question, not the note or source list, is the `SourceCutNote`'s EntityOfConcern. The project names its effective ReferenceScheme **Workflow and occurrence source cut, August 2026**; that scheme fixes the three editions below and the ordinary-English role statements. The intended use stays in the ClaimGraph.

```text
Receiving use: decide which subjects the later pattern must keep distinct.

Retain:
- OMG BPMN 2.0.2 (January 2014), §10.1: its workflow-structure claim changes the design-description side.
- W3C PROV-O Recommendation (30 April 2013), §3.1: its Activity claim supplies the performed-occurrence contrast.
- W3C SOSA/SSN Recommendation (19 October 2017), §4.3.2.2: Observation supplies an action-changing counterexample—an act that follows a Procedure and yields a Result, not a workflow graph.

Exclude for now:
- thermodynamic-process literature: no inspected claim changes this stated use.

Known limit: service commitments are outside this cut.
Reopen if: the use adds physical transformation or service commitments, a relied edition changes the relevant claim, or a known counterexample no longer fits.
Search policy: none needed for this bounded question.
```

The resulting `SourceCutNote` is identified by that ClaimGraph, the stated receiving question, and the named reading scheme. Because this cut turns on the difference between a designed workflow and a performed occurrence, the project recovers any disputed *process* reading through ordinary F.0.1 while inspecting source roles, before stabilizing the cut. It adds an F.17 cell afterward only if later reuse, a claim, a named receiver, or an actual relation needs one.

#### F.1:5.3 - Portable first-hour case — function-to-module allocation

“First hour” means a compact entry slice, not a deadline or completeness claim.

**Receiving question.** Which current FPF sources must a Systems Engineering author use to prepare a first function-to-module allocation teaching slice without collapsing functions into modules? The project identifies this sentence as one exact question before treating the note as a C.2.1 episteme; that question is its EntityOfConcern.

**Receiving use.** Prepare a slice that helps a practitioner generate and compare candidate bearers, modules, allocations, interfaces, and trade-offs instead of copying functions into a component list or selecting familiar bearers first. This use stays in the note's ClaimGraph.

**Effective ReferenceScheme.** `FPFCoreReferenceScheme`, applied to the FPF August 2026 edition and the exact section locators below.

**Retained sources and answer-changing roles.** All five are exact passages in that edition.

1. **A.6.F §§4.2 and 4.5.** Separates the possible subjects hidden by function-like wording and requires function, bearer, flow, module allocation, and interface claims to remain distinct. This blocks the one-function-one-component shortcut.
2. **A.6.M §§4 and 4.3.** Treats module use as claim content over exact holons, allows many-to-many or still-unallocated functional claims, and requires an actual interface specification when compatibility or substitution is claimed. This changes what an allocation row must show.
3. **C.30.TFS-REL §4.2.** Relates functional structure to selected transformation-flow structure without identifying them. This exposes candidate flow topology, crossings, and correspondence limits that can change bearer placement.
4. **C.31 §4.5.** Makes function-module alignment, interface burden, and flow-boundary alignment separate characteristics rather than one modularity score. This changes the trade-offs the comparison must expose.
5. **C.32 §§4–5.** Starts candidate synthesis from functional demand and candidate bearers, keeps materially different configurations visible, and records expected gain, known loss, constraints, and source-return conditions. This prevents the source cut from pretending to choose the architecture.

**Deliberate limits.** The cut claims neither an exhaustive survey of allocation algorithms nor one module taxonomy or cross-sector optimum. It does not decide the final DPF pattern identity.

**First result.** One `SourceCutNote` whose ClaimGraph contains the five roles, use, limits, and reopen conditions; whose EntityOfConcern is the stated question; and whose effective scheme is `FPFCoreReferenceScheme` for FPF August 2026. The later comparison must expose unsupported capabilities, unallocated functions, unresolved interfaces, alternatives, trade-offs, and accepted losses.

**Reopen when.** A relied FPF passage changes, the question expands to external allocation algorithms or another domain, or the intended DPF use changes the required answer or boundary.

#### F.1:5.4 - Readable reasoning moves

- **Retain:** “This exact source stays because this inspected claim changes the answer in this way.”
- **Exclude:** “No inspected claim from this source changes the stated use; record the exclusion and what would reopen it.”
- **Return a gap:** “This unavailable or uninspectable source may be load-bearing; the cut remains limited here.”
- **Keep meanings local:** “Selection puts both sources in view; it does not say their terms are identical or related.”
- **Use search assistance:** “The ranking tells us what to inspect next; the source claim decides whether it enters the cut.”
- **Reopen:** “This question, use, relied claim, rival, counterexample, or transfer boundary changed, so select again.”

<a id="f155---didactic-distillation"></a>

#### F.1:5.5 - Didactic distillation of source selection

> State and independently identify the question; keep the later use in the claims. Keep a source because an inspected claim can change the answer, expose a rival or counterexample, or mark a transfer limit. Return one finite `SourceCutNote` whose ClaimGraph carries those roles, exclusions, limits, and reopen conditions, whose EntityOfConcern is the exact question, and whose named effective scheme resolves the question and exact editions. Search scores may guide inspection; they do not admit or exclude a source. Stop when additional candidates do not change the answer.

#### F.1:5.6 - Manual archive: a rule under an unfamiliar name

A workshop reader asks, “May a shared bench be used while an acceptance run is cooling?” The available fictional archive has three paper binders labelled *Setup*, *Drawings* and *Bookings*. Its card catalogue lists current equipment names. The reader has no searchable index or retrieval service.

The reader preserves the whole question, including the cooling interval, and bounds the search to those binders. The catalogue has no “cooling” entry. That is a limitation of this route. Browsing *Setup* produces a reference to an older equipment name and a drawing whose legend says “reserved interval”. The reader tries that term in the drawing register and obtains drawing D-14, edition 2, note 6. The note reserves the bench through the cooling interval; its exception allows sharing only before the run begins.

The result is that inspected note, its drawing and edition address, why the interval and exception matter, and the scope of the archive searched. It supplies a rule for the subject practitioner to use with the actual run conditions. It does not establish the present bench state or permission by itself. The reader need not produce a SourceCutNote merely to return this sufficient source.

Change the question to “Which inspection condition changed between editions?” The reader obtains the available D-14 edition 1 note and compares it with edition 2 around the exception. Both passages become candidates. If the later comparison needs a justified two-edition basis, :4.2 selects their roles and returns a SourceCutNote. Change the question instead to “What word do these drawings use for the cooling interval?” The inspected wording can answer directly; further source selection adds nothing to that use.

The first failed route mattered because its catalogue vocabulary excluded the older name. The complementary route recovered source wording. This construction works with paper and ordinary reading; it requires no index engineering or automated ranking.

#### F.1:5.7 - An uncertain method-library vocabulary

A project reader asks, “Two proposed pattern uses each fit our concern, but both need the same exclusive instrument. What helps us say which use should precede the other?” They can search the available full FPF publication but know no PatternID for that concern.

The first lookup, “suitable methods”, yields only general fit cues. The reader preserves the shared-instrument condition and tries variants such as “coordination”, “shared constraint” and “precedence”. A contents row points to E.11.PUR. The reader opens the complete pattern, including :4.3–:4.4 and :5.5, rather than treating the row as an applicable Method.

The returned material explains why exclusion alone establishes conflict without selecting A-before-B. An applicable schedule or priority rule can supply a direction; when it is unknown, the direction remains unresolved. The reader returns that passage and the missing-rule question. The later judgement uses E.11.PUR; a work schedule or performed work claim belongs to A.15. Finding the passage creates neither kind of judgement.

A title-only service that cannot search or return those body conditions would require another accessible route or return its limit. If the reader already has a current adequate coordination judgement, finding can stop there. The example's useful search terms are variants for this concern, not fixed names every corpus must use.

#### F.1:5.8 - A changed edition with a known source

An engineer already has the needed fictional WS-4 procedure, edition 2, clause 7. An edition-3 notice names a changed inspection exception. The question remains whether the same inspection condition applies. The engineer opens edition 3 at that clause and reads the exception with its surrounding applicability conditions.

If the relied condition is unchanged, the passage remains usable for its earlier contribution, with the updated edition address. If the exception changed, the engineer returns the changed passage and the earlier passage when the comparison needs it, then reopens the affected subject judgement or source-cut claim. No unchanged chapter needs a new search merely because the cover changed.

Now change the question to whether a particular attachment can be accepted. The retrieved clause does not settle an unknown material or operating condition. The subject engineer receives the passage and that missing premise. A found rule and a justified source cut supply different contributions from engineering applicability.

#### F.1:5.9 - The original cannot be inspected

A review cites a 2025 original, but the reader can obtain only the review's excerpt and the original's catalogue record. The catalogue establishes a lead. The excerpt is inspectable at its own review address; the original's body and omitted conditions remain inaccessible.

Return those distinctions and identify the needed original or authorized access. Continue a use that the excerpt can actually support; keep a dependent judgement open when its missing context can change the answer. Another search over the same catalogue cannot turn the original into inspected material. A later copy of the original reopens that gap; it does not require discarding other unchanged findings.


#### F.1:5.10 - A changed question with two needed contributions

A workshop reader asks, “Which training material will reduce mistakes at handover?” The available fictional archive contains a course catalogue, an incident note, the current equipment register R-4, a handover procedure H-2 and several equipment-identification guides. The immediate concern is a receiver being sent to the wrong pump or being unable to tell whether its preparation is complete.

The catalogue points to a note about equipment labels. Reading it reveals that an old label is used for two different pumps. This gives the reader a more useful local inquiry: what must the handover distinguish so its receiver can identify the equipment and its preparation state? B.5.PI:4.4 permits this revision while retaining the original concern. Searching for another synonym of “course” would keep the earlier hypothesis in control.

The equipment register explains how current identifiers distinguish the pumps. Further guides found through different terms give more identification examples, but leave the preparation-state question unanswered. A reference in the register gives a route to H-2. The next search opens its completion condition in section 5, with the definition of the reported state and interval. The new contribution is that condition, not merely a new document.

The reader now returns R-4:2 for the equipment-identification basis and H-2:5 for the condition on reporting completed preparation. These supply the current requirement question. Stop searching and use them to examine the proposed handover. Choosing a course still requires judging the actual learning need; identifying the requirements did not make that judgement. If the available operations do not explain how to produce the required handover, use C.39 to develop the missing connection, with those passages as inputs.

If the procedure is inaccessible, return the inspected identification passage and the missing preparation-condition source. More identification guides do not close that gap. If both passages were already known and sufficient, open them directly. No additional route or SourceCutNote is needed for that use.

