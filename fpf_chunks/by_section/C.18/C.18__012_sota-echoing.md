---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open-Ended Search Archive and Front Stewardship"
section_id: "C.18:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__012_sota-echoing.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "C.18 — Open-Ended Search Archive and Front Stewardship"
  - "C.18:10 — SoTA-Echoing"
line_start: 49472
line_end: 49485
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "C.16"
  - "C.19"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
  - "C.36"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "currentness"
  - "descriptors"
  - "exploration archive"
  - "generation"
  - "lineage"
  - "non-dominated front"
  - "open-ended search"
  - "refresh"
  - "retained exploration value"
  - "telemetry"
---

### C.18:10 - SoTA-Echoing

**Source-currentness boundary.** This source-use basis was reviewed through 2026-08-01. Mutable preprints are pinned below to the edition actually used; the Qin et al. survey is pinned to its DOI-fixed journal article. Reopen the affected source-use row through `G.11` when a cited revision changes the archive, front, generation, or evaluation claim used here; when a newer field survey materially changes the known QD/OEE boundary; or when contrary evidence changes what can be claimed about bounded archives, descriptor generalization, or open-ended evaluation. C.18 records that trigger and the affected row but does not itself perform refresh.

| Source or source family | Adopted FPF move | Rejected overread | Field or boundary changed |
|---|---|---|---|
| Lin et al., `Quality-Diversity Optimization as Multi-Objective Optimization`, arXiv:2602.00478v1 (2026-01-31). | Treat QD and Q-front work through declared Q components, `DominanceSet`, comparator refs, archive relation, front relation, selected-set publication, and refresh. | Cell-filling or popularity accounts are the current ontology by default. | `FrontRecord@Context` must keep dominance grounds, comparator refs, and Q-component refs explicit. |
| Qin et al., `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI `10.1016/j.swevo.2025.102240`, `https://www.sciencedirect.com/science/article/pii/S2210650225003979`. | Use current survey support for approaches, applications, archive use, diversity use, and challenge framing. | Survey taxonomy replaces FPF governing loci. | `ExplorationArchiveRecord@Context`, `FrontRecord@Context`, and `OpenEndedVariantGenerationRecord@Project` stay governed by C.18 while selected-set publication and refresh stay with `G.5` and `G.11`. |
| Batra et al., `Quality Diversity for Robot Learning: Limitations and Future Directions`, arXiv:2407.17515v1 (2024-07-09). | State retained exploration value, generalization pressure, and limitations when an archive is used beyond current dominance. | Bounded archives or cell occupancy are enough evidence that NQD and OEE are useful. | `retainedExplorationValue`, `retentionPolicyRef`, `telemetryRefs`, and `nextGoverningRelation` must be filled when the archive is relied on. |
| Zhang et al., `Darwin Godel Machine`, arXiv:2505.22954v3 (2026-03-12). | Keep generated agents, archive lineage, empirically validated changes, method-family use, evaluation, and refresh separate. | OEE is one winner-selection method or source-free self-improvement story. | `OpenEndedVariantGenerationRecord@Project` records generation and archive or front linkage, while evaluation and refresh move to their governing patterns. |
| Novikov et al., `AlphaEvolve`, arXiv:2506.13131v1 (2025-06-16). | Separate generated method text, method description, evaluator relation, selected set, source-use relation, performed work, and work result. | Generated algorithm text is proof, gate permission, accepted method selection, or performed work. | `evaluatorOrComparatorRef`, lineage, source refs, and `nextGoverningRelation` decide whether to use C.18, A.19, `G.5`, `C.11`, A.15, or `G.11`. |
| Cultural-evolution and style-engineering source pressure from the music and dance intake. | Keep generated style or tradition variants as archive or front records until a cultural-evolution case or term bridge is current. | A cultural-style variant is a root cultural kind or a selected set by label. | `culturalVariantRefs` continue to `C.36`, `F.17`, `F.18`, or `F.9`; selected-set labels continue to `G.5`. |
| Architecture-search and product-family work. | Treat retained structures as candidate architecture moves only after the architecture claim is named. | An archive of layouts is the architecture or the architecture decision. | Architecture candidates exit to `C.30`, `C.30.ASV`, `C.30.AD`, or `C.32.P2S` after C.18 records descriptor, archive or front relation, and telemetry. |

