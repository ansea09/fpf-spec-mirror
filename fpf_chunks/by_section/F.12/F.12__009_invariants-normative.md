---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:8"
section_title: "Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__009_invariants-normative.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:8 — Invariants (normative)"
line_start: 84818
line_end: 84829
dependencies:
  - "A.2.3"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
  - "U.PromiseContent"
keywords:
  - "Service Level Agreement (SLA)"
  - "Service Level Objective (SLO)"
  - "acceptance criteria"
  - "binding"
  - "observation"
---

### F.12:8 - Invariants (normative)

1. **DesignRunTag split.** Clauses live on the **design stance**; judgements live on the **run stance** about **Work** (F.11).
2. **Context locality.** All terms are **context‑local**; Cross‑context meaning flows **only** across declared **Bridges**.
3. **Observation‑only evidence.** Verdicts require **Observations** that **about‑refer** to Work outcomes; **Actuation** and **Approvals** are not sufficient.
4. **Window explicitness.** Every verdict carries a **Window**; no timeless acceptance.
5. **Predicate declared.** The Clause’s **Predicate** is explicit; no hidden aggregation or default percentile.
6. **Non‑retroactivity.** Updating clauses or specs does not alter past verdicts; re‑evaluation must be explicit.
7. **One‑Work focus.** A verdict references a **specific Work** (or a defined population of Works) matched to the Clause’s scope.
8. **Loss honesty.** Each Bridge states **kind**, `CL`, and loss; wider claims require Bridges with the needed `CL` or same-Context alignment.
9. **No detached pass.** When the ClauseCell is a `U.PromiseContent` (service promise clause), `Satisfied` about a Work is admissible only if that Work also **delivers** the promised outcome spec for the clause (A.2.3:8.1 `fulfilsPromiseContent`). This keeps acceptance on the **same delivery evidence base** (Work facts + Δ anchors + Observations) and prevents “pass verdict separate from delivery”.

