---
chunk_kind: "child"
pattern_id: "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
pattern_title: "Declared-Substrate Interpretive View"
section_id: "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW/A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW__016_rationale.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW — Declared-Substrate Interpretive View"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:10 — Rationale"
line_start: 29933
line_end: 29949
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.6.3"
  - "A.6.P"
  - "C.19"
  - "C.24"
  - "E.17"
  - "E.17.0"
  - "G.10"
  - "G.2"
  - "G.5"
keywords:
  - "DeclaredSubstrateAtlasView"
  - "DeclaredSubstrateInterpretiveView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas-form interpretation"
  - "declared-substrate interpretive view"
  - "interpretive qualifiers"
  - "interpretive-only reading"
  - "thin interpretation"
---

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:10 - Rationale

The family needs one common interpretive-view pattern because neither of the earlier extremes is good enough.

If everything stays in the substrate, the substrate starts carrying interpretive and atlas-form requirements that are not part of its semantic center.

If everything stays inside one local specialization such as `G.2`, the common interpretive requirement gets trapped inside one tradition-facing case and starts looking like a local accident rather than a reusable family.

`A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` is the middle answer:

- it keeps the interpretive layer generic and reusable;
- it keeps the layer explicitly under existing view law;
- it lets ordinary thinner interpretive views remain first-class;
- and it reserves atlas-form reading for the cases that truly need it.

That is why `DeclaredSubstrateAtlasView` appears here as one richer interpretive specialization, while `TraditionAtlasView` remains one `G.2` specialization of it rather than the common head.

