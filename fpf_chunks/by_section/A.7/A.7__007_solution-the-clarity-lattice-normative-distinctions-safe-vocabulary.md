---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:5"
section_title: "Solution — The Clarity Lattice (normative distinctions & safe vocabulary)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__007_solution-the-clarity-lattice-normative-distinctions-safe-vocabulary.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:5 — Solution — The Clarity Lattice (normative distinctions & safe vocabulary)"
line_start: 21505
line_end: 21646
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "MethodDescription ≠ Method ≠ Capability ≠ Work"
  - "category error"
  - "system-role kind and assignment ≠ Work"
---

### A.7:5 - Solution — The **Clarity Lattice** (normative distinctions & safe vocabulary)

#### A.7:5.1 - **Terminology (normative): orthogonal characteristics**
- **senseFamily** — the categorical characteristic, used by F.7/F.8/F.9: {Role | Status | Measurement | Type‑structure | Method | Execution}. Rows must be **sense‑uniform**.
- **ReferencePlane** — the referent mode per CHR: {world/external | conceptual | epistemic}.
- **EntityOfConcern and Description-episteme boundary** — the item under concern is separated from Description epistemes (E.10.D2, C.2.1). Specification use is a gated use or refinement of a Description episteme; the exact gate must name checkability, formality plus checkable constraint, harness, acceptance condition, C.16 measurement criterion, verification use, or another specification-granting neighbouring pattern. Specification is not a third member of the strict distinction.
- **DesignRunTag** — the design vs run DesignRunTag. It is not a temporal “plane”, generic layer, or stance.
- **Publication face, form, unit, carrier, and rendering boundary** — Description epistemes, including Description epistemes admitted for specification use, may be made available through publication units, publication forms, faces, renderings, and carriers. These publication values are not the `EntityOfConcern` value, not the Description episteme itself, not the specification-use gate or refinement, and not evidence, gate passage, work, assurance, or decision force by readable form. The ordinary didactic faces for architectural patterns in FPF are:
  {**PlainView** (explanatory prose), **TechCard** (typed cards and IDs), **NormsCard** (TechCard profile for checklists), **AssuranceLane** (evidence bindings)}. Publication faces and forms are orthogonal to the `EntityOfConcern` and Description-episteme boundary, to specification-use gates and refinements, and to DesignRunTag.
- **Direct Description account and specification-use boundary** — a Description episteme is independently identified under C.2.1 by its complete claim content, exact `EntityOfConcern`, and effective `ReferenceScheme`. A.7 introduces no universal EntityOfConcern-to-Description constructor or morphism. When it matters how the claims were produced, selected, carried, or revised, state the exact authoring, measurement, observation, model, source-use, representation, refinement, or other direct relation that is current. A later specification-use claim remains governed by the pattern that supplies its checkability, harness, acceptance, measurement criterion, verification use, or other specification-granting force.

- **EntityOfConcern / episteme / publication boundary** — `EntityOfConcern` names the item under concern; it does not name a document, publication face, carrier, or unspecified referent. A Description episteme makes claims about that exact item under its effective scheme. Publication faces, forms, units, renderings, and carriers may make the episteme available, but they do not become the EntityOfConcern, the episteme, a specification-use gate, evidence, gate passage, Work, assurance, or decision force. Formal or readable presentation creates none of those relations.
A.7 establishes the following **pairs and triplets**. Use their **names** and **scope** exactly as below.

#### A.7:5.2 - System-role kind vs function-like wording, functional behaviour, capability, method, and work

* **System-role kind.** One local `U.Kind` with `U.System` candidates and an operative condition for a stable, assignable, work-facing contribution. Its member/non-member boundary and continuity rule complete the C.3 recovery. A practice or source reference locates the definition; it does not identify the kind. An obtaining assignment occurrence may relate a system to that kind only through a directly admitted `U.SystemRoleAssignment` species. The kind is **not behaviour**. Example: the kind currently named `CoolingCirculatorSystemRole`, whose ThermalLoop-7 provenance locates one definition.
* **Function-like wording.** A source phrase such as "function", "behaviour", "service", or "does X" may name a required transformation or effect (A.3.4), functional behaviour (A.6.F), a capability envelope, a method, performed work, a quality, or a structure. Recover the governed claim before choosing the FPF term.
* **Under a system-role assignment.** A System or acting holon that holds an assignment may have a **Capability** to enact a **Method** under conditions. A precise Work claim still uses A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently. Add F.6 only if the claim must also identify the assignment under which that Work was performed. The system-role kind, assignment, Method, Capability, transformation, and effect do not substitute for the Work or performer.

Safe rewrite for earlier "Holonic Duality (Substance vs Function)": **Holonic Duality (Substance vs system-role kind).** A `U.System` keeps its identity while its classifications and obtaining assignments change. A contribution named by a system-role kind may call for a Method, a Capability envelope to enact that Method under conditions, and possible Work occurrences; none follows from the kind alone.

**Normative guard:** Use **system-role kind** for that exact local `U.Kind`, an admitted direct species under `U.SystemRoleAssignment` for assignment occurrences, **functional behaviour** for a behaviour claim stated with A.6.F, **Method** for the abstract way-of-doing, **Capability** for a holder System's bounded ability or envelope for a Work family or result class under stated conditions, **Work** for the performed occurrence, and **Transformation** or effect wording for an actual change identified with A.3.4. Do not call the kind or assignment itself a function, and do not define Method as Capability or as the transformation or effect itself.

#### A.7:5.3 - MethodDescription vs Method vs Capability vs Work (description vs way-of-doing vs ability envelope vs occurrence)

* **MethodDescription** — one already identified claim-bearing `U.Episteme` whose exact C.2.1 `EntityOfConcern` is one admitted `U.Method` and whose claims, under its effective `U.ReferenceScheme`, say something substantive about that Method as a way of doing. A transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal method composition can satisfy the positive threshold. The labels *algorithm*, *SOP*, *recipe*, *script*, *procedure*, code, diagram, or design-time artifact are cues only. Authoring, revision, citation, publication, approval, or use time establishes neither episteme identity nor `U.MethodDescription` membership. Its publication cites A.10 carrier/source-currentness refs when the carrier is used as evidence or source.
* **Method** — the **abstract order-sensitive way-of-doing** composed with **Γ\_method** (B.1.5). A Method is not an occurrence, description episteme, or system ability. Actual participants and operation values remain occurrence-side facts of separately admitted `U.Work` and its direct bindings.
* **Capability** — a named holder System's **bounded ability or envelope** for a Work family or result class, stated with its operating and resource conditions, measures, qualification window, and currentness condition. Name a Method or system-role assignment only when that exact condition or fit input is current. It is not the MethodDescription and not the performed Work.
* **Work** — the **dated run-time occurrence** (what actually happened), with resource spend (Γ\_work) and temporal coverage (Γ\_time).

**Designation, reference, and description are different.** A Method identifier designates one exact `U.Method` under the applicable designation rules of an effective `U.ReferenceScheme`. A receiving claim's `methodRef` separately resolves under its effective scheme to that same Method. Neither operation needs a MethodDescription. Cite a separate `methodDescriptionRef` only when that receiving claim actually depends on claims in an exact episteme edition that has already passed A.3.2 membership.

**Minimally viable reference and membership case.** Under `MaintenanceReferenceScheme-2026`, identifier `PumpSealInspectionMethod` designates exact admitted Method `M-PSI`. `MaintenancePlan-47` is a separately governed `U.WorkPlan`; its `methodRef = PumpSealInspectionMethod` resolves directly to `M-PSI`, without a description hop. Episteme `PumpSealInspectionGuide-e3` is independently identified by C.2.1 from its exact claim content, `EntityOfConcern = M-PSI`, and effective scheme. Its claims state the inspection precondition, ordered clean–inspect–classify way of doing, rejection bound, and stop; the same episteme therefore passes A.3.2 membership as `U.MethodDescription`. If `MaintenancePlan-47` relies on those exact e3 claims, a separate `methodDescriptionRef = PumpSealInspectionGuide-e3` may be cited. The plan, Method, MethodDescription, Capability and any later Work remain different objects.

**Recognizable near misses.** A catalogue row containing only `PumpSealInspectionMethod` designates or mentions a Method but is not a MethodDescription. A file named `PumpSealInspectionSOP-v3.pdf` supplies neither the C.2.1 episteme identity nor the substantive method claim by filename. `methodRef = PumpSealInspectionMethod` does not imply that a description exists. A newly authored, revised, cited, approved, published, or used episteme does not gain membership unless its exact Method EntityOfConcern and substantive way-of-doing claim satisfy the same test.

**Normative guard:** Never use MethodDescription as evidence of Work; never present Method or Capability as if it had happened; never define Method as Capability; never infer MethodDescription membership from form, label, lifecycle time, or use. Resolve direct Method designation and receiving references without mandatory description indirection.

#### A.7:5.4 - Holon vs System vs Episteme (who can act)

* **System or acting holon.** A System can act because its physical or operational organization satisfies A.1. An ordinary sentence may name the recognizable System by a contribution noun: `The engineer designed the pump`, `The reviewer checked the manuscript`, or `The service accepted the request`. Keep that wording when the System and contribution are recoverable and no receiving inference depends on a local system-role kind or assignment identity.
* **System-role kind and assignment, when current.** Add a local system-role-kind classification when the claim uses that classification. Add an obtaining assignment occurrence and its admitted species only when the claim says that the System held that assignment, attributes a particular Work occurrence to it, or relies on assignment identity, extent, or participants. The assignment and kind do not make the System able to act and do not act themselves.
* **Capability, Method, and Work, when current.** Name Capability only for an ability or envelope claim, Method only for the way of doing, and Work only for a performed occurrence. An ordinary actor sentence need not materialize all three.
* **Episteme.** An episteme cannot act. A System may author, revise, use, or publish it; state the actual operation, Work, carrier, publication, evidence, or source relation only when the receiving claim uses that distinction.
* **Holon.** Use the umbrella word only when systemness is not part of the claim. If action is asserted, the acting entity must satisfy A.1 as a System; an assignment is not the admission test.

**Progressive example.** `The design team selected valve V-12` is enough for an ordinary design account when the team is a recoverable collective System and no later inference needs a precise Work or assignment identity. If an audit claims dated `ValveSelectionWork-47`, use A.13 to identify `DesignTeamSelectionSystem` as the actual performer and A.15.1 to admit the Work independently. If the audit must also identify the assignment under which that Work was performed, use F.6 to check `ValveSelectionAssignment-47` and compare its holder with the already identified performer. Add the admitted assignment species, assigned local kind, extent, Method, Capability, and evidence only to the degree used by the audit.

#### A.7:5.5 - Episteme vs publication carrier and source-currentness record

* **Episteme** — the knowledge content (claim, model, requirement set).
* **Publication carrier or source-currentness record** — the physical or digital carrier for an episteme publication or stored representation (file, volume, dataset item), tracked through A.10 carrier/source-currentness relations when evidence, source, or reliance use is current.
* **Use:** Evidence, provenance, and reproducibility address **carriers**; arguments and validity address **epistemes**.

**Normative guard:** When you say “we updated the spec”, detail **which carriers** changed (A.10).

#### A.7:5.6 - Formal inclusion, world-side collection, and collective System

- **Mathematical or representation inclusion** — say that an element is in a set, a value fills a tuple place, or a value lies in a coordinate domain under the applicable mathematical statement. Use `C.29`, with `A.19` when a characteristic scale or coordinate is current. No world-side belongs-to relation follows.
- **World-side collection** — identify the collection and use its subject-specific belongs-to rule. That rule says who or what may belong, when belonging begins and ends, whether it may recur, and how past belonging is stated. Belonging alone establishes neither parthood nor holonhood, but it does not prohibit a separately grounded constructive part relation.
- **Collective System** — treat a team or other grouping as an acting System only after the candidate passes all six `A.1` matters. A list, formal set, catalogue, or belongs-to statement does not establish that result.
- **Use the direct relation for every stronger claim:**

  - **ComponentOf** — mechanical or structural part in systems.
  - **ConstituentOf** — logical or content part in epistemes.
  - **PortionOf** — quantitative portion with conserved extensives.
  - **PhaseOf** — temporal part of the same carrier over a proper interval.
  - **System-role assignment** — a System is the `HolderSystemSlot` value in one obtaining occurrence of a directly admitted `U.SystemRoleAssignment` species.

**Normative guard:** Formal inclusion establishes no world-side belonging. Collection belonging establishes neither constructive parthood nor holonhood and does not make either impossible. If a grouping is claimed to act, test it against all six `A.1` matters. Add a local system-role kind, assignment, Method, Work, or constructive part relation only when that separate claim obtains.

#### A.7:5.7 - Operator alignment (required names)

* **Γ\_sys** — composition of **system** properties (physical/systemic).
* **Γ\_method** — composition of **Method** (order, branching).
* **Γ\_time** — composition of **Work** histories and temporal parts.
* **Γ\_work** — composition of **resource spend** and yields tied to Work. Do not track costs with Γ\_method; costs (resources/yield) belong to Γ\_work.

**Normative guard:** Avoid generic “process” for these operators. Reserve “process” for domain idioms; map internally to **Method** (design) and **Work** (run).

#### A.7:5.8 - EntityOfConcern and Description-episteme boundary vs publication face, form, unit, and carrier boundary (orthogonal, normative)
* **EntityOfConcern-to-description boundary.** A.7 keeps the EntityOfConcern and an episteme that describes it distinct; E.10.D2 supplies the Description and specification-use repair. What the `EntityOfConcern` value is and how it is described are different questions. A Description is a `U.Episteme` about that exact entity under its effective scheme. A named describing use may separately select one viewpoint when the selection changes what is read or checked. Specification is a checkable use or refinement of the Description episteme and requires checkable claims plus a named harness or validation relation; formality, acceptance, a C.16 measurement criterion, or verification practice may contribute to that test but does not substitute for it. EntityOfConcern, Description, selected viewpoint, and specification use remain distinct.
* **Publication governs availability.** Publication units, publication forms, faces, renderings, and carriers make Description epistemes available to readers or tools, including Description epistemes admitted for specification use. They do not become the `EntityOfConcern` value, the Description episteme, the specification-use gate/refinement, or an evidence/source carrier by the same relation; physical and digital carriers stay in A.10 carrier/source-currentness relations when evidence, source, or reliance use is current.
* **Publication-face field pins.** When Description epistemes or Description epistemes admitted for specification use are shown on **TechCard**, the minimal **CHR-Pins** are {**UnitType**, **ScaleKind**, **ReferencePlane**, **EditionId**}.
* **Semantic and plane boundary.** A context or ReferencePlane difference alone establishes no F.9 Bridge, `CL`, or trust penalty. When two exact F.17 local senses and the direct F.9 predicate establish a Bridge, cite that relation and a separate bounded-use claim; `CL` remains optional evidence shorthand. A cross-plane use cites its applicable plane relation. Apply a trust penalty only when a named current policy applies to the exact use.

#### A.7:5.8a - Same or near-same EntityOfConcern across descriptions and views

Different descriptions, views, viewpoints, publication units, or role-method-interest positions may concern the same `EntityOfConcern`, different entities of concern, or an unresolved candidate set. A.7 does not accept sameness by publication title, view label, carrier continuity, shared ordinary name, or common reader interest.

Use this split when the text needs to say whether two descriptions or views are about the same thing:

| Case | A.7 relation case | Admissible move |
| --- | --- | --- |
| same referent by value | the localized `EntityOfConcern` or relation named by value, carried by the current claim, or selected by a reference case and the resolved `entityOfConcernRef`, where live, refer to the same item by declared reference discipline | same-entity work inside the declared use |
| preserved by viewing | A.6.3 viewing preserves the exact EntityOfConcern while producing another episteme whose claim content or effective ReferenceScheme may differ; any representation relation and any viewpoint selected for a named describing use remain separate | same-EntityOfConcern Description, Specification, or view transformation |
| publication-unit primary only | a bounded publication unit states what it is mainly about, plus its carried move and outside-work boundary, without establishing a claim-bearing episteme trace by itself | publication-unit stability only |
| bridge-conditional near identity | An F.9 Bridge obtains, and a separate affirmative bounded-use claim names the proposed use, direction, correspondence rule, tolerated loss, and polarity. A practitioner may first use F.18 to settle the governed value's designations and, only when a durable term row is needed, then use F.17 to constitute that row; neither step establishes the Bridge or licenses reuse, while publication, evidence, and any reliance judgement remain separate. | bridge-scoped reuse only |
| retargeted under invariant | A.6.4 identifies an exact arrow r between epistemes with different EntitiesOfConcern. A separate C.2.1 bounded-use assertion q about exact r states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A separate current-case judgement compares exact facts with q's conditions and proposition and returns `satisfies`, `fails`, or `cannot decide`; `cannot decide` names the missing fact and reopen condition. | retargeted use only after an affirmative q for the named use receives a separate `satisfies` judgement; otherwise retain the exact result, including the missing fact and reopen condition for `cannot decide` |
| unresolved candidate | construction/reference/bridge/witness trace is insufficient | candidate tracking, question framing, or non-use |
| different entity | no admissible sameness or near-sameness path exists for the intended use | keep entities distinct |

If the same or near-same relation needs mathematical or postulate-theory justification, A.7 stops at the strict-distinction boundary instead of pretending to prove it: use C.29 for the mathematical lens, E.18 and E.18.1 where transformation-flow, carry-through, and postulate-theory work supply the required justification, E.18 where a gate crossing is the live relation, or the relevant architecture pattern where the comparison is about structure, graph, flow, or architecture description.

#### A.7:5.8b - Compact relation-position recovery aid

When one visible source-side carrier, publication face, diagram, dashboard, card, model output, `PublicationUnit`, rendering, or generated artifact can be read as several FPF values at once, use A.7 only to recover the current relation position. Name the current `EntityOfConcern`, Description episteme, view, publication face, publication form, `PublicationUnit`, carrier, rendering, mathematical-lens use, evidence relation, gate decision, work occurrence, authority-reference relation, source-currentness relation, or source-use claim, then apply the subject pattern for that position.

This aid is not a reusable object, local record, table, or master checklist. If the direct governed claim is already clear, do not add an A.7 recovery note; cite the direct pattern.

#### A.7:5.9 - Direct Description account and specification-use boundary (normative)

A.7 uses no `Describe_EoC_DescEp` function. To say that one episteme describes something:

1. identify the Description episteme through its complete C.2.1 claim content, exact `EntityOfConcern`, and effective `ReferenceScheme`;
2. state the claims it makes about that EntityOfConcern in ordinary language;
3. when the receiving use asks how those claims arose or are carried, name the exact authoring, measurement, observation, model, source-use, representation, refinement, or other direct relation and its participants; and
4. keep any publication occurrence, form, face, carrier, evidence use, Work, or specification-use gate separate.

If the EntityOfConcern is itself an episteme, the new Description does not automatically copy, preserve, refine, or extend its claims. Any representation, source-use, comparison, refinement, or loss claim needs its own direct rule. If the EntityOfConcern is a system, structure, Method, Work occurrence, physical object, characteristic, relation, or other non-episteme, claims are likewise not “inside” it waiting to be copied; the actual measurement, observation, model, postulate, authoring, or other relation explains the claim when that explanation is current.

**Example.** `PumpPerformanceDescription-e4` is a C.2.1 episteme whose EntityOfConcern is pump P-12 and whose claims state the measured flow and pressure under the named scheme. `MeasurementRun-88 produced ObservationEpisteme-88`, and that observation supports the stated measurement claim through its direct evidence-use relation. The Description, pump, measurement Work, observation episteme, evidence use, and publication carrier remain different objects. No universal constructor is needed.

A Description episteme becomes usable as a specification only through the neighboring pattern that supplies the required checkable constraints and named harness, validation, acceptance, measurement criterion, verification use, or other specification-granting force. Formal notation alone is insufficient. Specification use remains separate from the EntityOfConcern, Description identity, publication expression, and Work.

Describing, formalizing, and specifying are not execution. They carry no `Gamma_method`, `Gamma_time`, or `Gamma_work` actuals. Authoring or publishing them may involve separate Work with its own time and resource relations.

#### A.7:5.10 - Outcome specification strict distinction

A.7 supplies only the distinction. The authoritative promise-facing `OutcomeSpec` shape is in A.2.3:4.1.1, and the authoritative unit-of-delivery counting rule is in A.2.3:4.1.2.

An `OutcomeSpec` is a specification-use episteme form, not a new U-kind, a Work occurrence, an affected entity, a post-work state, an operation-result binding, or a verdict episteme. Its mode says which facts the promise constrains:

* `WorkOnly` constrains selected facts about one or more delivery Work occurrences;
* `ResultOnly` constrains the exact affected referent and required post-work state, regardless of method; and
* `Composite` constrains both.

**Readable example.** `The provider cuts and styles the client's hair within 20 minutes, and the resulting hairstyle meets the stated evening-style condition.` The first clause constrains delivery Work and may name the exact Method. The second constrains the client's post-work hairstyle state. Exact affected-referent, actual-change, production, delivery, acceptance, and evidence-use relations are stated only when the receiving claim needs them. No `U.Work.Delta` field or universal delta record is required; an optional mathematical change expression remains a separate lens when a named comparison uses it.

Evidence supports assertions about the selected Work facts, affected referent, post-work state, and direct relations. Evidence and its carrier do not become any of those facts. Counting is also separate: A.2.3's `unitOfDelivery` says how accepted delivery is counted and how double counting is prevented; it is not part of `OutcomeSpec`.

