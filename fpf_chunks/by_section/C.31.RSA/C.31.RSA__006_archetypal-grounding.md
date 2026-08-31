---
chunk_kind: "child"
pattern_id: "C.31.RSA"
pattern_title: "Reusable Structure Accounting"
section_id: "C.31.RSA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31.RSA/C.31.RSA__006_archetypal-grounding.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "C.31.RSA — Reusable Structure Accounting"
  - "C.31.RSA:5 — Archetypal Grounding"
line_start: 62644
line_end: 62736
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

**Tell.** Reusable structure is not a substance. It is structure located in declared places under a declared accounting basis.

**Show.** In one architecture, reusable structure may be located in a template and interface grammar. In another, it may be located in a test package, regulatory argument, work method, or flow pattern. In a third, the reusable part may be small, but the bounded exception is exactly what preserves safety or local fit.

**Show.** A share can be useful as a local report. It becomes misleading when it hides which structure was counted, which structure was not counted, and when the reader must return to source records.

Holon and episteme: the structures being accounted over are selected architecture-relevant structures in context. The RSA description, slots, report-only shares, and source-return condition are accounting descriptions, slot-bearing records, report-only records, and source-return records about those structures.

#### C.31.RSA:5.1 - Worked case: reusable evidence package, bespoke delivery work

Situation:

```text
A regulated product line has reusable component templates and a reusable test package.
Each customer delivery still repeats approval work and bespoke integration exceptions.
```

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
residueRefactoredInto:
  workStructure + evidencePackage + interfaceSpecification
residueAcceptedAsBoundedException:
  customer-specific regulatory clause with declared non-admissible reuse
sourceReturnCondition:
  return to deployment evidence and regulatory exception record before assurance or gate use
relatedClaimPatternsIfClaimed:
  `A.10` and `G.6` for evidence validity; `B.3` for assurance reliance; `A.6.M` for interface grammar; `C.16` if comparison is being made
stopCondition:
  report-only accounting unless comparator admission, evidence validity, and assurance validity are declared
```

Admissible move: publish the local report-only RSA note and repair the recurring delivery approval work into reusable work structure and reusable evidence structure. Non-admissible move: claim that the reusable evidence package proves every deployment or that a high reusable share makes the architecture better.

#### C.31.RSA:5.2 - Anti-case: high share hides a bad architecture move

Situation:

```text
A team reports that 85 percent of its architecture is reusable because most screens use one shared template.
The template makes many local exceptions necessary for product teams and side-channel integrations.
```

This is not a successful RSA result. The accounting basis counts template instances but hides interface relation cost, lost variation, hidden bespoke work, and evidence decay. The repair is to mark the share as report-only, add the missing bespoke-residue slots, and apply A.6.M, C.31, or an characteristic pattern governing the claim to the interface relation cost before any comparison or decision use.

Lowering replay: the team tries to use the 85 percent share to rank this template architecture above another product-line variant and approve the template program. The use is lowered to local report-only accounting because the comparator set, accounting-basis alignment, interface-cost measure, source-return condition, and decision record are absent. Before comparison or decision use, A.6.M must repair the interface grammar, C.16 or A.19 must govern comparability and characteristic space, and C.11 must govern the local decision claim.

Stop condition: do not use the 85 percent share for outside-RSA ranking, gate, assurance, or decision. Reopen the RSA note when the interface grammar, exception register, or comparator set changes.

#### C.31.RSA:5.3 - Transfer case: neural-network block replacement

Situation:

```text
A model architecture replaces a repeated attention block with a hybrid SSM-attention block.
The benchmark improves, but cache placement, memory access, and ablation evidence change.
```

RSA can transfer from product-line architecture to neural-network architecture only after `C.30.STRAT` has treated `block`, `cache`, and related terms as source labels unless the reusable locus is already recovered. Then RSA names the declared structures and accounting basis:

- reusable structure may be located in recovered repeated-block topology, dataflow pattern, cache-placement rule, or evaluation harness;
- bespoke residue may be located in model-specific tuning, data distribution dependence, memory-layout exception, or ablation gap;
- benchmark gain is not reusable-structure accounting by itself;
- evidence claims apply `A.10` and `G.6`; causal claims apply `C.28`; mathematical-lens or compression claims apply `C.29`.

Admissible move: record which recovered structural locus was reused, what changed, what source distinctions must remain reachable, and which governing pattern governs benchmark, evidence, causal-use, or mathematical-lens claims. Non-admissible move: treat "block replacement improved the architecture" as RSA proof.

