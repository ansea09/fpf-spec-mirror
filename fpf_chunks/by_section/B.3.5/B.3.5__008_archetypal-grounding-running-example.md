---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:6"
section_title: "Archetypal Grounding - Running example"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__008_archetypal-grounding-running-example.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:6 — Archetypal Grounding - Running example"
line_start: 45336
line_end: 45365
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:6 - Archetypal Grounding - Running example

> **Story.** A refinery team publishes `:PumpA ut:ComponentOf :Skid12`.

**Optional local wording.** The team’s glossary uses “assembly component of” for A.14 `ComponentOf`, with the component first and its containing whole second. It can state “In this assembly glossary, ‘assembly component of’ is an alias of `ut:ComponentOf` as defined in A.14.” This one declaration lets readers recover the relation intended by “PumpA is an assembly component of Skid12.” Whether PumpA actually satisfies that rule is examined in the account below.

Suppose a later inventory glossary widens that phrase to include uninstalled spares reserved for a skid. The earlier alias no longer covers the widened meaning. Keep the assembly meaning explicit or use the inventory’s separately defined reservation relation. PumpA’s existing component claim can remain valid while it stays installed; the label change alone supplies no new assertion about a reserved spare.

* **Publication — Working-Model relation layer.**
  They publish one assertion using the **Working-Model** relation **ComponentOf**, with exact named participants and the relation interpreted under its declared semantics. Those are its relevant expression properties under C.2.3; a universal F rank is unnecessary. The public view presents the Working-Model relation; a reviewer can follow its grounding link.

* **Constructive grounding (Γₘ).**
  In the background, the published assertion links to `:trace_Γₘ_sum_456`, a C.2.1 episteme that names the exact pump and skid, the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain, the applicable skid assembly rule, and the skid reidentification rule. An auditor replays that account to inspect the assertion's basis. The same listed parts under a different assembly can form another whole, while a permitted pump replacement can preserve Skid12; the direct relations and reidentification rule, not the trace or input list, decide.

* **Assurance stance & R-lane.**
Because the assertion is linked to the construction account required by its elected branch, authors set `tv:validationMode=axiomatic`. The account makes the relation's basis inspectable. B.3.3 considers the actual grounding and its currentness for the receiving claim and use.

* **Contrast (epistemic).**
When the same team asserts `:MassFlowRepresentation RepresentationOf :FlowModel`, they declare `validationMode=postulate` and attach a calibration dataset instead of a Γₘ trace. Judge that empirical basis for the claimed representation and receiving use; the declared mode alone does not establish lower confidence. Under B.3.4, a changed configuration, calibration qualification or other relevant premise can reopen the claim. The dataset's age alone does not defeat still-applicable support.

Result: **one** visible relation for engineers, a grounding reference and a validation-mode declaration for reviewers.

**Collection case — Fleet North.** First publish the ordinary sentence: “Vehicle 12 belongs to Fleet North under its registration rule.” Under that rule, the occurrence begins when Fleet North accepts the vehicle's registration, ends on withdrawal or transfer, and a later accepted registration begins another occurrence. If no current publication choice or requirement elects this profile, the direct sentence is sufficient and the author stops.

Here the fleet publication elects the profile. It links the assertion to one current C.13 `Γ_m.set` trace that names Fleet North and its identity rule, Vehicle 12, the obtaining registration occurrence, the registration rule, and its ending and recurrence conditions; it declares `validationMode=axiomatic`. If a vehicle enters or leaves the fleet, or the rule changes, the earlier trace remains an account of its earlier state but is not current support for the later assertion. The register and trace report this registration history. Any separately claimed ComponentOf relation needs its own grounds.

**Epistemic constituent case.** A proof of “the product of consecutive integers is even” uses the lemma “one of the two integers is even.” Inspection of that proof establishes `Lemma A ConstituentOf Proof P`. With no elected B.3.5 profile, the relation can be stated directly. A recipient may still require access to the proof under its own evidence requirement.

If that recipient elects B.3.5 and the basis is the followable argument, link the assertion through `tv:groundedBy` to that argument and choose `inferential`. If a qualifying C.13 account instead explains the proof's independently established constituent relations and assembly, it can supply an `axiomatic` basis. A later proof that omits the lemma requires a fresh content-part judgement; the earlier support remains about Proof P. Select and assess the support for the claim actually being used.

