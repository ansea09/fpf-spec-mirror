---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:11.7"
section_title: "SoTA-Echoing - lexical governance"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__021_sota-echoing-lexical-governance.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:11.7 — SoTA-Echoing - lexical governance"
line_start: 64099
line_end: 64111
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
keywords:
---

### E.10:11.7 - SoTA-Echoing - lexical governance

E.10 lexical governance is not a private FPF style preference. It is a compact authoring discipline for communication, comprehension, term formation, discoverability, and error prevention. These external practice rows are admitted only where they change what an author or reviewer does in a wording repair.

| Practice source | Use of source and source-currentness claim | What E.10 adopts | What E.10 rejects |
| --- | --- | --- | --- |
| ISO 704:2022 and ISO 1087:2019 terminology work on concepts, definitions, designations, and term formation. | Current-standard and reference-only for terminology work; official status does not make it complete SoTA for FPF semantic repair. | Mutates `E.10:0.2`, `E.10:0.2a`, and `E.10:11`: use explicit designation and definition discipline when a term is minted, repaired, or made reusable; keep head kind, context, and intended use recoverable. | Do not solve FPF wording by dictionary substitution, synonym stuffing, or global alias registry. Do not turn every term into a class hierarchy. |
| ISO 9241-110:2020 interaction principles and W3C WCAG 2.2 Understanding SC 2.4.6, 3.2.4, and 3.3.2 on descriptive headings and labels, consistent identification, and visible labels and instructions. | Current-standard and reference plus current practice anchor for comprehension, task suitability, predictable identification, and error prevention. | Mutates `E.10:0.2a`, `E.10:0.2c.15`, `E.10:0.2c.28`, and `E.10:11`: require a repair to preserve the remaining reader use, usable local label, and predictable repeated label; treat label clarity as a usability constraint after kind recovery. | Do not accept readability, friendliness, or a nicer label as proof that the term is semantically safe. Do not let a label change kind, scope, authority, or downstream use. |
| W3C SKOS Reference for controlled structured vocabularies and lexical labels, with heavier OWL and RDF ontology practice used only by ontology-bearing patterns named by value. | Current reference source for controlled-vocabulary publication and label relations; not current-best source for every FPF wording repair. | Mutates `E.10:0.2b`, `E.10:0.2c.18`, and `E.10:0.2c.28`: keep vocabulary labels, concept-like heads, registries, maps, and reusable names recoverable as publication or naming objects named by value before reuse; durable naming remains governed by `F.18`, while relation, source, or domain ontology remains governed by the pattern carrying that claim. | Do not make OWL-style term-to-class modeling the default answer to every vague term. Do not let a controlled vocabulary become a second FPF ontology or replacement wording-recognition table. |
| W3C WCAG 2.2 headings and labels guidance plus consistent-identification guidance, with FPF-internal `E.11`, README, ToC, and `I.2` entry-distribution practice. | Current reference source for discoverability and label consistency; FPF entry projection remains the governing local architecture. | Mutates `E.10:0.2b`, `E.10:0.2c.29`, `E.10:12`, and `E.11` coordination: keep trigger wording discoverable enough for first repair, but make final wording, governing-pattern application, and entry projection govern the result. | Do not turn wording-recognition lists into local lexical registries, front-door taxonomies, or accepted replacement vocabulary. Do not let search convenience select ontology. |

The practical result is simple: lexical governance must improve action guidance and semantic composability, not become language-police work. A SoTA row that does not change a rewrite, a forbidden shortcut, a governing-pattern application, a conformance prompt, or a reopen cue remains decorative and does not carry E.10.

