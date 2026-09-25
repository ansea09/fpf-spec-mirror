---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "Affordance and Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:4"
section_title: "Solution - Recover the claim, apply its subject rule and return sufficient wording"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__005_solution-recover-the-claim-apply-its-subject-rule-and-return-sufficient-wording.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.6.A — Affordance and Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:4 — Solution - Recover the claim, apply its subject rule and return sufficient wording"
line_start: 19333
line_end: 19627
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.3"
  - "A.6.B"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "action-first language"
  - "affordance"
  - "detection"
  - "inquiry question"
  - "physical opportunity"
  - "wording recovery"
---

### A.6.A:4 - Solution - Recover the claim, apply its subject rule and return sufficient wording

#### A.6.A:4.0 - Trigger rule

Use A.6.A when the intended claim or question remains unclear for the receiving use. The following cues help locate that ambiguity:

* the prose uses tokens such as **affords**, **invites**, **calls for**, **actionable**, **ready for**, **ripe for**, **natural next step**, **the model wants**, **the interface tells**, **this problem asks for**;
* a boundary, gate, incident note, design note, or review note uses such language for admission, selection, triage, or action guidance;
* different traditions are compared using the same action-first wording;
* a draft introduces *model affordance*, *interface affordance*, *actionable insight*, *policy invitation*, or *ready for formalization* without declared sense;
* the author intends the phrase to carry more than one of: situational action opportunity, latent cue, operator move, probe move, closure move, or control move.

#### A.6.A:4.0a - Operational repair sequence

1. **Recover the occurrence and receiving use.** Read the trigger sentence with its source context. State which interpretation, decision or action the reader needs it for.
2. **Compare the live interpretations.** Consider a physical opportunity, its detection, an operator prompt, a social response, a candidate inquiry, a proposed clarification, a learned policy tendency or a control option. Also consider an actual evaluation, ability, commitment or Work claim when the sentence supports that reading. Use §4.3 as a menu, not a required classification.
3. **Select what the grounds support.** State the intended interpretation and why a consequential rival is excluded. If the grounds do not choose, preserve the rival meanings and return the fact or question that would distinguish them. A short note is useful when a later decision needs those grounds; it is not a prerequisite to every repair.
4. **Recover the subject and relevant conditions.** Name the actual site, would-be actor, action and other participants only to the extent that they determine the claim. For an obtaining relation, recover its direct predicate and any needed occurrence identity under A.6.REL. For an inquiry, state the question and what an answer would resolve. A menu label supplies neither result.
5. **Express the first useful result.** Return a sufficient ordinary sentence, supported bounded claim, explicit question or exact missing basis. Use one of §4.5's optional forms only when the receiving use needs it. Separate a detector, viewpoint, source or representation when that distinction changes the result.
6. **Continue from that result.** Apply the subject pattern for a needed evaluation, Method selection, WorkPlan, actual Work, authority, gate or evidence claim. Use A.6.B for the actual boundary-bearing claim. Stop when the receiving question is answered; wording recovery creates no extra invitation occurrence to establish first.

#### A.6.A:4.1 - Recognition and assurance answer different questions

The first result is recognition of what the sentence means. Establishing the recovered claim then uses that subject's rule and evidence. An intelligible physical-opportunity claim can still lack support; an intelligible research question can be useful while its answer is unknown.

Use `A.16.1` or `B.4.1` when the cue cannot yet support a particular claim or question. When articulation is sufficient, express the recoverable content without requiring a relation record or a sense token. Any relevant `AE` or `CD` reading concerns the account and its next use; it does not establish a physical opportunity.

If an account later becomes unsupported, revise or withdraw it through the applicable subject pattern and A.16.2. With physical conditions fixed, changing its wording, carrier or detector establishes no beginning, ending or new occurrence of the physical opportunity. If information itself is constitutive under a source-specific relation predicate, use that predicate and its identity rule for the corresponding change.

#### A.6.A:4.1a - Optional recovery note

When a receiver needs a reusable account of the repair, a note may contain:

```text
trigger and source context
recovered statement or question
receiving use
participants and conditions that determine the result
subject rule and supporting sources, or the exact missing basis
material rival interpretations and their disposition, when needed
detector, viewpoint, representation and publication details, when relevant
next subject result or return, when one is needed
```

This is a way to express the result. It neither declares a common relation kind nor supplies an obtaining predicate. For an actual relation claim, its participants, direction, applicability, evidence requirements and same/new rule come from that relation's direct governor. Recover ref-backed participants and by-value content under A.6.5 when the note itself is changed.

Omit fields that do not change interpretation or use. A sufficient sentence remains a complete result. A particular receiving publication can require more structure under its own conditions; that requirement does not become a universal prerequisite to wording recovery.

**Viewpoint and view discipline.**
When `viewpointRef` is present, `effectiveReferenceScheme` is also explicit and the reference resolves under that scheme to one exact independently admitted `U.Viewpoint` episteme. `view` is a separate optional value: it names one independently identified C.2.1 episteme that already has `U.View` membership only because exact E.17.0 `EpistemeViewpointConformanceRelation(view, viewpoint)` obtains for at least one admitted viewpoint. The selected `viewpointRef` need not be the viewpoint to which an optional view conforms unless the record explicitly claims that relation. Including `viewpointRef` or `view` in a recovery note establishes neither `U.Viewpoint` nor `U.View` dependent-kind membership; it only cites already established objects. Detector, viewpoint selection, view membership, viewing construction and publication remain separate.

A sentence such as “X affords Y” needs repair when its intended action, participants or basis remain hidden for the receiving use. For a recovered relation claim, apply A.6.REL; for a recovered question, preserve the question. Earlier cue content may remain a cue pack, RoutedCueSet or another appropriate expression.

**Interpretation and enactment.**
The menu label records a candidate reading of the wording. It does not identify an occurrence or establish that different interpretations have one relation kind. A proposed action is not an actual `U.Work` or a `U.WorkPlan`. When the result selects a Method for enactment, name the exact independently admitted `U.Method`; any `methodDescriptionRef` remains a separate source episteme. Use **A.15.2** for intended-work planning and **A.15.1** for actual Work. Route an already returned result or Work consequence through **A.15.1 §4.6** or its direct result/measurement governor: distinguish the application result binding, returned value, any independently established evaluation Work, and a result episteme when one is needed. A Work-to-result claim needs its own declared domain predicate; a missing predicate returns the named gap while leaving an independently established application binding usable.

**A.7 boundary note.**
When the site affects interpretation, distinguish an EntityOfConcern-side participant, a Description episteme participant and any non-claim-bearing site kind. Name a participating publication face, publication form, carrier or rendering separately under A.7. An optional note may use `siteClassification` and `publicationOrCarrierParticipation` for these distinctions; ordinary wording can express them too.

**Separation note.**
`detector` and `invitedEnactor` are not synonyms.
When both matter, they SHALL be published separately.

**Enactor note.**
When the recovery result names an actual would-be enactor, that enactor SHALL resolve to a `U.System` or to a role assignment whose holder is a `U.System`. An episteme, description, publication face, or carrier may participate in the **site**, but not as the acting bearer.

**Episteme non-agency note.**
If the site is a Description episteme, any later enactment still occurs through carriers, acted-on systems, or both; the description itself never acts.

#### A.6.A:4.2 - Candidate interpretations

The `ActionInvitationSense` menu in §4.3 is a discovery aid. Its `AIS.*` labels can help compare interpretations or preserve search terms; using a label is optional. Choosing one label does not assert one common `actionInvitation` relation or impose common obtaining and identity conditions on the listed subjects.

For a consequential interpretation, recover the source-local meaning, the participants and action it concerns, the conditions under which the claim would hold, and the result the receiving use needs. Keep an unresolved interpretation as an alternative rather than assigning a default because the sentence occurs in an ecological, interface, control or research context.

If a local practice needs a named interpretation profile, it may specify applicable sites and actors, action structure, relevant substrate, admissible evidence, forms of expression, change conditions and cross-context use. Such a profile describes that local recovery use. A relation declaration, Method or commitment still needs its own independently applicable rule.

#### A.6.A:4.2a - A.16 articulation-token relation note

A recovery note may carry `articulationHint` as a **local articulation-cue field** when the receiving use needs it.

This field is deliberately **not** a new formality progression, **not** a maturity scale, and **not** a surrogate for **F**. Its only job is to preserve local articulation and closure cues until they can be related to `A.16` move logic and the explicit `C.2.4` and `C.2.5` governing facets.

Local `articulationHint` tokens SHALL be related to `A.16` move logic and to the explicit `C.2.4` and `C.2.5` governing facets one-for-one, and A.6.A SHALL treat them as local publication cues only.
Until then, local hints SHALL NOT be thresholded, aggregated, or compared across Contexts.

#### A.6.A:4.3 - Interpretation menu
Consider these candidate meanings and any source-local alternative that can change the result. The menu helps recover a claim; it does not select its truth conditions by classification.

| `ActionInvitationSense` token | Use when the action-first phrase means…                                                     |            Possible useful form | Typical substrate                                    | Must **not** be silently collapsed into                  |
| ----------------------------- | ------------------------------------------------------------------------------------------- | -----------------------------: | ---------------------------------------------------- | -------------------------------------------------------- |
| `AIS.PhysicalAffordance`      | a physical or environmental configuration offers a bodily action to an embodied agent       |    `CuePack` or `ActionOption` | `ecological-world-coupled` or `embodied-kinesthetic` | site-participant property alone, generic capability, executed work |
| `AIS.InterfaceAffordance`     | an operator-interface element, operator panel, alarm, or publication face presents an operator move | `ActionOption` or `PolicyHook` | `symbolic-local` or `hybrid`                         | duty or commitment, execution log                           |
| `AIS.SocialAffordance`        | another agent or social situation invites a response or coordination move                   |    `CuePack` or `ActionOption` | `embodied-kinesthetic` or `hybrid`                   | role assignment itself, deontic commitment               |
| `AIS.EpistemicProbe`          | a problem situation invites asking, contrasting, measuring, testing, or instrumenting       |  `ActionOption` or `OptionSet` | `hybrid`                                             | explanatory merit, evidence claim, finished method       |
| `AIS.ClosureAdvance`          | a situation invites naming, rescoping, proxy declaration, or formalization toward closure   |                 `ActionOption` | `symbolic-local` or `hybrid`                         | Formality **F**, acceptance status, quality ascription   |
| `AIS.LatentPolicyCue`         | a learned or distributed state carries an action-oriented tendency not yet locally articulated |       `CuePack` or `OptionSet` | `latent-distributed` or `hybrid`                     | explicit rationale, control adequacy, quality claim      |
| `AIS.ControlOpportunity`      | a closed-loop state invites braking, rollback, replanning, isolation, escalation, or override |    `OptionSet` or `PolicyHook` | `hybrid`                                             | bare “model wants”, obligation, work occurrence          |

**Using the menu.**

* In **ecological and embodied** contexts, consider the physical-opportunity reading, while checking whether the claim instead concerns its perception or detection.
* In **operator-interface, alarm, or operator-panel** contexts, consider the interface-prompt and control-option readings, retaining both only when the sentence makes both claims. If the wording instead claims module interface, functional port, API, protocol, signature, interface specification, or service-access compatibility, use `A.6.RSIR`, `A.6.M`, `A.6.F`, or `A.6.0` according to the recovered EoC rather than treating the cue as an action invitation.
* In **epistemic exploration** contexts, "this suggests probing, formalizing, or reframing" can mean an inquiry question, candidate investigation or proposed clarification. Recover that result directly.
* In **learned world-model, active-inference, or policy** contexts, consider a learned policy tendency and a control option as different readings. A model state does not by itself establish a control decision, duty or performed action.
* If the sentence is chiefly about **better, worse, fit, or merit**, use **C.16.Q** instead of A.6.A.

#### A.6.A:4.4 - Recover details that change the result

Use the following questions where their answer changes the recovered meaning or its use. They are not ten fields that every sentence must populate:

1. **Site tuple and site classification.**
   Site tuple members: named EntityOfConcern, scene, interface element or front-end element, Description episteme, episode, control state, or non-claim-bearing site kind - with publication or carrier participation stated separately when live.

2. **Invited enactor tuple.**
   Which `U.System`, collective system, or role assignment whose holder is a `U.System` is invited to act.

3. **Candidate action tuple.**
   What action or inquiry the phrase concerns. If the result selects a Method for enactment, identify its exact `U.Method`; keep any MethodDescription, WorkPlan and actual Work separate under their direct rules.

4. **Intended meaning.**
   Which interpretation the context supports, and which consequential rival remains or is excluded. An `AIS.*` label is optional.

5. **Coupling frame.**
   The actual conditions and, where applicable, coupling relation on which the recovered claim depends; recover their rule rather than treating their names as proof.
   Examples: reach envelope, interface state, incident horizon, control horizon, probe pack, open issue set.

6. **Detector, viewpoint reference, and independent view.**
   Who or what detected the cue; which exact viewpoint episteme `viewpointRef` resolves to under the effective reference scheme when a viewpoint is selected; and, independently, which already-conforming `view : U.View` is cited when a view itself participates. None follows from another.

7. **Normal form and `articulationHint`.**
   Whether a particular expression form or articulation cue changes what the receiver can recover or do.

8. **Scope and time when relevant.**
   `U.Scope` and `Γ_time` SHALL be explicit when omission changes meaning.

9. **Representation substrate when relevant.**
   Especially when comparing ecological, embodied, latent-distributed, and symbolic-local treatments.

10. **Witness mode and evidence references.**
    Exemplars, sensory traces, probe notes, kinematic data, interface events, controller traces, run logs, or review notes.

#### A.6.A:4.5 - Normal-form discipline

Use a sufficient ordinary sentence first. The four forms below are optional ways to preserve cues, present a candidate, compare alternatives or refer to an existing policy. Select one only when it contributes to the receiving use; no sense token requires a default form.

**Docking note.**
Where the recovered result selects a Method for enactment, cite the existing exact `U.Method` ref. A current `U.MethodDescription` ref remains a separate C.2.1 source for identifying, constraining or justifying that Method or intended Work; existing `U.WorkPlan` and `U.Work` refs remain separate when those objects already exist. `PolicyHook` SHALL always be a hook over pre-existing gate, method, or protocol publications; it does not mint a new Method, execution, admissibility, or deontic ontology.

**ANF-1 — `CuePack`.**
Use when preserving an early or incompletely articulated cue is the useful result, including `AIS.PhysicalAffordance`, `AIS.SocialAffordance`, and many cases of `AIS.LatentPolicyCue`.

A conforming `CuePack` publishes:

* exemplar or contrast episodes, sensory traces, or probe cues,
* site conditions,
* enactor descriptor or enactor constraints,
* a small gloss set of candidate actions,
* optional ordinal urgency or salience summaries,
* explicit warning that the cue is **not yet** a commitment, a selected method, a gate, or work,
* explicit note that witness-bearing does **not** by itself make the hinted action correct, required, or selected.

**ANF-2 — `ActionOption`.**
Use when one candidate action tuple is explicit.

A conforming `ActionOption` publishes:

* one candidate action tuple,
* invited enactor and role assignment when live,
* local guard sketch,
* expected near-field effect,
* an exact `U.Method` ref when the option selects that Method for enactment, plus a separate optional `U.MethodDescription` ref or `U.WorkPlan` ref only when that independently existing object is current,
* explicit note that the option is **not yet selected**, **not yet obligatory**, and **not yet executed**.

**ANF-3 — `OptionSet`.**
Use when several candidate actions coexist.

A conforming `OptionSet` publishes:

* explicit action members,
* any local comparator, triage rule, or partial order,
* admissible incomparability if no total order is admissible,
* prohibition on hidden scalarisation.

**ANF-4 — `PolicyHook`.**
Use when the receiving use needs an explicit reference to an existing controller, gate, playbook, Method or override protocol.

A conforming `PolicyHook` publishes:

* referenced policy, method, gate, and protocol ids (pre-existing governing FPF patterns or `authoritySourceRef` named sources only),
* applicable guard or trigger conditions,
* admitted acting or maintaining System; any exact system-role kind or assignment needed by the hook's work context; the direct responsibility relation that selects that System, or the exact A.6.RCD missing governor; and any separate `authoritySourceRef` source,
* escalation or override references when relevant,
* explicit note that the hook is a **binding publication** over existing semantics, not itself a commitment, an admissibility rule, or a work occurrence.

#### A.6.A:4.6 - Separation from quality, capability, commitment, and work

A.6.A SHALL prevent the collapse of action invitation language into neighbouring families.

* A statement about **better, worse, fit, or merit** belongs to **C.16.Q**.
* A statement about **what a system can do in general** belongs to capability wording, method wording, or method-description wording under **A.6.F** and the subject pattern for the asserted capability, method, or method-description claim.
* A statement about **what must be done** belongs to **A.6.B** when the wording asserts an A-classified admissibility claim or a D-classified commitment claim.
* A statement about **what was actually done** belongs to **A.15** and exact dated `U.Work`, whose `enactsMethod` relation points to the exact `U.Method`.
* A result that selects a Method identifies that Method without becoming a plan or occurrence; any `methodDescriptionRef` remains auxiliary. A proposed action can remain a proposal without inventing its Method. A Description episteme never acts and is never what Work enacts.
* When a sentence carries both evaluative and action-oriented content, make the two claims and their respective grounds distinguishable. Use linked records only when the receiving use needs them.

Two clear clauses or sentences may suffice.

Examples:

* “This scene is good for grasping” can combine a physical-opportunity claim with an evaluation under a particular criterion. Recover each claim and its rule.
* “This alarm requires rollback” needs the actual gate or duty rule, if that is the intended claim.
* “The robot can grasp this handle” can concern ability under conditions or a situated physical opportunity. Recover which result the reader needs and apply its rule.
* “The operator clicked rollback” is work, not invitation.

#### A.6.A:4.7 - Bridge discipline across traditions

Whenever two traditions are compared using action-first language, first ask whether the comparison asserts or relies on semantic correspondence between exact senses in different semantic contexts. If it does, resolve those senses and test F.9; cite an obtaining Bridge only when its direct predicate is true, and state a separate bounded-use claim only when a proposed use is live. That claim carries the use, direction, correspondence rule, tolerated loss, and polarity. If the comparison does not assert or rely on that correspondence, use E.17.ID.CR for bounded comparative review or the exact direct relation that supplies the contrast, then stop. Add an F.9.1 stance note only as optional reader help for an already constituted bounded-use claim.

Useful stance labels include, for example:

* **`localRename`**
* **`operationalizes`**
* **`partialAnalogy`**
* **`projection`**
* **`nonEquivalent`**

Examples:

* A named comparison between `AIS.PhysicalAffordance` and `AIS.InterfaceAffordance` may remain a direct bounded contrast under E.17.ID.CR or another exact direct relation. If it asserts cross-context semantic correspondence, any bounded partial analogy needs an obtaining F.9 Bridge and a matching use claim. An optional `partialAnalogy` note helps reject identity; the label alone establishes nothing.
* `AIS.EpistemicProbe` and `AIS.ClosureAdvance` usually need the direct progression-by-closure relation that is actually claimed. If their senses cross semantic contexts, apply F.9 before adding any optional stance note.
* A named use from `AIS.LatentPolicyCue` toward `AIS.ControlOpportunity` needs F.9 only when it relies on cross-context semantic correspondence; then any operationalization or projection reading follows the obtaining Bridge and the use claim's direction, rule, and tolerated loss. Otherwise the exact direct relation must supply the proposed contrast or use.
* A robotics comparison from `AIS.PhysicalAffordance` toward `PolicyHook` may remain a direct contrast. If it relies on cross-context semantic correspondence, a projection reading requires the obtaining F.9 Bridge and a matching bounded-use claim under the controller frame; an F.9.1 note only explains that existing claim.
* Action invitation and quality ascription may co-occur, but co-occurrence is **not** identity.

#### A.6.A:4.8 - Change lexicon

When a recovery note changes, state what changed. The following verbs are useful descriptions, not a required common operation signature:

* **`publishRecovery(...)`** — publish the recovered claim, question or missing basis.
* **`withdrawRecovery(...)`** — withdraw that account.
* **`retargetSite(...)`** — change the named site in the account, applying the subject identity rule separately when an occurrence claim changes.
* **`retargetInvitedEnactor(...)`** — change the invited enactor tuple when that slot is ref-backed.
* **`reviseAction(...)`** — change the candidate action tuple by value (or split into the corresponding `retargetParticipant(...)` form if the account declares that action slot as ref-backed).
* **`reviseSense(...)`** — change the interpretation attributed to the wording; state the resulting change in the claim.
* **`reArticulate(...)`** — change the articulation cue while preserving the recovered meaning.
* **`reFrame(...)`** — change coupling frame.
* **`reGuard(...)`** — change guard sketch or hook condition.
* **`rePolicyHook(...)`** — change policy, gate, or method hook details.
* **`reView(...)`** — change detector publication, ref-backed viewpoint selection, or independent view inclusion under the declared ref-vs-value discipline. Changing `viewpointRef` does not mutate the viewpoint episteme; adding or replacing `view` does not establish E.17.0 conformance.
* **`rescope(...)`** — change `U.Scope`.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnesses(...)`** — refresh witness bindings.
* **`changeRelationKind(...)`** — use only when an actual relation-kind claim changes under its direct governor. A different interpretation of wording need not be a change of relation kind.

These operations describe changes to the account or its publication. For any claim that the opportunity itself began, ended or became a different occurrence, apply its direct obtaining and identity rule; record declaration, withdrawal, wording and detector changes do not supply that result. A silent move from invitation to commitment, capability, or work is a breaking semantic change.

**A.6.P rewrite note.**
`retargetSite(...)` and `retargetInvitedEnactor(...)` describe participant retargeting in an account and SHALL be used only when the corresponding slots are ref-backed. `reviseAction(...)`, `reviseSense(...)`, `reArticulate(...)`, `reFrame(...)`, `reGuard(...)`, and `rePolicyHook(...)` are by-value revisions unless the account explicitly declares the corresponding slot as ref-backed, in which case the text SHALL use the matching `retargetParticipant(...)` form. This preserves A.6.5’s ref-vs-value discipline.

#### A.6.A:4.8a - Classify the recovered boundary-bearing claim

When the recovered claim is boundary-bearing, use its actual A.6.B classification:

* **L** — the rule that defines or constrains the recovered subject, including an actual relation predicate when that is the claim; applicable enactor/site discipline and the F.9/F.9.1 boundary retain their direct governors.
* **A** — admissibility conditions for the recovered result in selection, triage, automation or publication.
* **D** — a generic prescription with its exact normative episteme and applicable content, such as the rule to name the invited actor or required authority/override source. An asserted individual duty or commitment additionally needs its own obtaining basis; a generic prescription does not invent that individual occurrence.
* **E** — an exact adjudicable claim about actual Work, an evaluation or observation result, or a produced carrier’s condition under A.6.B. Cite the relevant sensory result, event, probe or log as its evidence; a list of trace or carrier references is not itself the E claim.

Do not let bare action-first language carry L-, A-, D-, or E-classified claims, admissible-use consequences, or evidence consequences by itself.

#### A.6.A:4.9 - Lexical guardrails

In **Tech prose and normative prose**:

* bare **affords, invites, calls for, actionable, ready for, ripe for, natural next step, the model wants, or the interface tells** MUST NOT appear without immediate repair;
* **actionable insight** MUST be made precise as the actual claim, candidate action, question or missing basis; use **C.16.Q** when the claim is evaluative;
* **affordance** MUST NOT be treated as a monadic property of a site participant without enactor, site, and coupling frame;
* an invitation MUST NOT be presented as if it were already a duty, gate, or work occurrence;
* a latent policy cue MUST NOT be presented as if it were already an explanation;
* `articulationHint` MUST NOT be treated as **F**, as acceptance status, or as a replacement for `A.16` grounding references;
* generic `Surface` facet tokens MUST NOT be introduced inside A.6.A; publication face, publication form, interop publication form, carrier, or rendering participation must be declared under A.7 and publication-face and publication-form discipline, not by widening the site classification;
* hidden enactor language inside adjectives such as *graspable*, *deployable*, *actionable*, *ready* SHALL be unpacked;
* quoted metalinguistic uses are allowed, but SHALL be marked as token-under-discussion.

#### A.6.A:4.10 - Elaborate only for the next use

Start with the recovered statement or question. Add participants, conditions, supporting sources, rival interpretations and expression structure only when the next use needs them. If further inquiry changes the interpretation, reopen it; elaboration is not a compulsory progression from cue to option to policy.

A move from a cue to a proposed action, from alternatives to a selection, or from a description to a Method, WorkPlan or Work claim requires that receiving subject's grounds. State the result of that move rather than silently upgrading the wording. Use §4.7 for a consequential comparison across traditions and A.6.B for an actual boundary-bearing claim.

#### A.6.A:4.10a - Continue from the recovered subject

Once the result identifies an actual authority, relation, Method, WorkPlan, Work, gate or inquiry question, continue through its direct pattern if further work is needed. A declaration-local planned-filling row is addressed through its WorkPlan. Preserve a separate recovery note only when a reader needs the interpretation or grounds; there is no common invitation occurrence to establish before continuing.

