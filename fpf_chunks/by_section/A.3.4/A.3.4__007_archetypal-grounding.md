---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__007_archetypal-grounding.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:5 — Archetypal Grounding"
line_start: 9569
line_end: 9617
dependencies:
  - "A.1"
  - "A.10"
  - "A.11"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.22"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "G.11"
keywords:
  - "actual bounded change"
  - "actual subject facts"
  - "changed referent"
  - "continuity and reidentification"
  - "occurrence boundary"
  - "transformation composition"
---

### A.3.4:5 - Archetypal Grounding

#### A.3.4:5.1 - Physical system change

A nuclear-plant team says that a revised operating method stabilized a temperature profile after a thermal-power change. **Result:** `CoolingLoopTransformation-7` is identified from the continuing cooling loop, stabilization interval, operating conditions, and before/during/after temperature facts. The method is `U.Method`; the control-law model is an episteme; measurements and the safety decision use their own patterns. This short case names no dated adjustment `U.Work` occurrence or work-to-change predicate, so it makes no such connection. If that claim is later needed, name both participants and apply `4.2.4`.

#### A.3.4:5.2 - Biological editing

A CRISPR project says that an editing protocol changed a DNA target while keeping off-target risk under a bound. **Result:** identify the biological transformation from the continuing DNA referent, edit interval, boundary conditions, and sequence facts. Keep the protocol description, biochemical mechanism, lab `U.Work`, sequence measurement, risk evaluation, acceptance verdict, and publication separate. This sketch names neither a lab-work/transformation pair nor a matching predicate, so it asserts no connection between them; apply `4.2.4` only if that later claim is needed. For phrases such as *edited sequence*, *lab output*, or *accepted result*, name the exact participant and relation needed by the receiving claim.

**Spontaneous non-agentive case — result:** `SeedlingFirstLeafUnfolding-B17 : U.Transformation` is an actual first-leaf unfolding without an actor, method, or work claim. The continuing subject is the already existing `Seedling-B17`. Its boundary runs from unfolding onset `t0` to the first stable full-expansion state `t1`; leaf-configuration and exposed-surface facts before, during, and after distinguish the episode under the stated growth conditions. The same-seedling rule permits ordinary cellular turnover and growth but excludes division, grafting, death, or replacement.

At this resolution the case asserts neither finer transformation parts nor partlessness. If a later use asks for an actor, apply A.3; if it asks for work, apply A.15.1 and then `4.2.4`. Otherwise keep the case non-agentive and do not open `A.15.PROD`.

#### A.3.4:5.3 - Specification repair

A safety specification is revised so that an emergency-stop boundary no longer permits two incompatible readings. **First result:** `EmergencyStopSpec-E1` and `EmergencyStopSpec-E2` are different C.2.1 epistemes because their claim content differs. `EpistemeEditionRelation(EmergencyStopSpec-E1, EmergencyStopSpec-E2)` may relate them when its historical-continuation predicate holds; neither is one continuing changed episteme.

A.3.4 may instead identify a change of `EmergencyStopSpec-Carrier-17 : U.PresentationCarrier` if `E.24.PUB` identifies the same carrier across the editing interval and the before/during/after borne-expression facts plus carrier-continuity rule are present. If the carrier identity, facts, or rule are missing, no carrier transformation follows. If editing `U.Work` first constituted `EmergencyStopSpec-E2`, name that work and the transformation by which the later identity closed. Apply `4.2.4` to the work-to-change pair, then apply `A.15.PROD` to the change-to-identity pair. Each connection needs a matching predicate or valid local compound basis; return `missing-governor` for either pair that lacks one. The repair method, ambiguity-removal assertion, review result, and publication of the later episteme remain separate.

#### A.3.4:5.4 - Formal construction

A proof constructs a formal object and shows that a morphism preserves an invariant. **Result:** within the declared formal substrate, the formal object and ordered boundary can ground one formal transformation. The proof term and morphism expression are representations; publishing the proof is another relation. If a later claim says that dated work realized the transformation, apply `4.2.4` and return `missing-governor` when the named pair has neither an existing predicate nor a valid local compound basis.

#### A.3.4:5.5 - Architecture change

An architecture team performs dated architecture `U.Work`. During the same interval, a selected structure undergoes a separately identified transformation: an interlevel conflict decreases while a key architecture characteristic stays within bounds. **Result:** the work and transformation are both present, but this sketch does not connect them. If that connection is needed, name both participants and apply `4.2.4`; use a matching predicate or valid local compound claim, otherwise return `missing-governor` for the pair. Characteristic evaluation, decision, and publication remain separate.

#### A.3.4:5.6 - Functional transformer in a flow

When a sentence says that a system *transforms input to output* or *implements an algorithm*, split at least four questions: which system and role assignment are claimed; which subject actually changed; which participant, port, or operation bindings hold at the boundary; and where the transformation sits in the selected E.18 flow. Add a method or method description only if the sentence also makes that claim.

Examples:

- A pump can be the acting system while the actual transformation is the bounded pressure change of an identified fluid volume. Inlet and outlet pressure facts are characteristic-state and port facts; the pump curve is a model episteme.
- A warehouse can perform receiving `U.Work` while pallet-location and inventory-state changes occur. If a later use needs a work-to-change claim, name the pair and apply `4.2.4`. Orders and pallets keep their work, transfer, resource, or affected-subject relations.
- A neural-network block can participate in an activation transformation. Tensor-shape declarations, the attention method, dated inference work, benchmark evaluation, and architecture allocation stay separate and use their own patterns.


#### A.3.4:5.7 - Assembly changes before PumpSkid identity

Before asking whether PumpSkid 7 exists as one entity, identify the already existing base frame `BF-7`, pump unit `PU-7`, motor `MU-7`, junction enclosure `JE-7`, pipe spool `PS-7`, cable set `CS-7`, and their still-open mechanical, electrical, and fluid interfaces. `AssemblyConfiguration-7` is the A.22 selected structure made from those referents and their actual attachment, terminal, and flange-connection organization during assembly. It is not another name for a future PumpSkid 7 entity.

The mounting transformation changes the frame-to-pump and frame-to-motor attachment facts. The wiring transformation changes cable-to-terminal connections. The fluid-connection transformation changes spool-to-flange and seal facts. Identify each independently through its subject, extent, boundary conditions, before/during/after facts, and continuity rule. The change of `AssemblyConfiguration-7` can also be identified if those attachment, terminal, flange, and seal relations have declared participants and obtaining rules and the selected structure has its own boundary and continuity rule. Call that occurrence the configuration transformation. The other three changes do not become its components merely because they occur in the same assembly episode.

No current FPF relation in this case says that the mounting, wiring, fluid-connection, and configuration changes compose one transformation. Keep all four changes and stop before a part or whole-transformation claim. The result from `4.2.1` is `missing transformation-composition governor`; a proposed local compound claim also lacks an admitted derivation substrate.

Positive A.1 classification on that basis stops as well, because no accepted composition result supplies an exact whole candidate and all six constructive components required by A.1. The point at which a separate PumpSkid 7 identity rule first becomes true remains an entity-identity inception question; production completion, commissioning work, evidence, acceptance, and any B.2 whole-reidentification claim also remain separate.

