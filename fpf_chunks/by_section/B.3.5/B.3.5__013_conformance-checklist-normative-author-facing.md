---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:11"
section_title: "Conformance Checklist (normative, author-facing)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__013_conformance-checklist-normative-author-facing.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:11 — Conformance Checklist (normative, author-facing)"
line_start: 39182
line_end: 39198
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:11 - Conformance Checklist (normative, author-facing)

The following obligations regulate **how to think and write** CT2R content. They are **notation‑agnostic** and purely conceptual.

| ID                                              | Requirement                                                                                                                                                                                                                                   | Purpose                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **CC-CT2R-1 (Canonical-first).**                | A relation published for readers **SHALL** be stated in Working-Model terms (`ut:*Of`) as the canonical form; any constructive or logical justification is recorded as **grounding** (not as the definition).                                         | Preserve human-first canon and didactic primacy.                          |
| **CC‑CT2R‑2 (Mode declaration).**               | For every relation or rule covered by an elected B.3.5 profile, the author **SHALL** declare `tv:validationMode ∈ {postulate, inferential, axiomatic}` in prose. A direct relation outside the profile needs no B.3.5 mode. | Make elected assurance intent explicit without taxing ordinary direct use. |
| **CC‑CT2R‑3 (Structural axiomatic grounding).** | A covered structural parthood assertion uses `validationMode=axiomatic` and links to its applicable current C.2.1 `sum` or `slice` construction trace. The account reports independently grounded participants, occurrences, rule, and identity conditions; it creates none. | Make elected structural assurance inspectable without turning it into a truth-maker. |
| **CC‑CT2R‑4 (No order/time in parts).**         | Authors **SHALL NOT** encode order (`Serial/Parallel`) or phase/time as part‑whole relations; handle them via `Γ_method` / `Γ_time` when relevant to the claim.                                                                               | Maintain the structure/order/time firewall.                               |
| **CC‑CT2R‑5 (Collection vs part).** | Authors keep collection belonging under the collection's own rule distinct from every `PartOf` branch. A direct claim needs no profile fields; after B.3.5 election it uses `validationMode=axiomatic` and one current `C.13 set` trace. If constructive parthood also obtains, state and support that claim separately. | Prevent category errors without taxing ordinary belongs-to prose or prohibiting a stronger independently grounded claim. |
| **CC‑CT2R‑5a (Set trace reports).** | The elected set trace names the collection, the entity said to belong, the already established occurrence, the collection's own belongs-to rule, and the identity conditions. It creates none of them and supplies no structural-composition reliability. | Keeps optional assurance from becoming ontology. |
| **CC‑CT2R‑6 (Fit is explicit).** | Where mappings or alignments matter, the author **SHALL** reason about fit explicitly and acknowledge that weak fit reduces the effective reliability of a composed claim. | Keep integration quality first-class. |
| **CC‑CT2R‑7 (Notational independence).**        | Core meaning **MUST NOT** hinge on any specific diagram or syntax; illustrative renderings, if present, are labelled *informative*.                                                                                                           | Ensure longevity and cross‑discipline portability.                        |
| **CC‑CT2R‑8 (Layer direction).**                | Grounding flows **downwards** from Working‑Model to Assurance layers (Mapping/Logical/Constructive). Authors **SHALL** avoid back‑defining the canonical relation by its Mapping, Logical, Constructive, or Empirical grounding.                                                  | Preserve unidirectional dependence of layers.                             |
| **CC‑CT2R‑9 (Scope split).**                    | When assurance is discussed, authors **SHALL** state the **typed claim** and **scope** `S ∈ {design, run}` and keep them distinct in reasoning.                                                                                               | Prevent DesignRunTag chimeras.                                              |

