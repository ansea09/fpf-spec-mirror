---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__003_problem.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:2 — Problem"
line_start: 72293
line_end: 72305
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

### G.Core:2 - Problem

Without one governing definition for Part‑G‑wide invariants, Part G drifts in at least six recurring ways:

1. **Shadow governing spec refs** emerge: downstream patterns restate CN‑Spec / CG‑Spec constraints, accidentally creating “local specs” that can diverge from the canonical governing spec refs.
2. **Crossing discipline becomes inconsistent**: “crossing events” and “crossing visibility” are described differently across `G.x`, causing ambiguity about what must be pinned (UTS/Path/policy‑ids/editions) and what triggers refresh/regression.
3. **Guard semantics drift**: tri‑state eligibility and “unknown handling” can be reinterpreted in local prose, producing hidden fourth statuses or implicit coercions.
4. **Hidden scalarization appears**: partial orders are silently collapsed into scalars, or totalization is introduced implicitly through “helpful” numeric summaries.
5. **Suite/kit/pack mixing blurs governing-definition assignment**: downstream patterns drift into “governing” what should remain governed by the suite boundary (`A.6.7` and `A.19.CHR`), kit surfaces (each `G.x`), or shipping (`G.10`).
6. **Refactoring breaks public IDs**: CC items and trigger labels become hard to evolve because removing duplicates risks breaking external references.

Part G requires a single place where these invariants and refactoring disciplines live, while keeping Part G patterns modular and method/discipline specifics explicitly separated.

