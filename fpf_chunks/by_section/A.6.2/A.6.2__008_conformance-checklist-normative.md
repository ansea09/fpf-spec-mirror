---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__008_conformance-checklist-normative.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:7 — Conformance Checklist (normative)"
line_start: 13828
line_end: 13840
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:7 - Conformance Checklist (normative)

| ID                                                  | Requirement                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC-EFEM.1 (Typed episteme objects).** | Every arrow presented as an effect-free episteme morphism SHALL have exact domain and codomain epistemes whose C.2.1 claim content, EntityOfConcern, and effective ReferenceScheme are recoverable. The FormalSubstrate declaration names which of those three values it uses and which exact separately obtaining relation occurrences its rule reads or compares. Reading or comparing an occurrence neither changes it nor makes it obtain or cease. A.6.5 SlotSpecs are required only for an exact reusable relation declaration and remain local to that declaration. |
| **CC‑EFEM.2 (Derived EntityOfConcernChangeMode).** | Each arrow family declares `entityOfConcernChangeMode : EpMorphism -> {preserve, retarget}` and derives each arrow's value from its resolved endpoint EntitiesOfConcern: `preserve` for the same exact entity, `retarget` for independently different entities. A named subtype may restrict one value but is closed under composition only when every admitted composite still meets that restriction. Any assertion that the arrow supports one use remains a separate A.6.4 q. An F.9 Bridge is additional only for a separate local-sense relation. |
| **CC‑EFEM.3 (Purity).** | An EFEM arrow SHALL assert no Work, mechanism execution, or carrier mutation. If a system constructs or changes an episteme, identify the exact application, bindings, system, Work, and resulting episteme separately; the arrow may then relate the exact epistemes under P2–P5. |
| **CC‑EFEM.4 (Conservativity).** | Each arrow family states which of the three endpoint identity values and which ClaimGraph parts remain the same or differ under the declared schemes and arrow-family conditions. A claim that one arrow supports a receiving use remains separate and states its use-specific invariant, visible loss, conditions, support, and polarity. An arrow declaration does not make unsupported output commitments valid. |
| **CC‑EFEM.5 (Category structure and repeat claims).** | Each arrow family names its exact endpoints, arrow rule or designator, declared equivalence, identity and composition conditions. Claim category `Ep` and mapping `α` only when identities and every matching composition close. The resolved endpoint EntitiesOfConcern uniquely determine the thin-base arrow `α(f)`, but they do not identify f itself. A retargeting round trip maps to the thin-base identity and is reclassified from its final endpoints. Idempotence or another repeat claim is added only for an endomorphism whose declared domain makes composition meaningful, with its equivalence and witness stated. Any evaluation operation, deterministic-execution claim, or repeat claim about an operation application is separate and follows that operation's rule. |
| **CC‑EFEM.6 (Formal domain and separate use conditions).** | Each arrow family SHALL state its allowed endpoint EntityOfConcern kinds, any endpoint facts or grounding relations its formal rule reads, admitted schemes and correspondences, and any ClaimScope constraint required by the arrow law. A use-specific scope, operating condition, selected viewpoint, invariant, visible loss, support, and polarity remain in the separate use assertion. When the use also relies on an obtaining Bridge between two exact F.17 local senses, cite F.9 and its separate bounded-use claim; when it crosses a ReferencePlane, cite the applicable plane relation. No context, scheme, plane, or operating-condition difference creates either relation automatically. |
| **CC‑EFEM.7 (Description and specification-use discipline).** | For any `...Description` or `...Spec` episteme, identify exact E and its EntityOfConcern under C.2.1; admit specification use only under E.10.D2; and state which endpoint claim content, EntityOfConcern, and effective scheme are preserved or differ. Name any grounding occurrence and describing-use viewpoint qualification separately and compare only the facts the rule actually reads. The arrow changes neither occurrence; viewpoint selection establishes neither identity nor E.17.0 conformance. |
| **CC-EFEM.8 (Endpoint-value and relation-read declaration).** | Any EFEM species SHALL declare its morphism family and change mode and compare the three C.2.1 endpoint identity values. It SHALL name every empirical-grounding, representation, or conformance occurrence and every describing-use viewpoint qualification that its rule reads, together with the endpoint facts compared. The arrow neither changes those occurrences nor makes them obtain or cease. Any actual relation change remains under its direct pattern and any producing activity under its exact application and Work. |

