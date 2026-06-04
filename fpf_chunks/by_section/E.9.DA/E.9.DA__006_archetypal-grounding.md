---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__006_archetypal-grounding.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:5 — Archetypal Grounding"
line_start: 57580
line_end: 57597
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
keywords:
---

### E.9.DA:5 - Archetypal Grounding

**Tell.** A `DRR` is not good enough because it has headings. It is good enough for drafting when a pattern author can rely on its selected answer, receiving-locus requirements, boundaries, source-use role and status, architecture choice, and examples without inventing a missing decision.

**Show, weak DRR.** A `DRR` about precision restoration says that `E.10`, `A.6.P`, and `C.2.P` are relevant, and notes that architecture terms may need repair. It does not decide whether there is a new architecture-structure branch, what name it has, which existing patterns lose repeated repair prose, or which regression cases test the split. `E.9.DA` returns `repairBeforeDrafting` because `SelectedAnswerDecisiveness`, `ReceivingLocusObligationClosure`, and `DraftingActionability` are below the floor.

**Show, adequate DRR.** The same `DRR` selects `C.30.P - Architecture-Structure Precision Restoration`, assigns `E.10` the shared recovery sequence, assigns branch ontology to `A.6.P`, `C.2.P`, `C.30.P`, and `C.16.P`, states which evaluation patterns are slimmed, rejects a separate `LanguagePrecisionRestoration` pattern, and gives regression cases. `E.9.DA` can return `admissibleForDeclaredAuthoringUse` for pattern-host drafting.

**Show, system-facing and episteme-facing paired grounding.** A system-facing `DRR` says that an architecture diagram, graph, or ADR-like note will guide a structure amendment. `E.9.DA` requires the `DRR` to state the architecture claim or structure claim, described or grounding object when live, structural view relation, preserved and lost structure, selected receiving loci, non-use boundary, and first drafting move. An episteme-facing `DRR` says that a source, seminar, review, standard, or SoTA article will shape a pattern. `E.9.DA` requires source-use role, source-currentness status, selected payload, rejected payload, non-use boundary, and receiving-locus disposition. In both cases, the description or source locates material; it is not itself the FPF decision.

**Show, SoTA-heavy DRR.** A `DRR` for a quantum-like modeling lens carries literature, seminar material, reviewer findings, and FPF neighbour decisions. It is not adequate merely because the sources are numerous. It becomes adequate when the selected answer states which mathematical-lens claims enter the new pattern, which claims remain non-use, which terms require `E.10`, `A.6.P`, or `C.2.P` repair, which evaluation patterns get concrete SoTA, examples, and conformance obligations, and why the selected pattern split is the right FPF content architecture. `SoTAAndEvidenceUseInDecision`, `SourceUseAndDecisionInheritanceCarryThrough`, `ReceivingLocusObligationClosure`, and `FPFContentArchitectureSelectionAdequacy` are active.

**Show, causal DRR.** A `DRR` for counterfactual realizability and causal use touches a new causal pattern plus evidence, assurance, benchmark, dispatch, and fairness neighbours. It is adequate only if it decides the causal-use vocabulary, the selected FPF content architecture, the receiving-locus obligations, the non-admissible overreads, and the exact status sets and value sets that downstream hosts may use. A clean external review of a smaller host subset does not by itself make the wider `DRR` adequate for a wider declared authoring use.

**Show, architecture-impact DRR.** A `DRR` for architecture precision restoration touches architecture and structure language, structural views, graphs, diagrams, dashboards, publication faces, and source plans. `FPFContentArchitectureSelectionAdequacy` and `ArchitectureSourceAndViewLossClosure` are active because the `DRR` must distinguish the architecture or structure claim from its description, state which structure kinds and views are live, state what view losses are admissible, and block the overread that a graph, diagram, dashboard, or ADR-like note is the architecture itself.

**Near-miss, small edit.** A `DRR` fixes one typo or one local Plain-register sentence with no semantic change and no downstream drafting obligation. `E.9.DA` should not force a full read. The admissible result is to use `E.9` lightweight form, run `E.10` on the changed wording when load-bearing wording is live, and avoid minting `DRRDecisionAdequacyRead`.

