---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__012_sota-echoing.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:11 — SoTA-Echoing"
line_start: 14034
line_end: 14046
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.B"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "are used only for pattern users"
  - "claims"
  - "component"
  - "conformance items"
  - "evidence records"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "platform"
  - "port"
  - "records"
  - "stack"
  - "substitutability"
---

### A.6.M:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt | Adapt for FPF | Reject or boundary | Practitioner implication |
| --- | --- | --- | --- | --- | --- |
| DoD OUSD(R&E) MOSA guidance and implementation guidebook (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Current official acquisition and engineering practice family for open modular systems; used as current practice guidance, not as a complete FPF ontology. | Modular design, interface standards, conformance verification, replacement or change policy, and competitive reuse are real conformance and substitution expectations. | Recover them as `InterfaceSpecificationRef`, `PlatformGrammarRef`, `substitutionOrChangePolicyRef`, conformance expectation, source relation, and evidence path only where live; route supplier-set, procurement, policy authorization, evidence, assurance, gate, decision, work, role, enactor, and mechanism claims to their exact neighboring patterns. | Do not treat `open`, interface publication, or modular-looking structure as substitutability, assurance, procurement suitability, supplier-set selection, policy authorization, quality proof, or decision authority. | A practitioner asking whether something is open first repairs the relation and the interface specification; selection, procurement, evidence, assurance, gate, work, and decision claims open only when that use is live. |
| Conway's law, the mirroring hypothesis, and Team Topologies and inverse Conway practice (`https://www.melconway.com/Home/Committees_Paper.html`; `https://doi.org/10.1016/j.respol.2012.04.011`; `https://itrevolution.com/wp-content/uploads/2022/06/TTOP_excerpt.pdf`) | Mature socio-technical law and empirical lineage plus current organization-design practice family; used as diagnostic pressure, not as a proof rule. | Team communication structure, team-boundary placement, and delivery responsibility can create real pressure on module and interface boundaries and useful correspondence clues. | Recover team and work material through `A.15`, `A.2`, `VP.RoleEnactor`, or `VP.Procedural` first; connect it to `ModuleInterfaceStructure` only through declared correspondence, allocation, boundary relation, and preserved and lost structure note. Use `C.29` when the correspondence is claimed as homomorphism-like or almost-same structure. | Do not treat Conway's law, an org chart, team responsibility label, or a delivery unit as proof of module interface, substitutability, modularity quality, evidence, gate passage, or architecture decision. | A practitioner may use team-boundary mismatch as a diagnostic prompt: repair the role, work, and module relation, then decide whether the module boundary, team boundary, communication relation, or architecture move changes. |
| Amdahl's law and communication and synchronization extensions (`https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf`; `https://arxiv.org/abs/1306.3302`; `https://arxiv.org/abs/2603.20654`) | Mature mathematical law plus current extension sources for communication, synchronization, and scalable-workload-fraction limits. | Serial work, synchronization, communication overhead, shared resources, and changing scalable workload fractions can limit the payoff of decomposition, parallelization, or specialization. | Use `C.29` for mathematical speedup or value-scalable-fraction reasoning, `E.18` and TGA for flow and crossing structure, and `C.31` and `C.16` for modularity and characteristic tradeoffs. | Do not treat module count, team count, service count, parallel-path count, or accelerator count as improvement, scalability, throughput, or evolvability by itself. | A practitioner considering a module split names the serial part, shared bottleneck, synchronization or communication overhead, and characteristic tradeoff before claiming improvement. |
| SEI Views and Beyond, ISO/IEC/IEEE 42010:2022, and multi-view architecture practice | Mature architecture-description lineage plus current international view-description discipline; not used as a current module-quality source. | Module and component-and-connector views are distinct architecture descriptions. | Use `ModuleInterfaceStructure` and `RuntimeInteractionStructure` as structure-kind signals under `C.30.ASV`. | Do not reduce architecture to a module diagram. | Module repair stays one architecture-structure concern, not the whole architecture ontology. |
| Platform and product-line engineering practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`; `https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature product-line variability lineage plus current platform-engineering maturity-model and current SPLE-review cues; used for variability-slot and extension-rule discipline, not as one FPF platform kind. | Variation slots and extension rules matter for reuse and substitution. | Use `PlatformGrammarRef`, `variabilitySlotRefs`, and change policy instead of a platform root kind. | Do not treat platform name as architecture quality, architecture scale-preference evidence, procurement suitability, supplier-set selection, or decision authority. | The next move is to identify extension rules and substitution conditions; quality, architecture scale preference, procurement, supplier-set, and decision claims exit to the exact neighboring patterns. |
| Architecture-operation language, with neural-network and software-system intakes as source examples | Current practitioner-language source examples accepted by the architecture workstream; used as recognition material, not as a standard or current-best-known authority. | Source labels such as block, layer, expert, router, cache, and state are useful recognition prompts. | Keep them as `C.30.STRAT` source labels until the receiving FPF kind, relation, claim-use, or source-use disposition is recovered; return to A.6.M only for module-interface relation, interface specification, platform grammar, substitutability, or open-architecture module-interface claims. | Do not import source-context labels as module kinds or evidence of adequacy. | The same repair works for neural-network block replacement, hardware module substitution, organizational module repair, and episteme-module repair without making any source context the ontology. |

Older or local sources may serve as lineage or worked examples only when the row says so. They do not stand in for current competitive source, and they do not make a module, interface, platform, or open-architecture claim admissible for comparison, assurance, gate, selection, or decision use without the exact neighboring pattern that governs that use.

