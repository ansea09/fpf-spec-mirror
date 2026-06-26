---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
section_id: "A.6.6:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
  - "A.6.6:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 16637
line_end: 16651
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.3-A.6.4"
  - "A.6.4"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.18"
  - "F.9"
  - "U.RelationSlotDiscipline"
keywords:
  - "SWBD"
  - "anchoring"
  - "base declaration"
  - "baseRelation"
  - "basedness"
  - "rebase"
  - "rescope"
  - "retime"
  - "scope"
  - "support-as-basedness"
  - "witnesses"
  - "Γ_time"
---

### A.6.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| **Generic support bucket** | Hides whether support means base-dependence, evidence polarity, assurance input, causal-use basis, mathematical-lens use, work enablement, source-description, publication companion, or ordinary help | Apply the support wording selection test; use SWBD only for genuine basedness and apply every other reading's ontology of the governing pattern for that claim |
| **Umbrella “anchored/attached/grounded” with no baseRelation** | Hides relation kind; cannot state invariants | Introduce a declared baseRelation token and rewrite prose to use it |
| **Perspective flip without endpoint-position names** | Directionality and typing become ambiguous | Use `dependent`/`base` endpoint positions consistently; declare polarity in baseRelation declaration |
| **Treating evidence as “the base”** | Confuses base with witnesses | Make evidence/pins witnesses unless the relation kind’s base is explicitly an evidence carrier |
| **Implicit “current/latest”** | Violates explicit time discipline | Declare `Γ_time` explicitly and use witness timespans for freshness where needed |
| **Decision gating without witnesses** | Becomes folklore; not reviewable | Add resolvable witnesses through evidence-use relations, A.10/G.6 carrier, source-currentness, or provenance records, certificate pins, or proof-bearing publications named by the direct governing pattern |
| **Semantic meaning expressed as a base declaration** | Confuses meaning lane with admissibility lane | Use SenseCell/ConceptSet; keep SWBD for non-semantic basedness |
| **Change baseRelation in place** | Semantic shift masquerades as update | Mint a new declaration and connect via continuity |
| **Using `*Slot` to name an endpoint/value** | Confuses SlotKind with ValueKind/RefKind; breaks substitution and tooling | Keep `*Slot` for positions; use `base`/`dependent` for values and `*Ref` for stored references |
| **Typing `baseRelation` as a `publication-side object*` carrier** | Confuses a relation-specific relation token with a publication-lane object; invites “free text as relation kind” | Store `baseRelation` as a declared `NameToken` that resolves to a vocabulary entry with an explicit signature and relation-specific constraints |

