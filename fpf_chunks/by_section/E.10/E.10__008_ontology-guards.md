---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:6"
section_title: "Ontology Guards"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__008_ontology-guards.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:6 — Ontology Guards"
line_start: 75146
line_end: 75314
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.10.MOVE"
  - "E.10.ROLE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.17"
  - "F.18"
  - "F.19"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
---

### E.10:6 - Ontology Guards

#### E.10:6.1 - Tech register ontology guards

> **Purpose.** This section stabilises the Tech register of the kernel lexicon by enforcing head-anchored naming, explicit kind naming, EntityOfConcern and Description-episteme boundaries, specification-use morphology, guarded use of bare *role*, exact `SystemRole` compounds, and subject-specific recovery of Domain wording. It aligns with **E.10.D1**, **F.4 SystemRoleKindDescription**, **A.2.5 SystemRoleAssignmentStateRelation**, **A.2.7 SystemRoleKindRelationStructure**, **F.11 Method Quartet Harmonisation**, and **F.17 UTS**. **Scope:** Guidance is register-agnostic and applies across the FPF; illustrative examples pass Minimal Generality and Domain Anchoring (MG-DA) and the other rules of E.10.
>
**Onto1 — Head‑anchoring**  *(use Kernel heads + pass LEX.TokenClass, EntityOfConcern and Description-episteme boundary, and specification-use gates)*
* **Rule:** The **head noun of a term explicitly signals the kind** (`System`, `Holon`, `Work`, `Episteme`, `Tradition`, `Lineage`, `Characteristic`, `Method`, `Profile`, `Description`, `Spec`, `TransformationFlowStructure`, `Card`, `Pack`, `Dashboard`, …). `SystemRole` is allowed only as the common compound inside one concrete context-local system-role-kind designation such as `ReviewerSystemRole`; bare *role* remains a recovery trigger rather than a kind head.
* **Figurative heads** with obvious overload (“Tradition”, “family”, “process”, “function”) are not admitted in the kernel. Plain twins are admitted only with a one-to-one Tech mapping and declared **`LEX.TokenClass`** for the Tech token. They appear in the Plain register as one-to-one mappings to a Tech token, not in the Tech register. Plain language minimizes lexical error from overloaded terms through plain-twin lexical guards.
  * **Do:** `IncidentDashboard`, `MethodSpec`, `TraditionProfile`, `TransformationFlowStructureDescription`.
  * **Don’t:** `IncidentBoard`, `TDD Tradition`, `Production Process` (kernel), `Service Function` (kernel).

 **Onto2 — EntityOfConcern and Description-episteme boundary and specification-use morphology**  *(ref. E.10.D2)*
* **Rule:** A term for the EntityOfConcern uses the bare head for the FPF kind under concern: `Method`, `Tradition`, `Characteristic`. A **Description episteme** appends **`…Description`** only under the membership rule of the pattern defining that episteme kind. In particular, a claim-bearing episteme is `U.MethodDescription` only when its exact EntityOfConcern is one admitted `U.Method` and it makes at least one substantive claim about that method as a way of doing. `Algorithm`, code, pseudo-code, recipe, procedure, diagram, or other expression form first remains source wording, a C.29 representation, or a publication expression; none establishes that membership. A qualifying Description episteme appends **`...Spec`** only after a named specification-use gate grants that use. Thus `MethodSpec` is available only when the same episteme passes both A.3.2 membership and the E.10.D2 specification-use gate; formal language, pseudo-code, or bundled tests alone settle neither condition.
* **Formal-description guard:** A formal mathematical or physical theorem, including a formal postulate theorem in physics, remains a Description episteme until a bounded use assigns specification use. Its formal language belongs to formality and publication-expression discipline; it becomes a specification only under acceptance criteria, harness checks, normative invariants, measurable anchors, verification use, or another specification-granting condition named by value.
* **Extension:** Apply the same morphology to non-method EntitiesOfConcern where appropriate: `TransformationFlowStructureDescription`, `TransformationFlowStructureSpec`, `SystemDescription`, and `SystemSpec`.
* **Do:** `SamplingMethod` - `SamplingMethodDescription` - `SamplingMethodSpec`.
* **Don’t:** `SamplingAlgorithm` (when it is just prose), `SamplingProcessSpec` (head not signalling kind).
**Onto3 — System-role kinds, assignments, and carrier-relation separation**  *(ref. E.10.ROLE, A.2, A.2.1, F.4, F.5, C.2.1+, C.2.P, E.17, A.10, and C.35)*
* **Positive distinction:** A system role is an exact context-local kind for entities already admitted under A.1 as `U.System`; a person, team, organization, or non-human technical object may qualify. Its Tech designation ends in `...SystemRole`, for example `ReviewerSystemRole`. The name creates no admission, assignment, agency, capability, or Work.
* **Assignment rule:** A system-role assignment is an obtaining occurrence of one directly declared species under `U.SystemRoleAssignment`. The species declaration defines `HolderSystemSlot`, the exact local system-role-kind domain of `AssignedSystemRoleKindSlot`, any other participant meanings, its predicate, applicability, and occurrence-identity rule. The occurrence supplies the actual holder System, assigned-kind value, any other participant values, and extent. An interpretation, taxonomy, scheme, description, display, or source-context episteme is not automatically an assignment participant; name it separately only when the assignment claim actually depends on it.
* **Readable example:** `TeamAlpha is classified under ReviewerSystemRole in JournalReviewContext.` Add `ReviewAssignment-42` only when the assignment itself matters and both its directly declared species and obtaining occurrence are recoverable. If performed Work is current, point to its complete A.15.1/F.6 basis. A short sentence may omit only an assignment identifier unused by the receiving claim; it does not omit a performer, Method, time, containing System, assignment occurrence, or F.6 attribution from the recoverable basis.
* **Carrier rule:** **Carrier** is not a free holon or system kind. Recover the direct carrier relation: use `U.PresentationCarrier` only under its C.2.1+ publication and presentation discipline; if a reusable carrier-relation declaration is separately current, `PresentationCarrierSlot` remains the declaration-local `SlotKind` of one A.6.5 `SlotSpec` and is not the carrier or relation. Other exits are a file, transport, rendering, front-end, or access-carrier relation under `E.17`; evidence or source-currentness carriage under `A.10` or `G.11`; generated or produced carriage under `C.35`; or a named episteme-symbol carrier relation independent of any system-role assignment.
* **Source-word rule:** Job titles such as *reviewer*, *owner*, and *lead* remain Plain or quoted wording until the current claim is recovered. Use `E.10.ROLE` for an ambiguous claim-bearing *role*. Use `...SystemRole` only for an exact local system-role kind, and preserve *owner* when an actual architectural, organizational, policy, source, or responsibility ownership relation is what the sentence states.
* **Do:** `ReviewerSystemRole`; `ReviewAssignment-42 : U.SystemRoleAssignment`; `LeanTraditionCarrier` only when its direct episteme-symbol carrier relation is declared.
* **Don’t:** `Reviewer` as a U-kind, `ReviewerCarrier` for an assigned system, an unqualified `...Role` Tech head, or `Carrier` as an unstated system kind.
**Onto4 — Recover what *domain* means in this use**  *(ref. E.10.D1 and F.17)*
* **Rule:** The word *domain* does not create a kernel kind, catalogue mark, family, bundle, or inheritance relation by spelling. Recover what *domain* names in the current claim—for example, a DPF subject, discipline, source-defined field, model domain, market, physical region, or policy extent—or keep it as ordinary prose when it carries no FPF-governed use.
* **Local-meaning rule.** When a durable domain expression carries source-local meaning, identify its source edition, effective `ReferenceScheme`, F.17 cell, and any obtaining basis relation. Use F.9 only for an independently obtaining Bridge between different semantic-context projections; state any proposed use separately.
* **Discipline boundary.** Use `U.Discipline` only when the claim satisfies the pattern that defines that kind. A domain label, shared vocabulary, or UTS row does not establish discipline identity.
* **DPF boundary.** A DPF states its domain subject, intended audience and use, source basis, scope, and qualification window under `E.4.DPF`; it need not invent `DomainFamily`, `DomainBundle`, or a list of Context identifiers.
* **Do:** “The Clinical Safety DPF addresses adverse-event analysis and device-labelling decisions for the stated audience and scope.”
* **Don’t:** infer `ClinicalSafetyDomain`, `DomainFamily`, or `DomainBundle` as a kind from that wording.

**Onto5 — Always state what the term names**
* **Rule.** The definition or first line of a gloss states the FPF kind or object named by the term—for example, a `U.Holon`, `U.System`, `U.Episteme`, `Tradition`, `Lineage`, `Profile`, exact context-local system-role kind, `U.Work` as the admitted kind or a Work occurrence admitted under it, `Characteristic`, or direct carrier relation.
* **Do:** “**Kind named:** `ReviewerSystemRole` — an exact context-local system-role kind for independently admitted systems that may receive review assignments. A concrete assignment names its directly declared species and one separately obtaining occurrence of that species under `U.SystemRoleAssignment`.”
* **Don’t:** “Reviewer — a person who …” (blurs the kind named).

**Onto6 — Bans and ontology recovery hints**  *(mirror E.10 § 9 L-rules; do not duplicate tables; not a substitution table)*
* `process`, `procedure`, `workflow`, `function`, or `activity` -> first recover the wording family: change-situation wording applies `A.3.4.P`; function-like wording applies `A.6.F`. Possible recovered values include `U.Method`, `U.MethodDescription`, `U.WorkPlan`, one dated Work occurrence admitted under `U.Work`, a separate episteme about it, `U.Transformation`, and `TransformationFlowStructure`. Choose among them only after naming the object, any obtaining method-side or other relation and its participants, the relevant declaration or representation use, or the claim kind and the pattern that defines it.
* `Tradition` → **`Tradition`** (Tech); leave “Tradition” only as a Plain twin with an adjacent Tech label.
* `domain` → **`DomainFamily` + {ContextId list} + UTS twins**.
* `…CarrierRole` used for an assigned System -> start with `E.10.ROLE`; recover the holder System, local `...SystemRole` kind, A.2.1 assignment occurrence, and its declared species only when the passage asserts those facts. Recover carrier, source-context, interpretation, publication, evidence-use, and Work claims through their own relations.
* ambiguous *owner* wording -> recover the precise relation or other claim being made—for example, an architectural, organizational, policy, source-maintenance, responsibility, authority, commitment, or work-facing claim. Keep *owner* when that precise ownership relation is current; use a `...SystemRole` designation only when the recovered object is an exact local system-role kind.
* job titles (`owner`, `lead`, `champion`) in the Kernel -> keep them in Plain or quoted wording until the claim is recovered; use exact `...SystemRole` designations only for admitted context-local system-role kinds.
* **Do:** `ReturnsTransformationFlowStructureDescription`, `Tradition: Test-Driven`; `LedgerTeam is classified under LedgerCustodianSystemRole`, with any exact assignment, responsibility, authority, source-maintenance, or interpretation relation stated separately when current.
* **Don’t:** `Returns Process`, `TDD Tradition` (kernel), `Ledger Owner` (underspecified).

**Worked mini-examples across arenas.** These names illustrate morphology only. Every `...MethodDescription` presupposes one claim-bearing episteme whose exact EntityOfConcern is one independently admitted `U.Method` and whose claims pass A.3.2; every `...Spec` also presupposes its subject-specific specification-use gate. The label establishes neither condition.

The Onto3 block above is the one bounded distinction and assignment example. The twelve rows below are morphology cues, not classification or assignment assertions. Read each candidate System label and candidate local system-role-kind label separately. Before asserting classification, pass C.3 and A.2; before saying an assignment obtains, admit the holder System and establish both the A.2.1 occurrence and its declared species. A schedule, place, office, desk, title, context cue, taxonomy, scheme, or interpretation episteme supplies none of those facts by wording.

| Arena | Morphology examples | Candidate system label | Candidate local system-role kind | Separate source cue or ambiguity | Avoid |
| --- | --- | --- | --- | --- | --- |
| Software engineering | `BuildTransformationFlowStructureDescription`, `CIHarnessSpec` | `RepoTeam` | `MaintainerSystemRole` | recover `RepoXContext` separately | `Build Process`, `Repo Owner` |
| Applied research and experimentation | `SamplingMethodSpec`, `CalibrationLineageCarrier` | `ReviewPanel` | `ReviewerSystemRole` | recover `GrantCallYContext` separately | `Sampling Algorithm` (if prose), `Lab Owner` |
| Production and service management | `ShiftWork`, `SafetyOfficerSystemRole` | `TeamAlpha` | `SafetyOfficerSystemRole` | recover `PlantOpsContext` separately | `Safety Officer` as a U-kind, `SafetyDomain Governance` |
| Operations research and optimisation | `RoutingMethodDescription`, `CostCharacteristic` | `AnalysisGroup` | `ModelStewardSystemRole` | recover `ORProgramContext` separately | `Routing Function`, `Model Owner` |
| Healthcare and clinical ops | `CarePathwayTransformationFlowStructureDescription`, `MedicationAdministrationWork` | `DrK` | `AttendingPhysicianSystemRole` | recover `Ward12Context` separately | `Care Process`, `Ward Owner` |
| Finance and accounting | `ReconciliationMethodSpec`, `JournalPostingWork` | `TreasuryTeam` | `TreasuryStewardSystemRole` | recover `LiquidityBookContext` separately | `Reconciliation Process`, `Account Owner` (underspecified) |
| Legal and compliance | `RetentionPolicySpec`, `InvestigationWork` | `PrivacyOffice` | `DataProtectionOfficerSystemRole` | recover `OrgXContext` separately | `Compliance Function`, `Data Owner` (underspecified) |
| Cloud and IT operations | `IncidentTransformationFlowStructureDescription`, `RunbookMethodSpec` | `OnCallEngineerTeamSystem` | `OnCallEngineerSystemRole` | `OnCallRotation` is schedule or roster wording under L-SCHED, not a holder; recover `ServiceYContext` separately | `Incident Process`, `Service Owner` (underspecified) |
| Logistics and supply chain | `PickingWork`, `RoutingMethodSpec` | `DispatchTeamSystem` | `DispatcherSystemRole` | `DispatchDesk` is an ambiguous desk label, not a holder; recover `HubZContext` separately | `Picking Process`, `Fleet Owner` |
| Construction and civil engineering | `PermitAcquisitionTransformationFlowStructureDescription`, `InspectionMethodSpec` | `SiteInspectionTeamSystem` | `SiteStewardSystemRole` | `SiteOffice` is an ambiguous place or office label, not a holder; recover `ProjectLot17Context` separately | `Inspection Process`, `Site Owner` |
| Emergency response | `TriageMethodDescription`, `EvacuationTransformationFlowStructureDescription` | `ResponderSystem-17` | `IncidentCommanderSystemRole` | `IncidentLead` is title-like role wording, not a holder; recover `EventRContext` separately | `Triage Function`, `Incident Owner` |
| Agriculture | `IrrigationTransformationFlowStructureDescription`, `SoilSamplingMethodSpec` | `FieldTeam` | `FieldStewardSystemRole` | recover `Plot17Context` separately | `Irrigation Process`, `Field Owner` |

**Checklist before minting a KernelToken**
* Head noun signals kind (Onto1).
* EntityOfConcern and Description-episteme boundary and specification-use morphology correct (Onto2).
* If system-role-related or carrier-related: local system-role kind, direct assignment species, and carrier relation remain separate; holder-system admission is explicit and the direct carrier-relation pattern is named (Onto3).
* Any action-changing Domain wording recovers its subject, use, and applicable pattern; a durable local expression uses F.17 only when its source-local meaning or public term row is current (Onto4, Onto6).
* Object‑of‑talk declared (Onto5).
* SCR-LEX rewrites checked for current system-role-kind, direct assignment-species, and carrier-relation separation (Onto6).
> **Note on registers.** Keep figurative or business-casual terms in the **Plain** register only, with strict **twin-label** links to the Tech token under current `E.10`. In the **Tech** register, speak in KL-CAL: **episteme-about-epistemes** (Tradition, Lineage, Profile), not in catalogue-admin idioms.

* **Onto‑Deon — Deontic lexicon guard (Core register)**
**Rule.** In the Conceptual Core, avoid using **“Standard”** as the head noun of an EntityOfConcern name unless the object is an explicit **deontic speech-act** under the **Gov** lens (cf. E.3).

For interface and boundary invariants concerning things such as holons, interfaces, and ports, name the exact invariant, compatibility condition, compliance profile, acceptance specification, or interoperability profile by value—for example `InterfaceCompatibilityCondition`, `ComplianceProfile`, `AcceptanceSpec`, or `InteropProfile`. State any promise or commitment separately; naming does not make it a property of the thing.

Use the word **standard** for a publication of a Description episteme, possibly admitted for specification use, that is *intended to be complied with* and has explicit compliance checks.

If an EntityOfConcern-side item is currently named `… Standard`, rename it to a proper EntityOfConcern-side name, and (optionally) add a separate publication of the relevant Description episteme under the needed compliance or specification use that contains the standard text and the intended compliance checks.
 **Rewrite hints (Tech → Tech).**
 `publication Standard` → `publication standard`;
 `frame Standard` → `frame standard`;
 `measurement Standard` → `measurement standard`;
 `Method Interface Standard (MIC)` → `Method Interface Standard (MIS)`;
 `Boundary-Inheritance Standard (BIC)` → `Boundary-Inheritance Standard (BIS)`.
 **Rationale.** Keeps Core prose centred on EntitiesOfConcern and their boundary invariants; reserves deontic obligations for governance contexts and **U.PromiseContent**‑like promises. Do **not** misuse “plane”: deontic speech‑acts are analysed via the **Gov** lens, while **ReferencePlane** remains `{world | concept | episteme}`.

#### E.10:6.2 - Twin‑Register Discipline (Tech and Plain)

**Plain twin (LEX).** A registry entry pairing the **authoritative Tech label** with a **display-only Plain label** for one governed Tech meaning in one `U.BoundedContext`: an admitted durable U-kind, C.3 `U.Kind`, Concept-Set row, imported signature symbol, or other directly governed value. Governed by **PTG (Plain Twin Governance; in the LEX registry)** and referenced by `Twin-Map ID (LEX)`. *“Plain twin” ≠ the **Plain register** (the register is where twins may be used; the twin is the 1:1 mapping).*
**Convention.** In this spec, **Plain** (capitalized) names the register; **plain twin** (lowercase) names the 1:1 mapping entry.

> **Rule R-0 (Registers).** Every Kernel and extension-pattern concept has a **Tech label** (the testable semantic token) and an optional **Plain label** (didactic synonym). The **Tech label is authoritative**; the Plain label is admitted only in expository text and maps one-to-one to the Tech meaning inside the current **Context**.

##### E.10:6.2.1 - Allowed pairs (normative table; examples)

| **Tech (authoritative)** | **Plain (didactic)**                        | **Notes and guards**                                                                           |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `U.System`               | system, machine, team                        | Bare “service” is **never** a safe Plain twin for `U.System`. Apply L-SERV only when a relied-on use hides the concrete subject or next route, then use `A.6.P:4.11a`; quoted, historical, illustrative, and harmless ordinary wording stays outside. Avoid “service-instance”; after recovery use “system instance”, “service access point”, “service offering”, or another head phrase supplied by the pattern for the recovered claim. |
| `U.Episteme`             | body of knowledge, document, dataset, model | The pair preserves the **Carrier and Content** distinction (A.7).                                              |
| `U.Method`               | how‑to, procedure (abstract)                | Do **not** call this “process” (L‑PROC).                                                     |
| `U.MethodDescription`    | account of how one identified method is done | `recipe`, `SOP`, `playbook`, `code`, and `spec-text` are recognition cues, not automatic twins. Use this pair only after the claim-bearing episteme has one admitted `U.Method` as its exact EntityOfConcern and passes A.3.2's substantive-description threshold; call out **Spec** separately only after the E.10.D2 gate. |
| `U.Work`                 | work (work kind)                           | This plain twin names the admitted kind only. A run, execution, activity, job, or case can name one Work individual only after A.15.1 grounds that occurrence; show an explicit occurrence name and the head **work occurrence** rather than reusing the kind twin. |
| one exact local `...SystemRole` kind | reviewer (system role), maintainer (system role) | Context-local kind for entities independently admitted as `U.System`; the Plain wording is local and first-use guarded. It creates no system admission or assignment. |
| `U.PromiseContent`              | promise, offering, service offering         | Never equate to provider system or API (L‑SERV).                                             |
| `U.Capability` | ability, capacity (within bounds) | Separate from a system-role kind, system-role assignment, Method, and Work; carries its own envelope and measures. |
| `U.Dynamics`             | law of change, model of evolution           | Not a capability or a method.                                                                |

**R‑1 (Plain first-use).** At first use in a section, show the **Tech label** and, optionally, the Plain twin only after membership is known: *"...one `U.Method` (the **how-to**); and, when a separately identified claim-bearing episteme has that method as its exact EntityOfConcern and passes A.3.2, one `U.MethodDescription` (an **account of that how-to**, sometimes called a recipe)..."*
**R-2 (No unpaired Plain in CC).** Conformance Checklists use **Tech labels** only.

Domains can mint aliases inside their `U.BoundedContext` glossary; each alias maps one-to-one to a Tech label through a **SenseCell** row in the Context's **Concept-Set Table** and, when exported across Contexts, through an **Alignment Bridge** with congruence-level and loss fields.

 Make “plain twins” (reader-friendly labels) **safe by construction**, not just style. The plain twin preserves kind, scope, and reader expectations of the canonical Tech name; it is **display-only** and **context-local**.

* **Tech name (tech)** — the canonical, kernel-conformant label used in **normative** clauses (for example `U.SystemRoleAssignment`, `TransformerSystemRole`).
* **Plain twin (plain)** — a didactic **display alias** permitted in **expository** prose and UI display contexts **inside one `U.BoundedContext`**.

> **Principle:** *Meaning lives in the Tech name; the plain twin may never move meaning.* (Locality is enforced by `U.BoundedContext` and Bridges.)

##### E.10:6.2.2 - Plain Twin Safety constraints (normative)

**CC‑TWIN‑1 - One‑to‑one and local.**
Each Tech name has **at most one** plain twin **per `U.BoundedContext`**; one plain twin points to at most one Tech name in the same Context.

**CC‑TWIN‑2 - Sense‑equivalence proof.**
A plain twin binds to the **same SenseCell** as its Tech name in that Context (F.3 and F.7). Its SenseCell notes include at least one **counterexample test** showing how the twin could be misread and why it still passes in this Context.

**CC‑TWIN‑3 - Head‑term discipline (HND).**
The plain twin preserves the **head term** of the Tech name or appends an explicit bracketed head on **first use**:

* A Plain twin for one exact local system-role kind keeps **“(system role)”** and names its Tech designation on first use. Bare *role* is not a Plain twin for a universal kind. When *service* or *access* still hides its object or relation, follow L-SERV and A.6.P:4.11a; after recovery, keep that object's or relation's head. Methods keep **“(method)”**, `U.Work` as a kind keeps **“(work kind)”**, one Work individual keeps **“(work occurrence)”**, a separate episteme about it keeps **“(work record)”** only when its Tech name denotes that record, and Capability keeps **“(capability)”**.
  *Examples:*
  `TransformerSystemRole` → “**Transformer (system role)**”,
  `U.PromiseContent` → “**post-op monitoring service promise (promise content)**”; an exact access relation → “**service access (access relation)**”,
  `U.Work` -> **work (work kind)**; `PumpInspection_2026-07-22T0900` -> **inspection work occurrence**; `PumpInspectionRecord_2026-07-22` -> **inspection work record** only when that Tech name denotes a separate episteme.

**CC‑TWIN‑4 - Kind‑consistent.**
A plain twin does not map across **Kinds** (C.3). If the twin's everyday interpretation can denote a different Kind (e.g., *Tradition* = organization, corpus, domain), it is admitted only with a bracketed head and **Context gloss** on first use (see CC-TWIN-7).

 **CC‑TWIN‑5 - Ambiguity stop‑list.**
The following base nouns are **reserved** and are not admitted as unqualified plain twins: *Tradition, service, process, function, model, system, method, standard, library, dataset, evidence, activity, task, action*.
They are allowed **only** with an explicit head per **CC‑TWIN‑3** and a **Context gloss** (CC‑TWIN‑7). *(This list MAY be extended in the registry.)*

**CC‑TWIN‑6 - No cross‑context by label.**
Plain twins are **not portable**. Reuse in another `U.BoundedContext` is admitted through a **Bridge** with CL and loss notes; names alone carry no authority.

**CC‑TWIN‑7 - First‑use gloss.**
At first occurrence in a document or screen, show a plain twin as **“Plain twin [Tech name] - Context gloss”**, e.g.:
“**Transformer (system role)** \[**TransformerSystemRole**] — *one local kind for systems already admitted under A.1 and eligible for the stated transformer assignments in `OR_2025`; classification creates neither an assignment nor Work. An assignment claim names both an A.2.1 occurrence and its declared `U.SystemRoleAssignment` species*”.

**CC-TWIN-8 - Normative publication-form overread ban.**
Plain twins are not admitted in **Conformance Checklists, predicates, type signatures, or acceptance clauses**. Only Tech names are normative; Plain twins are strictly didactic.

**CC‑TWIN‑9 - Twin budget.**
**At most one** plain twin per Tech name per Context. Synonym piles are non-conformant because they create uncontrolled vocabulary sprawl (see F.14).

**CC‑TWIN‑10 - Registry entry and DRR.**
Every admitted plain twin has a **registry entry** in the LEX registry recording `tech`, `plain`, `context`, `head`, **SenseFidelity = {3,2,1,0}**, ambiguity notes, counterexamples, and DRR id. A change opens a **DRR**.

**CC‑TWIN‑11 - Tests.**
 Twin entries pass the **Twin Harness** (see F.15): *Head term*, *Kind consistency*, *SenseCell match*, *Stop-list compliance*, and *First-use gloss*.

