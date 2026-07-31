---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__004_forces.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:3 — Forces"
line_start: 95442
line_end: 95451
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:3 - Forces

* **One governing definition vs. usability:** We must centralize universal invariants, but `G.x` must remain readable and pattern-scoped for authors.
* **Delegation-first vs. completeness:** Many norms already have canonical governing definitions such as `A.6.7`, `A.15.3`, `A.19`, `G.0`, `A.19.CHR`, and the relevant Part E patterns. `G.Core` must cite those governing definitions rather than duplicating semantics.
* **Public-id and alias continuity:** Public CC IDs and deprecated trigger labels must remain stable as labels; deduplication must not break citations.
* **Typed change control:** RSCR/refresh must become *id‑based* (catalogued trigger kinds) rather than prose-based “meaning”.
* **Strict distinction:** Keep governing spec refs (CN‑Spec, CG‑Spec), suites, kits/surfaces, policies, planned baselines, audits, and refresh orchestration distinct.
* **Minimal specificity naming:** New IDs must be kind‑suffixed and minimally specific, to reduce semantic lock‑in while remaining precise.
* **Phase‑2 scope discipline:** `G.Core` must not become a container for discipline/method/generator taxonomies; those remain pattern-scoped (`Extensions`), delegated to existing governing patterns, or marked Phase‑3 seeds (appendix) without new Phase‑2 norms.

