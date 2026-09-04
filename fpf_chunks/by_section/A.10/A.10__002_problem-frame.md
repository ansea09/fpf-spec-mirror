---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__002_problem-frame.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:1 — Problem frame"
line_start: 22641
line_end: 22658
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.19"
  - "A.2-family"
  - "A.2.4"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "G.11"
  - "G.4"
keywords:
  - "RelianceDisposition"
  - "actual-use relation"
  - "bounded use"
  - "carrier"
  - "claim/result episteme"
  - "currentness"
  - "dated work"
  - "direct relation"
  - "evidence-provenance path"
  - "relied-on claim"
  - "rival explanation"
  - "source publication"
  - "unsupported overread"
---

### A.10:1 - Problem frame

Use this pattern when a source, carrier, result episteme, credential, dashboard, provenance label, generated explanation, model card, or review note is being relied on for a named claim or bounded action and the source-to-use account is still implicit.

**Primary EntityOfConcern.** The live object is the exact relied-on claim and bounded use. A.10 builds a descriptive evidence-provenance path that represents the independently established sources, carriers, work, result epistemes, provenance relations, currentness, and later-use relations needed to judge that use. The path is not a new world-side relation and its edges establish none of the facts they cite.

**First useful move.** Write: “Claim episteme `E` is being relied on for bounded use `U`; `E` states local result `R`; the cited sources, carriers, and direct relations are `S`; currentness is `T`; the bounded A.10 disposition is `D`.” Add a dated `U.Work` occurrence only when that Work is itself a current claim. If the account says that Work returned, produced, or obtained a value, name the exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject relation under its own pattern; otherwise keep the Work and value as separate facts. Mark any missing rule or relation as a gap.

**What goes wrong if missed.** Carrier presence becomes truth, provenance becomes approval, a result record becomes performed work, MethodDescription becomes a run trace, a graph edge becomes an obtaining relation, and a currentness or assurance decision is inferred from display styling.

**What this buys.** A source-to-use account that can be replayed, contested, refreshed, narrowed, or handed to the pattern that defines or tests an additional claim, while keeping the claim, carrier, performed work, local result, result episteme, provenance, currentness, reliance, assurance, and action distinct.

**Not this pattern when.** A.10 does not establish measurement, formal, causal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, Work, or decision results. It does not establish representation correspondences. Use the pattern that defines or tests each result, A.15.1 and A.6.1 for performed Work and actual bindings, C.2.1 for the result episteme, G.11 for currentness, C.29 for representation, and B.3 only when an actual named assurance claim is current.

Use A.2.4 first when only the first evidence-use or status-use classification of an episteme is at issue. Enter A.10 when carrier identity, source recovery, provenance, currentness, rival explanations, or bounded reliance must remain replayable.

Here `path` means a path in a descriptive evidence/provenance graph, never a route of action or a universal evidence relation.

