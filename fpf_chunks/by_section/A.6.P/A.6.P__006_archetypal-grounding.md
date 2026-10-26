---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims"
section_id: "A.6.P:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__006_archetypal-grounding.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.6.P — Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims"
  - "A.6.P:5 — Archetypal Grounding"
line_start: 20150
line_end: 20205
dependencies:
  - "A.1.SCR"
  - "A.1.STM"
  - "A.10"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.B"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "F.9"
keywords:
---

### A.6.P:5 - Archetypal Grounding

#### A.6.P:5.1 - Physical assembly and repeated occurrences

**Tell.** A maintenance note says `replacement bearing is linked to Pump_P`.

**Show the ordinary repair.** Recover physical bearing `Bearing_B`, pump `Pump_P`, and interval `Interval_T` independently. The readable candidate claim is `Bearing_B is part of Pump_P during Interval_T`. Select the intended direct parthood reading under A.14 and its applicable subject rule. Where that predicate and the case facts already settle the receiving question, state the assertion and stop; an installation history or occurrence identifier is not required merely to report current parthood.

**Show the identity-dependent stop.** A reliability analysis needs to distinguish the installed-part relation before removal from that after reinstallation. Current A.14 does not define an `InstalledPart` relation kind, its participant meanings, obtaining predicate, applicability, or same-versus-new-occurrence rule. Return A.6.RCD `missing-governor` for that proposed relation, naming `Bearing_B`, `Pump_P`, the relevant intervals, and the reliability comparison. Removal and reinstallation alone do not establish two occurrences. A.6.REL explains how to apply a supplied identity rule; it does not supply this missing rule.

**Conditional continuation.** If a direct installed-part definition is accepted, apply its obtaining and same-versus-new-occurrence rules to the case facts. Distinguish two occurrences only when that rule and those facts warrant them; add stable designations or occurrence descriptions only when the receiving use needs them. For repeated typed reuse, an `InstalledPartRelationSignature` may then declare `InstalledPartSlot` and `AssemblyWholeSlot` under A.6.5. Until that definition exists, these names remain hypothetical declaration candidates, as in A.6.REL:5.2 and A.6.5:5.2.

If the adopted construction rule makes installation Work constitutive, identify that independently admitted Work and its declared identity contribution. Database rows, diagram edges, assertions, and declaration components retain their own identities and do not supply the obtaining or recurrence rule. When a mathematical representation is used, state its C.29 correspondence separately. A separate relator is needed only if the direct ontology identifies and justifies it.

#### A.6.P:5.2 - Clinical evidence use and negative reliance

**Tell.** A care note says `the measurement supports the dose change`.

**Show.** The repair distinguishes the measurement work occurrence, its measurement-result episteme, the work-plan claim, the measured characteristic, the applicable range, and the exact evidence relation. `C.16` governs measurement construction and applicability; `A.10` governs whether that episteme bears on the named dose-change claim for this use. The broad predicate is not replaced by a universal support relation.

**Show the boundary.** If current evidence refutes the dose-change assertion or leaves reliance unresolved, the receiving evaluation records that posture. It does not create a negative world-side measurement, treatment, or evidence occurrence. A fresh publication of the same measurement-result episteme changes availability, not the measured condition or evidence relation by itself.

#### A.6.P:5.3 - Episteme correspondence and representation

**Tell.** Two teams say `the models are aligned`, and one tool draws an edge between their model nodes.

**Show — models.** Model epistemes `DesignModel_E` and `MaintenanceModel_E` have `EntityOfConcern` `PumpAssembly_P204` and effective reference schemes `CAD-Part-Scheme-v7` and `Asset-Register-Scheme-2026Q2`, respectively. `AlignmentEdge_17` joins nodes labelled `BRG-6204` and `bearing-4471`.

**Structure decision.** No established model-use structure changes either label's reading or whether replacement approval may use the pairing. Add no `BoundedModelUseStructure`; a diagram boundary is not evidence.

**Needed sentence.** `For bearing-replacement planning on PumpAssembly_P204, CAD-Part-Scheme-v7 label BRG-6204 and Asset-Register-Scheme-2026Q2 label bearing-4471 denote the same installed bearing.` This is a candidate claim, not yet a fact.

**Edge meaning.** Under the selected graph convention, `AlignmentEdge_17` expresses the candidate sentence. Its presence does not establish one referent or a Bridge occurrence. Use C.29 only if a separate mathematical representation or transfer question remains.

**Adjacent reading.** Record `ninety-seven percent of endpoint pairs passed the mapping test` with `C.16`. If approval relies on that measurement, `A.10` governs the evidence relation. The percentage does not establish the needed sentence.

**Result.** Bearing-replacement approval is not yet supported. First recover what each label designates under its reference scheme and the grounding or identity evidence for those referents. If the applicable designation and subject-identity rules establish one independently identified bearing, return that bounded identity claim; it does not by itself authorize replacement. If the labels designate different referents, or a kind and an individual, revise or reject the candidate claim as warranted. Keep missing interpretation or evidence explicit. Return `A.6.RCD missing-governor` only when the exact remaining predicate or a required applicability or identity rule is absent, naming that gap and the affected use.

**Representation boundary.** The edge and endpoint positions represent the assertion and its participants under the graph convention. Their interpretation makes the claim readable; the designation and subject-identity evidence decide its truth. Neither shared labels nor a visible edge establishes substitutability or an individuated relation occurrence by itself.

When the claim is that both model epistemes concern the same world-side holon, recover each episteme's exact EntityOfConcern or grounding designation plus the observations, trajectory, or identity evidence governed for that holon. A Bridge preserves stated correspondences and losses; it does not prove the common world-side referent.

**Show the viewpoint-conformance use.** A review must decide whether model episteme `E` conforms to maintenance viewpoint episteme `P`. Identify `E` from its claim content, EntityOfConcern, and effective reference scheme, and resolve `P` as one claim-bearing viewpoint edition before reading a diagram, field, or reference as ontology. Then apply the direct predicate governed by `E.17.0`: `EpistemeViewpointConformanceRelation(E,P)`. Plainly, `E` conforms to this exact viewpoint.

For unchanged `E` and `P`, the pair `<E,P>` determines one positive occurrence. Selecting `P` for this review is a separate use qualification: selection neither makes conformance obtain nor enters occurrence identity. If another review selects `P2`, test `<E,P2>` instead of retagging `E`. A `viewpointRef` or diagram label does not identify either participant by itself. A query, transformation, or projection may supply construction history for `E`, but neither that history nor an assertion, evaluation, representation, or publication makes conformance obtain.

Add an occurrence designator when a receiving use needs to refer to or reidentify that conformance occurrence, distinguish it from another, or use it as a participant. Add evaluation, evidence, construction history, representation or publication detail only when the corresponding question matters. A.6.P stops after recovering E, P and the direct relation. E.17.0 governs the predicate and any separately requested U.View recognition; actual Work retains its own basis.

#### A.6.P:5.4 - Method, Work, system-role objects, and agency

The sentence `the inspection method checks Pump_P` may remain ordinary metonymy under F.19. For a separate claim about actual inspection history, recover the following exact case. The source basis says that admitted `System_S` has the A.13 core for inspection: it is independently classified under local kind `InspectorSystemRole` and holds obtaining `InspectionAssignment-17` of declared `MaintenanceInspectionAssignment` species for the stated scope and window. A.15.1 then independently admits `InspectionWork_W` and its `enactsMethod(InspectionWork_W, InspectionMethod_M)` relation; the examination relation separately connects the Work to `Pump_P`. Because this worked account expressly states under which assignment the inspection was performed, F.6 then establishes `performedUnderAssignment(InspectionWork_W, InspectionAssignment-17)` and checks the already recovered performer against the holder. If the deciding F.6 fact were missing, attribution would remain unresolved; contrary facts would refute that attribution. The independently admitted Work remains in either case. Taxonomy episteme and reference scheme may interpret the assertion but are not assignment participants. `System_S` performs `InspectionWork_W`.

#### A.6.P:5.5 - Formal reduced case

`3 < 5` states an ordinary mathematical comparison. The numerals designate values and the sign expresses the less-than predicate under familiar arithmetic conventions. No separate representation or transfer question remains, so C.29 requires no additional account. If a later use introduces one, explain the correspondence it needs. The present use requires no explicit occurrence identity and can stop at the assertion. A tool's graph edge, tuple or reifier represents that content without constituting the relation.

