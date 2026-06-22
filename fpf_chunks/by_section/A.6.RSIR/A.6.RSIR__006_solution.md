---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__006_solution.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:4 — Solution"
line_start: 14231
line_end: 14312
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.0"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "C.2.P"
  - "C.2.P.DR"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "affordance"
  - "capability"
  - "concern"
  - "endpoint"
  - "field"
  - "function"
  - "interest"
  - "interface wording"
  - "method"
  - "parameter"
  - "port"
  - "protocol"
  - "relation-signature-interface-role-slot recovery"
  - "role wording"
  - "shadow ontology"
  - "slot wording"
---

### A.6.RSIR:4 - Solution

Use `A.6.RSIR` as a first-level recovery move.

```text
RSIRRepairNote:
  encounteredWording:
  projectConcern:
  currentUse:
  recoveredEntityOfConcernOrClaimKind:
  selectedDirectGoverningPattern:
  slotDisciplineNeeded:
  neighboringCandidateValues:
  retainedSourceLabelUse:
  blockedOverread:
  nextAdmissibleMove:
  stopCondition:
```

The note is complete when the current object or claim kind is clear enough to apply the direct governing pattern, keep ordinary prose, keep quote-only wording, or stop the stronger claim.

#### A.6.RSIR:4.1 - Recovery order

1. **Recover the project concern.** Say what the project is trying to do: assign work responsibility, declare a signature, check an interface, compare functions, name a port, use evidence, assert status, describe a method, or make another claim.
2. **Recover the current governed object or claim kind.** Decide whether the wording points to relation, relation slot, signature, interface claim, role value, role assignment, role description, port, boundary claim bundle, capability, affordance, method, function, concern, interest, publication, source label, or ordinary prose.
3. **Name the direct governing pattern.** Use the table in `A.6.RSIR:4.2` only until the governing pattern is clear.
4. **Use `A.6.5` only when slot discipline is current.** SlotKind, ValueKind, RefKind, SlotSpec, slot content, and operation words belong to `A.6.5`. Relation identity, role ontology, interface semantics, evidence use, status use, work plans, work occurrences, and gate decisions belong elsewhere.
5. **Keep the source label reduced-use when no governed claim is current.** A word can remain a cue, quotation, title, or local shorthand without being admitted as FPF-governed vocabulary.

#### A.6.RSIR:4.2 - Direct governing pattern selection

| Recovered object or claim kind | Apply this governing pattern family | RSIR boundary |
|---|---|---|
| direct relation wording | `A.6.P`, with `A.6.5` for slot discipline | RSIR stops after relation repair is selected. |
| relation slot, field, parameter, argument, endpoint as relation position | `A.6.5`; sometimes `A.6.0` if the position is declared in a signature | Do not turn position labels into U-kinds. |
| signature or law-governed declaration | `A.6.0`, with `A.6.5` for relation or operator positions | Do not put mechanisms, methods, work, or evidence into the signature declaration. |
| role value | `A.2`, role-description and naming patterns in Part F | Do not treat the role as a SlotKind, capability, method, or status. |
| role assignment | `A.2.1`, `A.15`, `A.6.5` for SlotSpecs | `HolderSlot`, `RoleValueSlot`, `BoundedContextSlot`, and `AssignmentWindowSlot` are core; evidence and status uses stay outside. |
| role state or role relation structure | `A.2.5`, `A.2.7` | Do not infer role relation structure from ordinary label chains. |
| role description or durable role name | `F.4`, `F.5`, `F.18`, and `F.17` when public or cross-context reuse is current | Do not hide capability, method, or work inside the name. |
| role enactment wording | `A.15`, `A.15.1`, and `A.2.1` | Use direct work relation or `RoleEnactmentFact`; do not create a root enactment ontic. |
| module interface or architecture interface | `A.6.M` for module-interface claims; `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.TFS-REL` for architecture-of, structural-view, architecture-description, or transformation-flow-structure claims; `A.6.0` and `A.6.5` for signature or slot claims | Do not create generic `U.Interface`. |
| Markov blanket, Markov border, computational boundary, boundary leak, or active-inference boundary | Recover the current claim before choosing a pattern: accepted local Markov dynamics (`A.3.3`), mathematical or probabilistic lens (`C.29`, sometimes `C.26`), viability or measure-model-act envelope (`C.26.3`), holon delimitation or boundary crossing (`A.1` plus the direct relation owner), relation precision (`A.6.P` after a relation-bearing case is recovered), signature or slot claim (`A.6.0`, `A.6.5`), module-interface or interface-specification claim (`A.6.M`), functional port or functional element (`A.6.F`), physical component (`A.14`, `C.13`, `B.3.5`), boundary description or publication (`C.30.AD`, `E.17`), agency-threshold claim (`A.13`, `A.19`, `C.16`), or boundary-package statement classification (`A.6.B`) only when L, A, D, or E classification is the recovered object. | Do not create `U.MarkovBlanket`, generic `U.Boundary`, generic `U.Interface`, or binary `U.Agent`; do not treat a statistical separation, interface, interface module, physical component, description, and boundary-package classification as the same object. |
| functional port or functional structure | `A.6.F`, `A.3.4`, `E.18`, `C.30.TFS-REL` | Do not equate port, function, module interface, and signature by vocabulary alone. |
| API, protocol, connector, service-access wording | Recover the governed object first: `E.17` for API or interface-description publication; `A.6.0` and `A.6.5` for signature or relation-position claims; `A.6.M` for module-interface claims; `A.6.C` or `A.6.8` for agreement-like, protocol, SLA, service, or service-access cases; `A.6.B` only for L, A, D, or E statement classification inside a boundary package. | API may be description, protocol, service relation, signature, publication, module interface, or boundary-package statement classification. |
| capability | `A.2.2`; method, work, or gate patterns only when they name capability requirements | Role labels and interface labels do not create or demonstrate capability. |
| affordance or action invitation | `A.6.A` | Do not rename affordance as role, interface, or capability until the direct pattern admits it. |
| method, method description, work plan, or dated work | `A.3.1`, `A.3.2`, `A.15`, `A.15.1`, `A.15.2` | Method, description, plan, and work are distinct even when source wording says process. |
| function or functional wording | `A.6.F` | Function-like wording can point to several patterns; `A.6.F` governs that recovery. |
| concern, interest, viewpoint, problem, or characteristic-space selection | `A.7` for EntityOfConcern and description distinction; `C.22` or `C.22.2` for problem-card claims; `E.17.0` or `E.17.2` for viewpoint or view claims; `F.4` or `F.18` for role-description or naming cases; `A.19` or `E.21` for characteristic-space cases | Do not mint generic `U.Concern` or `U.Interest` by wording alone. |
| publication, description, declarative representation, source wording | `C.2.1`, `E.17`, `C.2.P.DR`, `E.10`, `E.10.ARCH` | Do not let description or publication use displace the EntityOfConcern selected by the project concern. |

#### A.6.RSIR:4.3 - Replacement candidate rule

Do not replace one umbrella with another. A repair candidate is admissible only when it names:

- the current object or claim kind;
- any relation or SlotKind that carries the claim;
- the governing pattern;
- the retained use of the source wording;
- the blocked overread.

If those cannot be named, leave the phrase in quote-only or reduced-use form and record the blocker.

#### A.6.RSIR:4.4 - Reduced-use source labels

Reduced-use labels are allowed. They are not failures. A source label remains reduced-use when it helps readers find or recognize the case but does not carry FPF-governed content.

Examples:

- "API role" can remain a quoted source phrase while the repair separately names software API description, provider role assignment, service promise relation, or interface specification.
- "parameter" can remain ordinary prose while SlotKind, ValueKind, and RefKind are named only when a relation or signature claim depends on them.
- "function" can remain ordinary engineering language when no architecture, capability, method, work, mathematical, quality, or module claim depends on it.

#### A.6.RSIR:4.5 - Shortcut Cost and Reopen Condition

`A.6.RSIR` is a deliberately weak first-level repair note. The baseline is full use of the direct governing pattern: `A.6.P` for relation repair, `A.6.5` for slot discipline, `A.2` and `A.2.1` for role and role assignment, `A.6.M` for module-interface, `A.6.F` for function-like repair, or the evidence, status, publication, architecture, method, work, gate, or problem pattern named by value.

The saved effort is that a practitioner does not run several full patterns before knowing which one is current. The loss budget is narrow: RSIR may select a governing pattern, preserve a reduced-use source label, or record a blocker. It may not decide the role assignment, signature, evidence-use relation, status assertion, service relation, architecture description, or method relation that belongs to the selected pattern.

Reopen RSIR when the selected pattern shows that the source phrase carried more than one governed object, the object kind was selected too early, a slot requirement was missed, or evidence, status, publication, gate, method, work, architecture, capability, or concern claims were folded into one label. The reopened repair splits the phrase into multiple governed values or keeps the excess wording reduced-use.

