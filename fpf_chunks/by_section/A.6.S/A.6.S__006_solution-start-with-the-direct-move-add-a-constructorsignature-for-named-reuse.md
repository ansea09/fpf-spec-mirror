---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
section_id: "A.6.S:4"
section_title: "Solution - start with the direct move; add a ConstructorSignature for named reuse"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__006_solution-start-with-the-direct-move-add-a-constructorsignature-for-named-reuse.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.6.S — TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
  - "A.6.S:4 — Solution - start with the direct move; add a ConstructorSignature for named reuse"
line_start: 20983
line_end: 21080
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.6"
  - "A.6.0"
  - "A.6.2-A.6.6"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.6"
keywords:
  - "appear"
  - "quadrant classification is governed by A.6.B)"
---

### A.6.S:4 - Solution - start with the direct move; add a ConstructorSignature for named reuse

#### A.6.S:4.0 - Keep the signature, arrow, application, and Work separate

The smallest account names the actual object and move. Describe a signature revision through its source and receiving signature epistemes. A changed C.2.1 discriminator identifies another episteme; an edition or continuity relation requires its own source use, continuation rule, and preserved or deliberately changed features. Republishing unchanged claim content need not identify another episteme. A view, direct relation assertion, operation application, carrier write, and performed Work remain under their own patterns.

A **ConstructorSignature** is optional. When used, it is a `U.Signature` whose reusable declaration content describes a family of constructor operations: its subject and value or result range, vocabulary, laws, and applicability. It does not perform those operations and does not contain the Work that applies them.

If a constructor family also uses an A.6.2 mathematical arrow, identify that arrow separately. The arrow relates exact source and receiving epistemes. Its rule states how their claim content, EntityOfConcern, and effective ReferenceScheme compare. When it reads a neighboring grounding, representation, conformance, edition, or provenance occurrence, name that occurrence and the endpoint facts compared; the arrow neither changes the occurrence nor makes it obtain. A.6.3 and A.6.4 apply only to their exact viewing or EntityOfConcern-retargeting cases.

When dated authoring, deriving, materializing, validating, storing, or publishing Work is claimed, first recover each actual performer as a System under A.1 and its complete A.13 core: the local agential system-role kind and criterion, System classification, obtaining A.2.1 assignment, and the scope, working situation, and window needed by the use, with evidence for those claims. A.15.1 then independently admits the dated occurrence from its performance history, at least one Method actually followed, temporal extent, and at least one obtaining locally declared containing-System relation. Use F.6 afterward only for precise assignment-bound attribution through that same obtaining assignment; missing or failed F.6 leaves the independently admitted Work intact. Additional classifications or assignments, an operation application and its bindings, the resulting episteme, and carrier, evidence, or publication relations enter only when their own claims are current. Add an agency-characteristic profile only when the local criterion, a claimed characteristic, or an assurance use requires it under A.13/A.15.1.

#### A.6.S:4.1 - Decide whether a second signature is needed

Start with the **TargetSignature**: the `U.Signature` being authored, stabilized, or revised. Its A.6.0 declaration content identifies its subject and value or result range and supplies the reusable vocabulary, laws, and applicability that make it a signature. It contains neither operational gates, deontic duties, evidence claims, nor construction Work merely because those topics occur nearby.

Add a **ConstructorSignature** only when a named receiver needs reusable constructor-operation vocabulary, laws, and applicability. The receiver may be a later editioning process, another authoring System, a publication process, or another repeatable use that would otherwise have to reconstruct the same operation declaration. A one-off edit, direct relation assertion, arrow, operation application, or Work occurrence does not qualify by itself.

The two signatures remain separate C.2.1 epistemes. State only the relation that is actually current:

* when one signature cannot interpret a required term or replay a law without the other, use the exact A.6.0 declaration-dependency claim;
* when a System uses a Method or MethodDescription that cites the ConstructorSignature while revising the TargetSignature, state that method/source use and any actual application or Work under its direct pattern;
* when both signatures are merely relevant to the same local question, name them without inventing a pair relation; and
* if a future use needs a durable relation occurrence between them, first supply that relation kind's participant meanings, predicate, applicability, occurrence identity, and E.24/E.24.UK settlement. A.6.S supplies none by default.

`TargetSignature` and `ConstructorSignature` are Tech designations of each signature's place in this use, not local system-role kinds. A publication may explain TargetSignature as “the signature being engineered”; it need not introduce the abbreviation *SoI*. Do not conflate the TargetSignature with its exact C.2.1 EntityOfConcern. Distinct signature editions remain distinct epistemes when their C.2.1 discriminator triples differ; any empirical-grounding, edition, continuity, dependency, source-use, or publication relation remains separately identified.

**Mint-or-reuse note.** A ConstructorSignature is admitted by the ordinary A.6.0 membership rule, not by being named next to a TargetSignature.

#### A.6.S:4.2 - Choose the constructor vocabulary that the receiving use needs

A ConstructorSignature declares only operation families that a named receiver will reuse. It need not contain both A.6.5 slot operations and A.6.6 declaration-change labels, and it need not contain either family when another direct operation declaration is enough.

**Slot operations, when current.** Use A.6.5 when a reusable relation declaration needs stable participant positions, fillers, or references. Its vocabulary distinguishes name binding, first or later by-value filling, reference retargeting, typed substitution, resolution, and parameter passing. Keep `bind` for name binding; do not use generic *edit* to hide a reference retargeting or a referent-internal change. A one-off ordinary edit that needs no reused SlotSpec stays an ordinary edit.

**Assertion or declaration history, when current.** Use A.6.6 first to state the actual dependent, base, and direct relation. Stop when that readable assertion answers the use. If a named receiver needs the history of an optional assertion representation or reusable declaration, its local labels such as `declareBase`, `rebase`, `rescope`, `retime`, or `refreshWitnesses` may describe which represented field changed. They do not establish or change the world-side relation. Producing new evidence is separate Work; changing a witness reference is only a record edit.

**Mathematical arrows, when current.** An operation description may cite an A.6.2, A.6.3, or A.6.4 arrow only when that mathematical relation is useful to the receiver. The ConstructorSignature states the arrow family and the endpoint values or facts it reads or compares. The arrow remains effect-free; an application that produces a receiving episteme and any performed Work remain separate.

**Publication operations, when current.** For E.17 publication, a ConstructorSignature may declare a reusable publication or view-producing operation when its named receiver needs that declaration. Apply A.6.3 only when the operation uses a mathematical source-to-receiving viewing construction; identify those epistemes and the viewing rule. Keep the publication face faithful to its source and apply §4.4 for any separate `U.View` claim. For publishing a face, writing a carrier, committing a file, or issuing a release, distinguish any claimed operation application under A.6.1, any actual changed-object or effect claim, and Work admitted under §4.0. Neither signature performs those actions.

The test is practical: remove the proposed operation family. If the named receiver can still perform or assess its use without reconstructing a shared vocabulary or law, leave that family out.

#### A.6.S:4.3 - Change discipline: Viewing vs Retargeting vs editing

When more than one distinction is current, classify each move separately rather than forcing all four buckets into every revision:

1. **Publication form and conditional viewing.**
   A *presentation* change (views, stakeholder cards, projections) may be an E.17/E.24.PUB form or carrier change. Use A.6.3 only when a mathematical source-to-receiving viewing construction is current, preserving the exact EntityOfConcern; E.17.0 separately governs any `U.View` membership claim.

2. **Direct edits and conditional declaration history.**
   State a one-off vocabulary, law, applicability, or reference change directly. Use A.6.5 only for reusable relation-participant declarations or reference operations that matter to the receiver. Use A.6.6 declaration history only after the actual base-dependence relation is stated and a named receiver needs that history.
3. **Editioning + reference retargeting (A.6.5).**
   Use when the TargetSignature meaningfully changes and downstream coordination needs a new TargetSignature edition. Do not silently mutate the existing episteme: identify the successor edition and retarget the references whose receiving use now selects it (`Retarget<...>` in the relevant Ref slots).


4. **Epistemic retargeting and structural reinterpretation (A.6.4; rarer).**
   Use only when the source and receiving `EntityOfConcernRef` values resolve to different exact EntitiesOfConcern. A reference-only change that still resolves to the same entity stays with its actual reference operation. A.6.4 identifies the source and receiving epistemes and one exact arrow `r`. A separate C.2.1 bounded-use assertion `q` is about that exact `r`; its ClaimGraph contains the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. A separate current-case judgement compares the exact facts with `q` and returns exactly `satisfies`, `fails`, or `cannot decide`; `cannot decide` names the missing fact and reopen condition. This is distinct from an ordinary new edition of the same TargetSignature.

Rule of thumb:

* If only the publication form or carrier changes, use E.17/E.24.PUB and stop; no slot/base declaration is required unless another receiving use needs it.
* If the change is “new TargetSignature edition for consumers”, identify the new edition and explicitly retarget the references whose receiving use now selects it.
* If the change is a different EntityOfConcern, use A.6.4's three-part account: the exact arrow `r`, a separate C.2.1 bounded-use assertion `q`, and a separate current-case judgement. A kind difference alone identifies none of them.

**EFEM discipline.**
When a constructor operation really uses an A.6.2 arrow family, declare its endpoint comparison and `entityOfConcernChangeMode` under A.6.2. An operation description that needs no mathematical arrow introduces none.
**Editioning is orthogonal**: you MAY mint a new edition even under `preserve`; references whose receiving use now selects that edition MUST be retargeted explicitly, with A.6.5 slot discipline where applicable.
For an actual measurement, actuation, validation run, carrier write, or other effect, identify any claimed operation application under A.6.1, changed-object or effect claim under its direct rule, and Work under §4.0 independently. An effect alone establishes neither application nor Work; the A.6.2 arrow performs none of these actions.

#### A.6.S:4.4 - Add publication and claim controls only when they are current

For E.17 publication, choose a faithful publication form for the bounded reader/use and point to the exact source episteme edition. Preserve E.17's no-content-extension rule: informative explanation may expose source meaning without adding boundary commitments. Only when the selected episteme's `U.View` membership is asserted or needed, resolve its exact viewpoint and E.17.0 conformance; add an A.6.3 source-to-receiving construction only when that separate relation is current. The publication occurrence, carrier, viewpoint use, conformance claim, and any publication Work remain separate. When E.17's CC-MVPK-3b boundary claim-set condition applies, keep normative face text traceable to that A.6.B claim set, with informative commentary; a face does not become a second boundary specification. No MVPK package is required merely because a signature changed.

Classify atomic claims under A.6.B, keeping laws, operational admissibility, deontic commitments, and evidence-use claims separate. Correct quadrant classification alone needs no register. Use the applicable claim register when stable identifiers serve reuse, a decision, audit, or cross-face citation; keep a return to the claim's ID or canonical source location for a material dependency. Do not put operational gates, duties, evidence results, or Work into the TargetSignature merely to make one authoring record complete. Without a need for the register, ordinary claim content and the direct patterns are enough.

#### A.6.S:4.5 - Signature-construction relation in a transformation-flow structure (informative)

If a team represents actual signature-construction Work as an E.18 `TransformationFlowStructure`, reference only the A.6.S objects and direct relations that the flow uses; do not convert them into a second graph ontology:

* Declared constructor arrows may appear at transformation-flow loci as independently defined A.6.2 values over signature epistemes. An actual operation application and any performed Work remain separately identified.
* Concrete carrier writes (commits, releases, registry writes, and carrier and source-currentness pinning) may be admitted as Work under §4.0; an E.18 Work locus may bind that already admitted Work. Use F.6 afterward only when the receiving flow account consumes precise attribution through the performer's obtaining A.13 assignment; missing or failed attribution leaves the carrier-write Work intact. Use A.10 for evidence and provenance, E.17 for publication, and the relevant carrier patterns for carriers. The constructor-operation declaration, any identified application that writes a carrier, and the admitted Work remain distinct.
* For validation and admission, E.18 governs any selected gate/check position; each check follows its own subject rule. When an actual gate decision is present, use A.21 and name its exact `GateDecisionResult`, bounded action, applicable `GateProfile` application, complete required `GateCheckApplicationResult` set, decision value, consequence, scope/window, and recheck condition. Use a short `GateCheckRef` only when a selected publication structure needs one, and a `DecisionLog` only when audit or reuse is current.
* When the source and receiving `EntityOfConcernRef` values resolve to different exact EntitiesOfConcern, use A.6.4: identify the exact arrow `r`, separate bounded-use assertion `q`, and any separate current-case judgement, then let E.18 place each only when that transformation-flow use is current. A kind change without that basis supplies no positive claim, and any actual operation application remains separate.

This mapping is optional. A one-off revision needs neither an E.18 flow nor a ConstructorSignature. When a flow is current, use E.18 for its structure and E.18.2 for any mathematical description of that selected structure, including a graph or path description. Use C.29 only for a declared mathematical-lens use. A.6.S identifies the TargetSignature and any independently justified ConstructorSignature and operation declarations.

#### A.6.S:4.6 - State during construction (informative)

Do not mint a new kernel “signature state” unless you need it.
In most cases, use:

* **edition** + explicit continuity/withdrawal links for semantic evolution, and
* a coarse **status** (`Draft`/`Review`/`Stable`/`Deprecated`) for process signalling.

If a project needs a reusable state-change policy, place it in the applicable signature's declared content or in a separately identified policy episteme, according to its actual EntityOfConcern and use. A one-off status change is stated directly.
Where state-change policy is normative, express it as a status or state-transition policy for the relevant signature episteme or publication under its effective scheme and ClaimScope, with A.2.4 and F.10 status-use discipline and A.6.5 slot discipline where needed. Do not call the episteme's status a system role or create a system-role assignment for it; use E.10.ROLE to route bare *role* wording to the actual status, state, declaration position, or other direct branch.

