---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
section_id: "A.6.S:4"
section_title: "Solution — two signatures and a small constructor vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__006_solution-two-signatures-and-a-small-constructor-vocabulary.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.6.S — U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
  - "A.6.S:4 — Solution — two signatures and a small constructor vocabulary"
line_start: 20674
line_end: 20856
dependencies:
  - "A.12"
  - "A.3"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.19"
keywords:
  - "ConstructorSignature"
  - "EFEM"
  - "MVPK views (no new semantics)"
  - "TargetSignature"
  - "appear"
  - "claim register"
  - "editioning"
  - "no epistemic agency"
  - "quadrant classification is governed by A.6.B)"
  - "retargeting"
  - "signature engineering"
  - "slot/base change lexicon"
  - "two-signature arrangement"
---

### A.6.S:4 - Solution — two signatures and a small constructor vocabulary

#### A.6.S:4.0 - Ontology and effect profile — constructor operators are epistemes; admitted Systems perform the Work

This pattern relies on **Strict Distinction** (A.7), transformation discipline (A.3.4), Method and Work discipline (A.3.1, A.3.2, A.15, A.15.1, A.15.2), and the separate system-role-kind, assignment, and Work-attribution disciplines (A.2, A.2.1, F.6):

* **ConstructorSignature (operator description; EntityOfConcern and Description-episteme boundary).**
  The ConstructorSignature is an **Episteme** (typically a Description/Spec) that *describes* a small family of constructor operations for signature evolution.
  For each constructor-operation family, the ConstructorSignature SHALL state whether it follows the general EFEM rules in A.6.2, the more specific viewing rules in A.6.3, or the retargeting rules in A.6.4. Its declaration states the effect of the episteme-to-episteme morphism on exact claim content, EntityOfConcern, and effective ReferenceScheme and separately names any empirical-grounding relation, representation relation, describing-use viewpoint selection, view-conformance claim, or edition value it consumes.
  As EFEM, constructor ops are **effect‑free** in the strict A.6.2 sense: **no Work, no Mechanism application, and no mutation of systems or carriers**.
  Concretely: an EFEM step *derives* a successor episteme (often a new edition) and its structured delta; the physical act of materialising that successor on carriers (files, repositories, registries, releases, or carrier and source-currentness records) is **Work** performed by an admitted System. Any local system-role classification remains a separate claim. F.6 identifies the assignment under which each performer acted; a short account may omit an assignment identifier that no later claim uses.

  Value-and-relation alignment requirement (C.2.1:7.1 and A.6.5): for each constructor-operation entry, a conforming ConstructorSignature SHALL state which C.2.1 identity values and neighboring relations it reads or changes and whether it follows the general A.6.2 EFEM rules, the A.6.3 viewing rules, or the A.6.4 retargeting rules. SlotKind, ValueKind, and refMode terms are used only for an exact reusable relation declaration and remain local to its `RelationSignature`.

* **Enactor (capability) vs enactment (world-contact).**
  An admitted `U.System` uses a **Method** and performs particular steps as dated **Work** on carriers such as repositories, releases, pins, and carrier and source-currentness references. A MethodDescription is a separate episteme that describes the Method. F.6 identifies the assignment under which each performer acted; neither a local system-role kind nor an assignment acts. A short account may omit an assignment identifier that no later claim uses.
  This is where traces, review records, evidence refs, and publication carriers appear.

Therefore:

* A ConstructorSignature **describes** how a TargetSignature may be constructed/evolved; it MUST NOT be written as if it *performs* the construction.
* Any step that performs measurements, actuation, validation runs, or other side‑effects is **not** an EFEM; model it as `U.Work` or a mechanism, and classify resulting claims with A.6.B.

#### A.6.S:4.1 - Core move: model signature engineering as a separate boundary

In a conforming design, model **two signatures**:

1. **TargetSignature.**
   The `TargetSignature` you want to stabilize. It is a `U.Signature` per A.6.0: direct `SubjectKind` and `RangedValueKind`, optional `ResultKind`, `SliceSet`, and `ExtentRule` when current, together with `Vocabulary`, `Laws`, and `Applicability`. These are components of the TargetSignature episteme, not a nested container. It does **not** contain admissibility gates, deontic obligations, or evidence claims (those are classified by A.6.B).

2. **ConstructorSignature.**
   A *separate* `U.Signature` whose purpose is to describe the **engineering operations** used to construct and evolve the SoI. Intuitively: it is the boundary signature of the enabling activity that produces the target signature.

A.6.S names this pairing discipline **U.SignatureEngineeringPair**: a signature engineering arrangement where a ConstructorSignature is explicitly defined for (at least) one TargetSignature.

Minimal definition (informative): a `U.SignatureEngineeringPair` binds exactly two signature epistemes for one named signature-engineering question and use: a **TargetSignature** (the boundary signature under stabilization) and a **ConstructorSignature** (the enabling signature describing the constructor operations used to build or evolve the TargetSignature). Each signature carries its own effective scheme, criterion, dependencies, and applicability in claim content; the pair stores neither a local kind nor a source-local meaning.

**Terminology note (C.2.1 alignment + twin discipline).**
This pattern uses `TargetSignature` as the **Tech designation** for “the signature episteme under construction and stabilisation”. It is a designation of the signature's place in this arrangement, not a local system-role kind or system-role assignment.
If a publication needs an explanatory Plain label, it MAY use **“signature of interest (SoI)”** as a **Plain twin** for `TargetSignature`, but Plain twins are didactic only and MUST NOT appear in conformance or acceptance clauses.

Do not conflate the **TargetSignature**—the signature episteme being engineered and published—with its exact C.2.1 EntityOfConcern, the boundary or entity that its claims concern.

In C.2.1 terms:
* the TargetSignature is the episteme, and distinct editions remain distinct epistemes under the C.2.1 identity rule;
* its exact EntityOfConcern is the boundary or entity in the world or model that the signature claims concern; and
* if empirical grounding is claimed, an exact `EpistemeEmpiricalGroundingRelation` separately names the covered claims and grounding holon.
If the “SoI” phrasing risks confusion with C.2.1 “entity‑of‑interest” talk, keep it out of Tech/normative prose and use **TargetSignature** vs **ConstructorSignature** consistently.

**Mint-or-Reuse note (informative).**
This pattern introduces the following **Tech names** in the A.6 cluster:
* **TargetSignature** — the target boundary signature episteme being stabilised;
* **ConstructorSignature** — the enabling signature (episteme) describing constructor operations for TargetSignature evolution;
* **U.SignatureEngineeringPair** — the two‑signature arrangement (TargetSignature + ConstructorSignature).

If any Plain twins are used (for example, “signature of interest”), they MUST follow the E.10 and F.* twin discipline: one-to-one correspondence under the effective scheme, registry entry when that public reuse needs one, and no Plain twin in normative register.

The intended shape is:

* TargetSignature is the published boundary signature used by downstream design and realization work.
* ConstructorSignature is the enabling signature used by authors and reviewers to produce and revise the TargetSignature in a disciplined, reproducible way.

This directly operationalises the idea already hinted in the A.6 cluster relations: A.6.5 and A.6.6 can be read as constructor/enabling operations for building well‑formed signatures. The new step is to **bundle those operations into an explicit ConstructorSignature** rather than leaving them as implicit editorial practice.

#### A.6.S:4.2 - Minimal constructor operation vocabulary

A conforming ConstructorSignature **SHALL** (conceptually) expose a *small, composable* set of operations. At minimum, include two groups of constructor operations, drawn from existing A.6 subpatterns:

**(A) Slot‑level constructor operations** (from A.6.5)

Use the canonical slot verbs to express “what changed” without ambiguity:

* `bind` or `rebind` (Identifier → SlotKind/slot‑instance; name binding only)
* `fill`
* `initialize` (first fill)
* `assign`, `set`, `write`, or `update` (subsequent fill; by‑value replacement)
* `retarget` (Ref slot update; same SlotKind/ValueKind)
* `substitute` (typed replacement with explicit compatibility claim)
* `resolve` or `dereference` (Ref → referent)
* `pass` (parameter filling at call boundaries)

**Avoid “mutate” as a generic edit verb.**
In Core, `mutate/modify` denotes **referent‑internal change while the slot‑content (Ref handle) stays the same**.
In edition‑disciplined contexts, prefer “revise, re-edition, and retarget” rather than “mutate”.

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
`refreshWitnesses` is an **edit of witness references**, not the generation of new evidence: producing/collecting new witness carriers is **Work**; `refreshWitnesses` only updates the base declaration to reference them.

**Optional but common: view construction operations (A.6.3)**

If the TargetSignature is published via MVPK (recommended), include constructor operations that produce views as **EpistemicViewing** (A.6.3) of the TargetSignature:

* “Emit MVPK faces” as views (PlainView, TechCard, InteropCard, AssuranceLane), explicitly treated as views and governed by E.17 “no new semantics”.
  In particular:
  * `PlainView`, `TechCard`, and `InteropCard` MUST add no new claims beyond the underlying TargetSignature or Mechanism claim set.
  * `AssuranceLane` MAY include procedural adjudication guidance and carrier pointers, but any normative pass-or-fail criteria MUST be stated canonically as `E-*` claims and be cited by ID.

These are best modeled as view‑producing operations whose output is an MVPK face, with the explicit constraint that the face is a view and therefore does not introduce new claims about the EntityOfConcern.
Publishing those faces (commits, releases, registry writes) is Work on carriers; it is not “the signature doing things”.

#### A.6.S:4.3 - Change discipline: Viewing vs Retargeting vs editing

To connect signature engineering to A.6.2–A.6.6, treat changes in four buckets:

1. **Viewing (A.6.3).**
   Use when you change *presentation* (views, stakeholder cards, projections) while preserving the EntityOfConcern.

2. **Slot and base construction edits (A.6.5 and A.6.6).**
   Use when you unpack and make explicit what was implicit (slot kinds, ref modes, base declarations), or when you adjust the SoI’s internal structure without changing what it is “about”.

3. **Editioning + reference retargeting (A.6.5).**
   Use when the TargetSignature meaningfully changes and you need a **new SoI edition** for downstream coordination. In that case, do not silently mutate the existing edition: mint a successor edition and **retarget references** (`Retarget<…>` in the relevant Ref slots) to the new edition.

4. **Epistemic retargeting and structural reinterpretation (A.6.4; rarer).**
   Use only when `EntityOfConcernRef` itself changes under an explicit `KindBridge` and stated invariants (e.g., reinterpretation across kinds/planes). This is distinct from ordinary “new version of the same TargetSignature”.

Rule of thumb:

* If the change can be defended as “same TargetSignature, clearer publication”, prefer slot/base construction plus viewing.
* If the change is “new TargetSignature edition for consumers”, require a new edition plus explicit reference retargeting.
* If the change is “different EntityOfConcern or different kind”, use A.6.4 retargeting under `KindBridge` with explicit invariants.

**EFEM discipline.**
Every constructor operation family declared as an EFEM MUST declare `entityOfConcernChangeMode ∈ {preserve, retarget}` (A.6.2).
**Editioning is orthogonal**: you MAY mint a new edition even under `preserve`, but if you do, downstream references MUST be updated explicitly via slot discipline (A.6.5).
Any operation that performs measurements/actuation/side‑effects MUST be modeled as Work or Mechanism application, not as a constructor op.

#### A.6.S:4.4 - Publication and claim discipline for reproducibility

A conforming signature engineering arrangement **SHOULD** include two publication‑adjacent constraints:

1. **MVPK publication for the TargetSignature (E.17).**
   Publish the TargetSignature through MVPK faces as `U.View` projections with viewpoint accountability (`viewRef` + `viewpointRef`). Each face must be explicitly treated as a view and must not introduce new semantic commitments beyond the underlying signature/mechanism claim set (per E.17 “no new semantics”).

2. **Claim Register for boundary discipline (A.6.B).**
   Maintain a claim register that assigns stable identifiers to atomic claims and classifies them into the correct quadrant (L/A/D/E). The engineering benefit is that changes to the SoI can be tracked as changes to specific claims rather than as unstructured prose diffs.

This keeps signature engineering aligned with A.6.B’s separation:

* **Laws** are stated in the SoI (L-claims).
* **Admissibility** and operational gate conditions are governed by mechanisms (A-claims).
* **Deontics** are about agents (D‑claims), not about epistemes.
* **Evidence/work effects** are recorded as outcomes of work (E‑claims), not smuggled into signatures.

#### A.6.S:4.5 - Signature-construction relation in a transformation-flow structure (informative)

If a team represents signature-construction work as an `E.18` `TransformationFlowStructure`, the A.6.S constructor arrangement is referenced from that structure rather than converted into a second graph ontology:

* EFEM constructor operations appear as transformation-flow loci whose governed value is an A.6.2 effect-free episteme-to-episteme morphism over signature epistemes. They remain constructor-operation descriptions, not performed work.
* Concrete carrier writes (commits, releases, registry writes, and carrier and source-currentness pinning) are performed-Work loci or Work occurrences identified with A.15 and A.15.1. Use A.2 for any separate local system-role classification and A.2.1 and F.6 for the assignment under which each performer acted; a short flow account may omit an unused assignment identifier. Use A.10 for evidence and provenance, E.17 for publication, and the relevant carrier patterns for carriers. None of these values is a constructor operation.
* Validation and admission checks are gate/check loci governed by A.21, with `OperationalGate(profile)`, `GateProfile`, `GateCheckRef`, `GateDecision`, and `DecisionLogRef` named when a gate-decision relation is present.
* Any `EntityOfConcernRef` or kind change is a retargeting relation or structural-reinterpretation relation governed by A.6.4, with explicit `KindBridge` plus invariants and witnesses.

This mapping is optional; A.6.S stays usable as a lightweight signature-engineering discipline even when no `E.18` `TransformationFlowStructure` is declared. When it is declared, use E.18 for the flow structure, C.29 for any graph or path representation, and A.6.S for the signature pair and constructor-operation vocabulary.

#### A.6.S:4.6 - State during construction (informative)

Do not mint a new kernel “signature state” unless you need it.
In most cases, use:

* **edition** + explicit continuity/withdrawal links for semantic evolution, and
* a coarse **status** (`Draft`/`Review`/`Stable`/`Deprecated`) for process signalling.

If a project needs a finer state-change policy (for example, “proposed → reviewed → published → frozen”), model it as Work policy in the ConstructorSignature's Applicability or as a separately identified local state-change episteme; keep the TargetSignature semantics unchanged.
Where state-change policy is normative, express it as a status or state-transition policy for the relevant signature episteme or publication under its effective scheme and ClaimScope, with A.2.4 and F.10 status-use discipline and A.6.5 slot discipline where needed. Do not call the episteme's status a system role or create a system-role assignment for it; use E.10.ROLE to route bare *role* wording to the actual status, state, declaration position, or other direct branch.

