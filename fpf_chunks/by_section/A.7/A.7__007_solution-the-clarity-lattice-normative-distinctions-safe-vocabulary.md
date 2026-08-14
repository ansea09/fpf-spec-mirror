---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:5"
section_title: "Solution — The Clarity Lattice (normative distinctions & safe vocabulary)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__007_solution-the-clarity-lattice-normative-distinctions-safe-vocabulary.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:5 — Solution — The Clarity Lattice (normative distinctions & safe vocabulary)"
line_start: 21426
line_end: 21637
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
• **senseFamily** — the categorical characteristic, used by F.7/F.8/F.9: {Role | Status | Measurement | Type‑structure | Method | Execution}. Rows must be **sense‑uniform**.
• **ReferencePlane** — the referent mode per CHR: {world/external | conceptual | epistemic}.
• **EntityOfConcern and Description-episteme boundary** — the item under concern is separated from Description epistemes (E.10.D2, C.2.1). Specification use is a gated use or refinement of a Description episteme; the exact gate must name checkability, formality plus checkable constraint, harness, acceptance condition, C.16 measurement criterion, verification use, or another specification-granting neighbouring pattern. Specification is not a third member of the strict distinction.
• **DesignRunTag** — the design vs run DesignRunTag. It is not a temporal “plane”, generic layer, or stance.
• **Publication face, form, unit, carrier, and rendering boundary** — Description epistemes, including Description epistemes admitted for specification use, may be made available through publication units, publication forms, faces, renderings, and carriers. These publication values are not the `EntityOfConcern` value, not the Description episteme itself, not the specification-use gate or refinement, and not evidence, gate passage, work, assurance, or decision force by readable form. The ordinary didactic faces for architectural patterns in FPF are:
  {**PlainView** (explanatory prose), **TechCard** (typed cards and IDs), **NormsCard** (TechCard profile for checklists), **AssuranceLane** (evidence bindings)}. Publication faces and forms are orthogonal to the `EntityOfConcern` and Description-episteme boundary, to specification-use gates and refinements, and to DesignRunTag.
• **Typed describing morphism and specification-use boundary** — `Describe_EoC_DescEp : EntityOfConcern -> DescriptionEpisteme` describes an `EntityOfConcern` value into a Description episteme under a declared construction/reference trace; it is **not** a mechanism and does not execute work. A later refinement, formalisation, or specification-use claim over that Description episteme is governed by the neighboring pattern governing the claim whose force is live: A.6.2 for effect-free episteme refinement, C.2.3 for formality and checkability, A.21 or the relevant gate/acceptance pattern for harness and acceptance force, C.16 for measurement criteria, E.17 for publication expression, and E.10 for suffix discipline. A.7 keeps those boundaries visible but does not turn them into a second strict-distinction member.
  **Laws (normative for A.7):** (DESC-1) *Non-extensibility of content* and (DESC-2) *identity and meaning-preserving composition*. Specification-use/refinement laws are enforced by the neighboring pattern governing the claim that selects the gate and value set.

• **EntityOfConcern / episteme / publication boundary** — `EntityOfConcern` wording names the item under concern under the declared construction/reference trace; it does not name a document, publication face, carrier, or unspecified referent. `Describe_EoC_DescEp` yields a Description-side `U.Episteme` about that `EntityOfConcern` value. A Description episteme may later be used as a specification only when a bounded use declares formality plus checkable constraint, harness, acceptance condition, C.16 measurement criterion, verification use, or another specification-granting gate. Publication faces, cards, views, publication relation positions, records, and carriers remain orthogonal relation positions: they can make Description epistemes available, but they do not become the EntityOfConcern value, the Description episteme, specification-use gate/refinement, evidence, gate passage, work, assurance, or decision force by appearing in a publication form.

A.7 establishes the following **pairs and triplets**. Use their **names** and **scope** exactly as below.

#### A.7:5.2 - System-role kind vs function-like wording, functional behaviour, capability, method, and work

* **System-role kind.** One local `U.Kind`, identified by a named practice or source boundary together with a stable assignable work-facing contribution, classifies systems by that contribution. An obtaining assignment occurrence may relate a system to that kind only through a directly admitted `U.SystemRoleAssignment` species. The kind is **not behaviour**. Example: `CoolingCirculatorSystemRole@ThermalLoop-7`.
* **Function-like wording.** A source phrase such as "function", "behaviour", "service", or "does X" may name a required transformation or effect (A.3.4), functional behaviour (A.6.F), a capability envelope, a method, performed work, a quality, or a structure. Recover the governed claim before choosing the FPF term.
* **Under a system-role assignment.** A System or acting holon that holds an assignment may have a **Capability** to enact a **Method** under conditions and may perform **Work** that produces, maintains, prevents, or checks a transformation or effect. Name both the assignment occurrence and its declared species when that distinction matters. The system-role kind is not the behaviour, Method is not identical to the transformation or effect, and Capability is not the Method.

Safe rewrite for earlier "Holonic Duality (Substance vs Function)": **Holonic Duality (Substance vs system-role kind).** A `U.System` keeps its identity while its classifications and obtaining assignments change. A contribution named by a system-role kind may call for a Method, a Capability envelope to enact that Method under conditions, and possible Work occurrences; none follows from the kind alone.

**Normative guard:** Use **system-role kind** for that exact local `U.Kind`, an admitted direct species under `U.SystemRoleAssignment` for assignment occurrences, **functional behaviour** for a behaviour claim stated with A.6.F, **Method** for the abstract way-of-doing, **Capability** for a system ability or envelope to enact a Method under conditions, **Work** for the performed occurrence, and **Transformation** or effect wording for an actual change identified with A.3.4. Do not call the kind or assignment itself a function, and do not define Method as Capability or as the transformation or effect itself.

#### A.7:5.3 - MethodDescription vs Method vs Capability vs Work (description vs way-of-doing vs ability envelope vs occurrence)

* **MethodDescription** — one already identified claim-bearing `U.Episteme` whose exact C.2.1 `EntityOfConcern` is one admitted `U.Method` and whose claims, under its effective `U.ReferenceScheme`, say something substantive about that Method as a way of doing. A transformation or enactment concern, generic participant meanings, applicability, precondition, intended effect or preserved condition, bound, or internal method composition can satisfy the positive threshold. The labels *algorithm*, *SOP*, *recipe*, *script*, *procedure*, code, diagram, or design-time artifact are cues only. Authoring, revision, citation, publication, approval, or use time establishes neither episteme identity nor `U.MethodDescription` membership. Its publication cites A.10 carrier/source-currentness refs when the carrier is used as evidence or source.
* **Method** — the **abstract order-sensitive way-of-doing** composed with **Γ\_method** (B.1.5). A Method is not an occurrence, description episteme, or system ability. Actual participants and operation values remain occurrence-side facts of separately admitted `U.Work` and its direct bindings.
* **Capability** — the **system ability or envelope** to enact a Method under stated system-role assignments, operating conditions, resources, and constraints. Attribute it to the exact system and state the conditions that bound the claim; it is not the MethodDescription and not the performed Work.
* **Work** — the **dated run-time occurrence** (what actually happened), with resource spend (Γ\_work) and temporal coverage (Γ\_time).

**Designation, reference, and description are different.** A Method identifier designates one exact `U.Method` under the applicable designation rules of an effective `U.ReferenceScheme`. A receiving claim's `methodRef` separately resolves under its effective scheme to that same Method. Neither operation needs a MethodDescription. Cite a separate `methodDescriptionRef` only when that receiving claim actually depends on claims in an exact episteme edition that has already passed A.3.2 membership.

**Minimally viable reference and membership case.** Under `MaintenanceReferenceScheme-2026`, identifier `PumpSealInspectionMethod` designates exact admitted Method `M-PSI`. `MaintenancePlan-47` is a separately governed `U.WorkPlan`; its `methodRef = PumpSealInspectionMethod` resolves directly to `M-PSI`, without a description hop. Episteme `PumpSealInspectionGuide-e3` is independently identified by C.2.1 from its exact claim content, `EntityOfConcern = M-PSI`, and effective scheme. Its claims state the inspection precondition, ordered clean–inspect–classify way of doing, rejection bound, and stop; the same episteme therefore passes A.3.2 membership as `U.MethodDescription`. If `MaintenancePlan-47` relies on those exact e3 claims, a separate `methodDescriptionRef = PumpSealInspectionGuide-e3` may be cited. The plan, Method, MethodDescription, Capability and any later Work remain different objects.

**Recognizable near misses.** A catalogue row containing only `PumpSealInspectionMethod` designates or mentions a Method but is not a MethodDescription. A file named `PumpSealInspectionSOP-v3.pdf` supplies neither the C.2.1 episteme identity nor the substantive method claim by filename. `methodRef = PumpSealInspectionMethod` does not imply that a description exists. A newly authored, revised, cited, approved, published, or used episteme does not gain membership unless its exact Method EntityOfConcern and substantive way-of-doing claim satisfy the same test.

**Normative guard:** Never use MethodDescription as evidence of Work; never present Method or Capability as if it had happened; never define Method as Capability; never infer MethodDescription membership from form, label, lifecycle time, or use. Resolve direct Method designation and receiving references without mandatory description indirection.

#### A.7:5.4 - Holon vs System vs Episteme (who can act)

* **System or acting holon** — the entity that can enact behaviour when it is the holder in one obtaining occurrence of an exact work-facing `U.SystemRoleAssignment` species.
* **Episteme** — **cannot act** and is not the holder in a work-facing system-role assignment; it is changed via carriers, publications, and work on those carriers by systems or acting holons. Reference, constraint-source, evidence, status, source, requirement, publication, and assurance uses are direct relations or uses, not system-role assignments.
* **Holon** — umbrella term; do not use it where the current claim requires a system as assignment holder. Write the exact holder and one named occurrence of the locally admitted direct assignment species—for example, `ValveSelectionAssignment-47 : ValveSelectionTransformerAssignment`, with `HolderSystemSlot = DesignTeamSelectionSystem` and `AssignedSystemRoleKindSlot = TransformerSystemRole@ValveSelectionContext`. In this source designation, `ValveSelectionContext` must resolve to the named practice or source boundary used to identify the local kind; the assertion may cite that boundary, but it is not an assignment participant.

**Normative guard:** Work-facing system-role kinds, including `TransformerSystemRole@ValveSelectionContext`, are local `U.Kind` values identified by their named practice or source boundary and stable contribution distinction. A declared `U.SystemRoleAssignment` species defines the holder and assigned-kind participant meanings, predicate, applicability, and occurrence identity. An occurrence supplies the holder System or acting holon, assigned local kind, any other participants, and extent. Epistemes do not acquire a system-role kind or assignment merely because they are used as references, evidence, constraints, sources, requirements, publications, or assurance inputs.

#### A.7:5.5 - Episteme vs publication carrier and source-currentness record

* **Episteme** — the knowledge content (claim, model, requirement set).
* **Publication carrier or source-currentness record** — the physical or digital carrier for an episteme publication or stored representation (file, volume, dataset item), tracked through A.10 carrier/source-currentness relations when evidence, source, or reliance use is current.
* **Use:** Evidence, provenance, and reproducibility address **carriers**; arguments and validity address **epistemes**.

**Normative guard:** When you say “we updated the spec”, detail **which carriers** changed (A.10).

#### A.7:5.6 - Collective vs Set, and MemberOf vs Component/Constituent/Portion/Phase (A.14)

* **Set / Collection (MemberOf)** — **mathematical or catalog** grouping; **no joint behaviour** implied.
* **Collective System** — a **system** with boundary and coordination Method (e.g., a team).
* **Use relations correctly:**

  * **ComponentOf** — mechanical/structural part in systems.
  * **ConstituentOf** — logical/content part in epistemes.
  * **PortionOf** — quantitative portion with conserved extensives.
  * **PhaseOf** — temporal part/state across a continuous identity.
  * **System-role assignment** — a **system or acting holon** is the `HolderSystemSlot` value in one obtaining occurrence of a directly admitted `U.SystemRoleAssignment` species.

**Normative guard:** If the grouping is expected to **act**, model a **collective system** (not a set) and provide its exact system-role kind and assignment when current, Method, and Work.

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
* **Bridge policy.** Cross-context or cross-reference-plane reuse cites **Bridge id + CL**; **Phi(CL)** and **Phi_plane** penalties apply to **R (trust)** only; **F and G invariant**.

#### A.7:5.8a - Same or near-same EntityOfConcern across descriptions and views

Different descriptions, views, viewpoints, publication units, or role-method-interest positions may concern the same `EntityOfConcern`, different entities of concern, or an unresolved candidate set. A.7 does not accept sameness by publication title, view label, carrier continuity, shared ordinary name, or common reader interest.

Use this split when the text needs to say whether two descriptions or views are about the same thing:

| Case | A.7 relation case | Admissible move |
| --- | --- | --- |
| same referent by value | the localized `EntityOfConcern` or relation named by value, carried by the current claim, or selected by a reference case and the resolved `entityOfConcernRef`, where live, refer to the same item by declared reference discipline | same-entity work inside the declared use |
| preserved by viewing | A.6.3 viewing preserves the exact EntityOfConcern while producing another episteme whose claim content or effective ReferenceScheme may differ; any representation relation and any viewpoint selected for a named describing use remain separate | same-EntityOfConcern Description, Specification, or view transformation |
| publication-unit primary only | a bounded publication unit states what it is mainly about, plus its carried move and outside-work boundary, without establishing a claim-bearing episteme trace by itself | publication-unit stability only |
| bridge-conditional near identity | An F.9 Bridge obtains, and a separate affirmative bounded-use claim names the proposed use, direction, correspondence rule, tolerated loss, and polarity. A practitioner may first use F.18 to settle the governed value's designations and, only when a durable term row is needed, then use F.17 to constitute that row; neither step establishes the Bridge or licenses reuse, while publication, evidence, and any reliance judgement remain separate. | bridge-scoped reuse only |
| retargeted under invariant | A.6.4 changes `entityOfConcernRef` under `KindBridge`, invariant, and loss discipline | retargeted use only under stated invariant |
| unresolved candidate | construction/reference/bridge/witness trace is insufficient | candidate tracking, question framing, or non-use |
| different entity | no admissible sameness or near-sameness path exists for the intended use | keep entities distinct |

If the same or near-same relation needs mathematical or postulate-theory justification, A.7 stops at the strict-distinction boundary instead of pretending to prove it: use C.29 for the mathematical lens, E.18 and E.18.1 where transformation-flow, carry-through, and postulate-theory work supply the required justification, E.18 where a gate crossing is the live relation, or the relevant architecture pattern where the comparison is about structure, graph, flow, or architecture description.

#### A.7:5.8b - Compact relation-position recovery aid

When one visible source-side carrier, publication face, diagram, dashboard, card, model output, `PublicationUnit`, rendering, or generated artifact can be read as several FPF values at once, use A.7 only to recover the current relation position. Name the current `EntityOfConcern`, Description episteme, view, publication face, publication form, `PublicationUnit`, carrier, rendering, mathematical-lens use, evidence relation, gate decision, work occurrence, authority-reference relation, source-currentness relation, or source-use claim, then apply the subject pattern for that position.

This aid is not a reusable object, local record, table, or master checklist. If the direct governed claim is already clear, do not add an A.7 recovery note; cite the direct pattern.

#### A.7:5.9 - Typed describing morphism and specification-use boundary (normative)

**What `Describe_EoC_DescEp` means in A.7.** For any `EntityOfConcern` value `X`, *describing X* is the morphism application `Describe_EoC_DescEp(X) : DescriptionEpisteme`. A.7 does not define a second strict-distinction arrow from Description to Specification. When a Description episteme is formalised, constrained, test-harnessed, accepted, or used as a specification, that is an episteme-refinement or specification-use question handled by A.6.2, C.2.3, A.21, C.16, E.17, E.10, or another neighboring pattern governing the claim according to the live force.

**Example.** A formal postulate theorem in physics can be a Description episteme about the behaviour of a physical grounding holon. Its formal language belongs to formality and publication-expression discipline. It becomes a specification only if a bounded use assigns specification force, such as acceptance criteria, harness checks, normative invariants, or verification use. Formal notation alone does not make it a third kind beside the physical `EntityOfConcern` and the Description episteme.

**Invariants (normative for A.7, split by EntityOfConcern kind):**
1. **Episteme-source preservation (DESC-1E).** When the `EntityOfConcern` value `X` is itself a `U.Episteme`, a claim graph, a claim-bearing view, or another claim-bearing source, `Describe_EoC_DescEp(X)` MUST NOT silently add epistemic commitments. Added structure is only declared representation, indexing, cross-reference, or refinement/loss under the neighboring pattern governing the claim that grants it.
2. **Non-episteme describing trace (DESC-1N).** When `X` is a system, structure, Work occurrence, system-role assignment, Method, physical object, characteristic, relation, or other non-episteme value, claims are not "inside X" waiting to be copied. A Description episteme may add claims about `X` only through a declared construction, reference, measurement, observation, model, postulate-theory, or witness trace, with admissibility conditions visible for the intended use.
3. **Identity and meaning preservation (DESC-2).** If `f : X -> Y` is a meaning-preserving, bridge-admitted, or construction-preserving map for the selected EntityOfConcern values, then `Describe_EoC_DescEp(f)` is defined only for the declared scope and preserves the exact identity, near-identity, bridge, loss, or retargeting relation established by its predicate and current facts. Where meaningful composition exists, `Describe_EoC_DescEp(f o g) = Describe_EoC_DescEp(f) o Describe_EoC_DescEp(g)` only under that declared relation.
4. **Specification-use refinement case.** If a Description episteme is refined into specification use, the refinement must name the neighboring pattern governing the claim and gate that grants that use. A.7 only requires that the refinement remains separate from the `EntityOfConcern`, from publication expression, and from Work.
5. **Separation from Gamma.** `Describe_EoC_DescEp` and any neighbouring specification-use refinement do **not** compose with **Gamma_method**, **Gamma_time**, or **Gamma_work**; describing, formalising, or specifying is not execution and accrues no resource or time semantics.
6. **Ontology preservation.** Describing any `EntityOfConcern` value, such as a Calculus, Signature, Mechanism, Structure, Work occurrence, or Episteme, via `Describe_EoC_DescEp` does **not** change its ontology; it yields a Description episteme under A.7 rules. Publication through faces, forms, units, and carriers is handled separately in E.17 (MVPK).

#### A.7:5.10 - Bridge to `U.Work` (normative invariants)

**OUTSPEC‑INV‑1 (No metonymy).**
`promisedOutcomeSpecRef` points to an **OutcomeSpec**, not to `U.Work` and not to an extensional delivered-result referent. The *actuals* live on `U.Work` (A.15.1) and its evidence carriers.

**OUTSPEC‑INV‑2 (Evaluability from work evidence).**
All predicates referenced by `workPredicateRef`, `postConditionRef`, and `unitOfDelivery.countingRule.*` MUST be evaluable from `U.Work` facts and cited evidence (including `U.Work.Δ` state records or evidence carriers). They MUST NOT require introspecting the internal structure of the provider system unless that structure is itself exposed as evidence.

**OUTSPEC‑INV‑3 (Counting coherence).**
If `unitOfDelivery` is present, its countingRule MUST select only work episodes that are eligible to satisfy the promise content and MUST not silently double‑count (use `dedupeKeyRef` or a cited policy).

##### A.7:5.10.1 - Canonical examples (didactic)

**Example 1 — Work‑only (promise the work): “provide consultation for ≥5 minutes”.**

```text
OutcomeSpec(OS‑Consult‑5min) := {
  mode: WorkOnly,
  workSpec: {
    methodConstraintRef?: ConsultationMethod,
    workPredicateRef: E‑(duration(work) ≥ 5 minutes)
  }
}

unitOfDelivery := {
  unitLabel: "minute",
  countingRule: {
    selectorRef: E‑(work fulfils OS‑Consult‑5min),
    quantityRef: E‑durationMinutes(work),
    aggregation: sum
  }
}
```

**Example 2 — Result‑only (promise the world state): “a hole of depth ≥ 1 m exists”.**

```text
OutcomeSpec(OS‑Hole‑1m) := {
  mode: ResultOnly,
  resultSpec: {
    deliveredResultReferentRef: kind(Hole),
    statePlaneRef: GeometryPlane,
    postConditionRef: E‑(depth(hole) ≥ 1 m ∧ location(hole) within SiteScope)
  }
}

unitOfDelivery := {
  unitLabel: "hole",
  countingRule: {
    selectorRef: E‑(work fulfils OS‑Hole‑1m),
    quantityRef: E‑1,
    aggregation: count,
    dedupeKeyRef: E‑holeId(work)         // prevents double counting when rework happens
  }
}
```

**Example 3 — Composite (promise both): “hairstyle for the evening, produced within 20 minutes, by cut+style (not a wig)”.**

```text
OutcomeSpec(OS‑Hair‑Evening‑20min) := {
  mode: Composite,
  workSpec: {
    methodConstraintRef: CutAndStyleNoWigMethod,
    workPredicateRef: E‑(duration(work) ≤ 20 minutes)
  },
  resultSpec: {
    deliveredResultReferentRef: kind(HairstyleOnClient),
    statePlaneRef: AppearancePlane,
    postConditionRef: E‑(looksLike(style="Evening") ∧ survivability(afterShower) ≥ acceptable)
  }
}

unitOfDelivery := {
  unitLabel: "session",
  countingRule: {
    selectorRef: E‑(work fulfils OS‑Hair‑Evening‑20min),
    quantityRef: E‑1,
    aggregation: count,
    dedupeKeyRef: E‑appointmentId(work)
  }
}
```

In these cards, each `methodConstraintRef` resolves directly to an admitted `U.Method`. Add a separate `methodDescriptionRef` only when the OutcomeSpec claim actually depends on claims in one exact A.3.2-admitted description edition; neither the constraint nor its reference creates that membership.

(Where `E‑(…)` is shorthand in these cards for a separately identified episteme or predicate under the card's named effective ReferenceScheme and ClaimScope; this appendix does not introduce an expression language.)

