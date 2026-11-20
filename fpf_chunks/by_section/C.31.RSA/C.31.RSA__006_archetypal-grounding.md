---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__006_archetypal-grounding.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:5 — Archetypal Grounding"
line_start: 79342
line_end: 79450
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

### C.31.RSA:5 - Archetypal Grounding

Account for structure at declared loci under a declared accounting basis.

In one architecture, reusable structure may be located in a template and interface grammar. In another, it may be located in a test package, regulatory argument, work method, or flow pattern. In a third, the reusable part may be small, but the bounded exception is what preserves safety or local fit.

A share can be useful as a local report. It becomes misleading when it hides which structure was counted, which structure was not counted, and when the reader must return to source records.

Holon and episteme: the structures being accounted over are selected architecture-relevant structures in context. The RSA description describes those structures; it records the local accounting slots, report-only share values, and any source-return condition.

#### C.31.RSA:5.1 - Worked case: reusable evidence package, bespoke delivery work

Situation:

```text
A regulated product line has reusable component templates and a reusable test package.
Each customer delivery still repeats approval work and bespoke integration exceptions.
```

Start with the delivery instructions, completed approval material and integration exceptions. The ordinary variants use the same component interfaces and test procedure within the package's stated operating envelope. One customer's approval adds an on-site witness required by its contract; another delivery repeats an adapter workaround because its input format falls outside the shared interface grammar.

Comparing those cases with their requirements separates three contributions:

- a reusable test procedure within its conditions;
- a necessary customer-specific witness; and
- an unresolved design choice about accommodating the input format.

Where the record does not explain a difference, recover that condition from the provider or governing requirement before deciding whether to remove it.

The next account can therefore retain the common test and approval preparation, preserve the contractual witness, and propose an interface or adapter change for the recurring format exception. Replaying that proposed change through input, integration and test shows whether it preserves the required result and whether it merely relocates work.

For the next delivery, the contract requires an on-site witness. A prior test may cover the unchanged component, while the witness clause still calls for work at this site. If the new adapter changes a signal used in the component test, inspect the qualification boundary. Evidence covering that adapter and signal can be used directly. Otherwise qualify the affected path or choose an already covered configuration. The purchase or acceptance decision can use these findings under its own rule.

`ReusableStructureTriage`:

```text
describedHolonRef: product-line delivery system
reuseQuestion: which selected structures are reused and where does bespoke residue grow?
deploymentBoundary: regulated customer deployments
intendedAccountingUse: decide the next reusable-structure repair
claimScopeRef: reusable-structure accounting for regulated delivery
qualificationWindowRef: 2026Q3 regulated-delivery review window
architectureClaimRef: C.30 architecture claim for the product-line delivery system and its selected delivery structures
structureRefs:
  component template structure
  interface grammar structure
  evidence package structure
  delivery work structure
accountingRelationRefs:
  reuse, exception, and bespoke-residue relations for the named deployments
evidenceRefs:
  deployment, approval, integration-exception, and reusable-test-package records
whereReusableStructureCurrentlyLives:
  component template structure
  reusable test package
  interface grammar for standard variants
whereBespokeResidueCurrentlyGrows:
  customer-specific approval work
  integration exceptions outside interface grammar
  local evidence witnesses not covered by reusable package
residueAcceptedAsBoundedException:
  on-site witness required by this customer’s contract
sourceReturnCondition:
  return to deployment evidence and regulatory exception record before assurance or gate use
relatedClaimPatternsIfClaimed:
  direct evidence-validity rule and its required source-to-use grounds; `A.10` when a replayable evidence account is needed; `G.6` for a needed citable provenance path; `B.3` for assurance reliance; `A.6.M` for an unresolved module-interface claim; `C.16` for measurement; `A.19.CPM` for a selected profile comparison
stopCondition:
  report-only accounting; establish comparison, evidence-validity or assurance grounds when that further use is made
```

Publish the account of shared and local work. The interface change is available for design and testing. Once it is implemented, use the affected deliveries to establish where the adapter work now occurs and what its cost is.

#### C.31.RSA:5.2 - Anti-case: high share hides a bad architecture move

Situation:

```text
A product line released 20 screens. Build records trace 17 to a shared template. Two were built from independent designs without the template and meet the same visual specification. The origin of the last screen is unknown.
Teams report local work on input and integration exceptions.
```

For an agreement requiring at least 85 percent of the released screens to use the template, the 17 traced uses suffice. Between 17 and 18 screens used it. An exact percentage, or a decision at a 90 percent threshold, depends on the origin of the remaining screen. Comparing screen appearance could establish conformity with a visual specification. It cannot recover that missing build history.

The same account leaves open whether to fund the template for the next release. Compare the cost of maintaining and adapting it with the cost of developing and maintaining the independent designs for the planned assortment. Include the local work on both alternatives. A common template can save production work while moving more work into integration.

Compare applicable offers, engineering estimates or work records for the planned assortment, including interface maintenance and local adaptations. Use observed costs when reporting work already done. An offer covering the full intended service can settle its quoted price while actual future expenditure is still open. Use A.6.M for a disputed interface interpretation, C.16 for a cost measure and C.11 for the local funding decision.

These grounds can support comparison of the existing variants before any interface is changed. A chosen repair changes the candidate and reopens the affected accounting and comparison.

Keep the release count when the next release changes the planned assortment or the cost comparison. Reopen only the answer that depends on the changed facts.

#### C.31.RSA:5.3 - Transfer case: neural-network block replacement

Situation:

```text
A model architecture replaces a repeated attention block with a hybrid SSM-attention block.
The benchmark improves, but cache placement, memory access, and ablation evidence change.
```

To transfer RSA from product-line architecture to neural-network architecture, use the already recovered reusable locus or first apply `C.30.STRAT` to treat `block`, `cache`, and related terms as source labels. Then RSA names the declared structures and accounting basis:

- trace which earlier topology, dataflow, cache rule or evaluation harness the team used. To credit a new design, establish which choice the team made beyond implementing the supplied architecture;
- check the target's memory layout, input distribution and tuning needs before offering the same change for another model;
- benchmark gain is not reusable-structure accounting by itself;
- establish evidence and causal claims under their direct rules; use `A.10` for a needed replayable source-to-use account, `G.6` for a needed citable provenance path, and `C.28` for causal-use recovery. Use `C.29` for an unresolved mathematical representation choice, transfer or reliance question.

Admissible move: record which recovered structural locus was reused, what changed, what source distinctions must remain reachable, and which pattern defines or tests each benchmark, evidence, causal-use, or mathematical-lens claim. Non-admissible move: treat "block replacement improved the architecture" as RSA proof.

