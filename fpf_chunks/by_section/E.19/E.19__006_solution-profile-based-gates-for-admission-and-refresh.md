---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:4"
section_title: "Solution — Profile-based gates for admission and refresh"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__006_solution-profile-based-gates-for-admission-and-refresh.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:4 — Solution — Profile-based gates for admission and refresh"
line_start: 119781
line_end: 120332
dependencies:
  - "A.15.1"
  - "A.6.P"
  - "E.10"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "inside the predicate)"
  - "under E.8 H-8 and CC-SG.4"
  - "where a non-deontic Invariant: predicate is required)"
---

### E.19:4 - Solution — Profile-based gates for admission and refresh

Establish **Pattern Quality Gates (PQG)**: a family of profiles that declare admission and refresh checks. Different reviews can combine different profiles instead of applying one checklist to every pattern.

A **Pattern Check Profile (PCP)** is a named bundle of check families. Profiles are **additive**: every review configuration includes the baseline profile and only the risk-driven profiles needed by the declared question. A PCP specifies questions and closure conditions; the reviewer applies them and returns findings or repaired text. An unselected profile requires no result row or durable disposition.

Choose review depth from the harm if a defect survives, the novelty and complexity of the claim, how widely the pattern will be reused, and how likely its sources or neighbors are to change. Pattern length, official status, and the number of available checks do not justify deeper review by themselves. Use cheap automated or template checks for properties they can test, then spend reviewer attention on semantic, ontological, practitioner-use, and current-source questions they cannot close.

**Editorial and runtime gates.** PQG and PCP are editorial review constructs in the authoring plane (Part E). They are distinct from enactment and runtime gating constructs such as `OperationalGate(profile)`, `GateProfile`, and `GateDecision` (A.21), which govern Work transitions and gate decision policies elsewhere in FPF.

For an ordinary bounded review, keep the reviewed edition or subset, question, selected profiles, checked loci, defects or repairs, and conclusion. When exact replay or a named later use needs a stronger account, also keep independently recoverable:

1. the exact reviewed FPF pattern edition or bounded subset and the declared admission/refresh question;
2. the review configuration: baseline and risk-selected PCP declarations, exact question scope, use, qualification window, and stop boundary;
3. the semantic review `U.Method`, when that identity matters; call an episteme its `U.MethodDescription` only after it passes A.3.2;
4. for each actual review, repair, or verification occurrence asserted as dated `U.Work`, recover every actual performer through A.13 and use A.15.1 to identify its time, Method, containing System, and Work independently. Add F.6 only when the review account expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. That attribution must be independently grounded. Holder identity or timing does not establish it. A missing or failed F.6 link alone leaves independently admitted Work intact. Recheck any A.13 or A.15.1 premise invalidated by the same finding and its dependent conclusions;
5. each PCP check application and A.6.1 binding only when the receiving use must replay those bindings;
6. any distinct authoring/repair work, changed pattern edition, and focused verification work/application in inspect-repair-verify form;
7. actionable finding or blocker claims, focused-verification claims, and one C.2.1 aggregate E.19 review-result episteme when a durable conclusion is required;
8. any separate authority-bearing admission, refresh, return-for-repair, or waiver decision and its decision work;
9. witnesses and the support the claim requires, including A.10 when an implicit or required-replayable source-to-use account is needed and any B.3 result the selected assurance claim requires; and
10. any F.10 status use, publication occurrence or form, carrier, and currentness relation used by the receiving claim.

Any local system-role kind and its independently evaluated classification are optional separate claims. Neither supplies assignment or performance. Route unresolved source *role* through `E.10.ROLE`. Name the intended-reader position or the representation position. When a later claim relies on a dated occurrence, apply item 4 and `CC-E19-0`.

In Plain, **review run** refers to the configuration, the reviewer’s actions and their results. The §4 account keeps the declarations, applied Method, actual review work, findings, result, and any authority-bearing decision distinct when those identities are needed.

#### E.19:4.1 - Define the reviewed pattern or subset

Name the reviewed pattern or bounded subset, its edition or other stable version basis, the admission or refresh question, the selected profile questions, and the review boundary. That is enough for an ordinary bounded review. Add exact scope, window, and review-configuration identities only when a receiving result or named reliance needs them. The profiles determine which questions to ask and how deeply to review them. An ordinary bounded review requires no progress record.

When a reusable result or named reliance depends on how the review was enacted, apply the item 4 actual-Work account and `CC-E19-0` to each asserted review, repair, or verification occurrence.

If a durable aggregate result is needed, constitute a C.2.1 result episteme whose EntityOfConcern is the reviewed pattern edition or subset and whose ClaimGraph states the review scope, applicable profile questions, actionable findings or aggregate cleared boundary, conclusion, and reopen condition. Add a non-use boundary only when it changes a named receiving use under the `F.19` plausible-intended-reader test. Witnesses, evidence use, the optional result publication, and any authority-bearing admission or refresh decision remain separate.

Choose inspect-repair-verify when the reviewer may edit and same-turn repair fits the declared use. Choose independent findings when the review needs separation from the author or an unchanged candidate. Independence changes who edits. The selected questions remain the same, and no additional dossier is required.

**Choose one review form.**

1. **Inspect, repair, and verify.** One bounded review may include inspection, repair, and focused verification. A reviewer performs those actions. Distinguish their performer, Method, affected object, or occurrence only when the positions differ or a named later use needs them. Apply item 4 and `CC-E19-0` if the account asserts dated Work. Apply every selected question, repair every in-scope defect, and reapply the affected checks. The changed edition and focused verification carry the substantive evidence. Constitute an aggregate E.19 result episteme only when a receiving admission or refresh decision requires it. Make a separate findings record only for an unresolved blocker, a decision outside current authority, or transfer to another author.
2. **Independent findings.** A reviewer applies the selected questions without changing the reviewed pattern or subset. One C.2.1 findings-result episteme or handoff file records every actionable defect and blocker, with repair direction precise enough for the author to act without repeating the diagnosis. It is neither the reviewing action nor an admission decision.

A selected question that reveals no defect requires no durable pass entry. Independent review records actionable findings without compiling positive recitals. In repair mode the repaired text and its verification show the completed repairs, with no parallel findings record.

If another pattern defines a reusable value or decision required by the declared use—such as an `E.21` coordinate, a `DRR` decision, or a landing result—that value belongs to the result required by that pattern rather than to an `E.19` progress account. `E.19` specifies the substantive questions and outcomes independently of how a working environment keeps place during the review.

**Complete the selected scope.** Inspect every independently answerable question in the declared baseline and risk-selected scope. The first defect, blocker, or already-negative admission conclusion may prevent a positive verdict, but it does not complete the review and does not suppress findings that remain independently obtainable. Stop before the selected scope is complete only when a missing source, missing authority, unsafe boundary, or equivalent condition makes the remaining questions impossible to judge truthfully or safely. In that case, identify the unexamined scope and the reason it could not be judged, and report the findings as partial.

A nontrivial pattern-quality review SHOULD state its quality-evaluation purpose before depth is selected. Use `E.22` or an equivalent compact question frame to say whether this review is a `floorEvaluation`, `exceptionalImprovementEvaluation`, `paretoTradeoffEvaluation`, `openQuestionDiscoveryEvaluation`, `absorptionEvaluation`, or a declared combination. If the purpose is absent, `E.19` treats the review as an admission-refresh blocker read, not as a request to raise every evaluated coordinate toward exceptional expression.

When coordinate values, `PatternQualityStatus`, or all-`4`/all-`5` claims are needed for one pattern version, the review opens or consumes an `E.21` result instead of assigning those values inside `E.19`.

When the review opens or consumes `E.21`, `E.19` treats `E.21` as a hard pattern-quality evaluation, not as a selectable profile. The review must not accept an `E.21` claim that omits required coordinates, omits `ShortRationale`, omits `PrecisionRestorationProfile`, uses inactive/triggered-coordinate language, narrows the requested use to make the result pass, or replaces coordinate values with blocker triage. In repair mode, repair or re-evaluate the affected result where that work is in scope. In independent findings, identify the defect.

Baseline triage can answer only the `E.19` review boundary when no `E.21` quality value, all-`4`/all-`5` claim, landing-quality claim, or pattern-improvement movement claim is being made.

If the aim is repeated improvement against an object-under-improvement evaluation, use `E.23` for the repeated method. An E.19 review configuration may supply PCP questions and its result episteme may supply findings inside that loop, while E.23 supplies the repeated Method. An E.19 result gives no ordinal quality value. Only a separate E.21 assessment application and result episteme can state the E.21 coordinate values for the changed pattern version.

In `E.19`, the reviewer judges the quality of an FPF pattern or bounded subset. `E.19` governs FPF admission, refresh, return-for-repair, blocker, and review-profile claims, not `E.21` coordinate assignment and not project-side publication interpretation, explanation interpretation, comparative review-unit use, or participation in a named project-side review relation. When those project-side relations are used, use the publication or project-side pattern that names the object being interpreted or reviewed.

**Project-side reuse boundary.** Use this boundary when an E.19 review-result episteme is cited for project certification, evidence, safety or compliance assurance, gate input, release justification, work authority, or publication truth. First identify the FPF pattern-quality claim it states: admission, refresh, repair return, or selected pattern-quality boundary.

Any project-side reuse then opens the concrete relation that governs that use: `A.10` for an implicit or required-replayable source-to-use account, `G.11` for source currentness, `B.3` for assurance, `F.10` for status use/interpretation, `A.20` for a current local CV status when applicable, `A.21` for gate decision, `A.15` for work, or the relevant project-side pattern.

The E.19 result may be evidence about FPF pattern quality; it is not certification of the project world. Plain wording in the reviewed text remains ordinary unless it changes admissible use, evidence, gate, assurance, work, decision, status use, or FPF pattern application. A project refusal or approval requires a project-side governing relation that states the project claim and its admissible use.



Give semantic or ontological defects and Solutions that fall short of current SoTA priority over formal or template defects, such as failure to follow E.8 structure or RFC deontic terminology. In repair mode, fix the formal or template defects within the declared boundary. In independent findings, identify them and say how to repair them.

For example, if the header block is missing or incomplete, **continue with ontology and semantic review first**. Treat missing header fields as one mechanical defect, not as a reason to stop (PCP-BASE #7).

When a proposed or accepted pattern change needs a best-known **Delta-Class (Δ-0…Δ-3)** and initial **impact radius**, place them in the governing change, decision, or landing result using E.15's actual-effect and actual-dependency tests. `E.19` repairs or reports an omission that matters to the selected review; it does not copy a successful change account into a second review record.

#### E.19:4.2 - Apply the baseline profile to every run

Every run MUST include **PCP‑BASE** as a triage baseline. Full-depth checking
is selected only where the relevant risk is present; reviewer depth SHOULD
prioritize the FPF-governed sections and enforceable requirements in E.19:4.2.1.

1. **Internal coherence (problem <-> conformance claim <-> solution)**
   The Conformance Checklist matches the Problem statement and Solution (no "orphan requirements" and no "unclaimed requirements").
2. **Lexical discipline & reserved vocabulary**
   Terms and registers follow lexical rules; ambiguous "everyday" synonyms do not silently replace kernel vocabulary.
3. **SoTA-Echoing minimum compliance (E.8)**
   SoTA-Echoing satisfies the E.8 authoring requirements applicable to the pattern kind (Architectural vs Definitional), including stated adopt/adapt/reject stances and the E.8 two-part SoTA test: current best-known problem-solving practice for the named practice question, and by-value incorporation into FPF-governed pattern loci. If a SoTA Synthesis Pack exists for the topic, SoTA-Echoing binds to it rather than forking an untracked narrative. Any divergence of pattern norms from contemporary practice is explicitly stated as such. SoTA-Echoing **MUST** be non-decorative, **MUST** reflect best-known current practice rather than official status, source recency, institutional adoption, or merely popular defaults for the declared problem, and **MUST** govern the Solution and other FPF-governed sections, or those sections **MUST** justify divergence explicitly.
4. **Cross-pattern compatibility & impact radius**
   Relations are consistent with declared dependencies and dependents. Declared scope and impact are compatible or explicitly limited.
5. **Didactic grounding**
   Apply E.8:4.2.1.3 to the connected explanation and its cases. Recover the common relation or Method being taught, its grounds, and the correspondence to the example. For a Method example, distinguish the reusable way, the depicted performance and its subject material. Inspect whether the cases make the material variation of the declared use intelligible; a correct result in the example's domain answers only that part of the review.
6. **Reader-fit**
   The pattern body addresses the intended FPF user in the working role governed by that pattern. FPF developers, package architects, reviewers, and evaluators are appropriate readers when they occupy that role. FPF-governed sections explain in user terms admissible use, costs, boundaries, the concrete definitions, constraints, tests, or other contributions used from FPF patterns named by value, and the project-side FPF kinds, references and related relations also named by value. Architecture placement, freeze or merge state, package-boundary rationale, reference boilerplate, quality or projection evidence, corpus-entry evidence, `PatternQualityStatus`, monolith-parity evidence, landing evidence, and broader package-development rationale stay in `DRR`, architecture documents, review handoff, `E.21` result, `E.19` findings, README, ToC, `E.11`, cards, retrieval or projection carriers, release or landing evidence carriers, companions, or ordinary references unless they change the working reader's first admissible move.
7. **Template & section integrity**
   This is lowest priority for review depth and **SHOULD NOT** consume effort that would displace ontology, semantics, modularity, slot discipline, or SoTA checks.
8. **Modularity & contradiction hygiene**
   The pattern **SHOULD NOT** be overloaded or significantly expand requirements or dependencies without an explicit reason and impact record.
   Checks include: scope containment, split/refactor recommendations when warranted, and contradiction scans against neighbor patterns in Relations.
   The pattern SHOULD balance cohesion and coupling across FPF.
   If the pattern defines specialization or an abstraction stack, it SHOULD NOT mix slot interfaces or parameters from different abstraction positions; use explicit `⊑/⊑⁺` or `Uses` cuts instead.
9. **Substantive solution and locus adequacy**
   For the reviewed pattern, ask a short set of questions about its problem and the change under review. Does the pattern still solve the stated problem? Are the decision points and applications of the relevant patterns correct? Are kind boundaries and selected companion or projection functions preserved? Has anything worsened? Are the SoTA rows current enough for the claim they discipline? Does that claim have enough support without excess material?
10. **Triggered method, performer, work, and result separation**
   When a Solution says how to do work, first distinguish content defining, constraining, testing, or guiding a Method from a claim that dated Work occurred or the world changed. Method guidance alone does not trigger a fictive performer or Work. If an account asserts dated `U.Work`, verify the §4 actual-Work account. If it asserts a world-side change, identify the change relation, the pattern that defines it, and the things it relates. Keep the intended-reader position, any qualifying A.3.2 method-description episteme, actual performer, Work, and problem-facing result separate. For a literal dated `U.Work` claim, return a finding when an episteme, checklist, plan, prose, or intended-reader or representation position is made to perform Work, or when Work and result are collapsed. Judge ordinary or metonymic wording through the complete-claim test in `F.19`; a familiar instrumental expression alone does not require a formal Work account.

##### E.19:4.2.1 - Where to focus baseline review

Focus review effort where it can improve semantic and ontological trust. Keep routine checks feasible by giving the following parts different depths.

* Treat **FPF-governed sections and deontic requirements** as the primary depth loci:
  * the pattern’s **Problem frame**, **Rationale**, and **worked slices** when a new family, profile, or specialization would otherwise be intelligible only from project context,
  * reader fit in **Problem**, **Solution**, **Consequences**, **Rationale**, and worked slices whenever the draft risks mixing user guidance with package-development rationale,
  * the pattern’s **Conformance Checklist** (the enforceable conformance check set): keep items universal and easy to use, limit prohibitions to what is needed, and leave checks that belong to another pattern there,
  * **deontic clauses** (`MUST/SHALL/SHOULD/MAY`) that define requirements on the authoring/validation plane (not laws of nature or mathematical facts; ensure an explicit conformance subject),
  * **admissibility constraints** (`Invariant:` / `Well-formedness constraint:`) that define valid models (cardinality, typing/kinds, totality) and are written as non-deontic predicates (no RFC keywords inside the predicate),
  * **definitions and mint/reuse decisions** (new terms, renamed terms, scope claims baked into names, avoiding overloaded names and choosing names that fit the intended use),
  * **cross-context and cross-plane claims** (Bridge hygiene and “sameness” assertions),
  * **SoTA** (when the pattern claims state-of-the-art rather than a popular-but-outdated solution or vocabulary),
  * **substantive solution and locus adequacy**: one reviewed-pattern-specific content pass checks whether the repaired text still solves the stated problem, assigns claim-bearing material to the correct governing loci named by value, preserves kind boundaries and selected companion or projection functions, keeps quality/projection evidence and executor/reviewer correspondence out of the pattern unless the pattern's own `EntityOfConcern` and user-facing action are that evaluation/projection work, and has not become either under-grounded or over-bureaucratic,
  * **modularity and Slot discipline of A.6.5** that provide evolvability of FPF,
  * **absence of contradictions in a pattern**,
  * **Relations** that define compatibility and impact radius.
* Check **mechanical corrections** briefly when their scope is limited to the named mechanical property and their semantic and practical effects are unchanged, for example a micro-typo or heading-format correction. For live recoverability or contribution questions in stylistic or narrative rewriting, including RFC-form deontic cleanup, use the whole-span `F.19` reading below. Automate a check only for a named property the tool tests. A clean result establishes that property alone. Semantics, ontology, practical usefulness and source currentness need their own grounds.
* **Do not block semantic review on template and RFC compliance defects.** Missing header block fields (E.8 H-5), missing canonical sections, or a missing footer marker are fixable integrity defects. Record them as repair items and continue with the FPF-governed section checks in the same run.
* **Whole-span precise language.** Reviewers SHOULD apply the complete connected Solution in `F.19` to the selected FPF-governed span: recover meaning, test the contribution of each optional expression, and compare useful content before and after repair. Retain its precision-before-coarsening order, cold intended-reader recovery, evidence-selection and coverage conditions. Use E.10 or the subject pattern only for an FPF meaning that remains unresolved.
* **Precision-restoration distribution must be preserved.** Apply `CC-E19-21`; keep only review-specific questions here and use the declared language or subject owner for the repair.
* **Review-specific continuity questions.** Apply these to the changed claim and affected uses:
  1. Is the pattern's own `EntityOfConcern`, first useful move, practical delta, and any action-changing applicability boundary recoverable, with its action guidance before auxiliary wording, publication, architecture-placement, package, or quality apparatus?
  2. After wording or reference migration, does the claim still reach the same referent through the intended slot or reference position and alignment path? Record any deliberate retargeting in the governing change decision.
  3. When phrase apparatus, semio bias, architecture placement, package rationale, or quality apparatus changed, did the repair preserve the function the claim needed and remove only the displaced apparatus? Name each outside definition, constraint, or test by its supplying pattern and use a formal identity only for a live distinction or named reliance.
  4. Do the affected current consumers still receive the intended meaning and use? Resolve semantic, mechanical, or compatibility changes in the affected sources; report unresolved conflicts rather than creating a disposition for every unaffected consumer.
* **Use preservation and guard selection are different decisions.** Always compare the admissible uses of the old and repaired claims under their governing rules, including any expansion or narrowing. The `F.19` plausible-reader test decides whether an explicit description, publication-use, or non-use guard deserves mention. A justified guard still undergoes the same before/after use comparison. Use `F.19` and the patterns that define or constrain the Method, Work, evidence, assurance, gate, status, decision, or unresolved *role* claim. Apply `CC-E19-0` to dated Work.

When E.21 is active, its `PrecisionRestorationProfile` carries the quality result; E.19 does not duplicate it.
* **Design-time and run-time both count.** The same precision discipline applies to FPF pattern prose and to any reviewed publication text, worked slice, or performed-work exemplar when that text is being assessed for admissibility, guidance, reuse, gating, release, policy, assurance, or action-selection use.
* **Report ordering (impact-first).** In run outputs and remediation direction, give priority to ontology, semantics, modularity and SoTA findings in FPF-governed sections. Group low-signal formatting/typos into one compact tail finding unless they change meaning.

#### E.19:4.3 - Add risk-driven profiles

**PCP‑PRAG (Pragmatic utility & adoption)** — Trigger: the pattern is Normative and claims practice guidance.
Check these connected uses:

* **Recognition and first action:** an early `Use this when` or equivalent, a recognizable working situation, the cost of missing it, practical gain, first admissible action and ordinary non-use boundary.
* **Performable guidance:** a worked application that makes the Method's own choices, intermediate results and continuation recoverable; useful Consequences and Anti-Patterns; and a clear adoption test. Select additional materially different applications when the declared use requires them.
* **Subject and reader:** a short account of the primary EntityOfConcern, relation or claim record and any minimal modeling lens needed by typed declaration content. Give early technical terms nearby plain glosses. When several reader situations are served, state the primary working reader, concern and viewpoint.
* **Recognition and assurance:** put first-use guidance before the declaration, modeling and review/check material needed for assurance. Keep its scope consistent with the recognition claim.
* **Grounding and breadth:** connect explanatory SoTA rows to their working-reader implication and the cases or boundaries they discipline. A universal or transdisciplinary claim needs heterogeneous recognition situations adequate to that breadth; F.16 is the preferred compact example-matrix template.

Compare the account with the promised subject before using a successful case as an adequacy result. Identify which general grounds explain the choices across the required variations and which differences change the action. Follow a continuing case back to that account when the example’s application problem begins to determine what the pattern teaches. Preserve its useful grounding, then obtain the missing explanation or varied application. Use E.21's scope and case-coverage coordinates when a quality value is required; a demonstration in one case does not settle a broader scope.
When admission or refresh includes precise-language repair, apply `CC-E19-7a`. It preserves practical guidance and the Plain/Tech relation under `E.2` `P-2` and `E.12`, with formal identity and dated-Work checks only under the conditions stated there. `F.19` governs the whole-span repair; `E.10` supplies compact cues and FPF routing.

For a broad cleanup across several patterns, or any cleanup that touches FPF-governed Problem frames, Problem sections, first-use recognition text, archetypal grounding, examples, or worked slices, check whether the didactic function was harmed. In inspect-repair-verify, restore the working situation, first useful move, and the definition, constraint, test, or other pattern contribution needed by the claim; in independent findings, record the exact harm and repair direction. A positive `improved` or `preserved` account is required only when another evaluation makes that value one of its substantive results, and it belongs in that evaluation.

**PCP‑MOD (Modularity and abstraction-boundary discipline)** — Trigger: the reviewed pattern or subset shows scope creep or mixes levels of abstraction (for example, a pattern bundles universal core rules with frame-specific content and discipline-specific method semantics, or it mixes EntityOfConcern, Description, and Specification positions in one object).

Checks include:

* an explicit **core vs extensions** cut (universal invariants are factored into one stable “core”, and extensions reference it rather than re-stating or mutating it),
* no conflation of **specialization vs dependency**: use `⊑/⊑⁺` for refinement/extension and `Uses` for pipelines; do not mix their semantics,
* no conflation of package-form, concrete pattern-to-claim contribution, and package-relation functions: **Pack vs Kit vs Suite vs Family vs Bundle vs Cluster vs Profile vs Overlay vs Record vs Umbrella** are not interchanged, and the review states carrier status, the definition, constraint, test, or other pattern contribution used, and the package relation, preserving those distinctions across stylistic changes,
* description-lane descriptions and their publications do not grow mechanism semantics; for an MVPK face or projected publication form, no-new-claim checks that it introduces no claim beyond the selected episteme and no-shadow-default checks that it introduces no undeclared default. Keep the selected episteme, optional projection/construction, face, publication form, publication occurrence, rendering, and carrier distinct. The selected episteme has `U.View` membership only when exact E.17.0 conformance independently obtains; face status, projection, profile selection, and compliance with these two checks establish no membership or truth,
* slot-discipline hygiene for any ordered specialization set: SlotKind invariance is preserved and inherited operations do not gain new mandatory inputs (A.6.5 / A.6.1 specialization discipline).

**PCP‑REFRESH (Staleness & compatibility refresh)** — Trigger: there are signs of staleness, such as an outdated SoTA claim, a renamed or superseded relation, terminology drift, or an explicit refresh window in a current source-use, change, or decision record.
Checks include:

* refresh-sensitive claims are identified and either (a) updated from the best current line of work for the problem with matching Solution changes, or (b) explicitly scope-limited and labeled as historical lineage. Source date, count, official status, or novelty alone does not establish current-best use,
* select living refresh only for a high-priority claim or pattern subset likely to change when new evidence or a changed neighbor appears. Monitor and reopen the smallest affected unit at a named trigger. When continued surveillance no longer justifies its cost, retain only a separately justified interval or trigger and any binding maintenance requirement; otherwise end that surveillance,
* Relations are updated to current pattern IDs; deprecations/renames are handled via explicit continuity notes (no silent relabeling),
* when a new or substantially revised pattern subset is being prepared for send or landing, inspect the related patterns, the concrete constraints or tests they supply, companion patterns, Relations entries, and monolith-backed pattern sections that may require aligned edits. Repair an in-scope mismatch or return it as a finding. The changed sources and the governing landing or release result show successful alignment. E.19 requires no separate pass entry,
* any long-lived companion, profile, check sheet, pattern-local companion row, review harness, or analogous selected non-pattern FPF kind-reference pair kept with the reviewed pattern or subset states its use question, the concrete pattern contribution or selected non-pattern FPF kind-reference pair it serves, admissible companion-only use, one real breakage if absent, and demotion or deletion condition when no such breakage exists.
* when the refresh causes Δ‑2/Δ‑3, verify that the governing change or decision result carries its actual-effect Delta-Class, actual dependent reach, and any DRR, focused verification, source-refresh, or F.9 consequence that the changed use requires under E.15, F.15, and F.9; repair or report an omission rather than copying a successful account into E.19,

A reviewer may override a trigger in rare cases. Override a triggered profile only when the risk that triggered it is absent here and a compensating check covers the live concern. When the override changes an admission, refresh, or other governing decision, place its reason in that decision basis. Otherwise E.19 requires no separate positive override account.

**PCP‑NORM (Normative guidance integrity)** — Trigger: the pattern introduces or changes normative requirements, introduces new conformance items, or shifts downstream requirements.
Checks include:

* **Delta‑Class (Δ‑0…Δ‑3)** and **impact radius** are explicit (what breaks, who depends on this),
* requirements are testable in principle, scoped, and non-contradictory,
* downstream patterns cited in Relations are compatible with the new guidance.
* for a Δ-2/Δ-3 change, apply E.15's actual-effect and material-decision test to the DRR requirement; a new normative pattern retains its DRR. When a DRR is required, it cites the applicable actionable PQG findings or the repaired candidate and focused verification, according to the selected review form; pointers suffice.

**PCP‑SOTA (Evidence and SoTA alignment)** — Trigger: the pattern’s Solution asserts “best practice”, “state-of-the-art”, or introduces new synthesis claims.
Checks include:

* each “best practice” claim or SoTA claim in the Solution has a stated link to SoTA‑Echoing rows (or to SoTA Synthesis Pack identifiers when used), so readers can recover its grounds. Those rows identify best-known current practice rather than popularity alone,
* the selected SoTA practice or source set answers the declared working problem and the relevant domain or practice tradition. Justifying package placement, naming or clustering alone is insufficient,
* each SoTA row changes at least one FPF-governed outcome for the pattern: what the user may do, a source-supported applicability or reliance limit, which FPF pattern application must be named, or a claim's eligibility for a named release, policy, assurance, gate, action-selection, or adjudication use. An explicit rejected reading follows F.19's grounded-guard test,
* novel synthesis retains its evidential status. Frame it as a scoped hypothesis with explicit limits, or substantiate the stronger claim through its source claims, support and conflict relations, shared dependencies and applicability under `B.1.3`. Admission as normative guidance requires those grounds and limits. Use `G.2` when the receiving use requires broad, refreshable SoTA harvesting and its handoffs. Pack registration alone does not establish the synthesis as best-known practice. A merely explanatory SoTA note that leaves the FPF-governed sections untouched is non-conforming,
* where traditions disagree substantively, the pattern makes the disagreement visible and states whether it adopts, adapts, or rejects each relevant source idea instead of silently selecting one tradition,
* retrieval or benchmark methods are used only when the relevant evidence relation is present; their dimensions do not become universal pattern-quality benchmarks,
* refresh‑sensitive claims (those likely to decay) are marked with scope limits, timespan notes, or lineage labeling when appropriate.

**PCP‑BRIDGE (Cross-context or cross-plane reuse integrity)** — Trigger: the pattern imports claims, terms or norms from another context, discipline or reference plane.
Checks include:

* explicit Bridge usage where required (no silent identity by spelling),
* Congruence and loss are made explicit where applicable,
* any cross-plane reuse is explicitly acknowledged and its penalties do not leak into unrelated assurances.

**PCP‑SUITE (Mechanism-suite integrity)** — Trigger: the reviewed pattern or subset introduces or revises a suite-level Description that enumerates multiple distinct mechanisms (e.g., `MechSuiteDescription` or a suite specialization) and/or changes suite requirements, conformance pins, or suite protocols.
Checks include:

* the suite remains a **Description-level** object: it enumerates member A.6.1 declaration epistemes through exact `MechanismDeclarationRef` values under A.6.7:4.1 and declares shared requirements/pins, but does **not** define mechanism blocks (`OperationAlgebra`, `Transport`, `Audit`, …) and is not used as a mechanism node,
* membership has **set semantics**: `mechanisms` contains no duplicates, and member order has no meaning. Express any intended ordering only in `suite_protocols`,
* suite protocols satisfy **A.6.7 WF-MS-2**: if `suite_protocols` is present, each step resolves to a selected member edition and a declaration-local operation in that edition; membership alone does not resolve the step,
* the suite is not a family of implementations: it MUST NOT be encoded as a `MechFamilyDescription` (families remain “many realizations of one mechanism”, not “many mechanisms”),
* the suite creates no transport exception. Apply `A.6.7:4.2` according to the claim. An F.9 semantic correspondence needs its obtaining Bridge, a C.3.3 kind correspondence needs its own basis, and a separately claimed plane relation remains governed by the rule defining that plane relation. A changed entity, edition, plane or notation alone creates none of those relations. Retain every activated channel's references and receiving-use conditions under `G.Core:4.2.3`. Loss assessment follows the receiving-use rule, numerical assurance penalties satisfy A.6.7:4.2(2), and the suite carries pins rather than CL/Φ/Ψ/Φ_plane tables,
* CG/CN authority pins remain explicit references to the single governance card and legality gate: if suite protocols include numeric comparison/aggregation/scoring, they cite `CG‑Spec` (SCP + Γ-fold + MinimalEvidence) and (where applicable) `CN‑Spec`, rather than duplicating “local CG‑Spec-like” content,
* suite protocols contain **no hidden tails**: if UNM/UINDM/ULSAM are required, the protocol expresses them as explicit `Uses` steps and suite audit requirements cite the chosen mechanism ids/refs (no “implicit normalization/aggregation inside score/compare/select”),
* gate separation is preserved: mechanisms and guards use tri-state `GuardDecision := {pass|degrade|abstain}` and MUST NOT publish `GateDecision` or `DecisionLog`; `block` remains gate-level only (`OperationalGate(profile)`),
* defaults remain single-sourced: portfolio mode, dominance regime, and unknown/failure behavior are either pinned in `TaskSignature` or one policy-assignment record, or not claimed; the suite does not define competing defaults,
* when the suite claims reusable outputs, publish/telemetry is an explicit external step of the surrounding protocol, governed by the rules for that use: G.10 for Part-G pack shipping and E.24.PUB for episteme availability, form or carrier claims. Under `A.6.7:4.4`, it is not a `ProtocolStep` in the suite-member sequence or a hidden tail inside selection.

**PCP‑P2W (Planned baseline & slot-fillings seam integrity)** — Trigger: the reviewed pattern or subset introduces or revises planned-filling content in one exact `U.WorkPlan` against an exact governed declaration member, including a publication or view of that content.

Apply the planned-filling rules in `A.15.3` to the changed plan content and its affected consumers:

* `A.15.3:4.0–4.4` govern declaration-local PlanItem content, declaration and member recovery, intended-performance and planned-value designation, target-declared cardinality, and positive intended-use meaning. Use the corresponding `CC-A15.3-01` and `CC-A15.3-03…09` questions.
* `A.15.3:4.2`, `4.5`, and `4.6` govern conditional reference/policy pins, independently established actual use, baseline-preserving comparison, and read-only publication. Use `CC-A15.3-11…14` for these uses.
* `A.15.3:12a–12b` supply the ordinary A.15.2 plan-content exit and the exact missing-source blocker when reusable typed use is needed but cannot be supported.

The declaration's own pattern defines member meaning and actual-use predicates; A.15.2/A.15.3 define the planned intention. Under those rules, review the use that changed, retaining the exact declaration and WorkPlan editions on which that use relies.

**PCP-TERM (Terminology & naming protocol)** — Trigger: the pattern introduces new terms, new U-kind pressure, new governed value names, new “unified names”, redefines existing labels, leans on FPF-governed phrases whose head kind or qualifier claim kind or admissible-use boundary is not yet restored, or uses FPF-governed trigger wording as if the word itself carried the needed kind.
Checks include:

* the “mint vs reuse” decision is explicit when a term is introduced or changed,
* naming follows the local-first naming protocol and avoids scope smuggling (role-word meanings, metrics, or stages baked into labels; overloaded words used as terms with a local sense). Remediation **SHOULD** use F.18 when its durable-name use condition applies,
* when `F.18` winner selection and `A.6.P` follow-through are both needed under their respective use conditions, treat them as one chain: inspect the candidate heads or phrases, kind conflicts, lexical conflicts, selected wording, and survival of the repaired phrase; repair a broken chain or identify the defect. A successful chain needs no pass entry,
* use the semantic-area cues in `E.10:0.2` with F.19's whole-span reading. The accepted sentence itself or its governing declaration must make the relevant object, value frame, relation, work, authority reference, pattern application, publication kind, companion function, or conformance claim recoverable; repair or report any case where it does not,
* for unresolved generic heads or claim-bearing qualifiers, and for a subsequent comparison, escalation, downgrade, or other use that depends on how the phrase is interpreted, apply `F.19:4`'s precision-before-coarsening rule,
* when repaired wording still carries an architectural claim kind or admissible-use boundary, verify that the resulting primary `EntityOfConcern`, first useful move, outside work, and any `E.10.ROLE` disposition or package-form decision remain recoverable in the repaired text or the decision that set the boundary; repair or report a mismatch, and
* source-side old wording and continuity rules are respected.

**PCP‑DEONT (Deontic clause hygiene: RFC keywords)** — Trigger: the pattern conflates admissibility/validity constraints with deontic obligations (for example, by using RFC keywords where a non-deontic `Invariant:` predicate is required).
Checks include:
* Deontic requirements are expressed with RFC-style keywords (see H-8);
* obligations are not smuggled into prose as informal imperatives. Admissibility/validity constraints are stated non‑deontically as `Invariant:` / `Well‑formedness constraint:` predicates and referenced from the Conformance Checklist when enforceable.
* **Subject discipline for RFC keywords.** If a sentence uses RFC keywords, its grammatical subject **MUST** be an agent or a published record or model whose required content is being constrained. State modeled-world admissibility or validity requirements as `Invariant:` or `Well-formedness constraint:` predicates and reference them from CC items when needed, under E.8 H-8 and `CC-SG.4`.

**PCP-ENTRY (Pattern-entry discoverability and entry-orientation changes).**
Trigger this profile when a change materially affects how a reader recognizes, selects, rejects or reclassifies a pattern body that directly governs the case, an applicable projection function, a set of patterns to compare on entry, a Problem-frame recognition signature, an expanded entry-disambiguation case or a lexical-query cue.

**Trigger classes**

`PCP-ENTRY` is a risk-selected editorial profile in the `PCP` family. Choose one lead profile for the change and add others for the specific failures they address.

Classify the change using the following cases.

* **Trigger class 0 — micro-edit**
  punctuation, formatting, typo repair, grammar, or meaning-preserving
  compression with unchanged pattern-selection effect.
  No `PCP-ENTRY`, no compact pattern-local note, no evidence mode, and no parity scan
  are required.

* **Trigger class 1 — local recognition wording repair**
  one improved `Use this when`, `Not this pattern when`, or one removed
  sequence-implying phrase with unchanged candidate-pattern set and unchanged
  governing-entry or applicable-projection-function boundary.
  Only the four-question core check is required.

* **Trigger class 2 — substantive entry, companion, or projection change**
  This class covers a new or changed README scenario, ToC query cue or `E.11` entry-distribution locus, including a worked comparison, pattern or applicable projection function newly used for entry. It also covers a changed boundary with a wrong pattern, a governing entry or an applicable projection function, a changed effect on local first-pattern selection, or a substantive change to a lexical-query cue.
  Run the core check and add the checks needed for unresolved entry risks. Reuse overlapping evidence. A compact pattern-local note is required only when the rationale is needed as described below.

* **Trigger class 3 — multi-companion-function or high-risk public entry change**
  A change affects several selected projection or companion functions together, rewrites a public entry, changes a frequently misclassified entry-recognition function, or introduces a set of patterns to compare on first entry.
  Run the core check and add the risk checks the case warrants, such as parity, wrong-pattern, public-entry or expanded-entry-disambiguation-case adequacy. Stop when the live risks are covered.

* **Trigger class 4 — retrieval-facing, observed-failure, or measured-improvement change**
  one retrieval-facing companion or projection function changes, one observed misretrieval or repeated
  search failure is being repaired, or the patch itself claims measured
  discoverability improvement.
  One selected evidence mode may be required, but benchmark-style reporting is
  not the default.

* **Trigger class 5 — normative authority, kind, or durable-name change**
  one entry-selection split, stable-name settlement, label-family change, or other
  normative architectural rewrite is in scope.
  `DRR`, `PCP-TERM`, and `PCP-MOD` are the lead decision or review profiles as applicable;
  `PCP-ENTRY` reviews only the entry-facing effects.

Ordinary changes outside this profile include the following.

* punctuation, formatting, and typo fixes;
* meaning-preserving prose tightening;
* one bare mention of a pattern without changed entry-selection effect;

* local wording repair that preserves what the reader can correctly recognize at first entry, candidate-pattern set, boundary of the governing entry or applicable projection function, and membership of the first-entry pattern-comparison set.

`PCP-ENTRY` reviews entry effects alongside any independently applicable `PCP-PRAG`, `PCP-MOD`, `PCP-TERM`, `PCP-NORM` or other profile.

It asks what changed in pattern selection, first-use recognition, the patterns compared at first entry, the boundary with a tempting wrong pattern, Problem-frame recognition, an expanded entry-disambiguation case, a lexical-query cue, or agreement in meaning among the affected companion or projection functions.

The default review consists of one core check with four questions.

1. **No workflow implication**
   Entry text does not imply mandatory sequence, control transfer, handoff, or
   publication, carrier, or record sequence unless another governing entry or applicable projection function
   explicitly governs that semantics.

2. **Governing-entry boundary preserved**
   Entry, index, and lexical-query companion functions do not redefine the direct pattern body's `Problem`
   or `Solution`.

3. **First honest entry-recognition function preserved**
   The change does not make the first entry-recognition function or case signal misleading.

4. **No duplicate high-detail companion or projection function**
   Does the change create a stale echo or a second high-detail companion or projection outside the pattern body or applicable projection function already named for the claim? It must not.

Limit review effort to the concern the change affects.
Learning-order edits do not trigger `PCP-ENTRY` unless they also change
candidate-pattern set, governing-entry or applicable-projection-function boundary,
first honest entry-recognition function, or first-entry pattern-comparison-set membership.
Lexical-only edits do not trigger extra entry-review scope unless they change
pattern-selection effect or entry recognition.
Retrieval fixtures are not required unless retrieval-facing behavior is
explicitly claimed, one machine-consumed projection is in scope, or one
observed misretrieval is being repaired.

When the risk warrants more than the core check, you may add only the relevant checks.

* one parity check when more than one pattern-entry
  discoverability-bearing projection changes;
* one wrong-pattern check when misclassification is observed or independently
  plausible for the intended reader under F.19's grounded-guard test;
* one lexical check when subject-language divergence is substantive;
* one expanded-entry-disambiguation-case check when a worked E.11 entry comparison changes or one high-risk
  first-entry pattern-comparison set still lacks depth;
* one public-entry check when coarse public entry wording substantively changes
  entry-selection effect or carries high public-entry risk;
* one retrieval check when the change is retrieval-facing or repairs one
  observed retrieval failure.

For a substantial discoverability change, keep one compact pattern-local note only when the governing decision needs its rationale. Use the current `DRR`, `PCP` result, patch note or other record of that decision.
One stated rationale can suffice when inspecting the governing entry or applicable projection function, partitioning the companion or projection functions, or repairing local wording already controls the risk.
It is not a separate review record unless the change is high-risk, disputed,
public-facing with substantive entry risk, or retrieval-facing.

When needed, the compact note names only the changed companion or projection function, the affected first-entry pattern-comparison set or pattern, the changed first-use recognition function or signature, and the entry or applicable projection function governing the claim or projection. Name the selected check if there is one.

Empirical evidence is required only when the change is:

* high-risk;
* disputed;
* retrieval-facing;
* repeatedly misclassified;
* public-facing with substantive entry-selection change, repeated failure, or one
  measured-improvement claim;
* or itself claims measured discoverability improvement.

Select `PCP-ENTRY-E4` only for a stated retrieval claim, a machine-consumed projection in scope, or an observed misretrieval being repaired.
Public-facing changes with substantive entry-selection risk usually select `PCP-ENTRY-E1`.
Lexical-hook changes usually select `PCP-ENTRY-E3`.
Changes across multiple projections or companion functions usually select `PCP-ENTRY-E5`.
Observed search or query failures usually select `PCP-ENTRY-E6`, optionally
together with `PCP-ENTRY-E3` or `PCP-ENTRY-E4` when the failure is lexical or
retrieval-facing.

Select only evidence modes needed for the changed entry risk. An unselected
mode requires no result row or durable disposition.
Selected evidence modes may include:

1. **PCP-ENTRY-E1 — cold-reader recognition or pattern-selection task**
   Given a real case signal, can a reader identify the pattern body that directly governs the case or an admissible set of candidate patterns?
   One short task is enough. Ask about the alternative in item 2 only when an observed choice or independent local cues make it plausible for the intended reader and the distinction changes selection or use. Otherwise omit item 2.

   ```text
   Given this entry-recognition phrase, name:
   1. the first candidate pattern,
   2. when grounded, one tempting wrong pattern,
   3. the admissible entry stop,
   4. the governing entry or applicable projection function.
   ```

2. **PCP-ENTRY-E2 — wrong-pattern and wrong-entry trap**
   For an observed or independently plausible misclassification, can the reader
   distinguish the intended pattern, entry, or family from that alternative?
   Use cues from the problem and its subject. State the rejected alternative only when F.19’s grounded-guard test warrants it.

3. **PCP-ENTRY-E3 — lexical query check**
   Does subject-domain phrasing retrieve the governing entry or applicable
   projection function without uncontrolled aliases?

4. **PCP-ENTRY-E4 — retrieval or `RAG` fixture**
   Does retrieval recover the governing entry or applicable projection function under
   exact-ID or keyword phrasing, under semantic paraphrase phrasing, and under
   projection-vs-governing-entry ambiguity, while keeping retrieved companion material,
   source faithfulness, stale echoes, and post-rationalized citation-like material distinct
   from the applicable direct pattern body?
   Retrieval returns the governing entry or intended projection cue before one
   stale echo, and answer-to-governing-entry faithfulness remains intact.
   When thin echoes are used, check that they carry a governing-entry reference.

5. **PCP-ENTRY-E5 — companion-or-projection function parity check**
   Check that the governing entry or applicable projection function is unique. The changed companion or projection functions must agree on first-use recognition, the wrong-pattern boundary and projection-only status. None may introduce a claim beyond the use admitted in the Core pattern. Wording and examples may differ. Include any stated absence in the comparison; rows may differ too.

6. **PCP-ENTRY-E6 — observed failure or query-log capture**
   Under the conditions in which the misretrieval, wrong-pattern loop or repeated query miss was observed, does the repair remove the failure?

##### E.19:4.3.1 - Reference cases for regression checks and worked examples

Select a case that exercises the changed entry risk. Cases 1–4 specialize `E.11:5.10`, `E.11:5.8`, `E.11:5.12`, and `E.11:5.9` respectively. `E.11` governs the entry-distribution use, and the direct subject patterns govern the recovered claims. Cases 5–6 add search and retrieval stress under `PCP-ENTRY-E1` and `PCP-ENTRY-E4`. Another relevant E.11 case may be used. Select empirical evidence under `PCP-ENTRY`. Unselected cases need no run or absence note.

The `tempting_wrong_pattern_or_wrong_relation` column is conditional on an observed or independently plausible reader mistake that changes selection or use. Leave it unused when that condition is absent; keep the case's positive recognition and admissible stop.

| Case | case_signal | expected_first_entry_pattern_comparison_set | candidate_patterns | tempting_wrong_pattern_or_wrong_relation | admissible_entry_stop | companion_or_projection_functions_that_help | projections_that_do_not_define_semantics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | “we need a shortlist, not one winner” | pattern-comparison set for comparison, pool treatment, and selected-set result declaration | `A.19.CN`, `A.17-A.19`, `C.18`, `C.19`, `G.0`, and `G.5` when selected-set result declaration is claimed | treating `C.11` as a one-off choice when the entry cue calls for selected-set result declaration or candidate-set stabilization | admissible candidate-pattern set stabilised or selected-set result declaration opened | README scenario or `E.11` entry-distribution cue, one pattern `Problem frame`, one expanded entry-disambiguation case if compact cues still fail | one README blurb, one thin echo, one lexical-query row alone |
| 2 | “we have a vague cue, not yet a claim” | pre-articulation cue pattern-comparison set | `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0` | forcing the cue into one endpoint-claim, quality, or assurance pattern too early | `entry-recognition-reclassified` or cue preserved for the admissible next entry-recognition function | README scenario or `E.11` entry-distribution cue, one pattern `Problem frame`, one case-linked worked entry comparison in `E.11` when needed | one coarse public entry projection alone |
| 3 | “this is the same EntityOfConcern re-expressed for another audience” | same-EntityOfConcern rewrite pattern-comparison set | `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `E.17.ID.CR` | changing the EntityOfConcern or creating a competing semantic rule track merely to serve another audience | `wrong-pattern-rejected` or same-EntityOfConcern rewrite opened | one expanded entry-disambiguation case, one pattern `Problem frame`, governing-entry pointer | a parallel explanation treated as a second pattern body |
| 4 | “the API says X” | boundary-claim unpacking pattern-comparison set | `A.6`, `A.6.B`, `A.6.C`, `A.6.P`, `C.16.Q`, `A.6.A`, `E.17` | treating a boundary phrase as an agent duty, promise, quality verdict, or generic agreement paragraph without atomic claim assignment or quality-term repair with recovered characteristic and scale | `boundary-claim-pattern-opened`, `quality-term-repair-exited`, or atomic claim set opened | one boundary-focused `E.11` entry-distribution cue, one pattern `Problem frame`, one expanded entry-disambiguation case where interface/access/confused-quality wording is common | a query cue or public entry projection treated as the governing entry |
| 5 | “I found a pattern by search, but I am not sure it is the right one” | one pattern-local recognition-signature case under the selected pattern-comparison set | a candidate for the pattern body that directly governs the case, plus a case-relevant neighbouring pattern when needed | a lexical near-match or same-family pattern that does not fit the governing entry | `non-use-confirmed` or `pattern-selected` | one pattern `Problem frame`, one `E.11` entry-distribution cue, one lexical-query hook | one search-query row alone |
| 6 | “the LLM retrieved a helpful-looking paragraph but not the pattern” | one retrieval-facing first-entry pattern-comparison case | one applicable direct pattern body plus one applicable projection function | a stale thin echo or projection-only companion used to answer as if it were the governing entry | `governing-entry-opened` or `expanded-entry-disambiguation-case-needed` | one governing-entry reference, one projection-only status marker, one retrieval-facing pointer to the applicable direct pattern body | one thin echo chunk without governing-entry reference or projection-only cue |

In case 3, evaluate episteme identity separately under `C.2.1`: its discriminators are claim content, EntityOfConcern, and effective reference scheme. Changed wording or audience alone leaves that identity unchanged; a changed discriminator identifies another episteme. `A.6.3.CR` permits claim-preserving or explicitly loss-declared same-EntityOfConcern re-expression under its own use conditions.

Selected cases test:

* entry-recognition consistency;
* wrong-pattern or wrong-entry rejection;
* admissible entry-stop honesty;
* lexical-query discipline;
* thin-echo retrieval hygiene;
* and governing-entry and projection separation in the changed entry text.

When one empirical or retrieval evidence run is selected, keep recoverable the
facts needed to understand its question and result. A structured result may use
the following field names, including only those needed by that run:

```text
viewpoint_class
task_prompt_or_query
expected_governing_entry_or_admissible_candidate_set
near_miss_patterns_or_projection_functions_if_any
time_budget_if_relevant
success_criterion_if_relevant
success_or_failure_note
observed_failure_mode_if_any
rationale_or_repair_action
```

For a retrieval check, distinguish what was retrieved, whether the answer is faithful to its source, and whether a stale echo was returned. Ordinary edits require no benchmark report.
Use the retrieval questions in `PCP-ENTRY-E4`, including its conditional
thin-echo reference check.
Ordinary local guidance stays in prose. It does not require a stable governing-entry reference by default.

##### E.19:4.3.2 - Additional questions for the selected review concern

Open a common hardening question when the concern has FPF-governed use, is disputed, or the reviewed pattern or subset expressly calls for it. Inspect the relevant source and the reviewed loci. In inspect-repair-verify, repair any defect and verify the affected use. In independent findings, record the defect and repair direction. When the question reveals no defect, make no durable absence or pass recital.

Use these questions only for the selected review concern:

1. **Usability and working-reader fit.** Open this when first-reading recognition text, assurance text, first-minute working-reader usability, practical payoff, worked slices, primary-reader fit, or `E.8` / `E.12` / `E.13` / `E.14` / `E.17.*` / `F.16` checks can change the admission or refresh result. If a separate evaluation assigns a value, use that evaluation's result rather than copying it into E.19 findings.
2. **Scenario, anti-case, and utility-fit source set.** Open this when a scenario pack, anti-case corpus, pilot bank, utility tree, fitness catalog, or analogous source is relevant to the case or substantively disputed. Record only a missing, misused, or failing source/case as an E.19 finding.
3. **Packaging, concrete pattern contribution, package relation, and shipping fit.** Open this for a publication, pattern-contribution, or package-relation claim. The changed sources and governing publication or release result carry successful alignment; E.19 repairs or reports a mismatch.
4. **Domain-tightened profile depth.** Open this when a domain-specific note tightens a selected profile. Apply its questions; do not add a second account of positive results.
5. **Accepted-decision or accepted-source-material carry-through.** Open this when the reviewed pattern, subset, or current change is claimed to implement an accepted `DRR`, repair findings, intake material, architecture source material, or other accepted source material named by value. Inspect each independently applicable decision against the reviewed loci and the concrete pattern, claim, companion, result, or accepted source that carries it; require exact predicate or defining `ClaimGraph` identity only when that decision or the named reliance needs it. Repair or report partial, missing, wrongly rejected, wrongly routed, or wrongly classified carry-through. The accepted source remains the decision source; E.19 does not duplicate decisions that are expressed sufficiently, inherited unchanged, correctly absent, or outside the reviewed subset. An `E.17.ID.CR` comparative review unit, `PublicationUnit`, publication form or face, source-pinned interpretation case, source material, or project-side review relation retains its own kind in that comparison.

6. **Decision-useful advice and evidence demands.** Open this when a pattern's advice, feasibility or evidential burden is in question and can change the review result. Use `C.11.DUA` to recover the demanded work, compare its attainable contribution and burden, and examine a disputed requirement's merits and force. Follow the selected method through its result, prescribed fields and stopping point: retain the useful basis and any explanation the decision or recipient needs, while inactive inquiry creates no omission account. A worthwhile evidence demand remains. Apply `F.19` to wording that needs repair; this question adds no universal profile or second language pass.

For `PCP-ENTRY`, the ordinary compact pattern-local change note remains enough when the governed discoverability decision requires one; no separate E.19 account is required for checking the profile.

##### E.19:4.3.3 - Pattern-Edition Use-Value Replay

Use this replay when an exact candidate pattern edition changes materially under `E.8:4.1.2`. Run it once on the stable candidate before acceptance or landing. Start with the bounded E.8 loop over the actual predecessor and proposed prose, then open only each affected prior-edition or candidate-only use whose result can differ, pinned to its exact basis and changed locus.

Treat a change as mechanical only when the smallest relevant comparison shows that every materiality value named in `E.8:4.1.2` is preserved. A genuinely bounded local semantic edit opens only its affected use probe and changed wording group; the physical size of the rewrite does not establish its scope.

When the candidate keeps, merges, removes, profiles, reuses, externally supplies, or omits a narrower contribution, apply the same-situation decision in `E.8:4.1.3`. If reuse or a gap answers the working question, establish what is returned: a result of its own kind from the supplying product, a MethodDescription reference, direct-source evidence, or a named unavailable result. For an external result, verify the exact result and supplying product, receiving use, practical discovery route, material currentness or availability, and the statement that it remains outside the receiving framework; state maintenance only when it changes that use. Otherwise the package still has a gap or omission.

When the resulting stable set materially changes a promised problem family, verify the current `E.4.DPF.DA` D12 judgement for the resulting exact edition required by `E.8:4.1.3`. Reuse a matching current result when the exact edition, promised families, declared use, relied-on results, and relevant conditions did not change; E.19 asks for neither a duplicate package evaluation nor evidence that a revisit occurred.


Judge each affected use probe separately when its result can differ by exact predecessor or candidate-only basis, working use or relying work, expected first useful result, boundary, necessity, or evidence mode. One review may contain probes from both bases.

A grouped verdict such as `uses preserved or added` or `usability preserved` cannot substitute for those judgements. Inspect and repair a failed probe in repair mode, then verify it. In independent review, record only regressions, insufficiencies, invalid transfers, unsupported decisions and blockers. Neither form requires a per-probe progress record. When `E.8`, `E.21`, or another governing evaluation requires reusable dispositions or values, keep them in that evaluation's result rather than copying them into E.19 findings.

**Changed-wording check inside each affected prior-edition probe.** Keep the selected use probe as the outer unit. When a predecessor-bearing candidate materially rewrites a normative sentence or inseparable sentence group that carries the governed extension, action discriminator, first useful result, stop, or neighboring-pattern exit, judge that wording group under the dispositions below before closing the use probe. Keep sentences together only when they serve one reader task and must receive one disposition; split them when their extension, action, result, or route can differ.

For each changed wording group:

1. pin the old and candidate wording and the exact use it serves;
2. state in plain language the subject, concrete action or choice, visible result, and any stop or exit the use needs;
3. compare the old and candidate head and modifiers, modal force, admitted referents or actions, applicability boundary under its governing rule, and local interpretation burden. Check every widening or narrowing against that rule and the accepted change decision, independently of the reader-plausibility question in the next step;
4. if independent local evidence makes one rival reading plausible to the intended reader and its treatment can differ, test that case. Use the plausible-reader test to decide whether an explicit guard contributes to the final wording; the extension comparison remains required. Do not invent an alien or excluded case to fill the review form; and
5. apply the differential disposition. `preserved` requires no unauthorized widening or narrowing and no greater decoding burden: a reader must not need campaign memory or an ontology-development memorandum to recover the action.

For a new action-guiding paragraph with no predecessor, do not invent history or a foil. Verify that the local wording exposes a recognizable situation, concrete action or choice, visible first result, and any independently grounded applicability or neighboring-pattern boundary needed for use.

Formatting, typo, link, citation, or exact-reference corrections remain mechanical when the smallest comparison proves that no `E.8:4.1.2` materiality value changed. A bounded semantic edit checks only its affected wording group and use probe. Reuse an earlier hunk or language result only when the object and compared editions, changed scope, and assurance question match this extension, modal-force, applicability, and interpretation-burden test; idea presence or broad-use preservation is not enough. Complete the review in the same increment on the stable candidate before acceptance or landing. It requires neither per-edit review nor a new ledger, and the first finding does not trigger a handoff.

**Prior-edition differential.** For one candidate pattern edition × one prior-edition use probe, distinguish the applicable disposition when the governing decision needs it:

| Disposition | Semantic test and recoverability |
| --- | --- |
| `preserved` | The situation, action, result, and any action-changing boundary carried by the prior use remain semantically available; every material changed wording group retains its head-and-modifier extension, modal force, admitted valid cases, valid rule-defined exclusions, and no-greater-decoding-burden condition. The declared use remains admissible and replayable from the pinned editions. |
| `improved` | The required old use and every required changed-wording boundary remain preserved, and the same bounded comparison also demonstrates an action, result, boundary, affordability, or interpretation-burden gain. |
| `transferred` | A discoverable handoff reaches one named neighboring pattern whose Solution carries the needed action guidance and exposes its result. A bare pattern ID or unreachable action is `regressed`. |
| `intentionally retired` | An accepted decision drops a harmful or false old action and supplies the corrected positive action or boundary as the recoverability endpoint. |
| `regressed` | A required action, result, risk disclosure, cheap exit, or usable handoff is absent; or changed wording changes modal force, widens or narrows admitted referents or actions without an accepted basis, alters a rule-defined applicability boundary, or makes the reader decode more unstated ontology. Repair or an explicit retirement decision is required. |

A use classified as unsupported historical residue before replay receives no differential disposition and supports no compatibility claim. New evidence of a valid old use reopens that classification instead of restoring wording silently.

A required `regressed` probe prevents a positive conclusion, but it does not stop inspection of the remaining independent probes.

**Candidate-only adequacy.** Review one candidate pattern edition × one new intended-use probe against its exact candidate-only basis, never against invented history. Distinguish these outcomes when the governing decision needs them:

| Outcome | Semantic test |
| --- | --- |
| **adequate for the candidate-only use** | The selected basis, recognizable situation, concrete action or choice, first useful result, intended reader, and any independently grounded action-changing boundary are recoverable from the local candidate wording and executable enough for the declared use. |
| **absent or insufficient for the candidate-only use** | The use is only promised, named, over-broad, ambiguous, or unsupported; the intended reader cannot perform the action, distinguish the first result, or recover an applicability or neighboring-pattern boundary that the declared use needs. |

A missing candidate-only decision or basis is `absent or insufficient`; it never licenses a fabricated prior edition. Absence for a required new use prevents a positive conclusion but does not stop the other independent probes. Missing optional breadth alone does not block a positive conclusion. It provides no grounds for breadth, transfer or exceptional-expression claims. If no exact new intended use is selected, no candidate-only check opens.

**Replay the positive Solution separately.** Judge the following over the candidate edition when their answers can differ:

1. the governed subject;
2. the recurring problem and ordinary failure;
3. an executable proposed move;
4. a first useful result rather than completed review apparatus.

**When the Solution uses a boundary or guard.** Judge each guard for which independent local evidence makes the exact rival reading plausible to the intended reader and whose presence changes action. Check whether any remaining guard merely supplies the outline that the positive Solution should state directly. Refine this question by boundary whenever boundaries can pass, fail, or route independently. This guard check leaves the rule-defined extension comparison above intact.

**When the Solution concerns a Method, work, or world-side change.** First distinguish content that defines, constrains, tests, or guides from an assertion of one actual occurrence. Method guidance alone triggers no fictive performer or Work. When an account asserts dated `U.Work`, verify the §4 actual-Work account; when it asserts a world-side change, identify the change relation, the pattern that defines it, and the things it relates. Keep the intended-reader position, any qualifying A.3.2 method-description episteme, actual performer, Work, and problem-facing result separate. A literal dated-Work claim is defective if an episteme, checklist, plan, prose, or intended-reader or representation position performs Work. Judge ordinary metonymy through `F.19`.

Follow the short first-use rendering's action and result logic against a concrete situation. Finding labels such as `situation`, `move`, `result`, or `stop` does not show that a reader can use the instruction. Repair each failed item or record it as a finding that identifies the failure and how to repair it; do not replace the replay with one prose-quality impression.

**Replay each triggered enumeration or coordination under `F.19`.** Apply its contribution, coordination/list, and foregrounding rules in `F.19:4`, including the return to a defining or testing pattern when an FPF kind, relation, or structure remains hidden. Review a member separately only when its membership or contribution can fail independently or require a different repair. An unchanged series covered by the same rule needs no positive entry. A blanket `all lists are coherent` conclusion cannot replace the reading.

Desk replay is the ordinary evidence mode for affected uses, changed wording groups, new action-guiding paragraphs, the positive Solution, and enumerations. Escalate to a cold reader, AI agent, or observed-work exercise when competing actions remain plausible, a near-miss boundary or result distinction is not recoverable by inspection, a transfer is uncertain, or a missed failure has high consequence.

When a claim extends recurring applicability beyond the exact cases, do not treat three examples alone—the traditional rule of three—as validation. When the claim's value or consequence warrants it, select a proportionate qualitative practitioner survey, action-research cycle, or case study. Select the additional evidence by risk. It is not a universal benchmark or a requirement for an ordinary rewrite. E.19 defines repair or finding outputs while leaving ordinal coordinate values and `PatternQualityStatus` to the full E.21 evaluation.

#### E.19:4.4 - Decision outcomes

Complete the selected review scope before making an admission, refresh, or return-for-repair conclusion. A first defect or already-negative conclusion does not end the search for other independently obtainable findings. If a condition makes the remaining questions impossible to judge truthfully or safely, report a partial result and identify the unexamined scope and the condition that prevents its review.

**Inspect, repair, and verify.** Complete every in-scope review application, repair every defect through the relevant authoring work, and perform focused verification over the affected questions. The changed pattern edition and focused-verification claims are the substantive evidence and remain distinct from the work that produced them. Constitute one aggregate E.19 result episteme only when a receiving admission/refresh decision needs it. Record only an unresolved blocker, a decision outside current authority or work that must transfer. Completed repairs need no parallel list.

**Independent findings.** Leave one compact C.2.1 findings-result episteme or handoff file containing all actionable in-scope defects and blockers, ordered by semantic impact, with repair direction precise enough that the author need not rediscover the diagnosis. If the selected questions reveal no defect, create neither an empty pass report nor positive checklist recital. The findings result is not the dated review work or an authority-bearing admission decision.

If a governing admission, refresh, `E.21`, `DRR`, publication, or release decision requires a durable conclusion or value, use its existing result. That result may cite E.19 findings or the repaired candidate; it does not turn per-question positive outcomes into a second review record.

**Precision-remediation order.** When a defect sentence combines a generic head, a claim-bearing qualifier, and pressure to compare values on mixed criteria, remediation SHOULD follow the precision-before-coarsening rule in `F.19:4`. That rule supplies the head/qualifier/comparison order and the recoverable precise interpretation required for a later Plain, didactic, or coarsened restatement.

**Kind-restoration verification.** A wording, naming, or F.19 phrase-level repair does not succeed merely because the old trigger word disappeared. Compare both versions for object kind, relation or claim kind, admissible use and scope. If the repair narrows, widens, splits, or changes them without an accepted decision, repair it or keep the defect unresolved. The repaired object, focused verification, or governing decision carries this evidence; E.19 does not require a per-repair pass account.

**Ordering and effort.** Put ontology, semantics, modularity, and SoTA defects in FPF-governed sections before compact low-signal formatting findings. If semantic defects are present, address them before mechanical edits; formatting and micro-typos must not dominate the work by volume.

