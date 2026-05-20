---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:11"
section_title: "Conformance Checklist (normative, author‑facing)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__012_conformance-checklist-normative-author-facing.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:11 — Conformance Checklist (normative, author‑facing)"
line_start: 31400
line_end: 31416
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:11 - Conformance Checklist (normative, author‑facing)

The following obligations regulate **how to think and write** CT2R content. They are **notation‑agnostic** and purely conceptual.

| ID                                              | Requirement                                                                                                                                                                                                                                   | Purpose                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **CC‑CT2R‑1 (Canonical‑first).**                | A relation published for readers **SHALL** be stated in Working‑Model terms (`ut:*Of`) as the canonical form; any constructive or logical basis is recorded as **grounding** (not as the definition).                                         | Preserve human‑first canon and didactic primacy.                          |
| **CC‑CT2R‑2 (Mode declaration).**               | For every declarative relation or rule, the author **SHALL** declare `tv:validationMode ∈ {postulate, inferential, axiomatic}` in prose (no silent defaults).                                                                                | Make assurance intent explicit and auditable by reading.                  |
| **CC‑CT2R‑3 (Structural axiomatic grounding).** | If the relation is **structural** (a subtype of `ut:StructPartOf`) **and** the author chooses `axiomatic`, they **SHALL** provide a **grounding narrative** that can be reconstructed as one of the Γ\_m aggregators (*sum*, *set*, *slice*). | Tie high‑assurance claims to constructive identity without tool mandates. |
| **CC‑CT2R‑4 (No order/time in parts).**         | Authors **SHALL NOT** encode order (`Serial/Parallel`) or phase/time as part‑whole relations; handle them via `Γ_method` / `Γ_time` when relevant to the claim.                                                                               | Maintain the structure/order/time firewall.                               |
| **CC‑CT2R‑5 (Collection vs part).**             | Authors **SHALL** keep **MemberOf** (collections) distinct from **PartOf** (structure) and refrain from carrying reliability as if membership implied structural composition.                                                                 | Prevent category errors flagged in B.3 anti‑patterns.                     |
| **CC‑CT2R‑6 (Fit is explicit).**                | Where mappings or alignments matter, the author **SHALL** reason about **fit** explicitly (Congruence Level, conceptually) and acknowledge that weak fit reduces the effective reliability of any composed claim.                             | Keep integration quality first‑class.                                     |
| **CC‑CT2R‑7 (Notational independence).**        | Core meaning **MUST NOT** hinge on any specific diagram or syntax; illustrative renderings, if present, are labelled *informative*.                                                                                                           | Ensure longevity and cross‑discipline portability.                        |
| **CC‑CT2R‑8 (Layer direction).**                | Grounding flows **downwards** from Working‑Model to Assurance layers (Mapping/Logical/Constructive). Authors **SHALL** avoid back‑defining the canonical relation by its Mapping, Logical, Constructive, or Empirical grounding.                                                  | Preserve unidirectional dependence of layers.                             |
| **CC‑CT2R‑9 (Scope split).**                    | When assurance is discussed, authors **SHALL** state the **typed claim** and **scope** `S ∈ {design, run}` and keep them distinct in reasoning.                                                                                               | Prevent DesignRunTag chimeras.                                              |


