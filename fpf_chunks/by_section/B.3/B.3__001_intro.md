---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__001_intro.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:intro — Intro"
line_start: 38548
line_end: 38570
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

## B.3 - Trust and Assurance Calculus (F-G-R with Congruence)

> **Type:** Foundational (B)
> **Status:** Stable
> **Normativity:** Normative for FPF use that claims assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for a named claim.

> **Plain-English headline.**
> B.3 defines how assurance or trust is assigned, aggregated, and reused for physical systems, epistemes, and publication or evidence records that are used to claim assurance. It uses one typed assurance tuple, F-G-R: `F` and `R` as characteristics, `G` as the scope value, plus edge-scoped `CL`; the aggregation rules stay conservative, respect the current composition, transformation, temporal, and work invariants named by their governing patterns, and keep the A.7 EntityOfConcern and description strict distinction. It treats the E.14 Working-Model layer as the publication-facing assertion layer for claims, with assurance inputs attached downward from Mapping, Logical, Constructive, and Empirical Validation layers.

**Use this when.** Use `B.3` when a claim, label, dashboard, evidence bundle, model, report, gate decision, or assurance-input package is being used to raise assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for a named claim.

**What goes wrong if missed.** Labels, dashboards, model cards, credentials, provenance marks, gate decisions, or evidence bundles start raising trust or readiness without one typed assurance claim, named evidence, scope, limitations, decay, and relying context.

**What this buys.** Assurance becomes a conservative typed claim over `F`, `G`, `R`, and edge-scoped `CL`, with explicit evidence, scope, time, limitations, contestability, and stop or reopen conditions.

**First output.** Write one typed `Assurance(H, C | K, S)` claim per named assurance claim `C`, or write an explicit no-assurance-claim disposition when the encountered publication face, rendering, cue, evidence pointer, wording issue, gate decision, role assertion, status-value assertion, commitment, or work occurrence does not carry an assurance claim.

**Not this pattern when.** If the encountered source or publication face is only a cue, action invitation, boundary wording, evidence question, currentness question, gate decision, release decision, role assertion, status-value assertion, commitment, or work occurrence, use `A.15`, `A.6`, `A.10`, `A.21`, `A.20`, `A.2.1`, `A.2.8`, `A.2.9`, or `A.15.1` as appropriate.

**Assurance result selection.** Use the lightest assurance result that can decide the assurance use being claimed. A cue or source pointer gets no B.3 tuple. A local, non-release, non-compliance, non-safety, non-reused claim may be written as a compact bounded assurance claim statement that names claim, assurance use carried by the assurance tuple or relying context, evidence pointer, limit, and stop or reopen condition. Reserve a full typed `Assurance(H, C | K, S)` claim for readiness, compliance, safety, release confidence, trust, `F`, `G`, `R`, `CL`, or reused assurance input.

**Assurance claim over time.** Treat an assurance claim as time-bounded and updateable: it can decay, reopen, narrow, or be withdrawn, not remain a one-time checklist result. For model, data, AI, documentation, release, or operational assurance, name the drift, monitoring, incident, evidence refresh, version change, policy change, gate change, or residual unsupported-use condition that reopens the assurance claim.

