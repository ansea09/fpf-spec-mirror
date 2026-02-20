   – Examples: `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ServiceEndpointSlot`, `CallerHolonSlot`, `MetricSlot`.
   – SlotKind is **structural**: it picks out **one distinguished place** in the argument/port/field list of a given relation, operator, record, or other signatured bundle; it does **not** name a “role” played by whatever fills the slot.
   – For an n‑ary relation/operator declared in a `U.Signature`, the pair *(Signature id, SlotKind)* identifies a **slot**; positional indices are merely a presentation‑level enumeration of these slots.
   – What a filler “does” in that place (its contribution to laws, constraints, effects) is governed by the **laws over the Signature** and by the corresponding ValueKind, not by SlotKind‑as‑“role”.

2. **ValueKind (kind of slot filler).**
   *Which kinds of things may fill this position in principle (at the intensional level).*
   – Examples: `U.Entity`, `U.Holon`, `U.Method`, `U.Episteme`, `U.ClaimGraph`, `U.Viewpoint`, `U.Characteristic`, `U.ReferenceScheme`.
   – ValueKind is a **Kind** (C.3.\*) or another kernel‑level type; it is **not** a slot and never carries `*Slot`/`*Ref` suffixes.

3. **RefKind (how we store / refer).**
   *What reference/identifier we actually store in episteme when we fill this slot.*
   – Examples: `U.EntityRef`, `U.HolonRef`, `U.MethodRef`, `U.EpistemeRef`, `U.ViewpointRef`, `U.SurfaceRef`, (optionally) `U.ClaimGraphRef` if a Context chooses to reference claim graphs rather than store them by value.
   – RefKind is **about references, not values**; it usually points to an editioned artifact (A.7, F.15) and carries the `.edition` field when pinning a phase.

**Discipline:**

* Each declared argument position in a `U.Signature` **MUST** be described by:

  * a SlotKind (name and documentation),
  * a ValueKind (type of permissible fillers),
  * and either a RefKind or an explicit declaration “**by‑value**” (no RefKind; the value is embedded).
* SlotKind and ValueKind are **intensional**; RefKind is **representational**. This mirrors I/D/S: *slot* describes structure, *value* describes what can sit there, *ref* describes how we point to concrete instances.

#### A.6.5:4.2 - Naming discipline: `*Slot` and `*Ref`

This pattern introduces the following **lexical constraints**, aligned with E.10:

1. **`*Slot` reserved for SlotKind.**

   * Any Tech name ending with `…Slot` **MUST** denote a SlotKind: a named place in a relation/morphism signature.
   * Examples:
     – `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`.
   * `*Slot` **MUST NOT** appear in names of:
     – ValueKind (e.g. `U.Entity`, `U.Holon`, `U.Method`),
     – RefKind (e.g. `U.EntityRef`),
     – concrete episteme fields (they may be named e.g. `describedEntityRef`, but not `describedEntitySlotField`).

2. **`*Ref` reserved for RefKind and reference fields.**

   * Any Tech name ending with `…Ref` **MUST** denote either:
     – a **RefKind** (type of references/identifiers), or
     – a **field** whose type is a RefKind (`describedEntityRef : U.EntityRef`).
   * `*Ref` **MUST NOT** appear in names of:
     – ValueKinds (e.g. `U.EntityRef` **cannot** mean “an entity”; it is a reference type),
     – SlotKinds,
     – Kinds themselves (`U.Kind`, `U.Entity`, `U.Holon`).

3. **ValueKind names carry no `*Slot`/`*Ref`.**

   * ValueKinds are named using standard FPF conventions (A/E/F, E.10), without `*Slot`/`*Ref`.
   * Examples: `U.Entity`, `U.Holon`, `U.Method`, `U.ClaimGraph`, `U.ReferenceScheme`, `U.Viewpoint`, `U.View`.

4. **No “Role” as SlotKind head.**

   * In the context of relation signatures, **do not** use “Role” as the head noun for SlotKinds (to avoid conflict with `U.Role`).
   * Use “Slot” or a neutral description: e.g. `EnactorHolonSlot` (ValueKind `U.Holon`) rather than `EnactorRoleSlot`.

These rules become part of the **LEX‑BUNDLE guards** and are enforced by F.18 / name‑acceptance harnesses.

#### A.6.5:4.3 - Integration with `U.Signature` (A.6.0)

`U.Signature` already provides a generic pattern for declaring morphism/relationship signatures (SubjectKind, BaseType, Quantification, ResultKind, Vocabulary, Laws).

`U.RelationSlotDiscipline` refines this by adding a **SlotSpec** layer:

*For each parameter position `i` in a signature*:

```
SlotSpec_i = ⟨name: SlotKind, value: ValueKind, refMode: {ByValue | RefKind}⟩
```

* **SlotKind** — Tech name with `*Slot` suffix, plus documentation.
* **ValueKind** — a `U.Type` (often a `U.Kind` or kernel type) declaring the intensional universe of admissible fillers.
* **refMode**:

  * `ByValue` — the actual value of ValueKind is embedded (typical for small structured values like `U.ClaimGraph` inside an episteme card).
  * `RefKind` — a **type** of references/identifiers for that ValueKind; e.g. `U.EntityRef` for `U.Entity`, `U.HolonRef` for `U.Holon`. Substitution then operates on references, not directly on the underlying values.

In practice, a `U.Signature` that follows this pattern:

* becomes **self‑documenting**: each parameter has a clear “slot vs value vs ref” story;
* supports **typed substitution**: replacing content within the same SlotKind requires only ValueKind compatibility;
* aligns with **tool signatures** in implementation languages (row‑typed records, dependently typed parameters, effect‑typed arguments). ([13])

#### A.6.5:4.4 - Typed substitution discipline

Given a relation or morphism `R` with signature Σ and SlotSpecs `{SlotSpec_i}`:

* A **substitution** at slot `i` is a change of the **slot content** that fills SlotKind_i, within or across episteme entries.
* `U.RelationSlotDiscipline` enforces:

1. **SlotKind invariance.**
   A substitution **never** changes SlotKind — only the slot content (Value/Ref).
   – “We put a different dataset into the `DatasetSlot`.”
   – “We switch the grounding holon in `GroundingHolonSlot`.”

2. **ValueKind compatibility.**
   The new content **MUST** be of the same ValueKind (or a declared subkind) as `SlotSpec_i.value`; Kind‑CAL governs this (`⊑` in C.3.1–C.3.2). If a Context uses EoIClass species constraints (C.3.2), those act as additional guards but do **not** change the SlotKind.

3. **RefKind correctness.**
   If `refMode=RefKind`, the stored field is of that RefKind; substitutions operate on references, not on underlying values. Edition pinning is handled as usual by `.edition` fields in F‑patterns (F.15, etc.).

4. **By‑value vs by‑ref awareness.**
   Substitutions at by‑value slots (e.g. `ClaimGraphSlot`) are **content edits** to the episteme or relation instance; they may affect formality F or assurance lanes. Substitutions at ref slots are **retargetings** of describedEntity or context, and their legality is governed by A.6.2–A.6.4 and Bridge/CL rules. Tooling SHOULD surface this difference explicitly in authoring surfaces (e.g. separate “Ref” vs “embedded content” columns).

These rules give a uniform way to say:

> “You may swap component X with Y in this slot, because they share ValueKind and pass the relevant Kind/Bridge constraints.”

#### A.6.5:4.5 - Slot operation lexicon (binding / filling / assignment / retargeting / mutation)

This subsection standardises **how Core and extensions talk about operations over slots**, without committing FPF to any particular programming language semantics. It is a *lexical* and *didactic* guardrail that preserves the SlotKind/ValueKind/RefKind stratification in prose.

##### A.6.5:4.5.1 - Four‑way separation: Identifier vs Slot vs Slot‑content vs Referent

*Diagram is illustrative; the term distinctions are normative.*

To avoid conflating “binding / assignment / passing / mutation”, FPF authors SHALL keep the following separation in mind:

```
(1) Identifier/Name  ──binds-to──>  (2) SlotKind  ──in an instance──>  (2′) Slot‑instance  ──filled-with──>  (3) Slot‑content (Value | Ref)
                                                              └─(if Ref) resolves-to──> (4) Referent value / artifact
```

**Normative terms**:

* **Identifier** (Surface): a name used in a syntax, table column, record field, port label, or parameter label.
* **SlotKind** (I‑plane): the signature‑level label for a distinguished place in a relation.
* **Slot‑instance** (S‑plane / representation): the actual location/cell/position corresponding to a SlotKind inside a specific relation instance, record, port bundle, or episteme card.
* **Slot‑content** (representation): what is stored in a slot‑instance. It is either:

  * a **by‑value value** of ValueKind, or
  * a **reference handle** of RefKind.
* **Referent**: the intensional thing the RefKind points to when resolved (often an editioned artifact).

This separation is the anchor for all “binding time” talk in A.6.5:4.6.

##### A.6.5:4.5.2 - Canonical verbs (Tech register) for slot operations *(normative)*

When a pattern, bridge, or operator description discusses a change or action “with respect to a slot”, it SHALL use (or explicitly map to) the following verbs. Each verb is tied to **which link/layer it affects**.

1. **bind / rebind** (Identifier → SlotKind/slot‑instance).
   *Use when the subject is an Identifier/Name and the effect is changing what that name designates.*
   – **bind**: establish a new association of an Identifier to a SlotKind/slot‑instance (or to a value in a language surface).
   – **rebind**: change an existing association of an Identifier to designate a different slot‑instance or different value.
   **Guard:** do not use “bind” to mean “write into a slot”. Binding is about *names*, not slots.

2. **fill** (Slot‑instance ← Slot‑content).
   *The generic, cross‑domain verb meaning “provide slot‑content for a slot‑instance”.*
   – Fill does **not** by itself imply first‑time vs update, nor by‑value vs by‑ref.
   – Use **fill** when discussing hardware slots, tuple coordinates, ports, record fields, or parameters uniformly.

3. **initialize** (first fill).
   *Use when the slot‑instance previously had no content.*
   – For `refMode=RefKind`: initialization sets the initial reference handle.
   – For `ByValue`: initialization sets the embedded initial value.
   **Guard:** do not call initialization “assignment” in normative text.

4. **assign / set / write / update** (subsequent fill; slot‑content replacement).
   *Use when a slot‑instance already has content and you replace it with new content.*
   – These verbs are allowed as near‑synonyms, but **SHOULD** be used consistently within one pattern family.
   **Guard:** when `refMode=RefKind`, prefer **retarget** (below) if the intent is “change what this ref points to”, not “edit content”.

5. **retarget** (Ref slot update, same SlotKind/ValueKind).
   *Use only for `refMode=RefKind` slots, when the operation replaces one reference handle with another, thereby changing the referent while preserving SlotKind and ValueKind.*
   – “Retarget `DescribedEntitySlot` from `UserService#staging` to `UserService#prod`.”
   Retargeting is the canonical FPF verb for “swap the referenced thing in this slot”.

6. **substitute** (typed replacement with explicit compatibility claim).
   *Use when the statement’s main point is the **compatibility law** (“allowed because ValueKind matches”).*
   – Substitute is a **discipline word**: it signals that SlotKind is fixed and ValueKind compatibility is being asserted/checked.

7. **resolve / dereference** (Ref → Referent).
   *Use when a reference handle is mapped to the intensional referent.*
   – This is where “late binding” often hides in runtime systems (dispatch, dynamic lookup, registry indirection).
   **Guard:** resolving a reference is distinct from retargeting the reference.

8. **mutate / modify** (Referent internal change; content unchanged).
   *Use only when the referent itself changes while the slot‑content (the reference handle) does not.*
   **FPF note:** In edition‑disciplined contexts, prefer to describe intentional change as **revise / re‑edition** + **retarget**, rather than “mutate”, because the Core treats editioned artifacts as stable per edition (A.7, F.15).

9. **pass** (parameter slot filling).
   *Use for method/service signatures when an argument fills a parameter slot at a call boundary.*
   – Passing is a specialised instance of **fill**, typically realised as parameter binding + slot filling in implementation languages. In FPF text, “pass into SlotKind” is acceptable if SlotKind names the parameter position.

##### A.6.5:4.5.3 - Canonical nouns *(normative)*

To prevent role metaphors from re‑entering slot talk:

* Use **slot‑content** (preferred) or **slot filler** for “the thing currently in the slot”.
* Avoid person/role metaphors such as **occupant** in normative writing. If a Context insists on using such a word in Plain register, it SHALL define it explicitly as a synonym for slot‑content and SHALL NOT derive role semantics from it.
* Use **target**/**referent** for what a Ref points to; use **retargeting** for changing the target by changing the Ref.
* Use **by‑value edit** (or **embedded content edit**) for changes to a `ByValue` slot such as `ClaimGraphSlot`.

##### A.6.5:4.5.4 - Operator naming guidance for slot‑writing operators *(normative, but intentionally lightweight)*

When naming an operator/morphism/bridge whose primary effect is a slot change, the Tech name SHOULD make two things legible:

1. **Which SlotKind(s) it writes**, and
2. **Which operation class it is**, using the canonical verbs above.

Recommended patterns (examples only; Contexts may adopt their own naming style via F.18):

* `Retarget<SlotQualifier>` for ref‑slot retargeting (e.g. `RetargetDescribedEntity`, `RetargetGroundingHolon`).
* `Edit<SlotQualifier>` / `Update<SlotQualifier>` for by‑value content edits (e.g. `EditClaimGraph`).
* `Substitute<SlotQualifier>` when the operator exists to enforce/declare ValueKind compatibility (e.g. `SubstituteDataset`).
* `Resolve<SlotQualifier>` when the operator is about resolving a Ref to a referent (e.g. `ResolveServiceEndpoint`).

This rule is a lexical enforcement of A.6.5:4.4 (typed substitution discipline): the name should tell the reader whether the operator is a **retargeting** (ref change) or a **content edit** (by‑value change).

#### A.6.5:4.6 - Binding time and “early vs late binding” *(normative framing, informative examples)*

In cross‑domain slot talk, “early binding / late binding” is meaningful only if the author states **which link is being fixed when**. Under A.6.5:4.5, there are three distinct “times” that writers must not conflate:

1. **SlotSpec time (signature time).**
   SlotKind / ValueKind / refMode are fixed when the `U.Signature` is declared. This is “early” by definition in FPF Core.

2. **Slot filling time (initialization / assignment / retargeting).**
   A particular relation instance / episteme card / parameter bundle acquires slot‑content for a SlotKind.
   – *Early‑filled* means: chosen at authoring/spec time (e.g. configuration pins a specific `U.HolonRef`).
   – *Late‑filled* means: chosen at runtime or late in a workflow (e.g. service endpoint selected by policy at deployment).

3. **Resolution / dispatch time (resolve RefKind; select referent).**
   Even if a ref handle is present, the referent may be resolved early or late.
   – *Eager resolution* means: resolve now, cache/commit to a referent.
   – *Lazy resolution* means: resolve on demand.
   – *Dynamic dispatch* is a special case: the “method slot” is resolved at call time based on a receiver/context, rather than being statically selected.

**Rule (lexical guard):**
Any use of “early binding” / “late binding” in Core or extensions SHALL specify which of the above it refers to, using one of:

* **early/late‑filled** (slot filling),
* **eager/lazy‑resolved** (resolution),
* **early/late name‑binding** (Identifier binding, if a language surface is being discussed).

This preserves the A.6.5 stratification and prevents importing accidental semantics from a specific programming language.

### A.6.5:5 - Archetypal Grounding (Tell‑Show‑Show)

Following E.7, we ground the pattern in a **System** example and an **Episteme** example.

#### A.6.5:5.1 - System example — authentication pipeline signature

Consider an `AuthPipelineSpecKind` (system‑level episteme describing an authentication pipeline for a microservice). Its key slots might be:

* `DescribedEntitySlot` — “which holon the pipeline is about”
  – ValueKind: `U.Holon` (EoIClass = “UserService system”).
  – RefKind: `U.HolonRef` (e.g. `UserService#prod`).

* `AuthProviderComponentSlot` — “which authentication provider component is selected”
  – ValueKind: `U.Holon` (EoIClass = “AuthProviderSystem”).
  – RefKind: `U.HolonRef` (e.g. `Auth_OIDC`, `Auth_LDAP`).

* `ClaimGraphSlot` — “what is asserted about the pipeline”
  – ValueKind: `U.ClaimGraph`.
  – refMode: `ByValue` (ClaimGraph stored inside the episteme card).

Substitutions / retargetings:

* **Retargeting** `AuthProviderComponentSlot` from `Auth_OIDC` to `Auth_LDAP`:
  – SlotKind fixed (`AuthProviderComponentSlot`).
  – ValueKind unchanged (`U.Holon`, `AuthProviderSystem ⊑ U.Holon`).
  – RefKind unchanged (`U.HolonRef`).
  – Semantically: “retarget the ref that fills the same slot”.

* **Retargeting** `DescribedEntitySlot` from `UserService#staging` to `UserService#prod`:
  – Same SlotKind and ValueKind.
  – Different `U.HolonRef` slot‑content.
  – May require different grounding and assurance episteme, but the slot discipline is identical.

#### A.6.5:5.2 - Episteme example — model evaluation result

Consider `ModelEvaluationResultKind` as an episteme kind:

* `DescribedEntitySlot` — the model being evaluated
  – ValueKind: `U.Method` (intensional ML model).
  – RefKind: `U.MethodRef` (id of `Model_v3`).

* `DatasetSlot` — the dataset on which it is evaluated
  – ValueKind: `U.Entity` (EoIClass = “Dataset”).
  – RefKind: `U.EntityRef` (e.g. `Dataset_A`, `Dataset_B`).

* `TargetCharacteristicSlot` — the characteristic being measured
  – ValueKind: `U.Characteristic` (`Accuracy`, `F1`, `AUROC`).
  – RefKind: `U.CharacteristicRef`.

* `GroundingHolonSlot` — evaluation environment
  – ValueKind: `U.Holon` (e.g. `EvalCluster#1`).
  – RefKind: `U.HolonRef`.

* `ClaimGraphSlot` — evaluation result graph
  – ValueKind: `U.ClaimGraph`.
  – refMode: `ByValue`; the numeric thresholds and results live inside `content : U.ClaimGraph`.

Typical moves:

* `DatasetSlot`: **retarget** `Dataset_A` → `Dataset_B` to test generalisation.
* `TargetCharacteristicSlot`: **retarget** `Accuracy` → `F1` to focus on class imbalance.
* `ClaimGraphSlot`: **by‑value edit** thresholds from “`P95Latency ≤ 200 ms`” to “`≤ 150 ms`” — a `ByValue` content edit, not a ref retargeting.

The SlotKind/ValueKind/RefKind discipline makes these moves **local and explicit**: the pattern describes which moves are allowed where, and A.6.2–A.6.4 then constrain how episteme morphisms may change ClaimGraphs and references.

#### A.6.5:5.3 - Didactic micro‑examples — substitution by SlotKind / ValueKind / RefKind *(informative)*

The following short examples are intended for a didactic guide or for cross‑references from A.6.0/A.6.x/C.2.1. In all of them:

* **SlotKind** names the **place/position in the structure** (slot/field/coordinate in a tuple/record/port bundle).
* **ValueKind** is the **kind of value** admissible at that place.
* **RefKind** is the **reference/identifier type** used in episteme when that slot is filled (absent when the slot is by‑value).
* `GroundingHolon` is **not** a separate kernel type: it is simply a `U.Holon` used as the ValueKind of `GroundingHolonSlot`.

Example names like `FurnitureSafetyDescriptionKind`, `AuthPipelineSpecKind`, `ModelEvaluationResultKind`, `IncidentRunbookSpecKind`, `ServiceSLARequirementKind` are **context‑local** kinds, not new kernel tokens.

##### A.6.5:5.3.1 - Mechanics — stool on a test rig

*EpistemeKind:* `FurnitureSafetyDescriptionKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — SlotKind “what this description is about”; ValueKind `U.Entity` with EoIClass ⊑ `U.Holon` (stool as a furniture holon); RefKind `U.EntityRef` (identifier of a concrete stool `S_i`).
* `GroundingHolonSlot` — SlotKind “where the test happens”; ValueKind `U.Holon` (test rig `LabRig_j`); RefKind `U.HolonRef`.
* `ClaimGraphSlot` — SlotKind for the internal content; ValueKind `U.ClaimGraph`; refMode `ByValue` (graph embedded in the episteme).

*Substitutions (all under the **same** SlotKinds):*

* Episteme `E₁`: `describedEntityRef = S_1`, `groundingHolonRef = LabRig_A`.
* Episteme `E₂`: `describedEntityRef = S_2`, `groundingHolonRef = LabRig_A` — **substitute another stool in the same `DescribedEntitySlot`** (different `U.EntityRef` slot‑content).
* Episteme `E₃`: `describedEntityRef = S_1`, `groundingHolonRef = LabRig_B` — **substitute another test rig in `GroundingHolonSlot`** while keeping the same object‑of‑talk.

In all three cases the SlotKinds (and ValueKinds) are stable; only the **Refs that fill those slots** change. This matches the engineering idiom “drop another module into the same slot”.

##### A.6.5:5.3.2 - Microservices — switching the authentication provider

*EpistemeKind:* `AuthPipelineSpecKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Holon` with EoIClass = “`UserService` holon”; RefKind `U.HolonRef` (e.g. `UserService#prod`).
* `AuthProviderComponentSlot` — SlotKind “which auth provider component is used in this pipeline”; ValueKind `U.Holon` with EoIClass = “`AuthProviderSystem` holon”; RefKind `U.HolonRef` (e.g. `Auth_OIDC`, `Auth_LDAP`).
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue` (pipeline invariants and flow logic).

*Substitutions / retargetings:*

* Episteme `Spec_OIDC`: `describedEntityRef = UserService#prod`, `authProviderComponentRef = Auth_OIDC`.
* Episteme `Spec_LDAP`: same `describedEntityRef = UserService#prod`, but `authProviderComponentRef = Auth_LDAP`.

Here SlotKind is identical (`AuthProviderComponentSlot`); ValueKind is “any auth‑provider holon”; the episteme change is purely a **retargeting** of the `U.HolonRef` slot‑content.

##### A.6.5:5.3.3 - Data/ML — swapping dataset or target characteristic

*EpistemeKind:* `ModelEvaluationResultKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Method`; RefKind `U.MethodRef` (e.g. `Model_v3`).
* `DatasetSlot` — ValueKind `U.Entity` with EoIClass = “dataset”; RefKind `U.EntityRef` (`Dataset_A`, `Dataset_B`, …).
* `TargetCharacteristicSlot` — ValueKind `U.Characteristic`; RefKind `U.CharacteristicRef`.
* `GroundingHolonSlot` — ValueKind `U.Holon`; RefKind `U.HolonRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`.

*Substitutions / retargetings:*

* `Eval_1`: `describedEntityRef = Model_v3`, `datasetRef = Dataset_A`, `targetCharacteristicRef = Accuracy`, `groundingHolonRef = EvalCluster#1`.
* `Eval_2`: same model / characteristic / cluster, but `datasetRef = Dataset_B` — **substitute another dataset in `DatasetSlot`** (retarget the dataset ref).
* `Eval_3`: same model and dataset, but `targetCharacteristicRef = F1` — **substitute another characteristic in `TargetCharacteristicSlot`**.

##### A.6.5:5.3.4 - Operational practice — the same runbook in different operating centres

*EpistemeKind:* `IncidentRunbookSpecKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Method`; RefKind `U.MethodRef`.
* `GroundingHolonSlot` — ValueKind `U.Holon`; RefKind `U.HolonRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`.

*Substitutions / retargetings:*

* `Runbook_DC1`: `describedEntityRef = MajorIncidentRunbook`, `groundingHolonRef = DC1_NOC`.
* `Runbook_DC2`: same `describedEntityRef`, but `groundingHolonRef = DC2_NOC`.

This is “one and the same method is specified and validated in two different operational environments”: SlotKind and ValueKind are stable; only the `U.HolonRef` slot‑content differs.

##### A.6.5:5.3.5 - SLO/SLA requirements — changing the target characteristic vs changing the threshold

*EpistemeKind:* `ServiceSLARequirementKind`.

*SlotKind / ValueKind / RefKind:*

* `DescribedEntitySlot` — ValueKind `U.Holon`; RefKind `U.HolonRef` (e.g. `CheckoutService#prod`).
* `TargetCharacteristicSlot` — ValueKind `U.Characteristic`; RefKind `U.CharacteristicRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`. Numeric thresholds live **inside the ClaimGraph as literals**, not as RefKinds.

*Moves:*

* `SLA_latency_200`: `describedEntityRef = CheckoutService#prod`, `targetCharacteristicRef = P95Latency`; ClaimGraph contains `P95Latency ≤ 200 ms`.
* `SLA_latency_150`: same refs, but ClaimGraph threshold is `P95Latency ≤ 150 ms`. This is a **by‑value edit** of `ClaimGraphSlot`.
* `SLA_availability_99_9`: same `describedEntityRef`, but `targetCharacteristicRef = Availability`; ClaimGraph states `Availability ≥ 99.9%`. This is a **retargeting** of `TargetCharacteristicSlot`.

### A.6.5:6 - Bias‑Annotation

**Lenses tested and scope.** This pattern was read through all five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`) and is intended as a **universal** discipline for n‑ary relation and morphism signatures across Parts A/B/C/E. It leans toward the `Arch` and `Onto/Epist` lenses (typed signatures, explicit kinds), but mitigates this by (a) keeping the discipline notation‑agnostic, (b) aligning with existing tooling rather than prescribing any, and (c) grounding the rules in System/Episteme examples with clear didactic intent. No domain‑specific scope limitation is claimed.

* **Typed‑language bias.**

  * The pattern leans on intuitions from typed programming languages (parameter types, records, references). This is intentional: it aligns FPF signatures with mainstream tooling and with post‑2015 typed effect/row systems. The pattern remains **notation‑agnostic** and does not commit to any specific PL or logic.

* **Slot‑first bias.**

  * We treat *slot* as the primary abstraction and discourage role‑style or object‑style naming for argument positions. This favours structural clarity over conversational metaphors (“subject/object/role”) and keeps `U.Role` free for RoleEnactment rather than param‑slots.

* **By‑value/by‑ref honesty.**
  We explicitly separate ValueKind and RefKind instead of hiding “by‑reference” behind the type system. This increases verbosity but makes reasoning about edition pinning, caching, and re‑targeting more robust, and keeps I/D/S distinctions visible inside signatures.

* **Lexicon bias (precision over metaphor).**
  We standardise the slot‑operation lexicon (bind/fill/initialize/assign/retarget/resolve/mutate) and discourage metaphors that smuggle role semantics back into SlotKinds. This increases didactic load, but directly reduces cross‑pattern ambiguity, especially in “binding time” discussions.

* **Episteme‑first describedEntity.**
  The examples and cross‑references prioritise episteme use‑cases (C.2.1, A.6.2–A.6.4) where describedEntity and retargeting are subtle. System‑only usages (e.g. method signatures) are absolutely allowed but not the driving case; they inherit the same discipline without additional obligations.

### A.6.5:7 - Conformance Checklist (normative)

**CC‑A.6.5‑1 - SlotSpec for every parameter.**
Every `U.Signature` that declares an n‑ary relation or morphism **SHALL** assign to each parameter position a SlotSpec triple: `⟨SlotKind, ValueKind, refMode⟩`.

**CC‑A.6.5‑2 - `*Slot` discipline.**
Any Tech name ending with `…Slot` **MUST** denote a SlotKind; SlotKinds **MUST NOT** be used as ValueKinds or RefKinds.

**CC‑A.6.5‑3 - `*Ref` discipline.**
Any Tech name ending with `…Ref` **MUST** denote either a RefKind or a field whose type is a RefKind. ValueKinds and SlotKinds **MUST NOT** end in `…Ref`.

**CC‑A.6.5‑4 - ValueKind purity.**
ValueKinds **MUST** be declared without `*Slot`/`*Ref` suffixes and **MUST** be FPF types (often `U.Kind` or kernel‑level types). Any existing type whose name violates this rule must be either:

* reclassified as a RefKind, or
* renamed to drop the suffix.

**CC‑A.6.5‑5 - Episteme core SlotKinds.**
For episteme kinds (`U.EpistemeKind`), the following SlotKinds **SHALL** be used (or their documented refinements) in C.2.1 / C.2.x:

* `DescribedEntitySlot` with ValueKind `U.Entity` **or a declared subkind** (e.g. `U.Method`, `U.Holon`) via Kind‑CAL (EoIClass ⊑ `U.Entity` at species level);
* `GroundingHolonSlot` with ValueKind `U.Holon`;
* `ClaimGraphSlot` with ValueKind `U.ClaimGraph` and `ByValue` mode in the minimal core;
* `ViewpointSlot` with ValueKind `U.Viewpoint`;
* `ViewSlot` with ValueKind `U.View` (`U.EpistemeView`);
* `ReferenceSchemeSlot` with ValueKind `U.ReferenceScheme` and `ByValue` mode in the minimal core.

**CC‑A.6.5‑6 - No “Role” as SlotKind head.**
SlotKinds **MUST NOT** use “Role” as their head noun; use “Slot” with a neutral qualifier instead (e.g., `EnactorHolonSlot`). `U.Role` remains reserved for RoleEnactment patterns.

**CC‑A.6.5‑7 - Substitution checks.**
Any pattern that describes substitution or replacement of arguments **MUST** phrase its rules in terms of SlotKinds and ValueKinds (and, where relevant, RefKinds), not in terms of unstructured parameter indices or ad‑hoc labels.

**CC‑A.6.5‑8 - Cross‑pattern consistency.**
When the same conceptual position is used across patterns (e.g. “describedEntity target”, “grounding holon”, “caller system”), the **same SlotKind name** and ValueKind **SHALL** be reused, unless a documented Bridge declares a different discipline or the pattern explicitly scopes itself to a distinct calculus.

**CC‑A.6.5‑9 - Migration of legacy `…Ref`/`…Slot` usage.**
Contexts adopting this pattern **MUST** maintain a migration table for legacy types/fields whose names contain `Ref` or `Slot` but do not comply with the new discipline. Each entry shall state:

* old name and role,
* new SlotKind/ValueKind/RefKind,
* whether the old name becomes an alias (deprecated) or is removed.

**CC‑A.6.5‑10 - Pattern integration.**
New or revised patterns in Part A/B/C/E that introduce n‑ary relations, morphisms, or signatures **SHALL** reference A.6.5 in their Relations section and attest that they follow SlotKind/ValueKind/RefKind discipline.

**CC‑A.6.5‑11 - Slot‑content terminology.**
Normative text that refers to “what is in a slot” **SHALL** use **slot‑content** (or **slot filler**) and **SHALL NOT** rely on role/person metaphors (e.g. “occupant”) unless explicitly defined as a strict synonym for slot‑content with no added semantics.

**CC‑A.6.5‑12 - Slot‑operation verb discipline.**
Any normative description of a change “to a slot” **MUST** specify which operation class it is (initialize vs assign/set vs retarget vs by‑value edit vs resolve vs mutate/revise), using the canonical verbs in A.6.5:4.5.2 or explicitly mapping local terms to them.

**CC‑A.6.5‑13 - Binding‑time clarity.**
Any use of “early binding / late binding” (or equivalent) **MUST** specify whether it refers to:

* Identifier binding (name‑binding),
* Slot filling (early/late‑filled),
* Reference resolution / dispatch (eager/lazy‑resolved).

### A.6.5:8 - Consequences

**Benefits**

* **Uniform language for arguments and for operations.**
  Any n‑ary relation (episteme, role, method, service, guard) can be described with the same SlotKind/ValueKind/RefKind triple **and** with a stable operation lexicon (fill/initialize/assign/retarget/resolve).

* **Safer substitutions.**
  Substitution, retargeting, and viewing laws (A.6.2–A.6.4) can be stated in terms of *which SlotKinds* they read/write and *which ValueKinds* they preserve or retarget, without accidentally collapsing into “just replace the thing”.

* **Cleaner naming and migration.**
  Misuses of `*Ref`, `*Slot`, “Role”, “Subject”, “Object” in signatures become guard‑detectable; migration strategies can be described as re‑factoring SlotKinds and ValueKinds rather than ad‑hoc renames.

* **Tool alignment.**
  Implementation languages with **row‑typed records, dependent types, and algebraic effects** map naturally to the SlotKind/ValueKind/RefKind layers, easing code generation and static analysis. ([13])

**Trade‑offs / mitigations**

* **Extra metadata in signatures.**
  Every parameter now has three pieces of information instead of one. Mitigation: template support in authoring tools; pattern‑guided macros for common shapes (episteme, role, method, service).

* **Stricter lexical rules.**
  Some legacy names will need migration (`EpistemicObject`, ad‑hoc `…Ref` types). Mitigation: migration notes in F.18 and dedicated anti‑pattern sections; transitional aliases allowed but marked deprecated.

* **Learning curve.**
  Authors must learn to think “SlotKind/ValueKind/RefKind” *and* distinguish “retarget vs edit vs resolve” before writing `id` or `subject`. Mitigation: Tell‑Show‑Show examples and a didactic micro‑guide on slot operations referenced from A.6.0/C.2.1/E.17.0.

### A.6.5:9 - Rationale

**Why a SlotKind/ValueKind/RefKind triple at all.**
In FPF this pattern makes `U.Signature` behave like a lightweight dependently‑typed record discipline: SlotKind plays the role of an index or label, ValueKind is the family of admissible fillers at that position, and RefKind captures the representation choice (by‑value or via a handle). This mirrors the way post‑2015 work on row‑polymorphic data and effect rows treats labels and field kinds as first‑class, while keeping the Core notation‑neutral.

**Why separate ValueKind from RefKind.**
In practice, “Ref” types tend to be quietly used as if they were values, eroding the I/D/S split and making edition discipline invisible. By insisting that ValueKind is always the conceptual kind (“what sort of thing is this about?”) and RefKind is always the reference/identifier kind (“how do we point at it in Episteme?”), the pattern aligns with E.10.D2’s intension/description/specification discipline and with modern resource‑aware logics that keep values and resources distinct.

**Why add a slot‑operation lexicon.**
The triple only buys safety if authors and tools can see it at a glance **and** can narrate changes without collapsing layers. A.6.5:4.5 makes the common “put something in a slot” moves explicit: initialization vs assignment vs retargeting vs by‑value editing vs resolution. This directly reduces ambiguity in episteme morphism descriptions (A.6.2–A.6.4) and prevents accidental imports from a specific PL’s terminology.

**Why standardise episteme SlotKinds.**
describedEntity and grounding recur across epistemes; standard SlotKinds (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, etc.) let A.6.2–A.6.4 and C.2.1 talk about substitutions and retargetings once, instead of re‑defining “what this is about” in every pattern.

**Why lexical rules (`*Slot`, `*Ref`, operation verbs, no “Role” heads).**
The discipline must be cheap to apply. Reserving `*Slot` for SlotKinds and `*Ref` for RefKinds/fields gives a syntax‑level guard against conflating places, kinds, and handles. Standardising operation verbs (initialize/retarget/resolve) prevents prose from re‑introducing the same conflation by different words.

### A.6.5:10 - SoTA‑Echoing (post‑2015 practice alignment)

**Purpose.** To situate SlotKind/ValueKind/RefKind discipline with respect to contemporary typed and relational approaches, without importing any external calculus into the Core. All items are used as conceptual comparators; concrete reuse in a `U.BoundedContext` would happen only via explicit Bridges (F.9) with declared CL penalties.

1. **Row‑typed, extensible data / effect rows (adopt/adapt).**
   Post‑2015 work on row polymorphism and extensible data/effect rows treats records and variants as labelled collections of fields whose presence and type can evolve independently.
   **Adopted:** the idea that **positions** (labels) are first‑class and carry their own typing discipline.
   **Adapted:** instead of row kinds, FPF uses SlotKind/ValueKind/RefKind triples for n‑ary relations and epistemic slots; the pattern is notation‑agnostic and applies equally to episteme structures, role relations, and service signatures. ([13])

2. **Dependent type systems engineered via macros (adopt/adapt).**
   Macro‑based dependent type systems such as Turnstile+ separate structural indices, value‑level types, and evidence, while allowing them to be related by construction.
   **Adopted:** the separation between **indices/labels** and **values**, and the intuition that signatures should expose both explicitly.
   **Adapted:** SlotKind corresponds to a structural index, ValueKind to the ordinary type of fillers, and RefKind to runtime‑level identifiers; the discipline is phrased at the FPF specification and kept independent of any particular PL.

3. **Relational models of types‑and‑effects (adapt).**
   Relational models for types‑and‑effects distinguish value positions from effect/resource annotations and track substitution separately across these layers.
   **Adopted:** the insistence that reasoning about **substitution and equality** must be stratified (values vs additional structure).
   **Adapted:** A.6.5 stratifies *slot / value / reference* instead of *value / effect*, and applies the discipline not only to programs but also to epistemes, roles, methods, and services. ([15])

4. **Optics / lenses as disciplined projections (echo).**
   Profunctor optics formalise get/put pairs where a fixed “focus” position within a larger structure is manipulated under composition laws.
   **Echoed:** SlotKind plays the role of the focus coordinate; ValueKind is the focus type; RefKind determines whether the focus is stored by value or via a handle. This perspective informs later use of SlotKind discipline in EpistemicViewing (A.6.3) and multi‑view publication (E.17). ([16])

**Cross‑Context reuse and Bridges.** When a `U.BoundedContext` chooses to adopt a concrete row‑typing discipline, relational logic, or optics library, it **SHALL** do so via explicit Bridges (F.9) with CL and (for plane crossings) `Φ(CL)`/`Φ_plane` policy‑ids, keeping numerical policies and notations Context‑local. A.6.5 only constrains the **slot discipline** that such Bridges must respect.

### A.6.5:11 - Relations (with other patterns)

**Specialises A.6.P `U.RelationalPrecisionRestorationSuite`.**
A.6.5 is the RPR specialisation for “n‑ary relation as slots”: it restores hidden arity by making participant positions explicit as SlotKinds, and stabilises change semantics via the slot‑operation lexicon + lexical guards.


**Builds on A.6.0 `U.Signature`.**
Refines parameter declarations with SlotSpec triples `⟨SlotKind, ValueKind, refMode⟩` while leaving the rest of the signature structure (SubjectKind, BaseType, Quantification, ResultKind, Laws) unchanged. SlotKinds become the canonical labels for argument positions.

**Constrains C.2.1 `U.EpistemeSlotGraph`.**
Fixes core episteme SlotKinds (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) and their ValueKinds/`ByValue` vs Ref discipline. C.2.1 and its extensions SHALL use these SlotKinds (or documented refinements) so that episteme morphisms can be expressed uniformly over slots.

**Supports A.6.2–A.6.4 (episteme morphisms and viewing).**
DescribedEntity‑preserving vs describedEntity‑retargeting morphisms can now be stated as constraints on which SlotKinds’ ValueKinds/RefKinds they may change. Retargeting becomes “retargeting at `DescribedEntitySlot` under a Kind‑Bridge” rather than an ad‑hoc parameter tweak. The operation lexicon in A.6.5:4.5 makes “retarget vs edit vs resolve” explicit in these morphism descriptions.

**Coordinates with B.5.* (RoleEnactment).**
Role/assignment relations may declare SlotKinds such as `HolderHolonSlot`, `RoleSlot`, `ContextSlot`, `WindowSlot` with clear ValueKinds/RefKinds, instead of overloading “role” for both holonic roles and relation positions. This keeps `U.Role` semantics (A.2, F.6) separate from slot discipline.

**Coordinates with E.17 `U.MultiViewDescribing`.**
`Viewpoint` and `View` positions are governed by SlotKind/ValueKind/RefKind; view‑changing operations can be described as substitutions at specific SlotKinds that preserve ClaimGraph content while re‑indexing viewpoints and views.

**Feeds F.18 (LEX‑BUNDLE) and E.10 (LEX).**
Provides lexical guards for `*Slot` and `*Ref`, and (via A.6.5:4.5) for operation verbs:

* `*Slot` reserved for SlotKinds only;
* `*Ref` reserved for RefKinds and reference fields;
* ValueKinds and Kind names MUST NOT carry either suffix;
* slot‑operation verbs must not collapse retargeting into “editing”.

**Used by A.19 `CharacteristicSpace` and measurement patterns.**
Characteristic‑space slots already behave as positions with attached kinds; slot discipline in A.6.5 gives a uniform story for how such slots appear inside relation signatures, episteme cards, and service definitions, and how substitution over those slots is checked.

[13] https://dl.acm.org/doi/pdf/10.1145/3290325
[14] https://www.williamjbowman.com/resources/wjb2019-depmacros.pdf
[15] https://iris-project.org/pdfs/2017-popl-effects-final.pdf
[16] https://arxiv.org/pdf/1809.00738

### A.6.5:End

## A.6.6 - U.BaseDeclarationDiscipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)

**Plain-name.** Scoped witnessed base declaration discipline.

**Status.** Normative (Core).

**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; adjacent to A.6.5 `U.RelationSlotDiscipline`.

**Depends on.**
– A.6.0 `U.Signature` (universal signature carrier).
– A.6.5 `U.RelationSlotDiscipline` (SlotKind/ValueKind/RefKind stratification + slot-operation lexicon).
– A.2.6 (Scope discipline; explicit `Γ_time`; implicit “latest/current” is forbidden).
– A.2.4 `U.EvidenceRole` (timespan + evidence-role discipline for decision-relevant witness sets).
– A.7 (Strict Distinction; I/D/S vs Surface).
– E.8 (pattern authoring order & SoTA discipline).
– E.10 (LEX‑BUNDLE discipline; D.CTX lexical guardrails).

**Coordinates with.**
– A.10 Evidence–Provenance DAG discipline (`verifiedBy`, `validatedBy`).
– A.14 per-edge constructive grounding (`tv:groundedBy`) and `validationMode` discipline.
– C.2.1 `U.EpistemeSlotGraph` grounding slots (`GroundingHolonSlot`, `describedEntity`).
– A.6.3 `U.EpistemicViewing` (describedEntity-preserving view operators; base-relative “how” without retargeting).
– A.6.4 `U.EpistemicRetargeting` (base-change along `KindBridge`; retargeting lexicon and continuity rules).
– C.3.3 `U.KindBridge` & `CL^k` (explicit repair/translation when endpoint kinds or Contexts differ; no silent re-typing).
– E.18 assurance-operations on `U.Transfer` (`CalibrateTo`, `CiteEvidence`, `AttributeTo`, `ConstrainTo`, …).
– F.9 Bridges & CL (cross-context / cross-plane base declarations cite Bridge ids + CL policy).
– F.15 F‑Suite validation harness (SCR/RSCR pins and refresh governance).
– F.18 naming governance (surface rules for Tech/Plain twins).

**Aliases (informative; discouraged for normative prose).**
– “anchoring / anchor” (legacy umbrella colloquial; a red‑flag token for *under-described dependence*). **Prohibited in Tech register** as a meaning‑surrogate; treat it as a defect to be rewritten into an explicit `baseRelation(dependent, base)` form. Allowed only when referring to a **pattern-defined primitive** that already reserves the word (e.g., E.10 MG‑DA *Domain Anchoring*; evidence/pin “anchors” where the term is explicitly reserved), or inside quoted legacy text that is immediately followed by a conformant rewrite.
– “Qualified statement / attributed edge” (knowledge-graph colloquial).
– “Pinning” (when witnesses are edition pins).

**Mint‑or‑Reuse note (informative).**
This pattern **mints** the record shape name `U.ScopedWitnessedBaseDeclaration` (SWBD) and the **base‑change lexicon** operation class names (`declareBase`, `rebase`, `retime`, …) as canonical labels for semantic change classes.
It **reuses** A.6.5 SlotSpec discipline (SlotKind/ValueKind/RefMode), A.2.6 Scope discipline (`U.Scope`, explicit `Γ_time` when time matters), and A.2.4 witness semantics (`U.EvidenceRole`) as the enforcement substrate.

### A.6.6:1 - Problem frame

FPF repeatedly needs to express a family of situations of the form:

> **A dependent content is admissible, usable, or interpretable only relative to an explicit base.**

This family appears across disciplines:

* reference selection and identification (IDs, handles, pointers, registries),
* scale/datums/calibration (measurement traceability, baselines, normalisation),
* grounding of properties and abstractions to objects (attribution; “this property is about that thing”),
* admissibility/assurance (claims linked to evidence, checks, or proofs),
* publication discipline (what a statement is fit to be used for, where, and when).

In drafts, authors often reach for a single umbrella metaphor (frequently “anchor/anchoring”). That metaphor collapses **different ontological situations** and **different operation classes**, blocking precise invariants and making perspective-flips inevitable.

> **Deconfliction note (lexical).** This pattern is about *base-dependence in content* (“X is usable relative to B”). It is not about E.10’s **Domain Anchoring** (MG‑DA), where “anchoring” is a *lexical* primitive meaning “object‑of‑talk anchoring” for token morphology. When you see `anchor*` in a basedness sentence, treat it as a defect unless an explicit baseRelation token is present.
>
> **Deconfliction note (context/meaning).** This pattern is also not a license to reintroduce “anchor” as a surrogate for **Context**, **SenseCell**, or “where meaning lives”. Any such use is an *anchor‑relapse* and SHALL be rewritten into explicit Context/SenseCell/ConceptSet lane constructs (E.10 D.CTX), not into SWBD.

Like A.6.5, this family also triggers **typing conflicts across viewpoints**: an endpoint may be spoken about in its self-kind while the baseRelation contract expects a different ValueKind (or a different `refMode`). If that mismatch is not made explicit (SlotSpec + contract), authors “solve” it by renaming ends or flipping direction, and the ontological obligation (bridge / narrowing / retargeting) is lost.

The structural reason for the collapse is consistent: what looks like “one anchoring” in prose is, in fact, a *based declaration* with at least five components:

1) **Dependent** — what is being made admissible/usable/meaningful,
2) **Base** — what it is relative to (reference frame / evidence carrier / standard / policy / object),
3) **BaseRelation** — the specific relation kind that states *how* dependent depends on base,
4) **Scope/Time** — where/when the declaration holds (`scope` plus explicit `Γ_time` when time matters),
5) **Witnesses / pins** — what justifies or enforces the declaration when it is used for decisions.

Until **BaseRelation** is named, umbrella words (“anchor”, “ground”, “attach”, “based on”) nearly always mean:

> “There is an under-described type of dependence here.”

This pattern introduces a single stable lens — **the based declaration** — and couples it with a strict lexical discipline and an operation lexicon, so that base-dependence can be expressed precisely across domains without collapsing back into metaphor.

### A.6.6:2 - Problem

Typical failure modes this pattern is designed to eliminate:

1. **Relation-kind elision.**  
   One verb phrase is used to cover: ID-to-registry reference, claim-to-evidence admissibility, calibration-to-standard, property-to-object attribution, policy gating, etc. Rules and invariants cannot be stated because the relation family is unspecified.

2. **Perspective flip (dependent-view vs base-view).**  
   The same situation is described alternately as “X is anchored/grounded” and “Y is an anchor/ground”, with incompatible naming, hidden directionality, and silent re-typing of the ends.

3. **Base–witness confusion.**  
   Evidence, pins, certificates, or proofs are treated as “the base”, even when they are only witnesses for a base relation (or conversely: a true base is treated as a mere witness).

4. **Scope/time collapse.**  
   Based declarations are treated as timeless truths; time dependence is smuggled in via “current/latest/recently”, violating explicit `Γ_time` discipline.

5. **`Γ_time` used as a proxy for freshness.**  
   Authors treat `Γ_time` as “freshness” or “evidence decay”, collapsing TimePolicy with witness-timespan/freshness predicates.

6. **Decision use without witnesses.**  
   Declarations that gate work, publication, or assurance are asserted without a witness/pin, breaking auditability and enabling folklore.

7. **Grounding conflation.**  
   “Grounding” is used as if it were one relation, while FPF already distinguishes at least:
   * constructive grounding of a model-edge by a trace (`tv:groundedBy`),
   * situational/empirical grounding of an episteme via a grounding holon (C.2.1),
   * semantic meaning assignment (SenseCell/ConceptSet lane; not a base declaration).

8. **Slot/basing conflation.**  
   A.6.5 disambiguates positions in n-ary relations (SlotKind) vs fillers (ValueKind) vs stored references (RefKind). Umbrella basing language reintroduces confusion at the next layer: “why this link exists” (BaseRelation) is missing, and slot-edit operations are conflated with base-declaration edits.

9. **Anchor relapse (Context/meaning surrogate).**  
   “Anchor/anchoring” is used to mean “the context”, “the meaning”, “the global reference”, or “the thing that makes this true”. This collapses D.CTX + SenseCell/ConceptSet lanes into a metaphor and makes review/tooling impossible.

### A.6.6:3 - Forces

| Force | Tension |
| --- | --- |
| **Universality vs precision** | One discipline must cover calibration, evidence linking, reference selection, attribution, gating, etc., without collapsing them into one pseudo-relation. |
| **Minimal kernel vs decision auditability** | Few primitives are preferred, but decision-relevant declarations must carry witnesses/pins and explicit time selectors where needed. |
| **Two perspectives, one reality** | Dependent-view and base-view must both be expressible without renaming roles or flipping meaning. |
| **Compatibility with A.6.5** | Base declarations introduce slots and edits; they must remain SlotKind/ValueKind/RefKind disciplined and must not collapse slot edits with semantic re-declarations. |
| **Lexical guardrails** | Without strict wording rules, umbrella metaphors will return and erase the structure. |
| **Cross-context integrity** | When dependent and base cross Contexts or planes, the declaration must remain explicit and reviewable; no silent semantic drift. |

### A.6.6:4 - Solution — The `U.ScopedWitnessedBaseDeclaration` object and its lexicon

#### A.6.6:4.1 - Canonical object

**Definition.** A **`U.ScopedWitnessedBaseDeclaration`** (SWBD) is a first-class base-declaration record *shape* (a signature in the A.6.0/A.6.5 sense): it reifies “dependent is usable relative to base via baseRelation, under scope/time, witnessed by pins”.

```
U.ScopedWitnessedBaseDeclaration ::=
  〈 * DependentSlot     : SlotContent(VK_dep,  refMode_dep),
    * BaseSlot          : SlotContent(VK_base, refMode_base),
    * BaseRelationSlot  : SlotContent(U.NameToken, ByValue),     // contract-bearing token; not free text; not U.Surface*
    * ScopeSlot         : SlotContent(U.Scope, ByValue),         // concretely: ClaimScope | WorkScope | PublicationScope
    * GammaTimeSlot?    : SlotContent(U.GammaTimePolicy, ByValue)?,
    * WitnessSetSlot?   : SlotContent(VK_wit,  refMode_wit)? 〉
 ```

Where:

* **`DependentSlot`** is the dependent content whose admissibility/usability/interpretation is being constrained.
* **`BaseSlot`** is the base (reference frame / target / object / standard / policy / evidence-carrier) that the dependent is declared relative to.
* **`BaseRelationSlot`** is a **declared relation/predicate/operator token** (a vocabulary element with a signature/contract) that states the precise kind of dependence. It is not a prose metaphor and is not a `U.Surface`/publication carrier.
* **`ScopeSlot`** is an explicit USM scope object (`U.Scope`): Claim scope (**G**), Work scope, or Publication scope.
* **`GammaTimeSlot`** is an explicit time selector/policy when time-dependent assumptions exist.
* **`WitnessSetSlot`** is a set of witness references/pins establishing justification or enforcement when the declaration is used for decisions.

**Notation.** `SlotContent(VK, refMode)` is a compact shorthand for “a slot whose SlotSpec declares `ValueKind=VK` and `refMode ∈ {ByValue | RefKind}` (A.6.5)”.

**SlotSpec note.** `VK_*` / `RK_*` / `refMode_*` above are **not** “anything goes”: they are fixed by the chosen `BaseRelationSlot` contract and must be declared as SlotSpecs (A.6.5). In other words, SWBD is a reusable *shape*, but each Context’s baseRelation family makes it a concrete, typed signature.

**Instance/prose notation note (convention).** In the prose and examples below, the *occupants* are written as `dependent`, `base`, `baseRelation`, `scope`, `Γ_time`, `witnesses` (no `*Slot` suffix). The `*Slot` suffix is reserved for SlotKinds/positions only (A.6.5 / E.10).

**Well-formedness constraints.**
* **WF‑BD‑1 (No kind-elision).** A base declaration is well-formed only if `BaseRelationSlot` is present and points to a declared vocabulary element with a known signature.
* **WF‑BD‑2 (No silent re-typing).** `DependentSlot` and `BaseSlot` type-check against the `baseRelation` contract (ValueKinds + `refMode`). If the intended endpoint kinds do not match, the repair path is explicit (Bridge / narrowing / explicit retargeting), rather than a rename.
* **WF‑BD‑3 (Time explicit when time matters).** If the declaration’s interpretation depends on time, `GammaTimeSlot` is explicit; “latest/current” is not a substitute.
* **WF‑BD‑4 (Decision use requires witnesses).** If the declaration is used for assurance, gating, or admissibility decisions, `WitnessSetSlot` is non-empty and resolvable.
* **WF‑BD‑5 (Edition fence for decision/publication).** An SWBD that is cited by PublicationScope or used for decision is immutable per edition: any permitted change class is represented as a new declaration linked via explicit continuity/withdrawal, not as an in-place rewrite.
* **WF‑BD‑6 (No silent cross-context reuse).** An SWBD that relates dependent and base across Contexts/planes (or requires scope translation) is admissible only if it cites the Bridge ids + CL policy that make the reuse admissible (F.9). No “it’s the same thing anyway” prose is an admissible substitute.

This is the discipline-level analogue of A.6.5’s move: disambiguation is achieved by making the missing structural component explicit and non-optional in decision-relevant contexts.

#### A.6.6:4.2 - Underlying mathematical lens

SWBD reifies a **kind-labelled dependence arrow over a base**:

* a dependence edge **(dependent → base)**,
* labelled by a declared **relation token** (`baseRelation`),
* qualified by explicit **scope** and (when time matters) explicit **`Γ_time`**,
* optionally supported by a **witness set** (mandatory for decision use).

This “object over a base” lens is stable across disciplines:
calibration is “measurement over standard”, admissibility is “claim over evidence”, attribution is “property over object”, and constructive grounding is “edge over trace”.

#### A.6.6:4.3 - Slot discipline for SWBD

Any signature that introduces SWBD (or SWBD-like relations) SHALL define SlotSpecs per A.6.5: every position declares **SlotKind / ValueKind / RefKind-or-ByValue**.

Recommended canonical SlotKinds for SWBD:

* `DependentSlot`
* `BaseSlot`
* `BaseRelationSlot`
* `ScopeSlot`
* `GammaTimeSlot`
* `WitnessSetSlot`

**Slot vs filler guard.** `*Slot` names the **position** (SlotKind), not the occupant. In prose, say “fills `BaseSlot` with …” rather than calling the base itself “a BaseSlot”. (`Slot` suffix is structural; E.10.)

**Slot-level invariants (derived from WF‑BD‑1..4; testable).**
* **Invariant (SlotSpec completeness).** In any SWBD signature, the SlotSpec for `DependentSlot` and `BaseSlot` declares admissible `ValueKind` and `refMode` explicitly (A.6.5). If those types cannot be stated, the `baseRelation` contract is not yet defined.
* **Invariant (Relation tokenness).** `BaseRelationSlot` holds a declared `U.NameToken` that resolves to a vocabulary entry with a known signature/contract (A.6.0 + A.6.5). It is not free text and is not typed as a publication surface (`U.Surface*`).
* **Invariant (Scope objectness).** `ScopeSlot` holds a `U.Scope` object (ClaimScope/WorkScope/PublicationScope) and is not replaced by “where it applies” prose.
* **Invariant (Time gating).** If time-dependent assumptions exist, the SWBD includes `GammaTimeSlot` carrying a `U.GammaTimePolicy` (WF‑BD‑3).
* **Invariant (Witness gating).** If the declaration participates in assurance/gating/admissibility decisions, the SWBD includes a non-empty, resolvable `WitnessSetSlot` (WF‑BD‑4).

**Field naming guard (implementation; informative).** When materialising SWBD as a record/card, implementations SHOULD avoid naming data fields with the `*Slot` suffix. Prefer `dependentRef`, `baseRef`, `baseRelationRef`, `scope`, `gammaTime`, `witnesses` (or Context‑local equivalents). `*Slot` remains reserved for SlotKinds/SlotSpecs (A.6.5).

#### A.6.6:4.4 - BaseRelation contract

A `baseRelation` token is not “just a label”. For each baseRelation declared in a Context, its definition SHALL include:

* **Role polarity.** Which end is dependent and which end is base (or declare symmetry explicitly).
* **Typing expectations.** Admissible ValueKinds and `refMode` for `DependentSlot` and `BaseSlot`.
* **Token discipline (LEX).** The token SHALL satisfy E.10 token-class morphology for relations/verbs; it SHALL NOT use metaphor heads (`Anchor*`, `Ground*`, `Attach*`) as a meaning-surrogate. If a legacy synonym exists, record it as an alias but keep the contract-bearing token specific.
* **Repair path for mismatches.** If an endpoint’s self-kind does not match the expected ValueKind, the allowed repairs are declared (KindBridge, explicit narrowing, or explicit retargeting); “renaming the endpoint” is not a repair.
* **Parameter placement.** Any additional qualifiers required by the relation kind (ranges, metrics, reference planes, policies) SHALL be represented either inside `scope` (preferred) or as explicit additional slots in an extended base-declaration signature; they MUST NOT be smuggled as adjectives on the endpoints.
* **Scope class.** Whether the declaration is claim-scoped (**G**), work-scoped, or publication-scoped.
* **Time discipline.** Whether `Γ_time` is required, optional, or forbidden for this relation kind.
* **Witness discipline.** Whether witnesses are always required vs required only for decision use, and what witness classes are admissible (`U.EvidenceRole`, edition pins, calibration cert pins, proof artefacts, policy pins).
* **Admissible change classes.** Which base-change operations are permitted (below) and what continuity requirements apply.
* **Cross-context / cross-plane policy.** Whether this baseRelation family may cross Contexts/planes at all; if yes, what Bridge ids/CL thresholds must be cited and what loss notes are required (F.9 / C.3.3).

This mirrors A.6.5: a SlotKind without ValueKind/RefMode is underspecified; a baseRelation without its contract is equally underspecified.

#### A.6.6:4.4.1 - Perspective/voice discipline (dependent-view vs base-view)

**Normative rule.** In Tech / normative prose, authors SHALL express a based declaration in one of the following explicit forms:

* `baseRelation(dependent, base)` (functional notation), or
* `dependent --baseRelation--> base` (arrow notation).

Authors SHALL NOT use passive/umbrella voice (“X is anchored/grounded/attached”) as a substitute for an explicit `baseRelation(dependent, base)` form, because it invites direction flips and silent re-typing.

**Base-view is allowed only if the polarity is preserved.** If authors use base-view wording (“B validates X”), they SHALL either (i) keep both endpoints visible using the same polarity-preserving token (e.g., `validatedBy(X,B)`), or (ii) use an explicit inverse token that is declared in the baseRelation contract. Authors SHALL NOT flip roles implicitly in prose.

#### A.6.6:4.5 - Lexical discipline

**Normative lexical rule.** In Tech / normative prose and Tech register naming, authors MUST NOT use umbrella metaphors (“anchor/anchoring”, “attach/attachment”, “ground/grounding”) as substitutes for an explicit `baseRelation` token.

**Red-flag rule (`anchor*` as dependence metaphor).**
* In **Tech / normative** prose: authors MUST treat `anchor*` as **prohibited** as a meaning-surrogate for an unnamed dependence kind. Authors SHALL rewrite into explicit `baseRelation(dependent, base)` form (or move to the correct reserved primitive lane).
* In **Plain / legacy** commentary only: authors MAY quote `anchor*` as a legacy umbrella *only if* it is immediately paired with an explicit baseRelation token (e.g., “legacy ‘anchored’ ⇒ `validatedBy(...)`”) and does not introduce a new contract-bearing token.

**Carve-outs (pattern-defined primitives).** This red-flag rule does **not** ban uses where “anchoring” is already a *pattern-defined primitive* elsewhere in the spec (e.g., E.10 MG‑DA “object‑of‑talk anchoring”, or A.10 evidence “anchors”). It still acts as a review trigger: confirm you are using the reserved sense, not smuggling a basedness meaning.

**Naming guard for baseRelation tokens.** Do not mint new baseRelation tokens whose head noun is a metaphor (`Anchor*`, `Ground*`, `Attach*`). If you are tempted to do so, you either (i) have not named the relation kind yet, or (ii) are introducing a legacy alias that must map onto an existing, more specific relation family.

Instead:
1) Name the **BaseRelation token** (declared vocabulary element), and
2) Use a **relation-specific verb phrase** that corresponds to that token.

**Lane guard for meaning.** If the intent is “attach meaning to a term”, do not introduce a baseRelation named `Anchor…` or `Ground…`. Use SenseCell/ConceptSet discipline; semantic meaning assignment is not expressed by SWBD.

**Grounding disambiguation rule.** If the prose says “grounded”, it MUST be rewritten into one of:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* meaning lane (SenseCell/ConceptSet; not SWBD).

**Bind deconfliction note.** Authors MUST NOT use the verb “bind/binding” as a synonym for declaring/refreshing/changing a base declaration. “bind/binding” is reserved for **name binding** (LEX discipline). For SWBD edits, authors SHALL use the base‑change lexicon (below) instead.

#### A.6.6:4.6 - Base-change operation lexicon

As A.6.5 distinguishes slot operations by whether they change a stored reference, resolve a reference, or replace a value, A.6.6 distinguishes **base declaration changes** by which component changes and what semantics are affected.

Operation classes (conceptual):

These names denote **semantic change classes**. In decision/publication lanes, implementations MUST represent these changes by minting a new SWBD (new id/edition) and linking it to the prior one via explicit continuity/withdrawal (WF‑BD‑5 / CC‑BD‑10), rather than mutating the old record.

1. **declareBase** — create a new base declaration with explicit `dependent`, `base`, `baseRelation`, `scope`, and, when applicable, `Γ_time`, plus witnesses when decision-relevant.
2. **withdrawBaseDecl** — retire a declaration (or render it inapplicable by scope narrowing or time restriction, depending on baseRelation contract).
3. **rebase** — change `base` while keeping the same `dependent` and `baseRelation` (legality depends on the baseRelation contract; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `baseRelation`.
5. **rescope** — change `scope` (widen/narrow/translate) under the baseRelation’s scope contract; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeBaseRelation** — not an edit-in-place. Changing `baseRelation` changes meaning; mint a new declaration and relate them via an explicit continuity relation (F.13 discipline), rather than silently rewriting the kind.

**Relation to A.6.5 slot operations (non-normative mapping).** These are *semantic change classes*; an implementation may realise them using A.6.5 slot operations on the SWBD record fields. Example: a **rebase** may be implemented as a `retarget` of `baseRef` on a *new* SWBD edition. The point of A.6.6 is that “we retargeted a ref” is not the semantic story; “we rebased the declaration” is.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, the allowed ops (`ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo`) can be viewed as Context-approved specialisations of `declareBase/rescope/rebase/refreshWitnesses` for specific baseRelation families, with stricter contracts and lintability.

#### A.6.6:4.7 - Disambiguation guide for selecting a baseRelation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it by selecting a baseRelation family:

| Colloquial intent | BaseRelation family (illustrative) | Dependent | Base | Typical witnesses |
| --- | --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification / indexing** (`identifies`, `indexedBy`, `registeredIn`) | entity-ref / slot-content | identifier / registry entry | issuance record, registry pin |
| “Make measurements comparable” | **Calibration / datum** (`calibratedTo`, `datumOf`, `normalisedTo`) | instrument/model/output | standard / datum | calibration work + certificate pin |
| “This claim is admissible because …” | **Evidence admissibility** (`validatedBy`, `verifiedBy`) | claim | evidence carrier / proof | SCR/RSCR pins, proof artefacts |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | WM edge | constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X under a view” | **Viewing / retargeting (specialised)** (`viewedVia`, `retargetedAlong`) | episteme/view | described entity | view operator pins, Bridge ids (if retargeting) |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | work-step / publication item | policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | property/abstraction | object | observation/derivation witnesses |
| “Meaning of this term is …” | **Meaning lane** (SenseCell/ConceptSet) | term occurrence | SenseCell/Concept row | definition/usage witnesses |

This table is illustrative; the discipline requirement is that the chosen baseRelation be explicit, declared, and contract-bearing. The “Meaning lane” row is included only as a **do-not-model-with-SWBD** reminder.

*Note.* The `viewedVia` / `retargetedAlong` families are defined by the A.6.3/A.6.4 viewing/retargeting operators; this table only classifies them as “relative-to-base” cases.

### A.6.6:5 - Archetypal Grounding

#### A.6.6:5.1 - System archetype: calibration to a standard

**Tell.** A lab instrument channel `TC‑17` is described as “anchored to ITS‑90”. Later, the reference standard is swapped, the phrase “still anchored” is kept, and the applicability window silently expands. Downstream work disagrees and nobody can reconstruct what changed.

**Show.** Express it as a base declaration:

```
BD#Calib_TC17_v5 :=
〈 dependent    = ThermocoupleChannelRef(TC-17),
base         = StandardRef(ITS-90 / CalStd-2025-09),
baseRelation = calibratedTo,
scope        = WorkScope{rig=R3, range=[0..200]°C},
Γ_time       = interval[2025-09-01, 2026-03-01],
witnesses    = { WorkRef(CalibrationRun#8841), CertRef(CalCert@edition=5) } 〉
```

**Show.** Disambiguate edits by operation class:

* New standard ⇒ **rebase** + **refreshWitnesses**.
* Wider applicability window ⇒ **retime** and likely **refreshWitnesses**.
* Relation-kind change (“not calibration, just normalisation”) ⇒ **changeBaseRelation** is not an edit; mint a new declaration and relate via continuity.

#### A.6.6:5.2 - Episteme archetype: claim admissibility via evidence relations

**Tell.** A report asserts: “Model M improves accuracy by 4%.” The team says the claim is “anchored in an experiment”, but dataset version, evaluation harness, and time selector are unclear, and no resolvable evidence is linked.

**Show.**

```
BD#AccGainClaim_2025Q4 :=
〈 dependent    = ClaimRef(CG:Claim#acc_gain_4pct),
base         = EvidenceCarrierRef(Work:EvalRun#2025-10-12),
baseRelation = validatedBy,
scope        = ClaimScope{dataset=BenchX@v3, metric=Top1, hardware=A100},
Γ_time       = snapshot(2025-10-12),
witnesses    = { SCRRef(EvalLog@edition=12), ComparatorSetRef@edition=7 } 〉
```

What becomes explicit is not “anchoring”, but:
* the relation kind (`validatedBy`),
* the scope slice,
* the time selector,
* the witness carriers that make the declaration admissible for decision use.

#### A.6.6:5.3 - Structural archetype: constructive grounding of a model edge

**Tell.** A structural edge is published (“A componentOf B”) without a constructor trace. It becomes treated as “obvious”, while the construction chain is not recoverable.

**Show.**

```
BD#EdgeGrounding_ComponentOf_17 :=
〈 dependent    = WMEdgeRef(Edge:componentOf#17),
base         = TraceRef(Γ_m:ComposeCAL#c17),
baseRelation = tv:groundedBy,
scope        = PublicationScope{view=WMCardLite, system=S, line=L3},
Γ_time       = snapshot(2025-11-02),
witnesses    = { WorkRef(AssemblyRun#7712), EditionPin(Γ_m:ComposeCAL@edition=4) } 〉
```

This example shows why “grounding” must be disambiguated: here it is a declared constructive relation with an explicit base (trace), not a vague claim of “stability”.

### A.6.6:6 - Bias-Annotation

| Lens | Bias introduced by this pattern |
| --- | --- |
| **Governance / assurance** | Prefers explicit witnesses and explicit time selectors for decision-relevant declarations; increases auditability but adds authoring overhead. |
| **Architecture** | Encourages reifying “relative-to” facts as first-class records rather than implicit prose. |
| **Onto-epistemic** | Treats “kind of base relation” as first-order; pushes authors to mint explicit baseRelation tokens instead of hiding semantics in adjectives. |
| **Didactic** | Introduces a new stable vocabulary (“dependent/base/baseRelation”) and requires authors to maintain it consistently across views. |

### A.6.6:7 - Conformance Checklist

A carrier (pattern, spec, schema, code artefact, or publication) conforms to A.6.6 iff:

1. **CC‑BD‑1 — Base relation kind is explicit.**  
   Every base-declaration-like statement SHALL name an explicit `baseRelation` token (a declared vocabulary element). No umbrella metaphor SHALL substitute for a relation kind.

2. **CC‑BD‑2 — Dependent and base are explicit and typed.**  
   Every based declaration SHALL make both `dependent` and `base` explicit, and SHALL be SlotKind/ValueKind/RefMode disciplined per A.6.5.

3. **CC‑BD‑3 — Scope is explicit.**  
   Every based declaration SHALL include an explicit `scope` (Claim scope (**G**) / Work scope / Publication scope).

4. **CC‑BD‑4 — `Γ_time` is explicit when time matters.**  
   If any time-dependent assumption exists, the based declaration SHALL include an explicit `Γ_time`; implicit “latest/current” SHALL NOT be used as a substitute.

5. **CC‑BD‑5 — Decision use is witnessed.**  
   If a base declaration participates in assurance, gating, or admissibility decisions, it SHALL include a non-empty, resolvable `witnesses` set (pins).

6. **CC‑BD‑6 — No silent kind edits.**  
   Changing `baseRelation` SHALL be treated as a semantic change: it SHALL be represented as a new declaration plus explicit continuity, not as an edit-in-place.

7. **CC‑BD‑7 — Grounding is disambiguated.**  
   Any use of “grounding/grounded” SHALL be disambiguated to a specific declared relation kind or moved to the meaning lane (SenseCell/ConceptSet).

8. **CC‑BD‑8 — Cross-context use is explicit.**  
   If dependent and base reside in different Contexts (or scope translation is required), the declaration’s reuse SHALL cite Bridge ids plus CL policy (no silent reuse across Contexts/planes).

9. **CC‑BD‑9 — `Γ_time` is not treated as freshness.**  
   When witness freshness/decay matters, it SHALL be expressed explicitly (evidence-role timespans, qualification windows, explicit freshness predicates), not by treating `Γ_time` as a proxy.

10. **CC‑BD‑10 — Edition fence for decision/publication.**  
   If a base declaration is used for decision or cited in PublicationScope, it SHALL be immutable per edition: updates SHALL mint a new declaration and connect it via explicit continuity/withdrawal.

11. **CC‑BD‑11 — Slot suffix discipline is respected.**  
   The `*Slot` suffix SHALL be used only for SlotKinds/positions, never for endpoint values or references.

12. **CC‑BD‑12 — No “anchor” relapse.**  
   `anchor*` / `ground*` / `attach*` SHALL NOT be used as surrogates for Context/SenseCell/ConceptSet or for an unnamed dependence kind. Authors SHALL either use the reserved primitive sense (where explicitly defined elsewhere) or rewrite into explicit `baseRelation(dependent, base)` form. Metaphor-head tokens SHALL NOT be minted as new contract-bearing `baseRelation` vocabulary entries (record them only as legacy aliases that map onto a specific, non-metaphor token).

13. **CC‑BD‑13 — BaseRelation contracts are explicit.**  
    Every `baseRelation` token used in an SWBD SHALL resolve to a vocabulary entry whose contract declares (at minimum): polarity; typing expectations (ValueKind + `refMode`) for `DependentSlot`/`BaseSlot`; admissible repair paths (KindBridge / narrowing / explicit retargeting); scope class; time discipline (`Γ_time` required/optional/forbidden); witness discipline; admissible change classes; and cross-context / cross-plane policy (Bridge ids + CL threshold + loss notes where applicable).

14. **CC‑BD‑14 — Authoring voice is explicit.**  
    In Tech / normative prose, based declarations SHALL be written as `baseRelation(dependent, base)` or `dependent --baseRelation--> base`. Base-view prose SHALL be used only if polarity is preserved via explicit inverse-token use; implicit role flips SHALL NOT be used.

15. **CC‑BD‑15 — Meaning lane separation.**  
    Semantic meaning assignment SHALL be modeled via SenseCell/ConceptSet lane constructs (E.10 D.CTX), not via SWBD. SWBD SHALL be used only for non-semantic base-dependence (admissibility, calibration, attribution, policy gating, constructive grounding, viewing/retargeting specialisations).

16. **CC‑BD‑16 — Reserved “bind” discipline.**  
    `bind/binding` SHALL be reserved for **name binding** (LEX discipline) and SHALL NOT be used as a synonym for declaring/refreshing/changing a base declaration. Authors SHALL use the base‑change lexicon (`declareBase`, `rebase`, `rescope`, `retime`, `refreshWitnesses`, …) and explicit continuity/withdrawal relations instead.

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Umbrella “anchored/attached/grounded” with no baseRelation** | Hides relation kind; cannot state invariants | Introduce a declared baseRelation token and rewrite prose to use it |
| **Perspective flip without role names** | Directionality and typing become ambiguous | Use `dependent/base` roles consistently; declare polarity in baseRelation contract |
| **Treating evidence as “the base”** | Confuses base with witnesses | Make evidence/pins witnesses unless the relation kind’s base is explicitly an evidence carrier |
| **Implicit “current/latest”** | Violates explicit time discipline | Declare `Γ_time` explicitly and use witness timespans for freshness where needed |
| **Decision gating without witnesses** | Becomes folklore; not reviewable | Add resolvable witnesses (`U.EvidenceRole`, SCR/RSCR pins, cert pins, proof artefacts) |
| **Semantic meaning expressed as a base declaration** | Confuses meaning lane with admissibility lane | Use SenseCell/ConceptSet; keep SWBD for non-semantic basedness |
| **Change baseRelation in place** | Semantic shift masquerades as update | Mint a new declaration and connect via continuity |
| **Using `*Slot` to name an endpoint/value** | Confuses SlotKind with ValueKind/RefKind; breaks substitution and tooling | Keep `*Slot` for positions; use `base`/`dependent` for values and `*Ref` for stored references |
| **Typing `baseRelation` as a `U.Surface*` carrier** | Confuses a contract-bearing relation token with a publication surface; invites “free text as relation kind” | Store `baseRelation` as a declared `NameToken` that resolves to a vocabulary entry with an explicit signature/contract |

### A.6.6:9 - Consequences

**Benefits**
* Disambiguation by construction: base-dependence becomes explicit via `baseRelation`.
* Cross-domain reuse: one stable record shape works for calibration, evidence admissibility, attribution, policy gating, and constructive grounding.
* Determinism where required: explicit scope and `Γ_time` prevent silent “latest/current” assumptions.
* Reduced “grounding” confusion: multiple grounding senses become distinguishable relation kinds.

**Trade-offs / mitigations**
* More explicit metadata and vocabulary: mitigated by defining baseRelation families once per Context and reusing them.
* Authoring overhead for witnesses in decision contexts: mitigated by pointing to already-existing artefacts (Work refs, pins) instead of creating new documents.

**Adoption test (informative).**
A team has adopted A.6.6 if, for any decision-relevant “relative-to” statement, it can produce a resolvable tuple
`〈dependent, base, baseRelation, scope, Γ_time?, witnesses?〉`
and can classify any update as one of:
`declareBase / withdrawBaseDecl / rebase / repointDependent / rescope / retime / refreshWitnesses / changeBaseRelation`.
### A.6.6:10 - Rationale

**Why focus on base declaration rather than a metaphor.**  
The recurring ambiguity is not “how to attach”, but “what is the declared base, and what kind of dependence is being asserted”. Naming the baseRelation token makes the dependence explicit and reviewable.

**Why separate base from witnesses.**  
Bases are semantic reference frames; witnesses are justifiers/enforcers for decision use. Conflating them makes both reasoning and audit impossible.

**Why include scope and `Γ_time`.**  
A declaration is never “everywhere forever” by default in FPF. Scope makes applicability explicit; `Γ_time` prevents hidden time dependence (“recent”, “current”, “latest”).

**Why prohibit kind edits.**  
Changing the relation kind changes meaning; treating it as an update erases history and breaks continuity discipline.

**Why the base-change lexicon.**  
Without explicit change classes, prose collapses distinct edits (rebase vs retime vs rescope vs witness refresh) and recreates the same ambiguity A.6.5 removed at the slot layer.

### A.6.6:11 - SoTA-Echoing

1. **RDF-star and statement qualification.**  
   **Adopt/Adapt.** RDF-star/SPARQL-star continues the semantic-web tradition of attaching qualifiers/provenance to statements and edges. We adopt the “qualified statement” intuition, but adapt it by requiring an explicit relation kind token and by tying time and scope discipline to FPF’s explicit `Γ_time` and USM scopes rather than leaving them implicit or purely notational.  
   *Primary source:* Hartig et al., “Foundations of RDF* and SPARQL*” (2017+).

2. **Wikidata-style statements with qualifiers and references.**  
   **Adopt/Adapt.** The Wikidata model popularised practical “statement + qualifiers + references” structures at scale. We adopt the separation of the core statement from its qualifiers/references, and adapt it by making decision-relevant witness requirements explicit via `U.EvidenceRole` and by requiring explicit scope/time where time-dependent assumptions exist.  
   *Primary sources:* Wikidata statement model documentation and design lineage (post‑2015 practice).

3. **Metrology traceability and calibration competence.**  
   **Adopt/Adapt.** Laboratory competence standards treat calibration as traceability to standards with documented evidence and bounded validity. We adopt the expectation that calibration-to-standard is not timeless, and adapt it by representing the validity window via explicit `Γ_time` plus witnesses as pinned calibration artefacts.  
   *Primary source:* ISO/IEC 17025:2017.

4. **Assurance case metamodels for claim–evidence structure.**  
   **Adopt/Adapt.** SACM formalises claim/evidence structures and emphasises structured support relations. We adopt the idea that decision-relevant admissibility links should be explicit, and adapt it by using FPF’s scope/time discipline and by treating relation-kind elision as a first-order defect.  
   *Primary sources:* OMG Structured Assurance Case Metamodel (SACM), 2018+.

5. **Objects over a base as a stable mathematical lens.**  
   **Adopt/Adapt.** Modern category-theory texts make “objects over a base” (slice categories) a reusable pattern for “X relative to B”. We adopt that lens as the stable abstraction behind base declarations, and adapt it with explicit scope/time and witness semantics needed for engineering governance.  
   *Primary source:* Riehl, *Category Theory in Context* (2016).

**SoTA binding note (informative).** This pattern’s “qualified statement + explicit relation kind + references” move aligns with RDF*/Wikidata practice (items 1–2); the explicit time-window + witness semantics in decision use align with metrology traceability and assurance-case structures (items 3–4); the “object over a base” lens is the abstraction used to keep the pattern stable across domains (item 5).

### A.6.6:12 - Relations

**Specialises A.6.P `U.RelationalPrecisionRestorationSuite`.**
A.6.6 is the RPR specialisation for “basedness / relative‑to” claims: it makes the relation kind explicit via `baseRelation`, qualifies it with scope/`Γ_time`/witnesses, and standardises evolution via a base‑change lexicon plus lexical red‑flags (`anchor*`).


**Builds on A.6.5 `U.RelationSlotDiscipline`.**  
SWBD introduces a structured record with slots; those slots must be SlotKind/ValueKind/RefKind disciplined, and its change classes must not be confused with slot-edit operations (A.6.5) or name-binding terminology (E.10 / L‑BIND).

**Constrains A.10 evidence admissibility links.**  
`verifiedBy` and `validatedBy` are treated as baseRelation tokens; their scope/time and witnesses become explicit when used for decisions.

**Aligns with A.2.4 `U.EvidenceRole`.**  
Decision-relevant witness sets should be representable as EvidenceRoles with explicit timespans and provenance discipline, not as ad‑hoc prose references.

**Aligns with A.14 constructive grounding (`tv:groundedBy`).**  
Constructive grounding is one specific baseRelation family: dependent is a model edge, base is a constructor trace; witnesses pin the trace and work artefacts.

**Coordinates with C.2.1 grounding holons.**  
Situational/empirical grounding via `GroundingHolonSlot` is treated as a distinct baseRelation family; it must not be collapsed with `tv:groundedBy` or with semantic meaning assignment.

**Coordinates with A.6.3–A.6.4 viewing/retargeting.**  
Viewing and retargeting are specialised “relative-to-base” moves (preserve describedEntity vs change it along a declared bridge). They should reuse SWBD vocabulary where an explicit base declaration is required (scope/time/witness), without collapsing into generic “anchoring” prose.

**Coordinates with A.2.6 and `Γ_time`.**  
Base declarations inherit the rule that time-dependent assumptions require explicit `Γ_time`; “current/latest” is not admissible.

**Feeds E.10 / F.18 lexical governance.**  
Umbrella metaphors are disallowed as substitutes for baseRelation tokens; prose must name explicit relation kinds and keep the meaning lane separate (SenseCell/ConceptSet).

### A.6.6:End

## A.6.7 - `MechSuiteDescription` — Description of a set of distinct mechanisms

> **Type:** Architectural pattern.
> **Status:** Stable.
> **Normativity:** Normative [A] (Core).

**One-line summary.** A `MechSuiteDescription` is a Kernel **Description** token that names a **set of distinct** `U.Mechanism.Intension` (different mechanisms, not realizations of one mechanism) and declares **suite-level obligations**, **required contract pins**, and **allowed usage protocols**, without conflating this with `MechFamilyDescription` or with publication `Pack`s.

**Plain-name.** mechanism suite description; mechanism suite passport.
**Placement.** Part A → cluster A.IV (A.6), immediately after A.6.5.

**Builds on.** E.8 (pattern template discipline), A.6.1 (`U.Mechanism.Intension` canonical form), A.6.5 (slot/ref discipline), E.10 (lexical + ontological rules; strict distinction; minimal specificity; kind suffixes), E.19 (conformance checks), E.18 (TGA / P2W graph discipline; crossing visibility), A.21 (OperationalGate(profile) and gate-level decisions).

**Used by.** Any framework area that needs a stable “universal kernel” shared across multiple mechanisms (notably the universalization of Part G patterns, including but not limited to G.5), and any “mechanism stack” whose correctness is defined by **shared legality + transport + audit obligations** rather than by a single shared `BaseType`.

**Mint vs reuse.**

* **Mints:** `MechSuiteDescription` (KernelToken, Description) and the record names used by its canonical form: `MechSuiteId`, `SuiteObligation`, `SuiteObligations`, `SuiteContractPins`, `SuiteProtocol`, `ProtocolStep`, `SuiteAuditObligations`.
* **Reuses (by reference):** `U.Mechanism.Intension` (members), `MechFamilyDescription` / `MechInstanceDescription` (optional citations), existing contract surfaces such as `CN‑Spec` / `CG‑Spec` (as pins), and E.TGA/P2W notions (as obligations/pins), without introducing new `U.*` kernel types.

**LEX.TokenClass.**
* `LEX.TokenClass(MechSuiteDescription) = KernelToken.`
* `LEX.TokenClass(MechSuiteId) = KernelToken.`
* `LEX.TokenClass(SuiteObligations) = KernelToken.`
* `LEX.TokenClass(SuiteContractPins) = KernelToken.`
* `LEX.TokenClass(SuiteProtocol) = KernelToken.`
* `LEX.TokenClass(SuiteAuditObligations) = KernelToken.`

**I/D/S.** Description (D); Tech name ends with `…Description`.
Lexical note: do **not** prefix this token with `U.` — `U.*` is reserved for Kernel **types**, while `MechSuiteDescription` is a Kernel **descriptor** (Description token).

### A.6.7:1 - Problem frame

In FPF, a **mechanism** is a node-level intensional object (`U.Mechanism.Intension`) with explicit SlotSpecs inside operator signatures, and a declared LawSet/guards/transport/audit (A.6.1, A.6.5). Many architectures, however, require **a stable bundle of multiple different mechanisms** that are intended to be used together under shared legality and crossing discipline (e.g., a characterization chain, a legality-gated selection pipeline, or a universal Part‑G kernel that multiple G.* patterns must reuse).

FPF already has `MechFamilyDescription`, but its meaning is: **many realizations of one and the same `U.Mechanism.Intension`**. That construct cannot correctly represent a bundle of different mechanisms (different intensions), and trying to overload it creates a level error.

Additionally, FPF reserves “Pack” for publication/shipping bundling (e.g., G.10); using “Pack” to mean “container of mechanisms” creates ontological collisions and downstream confusion.

### A.6.7:2 - Problem

We need a Kernel-level descriptor that can:

1. represent a **set of distinct mechanisms** (distinct `U.Mechanism.Intension`),
2. declare **shared obligations** that must hold across the set (e.g., crossing visibility, legality citation discipline, guard decision format, penalty routing),
3. provide **shared contract pins** (e.g., “this suite is contract-bound by CN‑Spec + CG‑Spec”), without duplicating those contract contents,
4. constrain **allowed protocols** of use (allowed pipelines / permitted ordering), without turning the suite into a mechanism, and
5. preserve strict distinction among:

   * a suite of mechanisms (`MechSuiteDescription`),
   * a family of realizations of one mechanism (`MechFamilyDescription`),
   * a publication bundle (`Pack`, e.g., G.10).

### A.6.7:3 - Forces

1. **Strict distinction (level hygiene).**
   *“many mechanisms”* must not be encoded as *“many realizations of one mechanism”*.
   Violating this blurs specialization laws, SlotKind invariance expectations, and audit/crossing responsibilities.

2. **Minimal specificity + kind suffix discipline (E.10).**
   The token name should encode only what is essential: it is a description, it is about mechanisms, it is a suite.
   It must not capture a particular domain (e.g., CHR) in the Kernel name.

3. **Contract-surface centrality (CN‑Spec / CG‑Spec).**
   Suites must cite contract surfaces as pins, not duplicate their internals, otherwise multiple competing “centers of legality” arise.

4. **Transport and crossing visibility discipline.**
   Cross-context and cross-plane steps must be visible and bridge-only; penalties must route to `R/R_eff` only; suites must not embed CL/Φ/Ψ/Φ_plane tables. Visibility is mediated via E.TGA / P2W (crossing surfaces + UTS/Path pins), not by “implicit semantics”.

5. **Guard vs gate separation.**
   Mechanisms can output tri-state guard outcomes and explanations; **gate decisions** (including `block`) and `DecisionLog` remain gate-level (`OperationalGate(profile)`). A suite must not collapse these layers.

6. **FPF is conceptual.**
   The suite is a conceptual descriptor: no implementation fields, no “lint rules”, no machine governance. The suite expresses obligations as conceptual constraints and required pins/anchors.

### A.6.7:4 - Solution

Introduce a new Kernel description token:

#### A.6.7:4.1 `MechSuiteDescription` (data model)

`MechSuiteDescription` declares:

1. **Suite identifier:** a stable identifier for downstream citation.
2. **Membership:** a finite set of distinct mechanism intensions.
3. **Suite obligations:** shared invariants that every member (and any permitted composition of members) must respect.
4. **Suite contract pins:** required citations/pins to contract surfaces and other “anchor” references.
5. **Suite protocols:** allowed pipelines of use (permitted ordering and optional steps), expressed at the descriptive level.
6. **Suite audit obligations:** required audit/pin visibility for downstream uses (UTS/Path pins, crossing pins, guard pins), expressed as required anchors (not run-time values).
7. **Notes:** didactic boundaries and anti-pattern warnings.

A minimal canonical form:

```
MechSuiteId := Identifier  // PascalCase; stable citation handle. Versioning MAY be carried externally.

SuiteObligation := one of {
   * bridge_only_crossings,
   * two_bridge_rule_for_described_entity_change,
   * transport_declarative_only,
   * penalties_route_to_r_eff_only,
   * guard_decision_tristate(pass|degrade|abstain),
   * unknown_never_coerces_to_pass,
   * gate_decision_separation,
   * guard_lexeme_reservations,
   * cg_spec_cite_required_for_numeric_ops,
   * no_silent_scalarisation_of_partial_orders,
   * no_silent_totalisation,
   * no_thresholds_in_suite_core,
   * crossing_visibility_required,
   * planned_slot_filling_in_work_planning_only,
   * finalize_launch_values_in_work_enactment_only,
   * implementation_export_discipline_when_cited
  +}

SuiteObligations := { SuiteObligation[*] } // clause set; duplicates-free.

MechSuiteDescription := ⟨
  mech_suite_id: MechSuiteId ,
  mechanisms: U.Mechanism.IntensionRef[+] ,     // distinct members; references preferred
  suite_obligations: SuiteObligations ,
  suite_contract_pins: SuiteContractPins ,
  suite_protocols?: SuiteProtocol[*] ,
  suite_audit_obligations?: SuiteAuditObligations ,
  suite_notes?: DidacticNotes
⟩
```

**Norms.**

* **Suite identifier.**
  `mech_suite_id` MUST be present and stable: it is the citation handle for downstream planning and `U.Work.Audit`.

**Well-formedness constraints (admissibility; non-deontic).**

* **WF‑MS‑1 (Membership set semantics).** `mechanisms` denotes a duplicates‑free set; order carries no semantics.
* **WF‑MS‑2 (Protocol closure).** If `suite_protocols` is present, then for every `ProtocolStep` in every `SuiteProtocol`, `step.mechanism ∈ mechanisms`.
* **WF‑MS‑3 (Suite ≠ Pack).** `MechSuiteDescription` does not carry shipping/publication payloads; publication remains the role of `Pack` patterns.
* **WF‑MS‑4 (Suite ≠ Mechanism).** `MechSuiteDescription` contains no `OperationAlgebra`/`LawSet`/execution semantics and is not admissible where a `U.Mechanism.*` node is required.

* **Membership is by mechanism intension (order-free).**
  `mechanisms` MUST denote a duplicates-free set of distinct `U.Mechanism.Intension` members. Membership order has no semantics; any intended ordering is expressed only in `suite_protocols`. A suite is **not** defined by a shared `BaseType`.

* **No substitution by `MechFamilyDescription`.**
  A suite MUST NOT be encoded as a `MechFamilyDescription`.
  If desired, a suite MAY additionally **cite** `MechFamilyDescription` / `MechInstanceDescription` for particular members (e.g., “preferred realization for this context”), but such citations do not redefine membership.

* **No “Pack” meaning.**
  A suite MUST NOT be named or treated as a publication pack. `Pack` remains reserved for publication/shipping bundling (e.g., G.10).

* **No mechanism semantics in the suite.**
  A suite is a **Description**, not a mechanism: it does not define `OperationAlgebra`, it does not execute, and it does not absorb gate logic.

#### A.6.7:4.2 SuiteObligations (canonical obligation vocabulary)

`MechSuiteDescription` MAY declare any obligations, but the following obligation vocabulary is **canonical** and is intended to be reused across the universalization of Part G and legality-gated characterization stacks.

`SuiteObligations` SHOULD be written as an explicit clause set, e.g.:

```
SuiteObligations := {
  bridge_only_crossings,
  two_bridge_rule_for_described_entity_change,
  transport_declarative_only,
  penalties_route_to_r_eff_only,
  guard_decision_tristate(pass|degrade|abstain),
  unknown_never_coerces_to_pass,
  gate_decision_separation,
  guard_lexeme_reservations,
  cg_spec_cite_required_for_numeric_ops,
  no_silent_scalarisation_of_partial_orders,
  no_silent_totalisation,
  no_thresholds_in_suite_core,
  crossing_visibility_required,
  planned_slot_filling_in_work_planning_only,
  finalize_launch_values_in_work_enactment_only,
  implementation_export_discipline_when_cited
}
```

**Obligation meanings (normative).**

1. **`bridge_only_crossings`.**
   Well-formedness constraint: cross-context / cross-plane reuse performed by any member mechanism is represented via that member’s published `Transport` as Bridge-only (no implicit crossings). A suite does not create transport exceptions.

1.1. **`two_bridge_rule_for_described_entity_change`.**

 * If a suite member’s lawful use requires changing the described entity (kind/identity change, `CL^k`), the crossing MUST be explicit and MUST satisfy the two-bridge rule: plane/context transfer and kind transfer are distinct, both are Bridge-mediated, and both remain penalty-routed to `R/R_eff` only.
 
1.2. **`transport_declarative_only`.**
 * Well-formedness constraint: suite obligations do not add transfer edges or embed CL/Φ/Ψ/Φ_plane tables. Any transport-related obligation is expressed only as referenced pins/anchors whose realization is mediated by E.TGA / gate surfaces.
 
2. **`penalties_route_to_r_eff_only`.**
   Well-formedness constraint: CL/Φ/Ψ/Φ_plane penalties associated with crossing discipline route to `R/R_eff` only; suites do not define transport penalties that alter `F/G`.

3. **`guard_decision_tristate(pass|degrade|abstain)` and `unknown_never_coerces_to_pass`.**
   Well-formedness constraint: admissibility/eligibility outcomes use a tri-state guard result `GuardDecision := {pass|degrade|abstain}`. Unknown/insufficient evidence is not coerced to `pass`; it resolves to `{degrade|abstain}` under declared failure behavior (e.g., probe-only as a SoS‑LOG branch id, not as a new decision value).

4. **`gate_decision_separation`.**
   Well-formedness constraint: suites do not define or use `GateDecision` values (including `block`) as part of mechanism/suite semantics. Gate-level outcomes and `DecisionLog` remain on `OperationalGate(profile)`.

5. **`guard_lexeme_reservations`.**
   Well-formedness constraint: `USM.CompareGuard` and `USM.LaunchGuard` denote gate-owned guard events/pins; member mechanisms and suite protocols use `…Admissibility` / `…Eligibility` for guard predicates, not the reserved gate lexemes.

6. **`cg_spec_cite_required_for_numeric_ops`.**
   Well-formedness constraint: any member operation that performs numeric comparison/aggregation/legality-sensitive scoring cites the applicable `CG‑Spec` (and relevant subrefs) as contract pins, rather than embedding equivalent “local legality” content.

7. **`no_silent_scalarisation_of_partial_orders` and `no_silent_totalisation`.**
   Well-formedness constraint: if a member mechanism induces a partial order, it preserves set-/relation-valued semantics; it does not silently reduce to a scalar/total order. Any totalization is explicit and policy-bound.

8. **`no_thresholds_in_suite_core`.**
   Well-formedness constraint: suite core does not publish acceptance thresholds (“passing scores” / hidden cutoffs). Thresholds belong to acceptance clauses / task signatures / gate profiles.

9. **`crossing_visibility_required`.**
   Well-formedness constraint: any GateCrossing relevant to suite use publishes a `CrossingSurface` (E.18) and can be cited as an audit anchor.
   GateCrossing includes (at minimum) cross-context, cross-plane, and cross-kind/described-entity changes, entry into `U.WorkEnactment` (LaunchGate), and any `edition_key` change of pinned `editions{…}` vectors.
   Suites may require `CrossingSurfaceRef` / UTS / Path pins and policy-id pins as anchors, and MUST NOT embed CL/Φ/Ψ/Φ_plane tables.

10. **`planned_slot_filling_in_work_planning_only`.**
   Well-formedness constraint: any planned slot filling used as a baseline for suite use is authored in `WorkPlanning` as a planned baseline (no run-time slot instances; no launch values).

11. **`finalize_launch_values_in_work_enactment_only`.**
   Well-formedness constraint: `FinalizeLaunchValues` (and any witness of actual launch values) occurs only in `U.WorkEnactment`; neither the suite nor any planned-baseline artifact is a place for launch values.

#### A.6.7:4.3 SuiteContractPins

A `MechSuiteDescription` MUST be able to declare required contract pins as references, not as duplicated content. Canonically:

```
SuiteContractPins := ⟨
  required_spec_refs?: {CNSpecRef?, CGSpecRef?, ...},
  required_edition_pins?: EditionPin[*],
  required_policy_id_pins?: PolicyIdPin[*],
  required_planned_baseline_ref?: PlannedBaselineRef?
⟩
```

**Norms.**

* If the suite is legality-gated for characterization, `CNSpecRef` and `CGSpecRef` MUST be required (as references/pins).
* Contract pins are citations and anchors. They do not replace the underlying `…Spec` objects.
* A suite MAY require the presence of a planned-baseline artifact in P2W (e.g., a WorkPlanning plan item such as `…SlotFillingsPlanItem` that pins chosen refs/editions), but MUST treat it as a **reference/pin requirement**, not as a place to store launch values or gate decisions.
  When required, the planned-baseline artifact is authored in `WorkPlanning` and is citeable by downstream `U.Work.Audit`; any `FinalizeLaunchValues` witness remains `U.WorkEnactment`-only.
* A suite MAY serve as `TargetSlotOwnerRef` for a planned-baseline plan item (planned slot filling owner role), but this does not make the suite a mechanism and does not create run-time slot instances.
 
#### A.6.7:4.4 SuiteProtocols

A suite MAY describe allowed protocols (pipelines) as descriptive constraints on how suite members are intended to be composed. A protocol description:

* MUST name the member mechanisms it uses (explicitly; no “implicit use”),
* MAY mark steps as optional,
* MUST NOT introduce hidden crossings or hidden legality steps,
* MUST treat “publish/telemetry” as an external protocol step that is realized through existing publication surfaces (e.g., Part G shipping), rather than as a hidden tail inside a mechanism.

A canonical shape for protocols:

```
SuiteProtocol := ⟨
  steps: [ ProtocolStep₁, …, ProtocolStepₙ ],
  invariants?: ProtocolInvariant[*],
  notes?: DidacticNotes
⟩

ProtocolStep := ⟨
  mechanism: U.Mechanism.IntensionRef,
  operation: OperationName,
  optionality: {required|optional},
  requires_pins?: PinRef[*]
⟩
```

#### A.6.7:4.5 SuiteAuditObligations

A suite MAY require that downstream use provide certain audit anchors. These are **requirements**, not run-time values. A suite audit obligation MAY include:

* required `UTS` + `Path` pins,
* required crossing-surface visibility pins for any crossing relevant to suite use,
* required presence of `USM.CompareGuard` and/or `USM.LaunchGuard` **pins** (not gate checks),
* required declaration of guard ownership (e.g., a `GuardOwnerGateSlot` anchor),
* required expression of guard violations as `GuardFail` events aggregated by the guard-owning gate (per `GuardOwnerGateSlot`), not as extra mechanism/suite states,
* required policy-id pins for any degrade/sandbox/probe-only branches (SoS‑LOG branch id anchors).
* required parity/selection-grade pins when applicable (e.g., when suite use claims parity-grade comparison/selection surfaces downstream).

**Norm.** A suite must never publish a `DecisionLog` or `GateDecision`. If the suite requires guard pins, it requires their **presence** as anchors so that the gate-level owner can aggregate `GuardFail`s and decide `degrade|block` per gate profile.

#### A.6.7:4.6 Examples (tell–show–show discipline)

**Example 1 (conformant).** A characterization legality suite:

```
CHRMechanismSuiteDescription : MechSuiteDescription :=
  mech_suite_id = CHRMechanismSuiteId
  mechanisms = { UNM, UINDM, USCM, ULSAM, CPM, SelectorMechanism }
  suite_obligations includes:
    bridge_only_crossings,
    penalties_route_to_r_eff_only,
    guard_decision_tristate(pass|degrade|abstain),
    gate_decision_separation,
    cg_spec_cite_required_for_numeric_ops,
    no_silent_scalarisation_of_partial_orders,
    crossing_visibility_required,
    planned_slot_filling_in_work_planning_only,
    finalize_launch_values_in_work_enactment_only
  suite_contract_pins requires: {CNSpecRef, CGSpecRef}
  suite_protocols includes:
    normalize → indicatorize → score → (fold_Γ?) → compare → select → publish/telemetry
```

This description is not a `MechFamilyDescription` (because it contains multiple distinct mechanisms), and it is not a `Pack` (because it does not ship artifacts; it only declares membership and shared obligations/pins/protocols).

**Example 2 (non-conformant).** Misusing a family as a suite:

```
CHRMechanismFamily : MechFamilyDescription := { UNM, UINDM, USCM, ... }
```

This is a level error: `MechFamilyDescription` is reserved for realizations of a single mechanism intension.

**Example 3 (non-conformant).** Turning a suite into a hidden gate:

* The suite declares `GateDecision` values or embeds a `DecisionLog`.
* The suite defines acceptance thresholds (“pass score ≥ 0.7”) as part of suite obligations.
* The suite embeds Φ/CL tables or invents ad-hoc “transfer edges”.

All violate the separation between mechanism/suite descriptions and gate-level operational control.

### A.6.7:5 - Archetypal Grounding

A suite is an archetypal “passport” or “capability bundle descriptor”:

* It answers **what mechanisms exist in the bundle** and **what shared invariants** make their composition lawful.
* It provides **shared contract anchors** (pins) that downstream planning and work must cite.
* It remains descriptive: it does not execute, it does not contain run-time outputs, and it does not replace the E.TGA subgraph that actually connects nodes by `Uses` and manages crossings.

### A.6.7:6 - Bias-Annotation

Common biases this pattern guards against:

* **Overloading “family”.** Treating “many different mechanisms” as “many realizations of one mechanism” destroys level hygiene and encourages semantic drift across members.
* **Publication conflation.** Using “pack” semantics to smuggle publication/shipping obligations into the meaning of a mechanism bundle.
* **Gate conflation.** Treating suite-level obligations as gate decisions (“block”) instead of keeping `block` at the gate layer.
* **Convenience totalization.** Collapsing partial orders into scalars “for ease of selection”, which undermines set-return semantics and legality gating.

### A.6.7:7 - Conformance Checklist

A `MechSuiteDescription` is conformant iff all applicable items hold:

**CC‑A.6.7‑1 (Correct level).** The suite’s `mechanisms` enumerate **distinct** `U.Mechanism.Intension` members. The suite is not encoded as `MechFamilyDescription`.

**CC‑A.6.7‑2 (Description token, not `U.*`).** The suite token is a Description token and MUST NOT be introduced under `U.*`. Its name ends with `…Description`.

**CC‑A.6.7‑3 (No execution semantics).** The suite MUST NOT define mechanism blocks (`OperationAlgebra`, `LawSet`, etc.) and MUST NOT be used as a mechanism node.

**CC‑A.6.7‑4 (No gate decisions).** The suite MUST NOT define `GateDecision`, MUST NOT publish `DecisionLog`, and MUST preserve gate/mechanism separation.

**CC‑A.6.7‑5 (Contract pins, not duplication).** If the suite is legality-gated for numeric comparison/aggregation/scoring, it MUST require `CG‑Spec` citation pins (and SHOULD require `CN‑Spec` pins where applicable). It MUST NOT duplicate contract content as “local CG‑Spec”.

**CC‑A.6.7‑5a (CN+CG pins for legality-gated characterization).** If the suite is legality-gated for characterization, it MUST require both `CNSpecRef` and `CGSpecRef` as pins (references), consistent with A.6.7:4.3.

**CC‑A.6.7‑6 (Transport discipline preserved).** The suite MUST NOT introduce transport exceptions. Any crossing obligations must remain Bridge-only and must route penalties to `R/R_eff` only.

**CC‑A.6.7‑7 (Tri-state guard discipline when used).** If the suite declares admissibility/eligibility semantics, it MUST use `GuardDecision := {pass|degrade|abstain}` and MUST NOT coerce unknown to pass.

**CC‑A.6.7‑8 (No thresholds in core).** The suite MUST NOT publish acceptance thresholds or “passing scores”. Thresholds must remain in acceptance clauses / task signatures / gate profiles.

**CC‑A.6.7‑9 (Crossing visibility anchors).** If suite use depends on crossings (context/plane/kind, entry into `U.WorkEnactment` (LaunchGate), or edition-key changes), the suite MUST require crossing visibility anchors (BridgeId/channel, ReferencePlane, CL mode, policy-id pins, UTS/Path pins) as audit obligations, without embedding the tables.

**CC‑A.6.7‑10 (Suite id present).** The suite MUST declare `mech_suite_id: MechSuiteId` so that downstream planning/audit can cite it stably.

**CC‑A.6.7‑11 (Two-bridge discipline preserved).** If suite obligations claim cross-kind/described-entity validity, they MUST require explicit `CL^k` handling (two-bridge rule) and MUST NOT allow implicit described-entity changes.

**CC‑A.6.7‑12 (Implementation export hygiene when cited).** If the suite cites realizations/implementations, the citations MUST preserve export/import discipline (LOG/CHR: no Γ export; CAL: exactly one Γ; imports acyclic).

**CC‑A.6.7‑13 (No Pack conflation).** The suite MUST NOT be introduced, named, or used as a publication/shipping `Pack`.

**CC‑A.6.7‑14 (Protocol closure & explicitness).** If `suite_protocols` is present, every `ProtocolStep.mechanism` MUST be a member of `mechanisms` (WF‑MS‑2) and the protocol MUST NOT rely on implicit mechanism steps or implicit crossings.

**CC‑A.6.7‑15 (P2W split preserved when applicable).** If the suite requires a planned-baseline pin (e.g., a planned slot-fillings artifact), that baseline MUST be a `WorkPlanning` artifact and MUST NOT contain launch values or `FinalizeLaunchValues` witnesses; such witnesses remain `U.WorkEnactment`-only.

### A.6.7:8 - Common Anti-Patterns and How to Avoid Them

1. **Anti-pattern: “Family-as-suite”.**
   Using `MechFamilyDescription` to list multiple distinct mechanisms.
   **Fix:** use `MechSuiteDescription` for “many mechanisms”, and keep `MechFamilyDescription` for “many realizations of one mechanism”.

2. **Anti-pattern: “Pack-as-suite”.**
   Naming/using the suite as a `Pack`.
   **Fix:** reserve `Pack` for publication/shipping bundling; use `Suite` for mechanism bundles.

3. **Anti-pattern: “Suite contains legality tables”.**
   Duplicating CG‑Spec or embedding CL/Φ/Ψ tables in suite obligations.
   **Fix:** publish pins and references only; keep legality content in `…Spec` and policy registries; keep crossing realization in E.TGA/gate surfaces.

4. **Anti-pattern: “Suite is a hidden gate”.**
   Introducing thresholds, `block`, or `DecisionLog` in the suite.
   **Fix:** suite declares guard formats and required pins; the gate owns decisions.

5. **Anti-pattern: “Implicit calls”.**
   A protocol implies “normalize happens somewhere” without explicit member and pin visibility.
   **Fix:** protocols enumerate steps and required pins; E.TGA `Uses` edges remain explicit.

### A.6.7:9 - Consequences

**Benefits.**

* Eliminates level confusion between “family of realizations” vs “bundle of mechanisms”.
* Provides a Kernel home for universal obligations reused across multiple patterns (notably Part G universalization).
* Makes legality/transport/audit obligations shared and explicit, reducing semantic drift across member mechanisms.

**Costs.**

* Introduces an additional descriptive artifact that must be maintained as suites evolve.
* Requires discipline: suites must remain descriptive and must not become “meta-mechanisms” or “hidden gates”.

### A.6.7:10 - Rationale

Characterization and legality-gated selection pipelines are not unified by a single shared `BaseType`; they are unified by:

* shared contract surfaces (e.g., CN‑Spec / CG‑Spec),
* shared transport and crossing discipline (Bridge-only; penalties to `R_eff`),
* shared guard semantics (tri-state, no coercion),
* and explicit protocol constraints (allowed pipelines).

Encoding this unity as “one mechanism” or “one family” forces false commonality and invites hidden semantics. A dedicated **suite descriptor** preserves modularity and keeps the level separation clean.

### A.6.7:11 - SoTA-Echoing

This pattern echoes post‑2015 best practice in modular reasoning systems: separation of **contract surfaces** from **operators**, explicit composition protocols, and strong boundaries between **decision procedures** and **gating/acceptance control**.

In modern multi-step evaluation pipelines (e.g., calibrated scoring, uncertainty-aware comparison, portfolio/pareto selection, and quality-diversity archives), correctness typically relies more on explicit contracts and lawful composition than on a single monolithic “universal metric”. `MechSuiteDescription` provides the Kernel representation that allows such pipelines to be described with stable obligations while keeping domain methods and FPF patterns generators outside the universal core.

### A.6.7:12 - Relations

* **Relates to A.6.1:** suite members are `U.Mechanism.Intension`; the suite does not replace the mechanism definition.
* **Relates to A.6.5:** suites must not weaken slot/ref discipline; any suite protocol assumes member mechanisms follow A.6.5 invariants (SlotKind stability, correct refMode, no semantic meaning in SlotIndex).
* **Relates to E.18 / P2W:** suite protocols describe intended composition; actual composition and crossings are expressed in E.TGA subgraphs and P2W flow.
* **Relates to E.19:** suite-level conformance is a conceptual review checklist; suites require pins/anchors rather than procedural validation.
* **Relates to G.10:** suites are not packs; publication/shipping is handled via G.10 and MVPK faces.

### A.6.7:End

## A.6.8 - Service Polysemy Unpacking (RPR‑SERV)

**Plain-name.** Service situation unpacking.
**One-liner:** “service” ⇒ clause | promised work‑kind | provider principal/system | access point | access spec | commitment | promise act | delivery method/work

> **Type:** Architectural (A) — A.6.P specialisation (RPR)
> **Status:** Stable
> **Normativity:** Normative
> **Placement:** Part A → A.6 (Precision restoration / stack discipline)
> **Builds on:** A.6.P (RPR recipe), A.6.5 (slot discipline), A.6.B (routing), A.2.3 (`U.PromiseContent`), A.2.8 (`U.Commitment`), A.2.9 (`U.SpeechAct`), A.15 (`U.Work`), E.10 (LEX, incl. L‑SERV, LEX‑BUNDLE & PTG stances), F.17 (UTS — Unified Term Sheet), F.18 (Name Cards / NQD‑front; promise ≠ utterance ≠ commitment).
> **Coordinates with:** A.6.C (contract bundle unpacking), A.7 (Object≠Description≠Carrier), G.* evidence discipline (EvidenceGraph / SCR), Context/Bridge policy for cross‑Context reuse, F.8 (Mint/Reuse), E.15 (LEX‑AUTH when refactoring existing prose at scale).
> **Delta-Class:** Δ‑3 (new normative pattern; corpus‑wide lexical refactor expected when adopted in Core)
> **Impact radius:** Any normative prose that uses the “service” cluster (`service`, `service provider`, `server`); LEX rules (L‑SERV / LEX‑BUNDLE); UTS blocks (F.17); contract/boundary patterns that already talk about services (esp. A.6.C); any automated repair/lint pipeline used for bulk refactors (E.15 / LEX‑AUTH).
 **Mint vs reuse:** Mints the `serviceSituation(…)` QRR lens id and the facet headphrase set defined in §4.3. Reuses `U.PromiseContent`, `U.Commitment`, `U.SpeechAct`, `U.System`, `U.Work`, `U.MethodDescription`, and the A.6.P/QRR recipe.
 **DRR pointer:** **REQUIRED before Core admission.** `DRR‑SERV‑POLYSEMY‑<id>` (TBD in draft; must cite the PQG run + refactor/harness plan).

**Intent.** Prevent category errors and metonymic drift caused by the borderline word “service” by forcing every normative mention to name the **facet** (promise content vs promised work‑kind/effect vs accountable principal vs realization system vs access object vs interface vs binding vs act vs run‑time work/evidence) and by providing a stable “service situation” lens that keeps those facets related without collapsing them.

**Non‑goal (modularity guard).** This pattern does **not** redefine the semantics or field structure of the promise‑content object (the **promise content**). That kernel meaning is defined in **A.2.3 (`U.PromiseContent`)**. A.6.8 is a precision‑restoration + lexicon discipline that (i) forces facet‑typed head phrases and (ii) provides an optional QRR lens to bind already‑defined kinds without collapsing them. Contract‑talk unpacking is handled by **A.6.C**, which invokes this pattern when contract language contains the service cluster.

### A.6.8:1 - Problem frame

In real engineering language, *service* can denote (and routinely collapses) multiple **facets** that admit different predicates and different governance rules:

* a **promise content** (`U.PromiseContent`),
* a **promised work‑kind / effect‑kind** (“what is to be delivered”, as a kind/template),
* a **service provider role** (role kind in the clause),
* a **service provider principal** (role‑enactor accountable for delivery and capable of holding commitments),
* a **service access point** (an addressable system/facility/desk/endpoint host),
* a **service access spec** (API surface / endpoint set / SOP visible to consumers),
* a **service delivery / realization system** (the socio‑technical system that actually performs fulfillment work),
* a **service delivery method** (workflow/runbook/procedure used to fulfill),
* a **service commitment** (deontic binding, e.g., SLA/SLO as obligation),
* a **service promise act** (promissory speech act: offer/promise/accept/agree/publish),
* a **service delivery work** episode (run/incident/fulfillment work + evidence).

FPF’s kernel uses `U.PromiseContent` as **promise content**, which is SoTA‑consistent for contracts and decision lanes, but clashes with the everyday addressability-centric use of “service”. This makes “service” a high‑risk metonymy attractor: authors start using the same word for (a) the clause, (b) the provider system, and (c) the delivery work, and readers cannot reliably recover which is meant.

In addition, lived “service talk” is rarely isolated to the token *service*: it co‑moves with **server** and **service provider** (and with “API service”, “service desk”, “service team”). Treating only the word *service* as ambiguous is an underfit to the domain.

Critically, everyday “service” often conflates **three different participants** that are frequently *not identical*:

1. the **provider principal** (accountable role‑enactor: a team/org/vendor),
2. the **delivery / realization system** (the socio‑technical system that does the work),
3. the **access point** (the addressable entrypoint/gateway/front desk/endpoint host).

This pattern forces those participants apart, because different predicates and different governance rules apply to each.

This pattern makes “service” an **always‑unpack token** in normative prose: you may use it only as part of a **qualified head phrase** that states which facet is meant.

### A.6.8:2 - Problem

Unqualified “service” in normative prose causes **referent ambiguity** that cannot be repaired by reader intuition, because the ambiguity is structural:

1. **Addressability mismatch:** you can *call/visit* an access point, but you cannot call a clause.
2. **Type mismatch:** work/telemetry/incidents are properties of **work + carriers**, not of promise content.
3. **Deontic mismatch:** “must/shall/guarantee” binds **actors/roles** via commitments, not abstract clauses.
4. **Speech‑act mismatch:** “promise/offer/accept” are **events/acts**, not the promise content itself.
5. **Evolution mismatch:** changing an API endpoint or deployment is not “changing the service” unless you declare which facet changed and narrate that change with stable change classes.

Result: reviewers can’t apply A.6.B routing, and engineers are incentivized to preserve ambiguity (“service” as a convenient metonym) because it avoids committing to a model.

### A.6.8:3 - Forces

| Force                                   | Tension                                                                                                 |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Precision vs readability                | Always‑unpacking improves auditability, but increases wordiness.                                        |
| Kernel minimality vs safety             | Avoid introducing new core primitives; still prevent category errors.                                   |
| Everyday language vs normative contract | Teams naturally say “service is down”; normative text must point to *what* is down.                     |
| Cross‑domain applicability              | Must work for microservices, human services, public services, and physical services.                    |
| Evolution vs continuity                 | Service facets evolve at different rates; prose must narrate changes without silently shifting meaning. |

### A.6.8:4 - Solution

#### A.6.8:4.0 — UTS + LEX preparation (mandatory for authoring/repair)

“Service” is a **polysemy cluster**, not a single token. Therefore, before applying the rewrite rules below to normative prose, the author/editor SHALL create or update a **thread‑local UTS block** (F.17) and its paired **LEX‑BUNDLE entries** (E.10) for the **service cluster** (Tech/Plain twins and PTG stance).

**Required cluster coverage (minimum).** The UTS block MUST cover, at minimum, the co‑moving surface forms:

* `service` / `services`
* `service provider` (and the corresponding provider term in the domain: team/shop/department/vendor, etc.)
* `server` (including “daemon”, “host”, “endpoint host” where those appear)
* `microservice` / `microservices` (and spelling variants such as “micro-service”) **when they appear in the source prose** as a stand‑in for the addressable system facet (“the thing you can call/deploy”) or as a collapsed bundle token
* “API service” / “service interface” / “service access” (when present in the source prose)
* “SLA/SLO/service level” language (when present)

**Context selection (universality guard).** The UTS block MUST cite **ContextName@Edition** in each SenseCell (F.17), and the cited contexts SHOULD span at least **three** distinct “service traditions” reflected in this pattern’s SoTA‑Echoing set (e.g., ITSM/service management, EA/modelling, speech‑act/coordination, microservices/SRE practice). This prevents a “FPF‑only” meaning loop and keeps facet names portable.

**Headphrase governance (no ad‑hoc synonyms).**

* Each facet head phrase used by this pattern (e.g., “promise content”, “service access point”) SHALL appear as a **UTS twin** (Tech/Plain) in the local UTS block, not as an author‑invented one‑off.
* Both the **Tech** and **Plain** twin for a facet head phrase SHALL carry an explicit **head kind word** that signals the facet category (**clause / role / principal / system / access point / spec / method / commitment / act / work**). Plain synonyms are permitted only if they preserve the head kind (e.g., “endpoint” as an access‑point head kind; “API spec” as an access‑spec head kind). This is the readability guard that prevents “mathematician renamings”.
* A conforming **normative Tech** text SHALL treat the bare word **service** (unqualified) as **PTG=Guarded** (E.10): it is allowed only under this pattern’s rewrite rules and only as part of a qualified head phrase.
* If a new facet head phrase must be introduced, it SHALL be treated as a **LexicalAct** with an explicit **Mint/Reuse** decision (F.8), and its **CandidateSet + rationale** SHOULD be recorded via a Name Card (F.18 / NQD‑front) to avoid “clever” but unstable vocabulary.

This preparation step is intentionally “linguistic”: it binds the pattern to how engineers actually write (service/provider/server), rather than to an isolated kernel token.

**SoTA binding (informative audit anchor).** The major disambiguation rules in §4.4–§4.7 are aligned with the SoTA‑Echoing rows in §11:
* “offering / promise content” vs “delivery operations” split → ITIL 4 + EA modeling,
* “interface/access” vs “realization/implementation” split → ArchiMate + SRE practice,
* “promissory act” vs “promise content” split → ISO 24617‑2 dialogue acts,
* “offering/commitment” vs “delivery event” split → service ontologies (e.g., S‑OPL / UFO),
* “actuals/telemetry” vs “targets/obligations” split → SRE evidence discipline,
* “roles + context” emphasis when discussing “service quality” → service science / service‑dominant logic.
(These anchors are informative; they do not assert cross‑Context identity and require Bridges when imported as terms.)

#### A.6.8:4.1 — Trigger rule

This pattern applies whenever **“service”** appears in **Tech/normative prose** as a head noun (including compounds like “X service”, “the service”, “our service”, “this service”), **even when the intended referent is `U.PromiseContent`**.

It also applies to the adjacent cluster terms **“service provider”** and **“server”** when they are used as stand‑ins for the same collapsed bundle (clause/access/provider/work). The rewrite outcome for those terms is facet‑typed (see §4.3 and §4.9).

**Carve‑out (informative, narrow):** quotations of external material may retain “service”, but SHALL be followed immediately by an unpacking rewrite in the surrounding normative text.

#### A.6.8:4.2 — Stable lens: the Service Situation Bundle

Define a stable, kind‑labelled qualified record (hyperedge lens) that makes the bundle explicit **without introducing a new core entity kind**. This record binds already‑defined referents so prose can talk about multiple facets without collapsing them:

**`serviceSituation(…)` — Qualified Relation Record (QRR) lens id**

Participant slots (principal facets). The slot names are intentionally *prose-facing* (engineer-readable): they are meant to make it hard to “silently collapse” clause/principal/system/access/work.

* `promiseContentRef : PromiseContentRef`
  *Promise content* — the `U.PromiseContent` referent (A.2.3). **Plain head:** *promise content* / *service offering clause* / *service promise clause*.
* `promisedOutcomeSpecRef? : OutcomeSpecRef`
  The **promised outcome template** described by the clause (`U.OutcomeSpec`, A.7:5.10). It may constrain:
  - **delivery work** (work‑only: “do X for ≥5 minutes”),
  - **delivered state / artifact** (result‑only: “a hole of depth ≥1 m exists”),
  - or **both** (composite).
  This is **not** a concrete `U.Work` run and **not** the delivered world object; it is the spec used to judge delivery work and evidence.
**Invariant: SERV‑INV‑1 (OutcomeSpecness).**
  `promisedOutcomeSpecRef` MUST denote a `U.OutcomeSpec` (kind‑labelled episteme), not a `U.Work` episode and not an extensional result object.
* `providerRoleRef : RoleRef`
  The provider **role kind** named by the clause (typically `clauseRef.providerRole`).
* `providerAssignmentRef? : RoleAssignmentRef`
  The concrete **role enactor assignment** that holds `providerRoleRef` in the relevant Context/window (E.10 / A.2.1). This is what everyday talk calls “the service provider” (team/shop/vendor/system).
* `providerPrincipalRef? : EntityRef`
  Convenience alias: the **accountable principal** extracted from `providerAssignmentRef` (when you need to name the accountable party explicitly).
  - Normative default: commitments attach here (or to the relevant role assignment), not to the access point.
* `consumerRoleRef? : RoleRef`
  The consumer **role kind** named by the clause (typically `clauseRef.consumerRole`, if present).
* `consumerAssignmentRef? : RoleAssignmentRef`
  The concrete **role enactor** of `consumerRoleRef` (when needed for accountability/evidence narratives).
* `accessSpecRef? : MethodDescriptionRef`
  The **service access spec** / request‑facing interface description (API signature, OpenAPI, endpoint contract, intake SOP, desk procedure). This is typically `promiseContentRef.accessSpec` (A.2.3) and is a `U.MethodDescription`.
* `accessPointRef? : SystemRef`
  The **service access point** — an addressable system/facility/desk/endpoint host through which requests arrive. In lived language this is often called “the service” or “the server”.
* `deliverySystemRef? : SystemRef`
  The **service delivery / realization system** that actually performs the delivery work. In software, this is usually the deployed application + dependencies (and may be behind gateways); in human services, this is the socio‑technical organisation + tooling that does the work.
* `deliveryMethodRef? : MethodDescriptionRef`
  The **service delivery method** / internal procedure/runbook/workflow used to fulfil the clause. This is distinct from `accessSpecRef` (request‑facing access).
* `commitmentRef? : CommitmentRef`
  Deontic binding to deliver the clause (required when the prose uses must/shall/guarantee/SLA force).
* `promiseActRef? : SpeechActRef`
  The instituting/promissory act (offer/promise/accept/agree/publish) when relevant.

  **Invariant: SERV‑INV‑2 (Responsibility alignment).**
  When the surrounding passage is normative about responsibility (D‑quadrant language), the promissory actor/authorizer of `promiseActRef` aligns with `providerPrincipalRef` (or the corresponding `providerAssignmentRef`), rather than being silently shifted to `accessPointRef`.
* `deliveryWorkRef? : WorkRef`
  The delivery / fulfillment work episode(s) (including incidents, runs, requests) when relevant.

  **Invariant: SERV‑INV‑3 (Outcome anchoring).**
  If both `deliveryWorkRef` and `promisedOutcomeSpecRef` are present, then the cited Work instance(s) either:
  (i) explicitly assert `deliversPromisedOutcome(deliveryWorkRef, promisedOutcomeSpecRef)` (A.2.3:8.1), or
  (ii) provide sufficient I/O/Δ evidence anchors for that relation to be derived in the Context.

  **Invariant: SERV‑INV‑4 (Unit-of-delivery measurability).**
  If `promiseContentRef.unitOfDelivery` is present, then its `countingRule` is stated (per A.7:5.10.3, with defaults allowed) and the cited Work carries the measurements required by that rule (duration, quantity, cases, kWh, etc).
* `adjudication? : AdjudicationHooks`
  Evidence anchors (e.g., `evidenceRefs`, `carrierRefs`) used for acceptance/breach evaluation when the passage asserts actuals.

Qualifier slots (as needed per A.6.P/A.6.B):

* `scope? : ClaimScope`
* `Γ_time?` (explicit Γ_time selector per A.2.6; time windows are explicit when the surrounding passage is time‑sensitive)
* `viewpoint? : ViewpointRef`
* `referenceScheme? / representationScheme?` (only when needed)

**Guidance (didactic).** In normative prose, prefer facet‑explicit predicates: if a predicate targets a specific facet (addressability, deontic force, actuals, mechanism), apply it to the corresponding slot rather than to an untyped “service” noun phrase. (Enforced by CC‑A.6.8‑3/4/6/9.)

**Agency + grounding clarifications (normative).**

* The **promise content** (`promiseContentRef`) is *promise content*; it does not act, deploy, crash, or guarantee. It can be **published** (via a carrier) and **used as payload** of a commitment.
* The **promisor / commitment‑holder** is the **provider principal** (or its role assignment) unless the Context explicitly models a system as an agent with standing. *(See CC‑A.6.8‑8.)*
* The **access point** and **delivery system** are typically *instruments/realizers*. The linkage to the accountable principal is expressed via an explicit relation kind (e.g., operated‑by / owned‑by / authorized‑by / fronts / routes‑to). *(See SERV‑WF‑1.)*

**Well‑formedness constraint: SERV‑WF‑1 (Explicit relation typing in bundles).**
When a `serviceSituation(…)` binds a principal/role assignment to systems (access point / delivery system), the relation kinds are explicit (prefer A.6.6 base relations when available). **Implicit “system implies provider” readings are invalid.**
* Mechanism/process claims target `deliverySystemRef` and/or `deliveryMethodRef` (and sometimes `accessSpecRef` if the claim is strictly about interface signature), not `promiseContentRef`. *(See CC‑A.6.8‑9.)*

**Well‑formedness constraint: SERV‑WF‑2 (Accountable subject present when binding is asserted).**
If `serviceSituation(…)` includes `commitmentRef` and/or `promiseActRef`, then it also includes an accountable subject slot:
`(commitmentRef ∨ promiseActRef) ⇒ (providerAssignmentRef ∨ providerPrincipalRef)`.
This prevents “floating” commitments/acts that can’t be routed to a holder/authorizer.

**Facet→Kind map (didactic, normative).** The bundle exists precisely because these facets are **different kinds** and therefore admit different predicates:

| Facet (slot) | Canonical FPF object | Kind family (A.7 / I‑D‑S) | Typical predicates that *belong* here |
| --- | --- | --- | --- |
| `promiseContentRef` | `U.PromiseContent` | **Episteme** (promise content) | states preconditions/outcomes; defines acceptance criteria; constrains what counts as fulfilment |
| `promisedOutcomeSpecRef` | `U.OutcomeSpec` | **Episteme** (outcome template) | constrains delivery work and/or delivered state; supplies the outcome target for acceptance; can be decomposed into work/result clauses |
| `providerAssignmentRef` | `U.RoleAssignment` | **Role assignment** (who is accountable) | is accountable; is the provider; bears duty; is authorized to promise |
| `providerPrincipalRef` | (derived from role assignment) | **Agent / principal** (responsible party) | holds commitments; is liable; delegates; authorizes carriers/systems |
| `deliverySystemRef` | `U.System` | **System** (realizer) | implements/realizes; contains components; has failure modes; produces operational evidence |
| `accessPointRef` (“server”) | `U.System` | **System** (addressable) | call/invoke/restart/down/latency |
| `accessSpecRef` | `U.MethodDescription` | **Episteme** (interface/spec) | versioned; published; compatible |
| `deliveryMethodRef` | `U.MethodDescription` | **Episteme** (procedure/runbook) | steps/controls; escalation; timing model; safety constraints |
| `commitmentRef` | `U.Commitment` | **Deontic object** (binding) | must/shall/obligated; breachable; has holder and counterparty |
| `promiseActRef` | `U.SpeechAct` | **Work event** (communicative) | promised/accepted/announced |
| `deliveryWorkRef` | `U.Work` | **Work event** (operational) | executed; incident occurred; evidence produced |

#### A.6.8:4.3 — Facet headwords (mandatory lexical rule)

In normative prose, **replace the head word “service”** with one of the following facet head phrases:

1. **promise content** (or **service offering clause** / **service promise clause**) — promise content (`promiseContentRef : PromiseContentRef`, i.e., `U.PromiseContent`)
2. **promised outcome spec** (or **promised deliverable spec**) — what is promised as an outcome template (work‑only / result‑only / composite) (`promisedOutcomeSpecRef`)
3. **service provider role** — the provider role kind (`providerRoleRef : RoleRef`) when the text is about role structure (not about actuals)
4. **service provider principal** (or **service provider (role enactor)**) — the accountable provider that can hold commitments (`providerAssignmentRef` / `providerPrincipalRef`)
5. **service delivery system** (or **service realization system**) — the system that performs/realizes delivery (`deliverySystemRef : SystemRef`)
6. **service access point** (or **service endpoint**) — addressable entrypoint (`accessPointRef : SystemRef`); this is the “thing you can call/visit”
7. **service access spec** (or **service interface spec**) — request‑facing interface/method description (`accessSpecRef : MethodDescriptionRef`)
8. **service delivery method** (or **service method** / **service runbook** / **procedure**) — internal procedure for fulfilment (`deliveryMethodRef : MethodDescriptionRef`)
9. **service commitment** — deontic binding (`commitmentRef : CommitmentRef`)
10. **service promise act** (or **promissory speech act**) — speech act (`promiseActRef : SpeechActRef`)
11. **service delivery work** (or **service run / fulfillment work**) — execution episode (`deliveryWorkRef : WorkRef`)

**SERV‑LEX‑3 (Family‑name modifier + shorthand, normative).**
The facet head phrases above are **canonical** for RPR‑SERV. In normative prose, authors SHALL use these phrases (including the family‑name modifier **service**) as the primary surface forms for the facets.
The modifier **service** inside these phrases is not an “unqualified service” use and does not itself trigger further unpacking.
For readability, a local shorthand MAY be introduced by parenthetical declaration immediately after the canonical phrase, and then used consistently within that declared scope (for example: “service delivery system (delivery system)”). A conforming text SHALL NOT introduce multiple shorthands for the same facet, and SHALL NOT reuse a shorthand for a different facet.
In code identifiers, slot names (e.g., `deliverySystemRef` in `serviceSituation(…)`), and diagrams/tables, the modifier MAY be omitted without an explicit shorthand declaration, because the surrounding construct already binds the facet.

**Cluster note (server/provider) — heuristics (informative).**
* If the draft uses **server** as a synonym for “the service”, it usually denotes the **service access point** (or host system), unless the domain’s “server” is explicitly a person (e.g., restaurant).
* If the draft uses **service provider** but then predicates deployment/restart/latency, it usually denotes a **service delivery system** or **service access point**, not an accountable principal.
* If the draft uses **service provider** but then predicates “guarantees / obligated”, it usually denotes the **service provider principal** plus an explicit **service commitment**.
* If a passage attributes promissory agency to a machine (“the server promises”), treat the machine as a carrier/witness unless the Context explicitly grants it standing as an agent.

(Normative enforcement is via CC‑A.6.8‑1 and CC‑A.6.8‑8.)

#### A.6.8:4.4 — Addressability rule (the “can you call it?” test)

If the draft sentence implies *addressability* (verbs like **call/invoke/request/visit/go to/connect to/route to/deploy/restart/scale**), then the referent MUST be a **service access point** (`accessPointRef : SystemRef`) or a **work episode** (`deliveryWorkRef`), never the promise content.

#### A.6.8:4.4b — Method/mechanism rule (the “how does it work?” test)

If the draft sentence asserts or explains *how the service works* (verbs like **implement/realize/work by/uses/consists of/pipeline/algorithm/workflow/runbook/process steps**) then the referent MUST be a **service delivery system** (`deliverySystemRef`) and/or a **service delivery method** (`deliveryMethodRef`).

If the draft uses *service* as the name of a **promised work method** (common in plain language: “cleaning”, “repair”, “haircutting”), treat that as part of the promise by constraining the `U.OutcomeSpec.workSpec.methodConstraintRef` (what is promised). Keep `deliveryMethodRef` for the provider‑internal runbook/procedure that realizes the promise (how it is executed).

If the draft sentence is specifically about the **externally visible signature/shape** (endpoints, request/response schema, SOP steps visible to consumers), route it to **service access spec** (`accessSpecRef`).

A conforming text **SHALL NOT** attach mechanism/process predicates to the **promise content**; the clause may constrain outcomes or acceptance criteria, but mechanism claims belong to design/method artefacts. *(See CC‑A.6.8‑9.)*

#### A.6.8:4.5 — Deontic rule (the “must/shall” test)

If the sentence contains deontic force (**must/shall/guarantee/obligated/SLA**), the referent MUST include a **service commitment** slot, and the deontic language MUST attach to the commitment/holder, not to the clause or to the access point.

When the prose needs a subject, prefer: **“the service provider principal SHALL … under commitment C”** rather than “the service SHALL …”.

**No hidden agency rule (normative):** A conforming text **SHALL NOT** use an access object (e.g., endpoint/access point) as the grammatical subject of an RFC‑keyword sentence. It **SHALL** use the accountable principal (or role assignment) as subject and then state the operational condition on the access point as a predicate/evidence claim. *(See CC‑A.6.8‑4 and CC‑A.6.8‑8.)*

#### A.6.8:4.6 — Speech‑act rule (the performative verb test)

If the sentence uses performatives (**promise/offer/accept/agree/commit/announce/publish**), the referent MUST include a **service promise act** (`promiseActRef`) and must not collapse the act into the clause.

If a server/webpage/API response is involved, a conforming text **SHALL** treat it as a **carrier/witness** of the promise act unless the Context explicitly grants it standing as an agent. A conforming text **SHALL** keep the promissory actor/authorizer aligned with the provider principal.

#### A.6.8:4.7 — Runtime/telemetry rule (the “actuals” test)

If the sentence asserts actuals (**down/slow/99.9% last week/latency is X/incident occurred**), the claim MUST be routed to **work + carriers/evidence** (deliveryWorkRef + witnesses), not to the clause.

If an actual is used in a conformance block, KPI, or acceptance argument, it MUST cite the underlying `U.Characteristic` and measurement procedure/evidence carrier (C.16/C.25), with pinned `{UnitType, ScaleKind, ReferencePlane, EditionId}`; otherwise it is prose only and MUST NOT be treated as a verified SLO/SLA measurement.

When needed, also name whether the actual is about the **access point** (entrypoint symptoms) or the **delivery system** (realizer symptoms). “Down” can be about the gateway even when the backend is fine; the pattern forbids collapsing those.

#### A.6.8:4.8 — Change‑class lexicon (service‑specific narrations)

When the draft describes “service changes”, narrate changes using stable change classes (A.6.P), specialized to the serviceSituation lens:

* `declareRelation(serviceSituation(…))` (introduce the bundle)
* `withdrawRelation(serviceSituation@ed=k)` (retire the bundle)
* `retargetParticipant(accessPointRef := …)` (move the access point / endpoint host)
* `retargetParticipant(deliverySystemRef := …)` (change the realizing delivery system; e.g., re‑platforming)
* `retargetParticipant(providerAssignmentRef := …)` (change provider role‑enactor; outsourcing / org change)
* `reviseByValue(accessSpecRef := …)` (edit interface description content)
* `reviseByValue(deliveryMethodRef := …)` (edit runbook/workflow/procedure)
* `reviseByValue(promiseContentRef := …)` (edit promise content; typically new edition)
* `changeRelationKind` is not applicable here unless splitting the family (rare)
* `rescope`, `retime(Γ_time)`, `refreshWitnesses(witnesses := …)` as required

#### A.6.8:4.9 — Disambiguation guide (rewrite/selection)

If the draft says:

* “**the service** is deployed/restarted/scaled/called” → rewrite as **service access point** (system) or **service delivery work** (deployment work), and (optionally) attach it to a `serviceSituation`.
* “**the service** promises/guarantees X” → rewrite as **promise content** (promise content), and if “guarantees” is deontic, also introduce **service commitment** held by the **service provider principal**.
* “**the service** is down/slow/has 5xx” → rewrite as **service access point** (down) and/or **service delivery work** (incident/run), with evidence.
* “we **promised** the service” / “we **agreed** the service” → rewrite as **service promise act** + **promise content** (+ commitment if binding).
* “**the service provider** guarantees X” → rewrite as **service provider (role enactor)** + **service commitment** (+ promise content as payload).
* “**the server** is down / slow / restarted” → rewrite as **service access point** (server/host system) and/or delivery work, not as clause.
* “**the service** is implemented by / realized by / works by doing Y” → rewrite as **service delivery system** and/or **service delivery method** (and keep the clause separate as the outcome constraint).
* “**the service** API signature / endpoint schema / request format is …” → rewrite as **service access spec**.
* “the service ticket / service request” → rewrite as **ticket** / **request work item**; “service” is adjectival legacy and must be eliminated or mapped via LEX.

### A.6.8:5 - Archetypal grounding

**Tell.** A “service” is not a single thing. In normative prose you MUST name which facet you mean, and (when needed) tie facets together via a `serviceSituation(…)` record so readers can follow accountability, access, deontics, and evidence without guessing.

#### Show 1 — System archetype (microservices + SRE)

**Draft (ambiguous):**
“Payments service is down; the service guarantees 99.9% uptime; we will restart the service.”

**Unpacked (facet‑explicit):**

* “The **Payments service access point** (the Payments API ingress/endpoint host) is down.”
* “The **Payments service delivery system** (the Payments backend realizer) is degraded (symptom attribution is explicit).”
* “The **Payments service access spec** (e.g., OpenAPI/endpoint contract) defines the request/response interface.”
* “The **Payments promise content** states target availability `SLO=99.9%` over `Γ_time=30d` (promise content).”
* “The **service commitment** held by the **service provider principal** binds them to that clause.”
* “The **service delivery work** `Incident#2025‑…` records outage evidence and the restart action; the runbook used is the **service delivery method**.”

**Optional `serviceSituation` bundle (sketch):**

* `serviceSituation( promiseContentRef=PaymentsAvailabilityClause, providerRoleRef=PaymentsPlatform#ServiceProviderRole, providerPrincipalRef=PaymentsPlatformTeam, accessSpecRef=PaymentsAPIv2, accessPointRef=PaymentsAPIIngressProd, deliverySystemRef=PaymentsBackendProd, deliveryMethodRef=PaymentsIncidentRunbook@ed=…, commitmentRef=AvailabilityCommitment@ed=…, deliveryWorkRef=Incident#…, Γ_time=Rolling30d, witnesses={SLOReport#…, IncidentLog#…} )`

#### Show 2 — Episteme archetype (physical/human service)

**Draft (ambiguous):**
“The auto service accepts walk‑ins and promises repair in 2 days.”

**Unpacked (facet‑explicit):**

* “The **service access point** is the *Auto Repair Shop front desk* (an addressable facility).”
* “The **service access spec** is the *intake procedure* (how to request/submit a car).”
* “The **promise content** promises ‘repair completed within 2 business days’ given stated preconditions.”
* “The **service delivery method** is the *shop workflow* (inspection → parts ordering → repair → QA → handover).”
* “The **service provider principal** is the shop entity that can hold a commitment (not the front desk as an access point).”
* “If advertised as binding, introduce a **service commitment** held by the shop’s provider role.”
* “Each repair job is **service delivery work** with evidence (work order, timestamps, acceptance sign‑off).”

### A.6.8:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Gov bias:** favors explicit accountability (provider role + commitment) and audit surfaces (witnesses); increases enforceability but raises authoring burden.
* **Arch bias:** encourages bundle/record lenses and explicit interfaces; may feel heavyweight for informal notes.
* **Onto/Epist bias:** strongly separates clause vs system vs work vs deontic; prevents category errors but reduces metaphor-friendly storytelling.
* **Prag bias:** optimizes for cross-team readability and reduced rework; may require refactoring existing prose at scale.
* **Did bias:** enforces teachable tests (“can you call it?”, “is it deontic?”, “is it actuals?”); can appear prescriptive but improves onboarding.

### A.6.8:7 - Conformance Checklist (CC‑A.6.8)

0. **CC‑A.6.8‑0 — UTS/LEX block exists for the service cluster.**
   Any document that applies this pattern (or that introduces normative “service” language) SHALL publish:
   (a) a local **UTS block** (F.17), and
   (b) paired **LEX‑BUNDLE entries** (E.10) for the Tech/Plain twins and PTG stances used here.
   +   Minimum cluster coverage SHALL include: `service`/`services`, `service provider`, `server`, `microservice`/`microservices` **when present in the source prose**, plus the chosen facet head phrases. If the document uses “API service / service interface / service access” or SLA/SLO/service‑level language, the local UTS/LEX block SHALL include those surface forms as well.
   Each SenseCell SHALL cite ContextName@Edition; cited contexts SHOULD not be “FPF only”.
   Any newly introduced facet head phrase SHALL have an explicit Mint/Reuse decision (F.8) and SHOULD have a Name Card rationale (F.18).

1. **CC‑A.6.8‑1 — Unqualified “service” (and cluster stand‑ins) is forbidden in normative prose.**
   A conforming boundary/spec text SHALL NOT use **service** as an unqualified head noun, and SHALL NOT use **server** or bare **service provider** as untyped stand‑ins for the same collapsed bundle.
   Every such occurrence SHALL be rewritten to a facet head phrase (promise content / promised work‑kind / service provider role or principal / service delivery system / service access point / service access spec / service commitment / service promise act / service delivery work) or replaced with the correct underlying FPF object (team, ticket, workflow, system, etc.).
   The facet head phrases in §4.3 are **canonical**; using **service** as the family‑name modifier inside those phrases is permitted and does not itself trigger further unpacking. Any local shorthand that drops the modifier is allowed only under SERV‑LEX‑3.
   *Exception:* direct quotations may retain the original surface form, but the surrounding normative prose SHALL immediately provide an unpacking rewrite.

2. **CC‑A.6.8‑2 — `U.PromiseContent` is referred to as a “promise content” in prose.**
   When the intended referent is `U.PromiseContent`, authors SHALL use “promise content” (or “service promise clause”) as the head phrase and SHALL NOT rely on the bare word “service”.

3. **CC‑A.6.8‑3 — Addressability implies `accessPointRef` (system), not clause.**
   Any statement implying invocation/connection/deployment/restart SHALL target a service access point (`SystemRef`) and/or delivery work, never a promise content (`U.PromiseContent`).

4. **CC‑A.6.8‑4 — Deontic language requires a commitment.**
   Any normative “must/shall/guarantee/SLA” statement about service delivery SHALL introduce (or reference) a `U.Commitment` and attach the deontic force to that commitment/holder.
   In addition, a conforming text SHALL NOT use a service access point / server as the grammatical subject of an RFC‑keyword sentence; the subject is the accountable provider principal (or role assignment), with access‑point conditions stated as predicates/evidence.

5. **CC‑A.6.8‑5 — Performative verbs require a speech act.**
   Any statement using “promise/offer/accept/agree/announce/publish” about the service SHALL reference a `U.SpeechAct` (promise act) and SHALL NOT collapse it into the clause.

6. **CC‑A.6.8‑6 — Actuals require work + evidence.**
   Any claim about runtime state/telemetry/incidents SHALL be routed to `U.Work` plus carrier/evidence references; it SHALL NOT be stated as a property of the promise content.

7. **CC‑A.6.8‑7 — Bundle lens is used when multiple facets are in play.**
   When a passage simultaneously discusses two or more facets (e.g., clause + endpoint + SLA + incident), the author SHOULD provide a `serviceSituation(…)` record (or equivalent explicit slot binding) so readers can track the linkage without guesswork.
   When a `serviceSituation(…)` record is provided, it SHALL satisfy SERV‑INV‑1, SERV‑INV‑2, and SERV‑WF‑1 from §4.2.
   When a `serviceSituation(…)` record is provided and it includes `commitmentRef` and/or `promiseActRef`, it SHALL also satisfy SERV‑WF‑2.

8. **CC‑A.6.8‑8 — Commitments and promises have an accountable principal.**
   Any statement that introduces a **service commitment** or **service promise act** SHALL name (directly or via role assignment) the **service provider principal** who is the holder/authorizer. A conforming text SHALL NOT attribute commitments/promises to a bare access point/server unless the Context explicitly models it as an agent with standing (and that modelling is declared).

9. **CC‑A.6.8‑9 — “How it works” claims route to method/system, not to the clause.**
   Any statement about implementation, mechanism, workflow, runbook, or process SHALL target **service delivery system** and/or **service delivery method** (or **access spec** if it is strictly interface‑signature). It SHALL NOT be stated as a property of the promise content.

### A.6.8:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern:** “The service is deployed on Kubernetes.”
  **Fix:** “The **service access point** (deployment) is deployed on Kubernetes.”

* **Anti‑pattern:** “The service guarantees X.”
  **Fix:** “The **promise content** states target X; the **service commitment** guarantees X.”

* **Anti‑pattern:** “The service provider guarantees X.”
  **Fix:** “The **service provider (role enactor)** holds a **service commitment** that guarantees X; the **promise content** is the promise content.”

* **Anti‑pattern:** “The server provides the service (as if server=promise).”
  **Fix:** “The **service access point** (server/host system) provides access; the **promise content** is promise content; any ‘must/shall’ binds via **service commitment**.”

* **Anti‑pattern:** “The service works by doing Y / is implemented with Z.”
  **Fix:** “The **service delivery system** works by doing Y / is implemented with Z; the **service delivery method** (runbook/workflow) is …; the **promise content** constrains outcomes/acceptance.”

* **Anti‑pattern:** “We promised the service.”
  **Fix:** “We performed a **service promise act** that published the **promise content** (and instituted a commitment if binding).”

* **Anti‑pattern:** “Service is down (therefore contract violated).”
  **Fix:** “The **service access point** is down (actual). Contract breach evaluation is a separate claim comparing actuals (work/evidence) to the clause + commitment.”

* **Anti‑pattern:** “Service and API are used interchangeably.”
  **Fix:** Use **service access spec** for the API description; use **service access point** for the addressable system; use **promise content** for promise content.

### A.6.8:9 - Consequences

* **Pros:**

  * Removes the incentive to keep “service” conveniently vague.
  * Enables A.6.B routing: clause (L), commitment (D), acts/work/evidence (E), mechanisms/interfaces (A/L depending on placement).
  * Makes incident/SLO/SLA discourse structurally sound and reviewable.

* **Cons:**

  * Increases verbosity and requires refactoring existing prose.
  * Requires authors to learn (and consistently apply) facet headwords.

**Adoption test (1 minute).**
After refactoring any normative section that contains ≥ 10 occurrences of the “service” cluster, you can answer “yes” to all of:
1) Unqualified head‑noun “service” occurrences in normative prose are **0** (CC‑A.6.8‑1).
2) Every deontic (“must/shall/guarantee/SLA”) sentence about service delivery references a **service commitment** / `U.Commitment` (CC‑A.6.8‑4).
3) Every runtime/telemetry “service is down/slow/…” claim is routed to **work + evidence** and, when relevant, distinguishes access‑point symptoms from delivery‑system symptoms (CC‑A.6.8‑6 + §4.7).

### A.6.8:10 - Rationale

The ambiguity here is not a simple synonym problem; it is a **bundle‑collapse problem**. “Service” routinely stands in for different ontological categories (episteme content, system, event, deontic binding). Since the word is too entrenched to ban entirely, the least‑surprising stable repair is:

* keep “service” only as a *family name* in informal discussion, but
* in normative prose always name the **facet** and, when needed, explicitly bind facets via a stable bundle lens.

This aligns with A.6.P’s requirement to replace umbrella tokens with explicit kind+slots forms and to provide rewrite guides and guardrails.

### A.6.8:11 - SoTA-Echoing

> **Informative.** Alignment notes; not normative requirements. This section is written to satisfy the SoTA‑Echo obligations for Architectural patterns (post‑2015, multi‑Tradition; adopt/adapt/reject with reasons).

**Bridge hygiene note.** This section makes **no cross‑Context identity claims** (no implicit “same thing across traditions”). If a later edit wants cross‑Context reuse of terms or structures from external traditions, it must be mediated by explicit Bridges with declared CL (and plane policy where relevant), per the general SoTA/Bridge discipline.

| Tradition (Context) | What this pattern uses | Stance | Primary sources (post‑2015) | Notes / divergence |
|---|---|---|---|---|
| IT service management (ITSM) | Separates promise/value proposition (“offering”) from delivery/operations talk; motivates forcing facet headwords instead of letting “service” float. | Adapt | ITIL 4 Foundation (AXELOS, 2019) | FPF diverges by treating bare “service” as an always‑unpack token in **normative** prose, because ITSM vocabulary is intentionally managerial and polysemous. |
| Enterprise architecture modeling | Distinguishes “service” from “interface” and from “realization/implementation”; motivates the access‑spec vs access‑point vs delivery‑system split. | Adopt/Adapt | The Open Group ArchiMate® 3.1 Specification (2019) | FPF adapts the split by making **promise content** (`U.PromiseContent`) explicit and by making “addressability” a first‑class disambiguation test. |
| Ontology‑driven conceptual modeling (service ontologies) | Distinguishes service offering/commitment from service delivery events; motivates the “PromiseContent + Commitment + Work+Evidence” separation and prevents metonymy between SLA text, promissory act, and delivered outcome. | Adopt/Adapt | *S‑OPL: An Ontology Pattern Language for Service Modeling* (Falbo et al., 2016); *Unified Foundational Ontology (UFO): A Multi‑layered Ontology for Conceptual Modeling* (Guizzardi et al., 2022) | FPF uses this as a semantic anchor for precision restoration, but stays neutral on any single foundational ontology by treating `U.OutcomeSpec` / `U.Commitment` / `U.Work` as minimal cross‑domain pivots. |
| Service‑dominant logic / service science | Treats service as applied capability for another actor’s benefit and emphasizes co‑creation and context; motivates being explicit about roles (provider/customer/beneficiary) and claim scope when “service quality” is discussed. | Adapt | Vargo & Lusch (2016); Vargo & Lusch (2017); *The SAGE Handbook of Service‑Dominant Logic* (Vargo & Lusch, eds., 2018) | FPF does not bake “value co‑creation” into kernel types; it supports it via role modeling + claimScope + explicit commitments rather than via the bare token “service”. |
| Dialogue‑act / speech‑act operationalization | Treats promissory moves as explicit act types; motivates separating promise‑act from promise‑content. | Adopt | ISO 24617‑2:2020 (Dialogue Act Annotation) | FPF diverges by requiring that binding effects are represented as explicit `U.Commitment` objects rather than being inferred from the act alone. |
| SRE / modern operations practice | Keeps interface specs, SLO targets, deployments/endpoints, and incident evidence as separate artefact families; motivates the “actuals → work+evidence” rule and the “access point vs delivery system” split. | Adopt/Adapt | *Site Reliability Engineering* (Beyer et al., 2016); *The Site Reliability Workbook* (Beyer et al., 2018) | FPF adapts SRE practice by routing deontics to commitments (D) and keeping telemetry/incidents as evidence (E), rather than letting “SLO/SLA” prose collapse into the word “service”. |


**Pack binding (status).** No dedicated SoTA Synthesis Pack is cited here yet for the “service polysemy” cluster; if/when such a pack is published, this section SHOULD be updated to cite the relevant ClaimSheet IDs / CorpusLedger entries (and Bridge ids where reuse is asserted) as the auditable anchors for the alignment statements above.

### A.6.8:12 - Relations

* **Specialises:** A.6.P (RPR) for the lexical/semantic ambiguity cluster around “service”.
* **Operationalises + extends:** the lexical disambiguation intent of L‑SERV by making “service” **always‑unpack** in normative prose (and by expanding the cluster to include *service provider* and *server* as co‑moving stand‑ins).
* **Requires (authoring discipline):** a local UTS block (F.17) and published Tech/Plain twins (E.10) for the service/provider/server cluster; this is the “anti‑FPF‑only loop” guard.
* **Coordinates with:** A.6.C (contract bundle unpacking). When contract-language includes *service* tokens, apply RPR‑SERV first to select **promise content** vs **commitment** vs **access point/system** vs **work/evidence**, then route the resulting atomic statements through A.6.C → A.6.B (L/A/D/E).

### A.6.8:End

## A.6.9 - U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)

> **Type:** Architectural (A) — A.6.P specialisation (RPR)
> **Status:** Stable
> **Normativity:** Normative
> **Placement:** A.6 cluster; immediately after A.6.8
> **Builds on:** A.6.P (RPR); F.0.1:2.3 (Explicit Bridge Principle); E.10.D1 (Context discipline); E.10.U9 (Alignment/Bridge lexical discipline); F.9 (Bridge discipline + reasoning primitives); F.7/F.8 (Concept‑Set rows & weakest‑link); F.5 (labels); A.7 (Strict Distinction: lanes + stance hygiene); E.19 (normative precision)
> **Coordinates with:** E.17 (Viewpoints / Views / Correspondences, when the prose is really about views/projections); C.3.3 (KindBridge, when the claim is about kind/classification transfer); A.6.6 (Identification/indexing, when the umbrella is really about IDs); Concept‑Set row scope rules; E.10 lexical SD (umbrella tokens); B.3 penalty conversion (if used)
> **Delta‑Class:** Δ‑3 (new normative pattern; additive; does not change existing kernel semantics)
> **Impact radius:** any document, table row, or boundary statement that asserts cross‑context sameness/compatibility/alignment between SenseCells, or collapses **A.7 lanes** / `CHR:ReferencePlane`s under umbrella “same/equivalent/…” wording
> **Mint vs reuse:** reuses `Bridge`, `BridgeKind`, `dir`, `CL`, `Loss`, `scope`; adds A.6.9‑specific Bridge‑Card qualifiers (`Γ_time`, `facetSpan`) (annotation slots; do not alter the kernel Bridge predicate); does not mint new kernel relations
> **Rationale witness:** required (in decision/publication lanes) for (i) declaring any Bridge with `scope` stronger than **Naming‑only**, and (ii) any strengthening edit (`scope` upgrade or `CL` increase). Provide the rationale as `witnessRefs` (review note, evaluation suite, decision log excerpt, etc.) and, where your process uses it, link the change to a DRR entry.

### A.6.9:1 - Problem frame

Cross‑Context prose routinely uses umbrella predicates (“same”, “equivalent”, “align”, “map”, “matches”, “corresponds”) to compress a multi‑dimensional claim into a single adjective.

In FPF terms, this is almost never a single claim. It is a *Bridge situation* that typically contains, at minimum:

* two (or more) **Contexts** (`U.BoundedContext`; each with its own idiom);
* a potentially hidden **direction** (A→B is not B→A);
* a hidden **degree of fit** (≈ vs ⊑/⊒ vs ⋂ vs ⊥, or interpretation‑only);
* near‑inevitable **loss/distortion** on transfer;
* a (usually implicit) **edition / time‑slice basis** for both endpoints and the correspondence judgement (`Γ_time`);
* a usually implicit **facet span** (`facetSpan`; “which aspects are being aligned?”) — the correspondence is often a *partial lens*, not whole‑cell sameness;
* a critical ambiguity between **lexical synonymy / translation** (“same word/label”), **referential co‑denotation** (“same referent under different IDs”), and **value‑level normalization** (“equivalent after φ‑normalization / unit conversion”).
* a critical ambiguity between **explaining** a correspondence and **licensing substitution**.

A.6.9 is the RPR specialisation that makes this structure explicit and prevents accidental “global identity” claims when the author’s intent is merely naming convenience or interpretive help.

### A.6.9:2 - Problem

When an umbrella predicate is used as if it were a single relation, readers (and downstream editors) silently choose defaults:

* **Symmetry hallucination:** “equivalent” is read as symmetric even when the intended relation is ⊑/⊒ (directional).
* **Scope creep:** “align/map” is read as substitution‑eligible, leaking into Role Assignment & Enactment or Concept‑Set row scopes.
* **Loss erasure:** “same” implies lossless transfer even when units, granularity, preconditions, or stance differ.
* **License confusion:** “explain X using Y” is mistaken for “Y can stand in for X”.
* **Implicit inversion:** later prose uses the inverse direction without an explicit redeclaration, breaking the “no silent inversion” rule.

The result is not merely imprecise wording: it changes what inferences are considered safe, and it pollutes Concept‑Set row scopes via unnoticed weakest‑link violations.

It also breaks **temporal coherence**: if the underlying canons (glossaries, schemas, code lists, ontologies) evolve, an un‑pinned “equivalent” claim silently becomes a claim about *two different editions at once*.

### A.6.9:3 - Forces

| Force                      | Pull                                            | Push                                                                      |
| -------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------- |
| Brevity                    | One word (“same”) is fast.                      | Fast words hide multi‑slot claims and create accidental licences.         |
| Practical interoperability | Teams want “one label” across artefacts.        | Shared labels are not structural sameness; they require scope discipline. |
| Direction sensitivity      | Many correspondences are one‑way.               | Natural language defaults to symmetry (“equivalent”).                     |
| Partial overlap is common  | Real systems rarely coincide perfectly.         | “Same” collapses overlap vs inclusion vs disjointness.                    |
| Evidence evolves           | Fit changes as counter‑examples are discovered. | Without change classes, people “re‑align” without recording what changed. |
| Version drift              | Canons/models are versioned and revised.        | Without `Γ_time` pinning, “equivalent” becomes temporally incoherent.     |
| Safety of reuse            | Substitution can reduce work.                   | Substitution without explicit `CL`/Loss is a latent defect.               |

### A.6.9:4 - Solution

Treat every cross‑Context umbrella‑sameness statement as an **RPR trigger** that must be rewritten into an explicit **Bridge claim** (F.9) with declared attributes.

This specialisation follows the A.6.P RPR envelope: it (i) defines a **trigger rule**, (ii) fixes the **stable lens** (Bridge Card), (iii) fixes a **minimal contract skeleton**, (iv) provides a **disambiguation guide**, and (v) standardises **change narration** for this class of ambiguity.

#### A.6.9:4.0 - Trigger rule (normative)

An occurrence SHALL be treated as an A.6.9 trigger when **either** (i) `CtxA ≠ CtxB`, **or** (ii) the statement collapses **A.7 lanes** (`Object | Description | Carrier`) or `CHR:ReferencePlane`s under an umbrella sameness predicate, and the prose (or a table row comment) uses any of the following as if they were a single relation:

* **Umbrella predicates**: “same”, “identical”, “equivalent”, “align”, “map”, “match”, “correspond(s)”, and close variants.
* **Reuse‑intent shorthands** that often smuggle licences: “treat as”, “reuse”, “share”, “unify”, “canonical”, “single source of truth”, “synced”, “normalized”, “one‑to‑one”, “same ID”, “mirrors”.
* **Endpoint umbrellas** in the presence of a cross‑context sameness claim (e.g., “the system/service/model/table/class”) — this is simultaneously an endpoint‑identity problem and a Bridge problem.

**ID/reference caveat.** Tokens like “same ID”, “same key”, “one‑to‑one”, “synced”, or “mirrors” often denote an **identification/indexing** claim or an **operational mapping artefact** rather than a sense‑level correspondence. If an ID claim is being used as a proxy for meaning (“same ID ⇒ same thing/role”), split it into (i) an explicit identification/indexing claim (A.6.6) and (ii) any Bridge claim about meaning (this pattern). Keep code/ETL facts as `witnessRefs`; they do not determine `kind/CL/Loss/scope` by themselves.

**Multilingual caveat.** In non‑English prose, treat local‑language equivalents of the umbrella tokens as the same trigger class (e.g., Russian “эквивалентно”, “соответствует”, “это одно и то же”).

**Lane/plane‑only caveat.** If `CtxA = CtxB` and the trigger is solely a lane/plane collapse, repair lane/plane typing first (A.7 / declared `Φ_plane`). You MAY satisfy this pattern by re‑typing endpoints + adding an explicit non‑licensing marker; do not invent a Bridge unless you actually need an auditable cross‑Context licence record.

When triggered, the author SHALL do exactly one of:

1. **Rewrite into an explicit Bridge** (BridgeId or inline Bridge Card) with the required slots (`kind/dir/CL/Loss/scope` at minimum), or
2. **Rewrite into an Explanation‑only form**: either declare an **Explanation‑only Bridge** (`scope=Explanation‑only`) or keep the statement as Plain explanatory prose with an explicit **non‑licensing marker** (“no Bridge licence; do not substitute; do not justify rows”). In either form, it MUST NOT be used to justify Concept‑Set rows, cross‑Context reuse, or substitution.

The repair has three moves:

**Terminology discipline (Tech register).**
* In this spec, **Context** means `U.BoundedContext` (E.10.D1 / D.CTX).
* Use **lane** for the A.7 split (**Object | Description | Carrier**).
* **CHR:ReferencePlane** is reserved for world/concept/episteme crossings; do **not** use it as a synonym for lane.

0. **Resolve endpoints as SenseCells (and pin editions where relevant).** If the surface text uses pronominal/metonymic bundles (“the system”, “the model”, “it”, “this class”, “that table”, “the service”), treat this as an endpoint‑identity problem first: enumerate candidates and select the intended `σ@Ctx` endpoints (Candidate‑Set Note, A.6.P:4.0b). Also check **lane** and **stance/time tags**: ensure each candidate sits on the intended A.7 lane (**Object | Description | Carrier**) and record any time‑stance tags on the relevant artefacts/sources (e.g., `DesignRunTag = design | run`) that affect substitution safety. Do not treat `DesignRunTag` as a separate Context; it is a time tag on artefacts/sources. If the only crossing is design↔run, route via an Interpretation Bridge (`kind=⇄ᴅʀ`, `scope=Explanation‑only`) unless you have a separately justified substitution Bridge within a fixed lane. If the triggering token is an identifier/key/code, repair it as a Carrier‑lane identification/indexing claim first (A.6.6), and only then decide whether there is also a sense‑level Bridge claim. If the ambiguity is actually a **CHR:ReferencePlane** mix (e.g., “a database column” vs “a real‑world attribute”), treat that as a ReferencePlane issue: restate endpoints on a single `CHR:ReferencePlane`, or route the crossing through a declared `Φ_plane` policy before attempting any substitution licence. In decision/publication lanes, endpoint ambiguity is fail‑closed: if the intended endpoints cannot be resolved from local cues and `witnessRefs`, keep the sentence as Plain explanatory prose (or an Explanation‑only Bridge) and do not use it to justify cross‑Context reuse, Concept‑Set rows, or substitution.
   * **Modularity note:** if the endpoint token itself is a known umbrella term (e.g., “service”), apply the relevant endpoint‑disambiguation RPR first (e.g., A.6.8 for “service”), then return here for the cross‑context sameness predicate.
   * **View/projection note:** if the prose is primarily about **views/projections/correspondences** rather than sameness licences, coordinate with E.17 (multi‑view describing). You may still need a Bridge for naming/substitution licences, but do not let “is a view of” silently become “is the same as”.
   * **Edition / canon pinning (Γ_time).** If either endpoint’s meaning is fixed by a versioned canon (glossary, schema, code list, ontology, model release), record the specific editions (or “as‑of” date) used to make the correspondence judgement, and carry that as `Γ_time` on the Bridge Card. If you cannot state `Γ_time` in decision/publication lanes, fail‑closed: keep the prose Explanation‑only and do not justify rows or substitution.
   * **Ontology category sanity (Kinds vs instances vs values).** Before declaring `kind/dir/CL/scope`, check that the endpoints live at compatible ontological strata (e.g., *Kind/classification* vs *instance* vs *measurement value*). If the “equivalence” is really a kind/classification transfer, coordinate with **C.3.3 KindBridge**; if it is a value‑normalization claim, treat it as a Measurement‑family bridge and make the normalization channel explicit in `Loss` (and/or `witnessRefs`).

1. **Replace the umbrella predicate with a Bridge reference** (or an inline Bridge Card).
2. **Choose the Bridge’s kind, direction, licence scope, `CL`, and Loss notes explicitly**, instead of letting readers infer them.
3. **Separate “interpretation” from “licence”** by using the Bridge scope rules: Explanation‑only vs Naming‑only vs Substitution‑eligible.

This is a pattern specialisation of A.6.P: it provides the stable lens, contract skeleton, change‑class lexicon, and a disambiguation guide tailored to cross‑Context “sameness”.

#### A.6.9:4.1 - Stable lens

**Stable lens (QRR):** the **Bridge Card** (F.9) used as a qualified relation record for cross‑Context sameness claims.

A conforming cross‑Context claim is expressed as a Bridge declaration:

```
⊢ Bridge(σA@CtxA, σB@CtxB) : ⟨senseFamily, kind, dir, CL, Loss, scope⟩
```

**A.6.9 qualifiers (pattern‑level; Bridge‑Card annotations).** A.6.9 additionally requires:
* `Γ_time` — edition/as‑of basis for the correspondence judgement (MUST in decision/publication lanes),
* `facetSpan` — the facet‑preservation span when the correspondence is not whole‑cell.
These live on the Bridge Card as qualifiers; they do **not** change the kernel Bridge predicate signature.

This record is a **conceptual judgement and licensed‑use record** (a thought‑format), not an ETL pipeline, API guarantee, or a “mapping implementation”. Operational mapping artefacts (aligner models, lookup tables, transformation code) belong in `witnessRefs` and do not erase `Loss` or relax `scope` by themselves.

**Non‑inheritance note.** A Bridge relates two local senses; it does **not** make `CtxA` a sub‑Context of `CtxB` (or vice versa), and it does not create “global identity” between Contexts.

**Kernel restraint reminder.** Bridges translate between local senses; they do **not** justify minting a new global `U.Type` by “sameness”. If the desired outcome is a new shared type/kind, route to the type‑minting discipline (A.11) and keep Bridges as translators.

**Direction note (avoid a common misread).** `dir = A↔B` expresses *symmetry of the correspondence* (e.g., for `kind∈{≈,⋂,⊥}` or for `kind=⇄ᴅʀ`), not “two substitution licences for free”. **Role Assignment & Enactment substitution is always directional** and must be stated as such (A→B). `scope=Type‑structure` is structural reuse, not substitution.

**Memory hook:** if the Bridge Card does not fit on one screen, you are describing the Contexts, not the Bridge.

#### A.6.9:4.2 - Explicit contract skeleton

A.6.9 fixes the minimal slot set that must be made explicit whenever a cross‑Context (or cross‑lane / cross‑plane) “same/equivalent/align/map/…” assertion appears.
| Slot                 |               Required | Meaning / constraints                                                                                                                  |
| -------------------- | ---------------------: | -------------------------------------------------------------------------------------------------------------------------------------- |
| `BridgeId`           |          Yes (if cited) | Required whenever the Bridge is referenced from multiple places, used to justify row scope, or used as a licence in decision/publication lanes. Inline cards MAY omit an id for a single‑use didactic gloss. **When present, the id is a registry reference** (per the F.9 registry‑reference note): check existence / edition pinning, not signature export. |
| `σA@CtxA`, `σB@CtxB` |                    Yes | Endpoints are **SenseCells** (not strings, not “the systems”).                                                                         |
| `senseFamily`        |                    Yes | Use a named family (F.9). For substitution‑capable Bridges, this MUST be a single family (Role / Status / Measurement / Type‑structure / …). If the correspondence crosses families, use an **Interpretation** kind (`⇄ᴅʀ / →ᴍᴇᵃ / →ᴅᵉᵒ`) and record the channel explicitly (e.g., `Method ⇄ᴅʀ Execution`, `Measurement →ᴍᴇᵃ Requirement/Clause`, `Deontic →ᴅᵉᵒ Execution`), keeping `scope=Explanation‑only`. |
| `kind`               |                    Yes | One of the F.9 kinds: `≈ / ⊑ / ⊒ / ⋂ / ⊥ / ⇄ᴅʀ / →ᴍᴇᵃ / →ᴅᵉᵒ`. Use `⊑/⊒` only for defensible inclusion. If you can name a counter‑case that violates inclusion for these endpoints, you do **not** have `⊑/⊒` — use `⋂` or refine endpoints (SenseCell split). |
| `dir`                |                    Yes | Always explicit (F.9). Use `A→B` for any **substitution** claim (Role Assignment & Enactment‑eligible), even when `kind=≈`. Use `A↔B` only to express a symmetric correspondence (or Type‑structure reuse); it does **not** imply bidirectional substitution. **No implicit inversion.** **Inclusion sanity:** when `kind∈{⊑,⊒}`, ensure `dir` matches the intended safe reading (substitution, when allowed, goes **from narrower to broader**); if needed, swap endpoints or declare the inverse Bridge explicitly rather than relying on prose. |
| `Γ_time`             | Yes (in decision/publication lanes); otherwise Should | **Edition / time‑slice basis** for the Bridge judgement. Pin (or reference) the editions of the canons that fix the endpoints’ meanings (glossary/schema/code list/ontology/model release), or state an “as‑of” date for both sides. If endpoint notation already pins editions unambiguously, you MAY set `Γ_time = =endpointPins`. If the correspondence is intentionally *rolling*, say so explicitly and attach an update policy + witnesses; rolling claims MUST NOT justify substitution unless a specific edition pair is pinned for the decision being justified. |
| `CL`                 |                    Yes | Integer `0–3` with label (`0 Opposed`, `1 Comparable`, `2 Translatable`, `3 Near‑identity`) and a one‑line “why”. For `CL=3`, the “why” MUST cite matched invariants (see below). |
| `Loss`               |                    Yes | **Non‑empty Loss Notes** stating what fails to carry (units, scope, granularity, preconditions, stance). `Loss: none` is permitted **only** when `CL=3` and matched invariants are cited; for `kind=⊥`, use `Loss: n/a (incompatibility claim)` (F.9). |
| `facetSpan`          | Yes (if not whole‑cell); otherwise May | The **facet span** of the correspondence (what is being aligned / preserved): e.g., `{label}`, `{identifier semantics}`, `{membership}`, `{value after unit normalization}`, `{role qualifiers}`, `{status lattice}`. If the bridge is facet‑limited, either (a) refine endpoints into facet SenseCells (preferred), or (b) declare `facetSpan` explicitly and keep `scope` capped appropriately. |
| `counterExample`     |           Yes (if CL≤2) | The crispest case where the next‑stronger reading would mislead (substitution, row scope, or type reuse). For `CL=3`, state “no known counterexamples under invariants” (and cite the invariant set). |
| `invariants`         |           Yes (if CL=3) | A short list of the invariants that justify `CL=3` (domain + measurement + stance constraints as applicable), with pointers (`witnessRefs`) to where they are checked or argued. |
| `scope`              |                    Yes | Allowed use (F.9): `Explanation‑only / Naming‑only / Role Assignment & Enactment‑eligible / Type‑structure`. This is a **maximum licence** for how the Bridge may be used in reasoning and tables. Do not confuse it with **Claim scope (G)** from USM (A.2.6), and do not encode “sometimes substitution” by mixing scopes—narrow endpoints instead (see below). |
| `witnessRefs`        | Should (MUST in decision/publication lanes for any Bridge used beyond Explanation‑only) | Evidence artefacts / witness set (rules, tests, audits, empirical evaluations, review notes, alignment reports). `witnessRefs` are how readers distinguish “declared” from “demonstrated”. |
| `didacticHook`       |                    May | A single sentence that teaches the safe reading.                                                                                       |

**Hard separation:** “shared label” is `Naming‑only`; “can replace in decisions/enactment” is `Role Assignment & Enactment‑eligible` and requires the substitution conditions; “can be treated as the same class/type for structural inference” is `Type‑structure` and requires near‑identity under invariants.

**Two “scopes” warning.** `scope` is a **licence scope** (how the Bridge may be used). The *facet span* of the correspondence (“which aspects are aligned?”) MUST be carried either by endpoint refinement (preferred) or by an explicit `span` + consistent `Loss`. Do not overload `scope` to mean facet span.
**Naming note.** Use `facetSpan` for facet limitation to avoid confusion with other “span” operators/vocabulary elsewhere in the spec.

**Kind/scope admissibility (concept‑level; non‑deontic).**

The following constraints are stated as *admissibility conditions* (E.19): they define when a Bridge Card is well‑formed for a claimed licence.

* **INV‑XCTX‑KS‑0 (Kind/CL sanity).** If `kind=⊥`, then `CL=0`. If `CL=3`, then `kind=≈` and `invariants` are stated.
* **INV‑XCTX‑KS‑1 (Overlap caps scope).** If `kind=⋂`, then `scope ∈ {Explanation‑only, Naming‑only}`.
* **INV‑XCTX‑KS‑2 (Disjoint embargo).** If `kind=⊥`, then `scope = Explanation‑only`, and the Bridge cannot support Concept‑Set rows or substitution (F.9:13.4).
* **INV‑XCTX‑KS‑3 (Interpretation embargo).** If `kind∈{⇄ᴅʀ, →ᴍᴇᵃ, →ᴅᵉᵒ}`, then `scope = Explanation‑only`, and the Bridge cannot support Concept‑Set rows or substitution (F.9:13.5).
* **INV‑XCTX‑KS‑4 (Role Assignment & Enactment substitution).** If `scope = Role Assignment & Enactment‑eligible`, then `kind∈{≈,⊑,⊒}`, `dir = A→B`, `CL≥2`, the Bridge is senseFamily‑preserving, endpoints are stance‑compatible, Loss notes are non‑empty, and a counter‑example is stated (F.9:13.2, F.9:13.8, F.9:16.1).
* **INV‑XCTX‑KS‑5 (Type‑structure reuse).** If `scope = Type‑structure`, then `senseFamily = Type‑structure`, `kind=≈`, `dir=A↔B`, `CL=3`, and matched invariants are stated (Type‑structure is only supported by near‑identity; see F.9:6.1 and F.9:16.1).
* **INV‑XCTX‑KS‑6 (Inclusion honesty).** `kind∈{⊑,⊒}` implies: the Bridge does not cite any membership counter‑case that violates inclusion for the stated endpoints. If such a counter‑case exists, then (for these endpoints) `kind=⋂`, or the endpoints are refined (SenseCell split) before any inclusion kind is stated.

**No “conditional scope” in one Bridge.** Authors SHALL NOT encode two licences in one Bridge (e.g., “Naming‑only generally; substitution in workflow X”). Instead, refine endpoints into the guarded subset SenseCells (SenseCell split) and declare a **separate** Bridge for the refined endpoints (new id or new edition), keeping the broad Bridge at the weaker scope.

#### A.6.9:4.3 - Change‑class lexicon

A.6.9 forbids “re‑align / re‑map / now equivalent” as a change description. Changes are narrated using the **A.6.P change classes**; the Bridge‑specific verbs below are narrative shorthands that map to A.6.P:4.4 (`declareRelation`, `withdrawRelation`, `retargetParticipant`, `reviseByValue`, `rescope`, `retime`, `refreshWitnesses`).
Authors SHALL NOT use umbrella verbs (“re‑align”, “re‑map”, “now equivalent”, …) as change narration. Narrate changes using the change‑class lexicon below (mapped to A.6.P:4.4).

1. `declareBridge(BridgeId, σA@CtxA, σB@CtxB, …slots…)`
2. `withdrawBridge(BridgeId)`
3. `retargetEndpoint(BridgeId, σA→σA', σB→σB')` (edition pinning or SenseCell split/merge)
4. `retime(BridgeId, Γ_time→Γ_time')` (maps to A.6.P `retime(newΓ_time)`; semantic; edition‑fenced in decision/publication lanes)
5. `changeBridgeKind(BridgeId, kind→kind')` (maps to A.6.P `changeRelationKind`)
6. `adjustCL(BridgeId, CL→CL')` (raise/lower, with at least one new invariant or counter‑example)
7. `rescope(BridgeId, scope→scope')` (Naming‑only → Role Assignment & Enactment‑eligible / Type‑structure is a strengthening; requires DRR and MUST be unconditional for the same endpoints)
8. `reviseLossNotes(BridgeId, Loss→Loss')`
9. `reviseFacetSpan(BridgeId, facetSpan→facetSpan')` (maps to A.6.P `reviseByValue`; semantic; edition‑fenced in decision/publication lanes)
10. `refreshWitnesses(BridgeId, witnessRefs→witnessRefs')` (adding one witness is a special case: set‑union + re‑publish)

**Edition fence (decision/publication lanes).** Any semantic edit to a Bridge’s slots (endpoints, kind, dir, CL, scope, invariants) SHALL be published as a **new Bridge edition** (with an explicit supersedes/withdraws note) rather than rewriting a prior edition in place. This preserves auditability and prevents “silent strengthening” through edits.

Semantic edits include changes to `Γ_time` or declared `facetSpan` (because they change what editions/aspects the correspondence judgement is about).

**Workflow/guard‑scoped strengthening is not a plain `rescope`.** If the stronger licence holds only after filtering/guards (e.g., “human users only”), represent that by **refining endpoints** (SenseCell split) and declaring a Bridge for the refined endpoints (new id or new edition), rather than upgrading the broad Bridge’s scope.

**Direction inversion is not an edit.** If the inverse relation is needed, declare a *new* Bridge (new `BridgeId`) with its own `dir`, `kind`, `CL`, and Loss; optionally withdraw the old one.

#### A.6.9:4.4 - Lexical guardrails and name selection

**Umbrella tokens (red‑flag triggers):** “same”, “identical”, “equivalent”, “align”, “map”, “match”, “correspond(s)”, and close variants.

These are only in‑scope here when used as **cross‑Context predicates** (`CtxA ≠ CtxB`) or when the prose collapses **A.7 lanes** / `CHR:ReferencePlane`s under an umbrella sameness predicate. For that case:
* In **Tech register** (normative / decision‑carrying prose), authors SHALL NOT use umbrella tokens as standalone cross‑Context predicates. Use a Bridge reference and a licence‑revealing verb instead (“share a label”, “substitutes for”, “explain in terms of”).
* In **Plain didactic** or quoted legacy prose, umbrella tokens MAY appear, but only if the paragraph also includes an explicit Bridge reference (BridgeId or inline Bridge Card) so readers are not forced to infer `kind/dir/CL/Loss/scope`.

Instead, choose a phrase that reveals the intended licence:

| Intended meaning                | Use this (canonical)                                                               | Avoid                                             |
| ------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------- |
| Interpretation only             | “Explain σB in terms of σA under an *Interpretation Bridge* (kind∈{⇄ᴅʀ,→ᴍᴇᵃ,→ᴅᵉᵒ}, scope=Explanation‑only).” | “σA is the same as σB.” |
| Naming convenience              | “Share a label under a *Naming‑only* Bridge (scope=Naming‑only; kind∈{⋂,⊑,⊒} (and **≈ only when you state why substitution is still forbidden); CL≥1; Loss + counterexample).” | “σA corresponds to σB (so we can treat them as…)” |
| Safe substitution (directional) | “Licence substitution A↠B under a *Substitution Bridge* (kind∈{≈,⊑,⊒}, dir A→B, CL≥2, same senseFamily + stance; Loss + counterexample; scope=Role Assignment & Enactment‑eligible).” | “σA and σB are equivalent.” |
| Type‑structure reuse (strong)   | “Declare a *Type‑structure* Bridge (senseFamily=Type‑structure; kind=≈; dir A↔B; CL=3; invariants; scope=Type‑structure).” | “They are literally the same class everywhere.” |
| Disjoint / contrast             | “Declare kind=⊥ with scope=Explanation‑only (contrast only).”                       | “Almost the same” / “basically equivalent”        |

**Name selection rule:** if the author wants “the same name”, choose *Naming‑only* and keep the verb “share a label”; if the author wants “can be substituted”, use *Substitution* and keep the verb “substitutes for” with explicit direction.

#### A.6.9:4.5 - RPR Disambiguation Guide (XCTX)

Use this table when you encounter umbrella‑sameness wording.

| Trigger in text                    | Candidate Bridges (default first)                                                                 | Discriminating questions / tests                                                                 | Canonical rewrite                                                                 | Routing hooks                                              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| “A is the same as B” (CtxA ≠ CtxB) | Explanation‑only (interpretation) → Naming‑only (⋂/⊑/⊒/≈) → Substitution (≈/⊑/⊒, CL≥2)            | Is this a licence or a teaching gloss? What direction is safe? What is lost? What is the counter‑example? | `Bridge(σA@CtxA, σB@CtxB): ⟨kind=?, dir=?, CL=?, Loss=?, scope=?⟩`                | E (witness), D (naming), A (admissibility if substitution) |
| “Align A and B”                    | Naming‑only with overlap (⋂)                                                                        | Do we only need a shared label, or do we need safe substitution/type reuse?                       | `Bridge(σA,σB): kind=⋂, dir=A↔B, CL=1, Loss + counterExample, scope=Naming‑only`   | D (labeling), E (counterexample)                           |
| “Map A to B”                       | (i) semantic Bridge (this pattern) vs (ii) operational artefact (ETL/transform/lookup)             | Is “map” about a thinking move (licence) or about code/execution? What is the substitution direction (if any) vs code direction? | `Bridge(σA,σB): dir A→B, kind chosen for that direction, Loss bullets + counterExample` | E (artefact), A (if substitution proposed)                 |
| “Same ID / same key / 1‑to‑1”      | Identification/indexing claim (A.6.6) ± semantic Bridge                                              | Is the claim about **Carrier‑lane equality** (identifier scheme), or about **sense/meaning**? What is the reference scheme? Are collisions/aliases possible? | First: repair as an identification/indexing relation (A.6.6). Then (only if needed): declare a Bridge for meaning with explicit `kind/dir/CL/Loss/scope`. | A.6.6 (Carrier), E (reference scheme), A.6.9 (meaning)     |
| “B is a view/projection of A”      | Explanation‑only or Naming‑only by default; substitution only after explicit guards/refined endpoints | Is this a view/correspondence statement (E.17), or a reuse licence? Does projection drop constraints/fields/stance? | `Bridge(σA,σB): kind=⊑ (if A is narrower), dir A→B (if substitution is intended), Loss states dropped structure/constraints, scope capped unless proven` | E.17 (views), E (artefact), A (if substitution proposed)   |
| “A matches B” / “corresponds to”   | Naming‑only overlap (⋂)                                                                             | Is it overlap (⋂) or inclusion (⊑/⊒)? What breaks under substitution?                              | `kind=⋂, scope=Naming‑only, CL=1 (or CL=2 if translatable), Loss + counterExample` | D, E                                                       |
| “Equivalent”                       | ≈ only under explicit invariants; otherwise overlap/inclusion                                       | Equivalent in what **senseFamily** and under what invariants? Any counter‑examples?               | Prefer `⋂ + Naming‑only`, or specify `≈` with invariants & CL                       | L (invariant claim), E                                     |

Updates:

* For “Align A and B”, default to `kind=⋂`, `scope=Naming‑only`, `dir=A↔B`, `CL=1`, with explicit Loss + counterexample. Use `kind=≈` only when you can state the equivalence criterion; invariants are mandatory for `CL=3` (and recommended whenever you use `≈`). Use `scope=Type‑structure` only when `kind=≈` and `CL=3` with matched invariants (INV‑XCTX‑KS‑5).
* For “Map A to B”, first decide whether “map” denotes (i) a semantic Bridge claim (this pattern) or (ii) an operational transformation artefact (ETL, id translation, schema mapping). If (ii), keep the artefact as `witnessRefs` and still declare the Bridge kind/dir/Loss separately; do not let “there exists a map” collapse into substitution.

**Default safety rule (normative):** authors SHALL NOT assign `CL≥1` (nor claim Naming‑only or substitution) unless they can state `Loss` notes and (for `CL≤2`) a `counterExample`. Otherwise, keep the statement as Explanation‑only (didactic gloss) or postpone the cross‑Context claim until evidence exists.
If the stable intent is **anti‑conflation** (“do not treat them as the same”), make that explicit as `kind=⊥` with `scope=Explanation‑only` (contrast), or—when the contrast is stable and repeatedly needed—publish a contrast row per the Concept‑Set discipline instead of relying on “not the same” prose.

When endpoint meanings are versioned, the same rule applies to `Γ_time`: if you cannot state the edition/as‑of basis, keep the claim Explanation‑only and do not justify rows or substitution.

#### A.6.9:4.6 - Mapping artefacts are not Bridges (normative clarification)

Many projects use “map” to mean an implementation artefact: a lookup table, aligner model, transformation function, or ETL step. A.6.9 treats such artefacts as **witnesses**, not as semantics. The Bridge is where you record:

* what correspondence is claimed (`kind/dir/senseFamily`);
* how strong it is (`CL`, invariants for `CL=3`);
* what breaks (`Loss`, counterexample);
* what it licenses (`scope`).

**Direction reminder.** A transformation artefact may be written `f:A→B` while the safe semantic substitution (if any) is `B↠A` (or none at all). Treat `dir` as the direction of the licensed **reading/substitution move**, not the direction of code execution.

If the artefact changes, narrate the update as `refreshWitness` / `reviseLossNotes` / `adjustCL` (editioned), not as “re‑mapped”.

#### A.6.9:4.7 - Coordination notes (keep A.6.9 modular)

* **Views / projections / correspondences:** if the core intent is multi‑view description (“this diagram is a view of that system”, “these views correspond”), route the modelling discipline to **E.17** and keep A.6.9 focused on preventing umbrella‑token licence smuggling. A.6.9 may still be used to declare any *naming/substitution* licence between view elements, but it MUST NOT replace E.17’s correspondence discipline.
* **Kinds / classifications:** if the cross‑context claim is about **kind transfer** (“Class X in A is the same kind as Class Y in B” as a classification move), consider recording the classification channel using **C.3.3 KindBridge**. Do not conflate Bridge‑CL with kind‑mapping CL^k.


### A.6.9:5 - Archetypal Grounding

#### A.6.9:5.1 - System archetype: identity “sameness” across products

**Tell (ambiguous):**
“An IAM *User* is the same as a CRM *Customer*.”

**Show A (Bridge Card repair):**

```
BridgeId: β-IAM→CRM-UserCustomer (edition-pinned)
Cells: “User”@IAM ↔ “Customer”@CRM
senseFamily: Role
kind: ⋂
dir: IAM↔CRM
CL: 2 (Translatable) — high overlap; service accounts and leads/prospects are counterexamples
Loss:
  - CRM “Customer” includes leads/prospects with no IAM account
  - IAM “User” includes service accounts and disabled identities not treated as customers
Counter-example: “svc-billing@” is a User@IAM but not a Customer@CRM
scope: Naming-only
Didactic hook: “Overlap only: share labels; do not substitute without guards/refinement.”
```

**Effect:** dashboards and prose may share labels (Naming‑only). Workflow substitution is *not* implied globally; it is gated by scope and guards.

**Show B (change narration, later evidence):**
After hard constraints are added (e.g., “human‑verified email”, “not a service account”), a team wants stronger reuse in the ticketing integration.

*Do not write:* “Now they are equivalent / now the mapping is fixed.”
*Write:*

0. Keep the broad Bridge **as‑is** (Naming‑only, overlap): it remains the correct “shared label” relation for the unguarded endpoints.
1. `refreshWitnesses(β-IAM→CRM-UserCustomer, witnessRefs→witnessRefs ∪ {TicketingIntegrationTestSuite_v3})`
2. `declareBridge(β-IAM→CRM-HumanVerifiedUser→VerifiedCustomer, HumanVerifiedUser@IAM, VerifiedCustomer@CRM, …slots…)` (new Bridge id or new edition family)
3. In that new Bridge: state `kind=⊑` (if inclusion is now true for the refined endpoints), `dir=IAM→CRM`, keep `CL=2`, restate Loss (remaining exclusions), and provide a crisp counter‑example for where substitution would still break.
4. `rescope(β-IAM→CRM-HumanVerifiedUser→VerifiedCustomer, Naming‑only → Role Assignment & Enactment‑eligible)` with DRR explaining why `CL=2` suffices for the refined endpoints.

Direction remains IAM→CRM; if the inverse is required, declare a separate Bridge with its own loss/counterexamples.

#### A.6.9:5.2 - Episteme archetype: schema/ontology alignment between knowledge graphs (class-level)

**Tell (ambiguous):**
“`Person` in KG‑A is equivalent to `Person` in KG‑B.”

**Show A (Bridge Card repair):**

```
BridgeId: β-KGA↔KGB-Person (edition-pinned)
Cells: Person@KG-A ↔ Person@KG-B
senseFamily: Type-structure
kind: ⋂
dir: A↔B
CL: 2 (Translatable) — overlap is high but invariants differ
Loss:
  - KG-A “Person” includes fictional characters; KG-B excludes them
  - KG-B requires a stable external identifier; KG-A does not
Counter-example: “Sherlock Holmes” ∈ Person@KG-A but ∉ Person@KG-B
scope: Naming-only
Didactic hook: “Shared label does not grant type-structure or substitution; the sets only overlap until invariants and membership rules are aligned.”
```

**Show B (strengthening attempt and rejection):**
A reviewer proposes Type‑structure reuse (“treat them as the same class across graphs”). Under A.6.9, this triggers a required invariant check:

* Since Type‑structure reuse requires CL=3 and matched invariants, the proposal is rejected unless the invariants are aligned and the counterexample class is eliminated (e.g., by refining `Person@KG-A` into `FictionalPerson` vs `RealPerson`).
* The correct change narrative is: `changeBridgeKind` (if kind changes), `adjustCL` only if the counterexample disappears and invariants are shown, else keep CL=2 and Naming‑only scope.

### A.6.9:6 - Bias‑Annotation

This pattern is biased toward:

* **Explicitness over fluency.** It intentionally slows down prose that would otherwise smuggle licences.
* **Safety in substitution.** It treats substitution as a high‑risk claim requiring declared direction, `CL`, and Loss notes.
* **Locality of meaning.** It assumes meanings are Context‑local unless bridged explicitly; it rejects label‑driven identity.
* **Ordinal confidence.** `CL` is treated as an ordinal safety ladder, not a probability; it is deliberately coarse.

Consequently, A.6.9 may feel “heavy” in early drafts, but it prevents latent cross‑Context defects that are costly to discover later.

### A.6.9:7 - Conformance Checklist

A document or boundary statement conforms to A.6.9 iff:

* **CC‑A.6.9‑0 (UTS/LEX trigger coverage).** The local lexicon treats umbrella‑sameness tokens as RPR triggers and points authors to Bridge‑explicit rewrites.
* **CC‑A.6.9‑1 (No standalone umbrella predicate).** Cross‑Context umbrella tokens SHALL NOT be used as standalone cross‑Context predicates unless either:
  * (a) the paragraph includes an explicit Bridge reference (BridgeId or inline Bridge Card), or
  * (b) the statement is explicitly marked as non‑licensing explanatory prose (“no Bridge licence; do not substitute; do not justify rows”).
* **CC‑A.6.9‑2 (SenseCell endpoints).** Every such claim names endpoints as `σ@Context` (edition‑pinned where relevant), not as strings or system names.
* **CC‑A.6.9‑3 (Direction explicitness).** `dir` is stated on every Bridge. If `kind` is non‑symmetric, any inverse use without redeclaration is non‑conformant.
* **CC‑A.6.9‑4 (Licence separation).** If the intent is explanation only, authors SHALL either (a) declare `scope = Explanation‑only` on a Bridge, or (b) use explicit non‑licensing prose (no Bridge licence). If the intent is naming compatibility, authors SHALL declare a Bridge with `scope = Naming‑only`. In all cases, the text SHALL NOT invite substitution unless a substitution‑eligible Bridge exists.
* **CC‑A.6.9‑5 (Substitution thresholds).** Any statement that implies substitution MUST be backed by a substitution‑eligible Bridge (`kind∈{≈,⊑,⊒}`, `CL≥2`, same `senseFamily`, stance‑compatible), with Loss notes and a counter‑example discipline.
* **CC‑A.6.9‑6 (Weakest‑link respect).** Any Concept‑Set row or composed claim that depends on multiple Bridges MUST bound its scope and `CL` by the weakest participating Bridge.
* **CC‑A.6.9‑7 (Loss visibility).** Loss notes are present and **non‑empty**. `Loss: none` is permitted only for `CL=3` with cited invariants; `Loss: n/a` is permitted for `kind=⊥`. Loss must be consistent with the allowed scope.
* **CC‑A.6.9‑8 (Change narration).** Changes to cross‑Context fit are narrated using the change‑class lexicon (declare/withdraw/adjustCL/rescope/…) rather than umbrella verbs.
* **CC‑A.6.9‑9 (Kind/scope admissibility).** Any Bridge used to justify cross‑Context sameness satisfies the admissibility constraints INV‑XCTX‑KS‑1 … INV‑XCTX‑KS‑5 (no overlap‑to‑substitution; no disjoint/interpretation rows; substitution is directional; Type‑structure only under `≈` + `CL=3` + invariants).
* **CC‑A.6.9‑10 (Registry reference hygiene).** If a BridgeId (or policy/edition id) is cited, it is treated as a **registry reference** (existence / edition pinning), not as a semantic symbol exported by signatures.
* **CC‑A.6.9‑11 (Edition basis).** In decision/publication lanes, any Bridge used to justify Naming‑only / substitution / Type‑structure SHALL state `Γ_time` (edition pins or “as‑of” basis). If `Γ_time` cannot be stated, the claim MUST remain Explanation‑only and MUST NOT justify rows or substitution.
* **CC‑A.6.9‑12 (Facet honesty).** If the correspondence holds only on a subset of facets, the author SHALL either (a) refine endpoints into the facet SenseCells (preferred) or (b) declare `facetSpan` explicitly, with `Loss` consistent with that facet span. Whole‑cell Bridges MUST NOT be used to smuggle facet‑only correspondences.

### A.6.9:8 - Common Anti‑Patterns and How to Avoid Them

| ID            | Anti‑pattern           | Example                                              | Why it breaks                                           | Remedy                                                               |
| ------------- | ---------------------- | ---------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| **AP‑XCTX‑1** | Bridge‑by‑adjective    | “A is the same as B (across contexts).”              | Smuggles scope + direction + loss as implicit defaults. | Replace with Bridge Card + explicit `scope`.                         |
| **AP‑XCTX‑3** | Stealth substitution   | “We’ll just treat A like B for now.”                 | Introduces implicit licence without CL/Loss gates.      | Publish Bridge Card; if CL<2, keep `Naming‑only`.                    |
| **AP‑XCTX‑2** | Symmetry hallucination | Treating `⊑/⊒` as symmetric “equivalence”.           | Causes unsafe inverse substitution.                     | Record `kind` and `dir`. Only symmetric kinds (`≈`, `⋂`, `⊥`, `⇄ᴅʀ`) may be written as `A↔B`; inclusion kinds require direction; substitution is always directional. |
| **AP‑XCTX‑4** | Lossless fantasy       | “Equivalent” with no loss note.                      | Loss is almost always present; hiding it misleads decisions.       | State Loss notes (even if “none”), add a counter‑example (CL≤2) or invariants (CL=3); adjust CL/scope accordingly. |
| **AP‑XCTX‑5** | Silent inversion       | Later prose uses B→A without redeclaration.          | Violates direction guard; breaks auditability.          | Declare inverse Bridge (new id) or withdraw+replace.                 |
| **AP‑XCTX‑6** | Confidence laundering  | Raising CL or scope without new invariants/evidence. | Inflates trust; expands row scopes illegitimately.      | Use `adjustCL`/`rescope` with witnessRefs + DRR.                     |
| **AP‑XCTX‑7** | Chain upgrade          | Treating A↠B and B↠C as “therefore A≈C”.             | Violates weakest‑link and loss accumulation.            | Use min‑CL and accumulated Loss; avoid chaining unless justified.    |
| **AP‑XCTX‑8** | Conditional scope smuggling | “Naming‑only generally; substitution in workflow X.” | Encodes two licences in one record; leaks into row scope and downstream reasoning. | Refine endpoints (SenseCell split) and declare a separate Bridge for the guarded subset; keep broad Bridge Naming‑only. |
| **AP‑XCTX‑9** | Artefact⇒equivalence fallacy | “There is a mapping table, so they are the same.” | Confuses operational transformation with semantic licence; hides Loss and direction. | Record artefact in `witnessRefs`, keep Bridge kind/dir/Loss explicit, and keep scope capped until CL+counterexamples justify promotion. |
| **AP‑XCTX‑10** | Two‑way substitution by symmetry | “The Bridge is A↔B, so we can substitute both ways.” | `A↔B` expresses correspondence symmetry, not two substitution licences; substitution is directional and must be stated (F.9:13.2). | Declare both substitution directions explicitly (two licences / two Bridges / two editions), each with Loss + counter‑examples. |
| **AP‑XCTX‑11** | Kind/dir mismatch | `kind=⊒` but `dir=A→B` is used as if it licensed substitution. | Inverts narrower/broader; encourages unsafe “narrowing substitution” and silent information loss. | Swap endpoints (so the intended safe direction is written as `A→B` with `kind=⊑`), or declare an explicit inverse Bridge; keep scope ≤ Naming‑only until the direction is justified. |
| **AP‑XCTX‑12** | Kernel promotion by Bridge | “Since A≈B, we can mint a unified global type and treat both as instances.” | Bridges translate local senses; they do not mint global meaning or new `U.Type`s. | If you need a new shared type/kind, follow A.11; keep Bridges as translators between Context-local senses. |
| **AP‑XCTX‑13** | Edition drift / timeless equivalence | “A is equivalent to B” with no edition/as‑of basis. | Makes the claim temporally incoherent as canons evolve; readers silently compare different revisions. | Pin editions via `Γ_time`; publish Bridge edits as new editions; fail‑closed to Explanation‑only when `Γ_time` cannot be stated. |
| **AP‑XCTX‑14** | Facet‑only alignment masquerading as whole‑cell sameness | “Customer corresponds to User” (but only `email` or an external ID aligns). | Collapses a partial lens into global sameness; invites unsafe substitution and row scope creep. | Refine endpoints to the facet SenseCells, or declare `facetSpan` explicitly and keep `scope` capped (usually Naming‑only). |
| **AP‑XCTX‑15** | Lexical translation ⇒ semantic identity | “Term A is the same as term B” (just a translation / synonym). | Confuses labels with referents; erases loss and context. | Use `scope=Naming‑only` with explicit `Loss` (incl. language/canon notes) and a counter‑example; do not imply substitution. |

### A.6.9:9 - Consequences

* **Pros**

  * Removes ambiguity between explanation, naming compatibility, and substitution.
  * Makes directionality explicit; prevents accidental inverse reasoning.
  * Forces Loss disclosure early; reduces later integration surprises.
  * Provides a disciplined evolution path (change classes) when evidence changes.

* **Cons**

  * Adds visible structure to prose; authors must choose `kind/dir/CL/scope` explicitly.
  * Requires reviewers to engage with counter‑examples and loss notes.
  * Can surface uncomfortable truth: many “same” claims are only Naming‑only.

**Adoption test (PRAG).** Take any cross‑Context sentence that uses an umbrella predicate (“same/equivalent/align/map/…”). If the team cannot (a) name the two SenseCell endpoints, (b) state `dir`, (c) write at least one Loss bullet, and (d) give a crisp counter‑example (for CL≤2), then the claim is not ready to be treated as Naming‑only or substitution‑eligible. Keep it as Explanation‑only (or explicit non‑licensing prose) until evidence exists.

If the endpoints’ canons are versioned and the team cannot state `Γ_time` (edition/as‑of basis), treat that as the same kind of “evidence missing”: keep the claim Explanation‑only.

### A.6.9:10 - Rationale

Cross‑Context “sameness” is a *family of relations*, not a single predicate. Making the Bridge explicit:

* preserves the locality of meaning (SenseCells are context‑bound);
* prevents licence creep (Naming‑only does not silently become substitution);
* supports auditability (BridgeId + slots, not adjectives);
* aligns prose with the formal reasoning primitives that govern safe substitution and row scopes.

A.6.9 turns a dangerous linguistic convenience into an explicit, reviewable, evolvable claim.

### A.6.9:11 - SoTA‑Echoing

(informative; post‑2015 alignment)

| SoTA practice                                                            | Primary source (post‑2015)                                              | What A.6.9 echoes                                                   | What A.6.9 adds                                                                                               | Stance                   |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Correspondences between viewpoints in architecture descriptions          | ISO/IEC/IEEE 42010:2022                                                 | Correspondences are not identity; they have intent and constraints. | Forces direction/degree/loss to be explicit via Bridge Card slots.                                            | **Adopt + specialise**   |
| Declarative constraint systems and validation shapes                     | W3C SHACL (Recommendation, 2017)                                        | Make implicit semantics checkable by explicit structure.            | Uses Bridge Cards as “shape of correspondence”: explicit slots + counterexample discipline.                   | **Adapt**                |
| Entity alignment as scored correspondences with errors (embedding‑based) | BootEA (Sun et al., 2018) and related post‑2015 KG alignment literature | Alignment is graded, not binary; error analysis matters.            | Replaces raw scores with a coarse, auditable ordinal (`CL`) + explicit Loss notes and scope licences.         | **Adapt**                |
| Entity alignment using textual encoders (transformer‑based)              | BERT‑INT (Tang et al., IJCAI 2020); Ditto (Li et al., PVLDB 2021)        | Modern matchers output scored/conditional correspondences.          | Turns “score” into an auditable licence (`CL/scope`) plus explicit error modes (`Loss` + counterexamples).    | **Adopt (conceptually)** |
| Deep learning for schema matching as a family of match types             | SMAT (Zhang et al., 2021) and post‑2020 neural/LLM schema matching lines | “Matches” are heterogeneous and directional in practice.            | Makes match type explicit as Bridge kind + direction + licence scope (separating semantics from artefacts).   | **Adapt**                |
| Human‑in‑the‑loop entity matching (thresholding + error analysis)        | “Deep Learning for Entity Matching: A Design Space Exploration” (Mudgal et al., SIGMOD 2018) and follow‑on work | Scores are not licences; practice needs thresholds, abstention, and curated error cases. | Mirrors the “explain vs name vs substitute” split: scores stay in `witnessRefs`; promotion requires Loss + counter‑examples and an explicit scope upgrade. | **Adapt** |

### A.6.9:12 - Relations

* **Specialises:** A.6.P (Relational Prose Repair) by fixing the contract skeleton for cross‑Context sameness claims.
* **Uses:** F.9 Bridge discipline (Bridge Card, `BridgeKind`, `dir`, `CL`, Loss notes, scope licences, weakest‑link).
* **Coordinates with:** E.10 lexical discipline (umbrella tokens) and F.5 label discipline (Tech/Plain labels do not imply bridges).
* **Constrains:** Any cross‑Context Concept‑Set row scope claims via weakest‑link and substitution thresholds.

### A.6.9:End

## A.6.S - U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Mixed (normative where RFC 2119 keywords appear; quadrant routing is governed by A.6.B)
> **One-liner:** **explicitly modelling signature engineering as a two‑signature arrangement** (TargetSignature + ConstructorSignature), with strict separation between **operator description** and **enactment as Work by transformer Systems**.

### A.6.S:0 - PCP-TERM/LEX token guards (local-first)

This pattern reserves the following tokens on Tech (normative) surfaces:

* **TargetSignature** — the engineered signature episteme (and its editions) under construction/stabilisation (**not** the described entity, and **not** a Bridge “target Context”).
* **ConstructorSignature** — the enabling signature that describes constructor operations for TargetSignature evolution (do **not** mint a second Tech token such as `EnablingSignature`).

Rename-guards (common collisions):

* **enabling** — Plain adjective meaning “producing/maintaining the TargetSignature”; it is not a `U.*` token.
* **constructor** — MUST be disambiguated as one of: `ConstructorSignature` (episteme), `constructor op` (EFEM), or `constructor System`/`enactor` (transformer). If the physics term is intended, spell **“Constructor Theory”** explicitly.
* **target** — avoid bare “target” in Tech clauses; use `TargetSignature` or qualify the target (e.g., “Bridge target Context”, “target holon”).
* **contract** — Plain shorthand for “published boundary interface description”; it MUST NOT be read as a promise/obligation. Promises, duties, and gates route via A.6.B.

### A.6.S:1 - Problem frame

Boundary descriptions rarely arrive as fully formed signatures. They show up as “half‑signatures”: an n‑ary relation in natural language, a few overloaded markers (“binding”, “anchoring”, “contract”), and implicit assumptions about bases, scope, and viewpoints. Teams then evolve the boundary through incremental edits, reviews, and partial publications.

FPF already provides local disciplines that help unpack such text into well‑formed components: slot discipline (A.6.5) and explicit base declarations (A.6.6). What is usually missing is a *first‑class* description of the engineering interface that turns half‑signatures into stable, publishable boundary interface descriptions (“contracts” in Plain shorthand; see §0 guards)—an explicit ConstructorSignature for constructing and evolving a TargetSignature.

When signature construction is not explicitly modeled, three failures recur:

1. the target boundary contract and the engineering workflow get conflated;
2. semantic changes happen without being made explicit as retargeting or edition changes;
3. published faces (views) drift into adding semantics, making “the contract” ambiguous.

Additionally, authors often (implicitly) treat a signature as if it *acts* (“the constructor builds the signature”).
In FPF this is a category error: an Episteme describes; any change is enacted by a System in a transformer role.
A.6.S therefore must keep **operator descriptions** separate from their **enactment as work**.

### A.6.S:2 - Problem

FPF needs a pattern for **engineering signatures as boundary artifacts**: a disciplined way to construct, revise, and publish a target `U.Signature` from partial input, while maintaining:

* separation between *signature* and *mechanism* (A.6.0 vs A.6.1),
* separation between *laws*, *admissibility*, *deontics*, and *work evidence* (A.6.B),
* explicit multi‑view publication without semantic drift (E.17),
* reproducible evolution across editions without silent mutation.

### A.6.S:3 - Forces

* **Stability vs evolution.** Boundary contracts must be stable enough to coordinate, yet change as understanding improves.
* **Explicitness vs overhead.** Unpacking slots/bases/views increases clarity but also increases authoring effort.
* **Effect‑free operators vs enacted work.** The construction/change language should be expressible as effect‑free epistemic morphisms (no measurement/actuation),
  yet the act of applying them to artifacts is still Work done by transformer Systems and must be auditable.
* **Multi‑view richness vs semantic coherence.** Views help stakeholders, but they risk becoming divergent “versions of truth”.
* **Local meaning vs cross‑context reuse.** Signatures should keep meaning local to a context; reuse across contexts requires explicit bridges and declared loss/penalty policy.
* **Contract talk vs ontology.** “Contract” language invites mixing promises, norms, and invariants; FPF requires quadrant discipline.
* **No epistemic agency.** It is tempting to phrase “the ConstructorSignature constructs…”. In FPF, only Systems act; epistemes do not.

### A.6.S:4 - Solution — two signatures and a small constructor vocabulary

#### A.6.S:4.0 - Ontology and effect profile — constructor operators are epistemes; enactment is Work by transformer Systems

This pattern relies on **Strict Distinction** (A.7) and the **transformer quartet** (A.3):

* **ConstructorSignature (operator description; intensional, D/S-plane).**
  The ConstructorSignature is an **Episteme** (typically a Description/Spec) that *describes* a small family of constructor operations for signature evolution.
  The ConstructorSignature SHALL specify each constructor operation family as an instance/species of `U.EffectFreeEpistemicMorphing` (EFEM; A.6.2) or a declared sub‑species (e.g., A.6.3/A.6.4): **episteme→episteme** morphisms over the `C.2.1 U.EpistemeSlotGraph` positions (`ClaimGraphSlot`, `DescribedEntitySlot`, `GroundingHolonSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) plus attached meta/edition fields.
  As EFEM, constructor ops are **effect‑free** in the strict A.6.2 sense: **no Work, no Mechanism application, and no mutation of systems or carriers**.
  Concretely: an EFEM step *derives* a successor episteme (often a new edition) and its structured delta; the physical act of materialising that successor on carriers (files, repos, registries, releases, SCR/RSCR pins) is **Work** enacted by a transformer System.

  Slot discipline alignment requirement (A.6.5 / C.2.1:7.1): a conforming ConstructorSignature SHALL state (for each constructor operator family) which `C.2.1` slots it may read and which it may write, expressed in SlotKind/ValueKind/RefKind terms, and SHALL declare whether the operator family is a species of A.6.2 / A.6.3 / A.6.4.

* **Enactor (capability) vs enactment (world-contact).**
  A **System** in a transformer role bears a **Method** that realises the constructor operations (A.3), and it enacts particular steps as **Work / WorkEnactment** on carriers (repos, releases, pins, SCR/RSCR references).
  This is where traces, review records, evidence bindings, and publication artifacts appear.

Therefore:

* A ConstructorSignature **describes** how a TargetSignature may be constructed/evolved; it MUST NOT be written as if it *performs* the construction.
* Any step that performs measurements, actuation, validation runs, or other side‑effects is **not** an EFEM; model it as Work/Mechanism and route resulting claims via A.6.B.

#### A.6.S:4.1 - Core move: model signature engineering as a separate boundary

In a conforming design, model **two signatures**:

1. **TargetSignature.**
   The *target* boundary contract you want to stabilize. It is a `U.Signature` per A.6.0: `SubjectBlock`, `Vocabulary`, `Laws`, `Applicability`. It does **not** contain admissibility gates, deontic obligations, or evidence claims (those are routed per A.6.B).

2. **ConstructorSignature.**
   A *separate* `U.Signature` whose purpose is to describe the **engineering operations** used to construct and evolve the SoI. Intuitively: it is the “interface” of the enabling activity that produces the target interface.

A.6.S names this pairing discipline **U.SignatureEngineeringPair**: a signature engineering arrangement where a ConstructorSignature is explicitly defined for (at least) one Signature‑of‑Interest.
A.6.S names this pairing discipline **U.SignatureEngineeringPair**: a signature engineering arrangement where a ConstructorSignature is explicitly defined for (at least) one TargetSignature.

Minimal definition (informative): a `U.SignatureEngineeringPair` binds exactly two signature artifacts in the same Context: a **TargetSignature** (the contract under stabilization) and a **ConstructorSignature** (the enabling signature describing the constructor operations used to build/evolve the TargetSignature).

**Terminology note (C.2.1 alignment + twin discipline).**
This pattern uses `TargetSignature` as the **Tech role label** for “the signature artifact under construction / stabilisation”.
If a Context wants an explanatory alias, it MAY use **“signature of interest (SoI)”** as a **Plain twin** for `TargetSignature`, but Plain twins are didactic only and MUST NOT appear in conformance/acceptance clauses.

Do not conflate:
* the **TargetSignature** (an episteme artifact that is engineered and published), with
* the TargetSignature’s **`DescribedEntitySlot`** (C.2.1), which refers to the boundary/entity the signature is *about* (a.k.a. “object‑of‑talk / entity‑of‑interest / describedEntity” in C.2.1 commentary).

In C.2.1 terms:
* the TargetSignature is the **episteme** (and its editions) that we engineer and publish;
* the TargetSignature’s `DescribedEntitySlot` refers to the **entity‑of‑interest / object‑of‑talk** (the boundary in the world or model);
* the TargetSignature’s `GroundingHolonSlot` anchors where/how that boundary description is grounded.

If the “SoI” phrasing risks confusion with C.2.1 “entity‑of‑interest” talk, keep it out of Tech/normative prose and use **TargetSignature** vs **ConstructorSignature** consistently.

**Mint-or-Reuse note (informative).**
This pattern introduces the following **Tech role labels** in the A.6 cluster:
* **TargetSignature** — the target boundary contract episteme being stabilised;
* **ConstructorSignature** — the enabling signature (episteme) describing constructor operations for TargetSignature evolution;
* **U.SignatureEngineeringPair** — the two‑signature arrangement (TargetSignature + ConstructorSignature).

If any Plain twins are used (e.g., “signature of interest”), they MUST follow the E.10/F.* twin discipline (1:1 mapping per Context, registry entry, and no use on normative surfaces).

The intended shape is:

* TargetSignature is the boundary contract used by downstream design and realization work.
* ConstructorSignature is the boundary contract used by authors/reviewers to produce and revise the SoI in a disciplined, reproducible way.

This directly operationalises the idea already hinted in the A.6 cluster relations: A.6.5 and A.6.6 can be read as constructor/enabling operations for building well‑formed signatures. The new step is to **bundle those operations into an explicit ConstructorSignature** rather than leaving them as implicit editorial practice.

#### A.6.S:4.2 - Minimal constructor operation vocabulary

A conforming ConstructorSignature **SHALL** (conceptually) expose a *small, composable* set of operations. At minimum, include two groups of constructor operations, drawn from existing A.6 subpatterns:

**(A) Slot‑level constructor operations** (from A.6.5)

Use the canonical slot verbs to express “what changed” without ambiguity:

* `bind` / `rebind` (Identifier → SlotKind/slot‑instance; name binding only)
* `fill`
* `initialize` (first fill)
* `assign` / `set` / `write` / `update` (subsequent fill; by‑value replacement)
* `retarget` (Ref slot update; same SlotKind/ValueKind)
* `substitute` (typed replacement with explicit compatibility claim)
* `resolve` / `dereference` (Ref → referent)
* `pass` (parameter filling at call boundaries)

**Avoid “mutate” as a generic edit verb.**
In Core, `mutate/modify` denotes **referent‑internal change while the slot‑content (Ref handle) stays the same**.
In edition‑disciplined contexts, prefer “revise / re‑edition + retarget” rather than “mutate”.

Guidance for naming (by slot qualifier) is inherited from A.6.5: e.g., `Edit<SlotQualifier>` for by‑value changes, `Retarget<SlotQualifier>` for ref changes, and avoid collapsing retargeting into generic “editing”.

**(B) Base‑level constructor operations** (from A.6.6)

Make base declarations and their evolution explicit via base‑change verbs such as:

* `declareBase`
* `withdrawBaseDecl`
* `rebase`
* `repointDependent`
* `rescope`
* `retime`
* `refreshWitnesses`
* `changeBaseRelation`

A ConstructorSignature does not need *all* of these in every use, but it must provide enough to express “what changed” when the SoI’s grounding base, scope, or anchoring assumptions shift.

**Witness refresh note.**
`refreshWitnesses` is an **edit of witness bindings**, not the generation of new evidence: producing/collecting new witness carriers is **Work**; `refreshWitnesses` only updates the base declaration to reference them.

**Optional but common: view construction operations (A.6.3)**

If the TargetSignature is published via MVPK (recommended), include constructor operations that produce views as **EpistemicViewing** (A.6.3) of the TargetSignature:

* “Emit MVPK faces” as views (PlainView, TechCard, InteropCard, AssuranceLane), explicitly treated as views and governed by E.17 “no new semantics”.
  In particular:
  * `PlainView` / `TechCard` / `InteropCard` MUST add no new claims beyond the underlying TargetSignature/Mechanism claim set.
  * `AssuranceLane` MAY include procedural adjudication guidance and carrier pointers, but any normative pass/fail criteria MUST live canonically in `E-*` claims and be cited by ID.

These are best modeled as view‑producing operations whose output is an MVPK face, with the explicit constraint that the face is a view and therefore does not introduce new claims about the described entity.
Publishing those faces (commits, releases, registry writes) is Work on carriers; it is not “the signature doing things”.

#### A.6.S:4.3 - Change discipline: Viewing vs Retargeting vs editing

To connect signature engineering to A.6.2–A.6.6, treat changes in four buckets:

1. **Viewing (A.6.3).**
   Use when you change *presentation* (views, stakeholder cards, projections) while preserving the described entity.

2. **Slot/base construction edits (A.6.5 / A.6.6).**
   Use when you unpack and make explicit what was implicit (slot kinds, ref modes, base declarations), or when you adjust the SoI’s internal structure without changing what it is “about”.

3. **Editioning + reference retargeting (A.6.5).**
   Use when the contract meaningfully changes and you need a **new SoI edition** for downstream coordination. In that case, do not silently mutate the existing edition: mint a successor edition and **retarget references** (`Retarget<…>` in the relevant Ref slots) to the new edition.

4. **Epistemic retargeting / Structural reinterpretation (A.6.4; rarer).**
   Use only when `DescribedEntityRef` itself changes under an explicit `KindBridge` and stated invariants (e.g., reinterpretation across kinds/planes). This is distinct from ordinary “new version of the same contract”.

Rule of thumb:

* If the change can be defended as “same contract, clearer surface”, prefer slot/base construction plus viewing.
* If the change is “new contract version for consumers”, require a new edition plus explicit reference retargeting.
* If the change is “different described entity / different kind”, use A.6.4 retargeting under `KindBridge` with explicit invariants.

**EFEM discipline.**
Every constructor operation family declared as an EFEM MUST declare `describedEntityChangeMode ∈ {preserve, retarget}` (A.6.2).
**Editioning is orthogonal**: you MAY mint a new edition even under `preserve`, but if you do, downstream references MUST be updated explicitly via slot discipline (A.6.5).
Any operation that performs measurements/actuation/side‑effects MUST be modeled as Work/Mechanism, not as a constructor op.

#### A.6.S:4.4 - Publication and claim discipline for reproducibility

A conforming signature engineering arrangement **SHOULD** include two publication‑adjacent constraints:

1. **MVPK publication for the TargetSignature (E.17).**
   Publish the TargetSignature through MVPK faces as `U.View` projections with viewpoint accountability (`viewRef` + `viewpointRef`). Each face must be explicitly treated as a view and must not introduce new semantic commitments beyond the underlying signature/mechanism claim set (per E.17 “no new semantics”).

2. **Claim Register for boundary discipline (A.6.B).**
   Maintain a claim register that assigns stable identifiers to atomic claims and routes them into the correct quadrant (L/A/D/E). The engineering benefit is that changes to the SoI can be tracked as changes to specific claims rather than as unstructured prose diffs.

This keeps signature engineering aligned with A.6.B’s separation:

* **Laws** live in the SoI (L‑claims).
* **Admissibility** and operational gate conditions live in mechanisms (A‑claims).
* **Deontics** are about agents (D‑claims), not about epistemes.
* **Evidence/work effects** are recorded as outcomes of work (E‑claims), not smuggled into signatures.

#### A.6.S:4.5 - Construction flow as a transduction graph fragment (informative)

If a team already models workflows as E.TGA transduction graphs, the “constructor graph” of A.6.S is a special case:

* EFEM constructor steps can be represented as `U.Transduction(kind=Signature)` vertices (A.6.0), because they are intensional episteme→episteme morphisms (A.6.2).
* Concrete carrier writes (commits, releases, registry writes, SCR/RSCR pinning) are `U.Transduction(kind=Work)` / `U.WorkEnactment` vertices (world‑contact).
* Validations/admission checks live at `U.Transduction(kind=Check)` nodes realised as `OperationalGate(profile)` with a `DecisionLog`.
* Any `DescribedEntityRef`/kind change is a `StructuralReinterpretation` vertex (E.TGA’s use of A.6.4), with explicit `KindBridge` + invariants/witnesses.

This mapping is optional; A.6.S stays usable as a lightweight discipline even without adopting E.TGA structure.

#### A.6.S:4.6 - State during construction (informative)

Do not mint a new kernel “signature state” unless you need it.
In most cases, use:

* **edition** + explicit continuity/withdrawal links for semantic evolution, and
* a coarse **status** (`Draft`/`Review`/`Stable`/`Deprecated`) for process signalling.

If a Context needs a finer lifecycle (e.g., “proposed → reviewed → published → frozen”), model it as Work policy in the ConstructorSignature’s Applicability or as a Context‑local workflow episteme; keep the TargetSignature semantics unchanged.
Where lifecycle is normative, prefer expressing it as a **role-state graph** (A.2.1) borne by the relevant episteme role, rather than minting a new core “signature state”.

### A.6.S:5 - Archetypal Grounding — Tell–Show–Show

**Tell.** A boundary contract becomes stable and evolvable when you model both the *target signature* and the *engineering signature* that constructs it, and you force every change to be expressed as either (a) a view, (b) a disciplined slot/base construction step, or (c) an explicit retargeting to a new edition.

#### A.6.S:5.1 - Show — System archetype

**Context.** A payments microservice exposes an external boundary used by multiple client systems.

**Half‑signature input (what arrives).**
“Service binds a `User` to a `PaymentMethod`, anchors charges to the `Ledger`, and guarantees idempotency.”

**Constructed artifacts.**

* **TargetSignature:** `PaymentBoundarySignature`

  * **Vocabulary:** operations like `Authorize`, `Charge`, `Refund`; slots made explicit (e.g., `UserRefSlot`, `PaymentMethodRefSlot`, `LedgerEntryRefSlot`).
  * **Laws (examples):** “Charge is idempotent under IdempotencyKey”; “Refund does not increase net balance”.
  * **Applicability:** bounded context = “Payments”, scope = “External API”.

* **ConstructorSignature:** `PaymentSignatureEngineering`

  * Transformer system (enactor): `PaymentSignatureEngineeringPipeline` (team + repo + linters + review protocol).
    It enacts the constructor operations as Work and produces new editions and publication carriers.

  * Slot operations used (as operator descriptions; enacted via Work):

    * `bind/rebind` to bind API field names (e.g., `userId`, `paymentMethodId`) to SlotKinds (`UserRefSlot`, `PaymentMethodRefSlot`) where a language surface exists,
    * `initialize` / `edit<…>` to introduce SlotSpecs and to by‑value edit Vocabulary/Laws in the TargetSignature,
    * `resolve<…>` to disambiguate overloaded prose markers (e.g., “idempotency”) into explicit SlotKinds + laws,
    * `retarget<LedgerRefSlot>` when switching the referenced ledger holon/edition (ref change, not by‑value editing).
  * Base operations used:

    * `declareBase` to ground “Ledger” via an explicit baseRelation and scope,
    * `rescope` when moving from “internal ledger view” to “external client view”,
    * `refreshWitnesses` when decision‑relevant evidence/pins must be updated for continued use.

* **Publication.**
  MVPK faces published as views of the TargetSignature: a PlainView for non‑specialists, a TechCard for implementers, and an InteropCard for integrators, all derived without adding new claims beyond the canonical claim set.

**What A.6.S prevents here.** The phrase “guarantees idempotency” does not silently become a deontic promise or an operational gate. It becomes: (a) an L‑claim (law) in the SoI; (b) if needed, a mechanism‑level admissibility condition for when the guarantee holds; and (c) evidence claims in work logs when validated.

#### A.6.S:5.2 - Show — Episteme archetype

**Context.** A research group publishes a “signature” for a boundary concept used across multiple theories (a common “interface” between models).

**Half‑signature input.**
“We define correspondence between model A and model B; parameters are anchored to a reference dataset.”

**Constructed artifacts.**

* **TargetSignature:** `ModelCorrespondenceSignature`

  * **Vocabulary:** relation `Corresponds(A_model, B_model, Φ_bridge)` with explicit slot kinds and ref/value modes.
  * **Laws:** invariants about correspondence preservation (“observable X is preserved up to tolerance ε”).
  * **Applicability:** bounded context = “Model alignment”.

* **ConstructorSignature:** `CorrespondenceSignatureEngineering`

  * Transformer system (enactor): `CorrespondenceSignatureWorkbench` (authors + toolchain) enacts constructor ops as Work.

  * Slot operations used: `resolve` to unpack “correspondence” into an explicit bridge slot; `edit<Laws>` (by‑value) to make tolerance explicit; `retarget<ModelRefSlot>` when moving from a draft model edition to a published edition.
* Base operations used: `declareBase` to ground “reference dataset” as an explicit base with scope/time policy; `retime` when updating the reference window.

* **Publication.**
  The SoI is published in multiple viewpoints (e.g., a mathematical view and an engineering view). Differences are handled as views, not as semantic drift.

**What A.6.S prevents here.** “Anchored to a dataset” does not remain a vague metaphor. It becomes a declared base and, when the dataset changes, an explicit base‑change operation rather than a silent reinterpretation.

### A.6.S:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for signature engineering within the A.6 cluster.

* **Architecture bias (Arch):** pushing a two‑signature structure can feel heavy for small boundaries.
  *Mitigation:* keep the ConstructorSignature minimal; reuse A.6.5/A.6.6 verb sets; treat views as optional unless publication demands them.

* **Onto/Epist bias (Onto/Epist):** treating “editing the signature” as harmless can hide semantic change.
  *Mitigation:* use the Viewing vs Retargeting rule; material meaning changes become explicit retargetings.

* **Pragmatic bias (Prag):** increasing discipline may slow down exploratory work.
  *Mitigation:* allow lightweight ConstructorSignatures early, and tighten conformance as assurance requirements rise.

### A.6.S:7 - Conformance Checklist

|             ID | Requirement                                                                                                                                                                                                                                                               | Purpose                                                               |
| -------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **CC‑A.6.S‑1** | A conforming boundary description **SHALL** identify a **TargetSignature** and (when the boundary is being actively constructed or evolved) a **ConstructorSignature** that describes how the TargetSignature is produced and revised.                                     | Prevents conflating the target contract with the engineering process. |
