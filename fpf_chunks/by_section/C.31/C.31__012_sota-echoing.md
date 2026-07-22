---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__012_sota-echoing.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:11 — SoTA-Echoing"
line_start: 61923
line_end: 61943
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.31.RSA"
  - "C.32"
  - "C.32.P2S"
  - "G.5"
keywords:
  - "ModularityVectorLite"
  - "bespoke residue"
  - "cohesion"
  - "coupling"
  - "evidence reuse"
  - "interface variation"
  - "modularity characteristics"
  - "reusable-structure characteristics"
  - "substitutability"
---

### C.31:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt and adapt for C.31 | Rejected overread | Practitioner implication |
| --- | --- | --- | --- | --- |
| DSM and dependency-structure practice (`https://dsmweb.org/design-structure-matrix-dsm/`; `https://dsmweb.org/introduction-to-dsm/`) | Mature and still-used architecture-analysis practice for dependency representation, clustering, and compact dependency communication. | Adopt typed dependency analysis as a possible declared measurement or comparison basis for specific C.31 heads such as `InternalCohesionDensity`, `ExternalCouplingDensity`, `InterfaceAlphabetSize`, and `HiddenCouplingDiscoveryRate`. | A dependency matrix is not architecture, proof, complete modularity, assurance, or decision by itself. | A dependency graph helps only after dependency kind, subject, scale, repair direction, and non-admissible use are declared. |
| Cabigiosu and Camuffo, "Measuring Modularity" (`https://doi.org/10.1109/TEM.2016.2614881`) | Published modularity-measurement source used as measure-plurality lineage, not as a universal current scoring rule. | Adopt the result that modularity measures answer different engineering or management questions; adapt it into `Characteristic plurality vs scalar pressure`, `MeasurementHeadMapping`, and proxy-risk fields. | One measure family is not universal modularity adequacy and does not settle architecture quality. | The practitioner asks which characteristic changes action before choosing any measure family. |
| Jung and Simpson modularity indices for DSM-based assessment (`https://pure.psu.edu/en/publications/new-modularity-indices-for-modularity-assessment-and-clustering-o/`) | Product-architecture and DSM-index lineage for index choice, clustering, and assessment variation. | Use as evidence that index choice depends on architecture type, dependency kind, and measure purpose; adapt by requiring characteristic, scale, measurement basis, comparability basis, and forbidden overread. | One modularity index is not FPF architecture quality, architecture adequacy, or decision authority. | Index use requires declared structure, dependency type, scale, and non-admissible overread before publication, comparison, or decision use. |
| MOSA and open systems practice (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Current engineering and acquisition practice family for modular interfaces, conformance, severable components, replacement, and supplier diversity. | Adopt the pressure to make interface standards, conformance, substitutability, and supplier-diversity relations explicit; adapt by applying A.6.M before C.31 characterizes `InterfacePublicness`, `SubstitutabilityWidth`, or related heads, and by applying `G.5` or `C.11` to supplier-set selection or procurement decision use when that use is being made. | `Open`, public, platform, API, conformance, or supplier-diversity label is not modularity, procurement suitability, or a beyond-local-repair claim by itself. | Open-system conformance and substitution claims may change C.31 repair only after the module-interface relation is repaired; procurement and other beyond-local-repair uses require their governing pattern. |
| Platform and product-line engineering practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`; `https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature product-line variability lineage plus current platform-engineering maturity-model and current SPLE-review cues; used for variability-slot, extension-rule, reuse, and exception-residue characteristic discipline. | Adopt variability slots, extension rules, template records, product-line records, allowed variation, and exception-residue tracking as possible C.31 characteristic subjects or declared measurement bases. | A platform or product-line label is not modularity value, reusable-structure proof, architecture scale-preference evidence, procurement suitability, or decision authority. | The practitioner names which characteristic changes action: interface standardization, module-type reuse, template compression, bespoke residue, exception curve, or the governing pattern for a beyond-local-repair claim being made. |
| Conway and mirroring, information-hiding, effective-interface, and abstraction-leakage lineage | Socio-technical and interface-boundary sources used as holon-architecture lineage, not as software-only ontology. | Adopt declared correspondence across role and enactor structures, work and procedural structures, and module-interface structures; separate explicit interface specification from observed or implicit interface; recover hidden coupling and source-return conditions. | Team boundary, delivery unit, documented interface, or abstraction label is not module boundary, substitutability, modularity quality, or decision by itself. | The practitioner separates team and work structure, explicit interface, implicit dependency, and modularity characteristic before claiming improvement. |
| Amdahl, queueing, and coordination-overhead laws (`https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf`; `https://arxiv.org/abs/1306.3302`; `https://arxiv.org/abs/2603.20654`) | Mature mathematical law and queueing lineage plus current extension sources for communication, synchronization, and scalable-workload-fraction limits. | Adopt serial fraction, synchronization, communication overhead, WIP, waiting, bottleneck, and partitionability as possible C.31 defect signals; apply `C.29`, `E.18`, or `C.30.TFS-REL` when mathematical speedup or flow claims are being made. | More modules, teams, services, flow branches, processors, accelerators, or work partitions are not improvement by count. | A module split is evaluated by changed characteristics and bottlenecks, not by decomposition count. |
| Goodhart and Campbell proxy-pressure laws and holon-architecture trade-off discipline | General proxy-risk and trade-off lineage for architecture characteristic use. | Adopt vector and trade-off discipline plus proxy-risk discipline: no single modularity score, reusable share, benchmark, or index establishes value or beyond-local-repair use without the governing pattern for that use. | One declared measure value, benchmark, reusable-share number, or modularity index is not architecture value or decision authority. | The practitioner states which characteristic changes action and which proxy overread is blocked before comparison or decision. |
| Architecture-operation language, with neural-network and software-system discussions as source examples, including the GonzoML architecture-operation intake | Current practitioner-language source for replacement, selection, pruning, distillation, ablation, block substitution, memory or cache placement, gating, routing, and architecture search; not used as a standard. | Adopt operations as recognition cues for structure, relation, flow, scale, or candidate-set repair under consideration; keep block, layer, expert, cache, router, and gate as `C.30.STRAT` source labels until the FPF characteristic subject, relation kind, scale, and admissible use are recovered. | Block, layer, expert, cache, router, gate, benchmark, ablation, pruning, or distillation label is not an FPF characteristic by default. | The operation points to a possible characteristic; it does not name the characteristic until the FPF kind, subject, scale, and admissible use are recovered. |

**Source-currentness front.** Use the table's `Currentness or lineage use` cell as the source-use boundary. A lineage row can explain why a characteristic family matters, but it cannot establish current comparison, procurement, assurance, benchmark, decision, publication, or other beyond-local-repair use without a current source relation under `G.2` or the governing pattern for that use. Refresh the source use when MOSA or acquisition guidance changes, platform or product-line practice changes, DSM or modularity-index practice changes, queueing or coordination-overhead assumptions change, proxy-pressure law is used for a new claimed value relation, or architecture-operation language is used as current practice rather than as source-side recognition language. When refresh changes the source-use relation, update the affected characteristic head, proxy-risk field, audit question, related claim governance, or report-only boundary rather than treating the older source as current by default.

Rows named current, such as MOSA guidance, current platform practice, current scalable-workload extensions, or current architecture-operation corpus material, require source refresh before beyond-local-repair use when the named practice changes. Rows named lineage stay lineage unless a current source relation is explicitly recovered.

Older or local sources may serve as lineage or worked examples only when the row says so. They do not stand in for current competitive source, and they do not make a modularity value admissible for beyond-local-repair use without the governing pattern for that use.


