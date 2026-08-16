---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__008_conformance-checklist-normative.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:7 — Conformance Checklist (normative)"
line_start: 87047
line_end: 87067
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

**Conformance use.** This checklist tests the governing-definition assignment guidance already stated in the Solution. It is not the first entry text for ordinary use or a mandatory full-corpus check; an item is applied only when its corresponding trigger triage, manifest, declaration target, suite, planning, wiring, lexical, RSCR, PQG, or deprecation move is present. Before applying any item, name the Solution guidance it tests; if no such reader use is present, treat the item as orientation-only or not applicable rather than expanding the applied assurance material.

**Conformance groups.** Ordinary E.20 use starts with trigger triage and stops at the current governing locus when no denotation or mechanism-meaning change is present. Manifest-core items apply only when a MIP-run is actually triggered. Publication and assurance items apply only when citeability, reference-reservation stubs, alias docking, RSCR, PQG, or deprecation continuity is part of the current claim. Crossing, launch, and work-enactment checks are not governed by E.20; if those claims become present, use the gate, planning, or work loci and keep E.20 to governing-definition assignment.

| ID | Requirement | Purpose |
|---|---|---|
| **CC-E20-0 (MIP trigger triage).** | Every proposed mechanism, suite, planned-baseline, wiring, governing-definition, or citeable-token edit is classified as `MIP not triggered`, `local wording or alias-docking only`, or `MIP-run manifest required` before E.20 is cited to start a MIP-run. | Prevents pure currentness cleanup from becoming a false runtime gate or expanded authoring event. |
| **CC-E20-1 (Governing-definition assignment declared).** | Every MIP-run **SHALL** provide a MIP-run manifest that lists each changed item, exactly one governing definition, and the canonical location; each changed item **SHALL** be written in that canonical location. | Prevents “floating commitments” and semantic placement errors. |
| **CC-E20-2 (Resolvable mechanism target).** | Every `MechanismDefinitionRef` resolves either to an explicitly non-mechanism reservation stub or to an introduced A.6.1 `U.Mechanism` episteme. Only the latter fills admitted mechanism positions. | Eliminates dangling references and card-form semio-bias. |
| **CC‑E20‑3 (Suite discipline preserved).** | If a suite is edited, it **SHALL** preserve: membership set semantics, protocol closure, no hidden tails, no gate decisions/logs, no publication records. | Prevents suite-as-gate and suite-as-mechanism drift. |
| **CC-E20-4 (Shared operation-member vocabulary preserves declaration locality).** | If a suite or family claims shared operation, argument, or result vocabulary, one citeable shared locus **SHALL** name its exact member declarations, and every member **SHALL** still define its own A.6.1 operation members and binding semantics. Equal spelling or a shared-term citation imports no declaration member or actual binding. | Prevents vocabulary drift without collapsing declaration-local semantics into a suite lexicon. |
| **CC-E20-5 (P2W planning-to-work boundary preserved).** | If planned baselines are edited, plan items **SHALL** remain WorkPlanning-only (pins/refs only), **SHALL** target exactly one Description-scoped slot-bearing description via `target_slot_bearing_description_ref` (and **SHALL NOT** target a `MechanismDefinitionRef`), and **SHALL NOT** contain enactment witnesses, launch values, or gate decisions. | Keeps planning and enactment distinct and replayable. |
| **CC‑E20‑6 (Kernel stability handled).** | If a kernel suite would gain a new required stage, the change **SHOULD** be expressed as a suite variant; if mutation occurs, it **SHALL** include continuity measures (alias docking and explicit delta). | Minimizes E.15 impact radius of kernel edits. |
| **CC‑E20‑7 (SoTA wiring, not kernel semantics).** | Method/comparator choices **SHALL** be represented via SoTA packs and wiring modules; if a SoTA update changes mechanism semantics, that change **SHALL** be made in the mechanism-subject pattern and not by wiring. | Prevents silent semantic shifts. |
| **CC‑E20‑8 (Terminology continuity).** | Any rename changing citeable tokens **SHALL** use alias docking and register updates; silent rewrites are non‑conformant. | Preserves reference stability. |
| **CC‑E20‑9 (RSCR triggers + regressions).** | Any semantic or reference-change **SHALL** emit RSCR triggers and extend the regression envelope to cover dangling refs + suite closure + guard/gate separation + P2W planning-to-work boundary. | Makes changed loci and regression obligations explicit and testable. |
| **CC‑E20‑10 (PQG coverage).** | Every MIP-run **SHALL** be reviewed under PQG (E.19) with PCP‑BASE and the triggered profiles implied by the change. | Normalizes review and refresh. |
| **CC‑E20‑11 (Deprecation preserves citeability).** | Any deprecation, supersession, or retirement action **SHALL** preserve citeability of the deprecated token, keep the mechanism episteme or reservation stub and every affected suite description, plan item, or wiring module resolvable, and state the direct successor relation or its absence (E.20:4.9.1). | Prevents broken citations and orphaned semantics during evolution. |

