---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
section_id: "A.6.P:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__011_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6.P — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline"
  - "A.6.P:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 12851
line_end: 12887
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.2.6"
  - "A.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.8"
  - "A.6.9"
  - "A.6.A"
  - "A.6.B"
  - "A.6.H"
  - "A.6.S"
  - "A.7"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.2a"
  - "C.26"
  - "C.3.3"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "QualifiedRelationRecord"
  - "RelationKind"
  - "coupling"
  - "endpoint referential compression"
  - "export"
  - "language-state seam"
  - "lexical guardrails"
  - "measurement"
  - "probe"
  - "relation precision restoration"
  - "selected support reading"
  - "support/support-headed wording"
  - "under-specified relational language"
---

### A.6.P:8 — Common Anti‑Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| ---------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| “Just define the umbrella word” | Definitions do not separate arity, operation classes, or viewpoint asymmetry. | Replace umbrella use with explicit RelationKind + qualified record + change lexicon. |
| Keep the umbrella verb, add adjectives | Adjectives are not relation specifications; invariants remain unstated. | Mint/select distinct RelationKind tokens; enforce rewrite discipline. |
| Leave a FPF-governed generic head uninterpreted | Readers cannot tell what kind of thing the phrase governs, so later qualifiers float without an ontology. | Restore the head kind first in source-local terms; only then repair the remaining relation or comparison reading. |
| Let a qualifier smuggle the real claim kind or admissible-use boundary | A phrase like "comparative note", "safe guidance", or "reliable output" sounds precise while leaving the actual relation, comparison reference set, or authority-reference requirement implicit. | Unpack the qualifier into explicit comparison reference set, relation kind, admissibility condition, or L, A, D, and E-classified claim before any claim requiring explicit relation, admissibility, authority-reference relation, or reliance. |
| Treat support as the recovered kind or relation | `SupportRecord`, `support source`, `support line`, `support relation`, or `supported use` can sound precise while hiding whether the claim kind being made or admissible-use boundary is evidence path, source-use relation, admissible-use boundary, assurance claim, causal-use relation, decision help, publication help, C.29 lens-use result, characteristic construction, or ordinary orientation. | Recover the governing claim kind named by value or admissible-use boundary and governing pattern first: evidence path, `E.17:5.1b` source relation or claim-admissibility vocabulary, relationClaimSlice, admissibleUse, projectSideFPFRef, assurance claim, causal evidence path or causal-use verdict, C.29 lens-use result, characteristic construction, bridge or comparison relation, or companion-only reader function. Use support-headed wording only when that local pattern named by value defines the field or record and states admissible and non-admissible use. |
| Leave pronominal/metonymic endpoints implicit | Endpoint identity/facet remains guesswork; slot typing cannot stabilise. | Reconstruct candidate referents/facets (**capture as a Candidate‑Set Note**); add explicit slots/refs; then rewrite (A.6.8 is the archetype for “service” polysemy). |
| Ontology only, no lexical guardrails | Prose re-collapses meaning. | Add red-flag tokens + prohibited umbrella use in Tech/normative prose. |
| Lexicon only, no structural lens | Becomes subjective policing. | Introduce stable lens + slot schema; then attach guardrails. |
| Solve viewpoint mismatch by renaming endpoints | Silent re-typing breaks cross-pattern reuse. | Keep roles stable; use explicit kind selection + explicit repair options. |
| Using “bind” to mean “edit relation” | Collapses name-binding vs slot-writing classes. | Reserve `bind/rebind` for names; use change lexicon / slot verbs properly. |
| Implicit “current/latest” | Violates explicit time discipline. | Add explicit `Γ_time` where time matters. |
| Treat `Γ_time` as witness freshness | Time selection does not equal evidence freshness/decay; this conflates time discipline with evidence lanes. | Keep `Γ_time` for temporal scope; express freshness/decay via witness metadata and carrier-anchored E-claims. |
| Collapse search-space refs, declared-substrate interpretive views, and publication forms into one `space` or `view` | Search-space refs, outcome-space refs, declared-substrate interpretive views, and source sets and set results become indistinguishable, so later claims lose their primary `EntityOfConcern` or relation named by value/claim record. | Restore the declared `CharacteristicSpace`, any `SearchSpaceRef` and `OutcomeSpaceRef`, the active source set or active set result, the declared-substrate interpretive view or atlas view if any, and any `OutcomeMapRef` or `BridgeDistortionNote` before making the claim. |
| Compare across mixed kinds | `PublicationUnit`, project record, process, authority-use claim, or source-use claim gets ranked on one comparison reference set before its kind and governing requirement are restored. | First restore head kind, then qualifier-carried claim, then rewrite the sentence through the evidence path named by value, threshold, transfer condition, admissible-use boundary, or source-description claim wording so the comparison reference set is homogeneous. |

**Worked repair slice — NQD/OEE space/view/publication stack.**

Draft: “The archive projects into the outcome space through the atlas view.”

Repair sequence:

* `TraditionArchive` = derived retention view over one declared palette.
* `OutcomeSpaceRef` = guarded role reference to the declared `CharacteristicSpace` used for outcome-side judgment.
* `TraditionAtlasView` = optional related interpretive view, not the default meaning of the archive.
* `OutcomeMapRef` = explicit source-to-outcome map ref if the passage must show how the archive maps into one outcome-side or effect-side declared space/ref.

Canonical rewrite:

* Keep `TraditionArchive` as the source set for the set publication.
* Cite `OutcomeSpaceRef` only when the claim is about outcome-side evaluation against the declared `CharacteristicSpace`.
* Cite `OutcomeMapRef` only when the source-to-outcome relation or named map ref itself matters.
* Use `TraditionAtlasView` only if several declared views or qualifiers must stay visible together; otherwise leave the passage at archive/palette-first precision.

