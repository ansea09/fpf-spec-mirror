---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__007_archetypal-grounding-worked-cases.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:5 — Archetypal Grounding (Worked Cases)"
line_start: 1788
line_end: 1851
dependencies:
  - "A.1.1"
  - "A.1.STM"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.3.4"
  - "A.6.1"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24.UK"
  - "G.11"
keywords:
---

### A.1:5 - Archetypal Grounding (Worked Cases)

#### A.1:5.1 - Pump As Acting System

Use this illustrative engineering case to decide whether Pump #37 qualifies as a `U.System`. Take the following construction and operating facts as the case inputs:

- Pump #37 is the assembly initially built from casing C37, impeller I37, seal S37, motor M37, inlet flange FI37, and outlet flange FO37. Each is a physical component of that pump under A.14 `ComponentOf`.
- C37 encloses I37; M37 is bolted to C37 and its shaft is coupled to I37; S37 seals the shaft entry; FI37 and FO37 are fastened to C37 and open into its water passage. These obtaining fastening, enclosure, coupling, sealing, and connection relations assemble the named components as one pump.
- The case's installed-assembly reidentification rule preserves Pump #37 through shutdown, temporary disassembly, and replacement of S37 by S38 with the same mating geometry and operating limits, provided C37 is retained and the assembly and its inlet/outlet boundaries are restored before return to service. Replacing C37 or permanently dismantling the assembly ends Pump #37 under this rule.
- With water at 20 °C and a 400 V, 50 Hz supply, this assembly sustains a flow of 10 m³/h against a pressure rise of 200 kPa. The coupled motor, impeller, casing, and sealed passage produce that whole-pump response; no one component supplies it alone.
- `U.System` is already an admitted public U-kind in FPF; `E.24.UK` governs admission of public U-kinds. The pump's physical organization can cause the stated water-moving change while retaining its identity, supplying the kind-specific acting-eligibility condition.

For the larger-assembly test, `CW-Install-1` is the case's governed plant-installation rule. It integrates the intact pump as the replaceable circulation unit of CoolingLoop-2: bolt its feet to the loop support, connect FI37 to the loop's return port and FO37 to its supply port, and connect M37 to the electrical supply. Compare its applicability conditions with the remaining case facts:

| CW-Install-1 condition | Pump #37 fact |
| --- | --- |
| Each water port must mate with a 50 mm bore flange having four 12 mm bolt holes on a 90 mm bolt circle. | FI37 and FO37 each have that bore and hole geometry. |
| The support accepts four mounting holes on a 120 × 180 mm rectangle and a pump mass of at most 40 kg. | The pump's feet have that hole pattern; the intact pump has a mass of 35 kg. |
| With the available 400 V, 50 Hz supply and water at 20 °C, the pump must sustain at least 8 m³/h against a pressure rise of 200 kPa. | The stated whole-pump response is 10 m³/h at that pressure rise under those conditions. |
| Installation must retain the casing, internal assembly, and pump-side inlet/outlet boundaries. | The rule uses the existing mounting holes and flanges; it changes only the external attachments, preserving Pump #37 under the stated reidentification rule. |

These facts supply one larger-assembly witness: CW-Install-1's conditions are satisfied and its construction preserves the pump as a constituent. Together with the identified candidate, components, assembly, reidentification rule, whole-level response, and acting eligibility, they establish the A.1 criterion for this illustrative `U.System` case. A classification evaluation given these inputs returns `true`; a separate C.2.1 assertion may state that result.

The candidate-side facts and the available evaluation inputs remain distinct. If the mass fact is withheld and no other input resolves the compatibility question, evaluation returns `unknown`; withholding that fact changes neither the pump nor whether the criterion holds. Replacing S37 by the specified S38 preserves Pump #37 through the admitted maintenance phase. Replacing C37 instead requires identifying the resulting assembly as another candidate under this case's rule.

If the intact candidate instead has a mass of 45 kg, CW-Install-1 cannot supply the sixth component because its support limit is 40 kg. A coupling, load-envelope, or boundary-interface violation likewise defeats that installation rule even when the drawing and rule-description episteme are current. Failure of this one rule does not settle the existential larger-assembly condition: the candidate fails that component only if none of the governed larger-assembly constructions has conditions satisfied by its actual facts. Evaluation returns `false` when its inputs determine that failure, and `unknown` when the searched methods or available facts do not settle it. Renaming or republishing the cited criterion pattern does not change Pump #37 or those facts; any change to the episteme's designation, edition, or currentness remains separately governed.

Separate direct relations then state that Pump #37 fills the holder-system slot of its cooling-water circulation `U.SystemRoleAssignment`, has a flow-rate capability envelope, and participates in the water-moving transformation. A separate inspection account may identify `WO-1842 : U.Work`, but the cooling-water assignment does not make Pump #37 its performer: the exact inspector System must have its own A.13 core, the Work must be independently admitted under A.15.1, and F.6 is added only if that account needs precise assignment-bound attribution through the inspector's same obtaining assignment. Pump #37 remains the inspected or participating subject unless another direct performer basis establishes otherwise. No omnibus participation or candidate-classification relation is added. The pump can have selected structures; its maintenance model may participate in a separately selected `BoundedModelUseStructure`, but that structure neither identifies the pump nor makes it a holon.

#### A.1:5.2 - Scientific Theory As Episteme Holon

This schematic illustration concerns Newtonian gravitation in one exact selected edition, first identified as a C.2.1 `U.Episteme` candidate. Its actual claim-bearing constitution can satisfy the A.1 criterion for the already admitted `U.Episteme` kind when the following facts obtain:

- exact law, definition, derivation, diagram, exercise, and evidence-relation epistemes are the candidate constituents;
- exact claim-composition and episteme part relations organize those constituents as one governed claim-bearing whole;
- C.2.1 identifies this theory episteme by its exact claim content, EntityOfConcern, and effective ReferenceScheme; a change to any of these identifies another episteme. Historical continuation between the earlier and later epistemes requires a separate `EpistemeEditionRelation` under an applicable edition-continuity rule;
- inferential and explanatory characteristics arise from the organized claim-bearing whole rather than from one constituent;
- its actual inferential interfaces, effective reference scheme, applicability conditions, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed method for composing it as a constituent of a larger explanatory or educational episteme;
- `U.Episteme` is already an admitted public U-kind in FPF; `E.24.UK` governs admission of public U-kinds, while C.2.1 supplies the kind-specific constitution condition.

For a particular theory, supply the constituent identities and an independently obtaining direct episteme-part or claim-composition predicate before drawing the recognition conclusion (C.13:5.3). A textbook publication can make this edition available, but the publication form and the episteme that describes the composition method do not create the theory's compatibility or holonhood. Classification work may evaluate the criterion and a separate C.2.1 assertion may state the result; evidence, warrant, edition currentness, receiving reliance, and any B.2 whole-reidentification question remain separately governed.

A system under an exact `U.SystemRoleAssignment` may explain, publish, compare, or use this episteme through separately governed Work and relation occurrences; the assignment alone establishes none of those acts. Revision Work yields another episteme, with any edition relation tested separately.

#### A.1:5.3 - Fleet As Collection Or Acting Collective

A fleet register supports the claim that a vehicle belongs to the fleet only under its registration rule. In the register-only case the fleet is not thereby established as a holon: no vehicle-to-whole assembly or composition-grounded characteristic is claimed. Fleet availability is a separate collection characteristic. A fleet-coordination organization that coordinates vehicles, drivers, rules, and Work can be an acting collective `U.System` only after all six A.1 matters, including its constructive relations and assembly, have been recovered.

If a source says "the fleet responded", recover the actual claim: individual vehicle work, fleet-coordination system work, collection-as-whole characteristic, or B.2 whole reidentification.

#### A.1:5.4 - Lathe Changing A Workpiece

A lathe can change a workpiece during manufacturing without thereby becoming a part of the workpiece or the larger whole containing it.

Use `A.3.4` to identify the bounded transformation from the exact changed referent, extent, boundary conditions, actual change facts, and continuity rule. Use the direct subject patterns for the lathe's participation, method, dated work, work-to-change facts, and evidence. Use A.14 or C.13 for part-whole only when an exact grounded part relation independently obtains.

#### A.1:5.5 - Stop Before A Whole Is Constructed

A pallet holding an unconnected pump, motor, baseframe, and manifold is a collection of exact entities. The list and physical proximity do not supply the fastening, coupling, enclosure, connection, assembly, or reidentification facts needed to recognize a skid holon. A construction drawing is an episteme about a possible assembly.

A selected `BoundedModelUseStructure` may organize model-applicability, delimitation, maintenance, and crossing relations for an engineering use. It remains dependent `U.Structure`; selecting it, naming it, or drawing it supplies no part relations, whole-level characteristic, acting eligibility, or B.2 whole reidentification.

Mounting, wiring, and fluid-connection changes may each be exact `U.Transformation` occurrences. Their participation in one work episode or one flow description does not identify a composite transformation. Without a direct transformation-composition governor, retain the separate changes and stop before transformation parthood, composite identity, or A.1 holon recognition. This stop does not say that the changes are atomic or have no finer parts.

