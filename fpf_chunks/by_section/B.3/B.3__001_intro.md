---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust & Assurance Calculus (F–G–R with Congruence)"
section_id: "B.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__001_intro.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "B.3 — Trust & Assurance Calculus (F–G–R with Congruence)"
  - "B.3:intro — Intro"
line_start: 30965
line_end: 30977
dependencies:
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
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

## B.3 - Trust & Assurance Calculus (F–G–R with Congruence)

> **Plain‑English headline.**
> B.3 defines how **assurance** (trust) is **computed and propagated** for both physical systems and epistemes and their carriers, using a small **typed assurance tuple** (**F–G–R**: **F/R** characteristics plus **G** as scope object) and **conservative aggregation rules** that respect the Γ‑invariants and A.7 **EntityOfConcern/Description strict distinction**. It treats the **E.14 Working‑Model layer** as the publication-facing assertion layer for claims, with assurance **attached downward** (Mapping - Logical - Constructive - Empirical) per E.14.

**Use this when.** Use `B.3` when a claim, label, dashboard, evidence bundle, model, report, or gate-decision or assurance-input package is being used to raise assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for a named claim.
**First output.** One typed `Assurance(H, C \| K, S)` claim per named assurance claim `C`, or an explicit no-assurance-claim disposition when the encountered publication face, carrier, rendering, or cue is only a cue, evidence pointer, wording issue, gate decision, role assertion, status assertion, commitment, or work occurrence.
**Not this pattern when.** Not when the item is only a cue, action invitation, boundary wording, evidence question, currentness question, gate decision, release decision, role assertion, status assertion, commitment, or work occurrence; use `A.15`, `A.6`, `A.10`, `A.21`, `A.20`, `A.2.1`, `A.2.8`, `A.2.9`, or `A.15.1` as appropriate.

**Assurance result selection.** Use the lightest assurance result that can decide the live assurance use. A cue or source pointer gets no B.3 tuple. A local, non-release, non-compliance, non-safety, non-reused claim may be written as a compact bounded assurance claim statement that names claim, assurance use carried by the assurance tuple or relying context, evidence pointer, limit, and stop/reopen condition. Reserve a full typed `Assurance(H, C \| K, S)` claim for readiness, compliance, safety, release confidence, trust, `F`, `G`, `R`, `CL`, or reused assurance input.

**Continuous assurance state.** Treat an assurance claim as an engineering-process state that can decay, reopen, narrow, or be withdrawn, not as a one-time checklist result. For model, data, AI, documentation, release, or operational assurance, name the drift, monitoring, incident, evidence-refresh, version-change, policy/gate-change, or residual non-admissible-use condition that reopens the assurance claim.

