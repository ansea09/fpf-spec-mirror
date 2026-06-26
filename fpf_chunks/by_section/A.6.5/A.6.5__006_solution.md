---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__006_solution.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:4 — Solution"
line_start: 15914
line_end: 16048
dependencies:
  - "A.1"
  - "A.2.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "F.6"
  - "U.EpistemeSlotRelation"
  - "U.MultiViewDescribing"
  - "U.Signature"
keywords:
  - "argument position"
  - "pass-by-reference"
  - "pass-by-value"
  - "reference"
  - "signature"
  - "slot"
  - "substitution"
  - "value"
---

### A.6.5:4 - Solution

`U.RelationSlotDiscipline` says that a relation-bearing structure with named positions uses `SlotSpec` declarations. A `SlotSpec` separates the local position, the admitted filler kind, and the instance reference mode.

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

This is a discipline over relation-bearing structures. It is not the identity of the relation itself. It is not a new kind for every possible field name. It is not a publication form.

#### A.6.5:4.1 - SlotKind, ValueKind, and RefKind

**SlotKind** names one position in one relation-bearing structure. It is structural and local to a governing relation, operator, record, signature vocabulary item, episteme slot relation, role assignment, interface specification, or other signatured bundle. Examples include `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `EvidenceTargetClaimSlot`, `RoleValueSlot`, `AssignmentWindowSlot`, `ServiceEndpointSlot`, and `DatasetSlot`.

**ValueKind** names what kind of value may fill that position. Examples include `U.Entity`, `U.Holon`, `U.System`, `U.Role`, `U.Method`, `U.MethodDescription`, `U.Episteme`, `U.ClaimGraph`, `U.Viewpoint`, `U.Characteristic`, and `U.ReferenceScheme`. A ValueKind is governed by its own pattern. It does not become a SlotKind because it fills a slot.

**RefKind** names how a filled relation instance points to a value when the value is not embedded by value. Examples include `U.EntityRef`, `U.HolonRef`, `U.SystemRef`, `U.RoleRef`, `U.MethodRef`, `U.EpistemeRef`, `U.ViewpointRef`, and `U.CharacteristicRef`. A RefKind is about references, not about the value itself.

**Slot instance** is the particular position in one filled relation instance. **Slot content** or **slot filler** is what the filled instance stores at that position. The slot content is either an embedded value of the ValueKind or a reference of the RefKind. If it is a reference, resolving it gives a referent value or editioned referent.

#### A.6.5:4.2 - Well-formed SlotSpec discipline

For each named position in a relation-bearing structure:

```text
Well-formedness constraint A6.5-S1 (SlotSpec completeness):
  each SlotSpec has exactly one SlotKind, exactly one ValueKind, and exactly one refMode.

Well-formedness constraint A6.5-S2 (SlotKind locality):
  SlotKind is interpreted relative to the governing relation-bearing structure.

Well-formedness constraint A6.5-S3 (ValueKind preservation):
  a substitution at a slot preserves the SlotKind and uses a filler whose kind is the declared ValueKind or an admitted subkind.

Well-formedness constraint A6.5-S4 (RefKind honesty):
  when refMode is a RefKind, the slot content is a reference value, not the referent itself.
```

A `U.Signature` uses this discipline when its vocabulary declares an n-ary relation or operator. The SlotSpecs live inside the relevant vocabulary item. They do not add a fifth row to the `A.6.0` Signature Block and do not move operational guards from `A.6.1` or method and work patterns into the signature.

#### A.6.5:4.3 - Naming discipline for `*Slot` and `*Ref`

Use `*Slot` only for SlotKinds. Do not use `*Slot` for ValueKinds, RefKinds, concrete fields, or publication labels.

Use `*Ref` only for RefKinds or fields whose type is a RefKind. Do not use `*Ref` for SlotKinds or for the value itself.

ValueKind names do not carry `*Slot` or `*Ref`. If a current source name violates this rule, recover the intended kind before renaming. The repair may split one old token into a SlotKind, a ValueKind, and a RefKind or field.

Do not use `Role` as the head noun for a SlotKind. `U.Role` is a role value governed by `A.2`. A relation position that admits a `U.Role` filler can be named `RoleValueSlot`; a position filled by a system or acting holon under a role assignment can be named `RoleHolderSlot` or a context-specific refinement. The head remains `Slot`, and the `U.Role` value remains a value.

#### A.6.5:4.4 - Role assignment under slot discipline

`U.RoleAssignment` is a typed assignment relation value for work-facing roles. It can be expressed with SlotSpecs without reducing roles to slots.

Core SlotSpecs for a work-facing role assignment include:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `RoleHolderSlot` | `U.System` or acting holon admitted by the governing work or method pattern as system-like performer | `RefKind` selected by the governing context | The system or admitted acting holon that holds the role in this bounded context. |
| `RoleValueSlot` | `U.Role` | `RefKind` or by-value local role value | The role value being assigned. |
| `BoundedContextSlot` | `U.BoundedContext` | `RefKind` or by-value context descriptor | The context in which the assignment has meaning. |
| `AssignmentWindowSlot` | temporal window value governed by the temporal pattern current in the context | `ByValue` or selected RefKind | The time window for the assignment claim. |
| `AssignmentJustificationSlot` | source, decision, gate, or claim relation governed by its direct pattern | selected by the direct pattern | The relation that justifies the assignment when such justification is current. |

Direct work-role patterns may add work-role qualifier slots. Evidence-use, source-use, publication-use, standard-use, requirement-use, assurance-use, and status-use relations do not become RoleAssignment slots merely because their prose says "role of the evidence" or "role of the standard". Those uses are governed by their direct patterns.

`RoleEnactment` is not introduced here as a root ontic. When a named fact is needed, use `RoleEnactmentFact` for the derived fact that a `U.Work` occurrence was performed under a specific `U.RoleAssignment`, or write the direct relation such as `Work.performedBy = RoleAssignment`.

#### A.6.5:4.5 - Evidence-use and status-use relations are not work roles

An episteme may be used as evidence for several claims. This creates evidence-use relation instances, not several roles held by the episteme.

Typical evidence-use SlotKinds include:

| SlotKind | ValueKind | Meaning |
|---|---|---|
| `EvidenceEpistemeSlot` | `U.Episteme` or admitted evidence episteme species | The episteme being used as evidence. |
| `EvidenceTargetClaimSlot` | claim value governed by the claim pattern current in context | The claim to which the evidence-use relation is addressed. |
| `EvidenceClaimGroundingHolonSlot` | `U.Holon` when the target claim needs grounding | The holon in which the target claim is grounded when current. |
| `EvidenceClaimScopeSlot` | scope value governed by the claim or evidence pattern | The scope for the evidence-use relation. |
| `EvidencePolaritySlot` | confirming, rebutting, undercutting, or another locally governed polarity value | The direction of bearing on the target claim. |
| `EvidenceRelevanceWindowSlot` | temporal or freshness window value | The window in which the evidence-use claim remains usable. |
| `EvidenceAssuranceUseSlot` | assurance-use relation or assurance input value | The assurance use when current. |
| `EvidenceWeightModelSlot` | weight, confidence, or calculus value governed by the evidence or assurance pattern | The model used to aggregate or compare evidence when current. |

Status-use relations likewise name the status bearer, status value, status scope, status window, and use relation under the direct status or assurance pattern. They do not create status roles for epistemes.

#### A.6.5:4.6 - Interface, port, and signature wording

`A.6.5` is often needed when a source says "interface", "port", "endpoint", "API", "protocol", or "connector". These words do not select one FPF kind by themselves.

Recover the current EntityOfConcern first:

| Source cue | Common recovery |
|---|---|
| interface between modules | module-interface claim, boundary claim, port relation, signature, protocol, or evidence of conformance under `A.6.M` and architecture patterns |
| port in a functional description | functional port or transformation-flow structure under `A.6.F`, `E.18`, or architecture patterns |
| API | software API description, service-access description, protocol, publication form, or boundary claim bundle |
| endpoint | relation endpoint, service endpoint, network endpoint, evidence target, claim target, or ordinary source label |
| signature | `U.Signature` under `A.6.0`, using A.6.5 SlotSpecs for n-ary vocabulary items |

After the governing EntityOfConcern is selected, use `A.6.5` only to state the SlotSpecs inside that value. Do not mint a generic `U.Interface` or erase interface language when it is the ordinary engineering recognition cue.

#### A.6.5:4.7 - Slot operation lexicon

Use slot-operation words by the link they affect.

| Operation word | Affected link | Use |
|---|---|---|
| bind or rebind | identifier or name to SlotKind, slot instance, or language-level value | Use for name binding. Do not use `bind` as a synonym for writing slot content. |
| fill | slot instance to slot content | Use as the generic verb for providing content to a slot instance. |
| initialize | first fill | Use when the slot instance previously had no content. |
| assign, set, or update | subsequent slot-content replacement | Use when replacing content in an already filled slot instance. |
| retarget | reference slot update, preserving SlotKind and ValueKind | Use when replacing one reference with another reference to another referent. |
| substitute | typed replacement with explicit compatibility claim | Use when the important claim is ValueKind or admitted-subkind compatibility. |
| resolve or dereference | reference to referent | Use when a reference is mapped to the value or editioned referent it points to. |
| revise or issue a re-edition | referent content change under edition discipline | Prefer these words to vague mutation when the referent itself changes across editions. |
| pass | parameter slot filling at a call or service boundary | Use only when the current relation is a method, service, protocol, or call boundary with parameter slots. |

Avoid person metaphors such as `occupant` for slot content. Use `slot content` or `slot filler`. If a local Plain register uses a metaphor, it cannot carry FPF-governed role, evidence, or status meaning.

#### A.6.5:4.8 - Binding time and currentness of slot operations

"Early binding" and "late binding" are admissible only after the affected link is named.

Use:

- early or late name binding for identifier-to-slot or identifier-to-value links;
- early or late slot filling for when a slot instance receives content;
- eager or lazy resolution for when a reference is resolved to a referent;
- dynamic dispatch only when a method or operation selection relation actually uses runtime context to select the invoked operation.

If the text does not say which link is affected, keep the phrase ordinary or repair it before use.

