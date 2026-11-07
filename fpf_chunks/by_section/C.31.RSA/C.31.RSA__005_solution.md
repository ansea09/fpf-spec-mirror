---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__005_solution.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:4 — Solution"
line_start: 75522
line_end: 75658
dependencies:
  - "A.10"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "G.5"
  - "G.6"
keywords:
  - "accounting basis"
  - "bespoke residue"
  - "refactoring opportunity"
  - "report-only share"
  - "reusable share"
  - "reusable-structure accounting"
  - "source return"
---

### C.31.RSA:4 - Solution

C.31.RSA governs reusable-structure accounting over declared structures and structural aspects. Use an adequate existing account directly. When reuse and residue have not yet been distinguished, recover them from the available instances below. The triage and accounting forms can retain the answer; a quantitative account still needs its declared basis.

#### C.31.RSA:4.0 - Recover reuse and residue from instances

Begin with the result for which reuse matters: for example, delivering another product variant, repeating a review, or applying an evidence package to another case. Select the instances that can answer that question, including a differing or failed instance when it can expose the limit of the apparent common rule. A known template-instance count can be reported directly; this construction is for an unresolved reuse claim.

1. **Follow the same required result through the instances.** Use the available products, configurations, instructions, test and approval material, or actual work records to recover what supplies that result, what it receives, and the conditions of each connection. C.30.ASV helps recover the selected structure; C.32.MWA.PP:4.1 and :4.4 help trace performance and provision when those relations matter. Compare the relation or way of doing.
2. **Explain the differences that matter.** For each consequential difference, find the requirement, input, environmental condition or arrangement that it responds to. Inspect a contrasting instance and the relevant instruction or requirement; ask its provider what would fail if the difference were removed. If that answer is unknown, name the document, participant, observation or justified bounded replay that could distinguish the possibilities. Keep the dependent part unresolved while using the supported common parts.
3. **State the reusable rule and its permitted variation.** Identify what can remain the same, which values or steps change, and under which conditions the resulting instance still supplies the required result. A necessary customer-specific approval or local adaptation may remain bespoke. A repeated workaround may instead expose a missing parameter, interface condition or Method step. Actual substitution, evidence validity and assurance claims retain their subject rules; resemblance between instances does not establish those claims.
4. **Choose the next sufficient result.** The common rule, its reusable locus, necessary exceptions and any unresolved dependency may finish a qualitative account. If a repair is needed, use :4.5 to consider where to place the common structure, then follow the affected instance through to its receiving result to check the change and any new burden. A proposed refactoring is a C.32 candidate; the account can also support retaining the present arrangement.
5. **Count only when the question needs a share.** Select the population, unit and reuse test from that question, then apply :4.1–:4.4. A count of template uses, a claim of valid evidence reuse and a claim that whole deliveries can share a Method answer different questions. Preserve the conditions and uncertainty of the one actually counted.

#### C.31.RSA:4.1 - Typed accounting description

```text
ReusableStructureAccountingDescription@Context:
  accountingBasisRef:
  structureRefs: FinSet(SelectedStructureReference)
  structuralAspectRefs: FinSet(StructuralAspectDescriptionRef)
  reusableStructureSlots:
  bespokeResidueSlots:
  hiddenOrResidualUncertaintySlots:
  slotBasisRefs?:
  admissibleAggregationRuleRef?:
  reportOnlyShares?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse?:
```

`accountingBasisRef` identifies the accounting rule. The rule may concern description length, dependency edges, work items, evidence package count, cost share, template instances, interface variants, regulatory case sections, or another declared basis. The accounting rule is not implied by the word "reuse".

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

These labels are local slots, not FPF ontology. `H_residual` is residual uncertainty or unmodelled variance under the accounting basis. Its value is not automatically commensurable with counts or other measures of interface grammars, work templates, evidence packages, or regulatory arguments.

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

Every numeric share needs its accounting rule, counted population and scale or unitless-value interpretation, with a unit when relevant. A comparison or ranking additionally needs aligned bases, preference direction when relevant, and its applicable comparator, such as `CG-Spec`, `ComparatorSetRef` or a governing comparator reference. A gate or decision needs that comparator only if its rule relies on such a comparison; it retains its own other requirements. A share with an established counting basis can remain a bounded local report when stronger reliance lacks grounds.

#### C.31.RSA:4.4 - Pseudo-sum boundary

An explanatory decomposition may be useful:

```text
total-described-structure under accountingBasisRef:
  reusable slots
  bespoke residue slots
  hidden or residual uncertainty slots
```

This is a readable decomposition of one declared accounting description, not an equation defining an architecture amount. If the slots do not share a declared accounting basis and comparability rule, they cannot be summed or ranked.

#### C.31.RSA:4.5 - Structure-relocation actions

RSA is useful because it points to relocation and repair actions:

| Situation | Repair direction |
| --- | --- |
| Repeated delivery work contains structure that is not explicit in the work or method description being used. | Move repeated structure into `MethodDescription`, work structure, or reusable work relation. |
| Repeated interface exceptions are handled one by one. | Add or revise interface grammar, variability slots, or substitution policy; use A.6.M when this is a module-interface claim. |
| An undocumented dependency crosses module or view boundaries. | Expose the dependency, revise boundary, add correspondence, or add source-return condition. |
| Evidence is recreated for each instance. | Move repeatable evidence into an evidence package, assurance argument record, or validity-context note. |
| Regulatory or safety-case residue remains one-off. | Split reusable argument structure from context-specific exception; apply B.3 to the assurance claim, including a claim about safety-case support, and G.6 when a citable provenance path is needed. |
| Compression hides needed distinctions. | Recover the omitted distinctions or reduce compression. Use C.29 when choosing or transferring the mathematical representation, or relying on its result, leaves an unresolved question. |
| Bespoke residue protects necessary local variation. | Keep it as a bounded exception with its use conditions and any action-changing limit. |

A high reusable-structure share is not always good. The architecture question is where structure lives—for example, in reusable templates, interfaces, flows, control relations, work methods, evidence packages, or unique exception networks and hidden coupling—and what action follows.

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

An RSA move identifies the reusable and residual loci, the basis needed for its accounting claim, and the warranted repair or retention. Inspect the possible costs and losses above; state those supported by the case and any condition that could change admissibility. Preserve an unresolved consequence as a question rather than inventing a loss or return condition.

#### C.31.RSA:4.6 - Triage and accounting use boundary

A qualitative account can be sufficient when the practitioner needs to locate reuse, residue and the next warranted repair. Use the triage form if it helps retain that answer.

Develop the accounting rule and structure references when the question depends on a numeric share, comparison of aspects or distinctions hidden by summarization. The fuller description can organize that content. Preserve source-return conditions when they change use. Publication of an adequate account does not require a new form; assurance, scale preference and decisions need the additional grounds of their own claims.

#### C.31.RSA:4.7 - Reopen and lowering conditions

An RSA result retains its declared scope, structure edition and accounting basis, together with source-return and comparator conditions on which its use actually depends. Reopen the triage or lower the admissible use when any of the following changes:

- a hidden source distinction becomes action-relevant;
- the accounting basis changes or proves heterogeneous;
- the selected structure, structural aspect, interface grammar, evidence package, work method, or assurance argument changes edition;
- a comparator set, CG-Spec, or outside-RSA use is added after a report-only share was recorded;
- downstream reliance uses the RSA result for outside-RSA evidence, assurance, gate, causal-use, scale-preference, or decision work that the RSA note did not admit;
- evidence validity, assurance window, or source-return condition decays;
- recurrence changes a bounded exception's cost, conditions or justification;
- a reuse move improves one locus while worsening interface cost, variation loss, evidence decay, assurance work, source-return cost, or hidden bespoke residue.

Block the dependent comparison or ranking when its required comparator or aligned basis is missing; preserve a valid bounded report. For another gate or decision, recover the particular missing premise under its own rule. If the accounting basis is unknown, retain only the qualitative or source-only meaning actually supported. If reuse and residue cannot be distinguished at one locus, mark that part unresolved while preserving independently established parts.

