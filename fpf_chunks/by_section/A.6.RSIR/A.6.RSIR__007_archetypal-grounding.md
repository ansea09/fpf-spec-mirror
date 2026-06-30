---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__007_archetypal-grounding.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:5 — Archetypal Grounding"
line_start: 14661
line_end: 14680
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.0"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "C.2.P"
  - "C.2.P.DR"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "affordance"
  - "capability"
  - "concern"
  - "endpoint"
  - "field"
  - "function"
  - "interest"
  - "interface wording"
  - "method"
  - "parameter"
  - "port"
  - "protocol"
  - "relation-signature-interface-role-slot recovery"
  - "role wording"
  - "shadow ontology"
  - "slot wording"
---

### A.6.RSIR:5 - Archetypal Grounding

**System case: module interface claim.** A team says "the cooling module exposes the heat-exchanger interface." RSIR first asks what claim is current. If the claim is substitutability or separate change, use `A.6.M`. If the claim is only a signature declaration for the exchanged medium and boundary conditions, use `A.6.0` plus `A.6.5`. If the claim is a functional port in a transformation-flow structure, use `A.6.F`, `A.3.4`, and `E.18`. RSIR does not create `U.Interface`.

**Role case: API provider role.** A source says "the API role is provider." RSIR splits the project concern. If "provider" is a work-facing role, recover `ProviderRole`, a `U.RoleAssignment`, `HolderSlot`, bounded context, and assignment window. If the API is a publication or protocol description, use `E.17` for publication and `A.6.8` or `A.6.C` for service, protocol, SLA, or agreement-like boundary wording. If a provider or consumer commitment is current, use `A.2.3` or `A.6.C`; if module-interface semantics are current, use `A.6.M`; if boundary-package statement classification is current, use `A.6.B`. Do not assign a work role to the API description.

**Evidence case: reviewer evidence role.** A report says "reviewer evidence role approved the gate." RSIR blocks the composite. A reviewer may be a role value assigned to a system or acting holon under `A.2` and `A.2.1`. A report episteme may be used in an evidence-use relation under `A.10`, `B.3`, `F.10`, or `E.17`. A gate approval may be a gate decision under `A.21` or a speech-act case under `A.2.9`. No episteme gets a work role by being evidence.

**Slot case: method parameter.** A method description says "parameter target controls the model." RSIR asks whether `target` is a source label, a SlotKind, a ValueKind, or the EntityOfConcern named by the claim. If it is a declared argument position, use `A.6.5` and name `TargetSlot`, ValueKind, and refMode. If it is a method requirement or work input, use method or work patterns.

#### A.6.RSIR:5.1 - Near-Miss Checks

| Source phrase | Positive recovery | Near miss to reject |
|---|---|---|
| "API role is provider" | `ProviderRole` and `U.RoleAssignment` when a team or system participates in work; `E.17`, `A.6.8`, or `A.6.C` when the API phrase names a publication, protocol, SLA, service-access, or agreement-like claim. | Do not assign a work-facing role to the API description or protocol itself. |
| "endpoint parameter source" | `A.6.5` when source is a relation-position SlotKind in a signature or relation; `E.17` or `A.6.8` when it is API or service documentation language. | Do not create an endpoint kind, a work-facing role from the word "source", or a parameter ontology by source wording alone. |
| "`Engineer#Verifier:Lab`" | `A.2.1`, `A.15`, and `A.6.5` when the old notation means holder, role value, bounded context, assignment window, or assignment SlotSpecs. | Do not keep `Holder#Role:Context` as the normative ontology or let it hide holder, role value, context, and window slots. |
| "function of the pump" | `A.6.F`, `A.3.4`, `E.18`, or `C.30.TFS-REL` when the phrase names functional structure; `A.2.2` when it names a system capability. | Do not treat "function" as the recovered kind before the current claim is known. |
| "standard evidence role" | `A.10`, `B.3`, `F.10`, or `E.17` when a standard episteme is used as evidence, source, status, or publication. | Do not keep `U.EvidenceRole` or put the standard episteme into `U.RoleAssignment`. |

