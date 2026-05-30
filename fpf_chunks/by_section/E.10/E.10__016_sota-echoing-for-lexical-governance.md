---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:11a"
section_title: "SoTA-Echoing for lexical governance"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__016_sota-echoing-for-lexical-governance.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:11a — SoTA-Echoing for lexical governance"
line_start: 57552
line_end: 57563
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.22"
  - "E.23"
  - "E.5"
  - "F.18"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:11a - SoTA-Echoing for lexical governance

E.10 lexical governance is not a private FPF style preference. It is a compact authoring discipline for communication, comprehension, term formation, and error prevention. These external practice rows are admitted only where they change what an author or reviewer does in a live wording repair.

| Practice basis | Source posture | What E.10 adopts | What E.10 rejects |
| --- | --- | --- | --- |
| ISO 704:2022 and ISO 1087:2019 terminology work on concepts, definitions, designations, and term formation. | Current-standard/reference-only for terminology work; official status does not make it complete SoTA for FPF semantic repair. | Use explicit designation and definition discipline when a term is minted, repaired, or made reusable. Keep the head kind, context, and intended use recoverable. | Do not solve FPF wording by dictionary substitution, synonym stuffing, or global alias registry. Do not turn every term into a class hierarchy. |
| Human-readable identifier and label clarity practice in software and HCI work. | Current practice signal for comprehension and error prevention; accepted only where it changes local naming or replacement wording. | Treat names as comprehension and error-prevention aids, not as cosmetic polish. Use clear local names only when they preserve the same FPF kind and relation. | Do not let a nicer label change kind, scope, authority, or downstream use. Do not accept readability as proof that the term is semantically safe. |
| Ontology and controlled-vocabulary practice. | Rationale and exact-neighbour source posture; specialized ontology work belongs in the receiving ontology, naming, relation, or domain pattern when live. | Use exact modeling only when the current problem really needs it, and then make the modeled kind and relation explicit. | Do not make OWL-style term-to-class modeling the default answer to every vague term. E.10 repairs wording first and applies `F.18`, `A.6.P`, or a domain pattern only when that heavier modeling move is live. |
| Documentation-search and entry vocabulary practice. | Current source-use pressure for retrieval/discoverability, carried locally through `J.4`, `E.11`, and entry/projection neighbours rather than by a separate E.10 search ontology. | Keep lexical triggers discoverable enough for the first repair, but make final wording and receiving-pattern application govern the result. | Do not turn trigger lists into local lexical registries, front-door taxonomies, or accepted replacement vocabulary. |

The practical result is simple: lexical governance must improve action guidance and semantic composability, not become language-police work. A SoTA row that does not change a rewrite, a forbidden shortcut, an exact governing-pattern application, or a conformance check remains decorative and does not carry E.10.
