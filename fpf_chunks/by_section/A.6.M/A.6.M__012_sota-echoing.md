---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module and Interface Claim Repair"
section_id: "A.6.M:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__012_sota-echoing.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.6.M — Module and Interface Claim Repair"
  - "A.6.M:11 — SoTA-Echoing"
line_start: 23070
line_end: 23080
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
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "component"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "platform"
  - "port"
  - "stack"
  - "substitutability"
---

### A.6.M:11 - SoTA-Echoing

| Source or practice | Role in this account | Adopt | Adapt for FPF | Reject or boundary | Practitioner implication |
| --- | --- | --- | --- | --- | --- |
| DoD OUSD(R&E) MOSA guidance and implementation guidebook (<https://www.cto.mil/sea/mosa/>; <https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf>) | Acquisition and engineering guidance on open modular systems, including the dated 2025 guidebook. | Modular design, interface standards, conformance verification, replacement policy, change policy, and competitive reuse are real conformance and substitution expectations. | Recover them as an independently identified `InterfaceSpecification` episteme plus an `interfaceSpecificationRef` that resolves it, `PlatformGrammarRef`, `substitutabilityPolicyRef`, `changePolicyRef`, conformance expectation, source relation, and evidence relation only where the recovered claim needs them. Non-module selection, procurement, policy, evidence, assurance, gate, decision, Work, system-role-assignment, responsibility, and mechanism claims keep their own direct patterns; a responsibility claim needs its own predicate and case facts, with A.6.RCD used only for a missing rule. | Do not treat `open`, interface publication, or modular-looking structure as substitutability, assurance, procurement suitability, supplier-set selection, policy authorization, quality proof, or decision authority. | A practitioner asking whether something is open first repairs the relation and interface specification; other claims remain with the patterns named in `A.6.M:12`. |
| Conway's law, the mirroring hypothesis, and Team Topologies and inverse Conway practice (<https://www.melconway.com/Home/Committees_Paper.html>; <https://doi.org/10.1016/j.respol.2012.04.011>; <https://itrevolution.com/wp-content/uploads/2022/06/TTOP_excerpt.pdf>) | Socio-technical conjecture, empirical mirroring research and organization-design practice; used diagnostically. | Team communication structure, boundary placement, and delivery-responsibility relations can create real pressure on module and interface boundaries and useful correspondence clues. | Recover the team, system-role, Work or responsibility claims actually needed under their separate rules and facts. Connect that material to `ModuleInterfaceStructure` only through declared correspondence, allocation, boundary relation, and preserved and lost structure note. Use C.29 when a separate mathematical representation, transfer or inference question remains. | Do not treat Conway's law, an org chart, assignment, responsibility label, or delivery unit as proof of module interface, substitutability, modularity quality, evidence, gate passage, or architecture decision. | A practitioner may use team-boundary mismatch as a diagnostic prompt, then repair each exact relation before deciding what architecture change is warranted. |
| Amdahl's law and communication and synchronization extensions (<https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf>; <https://arxiv.org/abs/1306.3302>; <https://arxiv.org/abs/2603.20654>) | Amdahl's mathematical result and proposed extensions concerning communication, synchronization and scalable-workload fractions. | Serial work, synchronization, communication overhead, shared resources, and changing scalable workload fractions can limit the payoff of decomposition, parallelization, or specialization. | Keep an adequate mathematical calculation; use C.29 when its representation, transfer or inference conditions remain unresolved. Use `E.18` for transformation-flow structure, `C.30.TFS-REL` when the module claim uses an architecture-to-transformation-flow relation, and `C.31` and `C.16` for modularity and characteristic tradeoffs. | Do not treat module count, team count, service count, transformation-flow path count, or accelerator count as improvement, scalability, throughput, or evolvability by itself. | A practitioner considering a module split names the serial part, shared bottleneck, synchronization or communication overhead, and characteristic tradeoff before claiming improvement. |
| SEI Views and Beyond, ISO/IEC/IEEE 42010:2022, and multi-view architecture practice | Architecture-description and viewpoint discipline; not a source of module-quality judgments. | Module and component-and-connector views are distinct architecture descriptions. | Use `ModuleInterfaceStructure` and `RuntimeInteractionStructure` as structure-kind signals under `C.30.ASV`. | Do not reduce architecture to a module diagram. | Module repair stays one architecture-structure concern, not the whole architecture ontology. |
| Platform and product-line engineering practice (<https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/>; <https://www.sei.cmu.edu/library/variability-in-software-product-lines/>; <https://arxiv.org/abs/2605.21353>) | Product-line variability, platform-engineering and review sources used for variability slots and extension rules. | Variation slots and extension rules matter for reuse and substitution. | Use `PlatformGrammarRef`, `variabilitySlotRefs`, and change policy instead of a platform root kind. | Do not treat platform name as architecture quality, architecture scale-preference evidence, procurement suitability, supplier-set selection, or decision authority. | The next module-repair action is to identify extension rules and substitution conditions; non-module quality, scale-preference, procurement, supplier-set, and decision claims are governed by the patterns named in `A.6.M:12` when those claims are being made. |
| Architecture-operation language, with neural-network and software-system intakes as source examples | Practitioner-language examples used for recognition. | `C.30.STRAT` source labels, including source examples such as `block`, `layer`, `expert`, `router`, `cache`, and `state`, are useful recognition prompts. | Keep them as source labels until the recovered FPF kind, relation, claim-use, or source-use disposition is known; use A.6.M only for module-interface relation, interface specification, platform grammar, substitutability, or open-architecture module-interface claims. | Do not import source-context labels as module kinds or evidence of adequacy. | The same repair works for neural-network block replacement, hardware module substitution, organizational module repair, and episteme-module repair without making any source context the ontology. |

