---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:13"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__015_conformance-checklist.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:13 — Conformance Checklist"
line_start: 45314
line_end: 45330
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
---

### C.3.2:13 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C32-1` | Local kind, `KindSignature` episteme, exact four-input judgment, and optional extension representation are separately recoverable. |
| `CC-C32-2` | The signature's exact EntityOfConcern is the local kind, and its content names candidate domain, criterion, slice conditions, reference scheme, assumptions, dependencies, formality, and any current extent rule. |
| `CC-C32-3` | Formality characterizes the declaration episteme only. |
| `CC-C32-4` | Direct governed candidate features make the criterion hold or fail; evidence supports an assertion and does not create membership. |
| `CC-C32-5` | Missing evidence, unavailable dependency, or out-of-domain input yields `unknown`, distinct from known `false`. |
| `CC-C32-6` | No A.14 `MemberOf`, `U.EntitySet`, collection holon, or direct classification occurrence is inferred from the judgment or extension. |
| `CC-C32-7` | Any separate classification assertion is a C.2.1 episteme and creates neither candidate nor kind; a value classification need not fabricate a value-shaped EntityOfConcern. |
| `CC-C32-8` | Subkind monotonicity is tested over defined judgments for the same candidate and slice; counterexamples repair links, editions, or bridges rather than extension rows. |
| `CC-C32-9` | Bounded-context crossing, signature-edition change within one context, C.3.1 kind continuity, candidate-state change, slice change, and extension change remain distinct. |
| `CC-C32-10` | The kind carries no scope; the context slice is an evaluation input, and declaration/assertion scopes stay on their own epistemes. |
| `CC-C32-11` | The five required cases and the `U.Work`/W/episteme distinction all close under the same four-object architecture. |
| `CC-C32-12` | Ordinary use stays readable, and reusable declarations or extensions have named receiving uses. |

