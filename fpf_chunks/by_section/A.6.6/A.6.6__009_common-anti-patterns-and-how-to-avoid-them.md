---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline: Say Exactly What Something Depends On"
section_id: "A.6.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.6.6 — Base Declaration Discipline: Say Exactly What Something Depends On"
  - "A.6.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 23899
line_end: 23913
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.24.UK"
  - "E.8"
  - "F.0.1"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.9"
  - "U.KindBridge"
  - "U.Transfer"
keywords:
---

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Generic support bucket** | Hides whether support means basedness, evidence use, assurance, work enablement, navigation, source description, or ordinary help | Apply the support wording selection test; state the direct relation or keep ordinary help instead of minting a support-headed relation or record |
| **Umbrella “anchored/attached/grounded” with no direct relation** | Hides relation kind and predicate | Name the participants, use the relation-specific verb, and apply its direct predicate |
| **Perspective flip without recoverable participants** | Direction and typing become ambiguous | Keep the same participants and direction in both active and passive wording; add formal endpoint names only when reused |
| **Work or carrier treated as evidence relation** | Collapses producing Work, result episteme, carrier, provenance, evidence use, and reliance | State the exact A.2.4 evidence-use relation; open A.10 only for the replayable provenance or reliance path |
| **Unclear temporal applicability** | Current or latest leaves the intended time-dependent claim ambiguous | State the applicable interval or temporal rule, using explicit Γ_time when the governing use needs it. Check witness freshness separately. |
| **Decision use without its actual basis** | A relied-on assertion cannot be checked | Cite the exact evidence-use, provenance, currentness, or assurance relations required by that decision; do not add a generic witness field or new document |
| **Semantic meaning expressed as basedness** | Confuses source-local meaning with another relation | Recover the source-local claim under F.0.1 and add an F.17 cell or basis relation only when needed |
| **Relation-kind change presented as an edit** | A semantic shift masquerades as continuity | State the new direct relation and use the applicable continuity rule when that history matters |
| **Using `*Slot` for a participant or designation** | Conflates declaration content, participant and reference | Reserve `...Slot` for a declaration-local SlotKind. Name the dependent and base directly, distinguishing their designations and any reference values under A.6.5. |
| **Optional record field treated as a carrier or free-text kind** | Lets a record label stand in for the direct relation | Make the field identify the already admitted relation vocabulary entry; keep the assertion, carrier, and relation occurrence separate |

