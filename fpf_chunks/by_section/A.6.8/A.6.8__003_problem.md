---
chunk_kind: "child"
pattern_id: "A.6.8"
pattern_title: "Service Polysemy Unpacking (RPR‑SERV)"
section_id: "A.6.8:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.8/A.6.8__003_problem.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.6.8 — Service Polysemy Unpacking (RPR‑SERV)"
  - "A.6.8:2 — Problem"
line_start: 17223
line_end: 17234
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

### A.6.8:2 - Problem

Unqualified “service” in normative prose causes **referent ambiguity** that cannot be repaired by reader intuition, because the ambiguity is structural:

1. **Addressability mismatch:** you can *call/visit* an access point, but you cannot call a clause.
2. **Type mismatch:** work/telemetry/incidents are properties of **work + carriers**, not of promise content.
3. **Deontic mismatch:** “must/shall/guarantee” binds **actors/roles** via commitments, not abstract clauses.
4. **Speech‑act mismatch:** “promise/offer/accept” are **events/acts**, not the promise content itself.
5. **Evolution mismatch:** changing an API endpoint or deployment is not “changing the service” unless you declare which facet changed and narrate that change with stable change classes.

Result: readers can’t apply A.6.B routing, and engineers are incentivized to preserve ambiguity (“service” as a convenient metonym) because it avoids committing to a model.

