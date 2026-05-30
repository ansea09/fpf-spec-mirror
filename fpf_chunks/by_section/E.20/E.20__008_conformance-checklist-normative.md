---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__008_conformance-checklist-normative.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:7 — Conformance Checklist (normative)"
line_start: 65418
line_end: 65441
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

### E.20:7 - Conformance Checklist (normative)

**Conformance use.** This checklist is evidence for the governing-definition assignment guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding trigger triage, manifest, card, suite, planning, wiring, lexical, RSCR, PQG, or deprecation move is live. Before applying any item, name the Solution move it tests; if no such reader move is live, treat the item as support-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary E.20 use starts with trigger triage and stops at the current governing locus when no denotation or mechanism-meaning change is live. Manifest-core items apply only when a MIP-run is actually triggered. Publication/assurance items apply only when citeability, card stubs, alias docking, RSCR, PQG, or deprecation continuity are live. Crossing, launch, and work-enactment checks are not governed by E.20; if they become live, use the gate, planning, or work loci and keep E.20 to governing-definition assignment.

| ID | Requirement | Purpose |
|---|---|---|
| **CC-E20-0 (MIP trigger triage).** | Every proposed mechanism, suite, planned-baseline, wiring, governing-definition, or citeable-token edit is classified as `MIP not triggered`, `local wording or alias-docking only`, or `MIP-run manifest required` before E.20 is cited to start a MIP-run. | Prevents pure currentness cleanup from becoming a false runtime gate or expanded authoring event. |

| **CC-E20-1 (Governing-definition assignment declared).** | Every MIP-run **SHALL** provide a MIP-run manifest that lists each changed item, exactly one governing definition, and the canonical location; each changed item **SHALL** be written in that canonical location. | Prevents “floating commitments” and semantic placement errors. |
| **CC‑E20‑2 (Card-first canonicalization).** | Any new `U.Mechanism.IntensionRef` enumerated anywhere **SHALL** resolve to a canonical mechanism card (stub allowed) before suite/protocol enumeration. | Eliminates dangling refs. |
| **CC‑E20‑3 (Suite discipline preserved).** | If a suite is edited, it **SHALL** preserve: membership set semantics, protocol closure, no hidden tails, no gate decisions/logs, no publication records. | Prevents suite-as-gate and suite-as-mechanism drift. |
| **CC‑E20‑4 (SlotKind lexicon used when shared).** | If mechanisms share slot vocabulary in a family/suite, a suite-scoped lexicon **SHALL** exist and member mechanisms **SHALL** cite it. | Stops slot token drift. |
| **CC‑E20‑5 (P2W seam preserved).** | If planned baselines are edited, plan items **SHALL** remain WorkPlanning-only (pins/refs only), **SHALL** target exactly one Description-scoped slot-bearing description via `target_slot_bearing_description_ref` (and **SHALL NOT** target a `U.Mechanism.IntensionRef`), and **SHALL NOT** contain enactment witnesses, launch values, or gate decisions. | Keeps planning and enactment separable and auditable. |
| **CC‑E20‑6 (Kernel stability handled).** | If a kernel suite would gain a new required stage, the change **SHOULD** be expressed as a suite variant; if mutation occurs, it **SHALL** include continuity measures (alias docking and explicit delta). | Minimizes E.15 impact radius of kernel edits. |

| **CC‑E20‑7 (SoTA wiring, not kernel semantics).** | Method/comparator choices **SHALL** be represented via SoTA packs and wiring modules; if a SoTA update changes mechanism semantics, that change **SHALL** be made in the mechanism-governing pattern and not by wiring. | Prevents silent semantic shifts. |
| **CC‑E20‑8 (Terminology continuity).** | Any rename changing citeable tokens **SHALL** use alias docking and register updates; silent rewrites are non‑conformant. | Preserves reference stability. |
| **CC‑E20‑9 (RSCR triggers + regressions).** | Any semantic or reference-change **SHALL** emit RSCR triggers and extend the regression envelope to cover dangling refs + suite closure + guard/gate separation + P2W seam. | Makes changed loci and regression obligations explicit and testable. |

| **CC‑E20‑10 (PQG coverage).** | Every MIP-run **SHALL** be reviewed under PQG (E.19) with PCP‑BASE and the triggered profiles implied by the change. | Normalizes review and refresh. |
| **CC‑E20‑11 (Deprecation preserves citeability).** | Any deprecation/supersession/retirement action **SHALL** preserve citeability of the deprecated token (alias docking if renamed), keep the canonical mechanism card, suite description, plan item, or wiring module resolvable, and declare a successor pointer or “no successor” explicitly (E.20:4.9.1). | Prevents broken citations and orphaned semantics during evolution. |

