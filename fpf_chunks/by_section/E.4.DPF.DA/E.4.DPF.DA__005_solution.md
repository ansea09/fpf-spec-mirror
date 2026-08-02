---
chunk_kind: "child"
pattern_id: "E.4.DPF.DA"
pattern_title: "Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
section_id: "E.4.DPF.DA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.DPF.DA/E.4.DPF.DA__005_solution.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "E.4.DPF.DA — Domain Principle Framework Package-Adequacy Evaluation CharacteristicSpace"
  - "E.4.DPF.DA:4 — Solution"
line_start: 70610
line_end: 70733
dependencies:
  - "A.19.ECS"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.DPF.DA:4 - Solution

Evaluate one DPF package edition for one declared use through a DPF-specific adequacy characteristic space. The evaluation is derived from the shape of `E.2.DA`, but it is not the FPF Pillar evaluation. It asks whether the package realizes FPF-grounded domain value for a declared domain or local context.

```text
DPFPackageAdequacyEvaluation@Context:
  evaluatedPackageRef:
  packageKind: domain-principle-framework | local-practice-framework | seed | selected-host-set | all-in-one-publication-carrier | skill-pack | mcp-backed-access-service | mixed
  declaredDomainOrLocalContext:
  intendedReaderOrOperator:
  declaredUse:
  nonUseBoundary:
  fpfCoreEditionRef:
  dependencyAndEditionRefs:
  sourceBasisRefs:
  pfadDecisionRefs:
  patternSetRefs:
  relationRecordRefs:
  publicationCarrierRefs:
  accessCarrierRefs:
  qualityEvidenceRefs:
  refreshRefs:
  evaluationEvidenceBasis:
  coordinateTable:
  protectedTradeoffSet:
  status:
  firstRepairOrNoProposalDisposition:
  reopenCondition:
```

#### E.4.DPF.DA:4.1 - Ordinal scale

| Value | Label | Meaning |
| --- | --- | --- |
| `0` | `wrongKindOrNoBasis` | The object is not an evaluable DPF package for the declared use, or required basis is absent. |
| `1` | `namedOnly` | The package name or topic exists, but the package cannot guide domain or local work. |
| `2` | `partialSeed` | Useful source, prompt, or pattern-seed material exists, but package obligations are incomplete or fragile. |
| `3` | `locallyUsableWithVisibleLimits` | The package can support bounded exploration or local use with explicit limits and repairs. |
| `4` | `wellGroundedForDeclaredDPFUse` | The package is coherent, source-grounded, FPF-dependent, navigable, and refreshable for the declared use. |
| `5` | `exceptionallyGroundedForDeclaredDPFUse` | The package is replayable across source basis, pattern set, relation records, heterogeneous cases, publication carriers, improvement route, refresh route, and blocked overreads. |

Default floor is `4` for public, teaching, enterprise, operational, or reliance-bearing DPF use. A fast seed or exploratory prompt output may use floor `3` only when non-use, missing evidence, and next repair are explicit.

#### E.4.DPF.DA:4.2 - Required coordinates

Every `E.4.DPF.DA` run evaluates every coordinate below. Do not drop a coordinate because the package is "only a seed"; assign the value that the seed earns.

In this pattern, `known failure modes` means beginner mistakes and experienced-practitioner failures caused by stale, local-only, or non-SoTA practice. Do not narrow the check to novice errors only.

| Coordinate | Evaluation question | Good state |
| --- | --- | --- |
| `D1DomainScopeAndUseAdequacy` | Is the domain or local context, reader, declared use, and non-use boundary recoverable? | The package tells whom it is for, what domain situation it covers, what it does first, and what it must not be used for. |
| `D2DidacticEntryAndAdoptionAdequacy` | Can the intended reader or assisting agent find the first useful entry and get a first working result without FPF developer knowledge? | ToC, readme, preface, pattern-use routes, skill entries, MCP access cues, and examples make adoption cheap and non-magical, while support maps are reached from work triggers rather than front-loaded as required reading. |
| `D3ScalableFormalityAndAssurancePathAdequacy` | Can the package move from plain local use toward stronger records, evaluation, evidence, or assurance without rewriting the package? | Plain guidance, typed records, source pins, evaluation rows, and stronger owners are staged. |
| `D4CoreDependencyAndDomainBoundaryAdequacy` | Does the package depend on FPF Core while keeping domain knowledge inside the DPF? | Core owners are reused; local terms do not redefine Core; possible Core amendment candidates are explicit; FPF Core and the main monolith do not depend on this DPF except through a deliberate Core amendment. |
| `D5PackageFormLayeringAndRelationAdequacy` | Are pattern set, support maps or appendices, relation records, edition dependencies, publication carriers, access carriers, source packs, and quality records separated? | `E.4.PFR`, `E.4.PFAD`, source, publication, access, quality, support-map, appendix, and refresh loci remain distinct, findable, and reached from the right work triggers. |
| `D6DomainLexiconAndKindSettlementAdequacy` | Are domain terms, local vocabulary, candidate ontics, and FPF owners settled well enough for use? | Local terms have kind, owner, admissible use, blocked overread, and naming route when needed. |
| `D7PracticeUtilityAndProblemResolutionAdequacy` | Does the package change real domain or local action, diagnosis, design, explanation, teaching, or repair? | Patterns solve recognizable domain problems with positive SoTA-informed moves, known failure modes or anti-patterns, and worked cases, not only taxonomy, ontology, commentary, or talk guidance. |
| `D8HeterogeneousCaseAndTransferAdequacy` | Has the package been tested against diverse enough domain cases, reader roles, or local situations? | Heterogeneous probes show where the same pattern set works, fails, or needs a neighbouring owner. |
| `D9EditionStateAndCurrentnessAdequacy` | Are package edition, source currentness, dependency pins, qualification window, and status of carriers explicit? | Readers can tell what version they use, what source state supports it, and what changes it. |
| `D10ImprovementAndRefreshAdequacy` | Can the package improve through `E.22`/`E.23` and refresh through `G.11` without giant reopen or process theatre? | Low values produce repair rows; source, edition, telemetry, and use failures have smallest reopen routes. |
| `D11DomainSoTAAlignmentAdequacy` | Does current domain or local SoTA discipline pattern selection, solution, examples, boundaries, and reopen triggers? | Sources change the package content; they are not bibliography, claim theatre, or authority by citation. |

#### E.4.DPF.DA:4.3 - Result row shape

An `E.4.DPF.DA` result uses this table shape:

| Coordinate | Value | ShortRationale | EvidenceLocus | RepairOrNoProposal |
| --- | --- | --- | --- | --- |
| `<D1..D11>` | `<0..5>` | `<why this value, why lower would understate evidence, why higher would overstate it or what would lower or reopen a 5>` | `<package section, source row, relation record, pattern body, readme, ToC, skill entry, MCP route, worked case, quality result, refresh route, missing locus>` | `<repair, no-proposal with checked loci, or owning neighbour>` |

A prose verdict, a checklist-count result, a table without evidence loci, or an average of `E.21` pattern values is not an `E.4.DPF.DA` result.

#### E.4.DPF.DA:4.3a - DPF-wide package-form checks

Run this subpass for any all-in-one DPF publication carrier, selected-host-set, card set, skill pack, MCP-backed access service, or package publication or access carrier. These checks do not replace the eleven coordinates; they supply package-level evidence mainly for `D1`, `D2`, `D4`, `D5`, `D7`, `D8`, `D9`, `D10`, and `D11`.

| Package-form check | Passing condition | Primary affected coordinates |
| --- | --- | --- |
| `PFM1 Front-door order` | The package front door has a usable ToC, readme, and preface or equivalent first-entry carrier before pattern bodies; the reader can choose a first pattern without reading support apparatus first. | `D2`, `D5` |
| `PFM2 Pattern-language primacy` | Pattern bodies remain the main language of use. Large maps, source-use tables, relation records, edition notes, and package architecture material appear after pattern bodies or in appendices or support sections unless they are a short first-entry aid. | `D2`, `D5`, `D7` |
| `PFM3 Map discoverability` | Every support map or appendix has at least one live entry route from ToC or readme, a pattern `Relations` section, low-value repair action, source-return condition, or package-refresh condition. A map that cannot be reached from work lowers package adequacy even if the map is correct. | `D2`, `D5`, `D10` |
| `PFM4 Dependency direction` | The DPF may cite FPF Core and explicitly depended-on upstream DPFs or local frameworks; FPF Core and the main monolith do not cite this DPF as required authority. If a DPF discovery belongs in Core, it returns through a Core amendment decision rather than a reverse dependency. | `D4`, `D5`, `D9` |
| `PFM5 Publication-and-access-carrier boundary` | The all-in-one carrier, readme, preface, ToC, card set, maps, skill pack, MCP-backed access route, retrieval route, and assistant integration are publication or access carriers. They do not become the framework architecture, source pack, quality result, admission status, process state, runtime dependency, work authority, evidence source, or currentness proof by being visible or callable. | `D5`, `D9` |
| `PFM6 Public package naming` | The public title and primary file or package name use a domain- or practice-specific framework name such as `<DomainOrPractice> Principles Framework`, with the domain or practice head visible. `Principles Framework` alone is only a kind or head phrase, not an individual framework name. Format slang such as `local monolith`, process state such as `draft`, and file-layout labels stay out of public package identity unless the carrier is explicitly a workspace-only artifact. | `D1`, `D2`, `D5`, `D6`, `D9` |
| `PFM7 Development-state absence` | Package carriers contain user-facing package content and durable package relations, not scattered `draft`, `DRR`, handoff, ledger, review-status, admission-blocker, helper-state, or process-run residue. | `D5`, `D9`, `D10` |
| `PFM8 Cross-DPF relation discipline` | References to another DPF or local framework are recorded as dependency, specialization, source reuse, publication, selected-set, or other `E.4.PFR` relation with blocked stronger reading and refresh condition. | `D4`, `D5`, `D9` |
| `PFM9 Normal-pattern maturity` | Every pattern body claimed as part of a public, teaching, enterprise, or reliance-bearing DPF is a normal action-guiding FPF-style pattern for its declared use: it is drafted through `E.8`, evaluated through `E.21`, and not merely a heading skeleton, seed note, prompt output, compressed DRR recap, term sheet, ontology catalog, or commentary about the domain. The pattern should show the typical problem, known failure mode or anti-pattern, SoTA-informed solution move, worked case, and boundary. Seeds are allowed only when the package status says `seedOnly` or the affected pattern is explicitly non-reliance-bearing. | `D2`, `D7`, `D8`, `D11` |
| `PFM10 Access-currentness and callable-use boundary` | Skill packs and MCP-backed access services expose framework edition, dependency, source and currentness, bounded use, and refresh route. Generated outputs route to `C.35`; tool and work actions route to `A.15` or the local work owner; evidence, assurance, decision, and currentness claims route to their direct owners. | `D2`, `D5`, `D9`, `D10` |
| `PFM11 Carrier structure-account and controlled structural coarsening` | Readme, Preface, or equivalent first-entry carrier provides a structure-account: what the package exposes for whom, which domain or local structures and source denominator it foregrounds, what it deliberately coarsens, abstracts, omits, loses, or sends to appendices and sources, and how a reader returns to pattern bodies, source packs, evidence owners, or relation records. This is source-structure-to-publication/access accounting, not only text summarization. The carrier is not itself the framework edition, the domain, or a narrative by type. In architecture-mediated narrative-rendering cases, the return chain is `narrative rendering carried by a publication or access carrier -> architecture description or view -> architecture as selected structures in context -> wider source structures`; when no narrative rendering is present, the first step is `framework publication or access carrier -> selected source structures`. Every arrow has its own selection, coarsening, abstraction, omission, preservation, and loss account. If package-level structure-capture or epiplexity is claimed, its declared use and lowering reason are explicit. | `D1`, `D2`, `D5`, `D7`, `D8`, `D10`, `D11` |

A failure in this subpass lowers the affected coordinate even when individual pattern bodies pass `E.21`. Repair the package carrier, relation record, first-entry route, dependency record, or support-map placement; do not copy the package-form proof into pattern bodies.

#### E.4.DPF.DA:4.4 - Evidence basis and neighbouring owners

Use these owners instead of expanding this pattern into a package bureaucracy:

| Evidence or defect | Owner |
| --- | --- |
| Source payload, rejected alternatives, source currentness, and source-use boundary | `G.2`, `G.11` |
| Framework architecture decision, selected pattern set, publication carrier, dependency boundary | `E.4.PFAD`, `E.4`, `E.4.PFR` |
| Individual pattern quality | `E.21` |
| Pattern admission or profile gating | `E.19` |
| First-entry and publication carrier | `E.11`, `E.17` |
| Carrier structure-account, captured/coarsened/lost structure, package-level source return, and structure-capture or epiplexity account | `E.4.DPF`, `E.11`, `E.17`, `A.6.3.CSC`, `C.33`, `C.34`, and `A.6.3.NAR` when sequential narrative rendering is load-bearing |
| Naming and local vocabulary | `E.10`, `F.18`, direct governing pattern |
| Generated or searched package candidate | `C.35`, then `E.4.PFAD` or direct owner |
| Carrier capture, loss, and preservation | `C.33`, `C.34` |
| Improvement framing and repeated improvement | `E.22`, `E.23` |
| FPF-level Pillar effect | `E.2.DA`, only when the package changes FPF-level adequacy |

When a coordinate is below floor, return a finding or repair proposal. When a coordinate is at `4` and improvement is requested, search for a substantive non-dominated improvement. Do not raise a value by adding proof apparatus, more maps, more citations, or quality-status prose unless the package becomes easier to use, more source-grounded, more accurately bounded, or more refreshable.

#### E.4.DPF.DA:4.5 - Status

| Status | Meaning |
| --- | --- |
| `admissibleForDeclaredDPFUse` | All coordinates meet the declared floor for the stated DPF use, with non-use and reopen conditions named. |
| `repairBeforeDPFUse` | One or more coordinates are below floor for the stated use. |
| `seedOnly` | The package is useful as a seed or prompt output but not for reliance-bearing use. |
| `holdForPFADDecision` | The package architecture, pattern set, dependency, or publication unit needs a framework architecture decision. |
| `holdForCoreAmendmentDecision` | A package claim may belong in FPF Core and must not be hidden inside a DPF. |
| `refreshNeeded` | The package was adequate before, but source, Core edition, local use, telemetry, or dependency state has changed. |

