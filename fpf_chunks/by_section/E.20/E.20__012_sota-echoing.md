---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__012_sota-echoing.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:11 — SoTA-Echoing"
line_start: 79491
line_end: 79500
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:11 - SoTA-Echoing

| SoTA source idea | FPF invariant | Reader use | Rejected shortcut |
| --- | --- | --- | --- |
| Mechanism semantics in A.6.1, effects-handler practice, and refinement-style signature discipline require an explicit operation/signature/law/admissibility locus. | Mechanism meaning is assigned to A.6.1-governed mechanism definitions: operation algebra, law set, admissibility conditions, `SlotIndex`, required input/output `SlotKind`s, per-operation `SlotSpec`s, transport/bridge regime, applicability, audit, and monotone realization relation when declared. | When a mechanism is introduced or changed, name the mechanism-governing definition that carries those semantic fields before suites, plans, or wiring cite it. | Treating suite text, wiring prose, or a MIP manifest as mechanism semantics. |
| SoTA method evolution is carried by SoTA synthesis packs, shipping boundaries, and refresh wiring rather than silent kernel mutation. | `G.2`, `G.10`, and `G.11` own method-evolution apparatus: SoTA packs, release/shipping boundary, and refresh wiring. If the SoTA change alters mechanism meaning, the mechanism-governing definition changes. Current-source examples are usable only through named pack refs, such as SLSA v1.2 for provenance and attestation discipline, RO-Crate 1.2 for research-package publication discipline, QDax JMLR 2024 for QD-library practice, or a named current domain survey or source when that domain claim is present. | Tie a mechanism-changing SoTA update to the SoTA pack or source ref named by value and the refresh or shipping locus, then edit the mechanism-governing pattern if semantics changed. | Rephrasing a fashionable method update as kernel semantics or hiding it in wiring. |
| Open-ended and set-valued method evolution may return candidate sets, archives, or selector outputs. | C.18, C.19, and G.5 preserve set-return and selection boundaries; MIP must not force one approved mechanism too early. | Keep candidate mechanisms, selected sets, abstain/reject states, and archive semantics in their receiving loci until a mechanism-governing definition is actually selected for introduction. | Collapsing open-ended exploration or selector output into one prematurely approved mechanism. |
| Mechanism-related refresh uses explicit pins and trigger kinds rather than restating method semantics. | G.11-style refresh uses edition pins, policy pins, `PathSliceId`, and RSCR trigger kinds; refresh wiring enables comparable reruns but does not redefine the method. | When a mechanism change affects refresh, name the pins and RSCR trigger kinds and keep method semantics in the mechanism or SoTA-pack locus. | Letting refresh wiring become a second method definition. |
| Stable identifiers and modular vocabularies preserve reference continuity. | Names, aliases, lexicons, and stable identifiers preserve citeability; they do not establish mechanism law, admissibility, evidence, or gate fit. Mechanism meaning and admissibility belong in governing definitions, signature/law/admissibility patterns, suite boundaries, SoTA packs, and wiring modules according to their role named by values. | Use alias docking and lexicon updates to preserve references, then return mechanism meaning to the governing definition that governs it. | Treating ontology or vocabulary modularity as sufficient mechanism introduction. |

