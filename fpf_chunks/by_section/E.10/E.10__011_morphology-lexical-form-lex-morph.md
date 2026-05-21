---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:8"
section_title: "Morphology & Lexical Form (LEX.Morph)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__011_morphology-lexical-form-lex-morph.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:8 — Morphology & Lexical Form (LEX.Morph)"
line_start: 50763
line_end: 51003
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.7"
  - "B.1"
  - "B.3"
  - "E.10.SEMIO"
  - "E.5"
  - "F.18"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:8 - Morphology & Lexical Form (LEX.Morph)

> **Principle.** Form follows the **FPF kind being named**. A token’s morphology (suffix/prefix/casing) must (a) express **what kind of thing** it names, (b) respect **MG-DA** (Minimal Generality & Domain Anchoring), and (c) pass **LEX.TokenClass** gates:
> `LEX.TokenClass(token) ∈ {KernelToken | ContextToken | DiscriminatorToken}`.
> Morphological choices never override **I/D/S layers** or **CHR\:ReferencePlane** semantics.

#### E.10:8.0 - Casing & basic forms

**M‑0 (Casing and categories).**
Types & role kinds: **UpperCamelCase** (`IncisionOperatorRole`, `MethodDescription`).
Relations/verbs: **lowerCamelCase** (`performedBy`, `isExecutionOf`, `bindsMethod`).
IDs/instances: **flat with delimiters** (context‑defined) but never collide with type forms (e.g., `W#Seam134`, `ctx:Hospital.OR_2025`).
**Register discipline:** normative tokens use the Technical register; Plain synonyms are allowed in prose only, never in constraints.


#### E.10:8.1 - Reserved suffixes (gated by LEX.TokenClass and I/D/S)

> **Use tables as a whitelist.** Rows indicate **when** a suffix is permitted and **what it means**. “Layer gate” prevents I/D/S confusion; “Examples” are illustrative.

| **Suffix**              | **Kind named by suffix**                   | **Layer gate**                       | **LEX.TokenClass gate**         | **Examples**                                      | **Forbidden misuses (typical)**                                       |
| ----------------------- | ------------------------------------------ | ------------------------------------ | ------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| **`Role`**              | **Role kind** (intensional)                | I‑layer                              | KernelToken/ContextToken        | `TransformerRole`, `ApproverRole`                 | Appearing in BoM/mereology; mixing with run logs.                     |
| **`Method`**            | **Abstract way of doing** (recipe type)    | I‑layer                              | KernelToken/ContextToken        | `SteriliseInstrumentMethod`                       | Versioning on `Method` (version the `MethodDescription` instead).     |
| **`MethodDescription`** | **Recipe/description** (notation‑agnostic) | D‑layer                              | KernelToken/ContextToken        | `JS_Schedule_v4_MethodDescription`                | Calling it “process”; encoding runtime actuals here.                  |
| **`…Spec`**             | **Testable specification** (acceptance‑bound) | S‑layer                              | KernelToken/ContextToken        | `MethodSpec`, `FlowSpec`, `SystemSpec`            | Using “Spec” without acceptance tests/harness; putting runtime actuals here. |
| **`Work`**              | **Execution** (runs or kinds of runs)      | (run record; not I/D/S)            | KernelToken/ContextToken        | `SpeechActWork`, `W#Seam134`                      | Plans/schedules; design‑time recipes.                                 |
| **`WorkPlan`**          | **Schedule of intent**                     | D‑layer (plan record)              | ContextToken                    | `MaintenanceWorkPlan_Q3`                          | Logging actuals; claiming execution.                                  |
| **`Service`**           | **External promise object**                | I‑layer (Standarded intension)       | KernelToken/ContextToken        | `ObjectStorageService`, `PassportIssuanceService` | Naming teams/APIs as “Service”.                                       |
| **`Capability`**        | **System ability**                         | I‑layer                              | KernelToken/ContextToken        | `ScheduleGenerationCapability`                    | Mislabeling roles or methods as capabilities.                         |
| **`Dynamics`**          | **Law/model of change**                    | I‑layer                              | KernelToken/ContextToken        | `LotkaVolterraDynamics`                           | Using for abilities (`Capability`) or recipes (`Method`).             |
| **`Observation`**       | **Observation record/kind**                | (run record; not I/D/S)            | ContextToken/DiscriminatorToken | `VibrationObservation`                            | Mixing with `MethodDescription` or `Evaluation`.                      |
| **`Evaluation`**        | **Evaluation episteme or evaluation record**        | D/S‑layer (epistemic episteme)              | ContextToken/DiscriminatorToken | `CalibrationEvaluation`                           | Using to name roles or methods.                                       |
| **`EvidenceRole`**      | **Role in evidence assembly**              | I‑layer (role kind)                  | KernelToken/ContextToken        | `WitnessStatementEvidenceRole`                    | Using as a generic “evidence”.                                        |
| **`Episteme`**          | **Epistemic knowledge unit** (structural)  | D/S‑layer                            | KernelToken/ContextToken        | `TraceabilityEpisteme`                            | Colliding with CHR **ReferencePlane** (never suffix “Plane”).         |
| **`System`/`Holon`**    | **Substantial entity**                     | I‑layer                              | KernelToken/ContextToken        | `AnesthesiaSystem`, `OrderFulfillmentHolon`       | Using to denote Context or run record.                              |
| **`Boundary`**          | **System boundary**                        | I‑layer                              | KernelToken/ContextToken        | `SterileFieldBoundary`                            | Using as a role or method.                                            |
| **`Objective`**         | **Target state**                           | I/D‑layer (depends on formalization) | KernelToken/ContextToken        | `HemostasisObjective`                             | Encoding acceptance tests here (put tests in Spec/MethodDescription). |
| **`Requirement`**       | **Obligation at acceptance**               | D/S‑layer                            | KernelToken/ContextToken        | `LatencyRequirement`                              | Using as a role or capability.                                        |
| **`BoundedContext`**    | **Context card**                           | (meta‑structural; not I/D/S)         | ContextToken                    | `ITIL_2020_BoundedContext`                        | Treating Context as domain; minting `U.*` inside a Context.           |
| **`Surface`**              | `PublicationSurface` or `InteropSurface` over an episteme   | D and S layer (publication)     | ContextToken                     | PublicationSurface, InteropSurface       | StructureSurface, MechanismSurface, PortfolioSurface |
| **`Card`**                 | UTS/record unit (episteme)               | D-layer (publication)       | ContextToken                     | MethodCard, ExternalIndexCard            | Encoding runtime actuals; using as a ‘Service’  |

| **Suffix** | **Lexical class** | **Meaning / Ontology** | **Where it lives** | **Examples / Notes** |
|--- |--- |--- |--- |--- |
| **Space** | Intensional kind | A typed **state space** (finite product of Characteristic×Scale slots); no procedures | Kernel A.19; CHR/space consumers | `CharacteristicSpace`, `CreativitySpace`. Edition of a Space is a **phase** of the episteme that defines it. |
| **SpaceRef** | Pointer | Registry reference to a Space | Data fields / UTS | `CharacteristicSpaceRef`. Use **`.edition`** on the **Ref** when pinning a historical phase. |
| **Map** | Intensional kind (method) | A **mapping method** from subjects to coordinates in a declared Space (encoder/featurizer) | Kernel/Method family (I‑layer), described/spec’d via I/D/S | `DescriptorMap` (declares invariances, corpus typing). Not a record or file. |
| **MapRef** | Pointer | Registry reference to a **Map** | Data fields / UTS | `DescriptorMapRef`. Pin the method phase via **`DescriptorMapRef.edition`**. |
| **Def** | S‑layer alias (CG‑Spec family) | A **definition/specification publication** that fixes a **formula** or **distance** over a space; *synonym of …Spec* **within CG‑Spec registries only** | Part G (CG‑Spec family) | `DistanceDef` ≍ `DistanceSpec`. Prefer **…Spec** in new normative prose; **…Def** retained where already published. |
| **DefRef** | Pointer | Registry reference to a **…Spec/…Def** | Data fields / UTS | `DistanceDefRef`. Use **`DistanceDefRef.edition`** to pin the exact formula edition. |
| **Spec** | S‑layer | Testable invariants bound to acceptance harnesses | E.10 & A.21 | For stable, testable definitions; **normative** by default; S‑layer, Spec‑gated | Use for normative calculi and scoring/normalization specifications. |
| **Slot** | Structural position | Named **argument position** in a relation/morphism signature (SlotKind in A.6.5) | Kernel A.6.0/A.6.5 | `DescribedEntitySlot`, `GroundingHolonSlot`. Always names a *position*; never used for ValueKinds or episteme fields. |
| **Ref** | Pointer | **Reference/identifier** to a registry item of some ValueKind (RefKind in A.6.5), not the thing itself | Data fields / UTS; RefKind types | `U.EntityRef`, `U.HolonRef`; episteme fields `…Ref : U.EntityRef`. Reserved for **RefKinds** and episteme fields typed as them; `…Ref` **never** carries content and is never used for ValueKinds or SlotKinds. |
| **Series** | Governance object | A **PhaseOf chain** (“editions”) for an episteme | Edition governance | `U.EditionSeries`. Holds immutability and provenance rules. |
| **.edition** | Attribute (on **Ref**) | The **phase id** of the **referenced record**; attaches to `…Ref`, not to the record name | Data fields / UTS | Use `XRef.edition`, **not** bare `XEdition` fields. Lower camelCase for keys. |

**Notes.**
• **Kernel‑only ban list** remains in § 8.3.
• **CHR guard:** the only token that may use the word *plane* is **CHR:ReferencePlane**.
• **Axis and dimension metaphors** are deprecated; use **Characteristic** for a measured aspect and **CharacteristicSpace** for a declared characteristic space where an enumeration is intended (see § 7).

**Not only suffix guard**
* Suffixes are closely related to kinds and **should** be clearly guarded by MG-DA.
* Other morphemes (not only suffixes) also **must** respect kinds. For example, **Space is a geometric concept** — **never** use it as a suffix (`…Space…`) or other morpheme in beginning or in the middle of a term to name non‑geometric entities (e.g. prefer **Set/Kid/Kit** instead of **Space** where membership is intended).

**L-EPI-PUB — episteme, publication, view, carrier, and authority-reference lane discipline**
* Use `U.Episteme` for the claim-bearing unit. Use `U.EpistemePublication` or governed `U.Episteme` publication only when that episteme is available as a published episteme under C.2.1/E.17 discipline.
* Name the exact publication form separately from the episteme: for example `U.PreArticulationCuePack`, `RoutedCueSet`, `U.AbductivePrompt`, typed route-bounded projection, partial normal form, endpoint-pattern-governed publication, or another declared form. A publication form is not itself the governing FPF source.
* Name `U.View` and MVPK face separately from the publication form. A `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane` is an episteme-level view or publication face, not the source claim, not the publication form itself, and not the SCR or RSCR carrier.
* Name the carrier or rendering lane separately. Documents, dashboards, generated screens, trace files, cards, and transport formats hold or render a publication; they are not the `U.Episteme`, not the claim or effect being relied on, and not the governing pattern.
* Name source-finding cues separately from source epistemes. A cue, badge, credential view, dashboard tile, heading, signature-looking mark, or generated explanation may help find a source; it does not by itself create an `authoritySourceRef` target, evidence relation, gate decision, assurance claim, role assignment, status assertion, work occurrence, or permission.
* Use `governingPatternRef` for a named FPF pattern that governs admissible interpretation or use. Use `authoritySourceRef` when a non-pattern `authoritySourceRef` target such as an external standard, editioned register, DRR, gate decision, policy source, or role-assignment or status register carries the relevant authority. Do not use generic semio wording, generic source wording, generic project-work wording, or container-placement wording as solution terms.
* When a published episteme is used for work, name the live P2W chain element: intended method family, selected method/method of work, `U.WorkPlanning` baseline, planned work, actual `U.Work` or `U.WorkEnactment`, work result, result measurement, or non-work reliance on a claim or effect. Do not let generic `action`, `use`, or `material` hide that distinction.
* Use `E.10.SEMIO` when semio-heavy wording carries episteme, publication, view, carrier, relation, admissibility, evidence, work, gate, decision, method, or FPF-pattern-application load. This parent pattern keeps the lexical and naming discipline; `E.10.SEMIO` supplies the semantic-rewrite profile that recovers the exact FPF kind, relation record, relation phrase, tuple-like record, exact project-side FPF kind and reference, or not-triggered disposition before final wording is accepted.

**L‑SURF — disciplined use of *Surface* **
* **Definition.** *Surface* is reserved for `PublicationSurface` and `InteropSurface`: UTS, shipping, and interop publication surfaces that present admissible, plane-aware summaries for a stated audience and purpose. A Surface is a conceptual bundle of views in the ISO 42010 sense, with declared viewpoint. Serialisations live in Annex and Interop. Surfaces package D and S projections produced via `Describe_ID` and `Specify_DS` in `A.7` and do not change object ontology.
* **Allowed:** `PublicationSurface`, `InteropSurface` (G.10/G.13).
* **Forbidden:** `StructureSurface`, `MechanismSurface`, `PortfolioSurface`, and any `…Surface` that denotes a structural, mechanistic, measurement, review, assurance, explanation, comparison, or publication-unit object.
* **Preferred alternatives:** use `…Boundary` (structural border), `…View` (publication view), or `…Card` (UTS record).

**L‑SPACE — disciplined use of *Space* **
* Use *Space* only for **CHR‑grounded measurement and state constructs** such as `CharacteristicSpace` per A.19. Do **not** coin generic `…Space` for sets, portfolios, or publication forms. Publish portfolios and archives as **sets** via admissible selectors; publish them on UTS as **views** or **cards**, not as spaces.
* **Field‑name guard (Kernel blocks).** In **Kernel conceptual blocks** (e.g., A.6.0/A.6.1 lists), **do not** name a field `…Space`; reserve *Space* to the **types** (CHR/ReferencePlane families). Use **BaseType** as the field name and let the referenced `U.Type` carry `…Space` where appropriate; otherwise, for set‑valued universes, use `…Set`.
* Space is geomertic concept, neve use it even not as a suffix for naming non-geometric spaces (e.g. instead of Sets with membership)

**L‑ROLE — disciplined use of *Role***
* **Role** is always **Role Enactment for the `U.Holon`/`U.System` kind** (agentive use).
* **Param‑slot / relation‑endpoint guard.** Do **not** use the morpheme **`Role`** for **formal parameter positions** in operator algebra declarations (`OperationAlgebra`) or Signature arguments. Reserve **`Role`** for **agentive kinds** only (A.2/F.4/F.6). Prefer SlotKinds + SlotSpecs (A.6.5) to type formal slots; if a didactic list is useful, use a `ValueKindView` (name→ValueKind) projection derived from SlotSpecs/SlotIndex. Same for similar situations (table columns, tuple placements): use MG-DA with domain‑**specific** terminology, never “Role”.

#### E.10:8.2 - Forbidden suffixes & the DevOps, Data Governance and Repository-Workflow Lexical Firewall

**M‑F (Forbidden in Kernel tokens).** In KernelToken names, do **not** use: *…Function*, *…Process*, *…Task*, *…Activity*. These are ambiguous or vacuous—map using § 6 typing rules (often to `Method`, `MethodDescription`, or `Work`).

**M‑FW (Tool/file markers).** Tooling/file suffixes (*…API*, *…JSON*, *…YAML*, *…CI*, *…Kafka*, *…Postgres*) are **not** part of conceptual names. Place them in **Context** glossaries or operational configs (DevOps Lexical Firewall). Kernel names never carry tool/format/notation marks. It is pure conceptual, no data management and data governance intended.

#### E.10:8.3 - Prefix discipline

**M‑P1 (Reserved prefixes).** `U.` reserved for **Kernel types**; `Γ_` for algebraic operators; `CAL/LOG/CHR` for **pattern packages**. Never mint `U.*` inside a Context.

**M‑P2 (Edition markers).** Apply explicit edition/version markers to **Contexts** and to `MethodDescription` / `Service`—**not** to `Method` (e.g., `BPMN_2.0_BoundedContext`, `JS_Schedule_v4_MethodDescription`, `PassportIssuanceService_v2025`).  Authors MAY annotate Context or Service names for didactics.
**Norms (edition vs release vs version).**
1) **edition** — the **content phase** of an episteme (Concept/Object/Symbol where Symbol‑only notation swaps do not force a phase). Lives in `U.EditionSeries`. Never embedded in labels (see R‑RD‑7); bind via data: `…Ref.edition`.
2) **release** — a **Work** of making a **Carrier** public; may carry tags/dates; does **not** change episteme identity or phase.
3) **version** — a **tooling/carrier** identifier (file/package/code). Use only in Tooling/Pedagogy families; not in Core names.

**Property discipline.** When a field pins a referenced record’s phase, write it as **`<Thing>Ref.edition`** (dot notation), never as a standalone `…Edition` key. E.g., replace `DHCMethodEdition` with `DHCMethodRef.edition`.

#### E.10:8.4 - Morphology tests (apply with § 7 MG-DA)

**M‑1 (Slot test).** The candidate fits **one** slot in the Strict Distinction lattice (Object ≠ Description ≠ Carrier; Role ≠ Method ≠ Work). If not, **rename** or split.

**M‑2 (Object‑of‑talk anchoring).** The head noun names the **object being classified** (Role/Method/Service/Work/Context/Characteristic). No free‑floating metaphors.

**M‑3 (Family congruence).** Where eligibility clarity is needed, add a **Context‑specific characteristic** (RCS) as a qualifier (e.g., `NormativeStandardRole`). Do **not** fake families with bare metaphors (no `RowPlane`, `senseFamily`, `…Lane`).

**M‑4 (Run vs design).** Use **`Work`** only for executions; use **`MethodDescription`** for recipes; never cross.

**M‑5 (Kernel parochiality).** KernelToken names carry **no domain nouns**; push domain markers to Context or RCS.

**M‑6 (Vacuity ban).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use established kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).

**M‑7 (Notation independence).** Intensional meaning survives notation/tool swaps.

**M‑8 (Collision & uniqueness).** Before merge, run **full‑text** + **Reserved‑Names** checks; the token must not collide with any other meaning anywhere in FPF (cf. § 7 MG-DA‑T5).

#### E.10:8.5 - Alias hygiene

Aliases live **only** inside a **Context Glossary** and map to **one** technical label with an **equivalence** note (≡). No global aliases.

#### E.10:8.5a - Entry lexeme support and lexical-query discipline

Canonical entry-neighborhoods may use one compact **entry lexeme support**
block when the lexical load is real.
That support should not live in every pattern body by default.
Keep it instead in:

* `J.4`,
* `I.2`,
* `Table of Content` query rows,
* or one bounded lexical-support record governed by `F.17`, `UTS`, or `F.18`.

This block remains one editorial lexical-query set.
It does not mint names, aliases, `U.Types`, bridges, or semantic equivalences
by itself.
When visible, it should distinguish at least:

* canonical label,
* plain-language twin,
* domain alias,
* lexical-query cue,
* deprecated cue,
* false friend or forbidden synonym.

Minimal visible lexical-query shape may therefore use one compact field set such
as:

```text
canonical
noncanonical_visible
domain_query_examples
forbidden_aliases
```

Ordinary lexical-query support should stay compact:

* ordinary `Table of Content` rows: prefer `2-5` query phrases;
* ordinary `J.4` neighborhoods: keep only the most discriminating domain phrases and
  false friends;
* fuller lexical sets belong under `F.17, F.18, and E.10` only when one real
  naming, alias, bridge, or collision load exists.

Lexical support should increase entry precision, not maximize keyword recall.
The same boundary should be kept explicit in lexical support:

* `lexical_hook` is not one alias;
* one alias is not one canonical name;
* one search cue is not one semantic equivalence;
* one `entry_orientation_label` is not one `RelationKind`.

Language-specific query cues may be added as entry-lexeme support.
They do not become canonical names, aliases, or semantic equivalents unless
admitted through `F.18` / `E.10`.
One Russian practitioner phrase may therefore help recover one English
canonical pattern while remaining lexical-query support only.

#### E.10:8.6 - Compatibility with USM (acts vs tokens)

**LEX applies to tokens; USM applies to acts.** Mint/rename/use are **LexicalActs** that carry a USM scope (e.g., ClaimScope, WorkScope). LEX constrains **where** a token form may appear via **AllowedScopes** policies:

`LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)`.

Example: using a `KernelToken` in a Context constraint may require a Bridge/alias; logging `Work` inside a MethodDescription violates M‑4 and the policy.

#### E.10:8.7 - Acceptance & regression checks (LEX/USM)

* **SCR‑MOR‑S01 (Suffix whitelist).** Every normative token with a reserved suffix matches § 8.1 row semantics and passes Layer gates.
* **SCR‑MOR‑S02 (Kernel bans).** KernelToken names contain none of the forbidden suffixes (§ 8.2).
* **SCR‑MOR‑S03 (Prefixes).** Reserved prefixes obey § 8.3; no `U.*` minted in Context.
* **SCR‑MOR‑S04 (Run/design gate).** `Work` appears only for executions; `MethodDescription` has no runtime actuals.
* **SCR‑MOR‑S05 (Collision).** Full‑text + Reserved‑Names checks pass (no other sense of the token elsewhere).
* **SCR‑MOR‑S06 (Object‑of‑talk).** Heads pass M‑2; no bare metaphors as heads.
* **RSCR‑MOR‑E01 (DevOps firewall).** Tool/file suffixes quarantined to Context; none leak into KernelToken names.
* **RSCR‑MOR‑E02 (USM compliance).** For each LexicalAct, verify `USM.Scope ∈ AllowedScopes(LEX.TokenClass)` (see § 7.5).

#### E.10:8.8 - Autonomy lexicon (L‑AUTO )
**Forbidden (Core):** bare “validity”, “actor/agent” (as free‑standing nouns), “kill switch”, “process” for behavior, “envelope” when used **as scope**.
**Use instead:** *Scope (G)* for epistemic scope; *WorkScope* for capability bounds; *RoleAssignment* for who acts; *SpeechAct* for overrides; *SafeStop* instead of “kill switch”.
**Named prefixes (policy & registry):**
* `aut:` for AutonomyBudgetDecl fields (e.g., `aut:action_tokens`, `aut:risk_bands`);
* `guard:` for guard checks bound to `AdmissibilityConditionsId`;
* `ovr:` for override SpeechActs (`ovr:PauseAutonomy`, `ovr:ResumeAutonomy`, …).

**Notes.**
1) Scope‑sensitive guards **must** declare the **Γ_time** window selector used for admission checks.
2) Proper names of patterns/components that already include “Agent/Agency” (e.g., *Agency‑CHR*, *Agent‑Tools‑CAL*) are permitted as **titled terms**; avoid re‑introducing “agent” as a free‑standing noun in new prose.

#### E.10:8.9 - LEX-CHR-STRICT — Reserve *Characteristic* for CSLC-measurable aspects

**Intent.** Prevent calling **non-measurable** objects (sets, statuses, scopes, policies, bridges, contexts, guards) “characteristics”.

**Rule L-CHR-S1 (Reservation).** Use **Characteristic** **only** for variables that **declare a CSLC scale** (nominal/ordinal/interval/ratio) with admissible values/units/polarity (Part C.16/A.17–A.18).
**Rule L-CHR-S2 (USM).** `U.Scope` / `U.ClaimScope (G)` / `U.WorkScope` are **USM scope objects**, not Characteristics; they **must not** appear in any `CharacteristicSpace`.
**Rule L-CHR-S3 (Status).** ESG/RSG statuses and deontic/epistemic statuses — **not Characteristics**; its statuses/states.
**Rule L-CHR-S4 (Lexical classifiers).** Lexical classifiers/tags — **Facets**/**attributes**; do not name them as Characteristics, if not declared **CSLC**.
**Checks.**
— **CC-L-CHR-1.** `scope characteristic(s)` is banned in Core/Context.
— **CC-L-CHR-2.** `CharacteristicSpace` near `Scope` — error.
— **CC-L-CHR-3.** Canonical rewrite: `F–G–R characteristics` → `F–G–R components`.

#### E.10:8.10 - LEX‑QA‑1 — Using “‑ility/‑ilities” terms (availability, reliability, …)

**Rule.** Tokens ending with **‑ility/‑ilities** or widely used quality names (**Availability, Reliability, Security, Safety, Scalability, Maintainability, Usability**, …) are **Quality‑Family labels**, not automatically CHR **Characteristics**.

**Authoring choice:**
— To use such a term as a **CHR** characteristic, **bind** it to a **named `U.Characteristic` with one CSLC Scale** (A.18) and refer to that Characteristic in guards/UTS;
— Otherwise **publish a Q‑Bundle** (see **C.25**) that includes **Measures (CHR)** (the measurable slots) and, where relevant, **Scope** (USM set over `U.ContextSlice`) and windows/mechanism/status fields.

**Rationale.** Scope is **set‑valued** (USM) and **not** a CHR measurement; mechanisms/statuses are governance records. Keeping them outside the CHR CSLC avoids illegal scalarisation and preserves set‑algebra semantics for scope. (A.2.6 § 6.2; A.6.1; C.16/A.18).


