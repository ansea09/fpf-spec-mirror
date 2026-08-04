---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:1"
section_title: "Intent & Scope (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__003_intent-scope-normative.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:1 — Intent & Scope (Normative)"
line_start: 28474
line_end: 28497
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.19.SelectorMechanism"
  - "A.2.5"
  - "A.2.6"
  - "A.3.3"
  - "A.6.5"
  - "C.16"
  - "C.2.1"
  - "E.18"
  - "E.24"
  - "F.9"
  - "G.0"
  - "G.11"
  - "G.4"
  - "U.ClaimScope"
  - "U.ContextSlice"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "role-specific space refs stay outside A.19"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
---

### A.19:1 - Intent & Scope (Normative)

**Intent.** Establish two composable A.19 values. `U.CharacteristicSpace` is the declared space of characteristics, scales, value sets, coordinate positions and groups, optional overlays, missingness semantics, comparability boundaries, normalization boundaries, and typing hooks. `CharacteristicSpacePredicate` is the by-value semantic predicate over declared coordinates in one such space. For dynamics, `U.Dynamics.stateSpace` points to the declared space so a holon's change can be described as a trajectory in typed coordinates. For epistemes, state remains governed by ESG; F-G-R are assurance coordinates, not an episteme state space.

**E.24.UK settlement.** `U.CharacteristicSpace` is retained as the root durable value for a declared multi-characteristic space. `CharacteristicSpacePredicate` is not a U-kind, relation occurrence, description edition, publication record, evaluation result, or acceptance result. A criterion-description episteme may express the predicate, and a direct consumer may evaluate it, but neither carrier nor result substitutes for the predicate's complete by-value meaning.

The A.19 objects are therefore the declared space and reusable predicate. They are not the filled evaluation, report, score table, dashboard, pattern-quality scale, DRR adequacy scale, FPF-level pillar scale, acceptance result, comparison result, or improvement portfolio that uses them.
**Scope.** Pattern A.19 **defines**:

- the declared `U.CharacteristicSpace` value as a finite product of slot value sets under A.18;
- the slot construct that binds one `U.Characteristic` to one selected scale and value set;
- the by-value `CharacteristicSpacePredicate` over declared coordinates, including its coordinate and scale bindings, normalization or F.9 Bridge basis where needed, operator or comparator semantics, cut or band, and polarity;
- optional order, topology, and distance overlays that downstream patterns may use when declared; and
- the typing hook `U.Dynamics.stateSpace : CharacteristicSpace`.

A.19 does not introduce measurement aspects, composite metrics, normalization semantics, comparison or selection work, consumer applicability, evaluation results, evidence relations, or dynamic laws. `A.19.UNM` governs normalization; `A.19.CPM` governs comparison; `A.19.SelectorMechanism` governs selection; C.16 and A.10 govern measurement and evidence provenance; A.3.3 governs dynamics.

**Space-and-predicate versus consumer boundary.** A consumer reference such as `...SpaceRef` designates one declared space. A consumer use of a predicate separately binds its exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective `U.ReferenceScheme` and reference plane, application or evaluation window, input projection, and direct evaluation operation. Those bindings are not fields of the space or semantic predicate. They may change while the predicate remains the same; conversely, changing a coordinate binding, scale, normalization or Bridge meaning, operator, cut or band, polarity, or governing comparator semantics creates a different predicate even if its wording is coextensional.

`A.19.ECS` constructs an evaluation `CharacteristicSpace` for an object kind under improvement. `E.21`, `E.9.DA`, `E.2.DA`, and other evaluation patterns consume declared spaces and predicates for their own evaluated objects. A.19 supplies the reusable values; those patterns supply object-specific applicability, evaluation, result, evidence-use, stop, and receiving-work semantics.
**Lexical guard (“map”).** Follow the normalization lexical discipline governed by **A.19.UNM**. In this pattern, lowercase **map** is used only in the mathematical sense, while capitalized **Map** retains its Part‑G suffix meaning (e.g., `DescriptorMap`). Do not mint new normalization terminology here.

**Lexical guard for value sets.** In A.19, the set that supplies values to a slot is `ValueSet(slot)` or an underlying value set. Do not call that value set a publication form, symbol bearer, source, description, or persistence object.

