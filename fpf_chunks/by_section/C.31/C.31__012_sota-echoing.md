---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__012_sota-echoing.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:11 — SoTA-Echoing"
line_start: 74501
line_end: 74518
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
| DSM and dependency-structure practice (`https://dsmweb.org/design-structure-matrix-dsm/`; `https://dsmweb.org/introduction-to-dsm/`) | Architecture-analysis practice for dependency representation, clustering, and compact dependency communication. | Adopt typed dependency analysis as a possible declared measurement or comparison basis for specific C.31 heads such as `InternalCohesionDensity`, `ExternalCouplingDensity`, `InterfaceAlphabetSize`, and `HiddenCouplingDiscoveryRate`. | A dependency matrix is not architecture, proof, complete modularity, assurance, or decision by itself. | Use the dependency kind and subject to select the architecture question; add a scale or comparison basis when making that measurement or comparison. |
| Cabigiosu and Camuffo, "Measuring Modularity" (`https://doi.org/10.1109/TEM.2016.2614881`) | Published modularity-measurement source used as measure-plurality lineage, not as a universal current scoring rule. | Adopt the result that modularity measures answer different engineering or management questions; adapt it into `Characteristic plurality vs scalar pressure`, `MeasurementHeadMapping`, and proxy-risk fields. | One measure family is not universal modularity adequacy and does not settle architecture quality. | The practitioner asks which characteristic changes action before choosing any measure family. |
| Jung and Simpson modularity indices for DSM-based assessment (`https://pure.psu.edu/en/publications/new-modularity-indices-for-modularity-assessment-and-clustering-o/`) | Product-architecture and DSM-index lineage for index choice, clustering, and assessment variation. | Use as evidence that index choice depends on architecture type, dependency kind, and measure purpose; adapt by requiring the characteristic, scale, measurement and comparability basis, with relevant limits. | One modularity index is not FPF architecture quality, architecture adequacy, or decision authority. | An index used for comparison or decision needs its declared structure, dependency type, scale and relevant limits. A published account preserves that qualification. |
| MOSA and open systems practice (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Engineering and acquisition practice family for modular interfaces, conformance, severable components, replacement, and supplier diversity. | Adopt the pressure to make interface standards, conformance, substitutability, and supplier-diversity relations explicit; adapt by applying A.6.M when the module or interface claim needed by `InterfacePublicness`, `SubstitutabilityWidth`, or another head remains unresolved, and by applying `G.5` or `C.11` to supplier-set selection or procurement decision use when that use is being made. | `Open`, public, platform, API, conformance, or supplier-diversity label is not modularity, procurement suitability, or a beyond-local-repair claim by itself. | Open-system conformance and substitution claims inform C.31 once their relevant module-interface meaning and basis are recoverable; procurement and other beyond-local-repair uses require their subject pattern. |
| Platform and product-line engineering practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`; `https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Product-line variability lineage, platform-engineering maturity-model and SPLE-review cues; used for variability-slot, extension-rule, reuse, and exception-residue characteristic discipline. | Adopt variability slots, extension rules, template records, product-line records, allowed variation, and exception-residue tracking as possible C.31 characteristic subjects or declared measurement bases. | A platform or product-line label is not modularity value, reusable-structure proof, architecture scale-preference evidence, procurement suitability, or decision authority. | The practitioner names which characteristic changes action: interface standardization, module-type reuse, template compression, bespoke residue, exception curve, or the subject pattern for a beyond-local-repair claim being made. |
| Conway and mirroring, information-hiding, effective-interface, and abstraction-leakage lineage | Socio-technical and interface-boundary sources used as holon-architecture lineage, not as software-only ontology. | Keep the source meaning in ordinary language. State only the correspondence claims that obtain: organization Systems and relations; system-role classifications and assignments; enactor relations; division of work; and dated Work whose exact actual performers are recovered through A.13 and which A.15.1 independently admits. Add assignment and F.6 refs to a reusable record only when it or the receiving use expressly represents precise assignment-bound attribution; keep module-interface structures separate. Infer none from the lineage phrase. | Team boundary, delivery unit, documented interface, assignment, or abstraction label is not module boundary, Work occurrence, substitutability, modularity quality, or decision by itself. | The practitioner separates organization relations, work or procedure organization, any Work chain, explicit interface, implicit dependency, and modularity characteristic before claiming improvement. |
| Amdahl, queueing, and coordination-overhead laws (`https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf`; `https://arxiv.org/abs/1306.3302`; `https://arxiv.org/abs/2603.20654`) | Mathematical law and queueing lineage plus extension sources for communication, synchronization, and scalable-workload-fraction limits. | Adopt serial fraction, synchronization, communication overhead, WIP, waiting, bottleneck, and partitionability as possible C.31 defect signals; apply `C.29`, `E.18`, or `C.30.TFS-REL` when mathematical speedup or flow claims are being made. | More modules, teams, services, flow branches, processors, accelerators, or work partitions are not improvement by count. | A module split is evaluated by changed characteristics and bottlenecks, not by decomposition count. |
| Goodhart and Campbell proxy-pressure laws and holon-architecture trade-off discipline | General proxy-risk and trade-off lineage for architecture characteristic use. | Adopt vector and trade-off discipline plus proxy-risk discipline: no single modularity score, reusable share, benchmark, or index establishes value or beyond-local-repair use without the subject pattern for that use. | One declared measure value, benchmark, reusable-share number, or modularity index is not architecture value or decision authority. | The practitioner identifies the characteristic and checks the proxy-to-value inference on which a comparison or decision relies. |
| Architecture-operation language, with neural-network and software-system discussions as source examples, including the GonzoML architecture-operation intake | Practitioner-language source for replacement, selection, pruning, distillation, ablation, block substitution, memory or cache placement, gating, routing, and architecture search; not used as a standard. | Adopt operations as recognition cues for structure, relation, flow, scale, or candidate-set repair under consideration; keep the local meaning of block, layer, expert, cache, router or gate and use `C.30.STRAT` when that meaning still obscures the characteristic use. | Block, layer, expert, cache, router, gate, benchmark, ablation, pruning, or distillation label is not an FPF characteristic by default. | The operation points to a possible characteristic. Recover its subject, interpretation and admissible use; establish a scale when measurement requires one. |

**Source-use and refresh.** A source row identifies a contribution and its limits. A historical method or result can support a use within its established premises; it does not establish the current comparative standing of an approach. When the question depends on present acquisition rules, a changed interface standard or newer comparative evidence, recover that basis through G.2 or the applicable source rule before relying on it. A source citation supplies no missing measurement, conformance test or decision premise.

Reopen only the dependent characteristic, comparison or repair when its source meaning, assumptions or applicable rule changes. For example, a changed substitution specification can alter InterfaceStandardizationShare and SubstitutabilityWidth while leaving an earlier counted population intact. A queueing-model change reopens the dependent bottleneck inference; it does not erase an independently observed dependency. Preserve unchanged source uses and bounded historical results.

