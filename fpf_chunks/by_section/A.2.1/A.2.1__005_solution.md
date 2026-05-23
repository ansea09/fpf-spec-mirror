---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment: Contextual Role Assignment"
section_id: "A.2.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__005_solution.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.2.1 — U.RoleAssignment: Contextual Role Assignment"
  - "A.2.1:4 — Solution"
line_start: 1756
line_end: 2002
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2"
  - "D.CTX"
  - "E.10.D1"
  - "E.10.D2"
  - "U.BoundedContext"
keywords:
  - "RCS/RSG"
  - "RoleEnactment"
  - "Standard"
  - "context"
  - "holder"
  - "role"
---

### A.2.1:4 - Solution

#### A.2.1:4.1 - Canonical definition (notation‑free)

**`U.RoleAssignment`** is a **context-local assignment**:

```
RoleAssignment ::=
  〈holder: U.Holon,
   role: U.Role,
   context: U.BoundedContext,
   window?: U.Window,
   justification?: U.Episteme,
   provenance?: U.Method〉
```

**Admissibility constraints (concept‑level; non‑deontic).**

* **Invariant RA‑1 (Locality).** `role ∈ Roles(context)`. The role’s meaning is exactly the one recorded in that Context’s RoleDescription/RoleSpec.
* **Invariant RA‑2 (No role‑of‑role).** `holder : U.Holon` and `holder ∉ {U.Role, U.RoleAssignment}`. (Roles/assignments are never holders.)
* **Invariant RA‑3 (Eligibility by role kind).**
  * **Behavioural roles** (agential/transformer/observer/speech and their refinements): `holder` is a `U.System`. Only systems can enact Methods and produce Work.
  * **Status roles** (epistemic‑status / normative‑status / service‑governance): `holder` is a `U.Episteme`. Epistemes never enact Work; they gate and justify.
  * Context refinements may tighten eligibility (e.g., “Approver must be human”) but are restrictions of the System/Episteme split (they do not weaken it).
* **Invariant RA‑4 (Window discipline).** If `window` is present, enactments occur within it. If `window` is absent, interpret the assignment as open‑ended **from an assignment time that is still traceable** (e.g., via an issuing `U.RoleAssigning` SpeechAct Work or other evidence).
* **Invariant RA‑5 (Separation).** A RoleAssignment confers **the capacity/authorization to act** (or the status to be recognised), but it is **not behaviour** (no Work implied), **not capability** (intrinsic ability lives elsewhere), and **not structure** (it does not participate in BoM / part‑of structure).

**Governance metadata (optional but first‑class when present).**

* `justification` carries *why* the assignment is valid in this Context (policy, standard, evidence Episteme).
* `provenance` carries *how* the assignment was issued or verified (method reference; may link to a `U.RoleAssigning` work step in the evidence graph).

**Didactic read.** Think **badge** (*who wears which mask, where, when*). The rules for the mask live **in the room** (Context).

**Two assignment modes.**
A RoleAssignment can be:
(a) Authoritative — issued by an authority or policy in the Context (often via a `U.RoleAssigning` SpeechAct Work); it can open a Green‑Gate for steps that require explicit authorization.
(b) Observational — an evidence‑backed classification that the holder occupies a Role in this Context (e.g., “Moon as SatelliteRole:IAU_2006”). Observational assignments never by themselves open operational Green‑Gates; they can gate decisions and analysis.

#### A.2.1:4.2 - Role Enactment (distinct from the assignment)

**`U.RoleEnactment`** captures the *run‑time* fact that **a specific piece of Work** was performed under **a specific Role Assignment**:

```
RoleEnactment ::= 〈work: U.Work, by: U.RoleAssignment〉
```

**Admissibility constraints (concept‑level; non‑deontic).**

* **Invariant RE‑1 (Actor reality).** `by.holder : U.System`. (Epistemes never enact Work.)
* **Invariant RE‑2 (Temporal fit).** `work.window` overlaps `by.window` (or `by.window` is open and contains `work.window`).
* **Invariant RE‑3 (Method gate).** For the `MethodStep` realised by `work`, `by.role` satisfies the step’s `requiredRoles` in that **same Context** (directly or via `≤` specialization inside the Context).
* **Invariant RE‑4 (Traceability shape).** `U.Work` records cite the performer as `performedBy = some U.RoleAssignment`. `U.RoleEnactment` is the conceptual (or derived) association `〈work, work.performedBy〉`; if a system persists it explicitly, it is 1:1 with Work.

*Reading:* **Assignments authorize; enactments happen.** That single sentence prevents months of muddled logs.

Role Enactment is the occurrence of `U.Work` performed by a `holder` while a valid `U.RoleAssignment` for the required Role is in an enactable state of its RoleStateGraph (A.2.5) within the same Context. Enactment is generic: it includes operational work (e.g., actuation) and communicative work (speech acts such as approvals).

#### A.2.1:4.3 - Role Characterisation Space (RCS) & Role State Graph (RSG)

These are **intensional facets** of a **Role**, not containers “inside” the Role. They are **recorded in** the **RoleDescription** (or **RoleSpec** once harnessed), per E.10.D2.

* **RCS (Role Characterisation Space).** A set of named characteristics that parameterise how the Role is understood in a Context (e.g., *AgencyLevel ∈ {None, Assisted, Delegated, Autonomous}*; *SafetyCriticality ∈ {SC0…SC3}*).
* **RSG (Role State Graph).** A directed graph of **named states** (nodes) and **admissible transitions** (edges) for the Role **within the Context** (e.g., *{Eligible → Authorized → Active → Suspended → Revoked}*).

  * Each **state** has a **Conformance Checklist** (set of observable cues) supporting **Evaluations** (“X ∈ *Authorized*@context in W”).
  * RSG governs **role state transitions**, independent of any Work instance.

**Discipline.** Prefer the phrasing *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*; avoid “Role **contains** its states.”


#### A.2.1:4.4 - Shorthand & reading

The canonical compact form used in prose and diagrams is:

```
Holder#Role:Context@Window
```

Examples:

* `PLC_17#Transformer:PipelineOps@2025‑04‑01..2025‑06‑30`
* `ISO_26262v2018#NormativeStandard:AutoSafetyCase` *(status role on an Episteme; no enactment)*

*The shorthand is didactic; the semantics are those of §§4.1–4.3.*


#### A.2.1:4.5 - No role chains (use algebra, not badge‑of‑badge)

Chained assignments are ill‑formed for encoding taxonomy (see **Invariant RA‑2** and **CC‑ELIG‑3**). Chaining hides intent and defeats validation.

Taxonomic inheritance between role names is declared explicitly in the Context’s role algebra. For example, if (per A.13) your Context treats every transformer as a kind of agent, state:

* `TransformerRole ≤ AgentialRole` *(in that Context’s role algebra)*

When a MethodStep requires two independent roles, express the conjunction where it belongs:

* the **MethodStep** requires both roles; the holder **wears two badges**, not a badge‑of‑a‑badge.

#### A.2.1:4.6 - Eligibility across holon kinds (normative matrix)

A Role’s **family** constrains **who can wear its badge**. Eligibility is part of **didactic hygiene** and prevents chains like “Transformer → Agent”.

##### A.2.1:4.6.1 - Holder kinds (recap)

* **`U.System`** — any acting holon (person, device, software service, team, organization, socio‑technical unit).
* **`U.Episteme`** — any knowledge unit (document, dataset, model, standard, Standard).
* **`U.Holon`** — supertype; only **Systems** enact Work; **Epistemes** can only hold **status** roles.

##### A.2.1:4.6.2 - Role‑kind × holder matrix

| Role kind (examples)                                                     | May be held by `U.System` | May be held by `U.Episteme` | Notes (eligibility refinements live in Context)                                                                                |
| ------------------------------------------------------------------------ | :-----------------------: | :-------------------------: | ------------------------------------------------------------------------------------------------------------------------------ |
| **Agential** (e.g., *Agent*, *Decision‑Maker*, *Approver*)               |           **✓**           |              ✗              | Requires an RCS characteristic such as *AgencyLevel*; RSG should expose *Authorized/Active* states.                            |
| **Transformer/Constructor** (e.g., *Welder*, *ETL‑Runner*)               |           **✓**           |              ✗              | Performs Methods; produces Work; often requires *Capability* evidence.                                                         |
| **Observer/Measurer** (e.g., *Observer*, *Monitor*)                      |           **✓**           |              ✗              | Produces `U.Observation`; may be passive (probe) or active (test rig).                                                         |
| **Communicator/Speech** (e.g., *Authorizer*, *Notifier*)                 |           **✓**           |              ✗              | A behavioural role; produces `U.Work` typed as SpeechAct.                                                                      |
| **Service‑Governance** (e.g., *ServiceOffering*, *SLO‑ClauseCarrier*)    |             ✗             |            **✓**            | **Episteme** (catalog entry, policy). If a System “offers”, the *offer* is a SpeechAct; the *offering* is an Episteme.         |
| **Epistemic‑Status** (e.g., *Evidence*, *Definition*, *AxiomaticCore*)   |             ✗             |            **✓**            | Status roles for knowledge; never enact Work.                                                                                  |
| **Normative‑Status / Deontic** (e.g., *Requirement*, *Standard*)         |             ✗             |            **✓**            | Source of obligations; Work is checked **against** them, not enacted by them.                                                  |

**Invariant — RA‑3 (eligibility)** *(restated)*: RoleAssignments are ill‑formed if they violate this matrix. A Context may **tighten** (e.g., “Approver must be human”), never loosen.

**Conformance checks (easy to remember).**

* **CC‑ELIG‑1.** If `role.family ∈ {Agential, Transformer, Observer, Speech}`, then `holder : U.System`.
* **CC‑ELIG‑2.** If `role.family ∈ {Epistemic‑Status, Normative‑Status, Service‑Governance}`, then `holder : U.Episteme`.
* **CC‑ELIG‑3.** No “role of a role”: `role` is bound to a **holder**, not to another role or assignment.


#### A.2.1:4.7 - Role algebra within a single Context (meaning relations)

Role algebra

The in‑Context role algebra relates **role types** inside **one** `U.BoundedContext`. It is **not** mereology. Its operators (`≤`, `⊥`, `⊗`) is specified normatively in **A.2.7 `U.RoleAlgebra`**.

A.2.1 relies on it for (i) `requiredRoles` substitution checks (`≤`), (ii) separation‑of‑duties validation (`⊥`), and (iii) conjunctive bundles (`⊗`), but does not restate the operator semantics here.

#### A.2.1:4.8 - Time & state transition calculus (windows, RSG, enactability)

**Assignments authorize**, **enactments happen** — in time. RSG governs the **role’s** state transitions; `window` governs the **binding’s** validity.

##### A.2.1:4.8.1 - Windows and overlap

* **Window form:** `@t_start..t_end` (ends may be open).
* **RE‑2 (temporal fit)** *(restated)*: `work.window` lies within (or overlaps appropriately with) `assignment.window`.
* **Handover pattern:** Close `A#Role@..t` and open `B#Role@t..` — history is preserved by closing windows rather than deletion.
* **(Conformance hook.)** See **CC‑WIN‑1**: preserve history by closing windows rather than erasing RoleAssignments.

##### A.2.1:4.8.2 - RSG gating of enactment

Each Role’s **RoleDescription/RoleSpec** defines an **RSG** with named states; some states are **enactable**.

* **Delegation.** Normative author‑facing requirements for `U.RoleStateGraph` structure (including enactability marking and per‑state checklists) and the shape of `StateAssertion` evidence are defined in **A.2.5**; A.2.1 only relies on the resulting enactment gate.
* **Invariant RE‑5 (RSG gate).** A `U.RoleEnactment` is valid **iff** at enactment time the `U.RoleAssignment` can be supported by a **valid StateAssertion** that the holder is in an **enactable** state of the Role’s RSG **in this Context**.
* **(A.2.5 hook.)** The Role’s `U.RoleStateGraph` (A.2.5) identifies enactable states and attaches a Conformance Checklist to each state; checklist verdicts can be recorded as `StateAssertion`s (see SCR‑A2.5‑S02/S03).
* **Example.** *SurgeonRole* states: *Eligible → Authorized → Active → Suspended → Revoked*. Only **Active** is enactable. A pre‑op checklist produces `StateAssertion(SurgeonRole, Active)`.

**Practical reading.** *Badge valid* (window) ∧ *state is right* (RSG) ⇒ you may act.

##### A.2.1:4.8.3 - Suspensions, revocations, probation

* **Suspend:** transition to a **non‑enactable** state (e.g., *Suspended*). Keep the assignment’s window open; enactment is blocked by **RE‑5**.
* **Revoke:** either (a) close the window, or (b) transition to *Revoked* (non‑enactable).
* **Probation:** a dedicated RSG state with limited enactability (e.g., only under supervision, modelled as an extra required role on Method steps).
* **Discipline (A.2.5).** RSG transitions are explicit; no implicit “back to Active”.

##### A.2.1:4.8.4 - Typical temporal patterns (didactic)

* **Shift rotation.** `A#Role@08:00..16:00`, `B#Role@16:00..24:00` — clean handover, no `⊥` issues.
* **Shadowing.** `Trainee#Role@..` + `Mentor#SupervisorRole@..`; Method steps require **both** roles.
* **Emergency bundle.** `SoloOperator := Incision ⊗ Hemostasis ⊗ Suturing`; activate only under declared emergency (Context‑level policy).

#### A.2.1:4.9 - Integration with A.15 (Role–Method–Work alignment)

> **One line.** A `U.MethodDescription` names the roles it needs; a `U.Work` cites the concrete `U.RoleAssignment` that enacted the step; the RSG state + window gates that enactment.

##### A.2.1:4.9.1 - Design‑time Standard (inside `U.MethodDescription`)

For every **MethodStep**:

* **`requiredRoles`** — a list of `U.Role` **from the same Context as the step**.
  *Example.* In `Hospital.OR_2025`, step “Make incision” has `requires: [IncisionOperatorRole]`.
* Role algebra in‑Context applies: if the Context defines `IncisionOperatorRole ≤ SurgeonRole`, then `requires: [SurgeonRole]` also admits holders of `IncisionOperatorRole`.
* **Separation of concerns.** Capability checks (does the holder *can*?) belong to `U.Capability` and resource limits; **authorization** belongs to `U.RoleAssignment` + RSG.

##### A.2.1:4.9.2 - Run‑time check (inside `U.Work`)

A `U.Work` record provides (or allows derivation of) the fields needed to satisfy **CC‑ENACT‑1..3**:

* **`performedBy` =** a concrete **`U.RoleAssignment`** (not just a person/system name).
* **Window gate.** The Work timestamp falls inside the assignment’s `@Window`.
* **State gate.** At that timestamp, an **enactable** state for the assignment is proven by a **`StateAssertion`** (the checklist verdict for a named RSG state).
* **Role algebra gate.** The assignment’s `role` is either one of `requiredRoles` or a **specialization (`≤`)** thereof; bundles (`⊗`) expand to conjunctions; incompatibilities (`⊥`) forbid overlaps on the same holder.

##### A.2.1:4.9.3 - Evaluation & acceptance (link to services & deontics)

* **Observation.** The Work produces `U.Observation`(s).
* **Evaluation.** A `U.Evaluation` compares Observations with **AcceptanceClause**(s) referenced by a **promise content clause** (`U.PromiseContent`) or a **RequirementRole**.
* **SoD hook.** If the step or evaluation demands independence (e.g., “not performed by its reviewer”), enforce via `⊥` between `PerformerRole` and `ReviewerRole` **in the same Context**.

##### A.2.1:4.9.4 - Planning & scheduling (design‑time “who will enact”)

* **`U.WorkPlan`** (aka “WorkDescription” in prose) binds forthcoming steps to **candidate RoleAssignments** and time windows.
* **Checks before the fact.** Validate windows (no gaps/overlaps where disallowed), enforce `⊥`, ensure expected RSG state will be **enactable** at scheduled time (or flag a pre‑flight checklist).

> **Didactic cue.** Think **“Step asks for badges; Run cites a badge; Badge must be valid & green.”**
> (Badge = RoleAssignment; valid = window; green = RSG state with a fresh StateAssertion.)

#### A.2.1:4.10 - Cross‑Context bridges in practice (with CL penalties)

Cross‑Context role substitution is **Bridge‑only** and is specified in **F.9** (with CL/waiver regimes) and **B.3** (CL‑penalty routing).

A.2.1’s only rule is *no substitution by label*: any “`Role_B@B` satisfies `Role_A@A`” claim used for checking or enactment **MUST** cite an explicit Bridge (direction, CL, loss notes) and **MUST NOT** override in‑Context `≤`, `⊥`, or `⊗`.

#### A.2.1:4.11 - Everyday pattern snippets (didactic moves)

> **Use these micro‑moves to think and speak cleanly; no tooling required.**

1. **“Who can do this step?”**
   On a `MethodStep`, write `requires: [RoleX]`. In your head, expand: “Any `performedBy` whose `role ≤ RoleX`, with a **valid window** and **enactable RSG state**.”
   *Example:* `requires: [SurgeonRole]` and `IncisionOperatorRole ≤ SurgeonRole` ⇒ `Dr.Kim#IncisionOperatorRole:Hospital.OR_2025` is admissible **iff** Active.

2. **Handover without history loss.**
   Close one window, open another. Never delete.
   `Alex#IncidentCommander:SRE_Prod@08:00..12:00`
   `Riya#IncidentCommander:SRE_Prod@12:00..20:00`

3. **Independence by construction (SoD).**
   Declare `Developer ⊥ IndependentAuditor`. Then it’s **impossible** (by validation) to have overlapping windows on one holder for both roles.

4. **Supervision as bundle.**
   Model apprenticeship by requiring `Trainee ⊗ Supervisor` on sensitive steps, or by RSG state **Probation** that flips `enactable` only if `SupervisorRole` is also present.

5. **Same badge name in two Contexts.**
   `LeadEngineer:ProjectPhoenix` ≠ `LeadEngineer:DivisionR&D`. If you must relate, create a **Bridge** with CL & loss notes; never rely on the name.

6. **Documents don’t act; they frame.**
   Replace “the SOP executed X” with: `SOP_v4#RequirementRole:SafetyCase` and a `SpeechAct` “approve run” by `QA_Officer#AuthorizerRole:Plant_2025`.

7. **Window + state ⇒ permission.**
   Quick mental check: *badge valid?* (window) ∧ *state OK?* (RSG) ⇒ **go**; else **no‑go**.

8. **Communicative enactment (approval)**
`CAB_Chair#ApproverRole:ChangeControl@2026-05-01T10:05` performs a SpeechAct Work “Approve Change-4711”. Effect: moves ApproverRole’s RSG state from Authorized?→Approved and
   opens the Green‑Gate for the operational step “Deploy Change-4711” (performed by a different RoleAssignment).

