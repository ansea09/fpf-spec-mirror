---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__008_conformance-checklist-normative.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:7 — Conformance Checklist (normative)"
line_start: 13264
line_end: 13276
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:7 - Conformance Checklist (normative)

| ID                                                  | Requirement                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC-EFEM.1 (Typed episteme objects).** | Every morphism advertised as `U.EffectFreeEpistemicMorphing` SHALL have exact domain and codomain epistemes whose C.2.1 claim content, EntityOfConcern, and effective ReferenceScheme are recoverable. The declaration names which of those values and which separately obtaining relations it reads or changes. A.6.5 SlotSpecs are required only for an exact reusable relation declaration and remain local to that declaration. |
| **CC‑EFEM.2 (Declared EntityOfConcernChangeMode).** | Each EFEM **species** SHALL declare the `EntityOfConcernChangeMode` characteristic `entityOfConcernChangeMode : EpMorphism -> {preserve, retarget}` as per C.2.1. For every instance `f`, `entityOfConcernChangeMode(f)` MUST be either `preserve` (=> `entityOfConcernRef` unchanged) or `retarget` (=> a KindBridge and invariant are explicitly named; see A.6.4 / F.9).                                                                                         |
| **CC‑EFEM.3 (Purity).**                             | EFEM morphisms SHALL be effect‑free: they MUST NOT directly perform Work or run mechanisms with operational guards; they only read input epistemes and construct output epistemes consistent with P2–P5. Any use of external solvers/measurements MUST be modelled as separate Mechanisms/Work that feed new epistemes into EFEM.                                                                     |
| **CC‑EFEM.4 (Conservativity).**                     | Laws for EFEM species SHALL state their conservativity regime: claims in the output MUST be logical consequences of input claims under declared ReferenceSchemes and any CorrespondenceModels/KindBridges. If an operation may strengthen claims (e.g. add commitments not entailed by inputs), it is **not** EFEM and MUST be modelled separately.                                                   |
| **CC‑EFEM.5 (Functoriality & idempotence).**        | EFEM species SHALL satisfy identity and composition with the usual category laws, and SHALL specify any structural equivalence under which idempotence holds. Non‑deterministic or order‑sensitive behaviour (beyond declared structural equivalences) is non‑conformant.                                                                                                                             |
| **CC‑EFEM.6 (Applicability and scope).** | Each EFEM species SHALL state the allowed EntityOfConcern kinds, grounding, effective schemes, claim scopes, operating conditions, and any optional describing-use viewpoint on which its operation actually depends. Applying EFEM outside those conditions is non-conformant. An actual cross-local or cross-plane use MUST name the exact F.9 or plane relation and any A.6.1 transport; no universal context object or automatic Bridge is inferred. |
| **CC‑EFEM.7 (Description and specification-use discipline).** | For any `...Description` or `...Spec` episteme, identify exact E and its EntityOfConcern under C.2.1; admit specification use only under E.10.D2; and state whether claim content, EntityOfConcern, grounding, effective scheme, and every material use qualification are preserved or changed. A viewpoint is named only for the describing use that selects it, and selection establishes neither identity nor E.17.0 conformance. |
| **CC-EFEM.8 (Value-and-relation read/change declaration).** | Any EFEM species SHALL declare its morphism family and change mode, name the C.2.1 values it reads or changes, and state its behavior on EntityOfConcern, claim content, and effective scheme. It SHALL separately state any empirical-grounding, representation, conformance, or describing-use viewpoint relation it reads or changes rather than treating that relation as episteme identity. |

