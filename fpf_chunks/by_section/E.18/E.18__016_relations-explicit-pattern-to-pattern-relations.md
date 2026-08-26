---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:14"
section_title: "Relations (explicit pattern-to-pattern relations)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__016_relations-explicit-pattern-to-pattern-relations.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:14 — Relations (explicit pattern-to-pattern relations)"
line_start: 83955
line_end: 83990
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.18.NET"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.18:14 - Relations (explicit pattern-to-pattern relations)
* **E.18 -> coordinates with -> A.15.5 WorkEntryReadiness.** A selected structure may position a launch or work-boundary readiness locus only in relation to A.15.5. E.18 supplies the current path, slice, and any actually present crossing, `LaunchGate` position, or structure-local pins; A.15.5 defines and tests `FullKitCondition`, planned preparation references, commitment disposition, resource-readiness references, and whether intended work is ready to enter performed-work execution.
* **E.18 -> coordinates with -> C.32.P2S ProblemToStructureArchitecturingFlow.** P2S may cite a selected transformation-flow structure, path, crossing, or valuation as architecture content or uncertainty. When Plain wording calls that value a method handoff, work handoff, or feedback input, C.32.P2S must identify the receiving entity or relation occurrence independently, including its participants, obtaining condition, and the pattern content that defines or tests it; those labels supply none of them. E.18 still defines the transformation-flow structure and does not become the whole architecturing flow.
* **E.18 -> coordinates with -> C.33, C.34, and C.35 structural-information patterns.** When a transformation-flow carrier, path, generated map, or independently identified changed entity or relation occurrence that carries or describes structure needs architecture-specific capture, preservation, or discovery adequacy, use `C.33`, `C.34`, or `C.35` for that architecture use. Before a selected structure is returned to a named architecture use, cite the exact selector or selection relation, or another relation occurrence, that returns it; name that relation's predicate, participants, obtaining condition, occurrence identity, and the content that defines or tests it. Also cite the exact source-to-use relation and the pattern that defines or constrains the receiving architecture claim. `C.33`, `C.34`, and `C.35` supply definitions or tests; they are not participants in those relations. E.18 keeps the selected transformation-flow structure, path, crossing, valuation, and any exact slice-local subject relation cited by that architecture use visible; it supplies no generic result, return, or receiving relation.
* **E.18 -> coordinates with -> A.22.CGUS through E.18.3 when transformation-flow unfolding is current.** Under E.18, independently identify the one-TFS or parent-relative internal-subflow substrate; use E.18.NET for an independently identified network substrate. `E.18.3` qualifies one separate A.22-selected CGUS only when that CGUS uses exact substrate positions, bindings, and already-obtaining occurrences under current applied-condition claims, any E.18 `GuardFail` events with their gate-assignment facts, and any independently defined guard-relation occurrences. The substrate ref does not resolve to `selectedCGUSRef`. Neighboring values and stronger claims remain independently identified and connect through exact supporting relations, predicate-definition content, and current facts. Ordinary E.18 use is not automatically substrate for a CGUS, and narrative, abductive, typing-grounding, improvement, evidence, refresh, and first-entry seed structures do not become E.18 structures by route-shaped wording alone.

> Relation rows use the named relation kinds **builds_on**, **constrains**, **coordinates**, **specializes**, **publishes_on**, **requires**, and **provides_checks_for**.

**Foundations**
* **E.18 -> builds_on -> E.17 MVPK (for publications of selected-structure content).** Faces, pins, lanes, functorial publication, Lean, Core, and Regulated profiles.
* **E.18 -> builds_on -> A.6.0 U.Signature and A.6.1 U.Mechanism.** Locus kinds and governing-definition content boundaries.
* **E.18 -> builds_on -> A.7 Strict Distinction (EntityOfConcern, Description episteme, Description episteme admitted for specification use, and publication and carrier separation).** No new claims on faces; publication faces project selected structure, crossing, or flow-valuation information without becoming the selected structure, Description episteme, specification use, evidence, gate decision, work occurrence, or carrier.

**Flow semantics and checks**
* **E.18 -> coordinates -> A.20 Flow Constraint Validity.** A.20 reports exact internal-constraint results for transformations, operation applications, or A.6.4 retargeting uses when those constraints are current. E.18 supplies no constraint truth, plane or unit declaration, gate consequence, or acceptance.
  **Terminology discipline (A.20 boundary).** Preserve A.20 applicability, evaluation state, outcome, summary, and witness or reason. `GateDecisionRationale` and `GateDecisionExplanation` remain A.21 terms.
* **E.18 -> coordinates -> A.21 Gate decisions.** When an `OperationalGate(profile)` decision is current, it consumes independently identified check-application results under one exact profile application. An unsatisfied or incomplete A.20 input affects the aggregate under that current rule without making another applicable check inapplicable; each deferred required check remains `notRun`. A.21 defines check-application identity, mappings, aggregation, result and rationale, and optional publication or reuse records.
* **E.18 -> uses -> USM.CompareGuard and USM.LaunchGuard.** Guards publish scope and responsible gate; guard failures are handled by the declared gate.
* **E.18 -> coordinates with -> F.9 and F.17 only for a current cross-semantic use.** Use E.18 for the structural `GateCrossing`; F.17 identifies the two exact local sense cells and F.9 alone decides whether a semantic Bridge obtains. The proposed structural use, reliance, optional Bridge Card, optional `CL`, actual gate decision, and any policy-based penalty remain separately identified.
* **Operational interpretation (default): Eulerian.** A flow is a **valuation** over `U.Transfer`; transfer relations carry **assurance-only operations** (see CC-E18-17); no token-passing semantics are assumed.

**UNM and comparability**
* **E.18 -> constrains -> UNM declaration and use loci.** Declare `CG-Spec`, `ComparatorSet`, and `UNM.TransportRegistryPhi` only at the UNM declaration locus; normalize-then-compare is mandatory.
* **E.18 -> constrains -> G.5 SelectionAndTuning.** Set-returning, comparator-pinned decisions and no hidden scalarization; cite the exact selector-declared set, handoff, abstain, or escalation outcome. Any next-step tuning remains in its separately identified `U.WorkPlan` with any declaration-local A.15.3 planned-filling rows, or in a separately identified configuration or policy that passes its own applicable rule, with no launch-value slot filling.
* **E.18 -> constrains -> G.11 EvaluatingAndRefreshing.** EditionBumpProposal, two-phase update through the UNM declaration locus, and path-local refresh. When current, identify `RefreshPlan@Context`, dated Work, later measurement and calibration, and `RefreshReport@Context` separately; no request, plan, record, audit artefact, or publication substitutes for another or becomes the returned world-side result by label.

**Work boundary**
* **E.18 -> coordinates with -> A.15.1 Work occurrences and A.15.5 work-entry readiness.** When an exact current `LaunchGate` relation consumes one prospective `workEntryClaimRef`, its current profile application selects any required freshness, tag, ingress, or other checks and maps their results to the attempted-entry consequence. If Work occurs, A.15.1 defines and tests the exact Work individual and requires the relevant world-side relations involving it to obtain independently; a separate `FinalizeLaunchValues` witness, telemetry record, or acceptance claim may designate the occurrence but is not that occurrence.
* **E.18 -> coordinates with -> A.3.4, A.15.1, and A.15.PROD at actual-change and production boundaries.** A `Transformation` locus points to one independently identified actual change under `A.3.4`; an adjacent `Work` locus points to an exact dated occurrence under `A.15.1`. A work-causes-change assertion uses A.6.RCD disposition 1 when its exact predicate and case facts are current; disposition 2 supplies only one local C.2.1 compound claim when no direct predicate expresses it and admitted base-predicate semantics support this receiving use. Work, Transformation, and that claim remain separate. Production-work participation, entity-identity inception, and historically indexed production completion cite separate local `A.15.PROD` claims; E.18 neither derives them from proximity nor introduces replacement relation kinds.

**Structure and reuse**
* **E.18 -> provides selected-structure base for transformation-flow families.** Flow patterns such as P2W and EvaluatingAndRefreshing use E.18 for selected structure, valuation, crossings, guards, MVPK faces, and slice-local refresh. `A.3.4` defines and tests each independently identified actual bounded `U.Transformation`; E.18 defines the selected compound structure over transformations and adjacent identified loci without asserting transformation composition; and the named neighboring patterns define or test method, work, mechanism, work-to-change, production, evidence, publication, gate, decision, and refresh claims when those claims are current.
* **E.18 -> coordinates with -> E.18.NET Network of Transformation-Flow Structures.** Use E.18 for one exact TFS, its `FlowPositionRef`, parent-relative `SubflowRef`, valuations, paths, slices, local state, and internal `U.Transfer`. E.18.NET starts only when independently identified TFS or nested-network members are selected with exact cross-member relation occurrences; it does not replace a detailed internal portion or several valuations of one TFS.
* **E.18 -> coordinates with -> architecture transformation-flow relation patterns.** When a selected transformation-flow structure is used in an architecture-flow relation, the architecture transformation-flow relation pattern records the relation between `TransformationFlowStructure` and `ArchitectureOf@Context`; E.18 keeps selected structure, crossing, and flow-valuation discipline.
* **E.18 -> publishes_on -> E.17 MVPK views** (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) for every transfer or locus where publication occurs; Lean mode applies only as per profile.

