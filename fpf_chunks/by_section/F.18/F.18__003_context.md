---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__003_context.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:1 — Context"
line_start: 92996
line_end: 93015
dependencies:
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:1 - Context

Names are handles for use, not creators of ontology. A good name lets people talk about a governed value without smuggling in extra role, capability, method, work, status, evidence, interface, or cross-context claims.

`FPFCoreReferenceScheme` is the by-value `U.ReferenceScheme` used to interpret current FPF Core Tech labels and relation names. A NameCard that uses it carries that reference-scheme value by value, consistent with `C.2.1`; F.18 does not introduce `U.ReferenceSchemeRef`. A name interpreted under another reference scheme carries that scheme by value. When a naming use must align two local senses, first identify each sense under its by-value reference scheme; name a `BoundedModelUseStructure` only when that selected structure changes the sense or the admitted use. Use `F.9` only if its current entry can take those two senses as endpoints and its result states the naming use that survives. Until then, keep the names local or record the unresolved alignment. A reference-scheme or model-use-structure difference alone supplies neither a Bridge nor governed-value identity, and it does not create `U.BoundedContext`.

`F.18` supplies the naming discipline for Part F and for any FPF pattern that needs a durable public term. It coordinates with:

- `F.5` for type-name and role-description label form;
- `F.8` for the prior decision that an expression should become a durable name rather than remain local, reused, or aliased;
- `F.9` for an actual cross-context sense Bridge;
- `F.13` for renames, aliases, splits, and merges;
- `F.14` for anti-explosion control;
- `F.17` only as a later public-row consumer whose current entry and result must accept the exact F.18 objects named below;
- `A.6.5` and `A.6.RSIR` when relation, signature, interface, slot, or role wording hides the governed object; `A.6.P.WMR` when work/method-boundary wording still hides the exact relation; and `A.15.1` when a candidate performed-work name still lacks occurrence grounding.

The central subject is one `F.18` naming settlement for one exact already-governed value. `F.18` governs the candidate comparison, selected Tech and Plain designations, declared naming use, and reopen conditions. The value's direct pattern still governs its kind, identity, obtaining, and other subject semantics.

Its complete claim graph records the selected designation expressions, exact local sense, covered and rejected alternatives, rationale, lineage, and reopen condition.

