---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__007_archetypal-grounding.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:5 — Archetypal Grounding"
line_start: 17489
line_end: 17508
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3.4.P"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "RelationSignature"
  - "SlotSpec"
  - "ambiguous role wording"
  - "direct relation participant"
  - "interface"
  - "operation declaration and binding"
  - "participant meaning"
  - "port"
  - "reduced-use source label"
  - "relation-signature-interface-role-slot recovery"
  - "representation position"
  - "system-role assignment"
  - "system-role kind"
---

### A.6.RSIR:5 - Archetypal Grounding

**System case: module interface claim.** A team says "the cooling module exposes the heat-exchanger interface." RSIR first asks what claim is current. If the claim is substitutability or separate change, use `A.6.M`. If a reusable relation declaration for exchanged-medium and boundary-condition participant meanings is current, use `A.6.0` plus `A.6.5` for the `RelationSignature` and complete `SlotSpec`s. If the current use is a diagram, API schema, or other representation, keep its positions under `C.29` or the exact representation pattern and state explicit correspondence. If the claim is a functional port in a transformation-flow structure, use `A.6.F`, `A.3.4`, and `E.18`. RSIR does not create `U.Interface`.

**Bare-role case: API provider wording.** A source says “the API role is provider.” Apply `E.10.ROLE` once. If it recovers a provider System, local `ProviderSystemRole` kind, assignment, capability, provider Work, promise, access relation, publication, or another direct object, apply that object's rule and do not apply RSIR. Apply RSIR only when the still-unanswered question is the participant meaning in a direct relation, a reusable declaration, an interface claim, an operation declaration or binding, or an API-schema representation position. For protocol, service-term, SLA, or agreement-like wording that bundles several claims, use A.6.C to unpack the claims before stating each object or relation. Use A.6.M only for a module-interface claim and A.6.B only for boundary-package statement classification. Do not assign a system role to the API description.

**Evidence case: reviewer and report wording.** A report says “reviewer evidence role approved the gate.” Apply `E.10.ROLE` once and split the claims. Apply A.2/A.2.1 for any exact reviewer system-role kind or assignment, A.10/B.3/F.10/E.17 for the evidence use, A.21 for the gate decision, and A.2.9 for any issuing speech act. None of those recovered branches needs RSIR unless a separate direct-participation, reusable-declaration, interface, operation, or representation-position question remains. No episteme receives a system-role assignment by being evidence.

**Slot case: method parameter.** A method description says "parameter target controls the model." That sentence has no exact governor in this case, so it is not retained as the repaired claim; keep `target` only as a reduced-use source label and write one positive A.6.1 use instead. In the current `recognizeAdmittedHolonCandidate` declaration, `candidate` is an `ArgumentDeclaration` meaning one exact entity being evaluated, with `ValueKind = U.Entity`; `recognitionJudgment` is the declared result meaning. Under A.6.1, the project independently identifies the bounded recognition-evaluation invocation `P-37` by that declaration's application predicate, identity rule, and extent rule. During `P-37`, Pump #37 is actually bound under `candidate`, and the returned value `unknown` is bound under `recognitionJudgment`. In a call representation such as `recognizeAdmittedHolonCandidate(target = Pump-37, ...)`, the named-argument position `target` corresponds to the declared `candidate` meaning but is neither the declaration nor either binding. The practitioner writes: "`target` is the call label; A.6.1 declares `candidate : U.Entity`; during exact application `P-37`, Pump #37 is bound as candidate." Stop there unless the receiving claim needs the result binding or another subject pattern.

#### A.6.RSIR:5.1 - Near-Miss Checks

| Source phrase | Positive recovery | Near miss to reject |
|---|---|---|
| “API role is provider” | Apply `E.10.ROLE` once. If it recovers `ProviderSystemRole`, an exact assignment, provider Work, API publication, promise, access relation, or another direct object, apply that object's rule and leave RSIR closed. Apply A.6.RSIR only for a remaining declaration, direct-participation, interface, operation, or representation-position question; use A.6.C only when protocol, SLA, service-term, or agreement-like wording bundles unlike claims. | Do not assign a system role to an API description or protocol, and do not repeat the E.10.ROLE recovery inside RSIR. |
| "endpoint parameter source" | Use the direct relation pattern when the phrase hides a participant meaning or actual participant; use `A.6.5` only for a complete `SlotSpec` in a current reusable `RelationSignature`; use `A.6.1` when it names an operation `ArgumentDeclaration`, `ResultDeclaration`, or an actual binding in one independently identified exact application; use `C.29` or `E.17` when it is a representation position or API description, and `A.6.P:4.11a` when a service-documentation label hides the concrete subject or relation; state explicit correspondence whenever the FPF claim consumes the representation. | Do not create an endpoint kind, a work-facing role from the word "source", a parameter ontology, a public application kind, a universal input/output relation, or a world-side participant or binding from representation shape. |
| “`Engineer-7#Verifier:Lab-A`” | Recover `Engineer-7` as the holder System, `VerifierSystemRole` as the local kind, and both the assignment occurrence and its declared `U.SystemRoleAssignment` species. In this case `Lab-A` is the facility System in which verification Work occurs; state that Work relation separately when claimed. | Do not put `Lab-A` into assignment identity or keep `Holder#Role:Context` as normative ontology. |
| "function of the pump" | `A.6.F`, `A.3.4`, `E.18`, or `C.30.TFS-REL` when the phrase names functional structure; `A.2.2` when it names a system capability. | Do not treat "function" as the recovered kind before the current claim is known. |
| “standard evidence role” | Apply `E.10.ROLE` once, then use A.10, B.3, F.10, or E.17 for the recovered evidence, source, status, assurance, or publication claim. Leave RSIR closed unless a separate direct-participation, declaration, interface, operation, or representation-position question remains. | Do not invent `U.EvidenceRole` or put the standard episteme into `U.SystemRoleAssignment`. |

