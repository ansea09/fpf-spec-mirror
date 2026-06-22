---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__005_solution.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:4 — Solution"
line_start: 57962
line_end: 58099
dependencies:
keywords:
---

### C.31.RSA:4 - Solution

C.31.RSA governs reusable-structure accounting as a typed description over declared structures and structural aspects. It starts with `ReusableStructureTriage`; it uses `ReusableStructureAccountingDescription@Context` only when the accounting basis is declared.

#### C.31.RSA:4.1 - Typed accounting description

```text
ReusableStructureAccountingDescription@Context:
  accountingBasisRef:
  structureRefs: FinSet(U.StructureRef)
  structuralAspectRefs: FinSet(StructuralAspectDescriptionRef)
  reusableStructureSlots:
  bespokeResidueSlots:
  hiddenOrResidualUncertaintySlots:
  slotBasisRefs?:
  admissibleAggregationRuleRef?:
  reportOnlyShares?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse:
```

`accountingBasisRef` states the accounting rule being used: description length, dependency edges, work items, evidence package count, cost share, template instances, interface variants, regulatory case sections, or another declared accounting rule. The accounting rule is not implied by the word "reuse".

Well-formedness: every slot is over declared `structureRefs`, declared `structuralAspectRefs`, and one declared accounting basis. Slot labels are explanatory; they are not root kinds and are not automatically commensurable.

#### C.31.RSA:4.2 - Explanatory slot labels

A local accounting description may use explanatory slot labels such as:

```text
S_function
S_flow
S_control
S_type
S_interface
S_scale
S_work
S_evidence
S_changePolicy
S_unique
S_crossScopeUnique
H_residual
```

These labels are local slots, not FPF ontology. `H_residual` is residual uncertainty or unmodelled variance under the accounting basis. It is not obviously the same unit as interface grammar, work template, evidence package, or regulatory argument.

#### C.31.RSA:4.3 - Report-only shares

```text
ReusableStructureShare:
  report-only share over declared structureRefs and structuralAspectRefs
  under accountingBasisRef; not an architecture amount

BespokeResidueShare:
  report-only share under accountingBasisRef

HiddenOrResidualShare:
  report-only uncertainty or residue interpretation under accountingBasisRef
```

Numeric shares require a declared `accountingBasisRef`, declared scale or unitless-value rule, unit when relevant, polarity when relevant, admissible comparability relation, and comparator admission named by value such as `CG-Spec`, `ComparatorSetRef`, or a comparator-governing reference named by value before they can guide outside-RSA use such as comparison, ranking, selection, gate use, or decision use. Without that, the share remains local report-only guidance.

#### C.31.RSA:4.4 - Pseudo-sum boundary

An explanatory decomposition may be useful:

```text
total-described-structure under accountingBasisRef:
  reusable slots
  bespoke residue slots
  hidden or residual uncertainty slots
```

This is not `ReusableStructureEquation`, not an architecture amount, and not a hidden `StructureAmount` kind. It is a readable decomposition of one declared accounting description. If the slots do not share a declared accounting basis and comparability rule, they cannot be summed or ranked.

#### C.31.RSA:4.5 - Structure-relocation actions

RSA is useful because it points to relocation and repair actions:

| Situation | Repair direction |
| --- | --- |
| Repeated delivery work contains structure that is not explicit in the work or method description being used. | Move repeated structure into `MethodDescription`, work structure, or reusable work relation. |
| Repeated interface exceptions are handled one by one. | Add or revise interface grammar, variability slots, or substitution policy under A.6.M. |
| An undocumented dependency crosses module or view boundaries. | Expose the dependency, revise boundary, add correspondence, or add source-return condition. |
| Evidence is recreated for each instance. | Move repeatable evidence into an evidence package, assurance argument record, or validity-context note. |
| Regulatory or safety-case residue remains one-off. | Split reusable argument structure from context-specific exception; apply B.3 or G.6 for assurance or safety-case reliance. |
| Compression hides needed distinctions. | Reduce compression, add source-return condition, or apply C.29 for lens-governed compression or reduction claims. |
| Bespoke residue protects necessary local variation. | Keep it as a bounded exception with admissible use and non-admissible use. |

High reusable structure is not always good. The architecture question is where structure lives and what action follows: reusable templates, interfaces, flows, control relations, work methods, evidence packages, or unique exception networks and hidden coupling.

After a relocation or reuse move, ask what got worse:

| Reuse move may improve | Check what may worsen |
| --- | --- |
| Template reuse | Loss of needed variation, hidden local exception, or stale source-return condition. |
| Interface grammar | Interface relation cost, conformance work, change cost, migration cost, or substitution constraint. |
| Work-method reuse | Context mismatch, extra handoff cost, slower local response, or hidden work exception. |
| Evidence-package reuse | Evidence decay, validity-window mismatch, missing context witness, or assurance overread. |
| Assurance-argument reuse | Weakest-link dependency, certification-window mismatch, or unexamined regulatory exception. |
| Compression or lens-backed accounting | Lost source distinction, observer-budget dependency, or C.29 stop-condition breach. |
| Bespoke-residue reduction | Reduced resilience, local-fit loss, or new hidden coupling. |

The result is not "more reuse is better." A conforming RSA move states the reusable locus, the bespoke or residual locus, the accounting basis, the first repair direction, and the first cost, loss, or source-return condition that can make the move inadmissible.

#### C.31.RSA:4.6 - Triage and accounting use boundary

Use only `ReusableStructureTriage` when:

- there is one local case;
- no outside-RSA use is being made;
- the practitioner only needs a repair direction;
- no numeric share is being relied on.

Use `ReusableStructureAccountingDescription@Context` when:

- the accounting basis is declared;
- a report-only share is useful;
- structure refs or structural aspects need to be compared inside one declared `accountingBasisRef`;
- source-return conditions matter;
- reusable structure or bespoke residue is used for outside-RSA use such as cross-case report, publication, assurance, architecture scale preference, or decision.

#### C.31.RSA:4.7 - Reopen and lowering conditions

An RSA result remains valid only inside its declared accounting basis, structure edition, source-return condition, and comparator admission. Reopen the triage or lower the admissible use when any of the following changes:

- a hidden source distinction becomes action-relevant;
- the accounting basis changes or proves heterogeneous;
- the selected structure, structural aspect, interface grammar, evidence package, work method, or assurance argument changes edition;
- a comparator set, CG-Spec, or outside-RSA use is added after a report-only share was recorded;
- downstream reliance uses the RSA result for outside-RSA evidence, assurance, gate, causal-use, scale-preference, or decision work that the RSA note did not admit;
- evidence validity, assurance window, or source-return condition decays;
- a local bounded exception becomes repeated enough to require refactoring;
- a reuse move improves one locus while worsening interface cost, variation loss, evidence decay, assurance work, source-return cost, or hidden bespoke residue.

Lower the result to report-only when outside-RSA comparison, ranking, selection, gate use, or decision use lacks comparator admission named by value. Lower it to quote-only or source cue when the accounting basis cannot be recovered. Mark it blocked when the reusable locus and bespoke-residue locus cannot be separated.

