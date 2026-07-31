---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:5"
section_title: "Solution — The Clarity Lattice (normative distinctions & safe vocabulary)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__006_solution-the-clarity-lattice-normative-distinctions-safe-vocabulary.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:5 — Solution — The Clarity Lattice (normative distinctions & safe vocabulary)"
line_start: 21381
line_end: 21584
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
  - "Role ≠ Work"
  - "category error"
  - "ontology"
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

#### A.7:5.2 - Role vs function-like wording, functional behaviour, capability, method, and work

* **Role (role value).** A context-bound work-facing role value assigned through `U.RoleAssignment` (A.2, A.2.1, A.15). A role value is **not behaviour**; it names the assigned work-facing position under which an acting system or holon may enact behaviour. Example: **CoolingCirculatorRole@Context** in a thermal loop.
* **Function-like wording.** A source phrase such as "function", "behaviour", "service", or "does X" may name a required transformation or effect (A.3.4), functional behaviour (A.6.F), a capability envelope, a method, performed work, a quality, or a structure. Recover the governed claim before choosing the FPF term.
* **Under role assignment.** A system or acting holon under a current `U.RoleAssignment` may have a **Capability** to enact a **Method** under conditions and may perform **Work** that produces, maintains, prevents, or checks a transformation/effect. The role is not the behaviour, Method is not identical to transformation/effect, and Capability is not the Method.

Safe rewrite for earlier "Holonic Duality (Substance vs Function)": **Holonic Duality (Substance vs Role).** A `U.System` keeps its identity while changing assigned role values; each assigned role value may require a Method, a Capability envelope to enact that Method under conditions, and possible Work occurrences.

**Normative guard:** Use **Role** for the role value, `U.RoleAssignment` for the assignment relation, **functional behaviour** when A.6.F governs the behaviour claim, **Method** for the abstract way-of-doing, **Capability** for a system ability/envelope to enact a Method under conditions, **Work** for the performed occurrence, and **Transformation** or effect wording when A.3.4 governs the change claim. Do **not** call the role itself a function, and do not define Method as Capability or as the transformation/effect itself.

#### A.7:5.3 - MethodDescription vs Method vs Capability vs Work (description vs way-of-doing vs ability envelope vs occurrence)

* **MethodDescription** — the **description** (algorithm / SOP / recipe / script) at design-time. Its publication cites A.10 carrier/source-currentness refs when the carrier is used as evidence or source.
* **Method** — the **abstract order-sensitive way-of-doing** composed with **Γ\_method** (B.1.5). A Method is not an occurrence and not the system ability itself; **concrete values** are **bound at `U.Work` creation**. Outside executions we **refer to it via MethodDescription** (see A.3.1 CC‑A3.1‑5/‑9; A.15 §2.2, §4.1).
* **Capability** — the **system ability/envelope** to enact a Method under stated roles, conditions, resources, and constraints. A Capability belongs to a system-in-context; it is not the MethodDescription and not the performed Work.
* **Work** — the **dated run‑time occurrence** (what actually happened), with resource spend (Γ\_work) and temporal coverage (Γ\_time).

**Normative guard:** Never use MethodDescription as evidence of Work; never present Method or Capability as if it had happened; never define Method as Capability.

#### A.7:5.4 - Holon vs System vs Episteme (who can act)

* **System or acting holon** — the entity that can enact behaviour when it is the holder of a current work-facing `U.RoleAssignment`.
* **Episteme** — **cannot act** and does **not** hold work-facing roles; it is changed via carriers, publications, and work on those carriers by systems or acting holons. Reference, constraint-source, evidence, status, source, requirement, publication, and assurance uses are direct relation/use cases, not episteme roles.
* **Holon** — umbrella term; **do not** use it where the current claim requires a system as role-assignment holder. Write the exact holder and `U.RoleAssignment(holderRef, roleRef, boundedContextRef)` when a work-facing role such as `TransformerRole@Context` is current.

**Normative guard:** Work-facing roles, including `TransformerRole@Context` when used, are role values in `U.RoleAssignment` and have a system or acting holon as holder in a bounded context. Epistemes do not hold roles merely because they are used as references, evidence, constraints, sources, requirements, publications, or assurance inputs.

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
  * **RoleAssignment** — a **system or acting holon** is the holder in a current `U.RoleAssignment`.

**Normative guard:** If the grouping is expected to **act**, model a **collective system** (not a set) and provide its role, Method, and Work.

#### A.7:5.7 - Operator alignment (required names)

* **Γ\_sys** — composition of **system** properties (physical/systemic).
* **Γ\_method** — composition of **Method** (order, branching).
* **Γ\_time** — composition of **Work** histories and temporal parts.
* **Γ\_work** — composition of **resource spend** and yields tied to Work. Do not track costs with Γ\_method; costs (resources/yield) belong to Γ\_work.

**Normative guard:** Avoid generic “process” for these operators. Reserve “process” for domain idioms; map internally to **Method** (design) and **Work** (run).

#### A.7:5.8 - EntityOfConcern and Description-episteme boundary vs publication face, form, unit, and carrier boundary (orthogonal, normative)
* **A.7 and E.10.D2 govern the EntityOfConcern-to-description boundary.** What the `EntityOfConcern` value is and how it is described are distinct questions. Description is a `U.Episteme` use with `DescriptionContext`. Specification is a gated use or refinement of a Description episteme, selected by checkability, formality plus checkable constraint, harness, acceptance, C.16 measurement criterion, verification use, or other neighboring pattern governing the claim force; it is not a peer class beside `EntityOfConcern` and Description.
* **Publication governs availability.** Publication units, publication forms, faces, renderings, and carriers make Description epistemes available to readers or tools, including Description epistemes admitted for specification use. They do not become the `EntityOfConcern` value, the Description episteme, the specification-use gate/refinement, or an evidence/source carrier by the same relation; physical and digital carriers stay in A.10 carrier/source-currentness relations when evidence, source, or reliance use is current.
* **Publication-face field pins.** When Description epistemes or Description epistemes admitted for specification use are shown on **TechCard**, the minimal **CHR-Pins** are {**UnitType**, **ScaleKind**, **ReferencePlane**, **EditionId**}.
* **Bridge policy.** Cross-context or cross-reference-plane reuse cites **Bridge id + CL**; **Phi(CL)** and **Phi_plane** penalties apply to **R (trust)** only; **F and G invariant**.

#### A.7:5.8a - Same or near-same EntityOfConcern across descriptions and views

Different descriptions, views, viewpoints, publication units, or role-method-interest positions may concern the same `EntityOfConcern`, different entities of concern, or an unresolved candidate set. A.7 does not accept sameness by publication title, view label, carrier continuity, shared ordinary name, or common reader interest.

Use this split when the text needs to say whether two descriptions or views are about the same thing:

| Case | A.7 relation case | Admissible move |
| --- | --- | --- |
| same referent by value | the localized `EntityOfConcern` or relation named by value, carried by the current claim, or selected by a reference case and the resolved `entityOfConcernRef`, where live, refer to the same item by declared reference discipline | same-entity work inside the declared use |
| preserved by viewing | A.6.3 viewing preserves `entityOfConcernRef` while changing content, representation, viewpoint, or other episteme slots | same-`EntityOfConcern` Description, Specification, or view transformation |
| publication-unit primary only | a bounded publication unit states what it is mainly about, plus its carried move and outside-work boundary, without establishing a claim-bearing episteme trace by itself | publication-unit stability only |
| bridge-conditional near identity | F.9, F.17, or F.18 admits bounded near-identity or substitution under bridge kind, CL, direction, loss, and bridge-admissible use | bridge-scoped reuse only |
| retargeted under invariant | A.6.4 changes `entityOfConcernRef` under `KindBridge`, invariant, and loss discipline | retargeted use only under stated invariant |
| unresolved candidate | construction/reference/bridge/witness trace is insufficient | candidate tracking, question framing, or non-use |
| different entity | no admissible sameness or near-sameness path exists for the intended use | keep entities distinct |

If the same or near-same relation needs mathematical or postulate-theory justification, A.7 stops at the strict-distinction boundary instead of pretending to prove it: use C.29 for the mathematical lens, E.18 and E.18.1 where transformation-flow, carry-through, and postulate-theory work supply the required justification, E.18 where a gate crossing is the live relation, or the relevant architecture pattern where the comparison is about structure, graph, flow, or architecture description.

#### A.7:5.8b - Compact relation-position recovery aid

When one visible source-side carrier, publication face, diagram, dashboard, card, model output, `PublicationUnit`, rendering, or generated artifact can be read as several FPF values at once, use A.7 only to recover the current relation position. Name the current `EntityOfConcern`, Description episteme, view, publication face, publication form, `PublicationUnit`, carrier, rendering, mathematical-lens use, evidence relation, gate decision, work occurrence, authority-reference relation, source-currentness relation, or source-use claim, then apply the direct governing pattern for that position.

This aid is not a reusable object, local record, table, or master checklist. If the direct governed claim is already clear, do not add an A.7 recovery note; cite the direct pattern.

#### A.7:5.9 - Typed describing morphism and specification-use boundary (normative)

**What `Describe_EoC_DescEp` means in A.7.** For any `EntityOfConcern` value `X`, *describing X* is the morphism application `Describe_EoC_DescEp(X) : DescriptionEpisteme`. A.7 does not define a second strict-distinction arrow from Description to Specification. When a Description episteme is formalised, constrained, test-harnessed, accepted, or used as a specification, that is an episteme-refinement or specification-use question handled by A.6.2, C.2.3, A.21, C.16, E.17, E.10, or another neighboring pattern governing the claim according to the live force.

**Example.** A formal postulate theorem in physics can be a Description episteme about the behaviour of a physical grounding holon. Its formal language belongs to formality and publication-expression discipline. It becomes a specification only if a bounded use assigns specification force, such as acceptance criteria, harness checks, normative invariants, or verification use. Formal notation alone does not make it a third kind beside the physical `EntityOfConcern` and the Description episteme.

**Invariants (normative for A.7, split by EntityOfConcern kind):**
1. **Episteme-source preservation (DESC-1E).** When the `EntityOfConcern` value `X` is itself a `U.Episteme`, a claim graph, a claim-bearing view, or another claim-bearing source, `Describe_EoC_DescEp(X)` MUST NOT silently add epistemic commitments. Added structure is only declared representation, indexing, cross-reference, or refinement/loss under the neighboring pattern governing the claim that grants it.
2. **Non-episteme describing trace (DESC-1N).** When `X` is a system, structure, work occurrence, role assignment, method, physical object, characteristic, relation, or other non-episteme value, claims are not "inside X" waiting to be copied. A Description episteme may add claims about `X` only through a declared construction, reference, measurement, observation, model, postulate-theory, or witness trace, with admissibility conditions visible for the intended use.
3. **Identity and meaning preservation (DESC-2).** If `f : X -> Y` is a meaning-preserving, bridge-admitted, or construction-preserving map for the selected EntityOfConcern values, then `Describe_EoC_DescEp(f)` is defined only for the declared scope and preserves the identity, near-identity, bridge, loss, or retargeting relation that the governing pattern admits. Where meaningful composition exists, `Describe_EoC_DescEp(f o g) = Describe_EoC_DescEp(f) o Describe_EoC_DescEp(g)` only under that declared relation.
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
    methodConstraintRef?: MD‑Consultation,
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
    methodConstraintRef: MD‑CutAndStyle‑NoWig,
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

(Where `E‑(…)` denotes an Episteme/predicate defined in the relevant Context; this appendix does not introduce an expression language.)

