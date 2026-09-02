---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__011_rationale.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:10 — Rationale"
line_start: 13866
line_end: 13886
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

### A.6.2:10 - Rationale

**Why a separate EFEM pattern (A.6.2) instead of folding into A.6.1 or C.2.1?**

* A.6.1 defines Mechanism declarations and their separately identified applications, including operational guards and time conditions. A.6.2 instead defines a local mathematical arrow class. Any semantic Bridge, plane relation, transport application, or Work remains under its direct pattern.
* C.2.1 fixes episteme identity through claim content, exact EntityOfConcern, and effective ReferenceScheme and keeps neighboring direct relations separate, but does not define morphisms. EFEM is a morphism-level pattern over those values and relations.

This split mirrors how A.6.0 separates a declaration from what later uses it: C.2.1 says what an episteme is; A.6.2 states the laws of a local episteme-to-episteme arrow family; A.6.1 and A.15 govern any application and Work.

**Why insist on EntityOfConcernChangeMode?**

Because a relation can look like a harmless view even though its endpoint epistemes concern different entities—for example, component assembly and function bundle. Declaring `preserve` versus `retarget` exposes that endpoint distinction. It does not make the arrow fit for a use; the separate assertion must state the invariant, visible loss, bounded use, conditions, support, and polarity.

**Why name actual values and exact relation reads instead of informal fields?**

FPF distinguishes actual participants and their references from the declaration-local SlotKinds used in a reusable `RelationSignature`. Reusing that distinction here:

* aligns episteme morphisms with the framework's direct-relation architecture;
* enables checks that an EFEM species compared only the three declared endpoint values, read only the named neighboring occurrences, and left any actual relation change to its direct pattern and producing application or Work;
* avoids minting another generic parameter, field, or relation-role vocabulary.

