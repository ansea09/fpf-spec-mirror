---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:6"
section_title: "Archetypal Grounding - Running example"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__008_archetypal-grounding-running-example.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:6 — Archetypal Grounding - Running example"
line_start: 47596
line_end: 47631
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:6 - Archetypal Grounding - Running example

> **Story.** A refinery team publishes `:PumpA ut:ComponentOf :Skid12`.

**Optional local wording.** The team’s glossary uses “assembly component of” for A.14 `ComponentOf`, with the component first and its containing whole second. It can state “In this assembly glossary, ‘assembly component of’ is an alias of `ut:ComponentOf` as defined in A.14.” This one declaration lets readers recover the relation intended by “PumpA is an assembly component of Skid12.” Whether PumpA satisfies that rule is examined in the account below.

Suppose a later inventory glossary widens that phrase to include uninstalled spares reserved for a skid. The earlier alias no longer covers the widened meaning. Keep the assembly meaning explicit or use the inventory’s separately defined reservation relation. PumpA’s existing component claim can remain valid while it stays installed; the label change alone supplies no new assertion about a reserved spare.

* **Publication — Working-Model relation layer.**
  They publish one assertion using the **Working-Model** relation **ComponentOf**, with named participants and the relation interpreted under its declared semantics. Those are its relevant expression properties under C.2.3; a universal F rank is unnecessary. The public view presents the Working-Model relation; a reviewer can follow its grounding link.

* **Constructive grounding (Γₘ).**
  In the background, the published assertion links to `:trace_Γₘ_sum_456`, a C.2.1 episteme that names the pump and skid, the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain, the applicable skid assembly rule, and the skid reidentification rule. An auditor replays that account to inspect the assertion's basis.

  The same listed parts under a different assembly can form another whole, while a permitted pump replacement can preserve Skid12; the relations and reidentification rule, not the trace or input list, decide. If both installed equipment and its next service are in question, identify the service obligation separately. Two configurations with the same installed pump can require different service under their operating conditions or agreements. Select the additional relation on which the service decision depends. The pump-to-skid assertion alone can finish a request confined to installation.

* **Assurance stance & R-lane.**
Because the assertion is linked to the construction account required by its elected branch, authors set `tv:validationMode=axiomatic`. The account makes the relation's basis inspectable. B.3.3 considers the grounding and its currentness for the receiving claim and use.

* **Contrast (epistemic).**
When the same team asserts `:MassFlowRepresentation RepresentationOf :FlowModel`, they declare `validationMode=postulate` and attach a calibration dataset instead of a Γₘ trace. Judge that empirical basis for the claimed representation and receiving use; the declared mode alone does not establish lower confidence. Under B.3.4, a changed configuration, calibration qualification or other relevant premise can reopen the claim. The dataset's age alone does not defeat still-applicable support.

Result: **one** visible relation for engineers, a grounding reference and a validation-mode declaration for reviewers.

**Collection case — Fleet North.** Consider a reader asking whether Vehicle 12 belongs to Fleet North. Under this fleet’s rule, the occurrence begins when the fleet accepts the vehicle’s registration, ends on withdrawal or transfer, and a later accepted registration begins another occurrence. State the membership supported for the date in question. This can finish the membership inquiry when no profile or further evidence has been requested.

Here the fleet publication elects the profile. It links the assertion to one current C.13 `Γ_m.set` trace that names Fleet North and its identity rule, Vehicle 12, the obtaining registration occurrence, the registration rule, and its ending and recurrence conditions; it declares `validationMode=axiomatic`.

An authoritative roster can establish membership on a given date when its meaning and coverage are known. To reconstruct membership from events, consider later accepted registrations as well as withdrawals and transfers. A question about the continuity of the original registration depends on its own ending conditions. A change involving another vehicle may affect a complete roster while leaving the grounds for Vehicle 12 sufficient. A replacement rule can preserve Vehicle 12’s eligibility or change it. If the use needs the full current roster, establish coverage of entries and exits under that rule. The elected trace must be current for the assertion it grounds. Preserve the earlier trace for the earlier state and establish any separately claimed component relation under its own rule.

**Epistemic constituent case.** In this proof, one of two consecutive integers is even, so their product contains a factor of two and is even. The premise about the even integer occurs in the inference to the conclusion. Inspection of this derivation establishes that the premise is a constituent of the argument. A reference to a separate proof of that premise establishes that the writer cited the proof. To identify the separate proof as a subargument, establish where its reasoning enters this derivation. With no elected B.3.5 profile, state the relation that holds. The recipient may still require access to the proof.

If that recipient elects B.3.5 and the basis is the followable argument, link the assertion through `tv:groundedBy` to that argument and choose `inferential`. If a qualifying C.13 account instead explains the proof's independently established constituent relations and assembly, it can supply an `axiomatic` basis.

A later proof that omits the lemma requires a content-part judgement; the earlier support remains about Proof P. Select and assess the support for the claim being used.

