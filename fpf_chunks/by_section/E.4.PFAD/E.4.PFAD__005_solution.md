---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__005_solution.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:4 — Solution"
line_start: 70384
line_end: 70468
dependencies:
  - "A.15.1"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.5"
  - "C.30.AD"
  - "C.30.STRAT"
  - "C.32.ADR"
  - "C.32.MWA"
  - "C.32.PAD"
  - "C.36"
  - "E.11.DSG"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.23.CDI"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:4 - Solution

#### E.4.PFAD:4.1 - Decide whether the architecture question is open

Ask whether choosing a framework, a maintained non-framework product, a thinner route, an existing-framework contribution, or stop will settle at least one boundary used by later authoring or review:

- the public field promise, a first use that does not depend on unpublished authoring context, or the problem-family coverage of a proposed DPF;
- an intended or existing framework edition;
- an FPF Core or other current edition dependency;
- initial pattern placement or a material relation among those patterns that changes the architecture;
- the direct subjects and maintenance boundary for a continuing programme, an admitted service, or a separate editioned result when later work must maintain or use them;
- a publication or access consequence; or
- for a proposed DPF Suite, the ecosystem use, which product series may belong, constitution, inclusion and removal rules, identity through change, maintenance and source-return conditions, exposure choice, and any separate DPF Suite Reference product decision.

If no such boundary and receiving use are present, close the exploratory use without `E.4.PFAD` or an `E.9` DRR. If they are present, decision Work selects a framework, maintained non-framework product, thinner route, existing-framework contribution, or stop and one `E.9` DRR records that answer. The cheap exit and the architecture decision are alternative entry outcomes, not serial stages.

For every maintained alternative, use *product* only as the first management cue. Then compare the direct subjects at the same grain: the exact framework or package episteme, System, service arrangement, Method, programme description, carrier, or other admitted result, and the relations that later work will rely on. A quality-management, service-management, publication, or content-management scheme may supply a useful probe, but it does not settle the FPF kind. If the unresolved kind can change the selected boundary, keep the boundary proposed and make that kind the next decision question.

#### E.4.PFAD:4.2 - State the compact framework answer

When the architecture question is open, the framework-specific part of the DRR states:

1. the intended practitioner, public field name and promise, recurring problem, and bounded architecture question;
2. the selected outcome: a new or revised framework edition, a contribution to an existing framework, a maintained non-framework product, a thinner publication or access route, or no new maintained product now; for a maintained non-framework product, also the direct subject kind and the identity, current-state, provision, or maintenance relations used by the decision;
3. its field boundary: who can first use it without unpublished authoring context and for what; the connected problem families and useful results; what the current FPF and admitted DPFs already provide and what remains uncovered; serious alternatives, such as splitting or merging the proposed framework, using existing sources directly, contributing to an existing framework, selecting a programme or service boundary, selecting a separate evidence-package episteme, or keeping no maintained product; the limits of evidence; and what change will require a refresh;
4. the selected problem-family pattern sets, first patterns and their material relations, representative cross-problem application, and important omissions;
5. which practice structures change the answer and how their Methods, descriptions, patterns, direct subjects, and managed result boundaries fit together. When those structures do not line up one-for-one, use a completed `C.32.MWA` synthesis; use `E.23.CDI` only when capability development for a named Work family changes the answer;
6. the existing or intended-edition boundary, selected FPF Core dependency, and only the other exact edition dependencies required by this answer;
7. the sources to revisit for each important claim, whether the evidence supports, suggests, or only motivates it, the limits of that evidence, and the publication or access consequence; and
8. material alternatives, accepted costs or losses, practical consequences, the first authoring action or stop, and the reopen condition.

When professional Method coverage can change point 5, the same compact framework answer projects five connected claim groups from points 1, 3, 4, 5, 7, and 8. The projection is content of that one answer and its one ordinary `E.9` DRR, not a second architecture record, fixed schema, or later DPF invention. Fill each group only to the grain that changes first use:

1. **Practice truth and first use:** identify every bounded practice claim or promised practice contribution by its exact subject and scope, mark that claim—not the answer as a whole—as obtaining or possible-future, and state practitioner, recurring or anticipated difficulty, sought result, first use, non-use boundary, qualification window, and receiving decision.
2. **Project and Method positions:** name the direct project subjects, use and environment, materially different solution forms, and Methods under their actual operational, system-change, solution, Method-of-interest, or Method-development relations. Keep incumbent Work, development or trial Work, candidate-practice Work, and intended Work distinct.
3. **Selected structures and correspondences:** include only the Method, Work, subject, transformation-flow, capability/provider, description, contribution, Method-development, and cultural structures whose correspondence, conflict, or non-isomorphism changes the answer.
4. **Pressures and evidence:** keep constraints, conflicts, failures, environment or interest changes, and observed, source-supported, estimated, contradicted, and missing links distinct from causal history and temporal unfolding.
5. **Contribution, subtraction, gaps, and reopen:** state what current FPF and admitted DPFs already supply, each receiving pattern and domain filling still needed, exact external results, honest omissions and gaps, and the observation that reopens the architecture.

One answer may contain several bounded practice claims with different truth status. Every selected practice question names the claim or claims it consumes, so an obtaining incumbent-practice claim can coexist with a possible-future candidate-practice claim without backdating the candidate or erasing current incumbent coverage. Independently obtaining A.13 agency claims and actual development or trial Work keep their own status; neither proves that the candidate practice obtains. Public coverage is another claim and remains limited to the exact obtaining or prospective contribution and later package evaluation.

For an obtaining practice claim, name actual recurring difficulties and representative actual Work. A precise Agent-performer branch first supplies A.13's core: the exact admitted System, local agential system-role kind and criterion, classification, obtaining assignment, and needed scope, working situation, and window. Add the agency-characteristic profile only when a Grade, autonomy or profile claim, a criterion-dependent characteristic, or a named assurance use consumes it. A.15.1 then independently admits the actual Work from its performance history, Method, extent, and containment. Only after admission does F.6 supply any precise assignment-bound attribution through that same obtaining assignment. State evidence limits; a missing F.6 relation leaves admitted Work intact and only the attribution unresolved.

For a possible-future practice claim, name intended use, incumbent Work or Method and observed problem evidence, candidate Methods and architecture, realization conditions, a planned representative trial, expected acceptance and failure observations, and reopen conditions. Any incumbent-practice or actual trial-Work claim stays independently obtaining when supported, but the candidate-practice Work, candidate-practice Agents, and current candidate-practice coverage remain unasserted until their own conditions obtain.

For every selected question, name its receiving pattern and the exact bounded practice claim or claims whose values change first use. If a required group or claim-to-question binding is absent at that grain, return a bounded PFAD gap before DPF authoring; the DPF author does not invent the missing value. A completed `C.32.MWA` synthesis is used only when several selected structures do not line up one-for-one, and `E.23.CDI` only when capability development changes the answer.

The answer is one identified claim-bearing episteme under C.2.1 and is recorded, with its rationale, in one ordinary E.9 DRR. Decision Work selects that answer. A separately identified authorized acceptance decision accepts, redirects, rejects, or reopens it; carrier identity, DRR identity, or the fact that authoring continued identifies neither the accepting decision nor acceptance. Only the exact accepted answer is handed to E.4.DPF.

Common practice questions include:

| Practice question | Pattern that supplies or tests the answer |
| --- | --- |
| What contribution or effect is required? | `A.6.F`; use `C.30.ASV` only when a selected architecture view changes the answer. |
| Which Methods construct a larger Method, and which genuine interfaces matter? | `B.1.5`; use `A.6.M` only for a real module, port, or implemented-interface claim. |
| What changed, and how are the transformation-flow positions related? | `A.3.4`, `E.18`, and `C.30.TFS-REL`. |
| What Work occurred, which Method did it enact, and who performed it? | `A.13` followed by independent `A.15.1` admission; `F.6` only afterward for precise assignment-bound attribution, with the A.13 profile branch only when consumed. |
| Which System has the needed capability, and what did a provider actually contribute? | `A.2.2` plus the applicable Work, provision, or service pattern. |
| What cultural generation, transmission, reconstruction, recognition, selection, retention, or loss matters? | `C.36`. |

If another question changes the answer, name it and the pattern that handles it instead of forcing it into these rows. Do not infer Method parthood from a required contribution, transformation, performed Work, capability, provider contribution, or cultural change.
For a DPF Suite answer, an architecture decision takes effect to constitute the continuing collection. It selects the ecosystem use, which product series may belong, inclusion and removal rules, identity through change, alternatives, practical consequences, and the reopen condition. The same `E.9` DRR records that answer. A current maintained-Suite claim also identifies the capable maintaining System and its accepted commitment, the working source return for product series and any product-series state presented as current, the refresh response, and one exposure choice: an independent Suite route, a bounded projection in a current DPF Suite Reference edition with source return, or a neutral combined carrier. Constituting and including the Reference product series, admitting and maintaining its editions, and refreshing their answers remain separate decisions and claims. A proposed result use or future constraint is not an obtaining dependency or compatibility relation; apply `E.4.PFR` only after the edition-level case facts exist.

For an existing-framework contribution, maintained non-framework product, thinner route, or stop, state only the parts needed to explain that outcome and the later-used boundary. A selected maintained product still names its direct subjects and the relations used; a proposed boundary with an unresolved kind says so. Do not fabricate a field assessment or package merely to fill the list.

When the architecture keeps, merges, removes, reuses, or omits a load-bearing contribution, record the `E.8:4.1.3` same-situation disposition and the action or result that changed. A narrower label or example is not a difference. A difference that adds an unsupported or needless burden is not worth preserving merely because it changes action.

When the answer treats a promised problem family as covered by a result maintained outside the framework, name the exact result, its direct kind, supplying product and edition or current state, receiving use, practical discovery route, and every currentness or availability condition that can change that use. State that the result remains external. If those facts are absent, or the result does not answer the promised use, record a gap or omission rather than relabelling the result as framework content, a MethodDescription, or source evidence. When the selected keep, merge, removal, profile, external reliance, or omission materially changes the stable set for a promised problem family, obtain a current `E.4.DPF.DA` `D12DomainProblemFamilyCoverageAdequacy` result for the resulting exact DPF or LPF edition. A matching current result remains usable when that edition and its exact basis are unchanged; the architecture answer does not ask D12 to prove that a revisit occurred.

Keep the ordinary `E.9` grounds, sources, affected loci, rationale, and consequences in the same DRR. Add naming, quality, admission, currentness, or package details only when they change this answer or a named later use requires them. Use the pattern that defines, constrains, or tests each added claim; do not make it a standing PFAD field.

#### E.4.PFAD:4.3 - State initial pattern relations directly

When an initial pattern relation changes the selected architecture, state the relation and its participants as an ordinary assertion. For example: `Pattern A frames the recurring problem; Patterns B and C specialize its reusable move for two stated situations.` Use the pattern that defines or constrains each relation function.

An optional `E.4.PFR` row may later represent these assertions for maintenance. The row neither makes the relations obtain nor becomes mandatory for the architecture answer. A generic relation catalogue is not a prerequisite for the decision.

#### E.4.PFAD:4.4 - Keep the answer, DRR, authoring, and publication distinct

Decision Work selects the answer. The `E.9` DRR records that answer and its rationale. An authorized acceptance decision accepts, redirects, rejects, or reopens it. Later authoring follows an accepted answer. A framework edition is the maintained pattern-language result assembled from accepted sources, not the DRR or the authoring Work. An ADR-like document, site, PDF, or other carrier publishes or projects claims about these things; its form creates none of them.

When the answer uses `C.32.MWA` or `E.23.CDI`, keep each proposed Method distinct from the pattern that describes it, the Work that performs it, the result of that Work, the framework answer, the DRR, and the resulting edition. A proposal or evidence locator may help a reader find supporting material; it is none of those things.

Use `C.32.PAD` only when the question is an exact project architecture decision about a named composite project Work, and use `C.32.ADR` only to project that project decision. For an ordinary framework answer, publish the selected decision episteme or a reader-specific projection through `E.17` and `E.24.PUB`. None of these is a mandatory stage of principle-framework authoring.

