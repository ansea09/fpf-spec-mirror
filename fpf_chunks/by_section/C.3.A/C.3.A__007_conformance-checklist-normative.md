---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:6"
section_title: "Conformance checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__007_conformance-checklist-normative.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:6 — Conformance checklist (normative)"
line_start: 45760
line_end: 45780
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

### C.3.A:6 - Conformance checklist (normative)

| ID | Requirement |
| --- | --- |
| **GC-01** | A universally quantified claim pins both claim-kind and receiving-kind declaration editions; same-context restriction requires the receiving kind to be identical to or a subkind of the claim kind, while producer/output positions use their own direction. No candidate is invented. |
| **GC-02** | Every claim-to-candidate use pins candidate, claim kind, receiving kind, both needed signature editions, and slice; it evaluates the target receiving judgment and consumes `true`/`false`/`unknown`. |
| **GC-03** | `unknown` and known `false` remain distinct from each other and from guard refusal. |
| **GC-04** | RoleMask use recovers the declaration episteme and exact masked judgment; any MaskAdapter remains a separate declaration. |
| **GC-05** | Cross-context use recovers both bridge channels, the exact target declaration, and a fresh target judgment when a candidate is current; penalties route to R only. |
| **GC-06** | Scope, `Gamma_time`, freshness, type compatibility, classification, and disposition remain separate. |
| **GC-07** | SpanUnion preserves one typed claim and line independence; candidate-specific evidence names exact candidates and judgments. |
| **GC-08** | KindAT appears in no guard, and no plan, row, card, log, or slice substitutes for an actual candidate or Work occurrence. |

#### C.3.A:6.1 - Proven-equivalent aliases

A context-specific guard alias is equivalent only when all required objects, inputs, classification values, bridge distinctions, and disposition boundaries can be recovered. Similar wording or the same final allow/refuse bit is insufficient.

#### C.3.A:6.2 - Bridge consequences

`Phi(CL_scope)` and `Psi(CL_kind)` are monotone non-increasing consequences on the receiving R path under the governing bridge patterns. This Annex prescribes no numeric form. It never performs arithmetic on F or G.

