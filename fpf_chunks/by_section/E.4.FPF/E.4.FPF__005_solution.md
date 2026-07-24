---
chunk_kind: "child"
pattern_id: "E.4.FPF"
pattern_title: "First Principles Framework Form and Publication-or-Access Carrier Assembly"
section_id: "E.4.FPF:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.FPF/E.4.FPF__005_solution.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "E.4.FPF — First Principles Framework Form and Publication-or-Access Carrier Assembly"
  - "E.4.FPF:4 — Solution"
line_start: 68574
line_end: 68632
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.9.DA"
  - "F.18"
  - "G.11"
  - "G.2"
  - "I.2"
keywords:
---

### E.4.FPF:4 - Solution

Treat FPF as a `FirstPrinciplesFrameworkEdition`: a transdisciplinary framework edition whose selected Core pattern set, first-principles scope, cross-domain problem-situation and solution-move architecture, relation records, and publication or access carriers are distinct but coordinated. FPF patterns render recurring first-principles problem architectures and reusable solution moves in pattern-language form; the carriers expose that rendering without becoming the framework edition itself.

Use these local names:

| Local name | Kind and use |
|---|---|
| `FirstPrinciplesFrameworkEdition` | One scoped FPF edition carrying transdisciplinary first-principles distinctions and the Core pattern set that downstream frameworks depend on. |
| `FPFCorePatternSet` | The selected governing pattern set for the edition. It is not the same kind as README, Preface, ToC, skill pack, or MCP route. |
| `FPFPublicationCarrier` | Reader-facing carrier such as `FPF-Spec.md`, README, Preface, ToC, extracted host set, reviewable bundle, card set, or split documentation that publishes selected FPF content. |
| `FPFAccessCarrier` | User-facing or agent-facing access carrier such as a skill pack, MCP-backed access service, retrieval route, assistant integration, or search or index carrier. It exposes FPF; it is not FPF architecture, source authority, quality proof, runtime dependency, or work permission by itself. |
| `FPFFormMap` | Context record naming edition, Core set, carriers, relation records, quality route, currentness route, and blocked overreads. |
| `FPFLevelAdequacyRoute` | Whole-FPF adequacy route through `E.2.DA`; individual pattern quality still uses `E.21`, and DRR quality still uses `E.9.DA`. |

Create the FPF form map with this shape when FPF itself is being assembled, republished, exposed, or evaluated:

```text
FPFFormMap@Context:
  firstPrinciplesFrameworkEditionRef: <FPF edition named by value>
  firstPrinciplesScopeRef: <transdisciplinary scope and non-domain boundary>
  selectedCorePatternSetRefs: <governing pattern set or selected host or monolith slice>
  selectedFirstPrinciplesProblemSituationRefs: <recurring cross-domain problem situations and forces rendered by the edition>
  selectedFirstPrinciplesSolutionMoveRefs: <reusable solution moves, consequences, and repair routes rendered by the edition>
  selectedPublicationCarrierRefs: <README | Preface | ToC | FPF-Spec | hosts | cards | bundle | split docs>
  selectedAccessCarrierRefs: <skill pack | MCP route | retrieval route | assistant integration | other access carrier>
  relationAndEditionRefs: <E.4.PFR records, edition pins, dependency boundaries>
  firstEntryAndProjectionRefs: <E.11, E.17, I.2, README, Preface, and ToC projection loci>
  publicationSelfRenderingRefs: <README | Preface | ToC statements of reader, selected first-principles structures, deliberate coarsening, abstraction, omission, deferral, and return to governing patterns>
  qualityAndImprovementRefs: <E.2.DA for FPF-level adequacy; E.21, E.23, and E.9.DA as evidence or local routes>
  currentnessAndRefreshRefs: <G.11 and source and currentness owners>
  blockedOverreadRefs: <carrier-as-framework | DPF-as-FPF | access-route-as-authority | local-quality-as-whole-FPF>
```

The ordinary method is:

1. Name the scoped FPF edition by value: current monolith edition, selected host set, release candidate, or whole-FPF edition.
2. State the first-principles scope: FPF supplies transdisciplinary distinctions that can be reused across domains, not a domain doctrine and not an encyclopedia of all domains.
3. Identify the selected Core pattern set and any companion or projection loci that expose it.
4. Separate publication carriers from access carriers. A README, Preface, ToC, monolith, host set, card deck, skill pack, MCP route, retrieval route, or assistant integration is a carrier, not the framework edition itself.
5. Record relation, dependency, edition, deprecation, supersession, publication, and access relations through `E.4.PFR`.
6. Keep downstream direction clear: DPFs and local practice frameworks may depend on FPF Core; FPF Core does not depend on them except by a deliberate Core amendment decision.
7. For whole-FPF adequacy, use `E.2.DA` over the scoped FPF object and declared use. Use `E.21` for individual pattern bodies, `E.9.DA` for DRR, and `E.4.DPF.DA` only for DPF or local-framework packages.
8. For first-entry and reader-facing exposure, use `E.11` and `E.17`; keep their projection text thin enough that governing pattern authority remains in the patterns.
9. Make the FPF readme, Preface, and ToC structure-account-aware: they should state the reader and use they serve, which first-principles structures they foreground, what they deliberately coarsen, abstract, omit, or defer, and where the reader returns for governing pattern detail. This protects adoption text from becoming a second spec while still telling readers what FPF is about.
10. For source-front, currentness, and refresh claims, use `G.2` and `G.11`; do not let a publication carrier become source-currentness proof.
11. For skill packs or MCP-backed access, expose edition identity, dependency boundary, and currentness or refusal conditions. Generated candidate text goes to `C.35`; tool and work claims go to `A.15` and local tool or work owners; assurance, evidence, and decision authority go to their direct owners.
Use this quick routing test:

| Live question | Use |
|---|---|
| "What is the form of FPF itself, and how are its carriers separated from the framework edition?" | `E.4.FPF` |
| "Does this whole-FPF object realize the Pillars for a declared use?" | `E.2.DA` |
| "How do FPF, a DPF, and a local framework depend on one another?" | `E.4` and `E.4.PFR` |
| "How do we author a domain or local framework grounded in FPF?" | `E.4.DPF` |
| "Is this DPF package good enough for one declared domain or local use?" | `E.4.DPF.DA` |
| "Is this individual pattern body good enough?" | `E.21` |
| "How do new users find and read FPF?" | `E.11` and `E.17` |

