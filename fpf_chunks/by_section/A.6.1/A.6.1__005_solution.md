---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__005_solution.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:4 — Solution"
line_start: 10395
line_end: 10542
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "B.3"
  - "C.16"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.18"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:4 - Solution

#### A.6.1:4.1 - Definition

`U.Mechanism` is a specialization of `U.Signature`. A mechanism publication includes the universal four-row Signature Block:

| Signature row | Mechanism realization |
| --- | --- |
| `SubjectBlock` | `SubjectKind`, `RangedValueKind`, `SliceSet`, `ExtentRule`, and optional `ResultKind` |
| `Vocabulary` | `OperationAlgebra` with SlotSpecs for operation arguments |
| `Laws` | `LawSet` of equations and invariants |
| `Applicability` | bounded context, plane, time, and compliance notes |

Mechanism-only additions are `AdmissibilityConditions`, `Transport`, `GammaTimePolicy`, `PlaneRegime`, and `Audit`. They extend the Signature without creating a fifth Signature row.

#### A.6.1:4.2 - Mechanism declaration

```text
MechanismDeclaration:
  DeclarationHeader:
  Imports:
  SubjectBlock:
    SubjectKind:
    RangedValueKind:
    SliceSet:
    ExtentRule:
    ResultKind:
  SlotIndex:
  OperationAlgebra:
  LawSet:
  AdmissibilityConditions:
  Applicability:
  Transport:
  GammaTimePolicy:
  PlaneRegime:
  Audit:
```

`DeclarationHeader` states `id`, `version`, and publication state. If the mechanism is intended to be imported or reused, it includes a `SignatureManifest`; `DeclarationHeader.id`, `DeclarationHeader.version`, publication state, imports, and public symbols must match the manifest.

`Imports` names signatures that supply non-kernel symbols used by the Signature Block or operation algebra. Imports are acyclic. Imported signatures are opaque: reference only their provided symbols and ClaimIds.

`SubjectKind` names the EntityOfConcern kind acted upon. `RangedValueKind` references an existing C.3 `U.Kind`, admitted durable U-kind, Concept-Set row, or imported signature symbol. A mechanism publication does not define a new core kind inside the mechanism definition.

`SlotIndex` is a derived index over SlotSpecs used by `OperationAlgebra` and guard-only SlotSpecs used by `AdmissibilityConditions`. It does not replace per-operator SlotSpecs and does not relax A.6.0 argument discipline.

`OperationAlgebra` names operations whose signatures use SlotKinds from the SlotIndex. Each operation publishes SlotSpec triples for argument positions; numeric indices are presentation only.

`LawSet` states equations and invariants. Admission and eligibility tests belong under `AdmissibilityConditions`, not under `LawSet`.

`AdmissibilityConditions` are deterministic, context-local guard predicates that fail closed. Unknowns become `degrade` or `abstain`; they are not coerced to zero or false.

`Applicability` binds the mechanism to a `U.BoundedContext` with plane, time, and comparison-compliance notes.

`Transport` is a declarative policy surface for cross-context or cross-plane use. It names the Bridge, channel, and `ReferencePlane` relation; when planes differ it names the plane-loss policy. It does not introduce a `U.Transfer` edge and does not restate CL, Phi, Psi, or plane-policy tables. Penalties are recorded in Reliability or effective Reliability only; Formality and Guarantee stay invariant.

`GammaTimePolicy` states point, window, or policy. There is no implicit latest.

`PlaneRegime` declares reference-plane treatment when values, operations, or comparisons cross planes.

`Audit` is a conceptual audit surface. It cites policy ids, crossing records, and edition pins by reference rather than embedding telemetry details or tool-specific execution details in the kernel pattern.

#### A.6.1:4.3 - U-kind and local declaration settlement

This pattern retains `U.Mechanism` as the durable U-kind governed by this host. The other names in the mechanism declaration are local relation, record, or description values, not additional root U-kinds admitted by this sentence.

| Name | Disposition |
| --- | --- |
| `U.Mechanism` | Durable U-kind: law-governed specialization of `U.Signature` over `SubjectKind` and `RangedValueKind`, with operation algebra, laws, admissibility, transport, audit, and monotone realization. |
| `MechanismMorphismRelation` | Mechanism-local relation constructor for refinement, extension, equivalence, quotient, product, and transport relations among mechanisms. It is governed here and by A.6.5 SlotSpec discipline; it is not a root U-kind. |
| `MechanismDeclarationTemplate` | Local record form for publishing a mechanism declaration. It is a description/publication aid, not a durable U-kind. |
| `MechanismDescription` | Description episteme for a mechanism declaration, governed by the episteme and publication patterns when description or publication claims are current. |
| `MechanismFamilyDescription` | Description form grouping one mechanism declaration with several monotone realizations; it does not admit a separate family U-kind here. |
| `MechanismInstanceDescription` | Context-local description of one mechanism declaration with windows, regimes, and BridgeIds; it is not an operational telemetry record and not a root U-kind. |

It reuses `U.Signature`, C.3 kind values, admitted durable U-kinds, `U.BoundedContext`, Bridge, ReferencePlane, characteristic-space, measurement, and reliability-channel terms without changing their governing patterns.

#### A.6.1:4.4 - Method and mechanism positions

Do not decide the method and mechanism question by vocabulary. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: is the current claim a law-governed mechanism declaration or realization over a `SubjectKind` and `RangedValueKind`? If the source label also raises method, method-description, formal-substrate, work-plan, dated-work, evidence, source, gate, result, publication, or temporal claims, keep those values linked only by explicit relation positions and apply their own governing patterns.

`U.Method` governs the context-local way of doing a transformation or enactment. `U.Mechanism` governs a law-governed declaration over a `SubjectKind` and `RangedValueKind`: operation algebra, laws, admissibility predicates, applicability, transport, audit surface, and monotone realization relation.

A solver-selection scheme can be a `U.Method` in one bounded context; a selector mechanism can declare operations over candidate methods; a selected method can fill a mechanism slot; and a mechanism realization can be implemented through a method description and enacted in dated work. Those links do not make `A.3.1` sufficient for a mechanism claim or `A.6.1` sufficient for a method claim.

Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing. Slot-position labels do not create alternate ontology.

#### A.6.1:4.5 - Morphisms and constructors

`MechanismMorphismRelation` provides structure-preserving relations and constructors between mechanisms:

| Relation or constructor | Meaning |
| --- | --- |
| Refinement `M' <= M` | narrows SubjectBlock or SlotSpecs and strengthens LawSet or AdmissibilityConditions; it must be safe for substitution |
| Extension `M <=+ M''` | adds operations or new SlotKinds for new operations without weakening existing laws or guards |
| Equivalence `M == M'` | maps subjects and operations bijectively while preserving and reflecting LawSet up to isomorphism |
| Quotient | factors a mechanism by a congruence such as a normalization equivalence |
| Product | combines independent RangedValueKinds componentwise and forbids hidden cross-operations |
| Transport | lifts a mechanism across contexts or planes using Bridge-only policy and Reliability penalties |

For specialization chains:

* name the parent and the morphism kind;
* keep inherited SlotKinds invariant;
* allow ValueKind narrowing and guard strengthening in Refinement;
* introduce extra required inputs only through new operations or adapter mechanisms;
* keep root mechanisms general and domain-specific policies in specialized mechanisms.

#### A.6.1:4.6 - Description records

`MechanismDescription` is the ordinary description episteme for a mechanism declaration. It can show:

```text
Mechanism:
  Imports:
  SubjectBlock:
  SlotSpecs:
  OperationAlgebra:
  LawSet:
  AdmissibilityConditions:
  Transport:
  GammaTimePolicy:
  PlaneRegime:
  Audit:
```

`MechFamilyDescription` groups one MechanismDeclaration with multiple realizations. Each realization may tighten laws or guards and must not relax them.

`MechInstanceDescription` records a mechanism declaration in one context with windows, named regimes, and BridgeIds. It is a conceptual instance description, not an operational telemetry record.

#### A.6.1:4.7 - Defaults

* Local-first semantics: judgments are context-local; crossings are explicit and costed in Reliability.
* Comparison compliance: numeric comparison or aggregation uses comparison, measurement, and characteristic-space rules; partial orders return sets.
* Tri-state guard discipline: unknown guard results become `degrade` or `abstain`.
* Reliability-only penalties: Bridge, kind, scope, and plane losses affect Reliability or effective Reliability, not Formality or Guarantee.
* Opaque imports: imported signatures are referenced by provided symbols and ClaimIds.

#### A.6.1:4.8 - USM and UNM as mechanism instances

USM can be represented as a `U.Mechanism` over `ContextSliceSet` with operations such as membership, subset, intersection, span union, translate, widen, narrow, and refit. Its laws include serial intersection, span union only under a named independence assumption, and mandatory time policy.

UNM can be represented as a `U.Mechanism` for normalization classes and normalization equivalence. It uses normalize-then-compare discipline, scale-appropriate transforms, and comparison-compliance rules.

These examples are informative. They show that scope, normalization, comparison, scoring, and publication mechanisms can share one kernel mechanism shape without changing their own governing patterns.

