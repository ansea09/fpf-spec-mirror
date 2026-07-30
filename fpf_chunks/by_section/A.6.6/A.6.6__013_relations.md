---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
section_id: "A.6.6:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__013_relations.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
  - "A.6.6:12 — Relations"
line_start: 19763
line_end: 19794
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

### A.6.6:12 - Relations

**Specialises A.6.P Relational Precision Restoration (RPR).**
A.6.6 is the RPR specialisation for “basedness / relative‑to” claims: it makes the relation kind explicit via `baseRelation`, qualifies it with scope/`Γ_time`/witnesses, and standardises evolution via a base‑change lexicon plus lexical red‑flags (`anchor*`).

**Builds on A.6.5 `U.RelationSlotDiscipline`.**
SWBD introduces a structured record with slots; those slots must be SlotKind/ValueKind/RefKind disciplined, and its change classes must not be confused with slot-edit operations (A.6.5) or name-binding terminology (E.10 / L‑BIND).

**Constrains A.10 evidence admissibility links.**
`verifiedBy` and `validatedBy` are treated as baseRelation tokens; their scope/time and witnesses become explicit when used for decisions.

**Aligns with A.2.4 evidence-use relation discipline.**
Decision-relevant witness sets should be represented through evidence-use relations or pinned witness records with explicit timespans and provenance discipline, not as ad-hoc prose references and not as roles held by epistemes.

**Aligns with A.14 constructive grounding (`tv:groundedBy`).**
Constructive grounding is one specific declared `baseRelation` reading: dependent is a model edge, base is a constructor trace; witnesses pin the trace and `U.Work` records.

**Coordinates with C.2.1 grounding holons.**
Situational/empirical grounding via `GroundingHolonSlot` is treated as a distinct declared `baseRelation` reading; it must not be collapsed with `tv:groundedBy` or with semantic meaning assignment.

**Coordinates with A.6.3–A.6.4 viewing/retargeting.**
Viewing and retargeting are specialised “relative-to-base” moves (preserve `EntityOfConcernRef` vs retarget it along a declared bridge). They should reuse SWBD vocabulary where an explicit base declaration is required (scope/time/witness), without collapsing into generic “anchoring” prose.

**Coordinates with A.2.6 and `Γ_time`.**
Base declarations inherit the rule that time-dependent assumptions require explicit `Γ_time`; “current/latest” is not admissible.

**Feeds E.10 / F.18 lexical governance.**
Umbrella metaphors are disallowed as substitutes for baseRelation tokens; prose must name explicit relation kinds and keep the meaning lane separate (SenseCell/ConceptSet).

**Constrains support wording in A.6.P/E.10.**
Support-looking phrases that mean base-dependence are governed here: select a declared `baseRelation`, name `dependent` and `base`, add scope/time/witnesses as live, and preserve polarity. Support-looking phrases that do not mean base-dependence use the ontology of the governing pattern for that claim rather than becoming `SupportRelation`, `SupportBasis`, or `SupportRecord` buckets.

