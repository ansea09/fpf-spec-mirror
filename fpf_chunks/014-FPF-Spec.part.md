> **Use this table mechanically.** “Ban” means the weak phrase is **not allowed** in Core prose/identifiers/diagrams unless the **canonical** appears alongside it (or as a registered Context alias). “Layer/Token gates” prevent I/D/S and TokenClass leaks (cf. § 8.1).

| **L‑rule**   | **Weak / ambiguous word (Ban)**                   | **Canonical FPF target(s)**                                                                                                                                                                     | **Layer gate**                                                                       | **TokenClass gate**                         | **Notes**                                                                                            |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **L‑PROC**   | *process / procedure / function step*             | `U.Method` (abstract way‑of‑doing); `U.MethodDescription` (recipe/notation‑agnostic); `U.Work` (execution); `U.WorkPlan` (schedule)                                                             | I for `Method`; D for `MethodDescription`; run artefact for `Work`; D for `WorkPlan` | Kernel/Context for types; Context for runs  | “Industrial process” as **line role** → model system + `…Role`; chemistry in `Method`/`Dynamics`.    |
| **L‑FUNC**   | *function*                                        | `U.Capability` (ability/envelope) **or** `U.PromiseContent` (promise clause / offering) **or** `U.Method` (recipe) **or** `U.Work` (what happened)                                                                       | I for Capability/PromiseContent/Method; run for Work                                        | Kernel/Context                              | Never use *function* as a type name in Core.                                                         |
| **L‑SERV**   | *service* used for team/system/API/ticket/process | Always unpack to the facet: `U.PromiseContent` (service offering / promise clause), `U.Commitment` (SLA obligation), `U.SpeechAct` (promise/offer act), `accessSpec : U.MethodDescription` (API/interface spec), **service access point** (`SystemRef`, addressable endpoint), **service delivery system** (`SystemRef`), **service delivery method** (`U.MethodDescription`), and/or `U.Work` (delivery run/case/ticket). | I for PromiseContent/Commitment/Method; D for specs; A for systems; run for Work                                        | Kernel/Context/Discriminator (per artefact) | “API = service” is forbidden; name the facet head phrase (A.6.8).                                                           |
| **L‑SLA**    | *SLA* / *service level agreement* used for target/contract/document | Unpack: (i) targets/SLOs → `U.PromiseContent.acceptanceSpec`; (ii) binding obligation/penalty → `U.Commitment`; (iii) packaged “the SLA” → Contract Bundle (A.6.C); (iv) published terms → `U.SpeechAct` + clause carrier (`U.Episteme`). | I for PromiseContent/Commitment; D for clause carriers/specs; run for Work+evidence | Kernel/Context/Discriminator | Treat “SLA” as polysemic shorthand; never store it as a single type name. |
| **L‑SCHED**  | *schedule / plan / calendar* as execution         | `U.WorkPlan` (intent/window) vs `U.Work` (actuals/telemetry)                                                                                                                                    | D vs run                                                                             | Context                                     | Never attach actuals to a plan.                                                                      |
| **L‑ACT**    | *activity / action / task* as type                | `U.Work` (execution); **steps** belong to `U.MethodDescription` (with `requiredRoles`, capability bounds)                                                                                       | run vs D                                                                             | Context                                     | Reserve verbs: *enact* (role/RSG), *execute* (Work), *actuate* (System), *approve* (SpeechAct Work). |
| **L‑AGENT**  | *agent / actor / doer* (bare)                     | say “system **bearing** `…Role`”; use `U.AgentialRole` where needed                                                                                                                             | I                                                                                    | Kernel/Context                              | Org titles (Owner/Operator/Reviewer) live as **roles in a Context**.                                 |
| **L‑OWNER**  | *owner of X* (global)                             | Ownership is a **Role** inside a `U.BoundedContext` (e.g., `OwnerRole:ITIL_2020`); SoD via `⊥`                                                                                                  | I                                                                                    | Context                                     | No global “owner” property in Kernel.                                                                |
| **L‑CAP**    | *capability* for assignment/recipe/run/promise    | `U.Capability` only = ability with envelope; assignments are `…Role`; recipes `Method/MethodDescription`; runs `Work`; promises `U.PromiseContent` (service promise clause / offering)                                                       | I vs D vs run                                                                        | Kernel/Context                              | Holder of a Capability is a `U.System`.                                                              |
| **L‑DYN**    | *process of diffusion / growth / learning*        | `U.Dynamics` (law/model of change)                                                                                                                                                              | I                                                                                    | Kernel/Context                              | Reserve for uncaused change models.                                                                  |
| **L‑EVID**   | “paper/dataset proves/ensures”                    | `…#EvidenceRole:Context` on an **Episteme**; claims/scopes/polarity/timespan; provenance from `Work`                                                                                            | D/S                                                                                  | Context/Discriminator                       | Evidence is a **role binding**, not an actor.                                                        |
| **L‑CTX**    | *context* (fuzzy trope)                           | `U.BoundedContext` (named card)                                                                                                                                                                 | —                                                                                    | Context                                     | Never use “depends on context” in Core; **name** the Context.                                        |
| **L‑BRIDGE** | cross‑context equivalence “by same label” | Explicit **Bridge Card** (F.9): state `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** for disambiguation + licence‑revealing name/verb choice). | — | — | Same label ≠ same concept; umbrella “same/equivalent/align/map/…” must be repaired into a Bridge before it can justify reuse, rows, or substitution. |

> **Red/Green pattern (example).** ✗ “The **process** ensures quality.” → ✓ “The **MethodDescription** defines steps; **Work** is **evaluated** against **RequirementRole**.”


#### E.10:9.2 - Quick, lintable substitutions (mechanical helpers)

> Editors may auto‑offer these rewrites; accept only if the transformed sentence passes **§ 7 MG-DA** and **§ 8 LEX.Morph** gates.

| **Ban**                         | **Canonical rewrite**                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| “the process owner approves”    | `SystemX#ApproverRole:Context` **performs a SpeechAct Work** “approve …”                |
| “the document enforces policy”  | `Policy_vN#RequirementRole:Context` **gates** Work; enforcement = **SpeechAct** + audit |
| “our service runs nightly jobs” | Nightly **Work** **claimsPromiseContent**(BatchProcessing); **promise content** defines acceptance     |
| “the API is the service”        | API = `accessSpec : MethodDescription`; **promise content** defines acceptance           |
| “capability assigned to team Y” | Team Y **plays** `Role`; the team (as system) **has Capability** C within envelope E    |
| “process health green”          | StateAssertion for `ObserverRole`/`Service` KPI **passes** acceptance window            |
| “function of component A fails” | **Work** performed by `SystemA#Role` **failed** acceptance (observations show …)        |
| “context is unclear here”       | **Name** the `U.BoundedContext`; else split and Bridge                                  |


#### E.10:9.3 - Acceptance tests (LEX‑AC)

A text **passes** LEX if all answers are **Green**:

1. **Context named.** Polysemous terms appear **inside a named `U.BoundedContext`** (or the page declares a local context card).
2. **Right layer.** I/D/S layer respected: types/roles on I; recipes/docs on D; actuals on runs (cf. § 8.1 gates).
3. **Promise vs ability vs performance.** `PromiseContent` (promise clause), `Capability` (ability), `Work` (performance) are not conflated.
4. **No anthropomorphism.** Documents/datasets/models do not “do”; **Systems** do.
5. **Scheduling hygiene.** No actuals on `WorkPlan`; all actuals live on `Work`.
6. **Cross‑context reuse.** Any reuse across Contexts cites a **Bridge id** with `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** when the surface prose uses “same/equivalent/align/map/…”).
7. **MG-DA ok.** New or refactored tokens pass **§ 7 MG-DA** (anchored head noun; collision check; CharacteristicSpace for enums).
8. **Morphology ok.** Suffix/prefix/casing respect **§ 8 LEX.Morph** (e.g., `…Role`, `MethodDescription`, `Work`, reserved prefixes).
9. **Banned tokens absent.** No *process/function/task/activity* in Kernel senses; no tooling/file suffixes in Kernel tokens.
10. **State gating present (when needed).** Readiness is expressed via **RSG state** + **StateAssertion**, not vague “approved/ready”.


#### E.10:9.4 - Coordination map (how LEX plugs into the rest of FPF)

* **With E.10.D1 D.CTX (Context discipline).**
  ULR–CTX‑1: Every Core meaning that can vary **names its `U.BoundedContext`**.
  ULR–CTX‑2: Same‑spelled labels are **distinct senses** across Contexts; reuse requires a **Bridge** (F.9) with CL & loss notes.

* **With E.10.D2 (I/D/S discipline).**
  Speak in the **right I/D/S layer**. ULR–IDS‑1..3 apply (types/roles = I; descriptions/specs = D/S; work/state assertions = evaluations/occurrences). Upgrades D→S only when **checkable acceptance** exists.

* **With A.2 / A.15 (Role–Method–Work alignment).**
  Role = **assignment**; Method = **way‑of‑doing**; MethodDescription = **documented recipe**; Work = **dated occurrence**. Sentences must keep this split.

* **With F‑cluster (Unification) & UTS (F.17).**
  Harvest in one Context → **SenseCell** → **Concept‑Set row** with relation (`≡/⋈/⊂/⟂`) and losses. UTS is the human‑readable roll‑up.

> **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance: `LEX.TokenClass(t)=c ⇒ USM.Scope(usage) ∈ AllowedScopes(c)` (see § 7.5).


#### E.10:9.5 - Conformance checklist (LEX‑CC)

1. **LEX‑CC‑1 (Bans).** Any banned token in Core/Arch fails unless the **canonical** appears (or the token is a registered Context alias).
2. **LEX‑CC‑2 (Context).** Each polysemous term names its **`U.BoundedContext`**.
3. **LEX‑CC‑3 (Layer/Morph).** Usage passes **§ 8** gates (suffix/prefix/casing) and I/D/S layer checks.
4. **LEX‑CC‑4 (Bridge).** Cross‑context reuse cites **Bridge id** and CL; same‑spelled labels without a Bridge are non‑conformant.
5. **LEX‑CC‑5 (MG-DA).** New tokens pass **MG-DA** tests, including **full‑text collision** and **Reserved‑Names** checks.
6. **LEX‑CC‑6 (Service & evidence).** Service acceptance computed from **Work**; evidence is an **EvidenceRole** on an **Episteme** with provenance.
7. **LEX‑CC‑7 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.


#### E.10:9.6 - Worked micro‑examples (short, cross‑domain)

**Factory.**
✗ “The **process** failed; the **service** restarted itself.”
✓ `PLC_17#ObserverRole:PipelineOps` logged **Observations**;
`CAB_Chair#ApproverRole:ChangeControl` **performed a SpeechAct** “approve restart”;
`OpsBot#DeployerRole:CD_Pipeline_v7` **executed Work** `RestartRun‑4711` which **claimsPromiseContent**(CoolingUtility);
post‑run **Evaluation** shows the **Service** acceptance **passed**.

**Cloud.**
✗ “The **process owner** approved; the **API service** deployed.”
✓ `ProductLead#AuthorizerRole:Rollout_2025` **performed a SpeechAct**;
`sCG‑Spec_ci_bot#DeployerRole:CD_Pipeline_v7` **performed Work** `Deploy‑F123`;
API = `accessSpec : MethodDescription#REST_v12`; **promise content** “Feature Access” declares acceptance; telemetry **Work** shows **fulfilPromiseContent**.

**Research.**
✗ “Dataset X **proves** the theory; the **process** is reproducible.”
✓ `DatasetX#ModelFitEvidenceRole:Theory_Context` **supports** claim C within scope S;
reproducibility via **StateAssertions** on `ReplicationEvidenceRole`;
procedures are `U.MethodDescription`; re‑runs are **Work**.


**Editorial note.**
This section **inherits** § 7 **MG-DA** (anchored head nouns; Characteristic/CharacteristicSpace for enums; collision checks) and § 8 **LEX.Morph** (suffix/prefix/casing). It deliberately **omits** their details to avoid duplication.  The only legitimate uses of *plane* in the Core are **CHR:ReferencePlane** and the derived operators **CL^plane** and **Φ_plane**; policy flags MUST NOT introduce new “planes”. To distinguish pre‑operational vs operational states *within* **ReferencePlane=world**, use **WorldRegime ∈ {prep|live}** (formerly `PlaneRegime`).

### E.10:10 - Migration playbook — turning messy language into ULR‑clean prose *(informative)*

> A pragmatic **three‑pass** routine. Works with plain text, diagrams, or models; no tools required.

#### E.10:10.1 - Pass 0 — *Pre‑flight (2 minutes per page)*

0.1 **Name the Context card** you’re writing in (title, edition, scope note).
0.2 For every new or renamed token, **declare `LEX.TokenClass`** ∈ {KernelToken, ContextToken, DiscriminatorToken}.
0.3 Run **MG-DA pre‑check** (anchored head noun; no metaphor heads; if enum → declare its **CharacteristicSpace**).
0.4 Run **collision/uniqueness**: full‑text grep + Reserved‑Names registry (see § 7). If collides → rename or DRR deprecate.

#### E.10:10.2 - Pass 1 — *Harvest in the Context*

1.1 **Underline overloaded words** (*process, service, function, workflow, ticket, approval, spec, plan,* …).
1.2 For each, write a **one‑line intent** in Plain register (what object‑of‑talk is meant).
1.3 Mark any cross‑Context reuse candidates.

#### E.10:10.3 - Pass 2 — *Map to Core anchors (mechanical)*

2.1 Replace underlined words via **§ 9 L‑rules** table:
 • recipe → **`U.Method` / `U.MethodDescription`**
 • scheduled run → **`U.Work` / `U.WorkPlan`**
 • promise → **`U.PromiseContent`**
 • ability → **`U.Capability`**
 • actor‑mask → **`…Role / RoleAssignment`**
 • document/evidence carrier → **`Episteme`** with **`EvidenceRole/RequirementRole`**
2.2 Apply **LEX.Morph** (§ 8): suffix gates (`…Role/…Work/MethodDescription/Service`), casing, reserved prefixes.
2.3 Pass **I/D/S layer** check: types/roles on I; recipes/docs on D; actuals on runs.
2.4 Attach **Context tags** on first use; set **twin labels** (Tech/Plain) in the local Glossary.

#### E.10:10.4 - Pass 3 — *Stitch & publish*

3.1 Add **safe rewrites** for any anti‑patterns you found (use § 9.2 quick table).
3.2 If sameness is needed across Contexts, create a **Bridge** (F.9) with explicit `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** when the source text uses umbrella “same/equivalent/align/map/…” language).
3.3 Publish a one‑page **UTS** (F.17) for the Context (columns: Context, Tech label, Plain label, Kernel anchor, Warnings).
3.4 Log a short **DRR** when renames/aliases occur (F.13), linking to grep results that motivated the change.


### E.10:11 - ULR conformance prompts *(normative, concept‑only questions)*

> Use these **prompts** during review. They reference § 7 (MG-DA) and § 8 (LEX.Morph) instead of repeating them.

1. **Context prompt.** Does each potentially polysemous noun live inside a **named `U.BoundedContext`**?
2. **Layer prompt.** Is each sentence in the correct **I/D/S layer** (I: type/role; D: description/spec; run: actuals)?
3. **Token prompt.** For new/renamed tokens, is **`LEX.TokenClass`** declared and consistent with where the token appears?
4. **Object‑of‑talk prompt.** Does the **head noun** name the object being classified (Role/Method/Service/Work/Context/Characteristic)?
5. **Morphology prompt.** Do suffix/prefix/casing pass **LEX.Morph** gates (e.g., `…Role`, `MethodDescription`, `Work`)?
6. **Promise vs ability vs performance.** Are **Service** (promise), **Capability** (ability), and **Work** (performance) distinct?
7. **Plan vs execution.** Are **WorkPlan** windows separated from **Work** actuals?
8. **Evidence prompt.** Do documents **hold roles** and **justify**, while **systems act**?
9. **Bridge prompt.** If sameness spans Contexts, is there an explicit **Bridge** with **CL** and loss notes?
10. **Collision prompt.** Did we run full‑text + Reserved‑Names checks (no other meaning of this token anywhere in FPF)?


### E.10:12 - ULR regression cues *(concept‑only “diff” triggers)*

Re‑review your prose when any of these happen:

* **Context edition** changes → re‑affirm twin labels, Bridges, and acceptance wording.
* **A role/type name grows** (“and/plus/‑‑”) → apply MG-DA: split or bundle (A.2).
* **A “service” statement broadens scope** → check that **acceptance** terms cover the new target; else split the Service.
* **Recipes gain/lose steps** → update **`MethodDescription`**, not `Service` or `Role` names.
* **Evidence verbs creep into actor sentences** → re‑apply L‑rules (documents don’t act).
* **New token minted** → ensure `LEX.TokenClass` declared; run collision checks; add CharacteristicSpace if enum.
* **Suffix drift** (e.g., `…Work` on a plan) → fix via **LEX.Morph**.
* **Cross‑Context reuse by label** appears → require a **Bridge** (F.9) or split senses.


### E.10:13 - Teaching deck — the ULR quick card *(reusable in any Context)*

> **Say it cleanly, once (memorise):**
> **Role** = assignment (mask) - **Method** = way‑of‑doing - **MethodDescription** = recipe (document) - **Work** = run (dated)
> **Capability** = can‑do within bounds (envelope + measures) - **Service** = promise (access + acceptance)
> **I/D/S are layers**; **documents don’t act**; **Contexts own meanings**; **Bridges** move meanings.

**Name forms (allowed morphology):**
• **Types/roles:** `<Noun><Role/Type>` (`IncidentCommanderRole`, `NormativeStandardRole`, `WorkItemType`).
• **Statuses:** `<Noun>Status` inside the Context’s role space (`ApprovedStatus`) — status‑only; not enactable.
• **No suitcase nouns:** avoid “and/plus/&” in names; use **bundles** (A.2) or separate roles.
• **Acronyms:** first expansion + register; short‑form registered per **§ 7.7**.


### E.10:14 - Three worked micro‑examples — ULR across domains *(informative)*

#### E.10:14.1 - Healthcare (OR context)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**ULR rewrite:**
“**WorkPlan** OR‑Case‑221 starts 08:00 and will execute **MethodDescription** `Incision_v4`.
`SOP_OR_v4` holds **RequirementRole**; a **SpeechAct Work** by `QA_Officer#ApproverRole` authorises the run.
The hospital offers **Service** ‘Post‑op monitoring’ (access = ward protocol; acceptance = vitals envelope).”

#### E.10:14.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**ULR rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
**Work** instances that **fulfil Service** ‘Provide seam S’ average 3 min; **acceptance** bounds are in `Seal_Acceptance.md`.
The **MethodDescription** is `Weld_MIG_v3`; the **Role** is `WelderRole`.”

#### E.10:14.3 - Cloud/SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**ULR rewrite:**
“`sCG‑Spec_ci_bot#DeployerRole:CD_v7` performed **Work** ‘Deploy r4711’ (failed at T+120 s).
The platform offers **Service** ‘Object Storage’ (access = `S3_API_Spec_vX`; **acceptance** = durability/availability targets).
`LogWriter` is a **System** bearing `TransformerRole` that wrote the records; *the service did not act*.”


### E.10:15 - Closing notes *(governance & purity)*

* **Notation‑agnostic.** ULR is a **language constitution**, not a scanner or template. Apply it in prose, sketches, or formal models.
* **Where checks live.** Convenience checks belong to Tooling; ULR itself stays notation‑agnostic. Conformance code lives in **SCR‑LEX / RSCR‑LEX** as referenced above.
* **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance:
  `LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)` (§ 7.5).
* **Guards honoured.** DevOps Lexical Firewall and Unidirectional Dependency remain intact.
* **Reserved “plane”.** Only **`CHR:ReferencePlane`** uses the bare word *plane*; I/D/S are **layers**; all other category talk is expressed as **Characteristics** in a **CharacteristicSpace**.

> **One‑line memory:** *“ULR keeps words honest so ideas stay composable.”*


### E.10:End
  
## E.10.P - Conceptual Prefixes policy & registry
 **Intent.** Provide a compact, **notation‑neutral** registry and **minting policy** for *conceptual prefixes* — short shorthands that signal **cognitive namespaces** used throughout the Core.

 **Policy (normative).**
1. **Purpose.** A conceptual prefix exists **to aid reasoning**, not to name files, serialisations, or APIs. It labels a **role in thought** (e.g., meta‑type, calculus operator, relation family).
 2. **Anchoring.** Every prefix **MUST** be anchored to a **Core extension patterns**  (CAL/LOG/CHR) or Kernel construct and documented in its *Relations*.
 3. **No tool lock‑in.** A prefix **MUST NOT** imply a particular notation or machine binding (see E.5.1–E.5.2).
 4. **Minting rule.** New prefixes are introduced by a **DRR** (E.9) that demonstrates
    (a) cross‑pattern need, 
    (b) non‑overlap with existing prefixes,
    (c) alignment with Pillars **P‑1/P‑5**.
 5. **Scope.** Prefixes are **globally reserved** within the Core; domain patterns  **MAY** mint local shorthands only inside their Contexts and **MUST NOT** collide with this registry.

 **Registered conceptual prefixes (Core).**
* `U.` — **U.Types meta‑namespace** (holons & primitives). *Anchor:* Kernel Part A.
* `Γ_` — **Calculus operator family** (by flavour: `Γ_sys`, `Γ_epist`, …). *Anchor:* Part B umbrella on Γ.
* `ut:` — **Universal relation family** (e.g., `PartOf` sub‑relations). *Anchor:* A.14 (Mereology) — informative alias vocabulary.
* `tv:` — **Trace & Validation vocabulary** (CT2R‑LOG): `tv:AliasOf`, `tv:groundedBy`. *Anchor:* B.3 (Trust & Assurance, LOG‑use). 
* `ev:` — **Evidence hooks** (bindings/roles). *Anchor:* A.10 / B.3 (Evidence Graph Referring).
* `mero:` — **Mereology trace types** (internal labels: `SumTrace` / `SetTrace` / `SliceTrace`) used **informatively** in examples. *Anchor:* B.1 (Γ‑aggregation).

**Conformance Checklist (E.10.P).**
* **CC‑LEX‑P.1** New Core text **SHALL NOT** introduce an unregistered conceptual prefix.
* **CC‑LEX‑P.2** Each occurrence of a registered prefix **SHALL** cite its anchor pattern on first use in a section.
* **CC‑LEX‑P.3** Examples that expand a prefix into a concrete URI or syntax **MUST** mark the expansion *informative* and locate it in Tooling/Pedagogy.

**Relations.** Constrains E.5.1 (Lexical Firewall) & E.5.2 (Notational Independence); Depends on E.9 (DRR).

### E.10.P:End
  
## E.10.D1 - Lexical Discipline for “Context” (D.CTX)

> **One‑sentence summary.** Make the word **Context** unambiguous: in FPF it **only** denotes the formal primitive **`U.BoundedContext`**; remove the term **anchor**; reserve **Problem Frame** for situational narrative; treat **Domain** as an **informative family label**, not a type.

**Status.** Discipline definitional pattern.
**Depends on.** C‑6 *Strict Distinction*; C‑7 *Temporal Duality*; G‑1 *Minimal Generality*; G‑2 *Contextual Specification*.
**Coordinates with.** E.10.U1 *Domain‑Family Landscape Survey*; E.10.U2 *Term Harvesting & Normalisation*; E.10.U7 *Concept‑Set Table*; E.10.U9 *Alignment/Bridge*; `RoleAssigning` patterns (e.g., E.10.U4).
**Aliases (informative).** Context Discipline; No‑Anchor Rule.


### E.10.D1:1 - Intent & Applicability

**Intent.** Eliminate ambiguity around “context” by (a) fixing **one** formal meaning—`U.BoundedContext`; (b) removing “anchor” from the vocabulary; (c) reserving **Problem Frame** for prose about situations; and (d) clarifying **Domain** as an **informative family** (workflow, provenance, services, …) that groups several `U.BoundedContext`s.

**Applicability.** Mandatory across **all FPF patterns** (Role Assignment & Enactment, Sys-CAL, KD-CAL, Kind-CAL, planned LCA-CAL). Apply at the start of any unification effort and whenever documentation introduces or refactors “context”, “domain”, “anchor”.

**Non‑goals.** No governance, workflow, or tool mandates; no storage formats; no team roles.


### E.10.D1:2 - Problem Frame

1. **Polysemy.** “Context” is used for formal scopes, narrative situations, and even runtime modes.
2. **Extra token (“anchor”).** “Anchor” pretends to be “where meaning is attached”, duplicating context semantics.
3. **Domain overreach.** “Domain context” conflates **families** (disciplinary areas) with **formal contexts**.
4. **Plane mixing.** Runtime/design stances and deontic/behavioural notions are smuggled into “context”.


### E.10.D1:3 - Forces

| Force                     | Tension to resolve                                                 |
| ------------------------- | ------------------------------------------------------------------ |
| Universality vs locality  | One calculus vs many local context of meaning (C‑6 vs C‑1).          |
| Brevity vs precision      | Short labels vs unambiguous reference.                             |
| Stability vs evolution    | Fixed terms vs edition turnover and language variants (C‑7).       |
| Parsimony vs expressivity | Few primitives vs enough hooks for Role Assignment & Enactment, Concept Sets, and Bridges. |


### E.10.D1:4 - Solution — **Name one thing “Context” can mean**

**D‑CTX‑1 (Canonical meaning).** In all FPF materials, **Context** denotes the formal primitive **`U.BoundedContext`** only. The short form **Context** is permitted in the *Tech* register strictly as an alias of `U.BoundedContext`.

**D‑CTX‑2 (Remove “anchor”).** The term **anchor** is **prohibited**. When you need “the place where a meaning lives”, use:

* **`SenseCell := (U.BoundedContext, Local‑Sense)`** — the *cell of meaning* inside a specific Context; or
* a **`ConceptSet.Row`** + column reference (see E.10.U7).

**D‑CTX‑3 (Domain is informative).** **Domain** (workflow, provenance, services, access, sensing, …) is **not** a U.Type. It is an **informative family label** grouping several `U.BoundedContext`s. There is no “domain context”.

**D‑CTX‑4 (Narrative is Problem Frame).** Use **Problem Frame** (or **Frame**) for situational narrative in patterns. Do **not** use “context” for narrative sections.

**D‑CTX‑5 (Time is a tag, not a context).** `design` / `run` are **TimeScope tags** (C‑7) on artefacts or sources; they do **not** create separate contexts.

**D‑CTX‑6 (No context inheritance).** `U.BoundedContext`s have **no is‑a** or containment relations. Any cross‑context relationship appears **only** via E.10.U9 *Alignment/Bridge* with explicit loss policies.

**D‑CTX‑7 (Language/edition discipline).** Different languages or editions may be **distinct `U.BoundedContext`s** when meaning or usage can diverge. Where an official source binds multilingual labels to the **same** semantics, record them as **labels** of the **same** Context.

**D‑CTX‑8 (Reference forms).** Use **one of the following** when pointing to meaning:

* **`ContextId:LocalLabel`** (e.g., `BPMN_2_0:process`), or
* **`SenseCell(ContextId, Local‑SenseId)`**, or
* **ConceptSet(RowId).Column(ContextId)** (E.10.U7).


### E.10.D1:5 - Structure — Minimal reference shapes (informative)

> Shapes shown **do not** prescribe formats; they are naming conventions.

* **Context Id.** Stable short handle (e.g., `BPMN_2_0`, `PROV_O_2013`, `ITIL4_2020`, `NIST_RBAC_2004`, `SOSA_SSN_2017`).
* **SenseCell.** `(ContextId, Local‑Sense)` where `Local‑Sense` is the Context‑local preferred label (from E.10.U2).
* **ConceptSet Row.** A table row keyed by a row id; columns are `SenseCell`s per Context (E.10.U7).


### E.10.D1:6 - Core Invariants (normative)

1. **LCTX‑INV‑1 (Uni‑meaning).** The word **Context** in formal text equals **`U.BoundedContext`**.
2. **LCTX‑INV‑2 (No anchor).** The token **anchor** does **not** appear in normative prose; use **SenseCell** or **ConceptSet reference**.
3. **LCTX‑INV‑3 (No domain contexts).** “Domain context” is invalid; use **Domain family** + list of `U.BoundedContext`s.
4. **LCTX‑INV‑4 (Frames, not contexts).** Pattern headers use **Problem Frame** for narrative.
5. **LCTX‑INV‑5 (No hierarchy).** Contexts are flat; relationships are declared **only** via E.10.U9 Bridges.
6. **LCTX‑INV‑6 (Plane hygiene).** Contexts describe **context of meaning** for sources; they are not roles, statuses, executions, or types (C‑6).
7. **LCTX‑INV‑7 (Time tags).** DesignRunTag is a **tag** on artefacts/sources; it does not multiply contexts.
8. **LCTX‑INV‑8 (Language/edition).** Multilingual or multi‑edition handling follows D‑CTX‑7.


### E.10.D1:7 - Conformance Checklist (normative)

* **CC‑LCTX‑1.** Grep‑style check: every “Context” in formal sections expands to **`U.BoundedContext`**.
* **CC‑LCTX‑2.** The token **anchor** is absent from normative text; where needed, occurrences are replaced by **SenseCell** or **ConceptSet reference**.
* **CC‑LCTX‑3.** Pattern headers use **Problem Frame**; none use “Context” for narrative.
* **CC‑LCTX‑4.** References to meaning are in one of the **reference forms** (Sec. 5).
* **CC‑LCTX‑5.** No file defines “domain context”; Domain appears only as an **informative family**.
* **CC‑LCTX‑6.** No is‑a edges between contexts; any cross‑context relation is located in **E.10.U9**.
* **CC‑LCTX‑7.** Language/edition handling matches **D‑CTX‑7** (separate Contexts when semantics can diverge).


### E.10.D1:8 - Anti‑patterns & Remedies

| Anti‑pattern                  | Symptom                                                           | Why harmful                          | Remedy (normative)                                                           |
| ----------------------------- | ----------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------- |
| **A1 Context-as-situation**   | “Context” used for narrative sections                             | Ambiguity                            | Use **Problem Frame**; reserve Context for `U.BoundedContext` (D‑CTX‑4).     |
| **A2 Anchor-speak**           | “role anchor”, “ontology anchor”                                   | Redundant token; hides locality      | Replace with **SenseCell** or **ConceptSet(Row).Column** (D-CTX-2, D-CTX-8). |
| **A3 Domain context**         | “Workflow domain context”, etc.                                   | Family ≠ formal context              | Use **Domain family** + explicit list of Context ids (D‑CTX‑3).              |
| **A4 Context hierarchy**      | Context A “is‑a” Context B                                        | Leaks meanings; blocks loss policies | Remove hierarchy; use **E.10.U9 Bridge** with loss policy (D‑CTX‑6).         |
| **A5 Time‑as‑context**        | “Runtime context” vs “Design context”                             | Multiplies Contexts incorrectly         | Use **TimeScope tags** (C‑7); keep one Context (D‑CTX‑5).                    |
| **A6 Cross‑lingual blending** | Mixing language labels as one context despite divergent semantics | Hidden drift                         | Split Contexts per **D‑CTX‑7** or document shared semantics if truly bound.  |


### E.10.D1:9 - Worked Examples

#### E.10.D1:9.1 Enactment — process vs activity (two context of meaning).

* Use `BPMN_2_0:process` and `PROV_O_2013:activity` as **SenseCell**s.
* In a Concept‑Set row, code the provisional relation `⋈` (overlap), not an equality.
* Role Descriptions later reference **the specific SenseCell**, not “an anchor”.

#### E.10.D1:9.2 Roles — behavioural mask vs access status.

* `BPMN_2_0:participant` vs `NIST_RBAC_2004:role`.
* Mark `⟂` (incompatible) in the Concept‑Set row to prevent conflation.
* Any cross‑use requires E.10.U9 with explicit loss policy.

#### E.10.D1:9.3 Services & evidence.

* `ITIL4_2020:service` / `ITIL4_2020:service‑level‑objective` with KD‑CAL cells `SOSA_SSN_2017:observation`.
* References in acceptance patterns point to **SenseCell**s; provenance stays within the PROV Context.


### E.10.D1:10 - Reasoning Primitives (conceptual judgements; notation‑agnostic)

> Pure **thinking moves**; no APIs, no storage, no governance.

* **(J1) Context expansion.** `⊢ Context ≡ U.BoundedContext`
  *Reading:* wherever “Context” appears in formal prose, it denotes `U.BoundedContext`.

* **(J2) Anchor ban.** `uses("anchor") ⊢ violation(D‑CTX‑2)`
  *Reading:* usage of “anchor” flags a discipline violation.

* **(J3) Sense reference.** `ref(ContextId, LocalLabel) ⊢ SenseCell(ContextId, Local‑Sense)`
  *Reading:* a well‑formed reference identifies a SenseCell.

* **(J4) Narrative frame.** `header("Context") ⊢ replaceWith("Problem Frame")`
  *Reading:* headings “Context” in patterns must become “Problem Frame”.

* **(J5) Domain family.** `label ∈ {workflow,…} ⊢ DomainFamily(label)`
  *Reading:* Domain labels are families, not contexts.

* **(J6) Time tag.** `stance ∈ {design, run} ⊢ TimeScopeTag(stance)`
  *Reading:* time is a tag, not a new context.


### E.10.D1:11 - Relations (with other patterns)

**Builds on:** C‑6, C‑7, G‑1, G‑2.
**Constrains:**

* **E.10.U1** — lists only `U.BoundedContext`s; no “domain contexts”; context records never encode pattern semantics.
* **E.10.U2** — Seeds and Occurrences are **always** Context‑anchored; references use forms from Sec. 5.
* **E.10.U7** — Columns are **SenseCell**s; row notes never call them “anchors”.
* **E.10.U9** — All cross‑context relations live here; no implicit equivalences elsewhere.
* **`RoleAssigning` patterns (E.10.U4, …)** — Context points to **SenseCell** or **Concept‑Set columns**, never to “anchors”.


### E.10.D1:12 - Migration Notes (conceptual playbook)

1. **Rename headings.** Replace any “Context” section title with **Problem Frame**.
2. **Delete “anchor”.** Replace with **SenseCell** or **Concept‑Set** references.
3. **Split domain vs context.** Where “domain context” appears, rewrite as **Domain family** + explicit list of `U.BoundedContext`s.
4. **Audit references.** Ensure every semantic reference is `ContextId:LocalLabel` or `SenseCell(ContextId, …)` or Concept‑Set column.
5. **Flatten contexts.** Remove any inheritance among contexts; move relations to **E.10.U9**.
6. **Tag time.** Replace “design/runtime context” with **TimeScope tags**.
7. **Language/edition pass.** Split or merge Contexts per **D‑CTX‑7**; document rationale.


### E.10.D1:13 - Acceptance Tests (SCR/RSCR stubs)

**SCR — Static discipline checks**

* **SCR‑DCTX‑S01.** No occurrence of the token **anchor** in normative sections.
* **SCR‑DCTX‑S02.** All formal uses of “Context” resolve to **`U.BoundedContext`**.
* **SCR‑DCTX‑S03.** Pattern headers contain **Problem Frame** instead of “Context”.
* **SCR‑DCTX‑S04.** All semantic references use the forms in Sec. 5.
* **SCR‑DCTX‑S05.** No “domain context” strings; Domain appears only as family metadata.
* **SCR‑DCTX‑S06.** No is‑a or containment relations between contexts outside **E.10.U9**.

**RSCR — Regression discipline checks**

* **RSCR‑DCTX‑E01.** Adding a new family or edition does not introduce “domain context” or context hierarchies.
* **RSCR‑DCTX‑E02.** Refactors of E.10.U1/U.2/U.7/U.9 do not re‑introduce “anchor”.
* **RSCR‑DCTX‑E03.** Multilingual updates follow D‑CTX‑7 (split/merge rationale recorded informatively).

### E.10.D1:End
  
## E.10.D2 - Intension–Description–Specification Discipline (I/D/S)

*Definitional pattern — normative, notation‑agnostic*

> **One‑sentence summary.** For every intensional FPF object (e.g., `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.PromiseContent`), clearly distinguish the **thing itself** (*Intension*), its **context‑bound Description** (KU), and its **formal Specification** (KU). Use **–Spec** only when strict, testable invariants and an acceptance harness exist; otherwise use **–Description**. This keeps semantics clean, didactic, and testable across all FPF patterns.

**Status.** Definitional pattern.
**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.10.D1 **D.CTX (Context ≡ U.BoundedContext)**; C.2.1 **U.EpistemeSlotGraph (DescriptionContext, IDS‑13)**; C.2.3 **Unified Formality Characteristic (F)**.
**Coordinates with.** F.4 **Role Description**; F.5 **Naming Discipline**; F.10 **Evaluation**; F.15 **SCR/RSCR Harness**.
**Non‑goals.** No editors, workflows, registries, or storage formats. No tooling commitments.

### E.10.D2:1 - Problem frame

**Intent.** Prevent perennial confusions such as “the role contains the checklist” or “the method is the document.” Establish a universal discipline so that:

* **Intensions** (e.g., `U.Role`, `U.Method`) remain I/D/S layer‑pure and context‑agnostic entities in the kernel.
* **Descriptions** (KUs) capture human‑readable, **Context‑local** semantics (labels, glosses, characterisations, state graphs, checklists).
* **Specifications** (KUs) exist **only** when there are verifiable invariants, an acceptance harness, **and a declared Formality F adequate for checkability (C.2.3; default F ≥ F4)**, making claims testable.

**Applicability.** Whenever an FPF text introduces or uses an intensional `U.Type` (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`, `U.RoleEnactment`) in any part (A–H).

### E.10.D2:2 - Problem

1. **Plane/layer mixing.** Intensions are routinely conflated with their documents and with runtime facts.
2. **Name drift.** “Spec” gets used for any write‑up; “status” drifts between states of a role and epistemic/deontic statuses over knowledge units.
3. **Didactic friction.** Inconsistent naming raises cognitive load and impedes reuse across FPF patterns.
4. **Unverifiable claims.** Without a clear gate to **–Spec**, normative wording appears without testability.

### E.10.D2:3 - Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Simplicity vs rigour**     | Easy‑to‑learn naming vs the need for machine‑checkable invariants.                |
| **Universality vs locality** | Kernel intensions must be universal; language and criteria are **Context‑local**. |
| **Stability vs evolution**   | Names should be stable; artefacts must mature via **ΔF** along the **F** ladder cleanly. |

### E.10.D2:4 - Solution — the I/D/S layer + a formal Spec‑gate

#### E.10.D2:4.1 The triad (applies to **any** intensional `U.T`)

**Terminology discipline (normative).** Say **I/D/S layers** when you mean the **stratified order with a Spec‑gate**; say **I/D/S triad** only to note **three‑ness without order or dependency**. **Do not call I/D/S a “plane”.** Reserve **plane** for uses explicitly defined elsewhere (e.g., **`CHR:ReferencePlane`** and status families).
**Layer semantics (clarity).** **I‑layer** = **kernel/intensional type** (non‑epistemic; **not** a episteme) . **D‑layer** and **S‑layer** = **epistemic Knowledge Units** (KUs). The **Spec‑gate** upgrades a Description to a Specification only under declared checkability and harness conditions (unchanged).

For every intensional type `U.T`:

* **Intension — `U.T`.**
  The thing itself (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *It does **not** contain documents, checklists, or carriers; it is not a runtime event or a file.*

* **Description episteme — `U.TDescription(@Context)`**
  A **Context‑local** knowledge unit that **characterises** `U.T` with labels (Tech/Plain), glosses, and, when applicable, **Role Characterisation Space (`U.RCS`)**, **Role State Graph (`U.RSG`)**, and **state conformance checklists**.
  *Readable, precise, didactic; may reference evaluation criteria but does not assert testable “shall”s by itself.*

* **Specification episteme — `U.TSpec(@Context)`**
  A **Context‑local** knowledge unit that states **testable invariants** for `U.T` and is **bound to an acceptance harness**.
  *Normative, verifiable, suitable for SCR/RSCR (F.15).*

> **Key phrasing discipline.** Intensions are **characterised by** (not “contain”) RCS/RSG/checklists, which **live in** the Description/Spec.
> **Terminology guard.** To avoid collisions with **ReferencePlane** and other semantic planes, the I/D/S triad is referred to as **I/D/S Layers** (Intension Layer - Description Layer - Specification Layer). The word **plane** is reserved for **semantic planes** (Role/Status/Measurement/Type‑structure/Method/Work, etc.) and for the **ReferencePlane** field used in describedEntity/assurance.

#### E.10.D2:4.2 The Spec‑gate (when “–Spec” is allowed)

Use the **–Spec** suffix **only if all** of the following hold:

1. **Formality F (C.2.3):** the artefact declares **F ≥ F4** (or a context-defined higher threshold) so predicates are checkable.
2. **Verifiability:** invariants are stated as checkable predicates or thresholds.
3. **Harness bound:** there is a linked **acceptance harness** (SCR/RSCR matrices per F.15).
4. **Context anchoring:** all wording is explicitly local to a named `U.BoundedContext` (E.10.D1).

If any condition is missing, the artefact **must be** a `…Description`.

#### E.10.D2:4.3 Where RCS/RSG and evaluations sit

* **`U.RCS` (Role Characterisation Space)** and **`U.RSG` (Role State Graph)** are **intensional** types that structure the space of role characteristics and permissible state transitions.
* Their **human presentation** (characteristics, dimensions, node labels, admissible transitions) lives in the **RoleDescription**, and becomes part of **RoleSpec** only when the transitions and state predicates are made **testable** and harness‑bound.
* **`U.Evaluation`** operates on **evidence** against the conformance checklist (from the Description/Spec) to produce a **state attestation** (“X is in state S @Context within window W”).
* **Epistemic/deontic statuses** (e.g., *Evidence*, *Requirement*, *Standard*) are **roles over Epistemes** (not states of the role). They are governed elsewhere (F‑R family) and must not be conflated with `U.RSG` state names.

#### E.10.D2:4.4 Plain‑language memory hook

> *Thing vs words vs rules.*
> **The thing** (`U.Role`, `U.Method`) is clean and abstract.
> **The words** (labels, glosses, RCS/RSG pictures, checklists) live in the **Description**.
> **The rules** (testable “shall”s with harness) live in the **Specification**.
> If you can’t test it, don’t call it **Spec**.

### E.10.D2:5 - Minimal vocabulary & naming discipline (this pattern only)

**Core trio (per intensional `U.T`).**

* **`U.T` — the Intension.**
  Kernel object (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *Never* a document, *never* an event, *never* a file.

* **`U.TDescription(@Context)` — the Description Episteme.**
  Context‑local characterisation of `U.T`: Tech/Plain labels, gloss, notes; for roles, may **characterise** with an `U.RCS` (characteristics/traits), an `U.RSG` (states/transitions), and **state conformance checklists** (per state). *Readable; precise; not yet a set of testable “shall”s.*

* **`U.TSpec(@Context)` — the Specification Episteme.**
  Context‑local, **testable** invariant set for `U.T`, explicitly **bound to an acceptance harness** (SCR/RSCR matrices per F.15). Use **–Spec** only through the Spec‑gate (Sec. 4.2).

**Suffix rules.**

* Use **`…Description`** by default (M‑mode or F‑mode without harness).
* Use **`…Spec`** *only* when **all** Spec‑gate conditions (Sec. 4.2) hold.
* No alternative suffixes (“Profile”, “Definition”, “Guide”) inside the Core; such epistemes live in pedagogy/tooling layers, not in the I/D/S discipline.

**Naming morphology (recap of F.5 as it applies here).**

* Two registers: **Tech** and **Plain** labels on every Description/Spec.
* Roles use **count nouns** (e.g., *Operator*); states use **state nouns** (e.g., *Approved*).
* Statuses over knowledge (e.g., Evidence/Requirement) are **not** role states; they name **roles over Epistemes** (F‑R family), not nodes in `U.RSG`.

**Context anchoring.**
Every Description/Spec is **local to** a `U.BoundedContext` (E.10.D1). Phrases in the episteme must read correctly once prefixed by the Context name (e.g., “(ITIL4) Acceptance criteria …”).

**Carriers.**
`U.Carrier` holds **encodings** of a Description/Spec; the Episteme’s identity is **not** the file. *Never* say “the role contains the checklist in the PDF”; say “the **RoleDescription** characterises the role with checklists; this **carrier** encodes them.”

**Time stance.**
Descriptions/Specs must declare DesignRunTag when inherent (e.g., RoleDescription is design‑time; state attestation via `U.Evaluation` is run‑time).

### E.10.D2:6 - Invariants (normative)

**IDS‑1 (Plane purity).**
An intensional `U.T` **MUST NOT** be conflated with its Description/Spec or with any `U.Carrier` or `U.Work`.

**IDS‑2 (Context locality).**
Every `…Description/…Spec` **MUST** name a `U.BoundedContext`. Wording inside is read **as‑local**; no global meaning is implied.

**IDS-3 (Spec-gate).**
A episteme **MUST NOT** use the **–Spec** suffix unless: *(a)* the artefact declares **`U.Formality = Fk` with k ≥ 4** per **C.2.3**, *(b)* invariants are testable predicates, *(c)* an acceptance harness is linked (F.15), *(d)* Context is explicit.

**IDS‑4 (Characterisation verbs).**
Texts **MUST** say: *“`U.Role` is **characterised by** `U.RCS`/`U.RSG` in the RoleDescription”*.
They **MUST NOT** say: *“the role **contains** the RCS/RSG”*.

**IDS‑5 (RCS/RSG scope).**
`U.RCS`/`U.RSG` are **intensional structures**. Their **presentations** (characteristics, state names, admissible transitions, checklists) live in the **RoleDescription**, and in **RoleSpec** only when transitions and state predicates are fully testable.

**IDS‑6 (Evaluation semantics).**
`U.Evaluation` **MUST** operate over evidence against conformance checklists from the Description/Spec and **MUST** produce a **state attestation** (who/what is in state *S* @Context within window *W*). Evaluation **does not** mutate the intensional object.

**IDS‑7 (Status separation).**
Epistemic/deontic statuses (Evidence/Requirement/Standard) are roles over **knowledge units**; they **MUST NOT** be used as state names in `U.RSG`.

**IDS‑8 (Register discipline).**
Every Description/Spec **SHOULD** include both **Tech** and **Plain** labels. Symbolic aliases are optional and informative.

**IDS‑9 (No stealth bridges).**
Descriptions/Specs **MUST NOT** import meanings from other Contexts by shared labels. Cross‑context relations exist only as **F.9 Bridges**.

**IDS‑10 (Window honesty).**
When an evaluation is time‑bounded, the **window** **MUST** be stated in the attestation.

**IDS‑11 (Ladder clarity).**
A Description may mature into a Spec by satisfying IDS‑3; the opposite move requires a rationale (loss of testability) and must drop the **–Spec** suffix.

**IDS‑12 (Didactic bound).**
A RoleDescription **SHOULD** fit on one screen per state graph plus one screen of notes; sprawling documents belong to pedagogy, not to the core Description.

### E.10.D2:7 - Reasoning primitives (judgement schemas, notation‑free)

> Judgements are **mental moves**—they assert what follows when premises hold. They do **not** imply queries, storage, or workflows.

1. **Description link (with DescriptionContext)**

   ```
   U.T, C, Vp ⊢ isDescriptionOf(TDesc, U.T, C, Vp)
   ```

   *Reading:* `TDesc` is the Context‑local Description of `U.T` in Context `C` under Viewpoint `Vp`. Its `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef(U.T), C, Vp⟩` (IDS‑13, C.2.1 §6.1).

2. **Spec link (Spec‑gate, viewpoint‑local)**

   ```
   isDescriptionOf(TDesc, U.T, C, Vp) ∧ U.Formality(TSpec) ≥ F4
      ∧ testableInvariants(TSpec) ∧ harnessBound(TSpec)
      ∧ sameDescriptionContext(TSpec, TDesc)
      ⊢ isSpecOf(TSpec, U.T, C, Vp)
   ```

   *Reading:* Only when F‑mode, testability, harness, and a matching `DescriptionContext` are present may we judge `TSpec` a Specification of `U.T` in `C` under Viewpoint `Vp`.

3. **Role characterisation**

  ```
   isDescriptionOf(RoleDesc, U.Role, C, Vp)
   ∧ characterises(RoleDesc, U.RCS) ∧ characterises(RoleDesc, U.RSG)
   ⊢ characterisedBy(U.Role, {U.RCS, U.RSG}) @C
  ```

   *Reading:* The role is *characterised by* the RCS/RSG as presented in the Description (which is pinned to `(C, Vp)`), not that it “contains” them.

4. **State conformance predicate**

   ```
   checklistFor(RoleDesc, state S) = χ
   ∧ evidence E within window W
   ⊢ conformsToState(E, χ, W) ⇒ attestation(subject ∈ S @C, W)
   ```

   *Reading:* Evidence satisfies the checklist for state `S`, yielding a state attestation.

5. **Transition admissibility**

   ```
   U.RSG allows (S → S') @C
   ∧ attestation(subject ∈ S @C, W)
   ∧ conformsToState(E', checklistFor(S'), W')
   ⊢ admissibleTransition(subject : S → S' @C)
   ```

   *Reading:* A move from `S` to `S'` is admissible when RSG permits it and `S'` is satisfied.

6. **Status / state separation guard**

   ```
   statusOverKU(KU, σ) ∧ stateInRSG(ρ)
   ⊢ σ ≠ ρ  (distinct planes)
   ```

   *Reading:* A status over a knowledge unit is not a role‑state.

7. **No Cross‑context import**

   ```
   isDescriptionOf(TDescA, U.T, CA, VpA) ∧ isDescriptionOf(TDescB, U.T, CB, VpB) ∧ CA≠CB
   ⊢ ¬equateByLabel(TDescA, TDescB)  (bridges required in F.9)
   ```

   *Reading:* Identical wording across Contexts (and Viewpoints) does not grant equivalence; only Bridges may relate them.

### E.10.D2:8 - Anti‑patterns & remedies

| ID   | Anti‑pattern                | Symptom                                                              | Why it harms thinking                     | Remedy (concept move)                                                                          |
| ---- | --------------------------- | -------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| A‑1  | **Spec‑by‑name**            | Every write‑up is titled “Spec”.                                     | Inflates normativity; untestable claims.  | Apply **Spec‑gate** (IDS‑3). If any condition fails, rename to `…Description`.                 |
| A‑2  | **Role contains RSG**       | “The role contains a state graph.”                                   | Plane mixing; mereological confusion.     | Use **characterised by** phrasing (IDS‑4); RSG presentation lives in RoleDescription/RoleSpec. |
| A‑3  | **Status ≡ state**          | *Approved* (status over episteme)  appears as a node in the role graph.     | Cross‑plane conflation; logic errors.     | Keep **statuses** (over Epistemes) separate from **role states** (IDS‑7).                            |
| A‑4  | **Stealth bridge**          | Copying state names across Contexts to imply sameness.                  | Hidden cross‑context import.              | Declare an **F.9 Bridge** or accept divergence (IDS‑9).                                        |
| A‑5  | **Checklist = process**     | Treating conformance checklist as an execution workflow.             | Category error (design vs run).           | Checklists are **criteria** used by `U.Evaluation`; executions live under `U.Work`.            |
| A‑6  | **Carrier identity**        | File path/version treated as “the spec itself.”                      | Identity drift; archival brittleness.     | Identity is the **KU**; `U.Carrier` is only an encoding (Sec. 5).                              |
| A‑7  | **Windowless verdict**      | Attestations omit time window.                                       | Unreproducible results; stale judgements. | Require **window** in attestation (IDS‑10).                                                    |
| A‑8  | **Over‑formal Description** | Description bloats into a standard; unreadable.                      | Violates didactics; blocks adoption.      | Enforce **one‑screen** discipline (IDS‑12); move exegesis to pedagogy.                         |
| A‑9  | **Spec without harness**    | “Shall” statements with no linked acceptance matrices.               | Unverifiable normativity.                 | Bind to **SCR/RSCR harness** (F.15) or downgrade to Description (IDS‑3).                       |
| A‑10 | **Global language leakage** | Description reads as universal definition rather than Context‑local. | Breaks locality; fuels conflicts.         | Prefix mentally with the Context; rewrite locally (IDS‑2).                                        |

### E.10.D2:9 - Worked examples (didactic)

> Each vignette shows **intension ↔ Description/Spec ↔ Evaluation** with **context‑local** wording. No workflows; only thinking moves.

#### E.10.D2:9.1 - Enactment (Role Assignment & Enactment line) — *Change Authority* role (ITIL 4 Context)

**Contexts.** `ITIL4_2020` (services/deontics), `PROV_O_2013` (run‑time traces).
**Intension.** `U.Role :: ChangeAuthority` — a behavioural mask that may be worn by a system (person/team/tool) to **authorise** a change.

**RoleDescription\@ITIL4.**

* **Tech/Plain.** *ChangeAuthority* / “change approver”.
* **RCS (characteristics).** CredentialLevel ∈ {L1,L2}; Scope ∈ {Service, Platform}; SeparationOfDuty ∈ {Clean, Violates}.
* **RSG (states).** `Proposed → Designated → Authorized → Active → Suspended → Revoked`.
* **State checklists (sketch).**

  * *Authorized:* { valid nomination, SoD=Clean, credential ≥ required, mandate window set }.
  * *Active:* *Authorized* ∧ { current shift/roster entry ∧ no conflicting active duty }.

**Evaluations.**
`U.Evaluation@ITIL4` over evidence (roster entries, mandate doc, SoD list, PROV Activities of approvals) yields **attestations**:

* `subject=Team‑X ∈ Authorized@ITIL4 in ⟨2025‑08‑01, 2025‑12‑31⟩`.
* Later, `subject=Team‑X ∈ Active@ITIL4 at 2025‑09‑14T10:05Z`.

**Didactic hooks.**

* The **role** is *characterised by* RCS/RSG in the **RoleDescription**; it **does not contain** them.
* The **attestation** is a statement about state‑in‑window; it does **not** mutate the role.

#### E.10.D2:9.2 - Method (Essence‑language Context) — *Backlog Refinement* method

**Contexts.** `OMG_Essence_Language_2023` (method language), `PROV_O_2013` (runtime).
**Intension.** `U.Method :: BacklogRefinement`.

**MethodDescription\@Essence.**

* **Tech/Plain.** *BacklogRefinement* / “tidy backlog”.
* **Inputs/Outputs (informative).** Work items (ideas) → clarified items (ready/not‑ready tags).
* **RCS (characteristics).** Cadence ∈ {weekly, continuous}; CollaborationMode ∈ {sync, async}.
* **RSG (states).** `Sketched → Defined → Adopted`.
* **State checklist (Adopted).** { team agreed practice note exists, cadence set, entry/exit criteria published }.

**Spec‑gate outcome.**
No acceptance harness yet → remains **MethodDescription**, **not** MethodSpec.

**Run‑time echo.**
`U.Work` instances (calendar sessions, chat threads) are traced in PROV; **Evaluation** can check whether an *Adopted* practice is being followed in window W without ever reifying the method as a workflow.

#### E.10.D2:9.3 - Service (SLO/SLA) — *Calibration Service* (ITIL 4 + SOSA/SSN Contexts)

**Contexts.** `ITIL4_2020` (service), `SOSA_SSN_2017` (observation), `ISO_80000_1_2022` (units).
**Intension.** `U.PromiseContent :: CalibrationService`.

**ServiceDescription\@ITIL4.**

* **Tech/Plain.** *CalibrationService* / “we calibrate your sensor”.
* **Acceptance facet (informative).** *SLO: error ≤ 0.5% FS under ISO 80000 units*; **formal criteria live in** ServiceSpec only if harness exists.

**Evaluation\@ITIL4+SOSA.**
Observations (SOSA) from test runs compared with thresholds → **ServiceEvaluation** attests *Met/Not‑Met* in a stated window.
No Cross‑context import: ISO units cited **as context‑local** references.

#### E.10.D2:9.4 - Epistemic (KD‑line) — *Evidence status vs role state*

**Contexts.** `PROV_O_2013` (provenance), `FPF_Evidence_Status` (status family).
**Intensions.** `U.KnowledgeUnit :: Report_42`; `U.EvidenceStatus :: SupportsClaim`.

**Separation.**

* `SupportsClaim@C` is a **status over a Episteme** (classifies the report).
* It is **not** a node of any role’s `U.RSG`.
* `U.Evaluation` produces `attestation(Report_42 has EvidenceStatus=SupportsClaim@C, W)`.

**Didactic point.**
State names in *role* graphs do not duplicate **statuses**; planes stay disjoint.

#### E.10.D2:9.5 - Control (Sys‑CAL line) — *Control‑Operator* role (IEC 61131‑3 Context)

**Contexts.** `IEC_61131_3` (control languages), `ISA_95` (integration).
**Intension.** `U.Role :: ControlOperator`.

**RoleDescription\@IEC61131‑3.**

* **RCS.** StationLevel ∈ {Cell, Line}; TaskMode ∈ {Cyclic, Event}; AlarmPrivileges ∈ {Ack, Ack+Shelve}.
* **RSG.** `Onboarded → Authorized → ConsoleActive → Paused → Suspended`.
* **Checklists (ConsoleActive).** { Authorized ∧ current console login ∧ task watchlist loaded }.

**Attestation (run‑time).**
`subject=Operator‑A ∈ ConsoleActive@IEC at 2025‑09‑14T08:00Z` based on log evidence.
No “workflow” required in the Description.

### E.10.D2:10 - Relations (with other patterns)

**Builds on:**

* **E.10.D1 — Lexical Discipline for “Context” (D.CTX).** Provides the *Context* primitive and bans “anchor” talk.
* **A.7 — Strict Distinction (Clarity Lattice).** This pattern concretises SD for intension vs description/spec vs carrier vs work.
* **C.2.3 — Unified Formality Characteristic (F).** Supplies the **F** anchors and **ΔF** moves that gate `…Spec`.

**Constrains:**

* **F.1–F.3 (Contexts → seeds → local senses).** Descriptions **must** cite context‑local senses (SenseCells) rather than global words.
* **F.4–F.5 (role/service naming).** Tech/Plain labels on Descriptions obey F.5 morphology rules.
* **F.8 (Service Acceptance Binding).** Evaluations of services read acceptance **from Description/Spec**, compare against Observations.
* **F.9 (Alignment & Bridge).** No Description/Spec may imply Cross‑context equivalence; Bridges carry all Cross‑context semantics.
* **F.15 (SCR/RSCR Harness).** Any `…Spec` must link to its harness; RSCR re‑checks verdict stability across editions/windows.

**Is used by.**

* **Part C Extention Patterns.** Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL cite `…Description/…Spec` epistemes explicitly and consume **state attestations** from `U.Evaluation`.
* **Part B trust calculus.** Uses the presence/absence of harnessed Specs and the windowed nature of attestations in confidence roll‑ups.

### E.10.D2:11 - Migration notes (conceptual refactor playbook)

> Goal: remove conflations and normalise names without changing underlying models.

1. **Rename by default.** Any `XSpec` lacking a bound acceptance harness becomes **`XDescription`**. Keep content intact; change suffix and preface with a “Description, not Spec” note.
2. **Promote selectively.** For epistemes that *are* testable and declare **F ≥ F4**, add harness links (F.15) and re-label as **`XSpec`** via the Spec-gate.
3. **Fix the verbs.** Rewrite “Role contains RSG/RCS” → “Role is **characterised by** RSG/RCS in RoleDescription”.
4. **Detach carriers.** Replace identity‑by‑file with **`U.Carrier` encodes …Description/Spec** wording.
5. **Add Contexts.** Where a Description drifts globally (“the backlog refinement is…”), prefix with the Context and adjust wording to be **local**.
6. **Split planes.** Move any Evidence/Requirement **statuses** out of role state lists; keep them as roles over **knowledge units**.
7. **Window‑ise verdicts.** Ensure every evaluation statement adds an explicit **window** (instant or interval).
8. **Document maturity.** **Declare each Description’s F** (C.2.3) and track **ΔF** promotions/demotions as part of change notes (no governance implied).

### E.10.D2:12 - Acceptance tests (SCR/RSCR — concept‑level)

#### E.10.D2:12.1 Static conformance checks (SCR)

* **SCR-D2-S01 (Suffix discipline).** Every episteme with suffix **–Spec** passes the **Spec-gate** (**F ≥ F4** ∧ testable invariants ∧ harness link ∧ Context named). Otherwise it bears **–Description**.
* **SCR‑D2‑S02 (Characterisation verbs).** Texts never say an intension “contains” RCS/RSG; they say it is **characterised by** them via the Description/Spec.
* **SCR‑D2‑S03 (Plane purity).** No episteme mixes role **states** and knowledge **statuses**; each appears only on its correct plane.
* **SCR‑D2‑S04 (context‑locality).** Every Description/Spec names its `U.BoundedContext`; wording reads correctly when prefixed by the Context.
* **SCR‑D2‑S05 (Two registers).** Tech **and** Plain labels present on all Descriptions/Specs.
* **SCR‑D2‑S06 (Carrier separation).** Identity statements refer to Epistemes; files are referenced only as `U.Carrier` encodings.
* **SCR‑D2‑S07 (Windowed evaluation).** All state attestations cite a window `W` (instant or interval).

#### E.10.D2:12.2 Regression checks (RSCR)

* **RSCR‑D2‑E01 (Spec demotion guard).** If a **–Spec** loses its harness or testability, it is demoted to **–Description**; diffs show no lingering “shall” claims.
* **RSCR‑D2‑E02 (Bridge drift).** If two Contexts begin to share identical labels, verify no Descriptions/Specs imply Cross‑context identity; add or revise **F.9 Bridges** instead.
* **RSCR‑D2‑E03 (Edition churn).** When a Context’s canon updates, previously valid attestations remain historical (windowed); new Specs/Descriptions cite the new edition.
* **RSCR‑D2‑E04 (Verb hygiene).** Automated grep over corpus finds “contains RSG/RCS” phrasing; none remain after refactor.
* **RSCR‑D2‑E05 (Status bleed).** Spot‑audit a random sample of role graphs to ensure no epistemic/deontic statuses appear as role states.

*Didactic takeaway.*
Think in three layers: **Intension** (what the thing *is*), **Description/Spec** (how we *state* its character and, when mature, *test* it), and **Evaluation** (what we can *attest* about it in a **window**). Keep Contexts local, planes separate, and “contains” out of your vocabulary.

### E.10.D2:13 - Author’s pocket guide (carry‑in‑mind rules)

> **Use these as thinking cues, not as paperwork.** Each cue is a one‑breath test you can apply while writing.

1. **Name the Context.** Write “*Role (ITIL4)*”, “*Method (Essence‑language)*”, “*Execution (PROV)*”. Never speak global words.
2. **Pick the *object-of-talk*.** Am I talking about an **intension** (Role/Method/Service), a **Description/Spec**, an **Evaluation**, or a **Carrier**? Stay on one object-of-talk per sentence.
3. **Prefer –Description.** Use **`…Description`** by default. Switch to **`…Spec`** only after the **Spec‑gate** (testable invariants + harness + F‑mode).
4. **Characterised by…** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, never *“Role **contains** its states”*.
5. **Window every verdict.** An Evaluation must read “*X ∈ State\@context **in** W*”. No naked, timeless verdicts.
6. **Status ≠ state.** Role **states** live in `U.RSG`; Evidence/Requirement **statuses** classify **knowledge units**. Do not mix.
7. **Bridge later.** If two Contexts “feel the same”, write the itch down and leave it for **F.9 Bridge**.
8. **Two registers.** Every Description/Spec has **Tech** and **Plain** labels; prefer the shortest tech term that matches the invariants.
9. **Carrier humility.** Files and records are **Carriers** of Descriptions/Specs; they don’t *equal* the thing you reason about.
10. **Spec = test.** If you can’t point to a harness that would falsify it, it isn’t a **Spec** yet.

### E.10.D2:14 - Phrasebook & pitfall table (say this, not that)

| Mistaken phrasing (avoid)              | Didactically correct phrasing (use)                                                                                  | Why                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| “The Role **contains** its states.”    | “The **Role** is **characterised by** RCS/RSG **recorded in** the RoleDescription.”                                  | Roles are intensions; state graphs live in their **Descriptions/Specs** (knowledge plane). |
| “MethodSpec (draft).”                  | “**MethodDescription** (Essence‑language Context); not a Spec yet.”                                                     | **–Spec** is reserved for testable artifacts that passed the Spec‑gate.                    |
| “We proved the service meets the SLO.” | “**Evaluation** attests *Service ∈ Met\@ITIL4 in W* based on observations and the **Acceptance harness**.”           | Evaluations produce **windowed attestations**, not timeless facts.                         |
| “Evidence status is a role state.”     | “**Evidence status** classifies a **KnowledgeUnit**; **Role states** live in RSG. Different planes.”                 | Prevents status/state conflation.                                                          |
| “The PDF is the Method.”               | “The PDF is a **Carrier** that **encodes** a **MethodDescription**.”                                                 | Carrier ≠ content.                                                                         |
| “BPMN workflow = PROV activity.”        | “Add a **Bridge (F.9)** if needed; in F.1/F.2/F.3 we treat them as **context‑local** senses.”                           | No Cross‑context identity outside Bridges.                                                    |
| “WorkSpec / WorkPlan (synonyms).”      | “**U.WorkPlan** (preferred). **WorkDescription** is an allowed alias; **WorkSpec** is deprecated.”                   | Aligns with the –Description/–Spec discipline.                                             |
| “RoleSpec is our template.”            | “**RoleDescription** is our template; promote to **RoleSpec** once the harness exists.”                              | Keeps the Spec word meaningful.                                                            |
| “Spec says the same in all Contexts.”     | “Each **Spec/Description** is **context‑local**; Cross‑context reuse requires an **Alignment Bridge** with CL/loss notes.” | Locality guard.                                                                            |

### E.10.D2:15 - Naming & alias policy (normative, notation‑free)

#### E.10.D2:15.1 - Suffix discipline (recap).**

* **Preferred default:** **`…Description`** for Role/Method/Service/Work.
* **Reserved:** **`…Spec`** only if the item passed the **Spec‑gate** (F‑mode, testable invariants, harness id, Context named).
* **Banned:** Using **–Spec** as a synonym for “detailed description”.

#### E.10.D2:15.2 - Canonical/alias map (current edition).**

| Concept (intension) | Preferred episteme name      | Allowed alias (equal scope)   | Deprecated alias | Notes                                                                                 |
| ------------------- | ---------------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------- |
| Role                | **RoleDescription**    | RoleCard *(Pedagogy only)*    | —                | *RoleCard* is informal (teaching layer), not a normative episteme name.                     |
| Role (F‑mode)       | **RoleSpec**           | —                             | —                | Only after Spec‑gate.                                                                 |
| Method              | **MethodDescription**  | —                             | **MethodSpec**   | Global rename complete; legacy references should be updated.                          |
| Method (F‑mode)     | **MethodSpec**         | —                             | —                | Now reserved for harnessed, testable methods.                                         |
| Work (schedule)     | **U.WorkPlan**         | **WorkDescription**           | **WorkSpec**     | *WorkSpec* alias removed; *WorkDescription* remains as didactic alias for *WorkPlan*. |
| Service             | **ServiceDescription** | ServiceCard *(Pedagogy only)* | —                | As above: Card is informal only.                                                      |
| Service (F‑mode)    | **ServiceSpec**        | —                             | —                | Requires acceptance harness id (F.15).                                                |

#### E.10.D2:15.3 - Verb & morphology rules.**

* **Verbs.** Use *characterised by*, *recorded in*, *encoded by*; avoid *contains*, *is stored in*, *is implemented by* when speaking at the conceptual level.
* **Morphology.**

  * Roles name **masks** as **count nouns** (*Operator, ChangeAuthority*).
  * States as **state nouns/participles** (*Authorized, Active*).
  * Status names are **classifiers over knowledge** (*SupportsClaim, NormativeStandard*).
  * Descriptions/Specs use neutral nouns (*RoleDescription, MethodSpec*).

#### E.10.D2:15.4 - Deprecations (effective now).**

* **MethodSpec** (as a general name) → **MethodDescription** unless Spec‑gate is met.
* **WorkSpec** (alias for WorkPlan) → **WorkDescription** (allowed alias), or **U.WorkPlan** (preferred).
* Texts must avoid “contains RSG/RCS” phrasing (see RSCR‑D2‑E04).

### E.10.D2:16 - Quick templates (fill‑in‑mind, not forms)

> Copy these **lines** into your prose as thinking scaffolds. They are not schemas, fields, or checklists to fill; they are didactic prompts.

#### E.10.D2:16.1 - Role (default).

* *Intension.* `U.Role :: <TechName> in <ContextId>`.
* *RoleDescription\@context.* Tech/Plain: **`<TechName> / <PlainName>`**.

* **RCS characteristics.** `<characteristic₁ ∈ {… }>; <characteristic₂ ∈ {… }>`.
* **RSG nodes (→).** `<S₀ → S₁ → …  → Sₙ>`.
* **State checklist (one node).** `<StateX : {criterion₁, …}>`.
* *Evaluation attestation.* `subject=<Holder> ∈ <StateX>@<ContextId> in <Window> (evidence: <cue₁,…>)`. 

#### E.10.D2:16.2 - Method (Essence‑language Context).

* *Intension.* `U.Method :: <TechName>`.
* *MethodDescription\@context.* Inputs/Outputs (informative), **RCS/RSG** (if you track adoption).
* *Spec upgrade (optional).* “Becomes **MethodSpec** when harness `<id>` exists.”

#### E.10.D2:16.3 - Service (acceptance‑bearing).**

* *ServiceDescription\@context.* Tech/Plain; **Acceptance facet** (informative until harnessed).
* *Evaluation.* `Service ∈ Met/Not‑Met@context in <Window>` based on observations and acceptance criteria.

#### E.10.D2:16.4 - Alignment reminder.

* “No Cross‑context identity is implied; if needed, add **F.9 Bridge**: `<ContextA:TermA> ↔ <ContextB:TermB>` with CL/loss notes.”

### E.10.D2:17 - Didactic distillation (90‑second script)

> **“Three layers; one context; no leakage.”**

1. **Pick the Context.** Every word lives **inside** a `U.BoundedContext`.
2. **Pick the I/D/S layer.** Speak about the **Intension (I)**, or about its **Description/Spec (D/S)**—but never mix layers. If your sentence also asserts describedEntity or evidence, **name the `ReferencePlane`** (`world|concept|episteme`).
3. **Describe, then test.** Start with **Role/Method/ServiceDescription**. Only when you can **falsify** it with a harness do you call it a **Spec**.
4. **State is attested.** Role **states** are attested by **Evaluations** as *“X ∈ State\@context **in** W”*. Evidence/Requirement **statuses** classify **knowledge**, not roles.
5. **Carriers carry.** PDFs and repos are **Carriers** of the Description/Spec; they aren’t the thing itself.
6. **Bridges are explicit.** Cross‑context sameness is never assumed; you declare a **Bridge** with CL/loss.
   Follow these six lines and SD (*Strict Distinction*) stops being an abstraction—you feel it in every sentence you write.

### E.10.D2:End

## E.12 - Didactic Primacy & Cognitive Ergonomics

### E.12:1 - **Problem Frame**

The FPF is designed as an "Operating System for Thought," a tool intended to augment and clarify human (and artificial) reasoning. This mission places a unique demand on its architecture: the framework's internal elegance and formal power are secondary to its primary function of being understandable and usable. A perfectly consistent but incomprehensible system fails in its didactic purpose. As formal mechanisms like `Assurance Levels` and epistemic scores are introduced, there is a significant risk that the pursuit of these metrics becomes an end in itself, overshadowing the ultimate goal of fostering clearer thought.

### E.12:2 - **Problem**

If the framework's design prioritizes theoretical purity or formal completeness over cognitive ergonomics, it becomes vulnerable to two critical failure modes:

1.  **Goodhart's Law:** When a measure (like `AssuranceLevel:L2`) becomes the primary target, it ceases to be a good measure of genuine understanding. Teams may start "gaming the metrics," producing artifacts that are formally perfect but conceptually shallow or pragmatically useless.
2.  **Cognitive Overload & Rejection:** The framework becomes so dense, jargon-laden, and procedurally complex that its users—the very agents it is meant to serve—either burn out or abandon it in favor of simpler, albeit less rigorous, methods. The "Operating System for Thought" devolves into a bureaucratic machine for certification.

### E.12:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Formal Rigor vs. Human Usability** | How to build a system that is both formally sound and cognitively accessible, without sacrificing one for the other. |
| **Intrinsic Complexity vs. Incidental Complexity**| How to distinguish the necessary cognitive load inherent in solving a difficult problem from the unnecessary friction imposed by a poorly designed framework. |
| **Means vs. Ends** | How to ensure that the production of high-quality artifacts (the means) always serves the ultimate goal of enhancing an agent's cognitive capabilities (the end). |

### E.12:4 - **Solution**

FPF elevates **Didactic Primacy (Pillar P-2)** to a normative architectural principle, operationalized through two conceptual mechanisms designed to act as a permanent counterbalance to excessive formalism.

#### E.12:4.1 - The Principle of Didactic Primacy (Expanded Definition)

The primary purpose of the FPF is to enhance the cognitive capabilities (`U.Capability`/`Mastery`) of an Agent (`U.Agent`) in service of its Objectives (`U.Objective`). The creation of artifacts with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in the agent's ability to reason effectively.

#### E.12:4.2 - Mechanism 1: The Rationale Mandate

Every key assurance artifact (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is not a technical description but a narrative explanation.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate forces a moment of reflection, formally linking the act of formalization back to its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally verified artifact (`AssuranceLevel:L2`), the `rationale` is where they answer your fundamental question: "This is impressive, but *so what*? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer isn't clear and compelling in the `rationale`, the formal work may have been a waste of resources. It keeps your most brilliant minds focused on creating value, not just elegant proofs.

#### E.12:4.3 - Mechanism 2: The Human-Factor Loop (HF-Loop)**

To provide a continuous, self-correcting mechanism against cognitive overload, FPF introduces a conceptual feedback loop.

*   **Core Concept:** The HF-Loop is a formal method of inquiry designed to distinguish between the *essential complexity* of the problem being solved and the *incidental complexity* introduced by the FPF itself.
*   **Trigger Concept:** A review is triggered when the **subjective cognitive workload** associated with using the framework exceeds a conceptual threshold. This is not about performance metrics, but about the perceived mental effort required to use FPF's concepts and structures.
*   **Review Concept:** When triggered, a formal review is conducted by individuals in roles that specialize in human-centric perspectives, such as the **`Ethicist`** and **`UX Design Critic`**.
*   **Output Concept:** The review produces a set of proposed **conceptual simplifications** or **didactic improvements** to the framework's patterns. These are then submitted as formal change proposals (DRRs).

#### E.12:5 - **Conformance Checklist**

*   **CC-E12.1 (Rationale Mandate):** Every `U.AssuranceCase` or `Proof` artifact at `AssuranceLevel:L2` **MUST** contain a non-empty `rationale` component that satisfies the "So What?" test.
*   **CC-E12.2 (HF-Loop Trigger Condition):** Each pattern that defines a significant workflow **SHOULD** specify a conceptual condition for triggering an HF-Loop review, based on the principle of managing cognitive load.
*   **CC-E12.3 (HF-Loop Review Mandate):** If a trigger condition is met, a review involving the designated human-centric roles **MUST** be initiated. Its outcome **MUST** be a documented set of conceptual refinement proposals.
*   **CC-E12.4 (Didactic Primacy in DRRs):** Any DRR proposing a change to a normative pattern **MUST** include a section analyzing its impact on cognitive ergonomics and didactic clarity.

#### E.12:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ivory Tower" Framework** | The FPF specification becomes a beautiful but impenetrable fortress of abstract logic that no practicing engineer can actually use. | The **HF-Loop** provides a formal channel for user feedback to drive conceptual simplification. The roles of `UX Design Critic` and `Ethicist` are constitutionally empowered to challenge complexity that does not serve a clear purpose. |
| **The "Meaningless Rationale"** | The `rationale` field is filled with boilerplate text like "To increase assurance," without any real connection to the problem. | The "So What?" test is part of the review process for L2 artifacts. A perfunctory `rationale` is grounds for rejecting the artifact's promotion to L2, forcing the author to articulate the *real* value of their formal work. |
| **Glorifying Complexity** | A culture emerges where the most complex and difficult-to-understand models are considered the "best," regardless of their utility. | The core principle of **Cognitive Elegance (P-1)** and the mechanisms in this pattern create a constant pressure towards simplicity and clarity. The framework formally values understanding over mere complexity. |

#### E.12:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Guards FPF's Core Mission:** This pattern acts as an "immune system," protecting the framework from devolving into sterile formalism and ensuring it remains a tool for enhancing thought. | **Introduces "Softer" Concepts:** Cognitive load and rationale quality are less quantifiable than formal proofs. *Mitigation:* FPF operationalizes them through a formal method. The HF-Loop is a structured inquiry, not an informal chat. |
| **Empowers Human-Centric Roles:** It gives the `Ethicist` and `UX Design Critic` roles a concrete, constitutional function in the evolution of the framework. | - |
| **Prevents User Burnout and Rejection:** The HF-Loop is an early warning system that detects when the framework is becoming too cumbersome, allowing for course correction before users become frustrated and abandon it. | - |
| **Creates a Self-Simplifying System:** The pattern creates a formal pressure that forces FPF to evolve towards greater clarity and usability, balancing the drive for formal rigor. | - |

#### E.12:8 - **Rationale**

This pattern operationalizes **Didactic Primacy (P-2)**, transforming it from a philosophical statement into an enforceable architectural Standard. The `Rationale Mandate` ensures that every act of formalization is tied to a clear purpose. The `Human-Factor Loop` ensures that the *cost* of using the framework is measured not just in resources, but in the most critical resource of all: the cognitive capacity of its users.

This pattern does not weaken the formal rigor established by other ADRs; it complements it. It guarantees that the powerful machinery of FPF is always directed towards a meaningful, human-relevant goal. It is the constitutional guarantee that FPF will remain, first and foremost, an "Operating System for Thought."

#### E.12:9 - **Relations**

*   **Implements:** Pillar `P-2 Didactic Primacy`.
*   **Complements:** `E.13 Pragmatic Utility & Value Alignment` (which focuses on the relevance of the *problem*, while this pattern focuses on the usability of the *framework*).
*   **Is constrained by:** The overall governance process (DRRs), which is the vehicle for implementing the conceptual simplifications proposed by the HF-Loop.

### E.12:End

## E.13 - Pragmatic Utility & Value Alignment

### E.13:1 - **Problem Frame**

The FPF provides a powerful engine for constructing formally correct and highly reliable holons. This power, however, introduces a subtle but profound risk: a team can create a perfectly verified and validated artifact (`AssuranceLevel:L2`) that solves an irrelevant, misunderstood, or non-existent problem. The framework guarantees that the solution is *correct*, but it does not, by itself, guarantee that the solution is *useful*.

Furthermore, many of the most important system objectives—such as "safety," "usability," or "security"—are not directly measurable. They are assessed via **proxy characteristics** (e.g., "number of reported vulnerabilities" as a proxy for security). This practice is vulnerable to Goodhart's Law: when a proxy becomes the primary target, it often ceases to be a good measure of the original goal, as teams begin to optimize the proxy at the expense of the real objective.

### E.13:2 - **Problem**

Without a formal mechanism to keep the entire assurance apparatus tethered to real-world value, FPF risks enabling two critical failure modes:

1.  **Formalism for Formality's Sake:** Teams become preoccupied with achieving high epistemic scores, producing elegant but useless artifacts. The framework is used to build beautiful solutions to the wrong problems.
2.  **Proxy-Metric Distortion (Goodhart's Law):** Teams successfully optimize for a chosen proxy characteristic, but in doing so, they diverge from—or even actively undermine—the true, often qualitative, `U.Objective` that the proxy was intended to represent. The system becomes technically successful but pragmatically a failure.

### E.13:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Measurability vs. Meaning** | How to use quantitative, measurable proxies for progress without losing sight of the qualitative, often un-measurable, goals that truly matter. |
| **Abstraction vs. Application** | How to build and reason with abstract models without them becoming disconnected from any concrete, practical application. |
| **Incremental Progress vs. Global Value** | How to ensure that local optimizations and incremental improvements are genuinely contributing to the overall value proposition of the holon. |

### E.13:4 - **Solution**

FPF elevates **Pragmatic Utility (Pillar P-7)** to a normative architectural principle, operationalized through two mandatory conceptual mechanisms.

#### E.13:4.1 - The Principle of Pragmatic Utility (Expanded Definition)

Any artifact created within the FPF is an instrument for achieving a specific, pragmatic `U.Objective`. The value of an artifact is determined solely by its **utility** in achieving that objective, not by its epistemic scores in isolation.

#### E.13:4.2 - Mechanism 1: The Proxy-Audit Loop

To formally manage the risk of Goodhart's Law, FPF introduces a conceptual feedback loop to periodically review the alignment between proxy characteristics and their intended goals.

*   **New Normative Relation:** A new relation, `isProxyFor: U.Characteristic → U.Objective`, is introduced. This relation **MUST** be used to explicitly declare when a measurable characteristic is serving as a proxy for a higher-level, often qualitative, goal.
*   **Conceptual Audit Process:** Any characteristic marked with the `isProxyFor` relation is subject to a **periodic conceptual audit**.
*   **Review Roles:** This audit is conceptually performed by the individual(s) in the **`Strategist`** role. They are tasked with answering the question: *"Is optimizing for this proxy still reliably driving progress toward the actual `U.Objective` it represents, or have we observed a divergence?"*
*   **Output Concept:** If a divergence is identified, a high-priority `U.Method` for revising or replacing the proxy **MUST** be proposed.

> **Didactic Note for Managers: Are You Climbing the Right Mountain?**
>
> The Proxy-Audit Loop is your compass. Your team's dashboards might show all green—metrics are improving, targets are being hit. But the audit loop forces a crucial question: "Are these the *right* metrics?"
>
> Imagine you are trying to improve "customer satisfaction" (`U.Objective`). You choose "average call handle time" as a proxy metric. Your team successfully drives this number down. But the Proxy-Audit reveals that customer satisfaction is actually *decreasing* because agents are rushing and providing poor service to meet the time target. The loop forces you to recognize this divergence and find a better proxy (e.g., "first-call resolution rate"). It ensures your team is not just climbing fast, but climbing the right mountain.

#### E.13:4.3 - Mechanism 2: The Minimally Viable Example (MVE) Mandate

To enforce a pragmatic, value-first approach from the very beginning of a project, any new `U.System` or major system component **MUST** begin its development cycle with the creation of a **Minimally Viable Example (MVE)**.

*   **Definition:** An MVE is a simple, end-to-end, working instance of the holon that demonstrates the achievement of at least one core, user-facing objective, however trivial. It is the FPF equivalent of a "Hello, World" for a complex system.
*   **Assurance Requirement:** The MVE **MUST** achieve a minimum of **`AssuranceLevel:L1 (Substantiated)`**. This means the MVE cannot be a mere mock-up or a purely conceptual sketch; it must be supported by at least one piece of tangible evidence (e.g., a passing test case, a formal assertion), as defined in Pattern B.3.3.
*   **Stege transition Precedence:** The development of the full-scale holon cannot proceed to `AssuranceLevel:L2` until the MVE has been created and has met its L1 requirement.

### E.13:5 - **Conformance Checklist**

*   **CC-E13.1 (Proxy Declaration Mandate):** Any `U.Characteristic` used as a primary driver for an objective **MUST** be explicitly linked to that `U.Objective` via the `isProxyFor` relation.
*   **CC-E13.2 (Proxy-Audit Mandate):** A formal Proxy-Audit review **MUST** be conducted at regular conceptual intervals (e.g., before each major release). The outcome of this review **MUST** be a documented episteme.
*   **CC-E13.3 (MVE Mandate):** The development of any new `U.System` **MUST** be preceded by the creation of an MVE that satisfies the `AssuranceLevel:L1` requirement.
*   **CC-E13.4 (MVE Traceability):** The full-scale `U.System` **MUST** maintain a formal traceability link (`isEvolutionOf`) to its originating MVE.

### E.13:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Perfectly Engineered Irrelevance"** | The team delivers a technically brilliant system that is formally verified and validated, but no one wants to use it because it doesn't solve a real problem. | **CC-E13.3** forces the team to build a working, end-to-end slice of value (the MVE) *first*. This grounds the entire project in a demonstrated solution to a real user need from day one. |
| **The "Metric Myopia"** | The team becomes obsessed with improving a specific KPI, ignoring clear signs that this is not improving—and may even be harming—the overall user experience or business goal. | **CC-E13.2** mandates the Proxy-Audit Loop. This forces a periodic, strategic step-back, where the `Strategist` role is constitutionally required to ask, "Are we still measuring what matters?" |
| **The "Big Design Up Front" Trap** | The team spends months creating a vast, abstract, and highly detailed model of a system before ever building a single working component. | The **MVE Mandate** prevents this. It forces an iterative, pragmatic "build-to-learn" approach, ensuring that models are always grounded in a working reality. |

### E.13:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Defense Against Goodhart's Law:** The Proxy-Audit Loop is a concrete, operational defense against the common failure mode of optimizing for the wrong thing. It forces regular, strategic reflection on the meaning of metrics. | **Introduces Strategic Overhead:** The Proxy-Audit Loop and the creation of an MVE require dedicated time for strategic thinking and early implementation. *Mitigation:* This is not an expense but a strategic investment. This upfront effort is designed to prevent the far greater cost of developing the wrong system over months or years. |
| **Ensures Value-Driven Development:** The MVE Mandate guarantees that all major development efforts are grounded in a demonstrated, working solution to a real problem, however small. This prevents teams from investing significant resources in abstract models that have no proven path to practical application. | - |
| **Prevents "Analysis Paralysis":** By requiring an early, working example, this principle encourages an iterative, pragmatic development style. It forces teams to build and learn, rather than over-specifying in a vacuum. | - |
| **Positions FPF as an Engineering Discipline:** This pattern firmly anchors FPF as a tool for practical engineering, not just theoretical modeling. | - |

### E.13:8 - **Rationale**

This pattern operationalizes **Pragmatic Utility (P-7)**. While Pattern E.12 protects the *agent* from the cognitive overload of the framework, this pattern protects the *problem* from being lost in a sea of formal abstraction. It provides the necessary constitutional guardrails to keep the powerful formal methods of FPF focused on delivering tangible, real-world value.

The **MVE Mandate** ensures that every journey starts with a destination in sight. The **Proxy-Audit Loop** ensures that the compass used on that journey remains pointed in the right direction. Together, these mechanisms guarantee that knowledge generated within FPF is not only formally correct and epistemically reliable, but also meaningful, useful, and aligned with its intended purpose.

### E.13:9 - **Relations**

*   **Implements:** Pillar `P-7 Pragmatic Utility`.
*   **Complements:** `E.12 Didactic Primacy & Cognitive Ergonomics`.
*   **Provides context for:** The definition of `U.Objective` and `U.Characteristic` by establishing a formal link between them.

### E.10:End

## E.14 - Human‑Centric Working‑Model

### E.14:1 - Intent

Establish a **single, human‑centric Working‑Model** that practitioners can read, discuss, and evolve **without exposure to formal machinery**.  
Each statement **declares a justification stance** (`validationMode`) and, when assurance is sought, attaches **appropriate grounding** via one or more assurance shoulders — **Mapping**, **Logical**, **Constructive** — and **may additionally attach Empirical Validation** (evidence) as defined by the Trust & Assurance calculus. Empirical Validation can accompany any stance; it is **required** when the stance is *postulate*. Assurance shoulders sit **beneath** the Working‑Model and **never define its vocabulary**.
 
+Put bluntly: *one model people work in; three assurance shoulders — plus empirical checks when the world is the judge.*

### E.14:2 - Problem & Context

+Teams need **one shared Working‑Model** to make decisions at speed. Historically this surface either:

* **drifts into jargon**—different terms for the same thing, slash‑labels, partial overlaps; or
* **calcifies into machinery**—too formal for day‑to‑day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable surface**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the surface is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working‑Model layer**: curated kinds and relations expressed in plain terms, governed by simple human rules.
* A **three‑rung Assurance stack** beneath it—**Mapping**, **Logical**, **Constructive**—that carries the heavy arguments (concept alignment, relational semantics, generative traces) and **never leaks back** into the Working‑Model narrative.

This pattern dovetails with the framework’s unification stance (**small Working‑Model surface, rigorous foundations**) and with our constructional mereology commitments (**sum/set/slice** provide extensional identity), while keeping the Kernel minimal and meta‑only.

### E.14:3 - Forces

1. **Cognitive economy vs. semantic precision.**
   Managers and engineers must navigate with a handful of names and relations; assurance authors must still certify that those names and relations **are unambiguous and extensional**.

2. **Speed of change vs. guarantees.**
   The Working‑Model must accommodate rapid iteration; the Assurance stack must **lag just enough** to check, without blocking practical progress.

3. **Parsimony vs. expressivity.**
   The Working‑Model should **not proliferate relation types or ad‑hoc categories**; fine‑grained distinctions live in the Assurance layers and are surfaced **only when they materially change a decision**.

4. **Downward grounding vs. upward contamination.**
   Grounding must always flow **down** (Working‑Model → Mapping → Logical → Constructive). No dependence **up** is allowed: proofs and traces never dictate wording or layout in the Working‑Model.

5. **Trans‑disciplinary unification vs. local dialects.**
   The Working‑Model must reconcile different disciplines’ habits **without erasing them**; Mapping captures dialects, while the Working‑Model exposes a **single usable choice**.

6. **Auditability vs. readability.**
   Every Working‑Model statement must be **auditable on request**, yet day‑to‑day views **hide the scaffolding** unless summoned.


### E.14:4 - Solution

#### E.14:4.1 - Human-Centric principles

> **E.14‑P.1 – Working‑Model first, stance explicit.**  
> Operate one **Working‑Model** for all human‑facing discussion. For **each** assertion, the author **SHALL declare** a justification stance (`validationMode`) and choose the **appropriate assurance shoulder(s)**: **Mapping** (term↔kind alignment via **Lang‑CHR** / D‑Projection), **Logical** (CT2R alias semantics, scope/constraints), **Constructive** (Γₘ generative trace), and **Empirical Validation** (evidence via `U.EvidenceRole` in a declared `U.BoundedContext`).

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small surface, big proof.**
> The Working‑Model exposes a **minimal set** of names (L‑1/L‑2 registers) and **a compact family of relations** used in everyday reasoning; precision and completeness are **proved below**.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears on the Working‑Model surface**.

> **E.14‑P.5 – Justification modes are explicit.**  
> Each Working‑Model relation **declares** `validationMode ∈ {axiomatic, inferential, postulate}`.  
> _axiomatic_ → **Constructive** grounding (Γₘ trace via `tv:groundedBy`); _inferential_ → **Logical** grounding (reasoned chain, often KD‑CAL‑backed for epistemic ties); _postulate_ → **Empirical Validation** (evidence bundle with scope and timespan). Empirical Validation (**LA**) may also accompany _inferential_ or _axiomatic_ claims as real‑world confirmation. **Mapping** contributes **TA**, **Logical/Constructive** contribute **VA**, and **Empirical** contributes **LA** (per the Trust & Assurance calculus; no calculus variables appear on the Working‑Model surface).

> **E.14‑P.6 – Parsimony at the surface.**
> No new Working‑Model relation types are introduced if the existing Logical aliases plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – Evidence is a first‑class support.**  
> When *postulate* is chosen, authors **SHALL** attach an **evidence pointer** (Empirical Validation) appropriate to the claim and context, governed by `U.EvidenceRole` within a declared `U.BoundedContext`.  
 
### E.14:5 - Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees**, and **how a single Working‑Model statement is carried down**.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — terms appearing on the surface are L‑1 or L‑2; L‑3/L‑4 remain in Mapping as synonyms or symbols.

**Obligations.**

* Every Working‑Model edge and node is **grounded downward** (see below).
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **callable on demand**.

#### E.14:5.2 - Assurance‑1: Mapping (from words to kinds)

**Role.** Consolidate human labels from varied sources and **bind them to the chosen kinds** used on the Working‑Model.

**Guarantee.** For any Working‑Model label, there exists a **stable alignment** to exactly one kind; synonyms, abbreviations, locales and registers are recorded here, **not** on the surface. Mapping primarily raises **Typing Assurance (TA)** by consolidating synonyms/registers and binding tokens/labels to **one chosen kind**; calculus‑level metrics live outside Part E.

**Deliverable.** A compact alignment table per scope that makes it obvious which **one label** the Working‑Model will show and which alternatives are tolerated in background sources.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to alias semantics)

**Role.** Give each Working‑Model relation **a precise alias meaning** and **its admissible use‑cases**, keeping the surface vocabulary small.

**Guarantee.** A Working‑Model edge such as *Component‑of* or *Aspect‑of* **carries one intended reading** (transitivity/antisymmetry expectations, scope notes), sufficient for auditors to assess whether the **use is legitimate** in a given context.

**Deliverable.** A short set of alias rules: “When an edge is labeled *Component‑of* at the surface, it intends the structural reading that is later verified by construction.” The Logical layer is **the Standard** that ties human labels to accepted meanings (CT2R alias rules); it primarily contributes **Verification Assurance (VA)**. Calculus‑level symbols are not used in E‑patterns.

*(Rationale: logical aliasing protects the small surface from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance‑3: Constructive (from meanings to generative traces)

**Role.** Provide **extensional guarantees** by **constructing** the wholes, collections, and slices that Working‑Model relations speak about.

**Guarantee.** For structural edges, **there exists a constructional narrative** (e.g., *sum*, *set*, *slice*) that, if told, would recreate the whole from its parts or the aspect from its bearer; this makes identity and containment **trackable and testable** across scales.

**Deliverable.** A **single generative story** per structural link (axiomatic justification). For non-structural ties on the surface (e.g., epistemic links), Constructive may be absent; Logical/Empirical take the lead. Constructive contributes **VA** (extensional identity via Γₘ); for **structural** edges, `tv:groundedBy` **MUST** reference exactly one Γₘ trace.

*(Rationale: constructional grounding turns everyday part‑whole talk into statements whose identity conditions are not left to taste.)*

#### E.14:5.5 - Assurance‑4: Empirical Validation (from claims to observed world)

**Role.** Record when and where a Working‑Model claim meets reality.  
**Guarantee.** Every empirical binding names a **`U.BoundedContext`**, a **target claim/scope**, and a **timespan**; **staleness/refresh** are managed per context policy.  
**Deliverable.** A `U.EvidenceRole` binding (status‑only) anchored into the Evidence–Provenance chain. Empirical Validation contributes **LA** (raises empirical **R** and constrains **G** to its validated envelope).

#### E.14:5.6 - The downward grounding for a single surface statement

Consider a Working‑Model arrow **A –Component‑of→ B**:

1. **Mapping** shows that the words *A* and *B* are the chosen labels for their kinds; it retains tolerated synonyms and symbols in the background.
2. **Logical** confirms that **Component‑of** on the surface means the **structural reading** with its ordinary mereological expectations; if the surface used *Member‑of* instead, Logical would similarly certify the intended reading and its boundaries.
3. **Constructive** exhibits the **constructional narrative** (e.g., a _sum_ of parts resulting in **B** with **A** among them), which yields **axiomatic justification** for the structural edge, sets `validationMode=axiomatic`, and binds the edge via **`tv:groundedBy → Γₘ.sum|set|slice`**.
4. **Empirical Validation** records the **evidence pointer** and scope that make the claim auditable within its `U.BoundedContext` (required for *postulate*; optional reinforcement for other stances).

Together, these three **ground the human arrow without leaking their machinery upward**. The Working‑Model remains simple; the Assurance stack carries the proof.

### E.14:6 - Archetypal Grounding *(System / Episteme)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

#### E.14:6.1 - `U.System` — Working‑Model first, Constructive grounding available

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When stronger assurance is sought, the same author **narrates** the constructive story of the whole as a composition of parts and, where appropriate, attaches a downward grounding to that narrative (sum / set / slice). The narrative remains concept‑level and notation‑neutral; order and time stay out of structure and are expressed in their own planes.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary surface; the constructive story is *supporting*, not *defining*.

#### E.14:6.2 - `U.Episteme` — Working‑Model first; Logical/Mapping preferred; Empirical evidence as appropriate

* **Publication (Working‑Model).** Authors connect meaning‑bearing artefacts using knowledge relations (e.g., **RepresentationOf**, **UsageOf**) in the same human‑oriented style.
* **Assurance (downward grounding).** Here assurance typically flows to the **Logical** or **Mapping** shoulders (reasoned argument; type/lexical alignment). **Empirical Validation** is used where observation is the right currency (status‑only roles on epistemes); Constructive grounding is optional and used only where a structural interpretation is genuinely intended.
* **Canonization move.** Again, Working‑Model text is the public form; assurance is attached deliberately and separately, without leaking method or time semantics into structure.

**6.3 - Pattern lesson (both cases)**
The **Working‑Model layer remains the canonical publication surface** for authors and reviewers; **assurance layers** (Mapping / Logical / Constructive) are **opt‑in** and used purposefully, with grounding flowing **downwards** from the Working‑Model to the appropriate shoulder. This presentation respects the authoring template’s *Archetypal Grounding* requirement and keeps notational choices illustrative rather than defining. 


### E.14:7 - Bias‑Annotation *(what to watch for, and the counter‑moves)*

| Bias (name)                       | Symptom in drafts                                                                           | Conceptual counter‑move                                                                                                                        | Where this is governed                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture**             | Treating a constructive narrative as “the real thing,” with **ut:\*Of** reduced to a label. | Re‑assert Working‑Model primacy: publish in **ut:\*Of**; attach assurance **downwards** only when needed.                                      | E.8 template; Notational‑Independence guard‑rail.                    |
| **Canonical inversion**           | Demanding constructive grounding for epistemic links by default.                            | Keep the **progressive** stance: prefer Logical/Mapping assurance for knowledge claims; raise to Constructive only when structure is at issue. | Authoring template; Working‑Model pattern family.                    |
| **Layer leakage (order/time)**    | Encoding sequence or phase as part–whole to “strengthen” claims.                            | Keep **order**/**time** in their planes; do not smuggle them into structure.                                                                   | Style/structure guidance in Part E; flavour separation in Γ‑family.  |
| **Collection ↔ Composition swap** | Using **MemberOf** as if it implied **ComponentOf** identity.                               | Keep collections (*set*) distinct from assemblies (*sum*); do not upgrade membership to component status.                                      | Working‑Model mereology guidance (Part B/C linkage).                 |
| **Notation lock‑in**              | Letting a diagram or syntax define meaning.                                                 | Apply **Notational Independence**: define semantics in prose (maths if needed); treat renderings as informative.                               | Notational‑Independence guard‑rail.                                  |
| **Backwards dependency**          | Letting an assurance artefact redefine public terms.                                        | Preserve **unidirectional dependence**: Working‑Model terms do not derive their meaning from assurance artefacts.                              | Part E guard‑rails (dependency discipline).                          |
| **Silent stance**                 | Publishing claims with no declared assurance stance.                                        | Declare the stance explicitly (e.g., working claim vs reasoned vs constructive).                                                               | Style/authoring discipline in Part E.                                |

> **Reading reminder.** Bias checks are *conceptual* reading aids; they never introduce notational or tooling mandates.

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical surface for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC‑E14‑2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working‑Model to the appropriate assurance shoulder (**Mapping / Logical / Constructive / Empirical**) and **SHALL NOT** impose vocabulary back onto the Working‑Model. | Maintain plane separation and cognitive economy. |
| **CC‑E14‑3 (Stance declaration).**         | For any claim where assurance matters, the author **SHALL** declare `validationMode` (*postulate / inferential / axiomatic*).                                                    | Make assurance intent explicit and readable.                  |
| **CC‑E14‑4 (No order/time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part–whole; keep them adjacent in their own planes.                                           | Prevent layer leakage and category errors.                    |
| **CC‑E14‑5 (Collection ≠ Composition).**   | Authors **SHALL** keep **membership** claims distinct from **component** claims; no implicit upgrade from collection to assembly.                                                | Guard extensional identity and reader expectations.           |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |  
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back‑defining Working‑Model terms by their assurance artefacts; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |  
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support the formality ladder without burdening early drafts.  |
|**CC-E14-10 (Structural grounding handshake).** | For **structural** edges on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.sum|set|slice` (see **Compose-CAL** and **CT2R-LOG**). Exactly **one** Γₘ trace is permitted per edge (CI rule alignment). | Aligns E.14 with CT2R-LOG and Compose-CAL; ensures extensional identity. |
| **CC‑E14‑11 (Empirical bindings).**        | When `validationMode=postulate` (or when adding real‑world confirmation), authors **SHALL** bind evidence via `U.EvidenceRole` in a declared `U.BoundedContext` with an explicit **timespan** and provenance anchors. | Aligns with Evidence Graph Referring and empirical ageing policies. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model artefacts **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable surfaces). Assurance artefacts **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids legacy “tiers/modes”. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Assembly from parts → “Component Of”**
   A pump skid is agreed to be nothing over and above its pump, frame, reservoir, and valve set considered together. Because the whole is conceptually *constructed* from those parts, the team may safely speak of each part as *Component Of* the skid. The justification is the construction itself: if any listed part were removed, the very same skid would no longer exist as that whole. This keeps identity extensional and makes the engineer‑facing alias (“Component Of”) truthful rather than conventional.

2. **Parallel elements gathered → “Member Of”**
   A test rig has four identical cartridges used in parallel. The rig treats them as a conceptual *gathering*; membership is fixed by inclusion in that gathering, not by sequence or timing. Speaking of each cartridge as *Member Of* the rig’s cartridge bank is then licensed by the same gathering act. Engineers can keep saying “member,” while architects know the warrant is the underlying construction of the bank as a collection, not an accidental tagging.

3. **Focused facet carved → “Aspect Of”**
   When the team talks about the *thermal envelope* of a reactor, they are not multiplying entities; they are taking the already‑agreed reactor and conceptually *carving out* its thermal facet for focused reasoning. Calling that carve‑out an *Aspect Of* the reactor is justified because the aspect owes its identity to the parent and the chosen facet, and nothing else. This licenses disciplined talk about “boundary,” “interface,” or “envelope” without mistaking them for independent systems.

> **Notes across the examples**
> • Everyday aliases (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; their truth is anchored by prior constructional choices.  
> • Structural links draw on **Constructive** grounding; **epistemic links**—like “Representation Of” or “Usage Of”—may instead rely on **Empirical Validation** (evidence bundles) or **Logical** grounding appropriate to the claim.  

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **Single dial for containment.** Teams can ask one plain question—“what is inside what?”—and trust that all structural talk reduces to shared constructional choices rather than ad‑hoc relation lists. Ontologists keep rigorous warrants without burdening day‑to‑day readers.
* **Extensional identity by default.** Wholes are the wholes they are because of the parts gathered; collections are the collections they are because of their members; aspects inherit identity from their parent and facet. This prevents silent drift when labels change.
* **Layer harmony.** Engineer‑facing aliases live at the same level as other relation names, while their warrants live one step below, keeping human language clean and the generative basis auditable.

**What to watch**

* **Discipline at the structural tier.** A structural link that lacks a constructional warrant is conceptually unsafe. Conversely, forcing epistemic links to pretend they are structural over‑physicalises knowledge claims; for those, evidence or argument is the right currency.
* **Author workload moves, not grows.** Day‑to‑day model authors stay with aliases; specification authors carry the burden of ensuring every structural statement really follows from a sum, a gathering, or a carve‑out. This is a conscious shift of complexity away from operations and into the pattern’s foundation.

**Invariants you must preserve**

* **Parsimony of constructors.** Build wholes by summing parts; build banks by gathering elements; focus facets by carving aspects. Do not invent extra generative acts for parallelism or time‑slicing; those concerns belong to other conceptual services.
* **Two‑tier justification.** Structural talk rides on construction; epistemic talk rides on evidence or proof. Keep the boundary sharp so that later reasoning (about reliability, compliance, or policy) remains clear.

**Known consequences**

* **Stable queries, fewer surprises.** Because aliases are backed by shared constructions, teams from different disciplines can interoperate without renegotiating meanings at hand‑off.
* **Audit trail without jargon.** Reviewers can trace every structural claim to a prior constructional choice, while everyday collaborators keep using familiar relation names.


### E.14:9 - Consequences

| Benefits                                                                                                                                                      | Trade‑offs / Mitigations                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Human‑first clarity.** Readers see the **Working‑Model layer** as the canonical publication form; Assurance layers remain optional and purpose‑driven.      | **Extra author discipline.** Declaring the stance and (when needed) a short grounding narrative takes effort; mitigated by the authoring template and style guide.           |
| **Progressive assurance.** Teams can start light and raise strictness deliberately (Mapping → Logical → Constructive) without changing the visible relations. | **Risk of “forever‑light.”** Some models may remain in low‑assurance stances; mitigated by the formal maturity ladder and reviewer prompts to escalate where risk warrants.  |
| **Layer hygiene.** Order/time remain outside mereology; structural identity is neither overloaded nor diluted.                                                | **Split attention.** Authors must learn to keep planes distinct; mitigated by the Tell‑Show‑Show pedagogy across architectural patterns.                                             |
| **Spec cohesion.** The same section order and safety subsections (Bias‑Annotation, Conformance Checklist) keep patterns comparable and auditable.             | **Tighter prose.** Patterns grow by a few concise checks; mitigated by the canonical template.                                                                               |

> **Quotable closer.** *“One layer to speak, three layers to justify—only when needed.”*


### E.14:10 - Rationale

**Why Working‑Model is canonical.** FPF privileges **human‑oriented relations** as the primary interface for thinking and communication. This satisfies didactic primacy while preserving conceptual integrity: formal work serves the human layer, not the other way around. The canonical template and style principles institutionalise this choice without inviting notation lock‑in.

**Why grounding flows downward.** Mapping, Logical, Constructive, and Empirical supports are **assurance shoulders** that sit *beneath* the Working‑Model claim. Authors select the shoulder(s) that fit purpose and risk: type/lexical alignment (**TA**), reasoned consequence (**VA**), constructive reconstruction (**VA**), and real‑world confirmation (**LA**). This keeps the Kernel small, avoids plane‑mixing, and provides a clear path to stronger guarantees when warranted.

**Why patterns teach before they tighten.** The Tell‑Show‑Show requirement couples each universal rule with System/Episteme illustrations, reducing cognitive load and preventing premature formalism. It is the didactic mechanism that makes Human‑Centric Canonization practical across disciplines.

**Why no notation talk in Core.** Guard‑rails and the style guide prohibit tool jargon and notation dependence inside normative prose; meanings are given in words and mathematics, with any renderings treated as illustrative only. This preserves longevity and cross‑disciplinary portability.

### E.14:11 - Relations

**Builds on:**

* **E.8 Authoring Conventions & Style Guide** — section order, style principles, and mandatory safety subsections used here.
* **E.7 Archetypal Grounding** — the Tell‑Show‑Show rule applied in this pattern’s own Grounding section.
* **C.2.3 Unified Formality Characteristic (F)** — declares the **F** scale and **ΔF** moves for progressive rigor; Working-Model artefacts **SHALL** declare **F** and remain notation-agnostic.

**Coordinates with.**

* **CT2R‑LOG — Working‑Model Relations & Grounding** — alias rules and `tv:groundedBy` Standard for edges grounded in Γₘ.   
* **Compose‑CAL (Constructional Mereology)** — provides the constructive shoulder (Γₘ: **sum | set | slice**) used to ground structural edges.
* **E.10 Lexical Discipline & Stratification** — ensures naming discipline and register hygiene when the human layer is published.

**Constrains:**

* All architectural patterns that publish relations **SHALL** present them in the Working‑Model layer and **MAY** attach assurance only as needed, preserving plane separation and notational independence. (Template conformance as per E.8.)

**Informs.**

* Part F unification practices (context of meaning, bridges, fit levels) by reinforcing the preference for human‑readable labels with explicit alignment notes rather than silent formal substitutions.

### E.14:End

## E.15 - Lexical Authoring & Evolution Protocol  (LEX‑AUTH)

> *Author patterns as evidence‑bearing epistemes, evolve them via governed open‑ended search, and publish an auditable trace that improves quality—not just compliance.*

### E.15:1 - Context

FPF patterns are the **canon**: they define the generative rules that other artifacts depend on. Teams need to **change** patterns as the SoTA moves, but ad‑hoc edits lead to drift, weak comparability, and brittle downstream updates. We need a **method** that (a) *generates* better alternatives, (b) *selects* them against explicit quality/assurance targets, and (c) *publishes* a machine‑ and human‑checkable **trace** that can be replayed, audited, and re‑run. (Built to cohere with **DRR (E.9)**, **LEX‑BUNDLE (E.10)**, **Canonical Evolution Loop (B.4)**, **NQD/E‑E (C.18/C.19)**, **Evidence Graph Referring (A.10)**, **Trust (B.3)**, **F‑Suite validation (F.15)**.)

### E.15:2 - Problem

Without a disciplined authoring protocol:

* **One‑shot generation** dominates; there is no *evolutionary* path from vN → vN+1.
* “Trace” degenerates into a proof‑of‑work: *a method ran*, not *quality improved*.
* Pattern edits blur **lexicon vs. norms vs. examples**, breaking didactics and tool‑independence.
* SoTA content is cited but not **integrated** via Bridges & CL; claims get over‑ported.

### E.15:3 - Forces

| Force                                       | Tension we must resolve                                                           |
| ------------------------------------------- | --------------------------------------------------------------------------------- |
| **Generativity vs Assurance**               | Open‑ended idea generation must not erode safety/traceability.                    |
| **SoTA speed vs Canon stability**           | Frequent small updates must preserve conceptual integrity and roll‑up invariants. |
| **Local meaning vs Global reuse**           | Context‑local meaning must cross contexts only via **Bridges** with CL penalties. |
| **Notational independence vs Checkability** | Text must stay notation‑free yet be verifiable by Tooling harnesses.              |

### E.15:4 - Solution — A *governed evolutionary* authoring method with a publishable **LEX‑AUTH Trace (LAT)**

LEX‑AUTH defines **how** a pattern is **proposed, varied, selected, validated, and merged**, with artifacts and evidence fit to the FPF kernel.

#### E.15:4.1 - Method (design‑time choreography)

**Stage A — Frame & Scope (Context, Objectives, Invariants)**

1. **Anchor** the work in a **`U.BoundedContext`** for the spec (e.g., `FPF/Core`), cite governing guard‑rails (**E.5.\***), and state **objectives** for the change (e.g., clarity ↑, universality ↑, assurance cost ↓).
2. **Declare the Delta‑Class** (see §4.3) and **impact radius** (dependent patterns, bridges, tests).
3. **Fix acceptance targets** (see §4.4 Quality & SoTA metrics).

**Stage B — Generate candidates (SoTA + NQD)**
4. **Harvest SoTA** inputs (standards, rival patterns, lived domain idioms) and **bind** them as *evidence* via `U.EvidenceRole` with **claim/claim‑scope/timespan** (empirical vs deductive lines).
5. **Generate candidate variants** using **NQD‑CAL** engines (Novelty/Quality/Diversity) with an **E/E policy** (explore↔exploit governor) to populate a **Pareto front** of pattern phrasings/structures. *(No single shot; multiple candidate clauses compete.)*

**Stage C — Shape & Align (Structure, Bridges, USM)**
6. **Shape** top candidates into the standard **architectural template** (Context → Problem → Forces → Solution → CC → Consequences → Rationale), obeying **LEX‑BUNDLE** (no tooling jargon; twin registers allowed).
7. **Bridge across Contexts** explicitly (F.9): any imported definitions/claims declare **CL** and *loss notes*; propose scoped **narrowing** where needed.
8. **Type scopes** with **USM (A.2.6)**: keep **ClaimScope (G)** distinct from **WorkScope**; no “applicability/envelope” smuggling.

**Stage D — Validate & Decide (Assurance, Tests, DRR)**
9. **Run the harness**: update **SCR/RSCR** (F.15), lint lexical rules (E.10), run **Γ‑consistency** and **RSG/SoD** checks where relevant.
10. **Score** candidates on **Quality & SoTA metrics** (§4.4) and **assurance deltas** (Δ⟨F,G,R⟩).
11. Record a **DRR** (E.9) with *options considered*, *trade‑offs*, chosen candidate, *blast‑radius*.
12. **Merge** the winner; version pattern **SemVer** by Delta‑Class.

**Stage E — Publish & Monitor**
13. Publish the **LEX‑AUTH Trace (LAT)** (§4.2) with the pattern.
14. Schedule **evidence refresh** windows and an **evolution watchpoint** (B.4 loop): when metrics or SoTA inputs decay, reopen Stage B.

#### E.15:4.2 - The **LEX‑AUTH Trace (LAT)** — what it is and why it matters

A LAT is **not** “we ran a script.” It is a **structured episteme** that lets others **reproduce quality gains** and **re‑run** the search when SoTA shifts.

**LAT minimal contents (publish with the pattern):**

1. **Context & version** (pattern id, context, SemVer, Delta‑Class).
2. **Objective vector** (what we tried to improve: clarity, universality, assurance cost, etc.).
3. **SoTA pack** (sources bound as `U.EvidenceRole` with claim/scope/time and polarity).
4. **NQD settings** (emitters/lenses, diversity characteristics) + **E/E policy** used.
5. **Candidate set** (top K variants with NQD scores + short deltas from baseline).
6. **Bridge ledger** (all cross‑context imports with **CL** and loss notes).
7. **Assurance delta** (Δ⟨F,G,R⟩ from baseline; penalties from CL applied).
8. **Harness results** (checks passed/failed, test diffs).
9. **DRR link** (decision rationale id).
10. **Refresh policy** (evidence decay windows and triggers).

**Uses of the LAT:**
*Reproducibility* (re‑run B‑stages as SoTA changes), *assurance* (explicit impact on F/G/R), *portfolio health* (diversity/coverage), *teaching* (didactic before/after), and *cross‑context safety* (no silent imports).
Publish the pattern with a DRR that carries a LAT pointer (id/URI). The LAT itself is a U.Work evidence pack (non‑normative), archived with edition and Γ_time.

**Example of a LAT‑stub**
```
LAT:
  context: FPF/Core, pattern: F.15, semver: x.y+1, delta-class: Δ‑2
  objectives: {clarity↑, universality↑, assurance-cost↓}
  SoTA-pack: {OpenAlex 2025‑Q3, SPECTER2‑23, DPP‑2019, MAP‑Elites‑2015+}
  NQD-settings: {CharacteristicSpace: domain‑family × …, grid: CVT@k=16}
  candidates: K=4 (wording of RSCR‑F04 & gates)
  bridge-ledger: none (intra‑canon refs only)
  assurance‑delta: ΔF=+, ΔG=+, ΔR=+ (after CL‑penalties=0)
  harness: LEX‑BUNDLE lint pass; F‑suite pass; Γ‑consistency ok
  DRR-id: DRR‑2025‑09‑DFCM‑roll‑in
  refresh: F1‑Card edition refresh window = 6 mo
```

#### E.15:4.3 - What counts as “changed the pattern as a whole” — **Delta‑Classes & versioning**

Classify the intended change **before** work starts (declared in DRR & LAT):

* **Δ‑0 Lexical polish** — wording/ordering only; **no** change to CC or semantics. → *Patch* (x.y.**z**+1).
* **Δ‑1 Didactic restructure** — narrative/layout; **unchanged** Conformance Checklist (CC). → *Minor* (**x.y**+1.0).
* **Δ‑2 Normative refinement** — CC tightened/clarified; *semantics preserved* by test equivalence. → *Minor* (**x.y**+1.0) + **RSCR** required.
* **Δ‑3 Semantic change** — CC **adds/removes** requirements; downstream contracts shift. → *Major* (**x**+1.0.0) + **impact review** + **bridges refresh**.

> **Definition of “pattern changed as a whole”:** any **Δ‑2/Δ‑3** change (i.e., the **normative surface** or **semantics** changed) counts as a pattern change in the canonical corpus and triggers harness & bridge reviews.

#### E.15:4.4 - Quality & SoTA metrics (selection lenses)

**Mandatory lenses** (declare in LAT; higher is better unless noted):

* **Clarity** (readability; plain‑register score from didactic rubric).
* **Universality** (C‑1): *≥3 heterogeneous domains* anchored in the Archetypal section.
* **Lexical discipline** (E.10): 0 violations (DevOps lexicon, process/function conflations).
* **Assurance delta**: ΔF (formality), ΔG (scope clarity), ΔR (reliability after CL penalties).
* **Bridge integrity**:  Bridge integrity (policy lens): declare minimum CL thresholds per Context policy; penalties route to R only (B.3/F.9); record policy‑id in LAT.
* **Test conformance**: F‑suite pass; RSCR clean.
* **Exploration health** (NQD): diversity coverage > threshold; no premature convergence.
* **Didactic economy**: length vs density ratio within band; “Tell‑Show‑Show” present.

**Optional lenses** (context‑specific): *Ethical/SoD guard strength; cross‑scale roll‑up integrity; aggregation proofs present;* etc.
### E.15:5 - Conformance Checklist (normative)

**CC‑LA‑1 (Context anchoring).**
Every authoring run **MUST** declare a `U.BoundedContext`, Delta‑Class, objectives, and acceptance lenses **before** generating candidates.

**CC‑LA‑2 (SoTA as evidence).**
External inputs **MUST** be bound as `U.EvidenceRole` epistemes with **claim, claim‑scope, polarity, timespan** (formal/empirical lines). No raw links.

**CC‑LA‑3 (Open‑ended generation).**
At least **K≥3** candidate variants **MUST** be generated via **NQD‑CAL** with a declared **E/E policy**; single‑shot edits violate LEX‑AUTH.

**CC‑LA‑4 (Bridges & CL).**
Any cross‑context reuse **MUST** appear in a **Bridge** with **CL** and *loss notes*. CL penalties apply to **R‑lane** when scoring.

**CC‑LA‑5 (Harness).**
The candidate winner **MUST** pass **LEX‑BUNDLE** lint, **SCR/RSCR** tests, Γ‑consistency, and SoD/RSG gates where applicable.

**CC‑LA‑6 (Assurance deltas).**
The LAT **MUST** publish Δ⟨F,G,R⟩ relative to baseline, explicitly accounting for CL penalties and any narrowed scopes.

**CC‑LA‑7 (DRR).**
A **DRR** entry is mandatory for Δ‑2/Δ‑3 changes; it records options considered, rationale, and impact radius.

**CC‑LA‑8 (Refresh plan).**
Empirical evidence in the LAT **MUST** carry a **decay/refresh** window; a watchpoint **MUST** be scheduled in the Canonical Evolution Loop.

**CC‑LA‑9 (Publication).**
Publish the **pattern + LAT** together; past LATs are immutable. New runs produce new LATs.

### E.15:6 - Consequences

**Benefits.**
*Evolutive quality*: patterns improve through **search + selection**, not edits by fiat. *Auditability*: a re‑runnable **LAT** shows *why* the chosen variant won. *Safety*: cross‑context reuse is explicit and penalized appropriately. *Comparability*: Δ‑classes & SemVer let downstream readers predict blast‑radius.

**Trade‑offs.**
Some ceremony (LAT/DRR, NQD lenses) and maintenance (evidence refresh, bridge upkeep). These costs buy reproducibility and SoTA tracking.

### E.15:7 - Rationale & Links (informative)

LEX‑AUTH extends the FPF constitution by **operationalising pattern evolution**: it plugs **B.4 Canonical Evolution Loop** into **E.9 DRR**, binds **SoTA** via `U.EvidenceRole` and **KD‑CAL**, drives **candidate generation** with **C.18 NQD‑CAL** under **C.19 E/E‑LOG**, enforces **lexical discipline** via **E.10 LEX‑BUNDLE**, and validates with **F.15** regression harnesses. Cross‑context safety is carried by **F.9 Bridges** with **CL penalties** in **B.3 Trust**. The whole remains **notation‑independent** (E.5.2) and stays within the **Core → Tooling → Pedagogy** dependency rule (E.5.3).

### E.15:8 - Operators (authoring deltas you are allowed to apply)

* **Refine** (tighten CC without changing acceptance meaning).
* **Split/Merge** (factor patterns; preserve links; update Bridges).
* **Generalise/Constrain** (expand/restrict ClaimScope (G) with proofs or loss notes).
* **Rephrase** (clarify language; leave CC untouched).

Each operator carries a default **Delta‑Class** and test obligations.

### E.15:9 - Self‑application Work Log (how this very pattern was authored)

> *This is **not** chain‑of‑thought; it is the required **`U.Work` evidence** for LEX‑AUTH.*

**Context.** `FPF/Core` (Canon); **Delta‑Class:** Δ‑2 (normative refinement by addition of method & CCs).
**Objectives.** Add an *evolutionary* authoring method; make trace *useful* (quality‑bearing); align with SoTA machinery already in spec.
**SoTA pack (evidence bound).** Prior FPF kernel commitments to **DRR (E.9)**, **E.10 LEX‑BUNDLE**, **B.4 Evolution**, **C.18/C.19** NQD/E‑E, **F.15** harness, **F.9** Bridges, **B.3** Trust; these are treated as the authoritative internal SoTA for the Canon here.
**NQD/E‑E.** Generated ≥3 alternative Solution sections; finalist chosen for clearer Δ‑classes and actionable LAT contents.
**Bridges.** No cross‑external mapping; intra‑canon references only (CL=3).
**Harness.** LEX‑BUNDLE lint (no tooling jargon), CCs unique/atomic, didactic “Tell‑Show‑Show” via Self‑application log, Universality criterion met by cross‑kernel applicability.
**Assurance Δ.** F: + (explicit method & CCs); G: + (scope separation & Δ‑classes); R: + (LAT obligations + bridge penalties).
**DRR.** Recorded: alternatives considered (lighter trace vs full LAT), chosen design (full LAT).
**Refresh.** Reopen when SoTA (e.g., G‑suite authoring kit or CHR templates) evolves or when LAT misuse is seen in reviews.

### E.15:End

## E.16 - RoC‑Autonomy Budget & Enforcement

**Intent.** Make any claim of autonomous behavior testable and enforceable via a published **AutonomyBudgetDecl**, **Guarded enactment**, **Override SpeechActs with SoD**, and a **Work‑anchored AutonomyLedger**. 
**Rule (summary).** If a Role/Method/Service claims autonomy, authors **MUST**: (i) publish an `AutonomyBudgetDecl` with `AdmissibilityConditionsId` and `OverrideProtocolRef`; (ii) gate Method steps with `requiresAutonomyBudget`; (iii) write a `AutonomyLedgerEntry` on every admitted Work; (iv) block on depletion until a `ResumeAutonomy` SpeechAct passes SoD; (v) surface autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.15 / A.21; B.3; C.16; E.8; E.10; E.18; F.4; F.6; F.8; F.15; F.17.
**Coordinates with:** A.13 (Agential Role), C.9 (Agency‑CHR), C.24 (Agent‑Tools‑CAL) where applicable; G.4–G.5–G.8–G.9–G.10 (method authoring/selection/shipping).

### E.16:1 - Problem Frame

Autonomy‑claiming **performers** (*RoleAssignments* over services/robots/teams operating without continuous human direction) must **stay within declared limits** (safety, risk, resource, remit) and **yield** to governance when required. Without a uniform rule, “autonomy” drifts into tacit norms, cannot be benchmarked or audited, and undermines selection (Part G) and publication (Part F).

### E.16:2 - Problem

* **Opaque autonomy.** Patterns assert “autonomous” behavior with no **budget** or **enforcement**.
* **Un‑gated execution.** Methods can execute beyond authority or risk limits.
* **Ad‑hoc overrides.** No standard **SpeechAct** for pausing/de‑scoping; SoD is unclear.
* **Non‑portable publication.** **UTS (Unified Term Sheet)** rows cannot surface autonomy‑critical data for parity or selection.

### E.16:3 - Forces

| Force                          | Tension                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ |
| **Creativity vs Safety**       | Exploration autonomy vs hard constraints and override duties             |
| **Locality vs Comparability**  | Context‑local rules vs cross‑context selection (G‑suite)                 |
| **Simplicity vs Auditability** | Lightweight authoring vs ledger‑grade evidence                           |
| **Autonomy vs SoD**            | Helpful self‑action vs separation‑of‑duties and human‑in‑the‑loop points |

### E.16:3.1 - Bias-Annotation

**Lenses tested:** `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`. **Scope:** Universal for any Role/Method/Service that claims autonomous operation (unsupervised decision or actuation) and is admitted via `AutonomyBudgetDecl` + Green‑Gate. It is **not** aimed at purely assistive “suggestion‑only” tools where each action is confirmed by a human at the point of execution.

* **Gov.** Bias toward enforceable oversight (hard gates, SoD, canonical override SpeechActs). Mitigation: exploration autonomy is still allowed, but only inside an explicit budget and time window.
* **Arch.** Bias toward gate‑and‑ledger structure (Green‑Gate + Work‑anchored `AutonomyLedger`). Mitigation: `telemetrySpecRef` can scope what is emitted when full deltas are unnecessary.
* **Onto/Epist.** Bias toward typed, testable constraints (MM‑CHR tokens, explicit admissibility checks). Mitigation: budgets are optional‑field (`?`) so low‑risk contexts can start minimal and tighten over time.
* **Prag.** Bias toward measurable quotas may under‑express “soft” autonomy goals. Mitigation: pair `decision_tokens` with `risk_bands` to capture non‑counting limits.
* **Did.** Bias toward explicit mechanics increases authoring surface area. Mitigation: provide a default `AutonomyBudgetDecl` template and minimal harness cases in **F.15**.

### E.16:4 - Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** a Role/Method/Service **claims autonomous operation** (any phrasing that implies unsupervised decision or actuation).

**E.16‑S1 (Autonomy Budget — mandatory).**
Any autonomy claim **MUST** publish an **AutonomyBudgetDecl** as a *named, versioned* object in the **same `U.BoundedContext`**:

```
AutonomyBudgetDecl {
  id, version
  scope: ClaimScope (G)                              // where this budget applies
  budget: {                                          // all typed via MM‑CHR (C.16)
    action_tokens?     : Unitful quota / rate
    decision_tokens?   : Unitful quota / rate
    risk_bands?        : CHR vector with acceptance bands
    resource_caps?     : set of unitful caps (Γ_work categories)
    time_window?       : Γ_time window & cadence
  }
  AdmissibilityConditionsId : PolicyIdRef                          // Aut-Guard policy naming gates & penalties
  overrideProtocolRef : Episteme                     // SpeechAct & SoD for pause/resume/escalate
  telemetrySpecRef? : Episteme                       // what to emit into AutonomyLedger
  editionPins : { RoleRef?, MethodDescRef?, CHR refs, …  } 
}
```

**E.16‑S2 (Guarded enactment — Green‑Gate).**
A **Method step** that *requires* autonomy **MUST** list `requires: [RoleX]` **and** `requiresAutonomyBudget: AutonomyBudgetDecl.id`. A **Work** instance is admissible *iff* at enactment time:

* the performer’s **RoleAssignment** is valid and in an **enactable** RSG state (A.2.5);
* the budget accounting for the **AutonomyBudgetDecl** indicates **tokens/limits remaining** for *this* budget in the declared **Γ_time** window (derived from the AutonomyLedger);
* all **guard checks** defined by `AdmissibilityConditionsId` evaluate to **pass** (e.g., risk ≤ band, resource ≤ cap).

Failing any gate **blocks** enactment (no “soft warnings” on Core surface).

**E.16‑S3 (Autonomy Ledger).**
All admissible Work **MUST** record **AutonomyLedger entries**:

```
AutonomyLedgerEntry {
  workId, performedBy: RoleAssignmentId
  budgetId, version, time
  deltas: { action_tokensΔ?, decision_tokensΔ?, riskΔ?, resourceΔ? }
  guardVerdicts: { name → pass|fail }
  pathIds: { PathId, PathSliceId }                  // for G‑suite parity/refresh
}
```

The ledger is **evidence**: attach to `U.Work` (A.15.1) and fold under **Γ_work** and **Γ_time** for reporting.

**E.16‑S4 (Overrides — SpeechActs & SoD).**
Every budget **MUST** reference an **OverrideProtocolRef** that defines canonical **SpeechActs**:

* **PauseAutonomy(budgetId)** — immediate stop of autonomy‑gated steps;
* **ResumeAutonomy(budgetId)** — resume after conditions;
* **NarrowAutonomy(budgetId, Δscope)** — apply stricter limits;
* **Escalate(budgetId)** — handover to a declared **SupervisorRole**.

**SoD:** The override caller **MUST NOT** be the same **RoleAssignment** that is consuming the budget (enforce `⊥` in the Context). All overrides are **Work** (SpeechActs) with **ledger entries** (zero or negative deltas as per policy).

**E.16‑S5 (Depletion behavior).**
When a budget **depletes** (no tokens / envelope exceeded / cap breached):

* **Block** further autonomy‑gated steps in the **same Γ_time window**;
* Emit **DepletionNotice** (SpeechAct), and either **Escalate** or **Park** per policy;
* Only a **ResumeAutonomy** SpeechAct from an admissible Role (per SoD) may reopen the gate.

**E.16‑S6 (Publication in UTS).**
UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy **MUST** include:

* `AutonomyBudgetDeclRef` (id & version);
* `Aut-Guard policy-id (PolicyIdRef)`;
* `OverrideProtocolRef`;
* declared **Scope (G)** and **Γ_time** window;
* edition pins for the referenced Role/Method/CHR.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18/C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

### E.16:5 - Archetypal grounding (Tell‑Show‑Show; human‑centric)

**Show‑A (U.System — mobile robot).**
`Robot_R7#NavigatorRole:Warehouse_2026` executes `Navigate_v3`.
`AutonomyBudgetDecl`: `action_tokens=10 k steps/day`, `risk_bands={maxSpeed ≤ 1.2 m/s, minDist ≥ 0.5 m}`, `resource_caps={battery ≥ 20%}`; `AdmissibilityConditionsId=Aut‑Guard‑R7‑v1`; override via `PAUSE`, `RESUME`, `ESCALATE` SpeechActs by `FloorSupervisorRole ⊥ NavigatorRole`. Ledger entries decrement `action_tokens`, track `minDist`. Depletion at 0 tokens halts autonomous moves and pages supervisor.

**Show‑B (U.PromiseContent — autonomous deploy).**
`DeployerRole` performs step “Promote to prod” under `AutonomyBudgetDecl` with `decision_tokens=3/day`, `risk_envelope={error‑budget burn ≤ 2% / day}`, guard “all pre‑deploy checks pass”. Overrides only by `CABChair#AuthorizerRole ⊥ DeployerRole`.

### E.16:6 - Conformance Checklist (SCR — E.16‑CC)

| ID            | Requirement                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E.16‑CC‑1** | Any autonomy claim **MUST** reference an **AutonomyBudgetDecl** in the same `U.BoundedContext`.                                                                             |
| **E.16‑CC‑2** | **Method steps** that depend on autonomy **MUST** declare `requiresAutonomyBudget: AutonomyBudgetDecl.id` (and `requires: [RoleX]`) and **MUST** be Green‑Gated by the budget’s guards at enactment. |
| **E.16‑CC‑3** | A **Work** admitted under autonomy **MUST** carry an **AutonomyLedgerEntry** with deltas and guard verdicts.                                                                |
| **E.16‑CC‑4** | **Overrides** are **SpeechActs** with SoD enforced (`⊥` between consumer and overrider roles); each override creates a ledger entry.                                        |
| **E.16‑CC‑5** | **Depletion** **MUST** block autonomy‑gated steps until a **ResumeAutonomy** SpeechAct passes SoD and guard checks.                                                         |
| **E.16‑CC‑6** | **UTS rows** for autonomy‑bearing Roles/Methods/Services **MUST** include `AutonomyBudgetDeclRef`, `Aut-Guard policy-id (PolicyIdRef)`, `OverrideProtocolRef`, `Scope (G)`, and `Γ_time`. |

### E.16:7 - Consequences

* **Testability.** Autonomy is measurable (tokens/envelopes), audit‑ready (ledger), and stoppable (SpeechActs).
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

### E.16:7.1 - SoTA‑Echoing (post‑2015 practice alignment)

> Each item states **Adopt / Adapt / Reject**, and why. Vendor/tool tokens are kept as *informative*, not normative.

1. **Corrigibility & safe interruptibility (2016→).**  
   **Adopt/Adapt.** Work on safe interruption and “off‑switch” incentives argues that capable systems should remain *stoppable* and should not be rewarded for resisting oversight (Orseau & Armstrong, 2016; Hadfield‑Menell et al., 2017). E.16 adapts this into canonical **PauseAutonomy / ResumeAutonomy** SpeechActs plus **SoD** and *hard* gating on depletion.

2. **AI safety as concrete operational hazards (2016→).**  
   **Adopt.** “Concrete Problems in AI Safety” pushes instrumentation and testable safety constraints over informal assurances (Amodei et al., 2016). E.16 mirrors this by turning “autonomy” into a **budget + ledger + guards** contract that can be benchmarked and audited.

3. **SRE error budgets & “stop the line” operations (2016→).**  
   **Adopt/Adapt.** Error‑budget practice treats reliability as a measurable envelope that gates risky change when depleted (Beyer et al., *Site Reliability Engineering*, 2016; Höller et al., *The Site Reliability Workbook*, 2018). E.16 adapts the idea into `risk_bands` and depletion behavior that blocks autonomy‑gated steps until governed resume.

4. **Risk management frameworks for AI systems (2023→).**  
   **Adopt/Adapt.** Contemporary risk frameworks emphasize governance, continuous measurement, and traceable controls (NIST AI RMF 1.0, 2023; ISO/IEC 23894, 2023). E.16 adapts these into **UTS publication** + **Work‑anchored ledger evidence** for parity and audit.

5. **Policy‑as‑code and provenance gating (2019→).**  
   **Adopt.** Modern supply‑chain integrity systems emphasize *policy‑checked actions with verifiable provenance* (in‑toto, 2019→; SLSA, 2021→). E.16 echoes the same principle for autonomy: **no autonomy‑gated enactment without passing declared guards and emitting ledger evidence** (without importing any specific tooling).

6. **Scaling laws & the Bitter Lesson (2019→).**  
   **Adapt/Reject.** Empirical scaling work and the Bitter Lesson motivate considering compute‑heavy search when returns are monotonic (Sutton, 2019; Kaplan et al., 2020). E.16 adapts this into an **optional** ScaleLensPolicy (E.16‑S7) constrained by the *same* budgets and guards, and **rejects** any interpretation that lets “scale” bypass safety gates.

### E.16:7.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Autonomy-by-label** | “Autonomous” is claimed but there is no `AutonomyBudgetDecl` or ledger | Autonomy becomes opaque; cannot be audited or compared | Require **E.16‑S1/S3**; reject publication without `AutonomyBudgetDeclRef` + version |
| **Soft gates** | Budget/guards only warn; enactment proceeds anyway | Violates Safety and SoD; makes budgets non-enforceable | Make Green‑Gate **blocking** on Core surface (**E.16‑S2**) |
| **Self‑override** | Same RoleAssignment consumes the budget and calls Resume/Narrow | Conflict of interest; SoD collapse | Enforce `⊥` between consumer and overrider (**E.16‑S4**) |
| **Budget bypass via “scale”** | Scaling preference weakens guards or ignores caps | Undermines declared limits; breaks comparability | In ScaleLensPolicy, **guards/SoD must remain non‑weakened** (**E.16‑S7**) |
| **Untyped quotas** | Tokens/caps are recorded without units, or units are mixed | Ledger becomes non-comparable; audits become meaningless | Type budgets and deltas via **MM‑CHR (C.16)**; keep unitful rates/quotas |
| **Ledger-as-logging** | Logs exist but are not Work‑anchored (no workId/budgetId/version/pins) | Evidence is non-portable; cannot support parity/refresh | Require `AutonomyLedgerEntry` attached to `U.Work` with ids, versions, and edition pins |

### E.16:8 - Rationale & E‑/F‑/G‑links

* **E.8** — follows the pattern template (Context → Problem → Forces → Solution → Grounding → CC → Consequences).
* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, no “validity/process/actor/agent‑as‑noun” language; new lexical rule **L‑AUTO** added in edits below.
* **Mint/reuse authority (policy-ids).** Mint/reuse authority is expressed via **F.8:8.1** (`PolicyIdRef`: `PolicySpecRef` + `MintDecisionRef?`) and explicit **GateCrossing** checks (**E.18**) evaluated by the active **GateProfile/GateFit** (**A.21**); no tier ladder is required.
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** Role Assignment & Enactment (Green‑Gate), **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.

### E.16:9 - Mini conformance checklist (cross‑E–F; author’s quick use)

1. **Declare** `AutonomyBudgetDecl` (scope, budgets, AdmissibilityConditionsId, overrides).
2. **Gate** steps with `requiresAutonomyBudget`.
3. **Emit** an `AutonomyLedgerEntry` for each admitted Work.
4. **Enforce SoD** on override SpeechActs; **block on depletion**.
5. **Publish** UTS autonomy fields for any autonomy‑bearing Role/Method/Service.

*(These five are sufficient for a working test harness in Part F.)*

### E.16:End

## E.17.0 - `U.MultiViewDescribing — Viewpoints, Views & Correspondences`

> **Tech‑name:** `U.MultiViewDescribing`
> **Plain‑name:** multi‑view describing (viewpoints, views, correspondence for families of descriptions/specifications)

**Status & placement.** Part E (Describing & Publication). Normative architectural pattern.
**Builds on:** C.2.1 `U.EpistemeSlotGraph` (DescribedEntity/Viewpoint/View slots), A.6.2 `U.EffectFreeEpistemicMorphing`, A.6.3 `U.EpistemicViewing`, A.6.4 `U.EpistemicRetargeting`, A.7 (Strict Distinction; I/D/S vs Surface), E.10.D1 (Context), E.10.D2 (I/D/S discipline).
**Used by:** E.17 (MVPK — publication as a specialisation of multi‑view describing for morphisms), E.17.1 `U.ViewpointBundleLibrary`, E.17.2 `TEVB`, E.18:5.12 (E.TGA engineering viewpoint families), domain‑specific description schemes (architecture, safety cases, governance, research). 

**Guard (lexical).**

* `U.Viewpoint` is the ValueKind of `ViewpointSlot` and denotes **intensional viewpoint specs**, not surfaces or carriers. 
* `U.View` is an alias of `U.EpistemeView`, i.e. an **episteme‑level view**, not a document or file. Views are epistemes; Surfaces are carriers in L‑SURF.
* `ViewFamilyId` is a lexical tag for **families of viewpoints** (e.g. TEVB), never for view kinds, MVPK `U.View`/`U.ViewFamily(-)` bundles or Surface kinds. MVPK face kinds remain `{PlainView, TechCard, InteropCard, AssuranceLane}`. 

### E.17.0:1 - Problem frame  *(informative)*

Complex systems (social‑technical, cyber‑physical, organisational) are routinely described from **many perspectives**:

* functional vs structural vs deployment vs behavioural views,
* safety vs performance vs cost vs governance views,
* formal specs vs operational runbooks vs regulatory dossiers.

Post‑2015 MBSE and architecture practice emphasise **viewpoints and views** (ISO 42010, SysML v2), and contemporary model‑based toolchains treat views as **queries or projections over shared models** rather than independent documents.

In FPF terms:

* the things we talk about — systems, methods, services, epistemes — are `U.Entity`/`U.Holon` values in `DescribedEntitySlot`; 
* descriptions and specifications of those things are `U.Episteme` instances (`…Description` / `…Spec`) with a **DescriptionContext** = `⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`; 
* episteme‑level views are `U.View` (`U.EpistemeView`) that slice ClaimGraphs under specific viewpoints and representation schemes. 

What we lack without this pattern is a **universal way to organise families of descriptions/specifications under multiple viewpoints** — for any entity‑of‑interest, not only for architecture, and without collapsing “view” into “document” or “diagram”.

### E.17.0:2 - Problem  *(informative, but sharp)*

Without `U.MultiViewDescribing`:

1. **Viewpoints, views, and surfaces collapse.**
   In practice, “architecture view”, “diagram”, “spec”, and “published deck” are used interchangeably. This:

   * confuses *episteme* (`U.View`) with *carrier* (`U.Surface`),
   * hides which **concerns and stakeholders** a description is written for,
   * makes it impossible to check whether a given description family is “complete enough” for a chosen viewpoint library.

2. **Descriptions float without viewpoints.**
   Legacy I/D/S discipline distinguishes Intension vs Description vs Spec, but does not, on its own, forbid “view‑from‑nowhere” descriptions (no declared viewpoint). That contradicts the pragmatic stance encoded in C.2.1: **no episteme without concerns**.

3. **Each domain reinvents multi‑view semantics.**
   Architecture, safety cases, governance frameworks, and research workflows all use local notions of “view”, “viewpoint”, and “consistency between views”. Without a shared pattern:

   * E.TGA, MVPK, and discipline packs introduce their own “view” laws, duplicating work;
   * cross‑domain reasoning (e.g. mapping a safety view to an architecture view) becomes ad‑hoc;
   * we cannot give a single formal story for consistency, correspondence, and EpistemicViewing across families of descriptions.

4. **No place to attach correspondence.**
   ISO 42010‑style *correspondences* and modern BX/consistency relations have nowhere canonical to live. We need a **CorrespondenceModel over families of D/S epistemes** that integrates with `U.EpistemicViewing`/`U.EpistemicRetargeting` and C.2.1’s slot graph.

### E.17.0:3 - Forces  *(informative)*

| Force                                  | Tension                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**      | One pattern should handle engineering, safety, governance, research, etc. ↔ domain communities expect their own jargon (architecture description, safety case, dossier…).              |
| **Viewpoint locality vs reuse**        | Viewpoints must be local to families of descriptions (`EoIClass`, Context) ↔ we want reusable **viewpoint bundles** (libraries) across projects and domains.                           |
| **I/D/S strictness vs pragmatics**     | Intension ≠ Episteme; D/S are epistemes with DescriptionContext ↔ engineers think in “views over a system”, not in pure I/D/S algebra.                                                 |
| **Slot discipline vs approachability** | C.2.1/A.6.5 give a clean SlotKind/ValueKind/RefKind discipline ↔ authors want to talk about “functional view” and “safety view” without carrying all slot jargon in didactic material. |
| **Epistemic vs surface layers**        | Views (epistemes) must be clearly separated from PublicationSurface and carriers ↔ authors often conflate “viewpoint”, “view”, and “document”.                                         |
| **Consistency vs incremental change**  | We want strong correspondence between views ↔ views evolve asynchronously; partial inconsistency must be representable and repairable (BX‑style).                                      |

### E.17.0:4 - Solution — `U.MultiViewDescribing` as the universal multi‑view scaffold  *(normative core)*

#### E.17.0:4.1 - Overview

`U.MultiViewDescribing` organises **families of descriptions/specifications** for a shared entity‑of‑interest into a multi‑view structure with:

* **explicit viewpoints** (`U.Viewpoint`) as intensional specs of stakeholders, concerns, allowed D/S kinds, and conformance rules; 
* **episteme‑level views** (`U.View = U.EpistemeView`) as view‑epistemes over those descriptions/specs; 
* a **CorrespondenceModel** capturing correspondences between D/S and their views across viewpoints.

The pattern is **parameterised by a class of described entities**:

> **Parameter:** `EoIClass ⊑ U.Entity` — the class of entities‑of‑interest
> (typical species: `U.Holon` for engineering holons, `U.Morphism` for morphism publication, `U.Episteme` for meta‑describing epistemes).

All members of a `U.MultiViewDescribing[EoIClass]` family share:

* `DescribedEntitySlot` value in that `EoIClass`, and
* a `BoundedContextRef` (E.10.D1) forming a **DescriptionScope** together with the entity. 

Informally:

* Fix an entity `T ∈ EoIClass` and a bounded context `C`.
* The **multi‑view family** for `<T,C>` consists of a set of `…Description` / `…Spec` epistemes, each under a declared viewpoint, plus their `U.View` views, together with a correspondence model relating them.

#### E.17.0:4.2 - Core constructs

##### E.17.0:4.2.1 - `EoIClass` and DescriptionScope

1. **EoIClass.**
   A `U.MultiViewDescribing` instance declares an `EoIClass ⊑ U.Entity` that acts as a **species‑level constraint** on the ValueKind of `DescribedEntitySlot`.

   * In engineering species (TEVB) this is typically `U.Holon` restricted to `U.System` or `U.Episteme`. 
   * In MVPK, `EoIClass = U.Morphism`. 

2. **DescriptionScope (informal).**
   For a fixed `T ∈ EoIClass` and `C : U.BoundedContext`, the **DescriptionScope** `Scope(T,C)` is the notional scope under which:

   * all descriptions/specifications have `DescribedEntityRef = T` and `BoundedContextRef = C` in their DescriptionContext; 
   * all views (`U.View`) attached to this family preserve that `DescribedEntityRef` and `BoundedContextRef` (for D/S views).

   Formal USM treatment of `U.DescriptionScope` is fixed in E.10/L‑SURF; here we only rely on the intuition “**we are describing this thing, in this context**”.

##### E.17.0:4.2.2 - `U.Viewpoint` (intensional viewpoint spec)

`U.Viewpoint` is already introduced in C.2.1 as the ValueKind of `ViewpointSlot`; E.17.0 fixes its **internal structure** for describing families. 

**Definition (normative, intensional).**
A `U.Viewpoint` is an intensional specification:

* `EoIClassSpec ⊑ U.Entity` — the class of entities this viewpoint is defined for (must be compatible with the family’s `EoIClass`);
* `StakeholderFamilies : FinSet(U.RoleEnactor)` — stakeholder / RoleEnactor families the viewpoint speaks for (e.g. “safety engineers”, “operations teams”).
* `Concerns : FinSet(U.Concern)` — concern set (qualities, risks, obligations) that matter under this viewpoint.
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindId)` — which D/S episteme kinds are admissible as **primary descriptions** and as **derived views** under this viewpoint (e.g. system‑level behaviour description, test harness spec, safety case, CG‑Spec slice).
* `ConformanceRules` — a structured bundle of rules/tests describing when a D/S episteme or view **conforms** to the viewpoint, including:

  * minimal content requirements (e.g. “must cover all safety‑critical functions”),
  * admissible `U.EpistemicViewing` pipelines to derive views from base descriptions,
  * allowed degrees of incompleteness and evidence requirements (link to GateProfiles/`OperationalGate(profile)` checks and Part F harnesses).

**Slot alignment.**

* `ViewpointSlot` has ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`; episteme fields are named `viewpointRef : U.ViewpointRef?`. 
* For D/S epistemes in a `U.MultiViewDescribing` family, `viewpointRef` is **mandatory** as part of `DescriptionContext`.

##### E.17.0:4.2.3 - `U.View` (episteme‑level views)

`U.View` is an alias for `U.EpistemeView`, a species of `U.Episteme` whose kind includes:

* `ClaimGraphSlot` (often a sliced or projected ClaimGraph),
* `DescribedEntitySlot`,
* `ViewpointSlot`,
* `ReferenceSchemeSlot` (and usually a `RepresentationSchemeSlot` in C.2.1+).

Normatively:

* A `U.View` in `U.MultiViewDescribing` is obtained via a `U.EpistemicViewing` morphism from some base D/S episteme in the family (see 4.3). It **shares the same `describedEntityRef`** and usually the same `BoundedContextRef`.
* `ViewSlot` is reserved for **references to such views** in meta‑structures (e.g. correspondence models, MVPK view families), never for carriers.

##### E.17.0:4.2.4 - `U.CorrespondenceModel` (view–view correspondence)

`U.CorrespondenceModel` is an episteme (typically a `U.EpistemeCard`) whose ClaimGraph expresses **correspondence relations between D/S epistemes and/or views** within a DescriptionScope:

* cross‑viewpoint correspondences (e.g. “this safety requirement is realised by this design element”),
* structural/behavioural consistency conditions (BX‑style consistency relations),
* change‑impact links (which views must be revisited when some view changes).

`CorrespondenceModel` is **used, but not defined, by A.6.3**: species of `U.CorrespondenceEpistemicViewing` reference it when computing views that depend on multiple epistemes or representation regimes.

#### E.17.0:4.3 - Multi‑view families and their laws (MVD‑0…MVD‑7)  *(normative)*

We now fix the laws that any `U.MultiViewDescribing[EoIClass]` instance must satisfy.

##### E.17.0:4.3.0 - MVD‑0 - Family objects

For a fixed `EoIClass` and bounded context `C`, a **multi‑view family** for an entity `T ∈ EoIClass` consists of:

* a (finite) set `D_S(T,C)` of D/S epistemes such that for each `E ∈ D_S(T,C)`:

  * `E : U.Episteme` of some kind in `AllowedEpistemeKinds` of its viewpoint,
  * `subjectRef(E)` decodes to `DescriptionContext(E) = ⟨DescribedEntityRef = T, BoundedContextRef = C, ViewpointRef(E)⟩`,
  * `viewpointRef(E)` lies in the family’s viewpoint set `Σ ⊆ FinSet(U.Viewpoint)`;
* a set `Views(T,C) ⊆ U.View` of view‑epistemes over those D/S epistemes, obtained by declared `U.EpistemicViewing` species (see MVD‑3);
* zero or more `U.CorrespondenceModel` epistemes over `{D_S(T,C), Views(T,C)}`.

Families are **scoped**: the same entity in a different `U.BoundedContext` belongs to a different family.

##### E.17.0:4.3.1 - MVD‑1 - Viewpoint locality and totality for D/S

For any multi‑view family:

1. **Viewpoint‑totality for D/S.**
   Each D/S episteme in `D_S(T,C)` **MUST** have a `viewpointRef` either:

   * explicitly populated, or
   * deterministically derived from a `U.ViewpointBundle` the family declares (see E.17.1).

   There are no “viewpoint‑free” D/S epistemes inside a `U.MultiViewDescribing` family.

2. **Viewpoint locality.**
   `ViewpointRef` values for `D_S(T,C)` must belong to a **finite viewpoint set `Σ`** declared for the family (locally or via a bundle). Cross‑family reuse happens **via bundles and Bridges**, not by silently sharing viewpoints across unrelated scopes.

3. **DescriptionContext alignment.**
   `DescriptionContext(E)` for any D/S episteme in the family must use the **same `DescribedEntityRef` and `BoundedContextRef`** as the family; any change of described entity or context is **outside this family** and must be expressed via `U.EpistemicRetargeting` and/or Context Bridges.

#### E.17.0:4.3.2 - MVD‑2 - Views are EpistemicViewing results

For any `V ∈ Views(T,C)`:

1. There exists a base episteme `E ∈ D_S(T,C)` and a morphism `v : E → V` such that:

   * `v` is a species of `U.EpistemicViewing`, i.e. an **effect‑free, describedEntity‑preserving** episteme morphism;
   * `describedEntityRef(V) = describedEntityRef(E) = T`,
   * `BoundedContextRef(V) = BoundedContextRef(E) = C`,
   * `viewpointRef(V)` is either:

     * the same as `viewpointRef(E)` (internal normalisation), or
     * a viewpoint in the same family `Σ`, with the change recorded in the family’s `CorrespondenceModel` (see MVD‑4).

2. No view may be introduced “out of thin air”: every `U.View` in the family is traceable to at least one D/S episteme (or a finite diagram thereof) via a **documented EpistemicViewing pipeline**.

3. Views **do not introduce new intensional commitments** about `T` beyond what is licensed by EFEM & EpistemicViewing laws (no new atomic claims about the same described entity). Strengthening Intension requires new D/S under A.7/E.10.D2, not a view.

#### E.17.0:4.3.3 - MVD‑3 - Applicability profiles for viewings

Any EpistemicViewing species used inside `U.MultiViewDescribing` **MUST**:

* declare an Applicability profile as per EV‑6: permitted `EoIClass`, grounding, viewpoint ranges, and representation schemes; 
* for D/S epistemes in a family:

  * **preserve** `DescribedEntityRef` and `BoundedContextRef` of `DescriptionContext`,
  * either preserve `ViewpointRef` or change it **within the family’s viewpoint bundle**, with constraints recorded in `CorrespondenceModel`,
  * never widen ClaimScope beyond EFEM/EpistemicViewing allowances.

Any change of described entity (even “small”, e.g. subsystem→system) must be expressed via `U.EpistemicRetargeting` and is **not** a MultiViewDescribing view refinement.

#### E.17.0:4.3.4 - MVD‑4 - CorrespondenceModel as the home of cross‑view correspondences

When views or D/S epistemes under different viewpoints are meant to be **kept in correspondence** (in ISO 42010 or BX sense), the family **SHALL**:

1. Provide a `U.CorrespondenceModel` episteme whose `ClaimGraph` captures correspondences and consistency relations over `{D_S(T,C), Views(T,C)}`.

2. Ensure that any `U.CorrespondenceEpistemicViewing` that depends on multiple epistemes or representation schemes:

   * references that `CorrespondenceModel`, and
   * publishes witnesses (proof objects, trace links) that make diagrams commute up to declared isomorphism (oplax naturality allowed).

3. Treat temporary inconsistency explicitly: there may be states where some correspondences are violated; this is represented as **facts in the correspondence ClaimGraph**, not as hidden weakening of viewing laws.

#### E.17.0:4.3.5 - MVD‑5 - Separation from publication (MVPK)

`U.MultiViewDescribing` is purely **epistemic**:

* D/S epistemes and views live entirely in Ep‑space (`U.Episteme`);
* it does **not** define PublicationSurface, carriers or rendering;
* MVPK (E.17) sits **on top**:

  * taking morphisms and/or D/S epistemes as input,
  * using `U.EpistemicViewing` plus publication‑specific viewpoints,
  * emitting `U.View` instances that then get attached to Surfaces via L‑SURF.

MultiViewDescribing therefore **does not re‑define I→D/D→S** (`Describe_ID`, `Specify_DS`) and does not introduce any Work on carriers; those remain in A.7/E.10.D2 and E.17.

#### E.17.0:4.3.6 - MVD‑6 - I/D/S alignment

For any `U.MultiViewDescribing` instance:

1. Every `…Description` and `…Spec` episteme in the family must satisfy E.10.D2:

   * be an episteme with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
   * be linked to a unique Intension via `isDescriptionOf` / `isSpecOf` with the additional `ViewpointRef` parameter.

2. Viewings and correspondence operations **must not**:

   * collapse Intension into episteme,
   * confuse D/S with publication surfaces,
   * reinterpret described entity without going through A.6.4 retargeting.

#### E.17.0:4.3.7 - MVD‑7 - Slot discipline

All constructs in this pattern **SHALL** respect `U.RelationSlotDiscipline`:

* SlotKinds (`DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`) and their ValueKinds/RefKinds follow A.6.5 and C.2.1.
* `*Slot` suffix is reserved for SlotKinds; `*Ref` for RefKinds/fields, never for Kinds or objects. 
* MultiViewDescribing patterns **must not** invent parallel slot disciplines for “roles in relations”; they reuse SlotKind as the notion of position.

### E.17.0:5 - Archetypal grounding  *(informative)*

1. **Engineering holon (TEVB).** 
   * `EoIClass = U.Holon` (restricted to `U.System`/`U.Episteme`).
   * TEVB (E.17.2) supplies a viewpoint bundle with canonical engineering viewpoints: Functional, Structural, Role‑Enactor, Module‑Interface, etc.
   * For a particular system `S` in context `C`, D/S epistemes include functional descriptions, structural designs, role‑enactment models, and interface specs.
   * Views derived via EpistemicViewing include sliced safety views, performance‑focused views, and minimal runbooks.
   * `CorrespondenceModel` records how functional elements are realised structurally, where hazards map to components, etc.

2. **Morphism publication (MVPK).**
   * `EoIClass = U.Morphism`.
   * D/S epistemes capture the semantic characterisation of morphisms (pre‑/post‑conditions, CG‑Specs, CHR pins).
   * Viewpoints are publication‑oriented (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`); views are MVPK faces over those morphisms.
   * CorrespondenceModel states how the same morphism appears as a simple narrative, a typed card with units, an interoperability card, and an assurance lane with evidence bindings — all without new claims.

3. **Safety case vs architecture vs operations.**
   * `EoIClass = U.Holon`.
   * Viewpoints: SafetyCase, Architecture, Operations.
   * Families tie together safety requirements, architectural structures, and operational procedures for the same plant `P` in context `C`.
   * Views: a safety‑focused slice of the architecture description, an operational runbook annotated with safety invariants, etc.
   * CorrespondenceModel expresses coverage and consistency between these views, enabling BX‑style repair when one side changes.

### E.17.0:6 - Conformance checklist (author’s quick use)  *(normative)*

When defining a new `U.MultiViewDescribing` species or using it in a discipline pack:

1. **Declare the EoIClass.**
   *Explicitly state `EoIClass ⊑ U.Entity` and ensure all families restrict `DescribedEntitySlot` accordingly.*

2. **Define the viewpoint set Σ.**
   *List `U.Viewpoint` instances (possibly via a `U.ViewpointBundle`) with stakeholders, concerns, allowed EpistemeKinds, and conformance rules.*

3. **Require DescriptionContext for D/S.**
   *Ensure every `…Description`/`…Spec` episteme in the family has `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` and that `ViewpointRef ∈ Σ`.*

4. **Specify admissible EpistemicViewing species.**
   *List the `U.EpistemicViewing` profiles used to derive views; declare their Applicability profiles and assert they are describedEntity‑preserving (EV‑6).*

5. **Attach CorrespondenceModel where needed.**
   *Whenever cross‑view consistency matters, introduce a `U.CorrespondenceModel` episteme and reference it from any `U.CorrespondenceEpistemicViewing`.*

6. **Separate describing from publication.**
   *Check that pattern text does not treat I→D/D→S as “publication”, and that any talk of Surfaces/carriers is clearly delegated to MVPK/L‑SURF.*

7. **Respect SlotKind/ValueKind/RefKind discipline.**
   *Use `*Slot` only for SlotKinds, `*Ref` only for RefKinds/fields; avoid `Subject`/`Object` roots in episteme types; use `DescribedEntitySlot` and `viewpointRef` instead.*

### E.17.0:7 - Consequences  *(informative)*

* **Unified multi‑view story across domains.**
  Engineering descriptions, safety cases, governance dossiers, research artefacts — all become instances of the same multi‑view pattern, enabling coherent tooling and education.

* **Explicit, testable viewpoints.**
  Viewpoints move from vague labels (“architecture view”) to first‑class objects (`U.Viewpoint`) with stakeholder families, concerns, allowed D/S kinds, and conformance rules. This allows `OperationalGate(profile)` checks and better review practices.

* **Views as disciplined projections, not new documents.**
  `U.View` is an episteme generated by viewings, not a free‑floating PowerPoint. This constrains what tools are allowed to do when “generating views”, and prevents silent strengthening of commitments.

* **Correspondence as a first‑class citizen.**
  Consistency and traceability between views are expressed via ClaimGraphs in `U.CorrespondenceModel`, not as scattered hyperlinks or spreadsheet columns.

* **Clean separation of describing vs publishing.**
  `U.MultiViewDescribing` ends the long‑standing conflation between describing (I→D→S) and publication (D/S→Surface). MVPK becomes a clean specialisation on top, not a second I/D/S discipline.

* **Slot‑level interoperability.**
  C.2.1/A.6.5 slot discipline applies uniformly; new domains can introduce viewpoint bundles and multi‑view families without inventing new ontologies for “view positions” or “roles in relations”.

### E.17.0:8 - Rationale & SoTA‑echoing  *(informative)*

* **ISO 42010 and viewpoint libraries.**
  ISO 42010 distinguished *viewpoints* (stakeholders + concerns + conventions) from *views* (descriptions under those viewpoints) and introduced viewpoint libraries. `U.MultiViewDescribing` generalises this beyond “architecture descriptions” to **any descriptions/specifications**, with `EoIClass` parameter and explicit viewpoint bundles used by TEVB and MVPK. 

* **MBSE & SysML v2 views‑as‑queries.**
  Modern MBSE treats views as **queries over shared models** with controlled rendering. That aligns with `U.EpistemicViewing` as a pure, describedEntity‑preserving morphism, and with `U.View` as an episteme view derived from D/S under a viewpoint.

* **BX / model synchronisation.**
  Bidirectional transformations literature treats consistency relations and repair as first‑class. `U.CorrespondenceModel` and `U.CorrespondenceEpistemicViewing` provide an FPF‑native home for such relations, ensuring that consistency rules live in ClaimGraphs and respect episteme morphism laws, rather than being buried in tool code. 

* **Optics and displayed categories.**
  With C.2.1 and A.6.3, epistemes form a category fibred over described entities; viewings act like optics over the episteme slot graph. `U.MultiViewDescribing` is the **displayed‑category‑like** organisation of families indexed by `DescribedEntitySlot` and `ViewpointSlot`, making later categorical reasoning (e.g. structured cospans for view composition) straightforward.

* **Hybrid symbolic/latent representations.**
  By treating `U.RepresentationScheme` and `U.RepresentationOperation` as episteme components, families can mix symbolic specs, diagrams, code, and latent representations (e.g. LLM‑based summaries) while staying within the same multi‑view discipline and EpistemicViewing laws.

### E.17.0:9 - Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotGraph`.**
  Uses `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` as the structural backbone for descriptions, views, and correspondence.

* **Builds on A.6.2–A.6.4.**
  Families rely on `U.EffectFreeEpistemicMorphing` for view‑producing morphisms, `U.EpistemicViewing` for describedEntity‑preserving views, and `U.EpistemicRetargeting` for moves that change the described entity (outside a given family).

* **Constrains E.17 (MVPK).**
  MVPK is a **publication‑specialised MultiViewDescribing for morphisms**: its viewpoints are publication viewpoints; its ViewFamily is a special case of `Views(T,C)` with `T` a morphism; its laws must respect MVD‑0…MVD‑7.

* **Constrains E.17.1 / E.17.2.**
  `U.ViewpointBundleLibrary` and TEVB provide concrete viewpoint bundles populating `Σ` for particular `EoIClass` (e.g. engineering holons), but they must treat viewpoints as `U.Viewpoint` values in `ViewpointSlot`, not as ad‑hoc tags. 

* **Coordinates with E.10.D2 (I/D/S) and E.10 LEX‑BUNDLE.**
  Ensures every D/S episteme in a family has a DescriptionContext, keeps “Describe/Specify” distinct from “Publish”, and respects lexical guards around `View`, `Viewpoint`, `Surface`, `ViewFamilyId`, `*Slot`, `*Ref`.

* **Coordinates with B.5.* / F‑cluster.**
  Viewpoints’ stakeholder families and concerns link naturally with RoleEnactment (B.5.\*) and Part F role descriptions, assignments, harnesses — without overloading `U.Role` as a coordinate in I/D/S or episteme slots.

### E.17.0:End

## E.17.1 - `U.ViewpointBundleLibrary — Reusable Viewpoint Bundles`

> **Tech‑name:** `U.ViewpointBundleLibrary`
> **Plain‑name:** viewpoint bundle library (reusable viewpoint families)

**Status & placement.** Part E (Describing & Publication). Normative architectural pattern.

**Builds on:**
A.6.2–A.6.4 (Episteme morphism classes),
A.6.5 `U.RelationSlotDiscipline` (SlotKind/ValueKind/RefKind discipline),
A.7 (Strict Distinction; I/D/S vs Surface),
E.7 (Archetypal Grounding),
E.10 (LEX‑BUNDLE, especially naming discipline for `ViewFamilyId`),
E.10.D1/D2 (Context and I/D/S discipline),
E.17.0 `U.MultiViewDescribing`.

**Used by:**
E.17.2 (TEVB — Typical Engineering Viewpoints Bundle),
E.18:5.12 (E.TGA engineering viewpoint families),
future domain‑specific viewpoint packs (architecture, governance, safety, research).

**Guard (lexical & ontological).**

* A **viewpoint bundle** is a family of `U.Viewpoint` values (intensional specs) plus metadata; it is **not** a collection of `U.View`, `PublicationSurface`, or files.
* `ViewFamilyId` is a lexical tag that names a **viewpoint family** (bundle), never:
  * a `U.View` kind,
  * an MVPK face/surface kind,
  * nor a file/folder label in L‑SURF.
* `EngineeringVPId` / `PublicationVPId` remain separate (E.18:5.12, E.17); E.17.1 does **not** collapse engineering and publication viewpoints into one id.
* Bundles are **intensional catalogue objects**: they specify reusable viewpoint families that `U.MultiViewDescribing` instances may import; they do not define new episteme kinds or surface kinds.

### E.17.1:1 - Problem frame  *(informative)*

`U.MultiViewDescribing` organises descriptions/specifications of an entity‑of‑interest into multi‑view families with explicit viewpoints and correspondence. In practice:
* engineering teams talk about “functional / procedural / structural / module‑interface” views of a system;
* governance teams talk about “risk / compliance / operations” views of a service;
* research teams talk about “theory / experiment / inference / limitations” views of a method.

Across organisations and projects, these **viewpoint families repeat** with only minor variations. ISO 42010 already recognises *viewpoint libraries* as a way to capture such recurring families for architecture descriptions; MBSE stacks and SysML v2 profiles do the same for model views.

FPF needs a **uniform way to define and reuse such viewpoint families**:
* so that `U.MultiViewDescribing` can import them instead of redefining Σ from scratch;
* so that E.TGA and MVPK can refer to the same engineering viewpoint families via stable ids;
* so that authoring guidance (E.8/E.12) and lexical discipline (E.10) can attach to named families rather than ad‑hoc sets.

### E.17.1:2 - Problem  *(informative)*

Without a dedicated pattern for viewpoint bundle libraries:

1. **Each domain bakes its own “viewpoint sets”.**
   E.TGA, MVPK, safety‑case disciplines, and governance packs tend to introduce local notions such as “engineering views”, “assurance views”, “governance decks” without a shared representation. Viewpoints drift, and cross‑domain mapping becomes opaque.

2. **Viewpoint identity is unstable.**
   A team may call something “functional view” in one project and “capability view” in another, even though the underlying concerns, stakeholders, and conformance rules are identical. The same `U.Viewpoint` is re‑invented and slightly renamed, making long‑term consistency and automation harder.

3. **MultiViewDescribing cannot easily reuse families.**
   `U.MultiViewDescribing` allows an arbitrary finite set of viewpoints Σ for each `<T,C>` (entity, context). Without a standard way to say “Σ is the TEVB engineering family” or “Σ is the governance‑risk bundle”, each family has to list viewpoints explicitly and locally.

4. **ISO 42010 viewpoint libraries remain external.**
   There is no canonical place in FPF where ISO‑style viewpoint libraries (for architecture descriptions) can be represented as first‑class objects and aligned with FPF’s `U.Viewpoint`, I/D/S discipline, and episteme morphisms.

5. **Lexical aliases leak into semantics.**
   Names like “Functional”, “SafetyCase”, or “Regulatory” may be used both as:

   * intensional viewpoint specs; and
   * ad‑hoc labels on documents, files or MVPK faces.
     Without a clear lexical discipline, this causes confusion about what exactly is being reused.

E.17.1 addresses these issues by introducing `U.ViewpointBundleLibrary` as the place where **reusable viewpoint families** are defined, named, and versioned.

### E.17.1:3 - Forces  *(informative)*

| Force                                     | Tension                                                                                                                                                                       |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reuse vs local fit**                    | Organisations want shared viewpoint families (engineering, safety, governance) ↔ projects need to tweak or subset them for specific contexts and maturity levels.             |
| **Domain idioms vs neutral core**         | Domains carry their own jargon (architecture, safety case, regulatory dossier) ↔ FPF needs a neutral `U.Viewpoint` core to support cross‑domain reasoning and tooling.        |
| **Stability vs evolution**                | Viewpoint families must be stable enough to support long‑term automation and training ↔ they must evolve as practices and standards evolve.                                   |
| **Intensional vs artefact layers**        | Viewpoint families talk about concerns and conformance rules ↔ teams routinely attach the same name to concrete documents or MVPK faces.                                      |
| **Engineering vs publication viewpoints** | Engineering viewpoints govern how a holon is described ↔ publication viewpoints govern how those descriptions are exposed as surfaces; we need both, without collapsing them. |
| **Library size vs cognitive load**        | Rich libraries with many viewpoint families increase flexibility ↔ authors must still be able to choose and understand a small subset in each project.                        |

### E.17.1:4 - Solution — `U.ViewpointBundleLibrary`  *(normative core)*

#### E.17.1:4.1 - Overview

`U.ViewpointBundleLibrary` is the **architectural home for reusable viewpoint families**.

* A **viewpoint library** is a collection of **viewpoint bundles**; each bundle names and packages a finite family of `U.Viewpoint` values that are intended to be reused together.
* Each **viewpoint bundle**:

  * is identified by a `ViewFamilyId` lexical tag;
  * constrains an `EoIClass ⊑ U.Entity` for which its viewpoints are valid;
  * enumerates a finite set Σ of `U.Viewpoint` definitions;
  * may carry archetypal grounding cards (E.7) and alignment notes (e.g., ISO 42010 mappings).

`U.MultiViewDescribing[EoIClass]` then uses such bundles as **providers of Σ** for families of descriptions/specifications:

* for a fixed entity `T ∈ EoIClass` and bounded context `C`, a `U.MultiViewDescribing` family may declare:

  * that its viewpoint set Σ is **imported from** a specific `ViewFamilyId`, possibly with a finite subset selection; or
  * that Σ is locally defined (no bundle) — still allowed, but less reusable.

TEVB (E.17.2) and E.TGA E.18:5.12 are species of this pattern for engineering holons.

#### E.17.1:4.2 - Core constructs

##### E.17.1:4.2.1 - `U.ViewpointBundleLibrary` (library object)

**Tech:** `U.ViewpointBundleLibrary` (kernel/species type).
**Plain:** viewpoint library.

A `U.ViewpointBundleLibrary` is a **catalogue of viewpoint bundles**, with at least:

* `libraryId : LibraryId` — lexical identifier of the library (e.g. `FPF.Core.Viewpoints`, `OrgX.EngineeringViewpoints`).
* `bundles : FinSet(U.ViewpointBundle)` — finite or countable set of bundles it provides.
* `editionId : EditionId` — edition of the library, subject to the usual LEX‑AUTH / LAT discipline (E.15).
* optional `scopeTags` and governance metadata (owner, change‑control).

**Normative constraints.**

1. Within a given `U.ViewpointBundleLibrary` edition, `ViewFamilyId` values **SHALL be unique**.
2. Libraries **SHALL NOT** define new kernel episteme kinds or surface kinds; they only package `U.Viewpoint` values and metadata.
3. Libraries **MAY** be specialised:

   * a core FPF library (e.g. TEVB, generic governance bundles);
   * organisational libraries extending or subsetting core bundles.

##### E.17.1:4.2.2 - `U.ViewpointBundle` and `ViewFamilyId` (viewpoint family)

**Tech:** `U.ViewpointBundle` (species type), `ViewFamilyId` (lexical id).
**Plain:** viewpoint family, bundle of viewpoints.

A `U.ViewpointBundle` is a **family of compatible viewpoints** packaged for reuse. Minimal structure:

* `viewFamilyId : ViewFamilyId` — lexical id for the family (e.g. `VF.TEVB.ENG`, `VF.GovRisk`, `VF.ResearchMethod`).
* `EoIClassSpec ⊑ U.Entity` — class of entities this family is meant for (must be compatible with each viewpoint’s `EoIClassSpec`).
* `viewpoints : FinSet(U.Viewpoint)` — finite, non‑empty set of `U.Viewpoint` values (typically referenced via `U.ViewpointRef` in episteme cards).
* optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)` — grounding cards per viewpoint (E.7).
* optional `AlignmentNotes` — e.g., ISO 42010 mappings, domain standard references.

**Normative constraints.**

VBL‑1. **EoIClass compatibility.**
For every `vp ∈ viewpoints`:

* `vp` **SHALL** resolve to a `U.Viewpoint` whose `EoIClassSpec` refines `EoIClassSpec` of the bundle (`EoIClassSpec(vp) ⊑ EoIClassSpec(bundle)`).

VBL‑2. **Finite, named family.**

* `viewpoints` **SHALL** be finite and non‑empty.
* Each `U.Viewpoint` **SHOULD** carry a stable `ViewpointId` (lexical id) distinct from `ViewFamilyId`.
* The same `U.Viewpoint` **MAY** appear in multiple bundles (e.g. a general “Regulatory” viewpoint in both engineering and governance bundles).

VBL‑3. **Lexical non‑collision.**

* `ViewFamilyId` **MUST NOT** be used as:

  * a `U.ViewId` / `U.ViewFamily(-)` id in MVPK,
  * a `SurfaceKind` or carrier kind in L‑SURF,
  * a generic `ViewpointId` without qualifier (E.18:5.12).
* Libraries **SHOULD** adopt naming schemes that make the distinction clear, e.g. `VF.*` for families, `VP.*` for viewpoints, `PV.*` for publication viewpoints.

VBL‑4. **Intensionality.**

* A `U.ViewpointBundle` is **intensional**: it talks about the family of `U.Viewpoint` specs and their intended use; it does **not** contain any D/S epistemes, `U.View` instances, or `PublicationSurface` artefacts.
* Any concrete document or MVPK face referencing a family **SHALL** do so through its `ViewFamilyId` and per‑view `ViewpointId`, not by embedding the bundle.

##### E.17.1:4.2.3 - Binding bundles into `U.MultiViewDescribing`

`U.MultiViewDescribing[EoIClass]` organises families of descriptions/specifications for a fixed `<T,C>` (entity, context) with a finite viewpoint set Σ.

**Binding rule (informal).**

* Given a `U.ViewpointBundleLibrary` and a bundle with `EoIClassSpec` compatible with the family’s `EoIClass`, a `U.MultiViewDescribing[EoIClass]` instance **MAY** declare:

  * `ViewFamilyId` — the bundle that provides its “canonical” viewpoint set;
  * `ActiveViewpoints ⊆ viewpoints(bundle)` — the subset actually used in this `<T,C>` family.

**Normative constraints.**

VBL‑5. **Bundle import.**
For any `U.MultiViewDescribing[EoIClass]` instance that declares a `ViewFamilyId`:

* its viewpoint set Σ **SHALL** be a finite subset of the `viewpoints` of that bundle;
* every D/S episteme in the family **SHALL** have `viewpointRef` in Σ (as required by E.17.0 / E.10.D2);
* every `U.View` attached to that family under E.17.0 **SHALL** preserve `viewpointRef` from Σ.

VBL‑6. **Multi‑bundle coordination.**
A single `<T,C>` family **MAY** rely on more than one bundle (e.g. TEVB + a safety bundle). In that case:

* the family **SHALL** declare how Σ is partitioned by `ViewFamilyId` (e.g. engineering vs safety);
* any CorrespondenceModel in the family that links views across families **SHALL** cite the relevant `ViewFamilyId` values.

VBL‑7. **No implicit bundles.**
If a `U.MultiViewDescribing` family does **not** declare a `ViewFamilyId`, its Σ is considered **local**. Such families are valid but:
* provide no guarantee of reuse in other projects;
* may be required, by organisational policy, to migrate to a library bundle before external publication.

### E.17.1:5 - Archetypal grounding  *(informative)*

#### E.17.1:5.1 - TEVB engineering viewpoints (preview species)

*Context.*
An engineering organisation wants a **standard family of viewpoints** for describing holons (`U.System` or `U.Episteme`) in E.TGA and MVPK.

*Bundle shape (TEVB, to be defined fully in E.17.2).*

* `viewFamilyId = VF.TEVB.ENG`
* `EoIClassSpec = U.Holon` (with species restriction “is `U.System` or `U.Episteme`”)
* `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface, …}`

Each `VP.*` is a `U.Viewpoint` with:

* `StakeholderFamilies` drawn from engineering RoleEnactors (design, operations, safety);
* `Concerns` tuned to capability, process, structure, and interface questions;
* `AllowedEpistemeKinds` pointing to E.TGA‑level descriptions/specs;
* `ConformanceRules` linked to CV/GF check catalogues.

The bundle is defined once, in a shared library; E.TGA E.18:5.12 then **imports** `VF.TEVB.ENG` and maps these viewpoints to E.TGA constructs without re‑defining them.

#### E.17.1:5.2 - Governance & risk bundle

*Context.*
A governance team wants a reusable set of viewpoints across projects: “Risk”, “Control”, “Compliance”, “Operations”.

*Bundle shape.*

* `viewFamilyId = VF.GovRisk`
* `EoIClassSpec = U.Holon` (holons representing services or programmes)
* `viewpoints = {VP.Risk, VP.Control, VP.Compliance, VP.Operations}`

The same bundle is used:

* in a MultiViewDescribing family for a specific service holon;
* in a publication context where MVPK faces for governance reports reference `VF.GovRisk` and specific `VP.*` ids.

Archetypal grounding cards (E.7) illustrate each viewpoint with a 1‑page “Tell–Show–Show” example.

### E.17.1:6 - Conformance checklist  *(normative)*

| ID                                           | Requirement                                                                                                                                                                          | Practical test                                                                             |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **CC‑VBL‑0 (Unique ViewFamilyId)**           | Within a library edition, each `ViewFamilyId` is unique and refers to exactly one `U.ViewpointBundle`.                                                                               | Scan library metadata; no duplicates; foreign keys resolve.                                |
| **CC‑VBL‑1 (EoIClass compatibility)**        | For every bundle, all `U.Viewpoint` members have `EoIClassSpec` refining the bundle’s `EoIClassSpec`.                                                                                | Check `EoIClassSpec(vp) ⊑ EoIClassSpec(bundle)` for each `vp`.                             |
| **CC‑VBL‑2 (Bundle‑backed families)**        | Any `U.MultiViewDescribing` family that declares a `ViewFamilyId` uses Σ equal to a finite subset of that bundle’s `viewpoints`; all D/S epistemes and views use `viewpointRef ∈ Σ`. | For each family, inspect Σ and `viewpointRef` fields; verify subset and coverage.          |
| **CC‑VBL‑3 (No surface hijack)**             | `ViewFamilyId` never appears as a `SurfaceKind`, MVPK face kind, or carrier type.                                                                                                    | Token scan of schemas and configs; no matches outside library metadata.                    |
| **CC‑VBL‑4 (Archetypal grounding coverage)** | For bundles intended for non‑expert authors, each viewpoint has at least one `U.ArchetypalGrounding` reference.                                                                      | For each such bundle, check that `ArchetypalCards` cover all `viewpoints`.                 |
| **CC‑VBL‑5 (Edition discipline)**            | Libraries and bundles are editioned; changes in viewpoint membership or semantics create new editions rather than silently mutating existing ones.                                   | LAT / change log shows edition bumps for breaking changes; older editions remain readable. |


### E.17.1:7 - Cross‑cutting constraints & naming discipline  *(normative)*

1. **E.10 / A.6.5 alignment.**
   `U.ViewpointBundleLibrary` **SHALL** follow LEX‑BUNDLE and `U.RelationSlotDiscipline`:
   * separate **Tech** and **Plain** registers in names and prose;
   * respect the `*Slot`/`*Ref` conventions from A.6.5 (no `ViewFamilySlot` here; `ViewFamilyId` is a lexical token, not a SlotKind);
   * treat `U.Viewpoint` as the ValueKind for `ViewpointSlot` and `U.ViewpointRef` as its RefKind (no new SlotKinds for viewpoint families);
   * avoid overloading `view`, `viewpoint`, `Surface`, `carrier`.

1. **Engineering vs publication viewpoint ids.**
   * Engineering viewpoint families (TEVB, E.TGA E.18:5.12) use `EngineeringVPId` for `U.Viewpoint` in the bundle.
   * Publication viewpoint families (MVPK) use `PublicationVPId` for MVPK viewpoint ids.
   * A bundle **MAY** contain engineering viewpoints, publication viewpoints, or both, but the id namespaces **SHALL** be disambiguated (e.g. `VP.Eng.*` vs `VP.Pub.*`).

1. **ISO 42010 mapping.**
   * An ISO 42010 “viewpoint library” becomes a `U.ViewpointBundleLibrary` edition.
   * Individual ISO viewpoints correspond to `U.Viewpoint` values inside one or more bundles.
   * ISO “architecture descriptions” correspond to concrete combinations of `U.MultiViewDescribing` families + MVPK surfaces that import those bundles; E.17.1 does not define architecture itself.

1. **Archetypal grounding linkage.**
   * For any bundle that is intended for non‑expert authors, each `U.Viewpoint` in `viewpoints` **SHOULD** have at least one `U.ArchetypalGrounding` card (E.7) referenced from the bundle.
   * These cards are didactic only; they do not alter the semantics of the viewpoints.

1. **Tooling hooks.**
   * Tools **MAY** treat `ViewFamilyId` as a primary key for viewpoint selection widgets, template libraries, or documentation navigation.
   * Tools **MUST NOT** infer semantics from the shape of `ViewFamilyId`; semantics come from the `U.Viewpoint` definitions.

### E.17.1:8 - Consequences  *(informative)*

| Benefit                                    | Why it matters                                                                                                           | Trade‑offs / Mitigations                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Reusable viewpoint families.**           | Teams and tools can share a common understanding of “functional view”, “risk view”, etc., across projects and domains.   | Requires governance of libraries and editions (E.15).                 |
| **Cleaner MultiViewDescribing instances.** | Families can say “we use TEVB+GovRisk” instead of spelling out Σ by hand.                                                | Local Σ are still allowed; migration to bundles may be an extra step. |
| **Better ISO 42010 alignment.**            | ISO viewpoint libraries become first‑class, mappable objects in FPF.                                                     | Needs careful mapping work per architecture sub‑domain.               |
| **Terminology hygiene.**                   | Distinguishing ViewFamilyId from ViewpointId and from surfaces reduces confusion in tooling and documentation.           | Enforced via LEX‑guards and CI checks.                                |
| **Cross‑domain reasoning.**                | The same bundle can be referenced from E.TGA, MVPK, and discipline packs, enabling consistent cross‑view correspondence. | Libraries must stay small and curated to avoid cognitive overload.    |

### E.17.1:9 - Rationale & SoTA‑echoing  *(informative)*

* **ISO 42010 (Edition 2) viewpoint libraries.**
  ISO 42010 generalises *system‑of‑interest* to *entity‑of‑interest* and allows viewpoint libraries that define reusable viewpoint sets for architecture descriptions. `U.ViewpointBundleLibrary` adopts this idea but generalises it beyond architecture to any `EoIClass`, and connects it to FPF’s explicit `U.Viewpoint`, I/D/S discipline, and episteme morphisms.

* **MBSE and SysML v2 view definitions.**
  Modern MBSE practice treats views as **queries over models** governed by named viewpoints, often organised into libraries or profiles. `U.ViewpointBundleLibrary` provides a neutral representation of such libraries so that SysML‑like stacks can be integrated without hard‑coding their terminology into the core.

* **Safety and assurance cases.**
  Safety‑case frameworks (e.g. GSN‑based) implicitly rely on recurrent viewpoints (“hazard analysis”, “mitigation design”, “evidence aggregation”). Embedding them into bundles allows assurance‑oriented Viewpoint families to be reused and linked to Part F harnesses and stance declarations (`DesignRunTag`/`Locus`).

* **Governance and research workflows.**
  Governance / audit frameworks and research pipelines similarly rely on recurring perspectives (e.g. “internal validity”, “external validity”, “reproducibility”). Viewpoint bundles allow these perspectives to be captured once and referenced across many MultiViewDescribing instances.

Overall, `U.ViewpointBundleLibrary` is the mechanism by which **post‑2015 multi‑view practice** (viewpoint libraries, reusable view definitions) is integrated into the FPF stack without compromising strict I/D/S separation or the episteme slot discipline of C.2.1/A.6.5.

### E.17.1:10 - Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotGraph`.**
  Uses `ViewpointSlot` / `ViewSlot` as the structural anchors for viewpoints and views; bundles provide reusable values for `ViewpointSlot`.

* **Builds on A.6.2–A.6.4.**
  Viewpoint bundles do not change episteme morphism laws; they parameterise which `U.EpistemicViewing` pipelines are admissible under a given viewpoint family.

* **Builds on A.7 / E.10.D2.**
  Description/specification epistemes remain I/D/S‑disciplined; bundles only constrain the `viewpointRef` part of `DescriptionContext`.

* **Builds on E.7.**
  Archetypal grounding cards for viewpoints are organised and referenced via bundles, making didactic examples reusable.

* **Constrains E.17.0 `U.MultiViewDescribing`.**
  Families that declare a `ViewFamilyId` must draw Σ from the corresponding `U.ViewpointBundle` (VBL‑5/6).

* **Constrains E.17 (MVPK).**
  MVPK viewpoint sets for publication **SHOULD** be declared as bundles in a library; MVPK faces must not treat `ViewFamilyId` as a surface kind.

* **Constrains E.17.2 (TEVB) and E.18:5.12 (E.TGA engineering viewpoint families).**
  TEVB must be expressed as one or more `U.ViewpointBundle` instances; E.TGA E.18:5.12 maps engineering viewpoints by referring to those bundles, not by defining its own opaque ids.

* **Coordinates with E.10 (LEX‑BUNDLE) and E.15 (LEX‑AUTH).**
  `ViewFamilyId` and `ViewpointId` naming, editioning and evolution follow lexical and authoring protocols; migrations between library editions are tracked in LATs.

### E.17.1:End

## E.17.2 - `TEVB — Typical Engineering Viewpoints Bundle`

> **Tech‑name:** `TEVB` (Typical Engineering Viewpoints Bundle, bundle id `VF.TEVB.ENG`)
> **Plain‑name:** typical engineering viewpoints bundle for holons
> **Tag:** Archetypal species of `U.ViewpointBundle` for engineering holons

**Status.** New; archetypal, notation‑agnostic species of `U.ViewpointBundle` / `U.ViewpointBundleLibrary`.
It is an engineering‑level bundle over holons; it does not itself constitute an architecture framework or architecture‑specific viewpoint library. Architecture‑focused viewpoint bundles are introduced as separate `U.ViewpointBundle` species that may import TEVB.

**Builds on.**
* **E.17.0 — `U.MultiViewDescribing`.** Supplies the generic notion of `U.Viewpoint`, `U.View`, and `ViewFamily` over an `EoIClass ⊑ U.Entity` (here: `EoIClass = U.Holon`).
* **E.17.1 — `U.ViewpointBundleLibrary`.** Provides the generic `U.ViewpointBundle`/`ViewFamilyId` structure; TEVB is a concrete bundle (`VF.TEVB.ENG`) in the core library.
* **A.1 — Holon.** Holon kinds `U.System` and `U.Episteme` as the typical engineering entities‑of‑interest.
* **A.6.2–A.6.4 — Episteme morphisms.** `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, `U.EpistemicRetargeting` as the generic morphism classes behind engineering views.
* **A.7 / E.10.D2 — Strict Distinction & I/D/S.** I/D/S discipline and DescriptionContext; engineering descriptions/specifications under TEVB are D/S‑epistemes with explicit `ViewpointRef`.
* **C.2.1 — `U.EpistemeSlotGraph`.** Provides `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot` and the slot discipline (A.6.5) used by TEVB‑aligned descriptions/specs.

**Used by.**
* **E.18:5.12 — E.TGA viewpoint map.** As a canonical consumer, E.TGA binds its engineering transduction families (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface) to TEVB viewpoints `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface`.
* **E.17 (MVPK).** Publication of engineering morphisms uses TEVB engineering viewpoints on the description/spec side and PublicationVPs on the Surface side.
* **Engineering description/spec patterns.** System, method, module/interface and role‑related description/spec patterns for holons (`U.System`, `U.Episteme`) refer to TEVB when declaring their `ViewpointRef`.
* **ISO‑aligned architecture‑description bundles.** Future species patterns for architecture‑specific viewpoint bundles reuse TEVB as the canonical engineering view family (Functional vs Structural etc.) over systems and their epistemes.

**Guard (lexical & ontological).**
1. **Engineering scope only.** TEVB applies to `EoIClass = U.Holon` with typical cases `U.System` and `U.Episteme`. Using TEVB viewpoints for non‑holonic entities (e.g., pure data structures, abstract theories) requires an explicit species‑level justification; by default it is a conformance violation.
2. **Viewpoint vs Surface.** `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface` are **viewpoints** (intensional `U.Viewpoint` specifications), **not** Surface kinds. They MUST NOT be used as carrier/Surface names (those remain `{PlainView, TechCard, NormsCard, InteropCard, AssuranceLane, …}` under L‑SURF).
3. **EngineeringVPId vs PublicationVPId.** `VP.*` in this pattern are **EngineeringVPId** values (E.18:5.12) and SHALL NOT be reused as PublicationVPs in MVPK. MVPK must introduce separate `PublicationVPId` symbols, linked to TEVB viewpoints only through correspondences.
4. **No new role coordinates in I/D/S.** TEVB references stakeholder groups via `U.RoleEnactor` families but does not introduce `U.Role` as a coordinate in I/D/S signatures (E.10.D2). Role semantics remain confined to RoleEnactment patterns (A.15, F‑R family).
5. **No extra viewpoints inside TEVB.** TEVB defines a **fixed core set** of four engineering viewpoints. Other labels such as “Assurance‑Oriented”, “Interop‑Oriented”, “Information/Data‑Oriented”, “Operational/Deployment”, “Mission/Context” may appear only as **lexical aliases** in E.18:5.12 (e.g. as `ViewFamilyId` / `AliasInViewFamilies` values for transduction species). They MUST NOT extend `TEVB.EngBundle.viewpoints` and MUST NOT be interpreted as additional `U.Viewpoint` kinds in this bundle; when SoTA or local practice demands explicit assurance, information, or mission viewpoints, these SHALL be provided as **separate `U.ViewpointBundle` species** that can be imported alongside TEVB rather than by mutating `VF.TEVB.ENG`.
6. **Not an architecture framework.** TEVB is an engineering‑level viewpoint bundle; architecture‑specific viewpoint bundles and architecture frameworks MUST be introduced as separate `U.ViewpointBundle` species that may import TEVB. They MUST NOT redefine `VF.TEVB.ENG` as an “architecture viewpoint library” or extend it with architecture‑only viewpoints.

### E.17.2:1 - Problem frame  *(informative)*

Engineering teams almost always talk about systems and their models through a **small set of recurring “views”**:
* *What capabilities and behaviours does the system enact?* — function‑oriented, transduction‑oriented talk.
* *What sequences, workflows, and control logics does it realise?* — procedure/process/state‑oriented talk.
* *Who or what enacts which roles?* — role‑enactment, organisational and socio‑technical talk.
* *How is the system decomposed into modules and interfaces?* — physical/logical architecture talk.

In industry, these lenses show up under many names: *functional view, logical view, behavioural view, process view, structural/physical view, deployment view, responsibility view,* and so on. Modern standards and tools (ISO/IEC/IEEE 42010:2022, INCOSE SE Handbook, SysML v2 “views as queries”) all recognise that **viewpoints should be reusable structures**, not ad‑hoc labels.

In FPF, E.17.0 and E.17.1 give the **generic machinery**:
* `U.Viewpoint` as an intensional specification (stakes/concerns/allowed D/S kinds),
* `U.View` as an episteme‑level view (epistema under a viewpoint),
* `U.ViewpointBundle` / `ViewFamilyId` as reusable collections of viewpoints.

E.TGA (E.18:5.12) already assumes a **canonical engineering family** with names like “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, “Module‑Interface”. Without a formal bundle tying these together, those names drift and the mapping between E.TGA, MVPK and I/D/S becomes fragile.

TEVB addresses this by defining a **single, explicit engineering bundle** with a fixed `ViewFamilyId` and a small set of canonical engineering viewpoints over `U.Holon`.

### E.17.2:2 - Problem  *(informative)*

Without TEVB, several failure modes recur:
1. **Inconsistent “functional/structural/behavioural” vocabularies.** Different teams define “functional view” or “process view” differently, even within one organisation; E.TGA E.18:5.12 then has to guess how to map transduction graphs onto whichever interpretation is currently in play.
2. **Architecture frameworks leak into the kernel.** 4+1‑style and similar architectural frameworks get hard‑coded as if they were universal; FPF loses its holonic neutrality and becomes biased to a particular school.
3. **Viewpoints conflated with surfaces and files.** “Functional view” is used both for the underlying viewpoint and for a concrete document or dashboard; MVPK faces, E.TGA transduction families, and I/D/S disciplines become entangled.
4. **Role leakage into I/D/S.** Engineering views that are about role‑enactors are written directly in terms of `U.Role`, blurring the boundary between RoleEnactment (A.15) and description/spec layers, and breaking A.7/E.10.D2.
5. **Poor reuse across systems.** Even when organisations want to reuse the same engineering views across products, plants, or models, there is no canonical bundle to import; each programme recreates “its own” functional/structural views.

TEVB makes engineering viewpoint families **first‑class reusable bundles** and pins them to an explicit `EoIClass` (engineering holons) so that E.TGA, MVPK and discipline‑packs can align on the same vocabulary.

### E.17.2:3 - Forces  *(informative)*

| Force                                       | Tension                                                                                                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**           | We need engineering viewpoints that work for *any* holon (hardware/software/socio‑technical), yet remain recognisable to practitioners steeped in domain‑specific frameworks. |
| **Parsimony vs expressiveness**             | A small, stable **NQD‑front** set of engineering view families (Function, Behaviour/Process, Role‑Enactor, Module‑Interface) vs the temptation to proliferate specialised views for every stakeholder group or quality attribute. |
| **Neutral core vs architecture frameworks** | FPF core must stay neutral and not encode a specific framework (4+1, DoDAF, etc.), while still being compatible with them.                                                    |
| **Consistency vs organisational autonomy**  | Central TEVB definitions must be stable, yet individual organisations need room to refine concerns and episteme kinds within the bundle.                                      |
| **I/D/S clarity vs convenient shortcuts**   | Viewpoints must not re‑introduce `Role` as a coordinate in I/D/S, nor blur Description/Spec/Surface distinctions, even though practitioners informally mix these.             |

TEVB resolves these by fixing a **minimal engineering bundle** and leaving customisation to **species patterns and ViewpointBundleLibrary entries** that refine concerns and allowed episteme kinds without changing the core families.

### E.17.2:4 - Solution — TEVB as a core `U.ViewpointBundle` for holons  *(normative)*

#### E.17.2:4.1 - TEVB bundle identity

TEVB is the **core engineering viewpoint bundle** over holons.

* **Bundle object.** There exists a canonical `U.ViewpointBundle` instance:

  ```
  TEVB.EngBundle : U.ViewpointBundle
  ```

* **ViewFamilyId.**

  ```
  TEVB.EngBundle.viewFamilyId = VF.TEVB.ENG
  ```

  `VF.TEVB.ENG` is reserved for **“Typical Engineering Viewpoints (Engineering)”** in the FPF core ViewpointBundleLibrary.

* **EoIClassSpec (holon scope).**

  TEVB is parameterised by

  ```
  TEVB.EngBundle.EoIClassSpec =
    { h : U.Holon | holonKind(h) ∈ {U.System, U.Episteme} }
  ```

  That is, TEVB applies to holons that are either `U.System` or `U.Episteme`. Other holon kinds MAY be added by species patterns but MUST be justified and documented; the default conformance profile assumes systems and epistemes.

* **Library placement.**

  TEVB lives in the core viewpoint library:

  ```
  TEVB.Library : U.ViewpointBundleLibrary
  TEVB.Library.libraryId = FPF.Core.Viewpoints
  TEVB.Library.bundles ⊇ { TEVB.EngBundle }
  ```

  Additional organisational libraries MAY import and specialise TEVB, but SHALL NOT redefine `VF.TEVB.ENG` with incompatible semantics.

* **Viewpoint set.**

  TEVB defines a **finite set of canonical engineering viewpoints**:

  ```
  TEVB.EngBundle.viewpoints =
    { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
  ```

The selection `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the current **NQD‑frontier** for engineering holon viewpoints in Part G: it realises a Function–Behaviour–Structure‑plus‑Role (`F–B–S+R`) cut that is non‑dominated against candidate families including explicit information/data, assurance/safety, and mission/context viewpoints under the N/U/C/D axes (C.18, G.0). Part G records the SoTA candidate set and rejected alternatives; TEVB only fixes the **core four** where each `VP.* : U.Viewpoint` is defined below. These four are the **only** viewpoints in the core TEVB bundle.

  > **Note.** Other ViewFamilyId values used in E.TGA (e.g., *Assurance‑Oriented*, *Interoperability‑Oriented*, *Information/Data‑Oriented*, *Operational/Deployment*, *Mission/Context*) remain **lexical families only** for transduction species (E.18:5.12). They do not add viewpoints to TEVB; they are orthogonal to TEVB’s `viewpoints` set.

#### E.17.2:4.2 - TEVB engineering viewpoints

Each TEVB viewpoint is a `U.Viewpoint` with:
* `viewpointId : ViewpointId` (concrete identifier, e.g., `VP.Functional`);
* `EoIClassSpec` **inherited from the bundle** (`U.Holon` with `System`/`Episteme` kinds);
* `StakeholderFamilies : FinSet(RoleEnactorFamilyId)` — families of `U.RoleEnactor` that are the primary audience;
* `Concerns : FinSet(ConcernId)` — engineering concerns this viewpoint foregrounds;
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindRef)` — description/spec kinds admissible under this viewpoint (all obeying I/D/S discipline and C.2.1 slot discipline);
* `ConformanceRules : FinSet(RuleId)` — references to checklist items in conformance packs (CV/GF/engineering checklists).

The subsections below fix the **normative intent and minimal field profiles** for each TEVB viewpoint. Species patterns and discipline‑packs may refine `Concerns`, `AllowedEpistemeKinds` and `ConformanceRules`, but MUST preserve the intent.

##### E.17.2:4.2.1 - `VP.Functional` — capability & transduction viewpoint

**Intent.** Look at a holon in terms of **what it can do** under roles: capabilities, transductions, and functional responsibilities, rather than in terms of modules or procedures.

* **viewpointId.**

  ```
  VP.Functional : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**
  Same as the bundle: `U.Holon` with `System`/`Episteme` kinds.

* **StakeholderFamilies (typical examples).**
  Actual `StakeholderFamilies : FinSet(U.RoleEnactor)` values are defined in RoleEnactment discipline packs; labels below are informal.
  * System engineering leads and architects (e.g. SysEng‑lead enactors).
  * Product owners / capability owners.
  * Reliability / performance engineers when reading capability envelopes.

* **Concerns (typical).**
  * Capabilities and functions provided by the holon (`CapabilityConcerns`).
  * Behaviour under roles (`RoleBehaviourConcerns`).
  * Non‑functional envelopes: throughput, latency, availability, energy, safety (`NFPEnvelopeConcerns`).
  * Compositional semantics of functions/transductions (`TransductionCompositionConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Functional` admits descriptions/specifications whose **DescribedEntitySlot** is a holon’s **capability/Method/Mechanism** under a role, e.g.:
  * `SystemFunctionalDescription`, `SystemFunctionalSpec` (species of `U.EpistemeKind` describing system‑level capabilities and their interconnection).
  * `TransductionDescription`, `TransductionSpec` (E.TGA functional lanes).
  * `ServiceCapabilityDescription`, `ServiceCapabilitySpec` (when a holon is in Service role).

  All such epistemes MUST:
  * obey I/D/S discipline: `…Description`/`…Spec` as D/S‑layers for `U.Method`/`U.Mechanism`/`U.PromiseContent`;
  * make their `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` explicit, with `ViewpointRef = VP.Functional`.

* **ConformanceRules (examples).**
  * Functional flows are **total** over their declared domain (no implicit dangling capabilities).
  * Transductions are typed at interfaces (A.6.0, A.6.1) and respect A.6.2/A.6.3 purity/conservativity.
  * When functional views participate in retargeting patterns (e.g. structural reinterpretation species based on `U.EpistemicRetargeting`), they MUST satisfy the relevant retargeting constraints from A.6.4; concrete consumer patterns (such as E.TGA structural reinterpretation, E.18) MAY impose additional rules.

* **SoTA echo (informative).** `VP.Functional` corresponds to the “functional view” in ISO‑aligned architecture descriptions and domain reference architectures (functional viewpoints in IoT and space reference architectures, functional/logical layers in sector frameworks), and to the **Function** axis in FBS‑style design ontologies. It is also the natural home for SysML/SysML‑v2 capability and logical architecture models and for “logical view” slices in 4+1‑style frameworks, once recast into holon/capability terms.

##### E.17.2:4.2.2 - `VP.Procedural` — process & control viewpoint

**Intent.** Look at a holon in terms of **how behaviours are sequenced and controlled**: workflows, state machines, operational procedures, and control logic.

* **viewpointId.**

  ```
  VP.Procedural : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Operations and run‑time owners (`OperationsEnactorFamily`).
  * Control engineers and automation specialists (`ControlEngineerEnactorFamily`).
  * Safety engineers concerned with procedural correctness (`SafetyEngineerEnactorFamily`).

* **Concerns (typical).**
  * Control flow and ordering of actions (`OrderConcerns`).
  * State‑machine behaviour and lifecycle (`StateLifecycleConcerns`).
  * Concurrency, synchronisation, and error handling (`ConcurrencyConcerns`).
  * Operational modes and transitions (startup, shutdown, degraded modes) (`OperationalModeConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Procedural` admits descriptions/specifications where the **DescribedEntitySlot** is a method/process/control Behaviour for the holon, e.g.:
  * `MethodDescription`, `MethodSpec` for operational procedures (A.3.1–A.3.2).
  * `ControlLogicDescription`, `ControlLogicSpec` (IEC 61131‑3 style step diagrams/statecharts).
  * `WorkflowDescription`, `WorkflowSpec` (business processes, orchestration logic).

  These epistemes:
  * must respect the **order discipline** (Γ_method, Γ_ctx) and A.15 (Role–Method–Work alignment);
  * must carry I/D/S‑conformant DescriptionContext with `ViewpointRef = VP.Procedural`.

* **ConformanceRules (examples).**
  * Pre/post‑conditions at step boundaries are explicit and type‑checked (A.3.1/A.3.2, Γ_method).
  * No embedding of Work or calendars inside procedural descriptions (A.7/E.10.D2).
  * Failure modes and recovery actions are declared and traceable to safety analyses (F.15 harnesses where relevant).

* **SoTA echo (informative).** `VP.Procedural` captures the dynamic/process dimension found in SoTA architecture and MBSE practice: process views in 4+1, operational/behavioural views in defence and enterprise frameworks, behaviour diagrams in SysML (activity, sequence, state, interaction), and procedure/control‑oriented models in industrial standards. TEVB abstracts this into a notation‑agnostic “behaviour over time” viewpoint for holons.

##### E.17.2:4.2.3 - `VP.RoleEnactor` — role & device‑structure viewpoint

**Intent.** Look at a holon in terms of **who/what plays which roles** and **how physical/organisational structure supports those roles**. This viewpoint covers both socio‑technical role assignments and “device view” readings of transduction graphs (E.TGA).

* **viewpointId.**

  ```
  VP.RoleEnactor : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Organisational designers and operations managers (`OrgDesignEnactorFamily`).
  * Safety and compliance officers concerned with separation of duties (`SegregationOfDutyEnactorFamily`).
  * Hardware/system engineers concerned with which devices carry which functions (`DeviceEngineerEnactorFamily`).

* **Concerns (typical).**
  * Which holons enact which roles under which contexts (`RoleEnactmentConcerns`).
  * Allocation of capabilities to devices/subsystems (`CapabilityAllocationConcerns`).
  * Organisational constraints: segregation of duties, responsibilities, escalation paths (`GovernanceConcerns`).
  * Device‑view readings of functional graphs (E.TGA Device‑View).

* **AllowedEpistemeKinds (shape).**
  `VP.RoleEnactor` admits descriptions/specifications where the **DescribedEntitySlot** is a **role structure or capability allocation** associated with the holon, e.g.:
  * `RoleDescription`, `RoleSpec` (F.4, F.18) for human or system roles.
  * `RoleEnactmentDescription` for mappings `Holder#Role:Context` (A.15).
  * `DeviceAllocationDescription` mapping functions/transductions to physical modules or devices.

  As with other TEVB viewpoints, these are D/S‑epistemes with `DescriptionContext.ViewpointRef = VP.RoleEnactor`.

* **ConformanceRules (examples).**
  * Role vs Method vs Work vs Capability separation is upheld (A.7, A.15).
  * Device‑view reinterpretation from functional flows MUST be expressed as `U.EpistemicRetargeting` with an explicit `KindBridge` witness (A.6.4). Specific retargeting schemes (for example, E.TGA’s structural reinterpretation in E.18) may add further constraints but are not fixed by TEVB itself.
  * No “role as behaviour” conflation: Roles are masks, behaviours remain Methods/Work.

* **SoTA echo (informative).** `VP.RoleEnactor` aligns with the allocation/responsibility and resource/organisational view clusters seen across MBSE frameworks: allocation views in UAF/NAF, role‑responsibility matrices and RACI‑style artefacts, and “who/what plays which role” slices in usage and operational viewpoints. Many post‑2015 reference architectures treat this axis implicitly; TEVB makes it explicit and holon‑centred while remaining compatible with socio‑technical and device‑allocation practices.

##### E.17.2:4.2.4 - `VP.ModuleInterface` — module & interface viewpoint

**Intent.** Look at a holon in terms of its **modules, interfaces, and structural composition**: what parts exist, how they connect, and how their contracts are specified.

* **viewpointId.**

  ```
  VP.ModuleInterface : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**
  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Hardware and software architects responsible for structure (`StructureArchitectEnactorFamily`).
  * Integration and test engineers (`IntegrationEngineerEnactorFamily`).
  * Lifecycle and maintenance planners looking at replaceable units (`MaintenancePlannerEnactorFamily`).

* **Concerns (typical).**
  * Module decomposition and containment (mereology) (`ModuleMereologyConcerns`).
  * Interfaces and contracts — ports, APIs, physical connectors (`InterfaceConcerns`).
  * Dependency structures and allowed couplings (`DependencyConcerns`).
  * Replaceability and variation points (`VariabilityConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.ModuleInterface` admits descriptions/specifications where the **DescribedEntitySlot** is a **structural architecture** of the holon, e.g.:
  * `SystemStructureDescription`, `SystemStructureSpec` (module/connector descriptions).
  * `ModuleInterfaceDescription`, `ModuleInterfaceSpec` (signature, contracts, physical interface definitions).
  * E.TGA‑style interface/port descriptions over `Signature`/`Mechanism` graphs.

  These epistemes describe the carrier (structure) rather than capability. Functional↔physical reinterpretations between `VP.Functional` and `VP.ModuleInterface` are expressed via `U.EpistemicRetargeting` + `KindBridge` (A.6.4, E.18).

* **ConformanceRules (examples).**
  * Interfaces are typed and explicitly bound to standards where applicable (A.6.0, F‑specs).
  * No inlining of Methods/Work into structure (strict separation of structure vs behaviour).
  * Reinterpretations from functional views into structure MUST respect the applicable `U.EpistemicRetargeting`/Bridge constraints (A.6.4). When combined with a concrete retargeting scheme (e.g. E.TGA structural retargeting, CC‑TGA‑06‑EX), that scheme’s additional rules also apply.

* **SoTA echo (informative).** `VP.ModuleInterface` matches the structural/implementation/deployment families that dominate SoTA architecture descriptions: development and physical views in 4+1, construction/deployment viewpoints in IoT reference architectures, logical/physical architecture layers in UAF/NAF and RASDS‑style frameworks, and structural and interface‑focused models in SysML‑based MBSE. TEVB treats all of these as specialisations of a single holonic “modules and interfaces” viewpoint.

### E.17.2:5 - Archetypal grounding  *(informative)*

A minimal TEVB instantiation looks as follows:

```
TEVB.EngBundle :
  U.ViewpointBundle {
    viewFamilyId   = VF.TEVB.ENG
    EoIClassSpec   = { h : U.Holon | HolonKind(h) ∈ {System, Episteme} }
    viewpoints     = { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
    LibraryRef     = FPF.Core.Viewpoints
  }
```

Each `VP.*` viewpoint is a `U.Viewpoint` as in E.17.0, with:

* `viewpointId ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `EoIClassSpec` inherited from `TEVB.EngBundle`,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` aligned with the subsections above.

**Engineering holon (example).**

Let `Plant_X : U.System` be a production plant, and `ControlStack_X : U.Episteme` be its control and optimisation stack as a holon.

* Under `VP.Functional`, `Plant_X` is viewed as a bundle of capabilities and transductions: material/energy/product flows, optimisation functions, safety envelopes.
* Under `VP.Procedural`, `Plant_X` is viewed as sets of procedures and control sequences: startup/shutdown, normal operation, emergency handling.
* Under `VP.RoleEnactor`, `Plant_X` is viewed as networks of role‑enactors: human operators, controllers, subsystems enacting roles in SOPs and safety cases.
* Under `VP.ModuleInterface`, `Plant_X` is viewed as modules and interfaces: equipment units, pipelines, control modules, buses, and their interfaces/contracts.

Each of these is a **family of D/S‑epistemes** with `DescriptionContext = ⟨DescribedEntityRef(Plant_X or ControlStack_X), BoundedContextRef, ViewpointRef=VP.*⟩` and TEVB ensures that E.TGA and MVPK can rely on this common structure.

### E.17.2:6 - Conformance checklist  *(normative)*

**CC‑TEVB‑1 (Bundle identity).**
Any artefact claiming to be “TEVB engineering viewpoints” MUST:

* refer to `viewFamilyId = VF.TEVB.ENG`,
* have `EoIClassSpec = {h : U.Holon | HolonKind(h) ∈ {System, Episteme}}`,
* enumerate `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` and no others.

**CC‑TEVB‑2 (Viewpoint definition).**
Each `VP.*` viewpoint MUST be a well‑formed `U.Viewpoint` per E.17.0:

* `viewpointId` equal to one of the four engineering IDs,
* `EoIClassSpec` equal to the bundle’s,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` explicitly declared.

**CC‑TEVB‑3 (DescriptionContext completeness).**
Every D/S‑episteme participating in a TEVB‑managed multi‑view family for a holon MUST have a `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` with:

* `DescribedEntityRef` referencing a `U.System` or `U.Episteme`,
* `ViewpointRef ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `BoundedContextRef` pointing to the engineering context (E.10.D1).

**CC‑TEVB‑4 (Separation from PublicationVPs).**
`VP.*` identifiers from TEVB MUST NOT be used as `PublicationVPId` in MVPK. Publication viewpoints live in MVPK and may **correspond** to TEVB engineering viewpoints via `CorrespondenceModel`, but are separate symbols.

**CC‑TEVB‑5 (No Role coordinate in I/D/S).**
TEVB‑aligned descriptions/specs MAY reference `U.RoleEnactor` families in `StakeholderFamilies` but SHALL NOT add `Role` or `RoleEnactor` as axes in I/D/S signatures beyond what A.7/E.10.D2 already provides. Role semantics stay in RoleEnactment patterns; TEVB just selects concerns.

**CC‑TEVB‑6 (Alignment with consumer viewpoint maps).**
When a pattern defines engineering viewpoint families named “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, or “Module‑Interface” over the same `EoIClass` and claims TEVB alignment (for example, E.TGA E.18:5.12 viewpoint map), it MUST bind them to TEVB viewpoints as follows:

* “Functional” → `VP.Functional`,
* “Procedural” → `VP.Procedural`,
* “Role‑Enactor (Device‑Structure)” → `VP.RoleEnactor`,
* “Module‑Interface” → `VP.ModuleInterface`.

Any deviation MUST be explicitly documented as a species‑level extension and MUST NOT reuse `VF.TEVB.ENG`.

### E.17.2:7 - Rationale & SoTA echoing  *(informative)*

#### E.17.2:7.1 - NQD‑grounded choice of the core four

Part G’s NQD discipline treats candidate viewpoint families as points in an N/U/C/D quality space (Use‑Value, Constraint‑Fit, Novelty, Diversity_P). Applied to a SoTA‑harvested candidate set of engineering viewpoints (Functional, Behavioural/Procedural, Structural/Module, Allocation/Role, Information/Data, Assurance/Safety, Mission/Context, Deployment/Operational, Business/Usage), this yields a small Pareto frontier for *engineering holon* viewpoints. On that frontier, the `F–B–S+R` cut implemented by `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the minimal set that:
* spans the Function–Behaviour–Structure ontology used in contemporary design theory while adding an explicit allocation/responsibility axis;  
* aligns with the “functional/process/structural/deployment” clusters recurrent in standards and architecture frameworks;  
* stays neutral with respect to domain‑specific qualities (`‑ilities`) and business/mission framing, which are captured in separate Q‑bundles and governance/viewpoint packs rather than in TEVB itself.

Other candidates (e.g. dedicated information, assurance, or mission viewpoints) remain important but either duplicate concerns already captured by TEVB (when specialised to engineering holons) or are better modelled as orthogonal quality bundles (C.25) or non‑engineering bundles (business/governance packs). TEVB therefore pins only the core four and leaves the rest to specialised families.

#### E.17.2:7.2 - Alignment with post‑2015 engineering practice

* Modern architecture standards built on ISO/IEC/IEEE 42010 describe viewpoint libraries in which functional, behavioural/process, structural/deployment, and business/usage concerns are the dominant clusters; sector RAs such as IoT RA 30141 and space‑domain RAs provide explicit functional and construction/implementation viewpoints alongside business/usage and trustworthiness viewpoints. TEVB reuses the functional and construction/structural clusters as `VP.Functional` and `VP.ModuleInterface`, while treating business and trustworthiness as separate bundles.  
* Model‑based systems engineering practice (INCOSE MBSE guidance, SysML v2 “views‑as‑queries”, UAF/NAF view grids) converges on a small set of core diagram families: structure vs behaviour vs allocation/responsibility vs requirements/mission. TEVB’s `VP.Procedural` and `VP.RoleEnactor` correspond to the behaviour and allocation/responsibility axes, respectively, and are designed to be notation‑neutral over SysML/UAF/UML/Capella‑style models.  
* The FBS family of design ontologies (Function–Behaviour–Structure and extensions) provides a widely used conceptual basis for separating what a system is for, what it does over time, and what it consists of. TEVB’s four viewpoints intentionally implement an FBS+R split at the holon level: `VP.Functional` ≈ Function, `VP.Procedural` ≈ Behaviour, `VP.ModuleInterface` ≈ Structure, with `VP.RoleEnactor` capturing the explicit mapping from functions/behaviours to role‑enacting carriers.  
* Within FPF itself, E.TGA’s “viewpoint families” (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface, plus assurance/interoperability/data/operational/mission aliases) are harmonised by letting the **core four** be TEVB viewpoints and treating the rest as lexical or bundle‑level overlays, not as new kernel viewpoints.

#### E.17.2:7.3 - Why TEVB stays small

TEVB is deliberately *not* a complete architecture framework. It gives FPF a stable, holon‑centred engineering bundle that:
* is small enough to keep in working memory and to govern via EpistemeSlotGraph discipline;  
* is expressive enough to host mappings from SoTA architecture frameworks (4+1, domain‑specific RAs, UAF/NAF grids, SysML‑based MBSE method kits);  
* can be safely combined with additional `U.ViewpointBundle` species (safety/assurance packs, business/mission packs, information/data packs) without mutating the core four;
* sits conceptually **below** architecture‑specific viewpoint libraries, which are introduced as separate `U.ViewpointBundle` species layering TEVB with mission/quality/business viewpoints instead of redefining TEVB.

As SoTA evolves, new bundles can be added or TEVB can gain a new edition with a revised NQD‑frontier, but the TEVB‑A edition fixed here remains the archetypal engineering bundle for holons.

### E.17.2:8 - Relations  *(informative)*

* **Builds on.** E.17.0 (`U.MultiViewDescribing`), E.17.1 (`U.ViewpointBundleLibrary`), A.7/E.10.D2 (I/D/S), C.2.1 (EpistemeSlotGraph), A.6.2–A.6.4 (episteme morphisms).
* **Constrains.** E.18:5.12 (E.TGA viewpoint map), engineering description/spec patterns, MVPK engineering publication profiles.
* **Coordinates with.** L‑SURF/L‑PUBSURF (Surface kinds), F‑R family (Role, RoleDescription, RoleSpec), F.18 (naming discipline for ViewFamilyId / ViewpointId / EngineeringVPId / PublicationVPId).
* **Non‑goals.** TEVB does not prescribe modelling notations (SysML, BPMN, IEC 61131‑3, etc.), storage formats, or tool APIs. It only fixes the **conceptual viewpoint bundle** that such tools must respect when claiming FPF alignment.

