---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:1"
section_title: "Intent & Scope (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__003_intent-scope-normative.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:1 — Intent & Scope (Normative)"
line_start: 29797
line_end: 29814
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UNM"
  - "A.2.6"
  - "A.6.5"
  - "B.1"
  - "C.16"
  - "C.2.1"
  - "E.24"
  - "F.17"
  - "F.9"
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
  - "state trajectories"
  - "structural overlays"
  - "subspace"
  - "system-role–Method–Work assertions stay outside A.19"
---

### A.19:1 - Intent & Scope (Normative)

**Intent.** Establish two composable A.19 values. `U.CharacteristicSpace` is the declared space of characteristics, scales, genuine Scale value sets, Coordinate positions and groups, optional overlays, comparability boundaries, normalization boundaries, and typing hooks. `CharacteristicSpacePredicate` is a typed unary Boolean predicate over declared Coordinates in one such space. Partial observations and their absence statuses remain consumer inputs. For dynamics, `U.Dynamics.stateSpace` points to the declared space so a holon's change can be described as a trajectory in typed Coordinates. For epistemes, state remains governed by ESG; F-G-R are assurance coordinates, not an episteme state space.

`U.CharacteristicSpace` is the declared multi-characteristic space. `CharacteristicSpacePredicate` is a reusable predicate by value, not its wording, evaluation, or result. Consumer uses remain separate from both.

**Scope.** Pattern A.19 defines:
- the declared `U.CharacteristicSpace` value as a finite product of slot value sets under A.18;
- the slot construct that binds one `U.Characteristic` to one selected scale and value set;
- the typed unary `CharacteristicSpacePredicate` over declared Coordinates, including its input variable, domain and coordinate projection, Scale meanings, any A.19.UNM normalization used to obtain its inputs, Boolean expression, cut or band, composition, and polarity;
- optional order, topology, and distance overlays that downstream patterns may use when declared; and
- the typing hook `U.Dynamics.stateSpace : CharacteristicSpace`.

A.19 stops after the space, predicate, optional overlays, and dynamics typing hook. Use A.19.UNM for normalization, A.19.CPM for comparison, A.19.SelectorMechanism for selection, C.16 and A.10 for measurement and evidence, and A.3.3 for dynamics.

**Space-and-predicate versus consumer boundary.** A consumer reference such as `...SpaceRef` designates one declared space. A consumer use of a predicate separately binds its exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective `U.ReferenceScheme` and reference plane, application or evaluation window, available input or partial-input status, and evaluation operation. Those bindings are not fields of the space or predicate. They may change while the predicate remains the same; changing the predicate's input domain or coordinate projection, Scale meaning, normalization, Boolean expression, cut or band, composition, or polarity creates a different predicate. Any obtaining semantic Bridge, its bounded-use claim and reliance, and any applicable plane relation are separately identified for the consumer use; none identifies the predicate. A.19.CPM separately governs comparison relations, comparator applications, and their results.

`A.19.ECS` constructs an evaluation `CharacteristicSpace` for an object kind under improvement. `E.21`, `E.9.DA`, `E.2.DA`, and other evaluation patterns consume declared spaces and predicates for their own evaluated objects. A.19 supplies the reusable values; those patterns supply object-specific applicability, evaluation, result, evidence-use, stop, and receiving-work semantics.
