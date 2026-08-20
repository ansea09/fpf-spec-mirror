---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
section_id: "A.6.S:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__009_conformance-checklist.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.S — U.SignatureEngineeringPair - Signature engineering via a ConstructorSignature and a TargetSignature"
  - "A.6.S:7 — Conformance Checklist"
line_start: 20938
line_end: 20950
dependencies:
  - "A.12"
  - "A.3"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.19"
keywords:
  - "ConstructorSignature"
  - "EFEM"
  - "MVPK views (no new semantics)"
  - "TargetSignature"
  - "appear"
  - "claim register"
  - "editioning"
  - "no epistemic agency"
  - "quadrant classification is governed by A.6.B)"
  - "retargeting"
  - "signature engineering"
  - "slot/base change lexicon"
  - "two-signature arrangement"
---

### A.6.S:7 - Conformance Checklist

|             ID | Requirement                                                                                                                                                                                                                                                               | Purpose                                                               |
| -------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **CC‑A.6.S‑1** | A conforming boundary description **SHALL** identify a **TargetSignature** and (when the boundary is being actively constructed or evolved) a **ConstructorSignature** that describes how the TargetSignature is produced and revised.                                     | Prevents conflating the TargetSignature with the ConstructorSignature engineering work. |
| **CC‑A.6.S‑2** | The ConstructorSignature **SHALL** use (or explicitly relate its terms to) the canonical **slot operation verbs** from A.6.5 and the **base-change lexicon** from A.6.6 (`declareBase`, `rebase`, `rescope`, `retime`, …). It **MUST NOT** use umbrella metaphors (for example, `anchor*`) or “bind/binding” as substitutes for explicit baseRelation/base-change talk, and it **MUST NOT** collapse distinct meanings (for example, using “edit” for both by-value updates and ref retargeting). Source- or project-specific shorthands MAY exist, but each has an explicit relation to the canonical verb class and is registered only when the receiving use needs durable reuse. | Keeps change semantics explicit and reviewable. |
| **CC‑A.6.S‑3** | Any TargetSignature change that alters TargetSignature meaning **SHALL** mint a **new TargetSignature edition** and downstream references **SHALL** be updated via explicit **ref retargeting** (A.6.5), not by silent in‑place mutation. Use A.6.4 retargeting only when `EntityOfConcernRef` changes under a `KindBridge`. | Makes semantic evolution explicit without confusing editioning with described‑entity retargeting. |
| **CC‑A.6.S‑4** | If MVPK is used, each published face (`U.View`) **SHALL** be constructed as a **view** of the canonical L/A/D/E-classified claim set and **MUST NOT** introduce new semantic commitments. `AssuranceLane` MAY add procedural adjudication guidance and evidence pointers, but any normative criteria MUST be stated as canonical `E-*` claims and be cited by ID. | Prevents parallel Contract Bundles or rival canonical claim sets emerging from views.                    |
| **CC‑A.6.S‑5** | Claims about laws, admissibility, deontics, and work evidence **SHALL** be classified using A.6.B’s quadrant discipline and (where used) recorded with stable claim IDs in a claim register.                                                                                  | Prevents quadrant mixing in contract prose.                           |
| **CC‑A.6.S‑6** | The TargetSignature **SHALL NOT** contain operational gate predicates or deontic obligations; such constraints belong to mechanisms and agent norms respectively (A.6.1, A.6.B).                                                                                         | Preserves the signature/mechanism boundary.                           |
| **CC-A.6.S-7** | Constructor operations described by the ConstructorSignature SHALL be expressible as effect-free epistemic morphisms (A.6.2). For each EFEM constructor operation family, the ConstructorSignature MUST declare `entityOfConcernChangeMode` and its C.2.1 value-and-relation read/change profile. Any step that performs measurements, actuation, validation runs, or other side effects MUST be modeled as Work or Mechanism application and cannot be a constructor operation. | Prevents smuggling mechanisms or Work into signature editing. |
| **CC‑A.6.S‑8** | Any concrete change to a TargetSignature edition or its MVPK faces **SHALL** be represented as Work performed by an admitted System, with A.10 evidence and E.17 publication relations where current. It **SHALL** satisfy F.6 for every performer; a short boundary account may omit an assignment identifier not used by its receiving claim. Normative text **MUST NOT** ascribe agency to the signature, local system-role kind, or assignment. | Aligns no-epistemic-agency with current System, Work, assignment, evidence, and publication discipline. |

