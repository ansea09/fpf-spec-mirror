---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 19900
line_end: 19914
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "C.2.1"
  - "E.10"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Generic support bucket** | Hides whether support means basedness, evidence use, assurance, work enablement, navigation, source description, or ordinary help | Apply the support wording selection test; state the direct relation or keep ordinary help instead of minting a support-headed relation or record |
| **Umbrella “anchored/attached/grounded” with no direct relation** | Hides relation kind and predicate | Name the participants, use the relation-specific verb, and apply its direct predicate |
| **Perspective flip without recoverable participants** | Direction and typing become ambiguous | Keep the same participants and direction in both active and passive wording; add formal endpoint names only when reused |
| **Work or carrier treated as evidence relation** | Collapses producing Work, result episteme, carrier, provenance, evidence use, and reliance | State the exact A.2.4 evidence-use relation; open A.10 only for the replayable provenance or reliance path |
| **Implicit “current/latest”** | Violates explicit time discipline | Declare `Γ_time` explicitly and use witness timespans for freshness where needed |
| **Decision use without its actual basis** | A relied-on assertion cannot be checked | Cite the exact evidence-use, provenance, currentness, or assurance relations required by that decision; do not add a generic witness field or new document |
| **Semantic meaning expressed as basedness** | Confuses source-local meaning with another relation | Recover the source-local claim under F.0.1 and add an F.17 cell or basis relation only when needed |
| **Relation-kind change presented as an edit** | A semantic shift masquerades as continuity | State the new direct relation and use the applicable continuity rule when that history matters |
| **Using `*Slot` to name an endpoint/value** | Confuses SlotKind with ValueKind/RefKind; breaks substitution and tooling | Keep `*Slot` for positions; use `base`/`dependent` for values and `*Ref` for stored references |
| **Optional record field treated as a carrier or free-text kind** | Lets a record label stand in for the direct relation | Make the field identify the already admitted relation vocabulary entry; keep the assertion, carrier, and relation occurrence separate |

