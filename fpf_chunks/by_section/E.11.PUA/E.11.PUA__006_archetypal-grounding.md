---
chunk_kind: "child"
pattern_id: "E.11.PUA"
pattern_title: "Pattern Use in a Working Situation and First Useful Result"
section_id: "E.11.PUA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUA/E.11.PUA__006_archetypal-grounding.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "E.11.PUA — Pattern Use in a Working Situation and First Useful Result"
  - "E.11.PUA:5 — Archetypal Grounding"
line_start: 75627
line_end: 75686
dependencies:
  - "A.15"
  - "A.6.5"
  - "C.2.1"
  - "E.11"
  - "E.11.PUR"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.22"
  - "E.23"
  - "E.8"
  - "G.11"
keywords:
---

### E.11.PUA:5 - Archetypal Grounding

#### E.11.PUA:5.1 - Episteme result: a usable problem card

A team has a vague recurring pump-failure concern and asks whether it can be articulated well enough to guide later method selection. In ordinary conversation the team says: "Use C.22.2 to make the pump-failure concern into a usable problem card." It inspects C.22.2, applies the Solution, obtains the card, and stops once the current question is answered.

The card's `ProblemCard@Context` kind and application-flow position remain recoverable from C.22.2 when a later distinction needs them; the team need not state or record those fields during this cheap use. A durable closure or receiving-use relation is created only when the later P2W use or another named receiving use relies on replay.

#### E.11.PUA:5.1a - Evaluation specification without a ProblemCard

An architecture team already has a bounded comparison question but no accepted `ProblemCard@Context` is needed for this use. It applies `A.19.ECS` and produces an `EvaluationCharacteristicSpaceSpec` with declared coordinates, scales, comparators, and evidence rules. The optional `problemCardRef` remains absent. The exact episteme is the `selectedPatternApplicationFlowResult`; when the later comparison actually uses it, the receiving-use relation records that realized use without opening P2W.

#### E.11.PUA:5.1b - A selection result can support later planning

Pattern-selection work under E.11.PUR produces a `PatternUseRecommendation@Context`. That recommendation is a `patternSelectionFlowResult`. A later PUA use applies the recommended planning pattern and produces a `U.WorkPlan` as a separate `selectedPatternApplicationFlowResult`. E.18 may relate the recommendation to the later use through an explicit crossing, but neither the recommendation nor the plan becomes the machined component expected from downstream subject work.

#### E.11.PUA:5.1c - AI-assisted ordinary use returns the subject result

An engineer asks an AI assistant to apply an already selected `A.19.ECS` pattern to a pump-comparison question. The needed result is an `EvaluationCharacteristicSpaceSpec` with admitted coordinates, scales, comparators, and evidence rules. No later use asks for a durable pattern-selection trace.

The assistant returns that specification as the `selectedPatternApplicationFlowResult` and keeps the concern, pattern fit, and stop condition recoverable in the conversation. It does not add candidate, fit, applicability, rationale, or closure records merely because an AI assisted the use. If the available basis cannot support the specification, it names the unresolved coordinate, scale, comparator, or evidence-rule position, returns the use to `A.19.ECS`, and leaves the completed-specification expectation open. Materialize that return as `PatternUseBoundaryCondition@Context` only when a named reliance needs an addressable boundary; do not emit a complete meta-record stack.

#### E.11.PUA:5.2 - Physical result: work is still future

A machining team inspects a planning pattern for a dimensionally accepted component. Applying the selected pattern produces a `U.WorkPlan`. The metal blank remains unchanged.

The plan is an honest `selectedPatternApplicationFlowResult`. The component remains an expected `downstreamSubjectWorkFlowResult` until dated machining work occurs. The team may continue with the A.15 work patterns; it cannot fill the component result position with the plan, simulation, inspection checklist, or generated prose.

After the dated machining `U.Work` occurs, the actual-result relation names the dimensionally accepted physical component or changed physical state in `downstreamSubjectWorkFlowResult` position and cites only work occurrences that produced or changed it. An inspection record may support evidence or description use; it does not replace the physical result.

#### E.11.PUA:5.3 - Clinical result: a state and its note stay separate

A clinician uses a direct pattern to structure a treatment decision. The application produces a treatment-plan episteme and an intended receiving use. The patient's changed clinical state does not yet exist merely because the plan is accepted.

After treatment work occurs, the clinical state and the case-note episteme can both be current, but they keep different kinds and governing relations. The note may support grounding and later reliance; it does not become the patient's state.

If the clinically relevant state existed before the current pattern use, record `preExistingWithGrounding` and produce a `PreExistingResultGroundingFinding@Context` from the current examination or accepted evidence. The examination grounds use of the state for the present question; it does not produce that state or supply an unknown earlier treatment history.

#### E.11.PUA:5.3a - Learned capability and assessment remain separate

Teaching work is performed under its direct educational and A.15 patterns. A later assessment may support a claim that the learner has demonstrated a bounded capability or skill. The capability result and the assessment episteme keep different kinds and governing relations: a completed lesson, assessment plan, or filled assessment record cannot occupy the learned-capability result position by itself.

#### E.11.PUA:5.4 - Pre-existing result: inspection does not reproduce it

A maintenance engineer inspects an installed pump that predates the current pattern use. Current measurements adequately ground the pump for a compatibility question, but the historical production relation is outside the evidence basis.

Use `PreExistingResultGroundingFinding@Context` for the present grounding. Keep producing-work provenance absent. The current inspection neither manufactures the pump nor proves how it was manufactured.

#### E.11.PUA:5.5 - Repair a plan-as-component closure locally

A machining rehearsal selected the correct planning pattern and produced a valid `U.WorkPlan`, but its closure named the plan as `downstreamSubjectWorkFlowResult` and treated the component expectation as satisfied. The concern, candidate basis, direct pattern, and WorkPlan remain sound.

Repair the expectation and actual-result closure: name `U.WorkPlan` as the `selectedPatternApplicationFlowResult`, remove the claimed component actual result and any realized receiving-use relation that depended on it, and keep the component as an open downstream expectation. The next current use enters the A.15 work family. No new candidate selection or reconstruction of the WorkPlan is needed.

#### E.11.PUA:5.6 - Complete trace, absent result

An automated report raises pattern-use trace completeness to 100 percent by filling every candidate, rationale, expectation, and boundary position. Operators begin treating the green report as completion, while actual-result grounding and the intended receiving use remain absent more often.

The trace measure improved while subject progress worsened. Keep completeness as a trace-quality measure, apply `E.13` to the substitution, and evaluate PUA success from the exact grounded result or honest interim result, its flow position, and its receiving-use disposition. Empty actual-result positions are not repaired by adding more support records.

