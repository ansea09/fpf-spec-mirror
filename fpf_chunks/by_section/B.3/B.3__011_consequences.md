---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__011_consequences.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:9 — Consequences"
line_start: 34262
line_end: 34274
dependencies:
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.3.x"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "D.4"
  - "E.14"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

### B.3:9 - Consequences

**Benefits**

* **Comparable, conservative, improvable.** The tuple ⟨F, G, R⟩ with **edge-scoped Congruence Level (`CL`) values** gives a compact, auditable view that improves monotonically under targeted moves (formalize, replicate, reconcile).
* **Cross-scale coherence.** Works for assemblies and arguments, methods and histories, without leaking order, time, or cost into structure.
* **Clear improvement moves.** It is obvious what to do to raise each component: raise `F`, `G`, or `R` locally, or raise `CL` on the integration edge.

**Trade‑offs**

* **More explicit metadata.** You must state scale kinds, cutsets, and mapping congruence; this is intentional transparency.
* **Conservatism may feel pessimistic.** True synergy appears only via **MHT** or after raising CL—never by arithmetic optimism.

