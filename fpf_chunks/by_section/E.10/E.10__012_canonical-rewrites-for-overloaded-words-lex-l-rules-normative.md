---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:9"
section_title: "Canonical rewrites for overloaded words (LEX L‑rules; normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__012_canonical-rewrites-for-overloaded-words-lex-l-rules-normative.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:9 — Canonical rewrites for overloaded words (LEX L‑rules; normative)"
line_start: 59155
line_end: 59277
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.22"
  - "E.23"
  - "E.5"
  - "F.18"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:9 - Canonical rewrites for overloaded words (LEX L‑rules; normative)

> **What this section does.** LEX L‑rules standardise **how we speak** in Core/Context by mapping overloaded everyday words to **canonical FPF concepts**.
> **What this section does not do.** It does **not** restate naming (see **§ 7 MG-DA**) or morphology/casing/suffix rules (see **§ 8 LEX.Morph**); it **depends** on them.
> **Guards.** Tokens are classified by **`LEX.TokenClass ∈ {KernelToken, ContextToken, DiscriminatorToken}`** (§ 7.1). Only **CHR:ReferencePlane** may use the bare word *plane*. E.10.D2 names the boundary between EntityOfConcern and Description epistemes with `DescriptionContext`; specification use needs an exact granting gate; publication faces/forms/units/carriers/renderings stay in publication lanes. Enumerations are **Characteristics** in a **CharacteristicSpace** **only when a CSLC scale is declared; otherwise treat such slots as non-measurable attributes (not Characteristics)**.

#### E.10:9.1 - Hard bans and canonical rewrites (single table; normative)

> **Use this table mechanically.** “Ban” means the listed phrase is **not allowed** in Core prose, identifiers, or diagrams unless the **canonical** appears alongside it (or as a registered Context alias). EntityOfConcern and Description-episteme boundary, specification-use gates, and token gates prevent EntityOfConcern, Description episteme, specification use, publication-lane, and TokenClass leaks (cf. § 8.1).

| **L‑rule**   | **Ambiguous or low-precision word (Ban)**                  | **Canonical FPF target(s)**                                                                                                                                                                     | **EntityOfConcern and Description-episteme boundary and specification-use gate**                                                                       | **TokenClass gate**                         | **Notes**                                                                                            |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **L‑PROC**   | *process*, *procedure*, or *function step*         | `U.Method` (abstract way-of-doing); `U.MethodDescription` (recipe/notation-agnostic); `U.Work` (execution); `U.WorkPlan` (schedule)                                                             | EntityOfConcern-side for `Method`; Description episteme for `MethodDescription`; run record for `Work`; Description episteme for `WorkPlan` | Kernel/Context for types; Context for runs  | “Industrial process” as **line role** -> model system + `…Role`; chemistry in `Method`/`Dynamics`.    |
| **L‑FUNC**   | *function*                                        | `U.Capability` (ability/envelope) **or** `U.PromiseContent` (promise clause or offering) **or** `U.Method` (recipe) **or** `U.Work` (what happened)                                                                       | EntityOfConcern-side for Capability/PromiseContent/Method; run record for Work                                        | Kernel/Context                              | Never use *function* as a type name in Core.                                                         |
| **L‑SERV**   | *service* used for team/system/API/ticket/process | Always unpack to the facet: `U.PromiseContent` (service offering or promise clause), `U.Commitment` (SLA obligation), `U.SpeechAct` (promise or offer act), `accessSpec : U.MethodDescription` (API or interface spec), **service access point** (`SystemRef`, addressable endpoint), **service delivery system** (`SystemRef`), **service delivery method** (`U.MethodDescription`), or `U.Work` (delivery run, case, or ticket). | EntityOfConcern-side for PromiseContent/Commitment/Method; Description episteme for specs; system-side for systems; run record for Work                                        | Kernel/Context/Discriminator (per facet) | “API = service” is forbidden; name the facet head phrase (A.6.8).                                                           |
| **L‑SLA**    | *SLA* or *service level agreement* used for SLO, contract, or document | Unpack: (i) SLOs or acceptance thresholds -> `U.PromiseContent.acceptanceSpec`; (ii) binding obligation/penalty -> `U.Commitment`; (iii) packaged “the SLA” -> Contract Bundle (A.6.C); (iv) published terms -> `U.SpeechAct` + clause carrier (`U.Episteme`). | EntityOfConcern-side for PromiseContent/Commitment; Description episteme for clause carriers/specs; run record for Work+evidence | Kernel/Context/Discriminator | Treat “SLA” as polysemic shorthand; never store it as a single type name. |
| **L‑SCHED**  | *schedule*, *plan*, or *calendar* as execution    | `U.WorkPlan` (intent/window) vs `U.Work` (actuals/telemetry)                                                                                                                                    | Description episteme vs run record                                                                             | Context                                     | Never attach actuals to a plan.                                                                      |
| **L‑ACT**    | *activity*, *action*, or *task* as type           | `U.Work` (execution); **steps** belong to `U.MethodDescription` (with `requiredRoles`, capability bounds)                                                                                       | run record vs Description episteme                                                                             | Context                                     | Reserve verbs: *enact* (role/RSG), *execute* (Work), *actuate* (System), *approve* (SpeechAct Work). |
| **L‑AGENT**  | *agent, actor, or doer* (bare)                     | say “system **bearing** `…Role`”; use `U.AgentialRole` where needed                                                                                                                             | I                                                                                    | Kernel/Context                              | Org titles (Owner/Operator/Reviewer) live as **roles in a Context**.                                 |
| **L‑OWNER**  | *owner of X* (global)                             | Ownership is a **Role** inside a `U.BoundedContext` (e.g., `OwnerRole:ITIL_2020`); SoD via `⊥`                                                                                                  | I                                                                                    | Context                                     | No global “owner” property in Kernel.                                                                |
| **L‑CAP**    | *capability* for assignment, recipe, run, or promise | `U.Capability` only = ability with envelope; assignments are `…Role`; recipes `U.Method` or `U.MethodDescription`; runs `Work`; promises `U.PromiseContent` (service promise clause or offering)                                                       | EntityOfConcern-side vs Description episteme vs run record                                                                        | Kernel/Context                              | Holder of a Capability is a `U.System`.                                                              |
| **L‑DYN**    | *process of diffusion, growth, or learning*       | `U.Dynamics` (law/model of change)                                                                                                                                                              | I                                                                                    | Kernel/Context                              | Reserve for uncaused change models.                                                                  |
| **L‑EVID**   | “paper/dataset proves/ensures”                    | `…#EvidenceRole:Context` on an **Episteme**; claims/scopes/polarity/timespan; provenance from `Work`                                                                                            | Description episteme, possibly admitted for specification use                                                                                  | Context/Discriminator                       | Evidence is a **role binding**, not an actor.                                                        |
| **L‑CTX**    | *context* (fuzzy trope)                           | `U.BoundedContext` (named card)                                                                                                                                                                 | —                                                                                    | Context                                     | Never use “depends on context” in Core; **name** the Context.                                        |
| **L‑BRIDGE** | cross‑context equivalence “by same label” | Explicit **Bridge Card** (F.9): state `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** for disambiguation + licence‑revealing name/verb choice). | — | — | Same label ≠ same concept; umbrella “same/equivalent/align/map/…” must be repaired into a Bridge before it can justify reuse, rows, or substitution. |

> **Red/Green pattern (example).** ✗ “The **process** ensures quality.” → ✓ “The **MethodDescription** defines steps; **Work** is **evaluated** against **RequirementRole**.”

#### E.10:9.2 - Quick substitutions (common rewrite hints)

> Use these as quick rewrite hints; accept only if the transformed sentence passes **§ 7 MG-DA** and **§ 8 LEX.Morph** gates.

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
2. **Right EntityOfConcern and Description-episteme boundary and specification use.** EntityOfConcern, Description-episteme, specification-use, publication-lane, and run-record uses are not conflated (cf. § 8.1 gates).
3. **Promise vs ability vs performance.** `PromiseContent` (promise clause), `Capability` (ability), `Work` (performance) are not conflated.
4. **No anthropomorphism.** Documents/datasets/models do not “do”; **Systems** do.
5. **Scheduling hygiene.** No actuals on `WorkPlan`; all actuals live on `Work`.
6. **Cross‑context reuse.** Any reuse across Contexts cites a **Bridge id** with kind, direction, congruence level, loss, and scope. Apply **A.6.9 (RPR‑XCTX)** when the published prose uses “same”, “equivalent”, “align”, “map”, or similar bridge wording.
7. **MG-DA ok.** New or refactored tokens pass **§ 7 MG-DA** (anchored head noun; collision check; CharacteristicSpace for enums).
8. **Morphology ok.** Suffix/prefix/casing respect **§ 8 LEX.Morph** (e.g., `…Role`, `MethodDescription`, `Work`, reserved prefixes).
9. **Banned tokens absent.** No *process/function/task/activity* in Kernel senses; no tooling/file suffixes in Kernel tokens.
10. **State gating present (when needed).** Readiness is expressed via **RSG state** + **StateAssertion**, not vague “approved/ready”.

#### E.10:9.4 - Coordination map (how LEX plugs into the rest of FPF)

* **With E.10.D1 D.CTX (Context discipline).**
  ULR–CTX‑1: Every Core meaning that can vary **names its `U.BoundedContext`**.
  ULR–CTX‑2: Same‑spelled labels are **distinct senses** across Contexts; reuse requires a **Bridge** (F.9) with CL & loss notes.

* **With E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use/refinement discipline).**
  Speak in the **right EntityOfConcern and Description-episteme boundary and specification use**. ULR-EOC-DESC-SPEC-1..3 apply (the EntityOfConcern is named directly; Description suffixes name Description-episteme use; Spec suffixes name specification use on a Description episteme; work/state assertions are evaluations or occurrences). Upgrades Description to specification use only when **checkable acceptance** or another exact specification-granting gate exists.

* **With A.2 / A.15 (Role–Method–Work alignment).**
  Role = **assignment**; Method = **way‑of‑doing**; MethodDescription = **documented recipe**; Work = **dated occurrence**. Sentences must keep this split.

* **With F‑cluster (Unification) & UTS (F.17).**
  Harvest in one Context → **SenseCell** → **Concept‑Set row** with relation (`≡/⋈/⊂/⟂`) and losses. UTS is the human‑readable roll‑up.

> **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance: `LEX.TokenClass(t)=c ⇒ USM.Scope(usage) ∈ AllowedScopes(c)` (see § 7.5).

#### E.10:9.5 - Conformance checklist (LEX‑CC)

1. **LEX‑CC‑1 (Bans).** Any banned token in Core/Arch fails unless the **canonical** appears (or the token is a registered Context alias).
2. **LEX‑CC‑2 (Context).** Each polysemous term names its **`U.BoundedContext`**.
3. **LEX‑CC‑3 (EntityOfConcern and Description-episteme boundary and specification-use morphology).** Usage passes **§ 8** gates (suffix/prefix/casing), EntityOfConcern and Description-episteme boundary checks, and specification-use checks.
4. **LEX‑CC‑4 (Bridge).** Cross‑context reuse cites **Bridge id** and CL; same‑spelled labels without a Bridge are non‑conformant.
5. **LEX‑CC‑5 (MG-DA).** New tokens pass **MG-DA** tests, including **full‑text collision** and **Reserved‑Names** checks.
6. **LEX‑CC‑6 (Service & evidence).** Service acceptance computed from **Work**; evidence is an **EvidenceRole** on an **Episteme** with provenance.
7. **LEX‑CC‑7 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
8. **LEX‑CC‑8 (Minting discipline).** If overload cleanup requires one local replacement phrase, the text records the repaired phrase and the governing local repair pattern. If cleanup requires one durable reusable name, the text runs the full **F.18 `MintNew` or `DocumentLegacy`** procedure; intuition-first partial Name Cards are non-conformant.

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

**Semioarchitecture.**
✗ “`projection` has one meaning in routing and bridge prose.”
✓ `A.16` keeps `projection` as a move name for route-bounded partialization; `F.9.1` keeps `projection` as a bridge stance label. If one durable reusable replacement name is really needed, handle the naming question with **F.18 `MintNew` or an explicit source-retention naming decision** rather than flattening both local interpretations into one umbrella rewrite.

**Editorial note.**
This section **inherits** § 7 **MG-DA** (anchored head nouns; Characteristic/CharacteristicSpace for enums; collision checks) and § 8 **LEX.Morph** (suffix/prefix/casing). It deliberately **omits** their details to avoid duplication.  The only legitimate uses of *plane* in the Core are **CHR:ReferencePlane** and the derived operators **CL^plane** and **Φ_plane**; policy flags MUST NOT introduce new “planes”. To distinguish pre‑operational vs operational states *within* **ReferencePlane=world**, use **WorldRegime ∈ {prep|live}** (formerly `PlaneRegime`).

#### E.10:9.7 - Guarded-head cross-reference *(normative lexical caution)*
When one wording head already carries several FPF-governed local interpretations, lexical cleanup should prefer a **guarded-head note** over silent flattening. The note may record that the head remains risky, name the cited texts or patterns that govern the local interpretations, and point readers to the local canonical interpretation in each cited text.

If cleanup reveals that no admissible existing token can carry the needed meaning, use the local repair pattern for one-off wording. If the change needs one durable reusable name, handle the naming question with **F.18 `MintNew` or `DocumentLegacy`** rather than inventing an ad hoc synonym by feel.

This cross-reference is lexical only. It does **not** create a new repair-side definition site, does **not** establish Cross-context equivalence, and does **not** overrule cited local definitions. It simply keeps overloaded heads from being normalized into one false global interpretation.

`projection` is the main current example: `A.16` keeps it as a move name for route-bounded partialization, while `F.9.1` keeps it as a bridge stance label. E.10 therefore requires deconfliction notes and explicit naming of the cited text that governs each local interpretation, not one umbrella rewrite that erases the distinction.

