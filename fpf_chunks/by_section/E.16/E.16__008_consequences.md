---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__008_consequences.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:7 — Consequences"
line_start: 76800
line_end: 76841
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

### E.16:7 - Consequences

* **Testability.** Autonomy is measurable (tokens/envelopes), audit‑ready (ledger), and stoppable (SpeechActs).
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

#### E.16:7.1 - SoTA‑Echoing (post‑2015 practice alignment)

> Each item states **Adopt / Adapt / Reject**, and why. Vendor/tool tokens are kept as *informative*, not normative.

1. **Corrigibility & safe interruptibility (2016→).**
   **Adopt/Adapt.** Work on safe interruption and “off‑switch” incentives argues that capable systems should remain *stoppable* and should not be rewarded for resisting oversight (Orseau & Armstrong, 2016; Hadfield‑Menell et al., 2017). E.16 adapts this into canonical **PauseAutonomy / ResumeAutonomy** SpeechActs plus **SoD** and *hard* gating on depletion.

2. **AI safety as concrete operational hazards (2016→).**
   **Adopt.** “Concrete Problems in AI Safety” pushes instrumentation and testable safety constraints over informal assurances (Amodei et al., 2016). E.16 mirrors this by turning “autonomy” into a **budget + ledger + guards** specification that can be benchmarked and audited.

3. **SRE error budgets & “stop the line” operations (2016→).**
   **Adopt/Adapt.** Error‑budget practice treats reliability as a measurable envelope that gates risky change when depleted (Beyer et al., *Site Reliability Engineering*, 2016; Höller et al., *The Site Reliability Workbook*, 2018). E.16 adapts the idea into `risk_bands` and depletion behavior that blocks autonomy‑gated steps until governed resume.

4. **Risk management frameworks for AI systems (2023→).**
   **Adopt/Adapt.** Contemporary risk frameworks emphasize governance, continuous measurement, and traceable controls (NIST AI RMF 1.0, 2023; ISO/IEC 23894, 2023). E.16 adapts these into **UTS publication** + **Work‑anchored ledger evidence** for parity and audit.

5. **Policy‑as‑code and provenance gating (2019→).**
   **Adopt.** Modern supply‑chain integrity systems emphasize *policy‑checked actions with verifiable provenance* (in‑toto, 2019→; SLSA, 2021→). E.16 echoes the same principle for autonomy: **no autonomy‑gated enactment without passing declared guards and emitting ledger evidence** (without importing any specific tooling).

6. **Scaling laws & the Bitter Lesson (2019→).**
   **Adapt/Reject.** Empirical scaling work and the Bitter Lesson motivate considering compute‑heavy search when returns are monotonic (Sutton, 2019; Kaplan et al., 2020). E.16 adapts this into an **optional** ScaleLensPolicy (E.16‑S7) constrained by the *same* budgets and guards, and **rejects** any interpretation that lets “scale” bypass safety gates.

7. **Budgeted specialist acquisition and checkpointed exploitation (2024→).**
   **Adopt/Adapt.** Recent agentic tool-use, self-play, and open-ended search lines reinforce that the competition variable is time or budget to threshold plus fast exploitation after a viable route is found. E.16 adapts this into distinct scout/probe/commit control surfaces and rejects any reading where early probe success authorizes rollout without an explicit checkpoint.

#### E.16:7.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Autonomy-by-label** | “Autonomous” is claimed but there is no `AutonomyBudgetDecl` or ledger | Autonomy becomes opaque; cannot be audited or compared | Require **E.16‑S1/S3**; reject publication without `AutonomyBudgetDeclRef` + version |
| **Soft gates** | Budget/guards only warn; enactment proceeds anyway | Violates Safety and SoD; makes budgets non-enforceable | Make Green‑Gate **blocking** on Core surface (**E.16‑S2**) |
| **Self‑override** | Same RoleAssignment consumes the budget and calls Resume/Narrow | Conflict of interest; SoD collapse | Enforce `⊥` between consumer and overrider (**E.16‑S4**) |
| **Budget bypass via “scale”** | Scaling preference relaxes guards or ignores caps | Undermines declared limits; breaks comparability | In ScaleLensPolicy, **guards/SoD must remain non‑weakened** (**E.16‑S7**) |
| **Untyped quotas** | Tokens/caps are recorded without units, or units are mixed | Ledger becomes non-comparable; audits become meaningless | Type budgets and deltas via **MM‑CHR (C.16)**; keep unitful rates/quotas |
| **Ledger-as-logging** | Logs exist but are not Work‑anchored (no workId/budgetId/version/pins) | Evidence is non-portable; cannot support parity/refresh | Require `AutonomyLedgerEntry` attached to `U.Work` with ids, versions, and edition pins |

