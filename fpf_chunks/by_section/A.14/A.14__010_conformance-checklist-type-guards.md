---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:9"
section_title: "Conformance Checklist - type guards"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__010_conformance-checklist-type-guards.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:9 — Conformance Checklist - type guards"
line_start: 24100
line_end: 24199
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27.TA"
  - "C.29"
  - "C.3"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
keywords:
  - "AspectOf"
  - "ComponentOf"
  - "ConstituentOf"
  - "PhaseOf"
  - "PortionOf"
  - "aspect"
  - "belongs to"
  - "component"
  - "constituent"
  - "member"
  - "part"
  - "phase"
  - "portion"
---

### A.14:9 - Conformance Checklist - type guards

#### A.14:9.1 - Global firewall and scope

| ID            | Requirement                                                                                 | Purpose                                                 |
| ------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **CC-A14-0** | A local system-role kind **MUST NOT** occur as a node in any `partOf` chain by kind identity; a `U.System` classified by that kind remains eligible for holon mereology on its independent system identity. `U.Method` **MUST NOT** occur in A.14 structural `ComponentOf` or structural `partOf` chains by method identity alone; A.3.1 and B.1.5 define submethod assembly. If an exact admission predicate establishes a different carrier, such as a `SystemRoleKindDescription`, Work occurrence, `U.SystemRoleAssignment` occurrence, `SystemRoleKindRelationStructure`, method relation structure, or episteme, name that carrier, assertion, and subject-pattern locator. | Keeps local system-role kinds out of holon mereology by kind identity and keeps method holarchy out of structural component mereology while preserving admitted carriers. |
| **CC‑A14‑0a** | `U.MethodDescription` / `U.WorkPlan` and other describing epistemes **MAY** participate in `partOf` only as `U.Episteme` nodes: content `ConstituentOf`, measured text `PortionOf`, or `PhaseOf` for a proper interval of one unchanged C.2.1 identity. A changed C.2.1 discriminator identifies another episteme; connect two such identities only through an independently obtaining `EpistemeEditionRelation`. They **MUST NOT** be asserted as `ut:StructPartOf` of any `U.System`. | Allows episteme structure and legitimate temporal restriction without smuggling Methods or automatic edition continuity into structure. |
| **CC‑A14‑0b** | A collection-belonging relation **MUST NOT** be inferred or auto-rewritten as any `partOf` sub-relation. This non-inference does not prohibit a separately grounded constructive part relation for the same entities. | Separates collection belonging from parthood without assuming they can never coexist. |
| **CC‑A14‑0c** | `SerialStepOf` / `ParallelFactorOf` **MUST NOT** appear in any `partOf` chain or table in A.14; model order and concurrency potential via **A.15** and direct method-composition patterns such as `B.1.5`. If a node linked by those relations is also a submethod, state that `U.Method` claim separately before using method holarchy. | Prevents the “order‑as‑structure” and “edge-as-part” category errors.       |

#### A.14:9.2 - PortionOf guards

| ID                                 | Requirement                                                                                                                                                               | Purpose                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **CC‑POR‑1 (Domain)**              | `PortionOf(x,y)` is valid only if the modelling scope declares at least one **extensive measure** μ for y (mass, volume, token count, byte size, wall‑time budget, etc.). | Prevents “portion” without a measure.   |
| **CC‑POR‑2 (Kind)**                | x and y **SHALL** share the same μ‑kind and compatible units (or an explicit conversion).                                                                                 | Prevents apples‑to‑oranges addition.    |
| **CC‑POR‑3 (Monotone additivity)** | For disjoint portions `x ⟂ z` with `PortionOf(-,y)`: μ(x ⊔ z) = μ(x)+μ(z).                                                                                                | Secures Σ‑reasoning and Γ\_sys proofs. |
| **CC‑POR‑4 (Boundary)**            | For physical systems, the whole’s boundary encloses the union of portions; cross‑boundary flows are **not** portions.                                                     | Distinguishes stock vs flow.            |
| **CC‑POR‑5 (Non‑replacement)**     | “Replacing 20% of y by v” **MUST** be modelled as **PortionOf** removal + **Component/Constituent** insertion, not as a single PortionOf rewrite.                         | Avoids silent identity change.          |

#### A.14:9.3 - PhaseOf guards

| ID                                    | Requirement                                                                                                                                                      | Purpose                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **CC‑PHA‑1 (Proper interval & carrier identity)** | `PhaseOf(x,y)` requires `x ≠ y`, a proper sub-interval of y's interval, and an explicit identity criterion for y valid throughout both restrictions (e.g., serial number, legal identity, theorem statement). | Excludes self/whole-lifetime phasing and prevents re-identification by stealth. |
| **CC‑PHA‑2 (Nesting & overlap)** | Nested or overlapping `PhaseOf` values for one carrier **MAY** obtain. Do not infer a partition, aspect difference, or carrier difference merely from overlap. | Keeps universal temporal parthood consistent and permits ordinary windows. |
| **CC‑PHA‑3 (Selected partition)** | If a claim selects an exhaustive partition, it **MUST** name one carrier, covered interval, aspect or partition rule, and family of phase cells. Only cells of that same selected partition are required to be pairwise non-overlapping and jointly cover the declared interval. | Makes coverage and non-overlap local to the claim that needs them. |
| **CC‑PHA‑4 (Escalation)**             | If identity criteria fail during change, declare a **Meta‑Holon Transition** (B.2) instead of PhaseOf.                                                           | Makes re‑identification explicit.      |
| **CC-PHA-5 (Episteme & Work boundary)** | `PhaseOf` **MAY** restrict one unchanged `U.MethodDescription` episteme to a proper interval only after its C.2.1 identity triple remains fixed. Changed description epistemes use `EpistemeEditionRelation` only when C.2.1's historical-continuation predicate obtains. Work intervals, episodes, performed parts, retries, resumptions, and later occurrences **SHALL** use A.15.1's exact relations; generic `PhaseOf` is not their substitute. `PhaseOf` never applies to a local system-role kind by kind identity or to `U.Method`. | Keeps episteme identity, edition continuity, and Work-temporal law with their subject patterns. |

#### A.14:9.4 - AspectOf guards

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-ASP-1 (Participants and rule)** | Name the aspect and bearer in the `U.Holon` parthood domain, the facet rule, the relation occurrence, and the aspect-identity rule. The relation grants neither systemness nor independent-whole status. | Prevents an aspect label from admitting its own object. |
| **CC-ASP-2 (Obtaining)** | The facet rule must state what distinguishes the aspect and what change preserves or ends it. A chosen concern, Characteristic, viewpoint, view, projection, partition, label, or temporal window establishes no `AspectOf` occurrence. | Keeps selection and description from becoming world-side parthood. |
| **CC-ASP-3 (Relation properties)** | `AspectOf(x,y;f)` implies one asymmetric `ut:StructPartOf(x,y)` occurrence with `x != y`. Infer neither another facet occurrence, transitivity, ComponentOf, ConstituentOf, PortionOf, PhaseOf, collection belonging, nor independent systemhood. | Keeps the relation facet-local and non-omnibus. |
| **CC-ASP-4 (Identity and assurance)** | Bearer reidentification or failure of the facet and aspect-identity rule ends the old occurrence. A direct claim needs no B.3.5 fields; after profile election it uses one current `C.13 slice` trace and `validationMode=axiomatic`. | Keeps occurrence identity and optional assurance separate. |

#### A.14:9.5 - Grounding and validation (normative)

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-GND-1** | A direct `ut:StructPartOf` assertion is usable without this assurance profile. When its publication elects B.3.5 or a named current requirement demands that profile, the assertion must use `validationMode=axiomatic` and link through `tv:groundedBy` to its applicable current C.2.1 `sum` or `slice` construction trace. The trace reports independently grounded participants, direct relation occurrences, the construction rule, and identity or reidentification conditions; it creates none of them. | Makes an elected assurance basis inspectable without making it the relation's truth-maker. |
| **CC-GND-2** | For epistemic edges (`ut:EpiPartOf` and its sub-types), `tv:groundedBy` is optional; instead supply `ev:evidence` and set `validationMode in {axiomatic, postulate, inferential}`. | Harmonises evidence treatment for epistemic edges. |
| **CC-GND-3** | The public query Standard remains `?x ut:PartOf+ ?y`; every result still depends on its direct relation semantics and identity. Alias, trace, or validation mode creates or reidentifies no occurrence. | Preserves one query surface without moving authority into assurance apparatus. |

*Note.* Property names and trace semantics are defined in CT2R-LOG and Compose-CAL.

#### A.14:9.6 - Collection belonging and separately grounded parthood

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-MEM-1** | State collection belonging with the predicate defined for that subject. Name the entity, collection, collection identity rule, what makes belonging begin and end, whether it can recur, and how past belonging is said. | Keeps unlike fleets, corpora, communities, populations, products, and Suites under their own rules. |
| **CC-MEM-2** | From collection belonging alone infer neither a constructive part relation nor holonhood. Also do not infer that either is impossible. | Separates non-implication from universal prohibition. |
| **CC-MEM-3** | If the same collection independently passes all six `A.1` matters and a constructive part relation obtains, publish that second claim under its direct pattern. A direct belonging sentence needs no B.3.5 fields. When B.3.5 assurance is elected for it, use `validationMode=axiomatic` and one current `C.13 set` trace; the trace reports the collection, entities, relation occurrences, rule, and identity conditions and creates none of them. | Keeps collection belonging, constructive parthood, assurance, and collective action separate. |

#### A.14:9.7 - CT2R‑LOG handshake (Working‑Model → Assurance)

| ID                 | Requirement                                                                                                                                                              | Purpose                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **CC-A14-10** | A published direct relation may remain usable without B.3.5 fields. When its publication elects B.3.5, follow the relation's branch: structural parthood links its current `sum` or `slice` construction trace, while collection belonging links one current `C.13 set` trace under the collection's own rule; both declare `validationMode=axiomatic`. The direct relation and identity tests remain decisive; trace and mode create neither occurrence nor identity. | Keeps direct use lightweight while making an elected assurance posture inspectable. |
| **CC‑A14‑11**      | **PhaseOf** edges **SHALL NOT** use Γ_m for grounding. The relation record **SHALL** provide identity and proper-interval criteria per **CC‑PHA‑1/2**; a selected exhaustive partition additionally follows **CC‑PHA‑3** and references **Γ_time** when ordering matters. | Keeps temporal parthood distinct from construction and partition-specific constraints.       |

#### A.14:9.8 - Relation-use decision procedure

**Step 0 — Recover the claim.** If the sentence concerns system-role-kind classification or assignment, Method, Work, evidence, a Characteristic, viewpoint, view, projection, partition, or temporal claim without parthood, use that direct pattern. A.14 is not selected merely because ordinary speech says *part* or *aspect*.

**Step 1 — Is it measured stuff or extent?** If yes, use **PortionOf**. Declare μ, unit, boundary, and additivity conditions.

**Step 2 — Is it a discrete integrated or conceptual part?** If yes, use **ComponentOf** or **ConstituentOf**. Do not use PortionOf merely because the part can also be measured.

**Step 3 — Is it the same carrier during a proper sub-interval?** If yes, use **PhaseOf** after the carrier-identity and interval tests. Another episteme or Work occurrence uses its own identity and relation patterns.

**Step 4 — Is it a bearer-dependent structural aspect?** Use **AspectOf** only after naming the aspect, bearer, facet rule, relation occurrence, and aspect-identity rule. If the source names only a Characteristic, viewpoint, view, projection, selected partition, concern, or time window, return that actual claim instead.

**Step 5 — Does the entity belong to a collection?** Use the belongs-to rule defined for that collection after naming the entity, collection, beginning, ending, recurrence, and history conditions. Infer neither part nor holonhood and do not infer that separately grounded parthood is impossible. If collective action is current, apply all six A.1 matters separately.

**Quick spot-tests.**

| Smell | Likely error | Fix |
| --- | --- | --- |
| “20% of the chassis” | Structure is treated as stuff. | Use ComponentOf for the chassis part; use PortionOf only for material stock under one measure. |
| “Chapter 2 is 15% of the book” | Content assembly and text measure are collapsed. | Use ConstituentOf for the chapter and a separate PortionOf measurement statement. |
| “Safety is an aspect of the design.” | Characteristic, concern, viewpoint, or structural aspect remains unresolved. | Recover the actual claim. Use AspectOf only with an identified aspect, bearer, facet rule, occurrence, and identity condition. |
| “The dashboard slice is an aspect of the reactor.” | A view or projection is made into a world-side part. | Use the view, publication, or representation pattern; add AspectOf only for an independently established reactor aspect. |
| “Spec v2 overlaps v1.” | A version label is asked to decide identity and phase. | Compare C.2.1 identities and test edition continuity; use PhaseOf only for one unchanged episteme over a proper interval. |
| “Team is part of the project.” | Collection belonging is confused with constructive parthood. | State the affiliation rule. If an integrated whole is also claimed, apply all six A.1 matters and state the part relation separately. |

#### A.14:9.9 - Interplay with Γ‑flavours (how these relations behave under aggregation)

| Γ‑flavour                    | Mereological hooks (what A.14 supplies)                                                                                                                | Key effect                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Γ\_sys (B.1.2)** | Treat PortionOf as additive stocks; ComponentOf respects boundary integration; AspectOf remains facet-local structural parthood and is not a separate aggregation operator; PhaseOf is not aggregated here. | Conserves extensive measures and prevents facets from becoming system decompositions. |
| **Γ\_epist (B.1.3)** | PortionOf of text or data uses a declared measure; ConstituentOf composes arguments or sections; AspectOf is available only for an independently admitted episteme-dependent structural aspect under a declared facet rule. A viewpoint, view, heading, or projection remains with E.17 or C.29. PhaseOf may restrict one unchanged episteme to a proper interval. | Preserves provenance and prevents description choices from creating episteme parts. |
| **Γ\_ctx / Γ\_time (B.1.4)** | **PhaseOf** supplies proper temporal restrictions, including nested or overlapping windows. A separately selected partition supplies non-overlap and coverage only for its own cells. Order/dependencies live in **Γ\_ctx** and method graphs (A.15/B.1.5). **PortionOf** is orthogonal (quantities inside steps/runs). | Ensures chronological consistency without turning every temporal restriction into one partition. |
| **Γ\_method (B.1.5)** | Γ\_method composes Methods rather than A.14 structural parts. A recipe-labelled claim-bearing episteme is a **MethodDescription** only when its `EntityOfConcern` is one admitted `U.Method` and at least one substantive way-of-doing claim obtains under A.3.2; any graph form is a representation handled by C.29, not evidence that the Method belongs to a collection. When a recipe refers to stuff-like inputs, those are **PortionOf** statements on resources. | Separates recipe composition from structure. |
| **Γ\_work (B.1.6)**          | Only **Work** carries resource deltas; when logging “consumed 5 kg from Tank A”, model it as **PortionOf** relation to the stock prior to consumption. | Makes Σ‑balance explicit; aligns with CC‑POR‑3/4.                                             |

