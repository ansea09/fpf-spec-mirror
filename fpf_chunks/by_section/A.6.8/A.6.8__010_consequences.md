---
chunk_kind: "child"
pattern_id: "A.6.8"
pattern_title: "Service Polysemy Unpacking (RPR‑SERV)"
section_id: "A.6.8:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.8/A.6.8__010_consequences.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "A.6.8 — Service Polysemy Unpacking (RPR‑SERV)"
  - "A.6.8:9 — Consequences"
line_start: 20125
line_end: 20143
dependencies:
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.9"
  - "A.6.5"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "C.26.1"
  - "C.26.3"
  - "E.10"
  - "E.15"
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "API read/export"
  - "boundary exchange"
  - "interface semantics"
  - "promise content"
  - "provider principal"
  - "service polysemy"
  - "service situation"
  - "service/cell analogy"
  - "viability envelope"
---

### A.6.8:9 - Consequences

* **Pros:**

  * Removes the incentive to keep “service” conveniently vague.
  * Enables A.6.B routing: clause (L), commitment (D), acts/work/evidence (E), mechanisms/interfaces (A/L depending on placement).
  * Makes incident/SLO/SLA discourse structurally sound and reviewable.

* **Cons:**

  * Increases verbosity and requires refactoring existing prose.
  * Requires authors to learn (and consistently apply) facet headwords.

**Adoption test (1 minute).**
After refactoring any normative section that contains ≥ 10 occurrences of the “service” cluster, you can answer “yes” to all of:
1) Unqualified head‑noun “service” occurrences in normative prose are **0** (CC‑A.6.8‑1).
2) Every deontic (“must/shall/guarantee/SLA”) sentence about service delivery references a **service commitment** / `U.Commitment` (CC‑A.6.8‑4).
3) Every runtime/telemetry “service is down/slow/…” claim is routed to **work + evidence** and, when relevant, distinguishes access‑point symptoms from delivery‑system symptoms (CC‑A.6.8‑6 + §4.7).

