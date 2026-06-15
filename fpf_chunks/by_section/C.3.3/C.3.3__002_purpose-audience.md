---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:1"
section_title: "Purpose & Audience"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__002_purpose-audience.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:1 — Purpose & Audience"
line_start: 39942
line_end: 39950
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
keywords:
  - "CL^k"
  - "KindBridge"
  - "R penalty"
  - "cross-context mapping"
  - "type-congruence"
---

### C.3.3:1 - Purpose & Audience

Cross‑context reuse fails in two **orthogonal** ways:

1. **Applicability** (G): *where* the claim holds (handled by USM Scope Bridge).
2. **entityOfConcern** (Kind): *what* the claim quantifies over (handled by **KindBridge**).

**C.3.3** gives managers an explicit, auditable channel for **(2)**, so a team can say, with evidence: *“`Vehicle` in Lab maps to `TransportUnit` in Plant with `CL^k=2`; the EV subkind collapses; here’s what we lost.”* Guards stay deterministic; assurance math stays clean (penalties in **R** only).

