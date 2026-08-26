---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__001_intro.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:intro — Intro"
line_start: 19166
line_end: 19216
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

## A.6.6 - Base Declaration Discipline - Direct relation first; reusable declaration only when needed
> **Status:** Stable
> **Type:** Definitional relation-discipline pattern

**Plain-name.** Saying exactly what something depends on.

**Use this pattern when** a sentence says that one thing is calibrated to, based on, attributable to, constrained by, or otherwise usable relative to another, and the actual relation is still hidden by words such as *anchor*, *support*, *ground*, or *based on*.

**First useful move.** Name the actual dependent and base, state the direct relation in an ordinary sentence, and apply that relation's own predicate to the current facts. Stop when this readable assertion answers the receiving question.

**What goes wrong if missed.** An umbrella word hides the relation kind or reverses its participants. At the opposite extreme, a simple assertion is expanded into slots, witnesses, editions, and a new record even though no later use needs them.

**What this buys.** A direct, testable assertion first. Scope, time, evidence, a reusable `RelationSignature`, or a reviewable record is added only when the direct predicate or one named receiving use needs that distinction.

**Not this pattern when.** If the direct relation and its participants are already clear, use its direct pattern. If *support* means evidence use, assurance, ordinary help, work enablement, navigation, source description, or another non-basedness reading, use that reading's direct pattern instead.

**E.24.UK settlement.** A.6.6 admits neither `U.BaseDeclarationDiscipline` nor `U.ScopedWitnessedBaseDeclaration`. The retired `U.ScopedWitnessedBaseDeclaration` spelling must not be used as a kind or as a world-side relation occurrence. When a named receiver needs a reviewable scoped assertion, the phrase *scoped witnessed base declaration* denotes an optional representation of one C.2.1 assertion or description episteme. Its ClaimGraph states a separately governed direct relation and any current qualifiers; the record makes none of those facts obtain. An already admitted relation kind may separately have a reusable `RelationSignature` under A.6.0.
**Status.** Normative (Core).

**Placement.** Part A, cluster A.IV “Signature Stack & Boundary Discipline”; adjacent to A.6.5 relation-declaration slot discipline.

**Depends on.**
- A.6.0 `U.Signature` (universal signature carrier).
- A.6.5 relation-declaration slot discipline (SlotKind, ValueKind, and RefKind stratification plus the slot-operation lexicon).
- A.2.6 (Scope discipline; explicit `Γ_time`; implicit “latest/current” is forbidden).
- A.2.4 evidence-use and status-use relation discipline for decision-relevant witness sets, including timespan, provenance, scope, polarity, and freshness constraints.
- A.7 (Strict Distinction; EntityOfConcern vs Description-episteme and specification-use cases vs publication face, form, unit, carrier, and rendering lanes).
- E.8 (pattern authoring order & SoTA discipline).
- E.10 and E.10.D1 for wording-use recovery, with F.0.1 and F.17 for source-local meaning and its optional durable address.

**Coordinates with.**
- A.10 evidence-provenance and bounded-reliance discipline; its graph cites independently obtaining direct relations and admits no generic `verifiedBy` or `validatedBy` fallback edge.
- A.14 per-edge constructive grounding (`tv:groundedBy`) and `validationMode` discipline.
- C.2.1 episteme constitution through exact claim content, EntityOfConcern, and effective ReferenceScheme, plus the separately obtaining `EpistemeEmpiricalGroundingRelation` between an exact episteme and grounding holon.
- A.6.3 `U.EpistemicViewing` (`EntityOfConcernRef`-preserving view operators; base-relative “how” without retargeting).
- A.6.4 EntityOfConcern retargeting: one local arrow between exact epistemes with different EntitiesOfConcern, plus a separate use assertion for invariant, visible loss, bounded use, conditions, support, and polarity.
- C.3.3 `U.KindBridge`, including the `CL^k` value declared for that bridge (explicit repair or translation when exact endpoint kinds differ; no silent re-typing).
- E.18 assurance-operations on `U.Transfer` (`CalibrateTo`, `CiteEvidence`, `AttributeTo`, `ConstrainTo`, …).
- F.9 only when the declaration consumes an obtaining Bridge between two exact F.17 local senses. Cite the Bridge and its separate bounded-use claim; `CL` is optional evidence shorthand. A ReferencePlane difference uses its applicable plane relation and does not create an F.9 Bridge.
- F.15 F-Suite validation harness (carrier/source-currentness, provenance, and refresh governance).
- F.18 naming governance (Tech/Plain twins and publication-lane naming boundaries).

**Source phrases and red-flag cues (informative; not normative vocabulary).**
- “anchoring / anchor” (source umbrella colloquial; a red-flag cue for *under-described dependence*). In Tech register, replace it with the ordinary sentence and relation-specific verb that name the actual participants and direct relation. Keep it only for an already reserved primitive (for example, E.10 MG-DA *Domain Anchoring*), or in quoted source text followed immediately by the direct rewrite.
- “Qualified statement / attributed edge” (knowledge-graph colloquial).
- “support / supported by / support basis / support relation” (ordinary umbrella support wording). Diagnostic for possible basedness only when the phrase asserts that a dependent content is admissible, usable, interpretable, comparable, publishable, or actionable relative to an explicit base. Otherwise classify the live reading and apply the governing ontology named by value: source-description, evidence, assurance, causal-use, mathematical-lens, work/resource, publication/navigation, or ordinary help.
- “Pinning” (when witnesses are edition pins).

**Mint-or-reuse note (informative).**
A.6.6 mints no public kind. It reuses the direct relation kind and predicate selected for the claim. A reusable definition uses that relation kind's existing or newly justified A.6.0 `RelationSignature`; one scoped assertion remains a C.2.1 episteme. The local labels `declareBase`, `rebase`, `retime`, and related terms may classify edits to such an assertion or declaration when a named receiver needs that history. They neither make the world-side relation obtain nor require a record for an ordinary sentence.

