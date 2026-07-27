---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
section_id: "A.6.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__001_intro.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
  - "A.6.6:intro — Intro"
line_start: 18688
line_end: 18736
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

## A.6.6 - Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)
> **Status:** Stable
> **Type:** Definitional relation-discipline pattern

**Plain-name.** Scoped witnessed base declaration discipline.

**Use this pattern when** a dependent content is admissible, usable, interpretable, comparable, publishable, or actionable only relative to an explicit base through a declared base relation, scope and time condition, and witness set.

**What goes wrong if missed.** Umbrella words such as anchor, support, ground, attach, or based-on hide the relation kind, endpoint kinds, scope, time, and witness discipline; authors then rename endpoints or flip directions instead of repairing the relation.

**What this buys.** The project gets a scoped witnessed base declaration with typed dependent and base slots, explicit baseRelation, scope and time condition, witnesses or pins, and named change classes for rebasing, retiming, or withdrawing the declaration.

**E.24.UK settlement.** A.6.6 does not admit `U.BaseDeclarationDiscipline` as a durable U-kind. The pattern governs base-declaration discipline. It retains `U.ScopedWitnessedBaseDeclaration` only as a dependent durable declaration value under the A.6 signature and slot-relation settlement: a scoped declaration that relates dependent content to an explicit base through a declared base relation, scope and time condition, and witnesses. Local support wording, anchor wording, source pointers, publication records, and witness carriers do not become U-kinds by appearing in this discipline.

**Status.** Normative (Core).

**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; adjacent to A.6.5 `U.RelationSlotDiscipline`.

**Depends on.**
– A.6.0 `U.Signature` (universal signature carrier).
– A.6.5 `U.RelationSlotDiscipline` (SlotKind/ValueKind/RefKind stratification + slot-operation lexicon).
– A.2.6 (Scope discipline; explicit `Γ_time`; implicit “latest/current” is forbidden).
– A.2.4 evidence-use and status-use relation discipline for decision-relevant witness sets, including timespan, provenance, scope, polarity, and freshness constraints.
- A.7 (Strict Distinction; EntityOfConcern vs Description-episteme and specification-use cases vs publication face, form, unit, carrier, and rendering lanes).
– E.8 (pattern authoring order & SoTA discipline).
– E.10 (LEX‑BUNDLE discipline; D.CTX lexical guardrails).

**Coordinates with.**
– A.10 Evidence–Provenance DAG discipline (`verifiedBy`, `validatedBy`).
– A.14 per-edge constructive grounding (`tv:groundedBy`) and `validationMode` discipline.
– C.2.1 `U.EpistemeSlotRelation` grounding slots (`GroundingHolonSlot`, `EntityOfConcernSlot`).
– A.6.3 `U.EpistemicViewing` (`EntityOfConcernRef`-preserving view operators; base-relative “how” without retargeting).
– A.6.4 `U.EpistemicRetargeting` (base-change along `KindBridge`; retargeting lexicon and continuity rules).
– C.3.3 `U.KindBridge` & `CL^k` (explicit repair/translation when endpoint kinds or Contexts differ; no silent re-typing).
– E.18 assurance-operations on `U.Transfer` (`CalibrateTo`, `CiteEvidence`, `AttributeTo`, `ConstrainTo`, …).
– F.9 Bridges & CL (cross-context and cross-plane base declarations cite Bridge ids + CL policy).
– F.15 F-Suite validation harness (carrier/source-currentness, provenance, and refresh governance).
- F.18 naming governance (Tech/Plain twins and publication-lane naming boundaries).

**Source phrases and red-flag cues (informative; not normative vocabulary).**
– “anchoring / anchor” (source umbrella colloquial; a red-flag token for *under-described dependence*). **Prohibited in Tech register** as a meaning-surrogate; treat it as a defect to be rewritten into an explicit `baseRelation(dependent, base)` form. Allowed only when referring to a **pattern-defined primitive** that already reserves the word (e.g., E.10 MG‑DA *Domain Anchoring*; evidence/pin “anchors” where the term is explicitly reserved), or inside quoted source text that is immediately followed by a conformant rewrite.
– “Qualified statement / attributed edge” (knowledge-graph colloquial).
– “support / supported by / support basis / support relation” (ordinary umbrella support wording). Diagnostic for possible basedness only when the phrase asserts that a dependent content is admissible, usable, interpretable, comparable, publishable, or actionable relative to an explicit base. Otherwise classify the live reading and apply the governing ontology named by value: source-description, evidence, assurance, causal-use, mathematical-lens, work/resource, publication/navigation, or ordinary help.
– “Pinning” (when witnesses are edition pins).

**Mint‑or‑Reuse note (informative).**
This pattern **mints** the declaration value name `U.ScopedWitnessedBaseDeclaration` (SWBD) and the **base‑change lexicon** operation class names (`declareBase`, `rebase`, `retime`, …) as canonical labels for semantic change classes.
It **reuses** A.6.5 SlotSpec discipline (SlotKind/ValueKind/RefMode), A.2.6 Scope discipline (`U.Scope`, explicit `Γ_time` when time matters), and A.2.4 evidence-use relation discipline as the enforcement substrate for witness use.

