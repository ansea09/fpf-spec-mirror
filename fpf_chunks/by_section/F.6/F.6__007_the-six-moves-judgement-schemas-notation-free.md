---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "Role Assignment & Enactment Cycle (Six-Step)"
section_id: "F.6:6"
section_title: "The six moves (judgement schemas, notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__007_the-six-moves-judgement-schemas-notation-free.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "F.6 — Role Assignment & Enactment Cycle (Six-Step)"
  - "F.6:6 — The six moves (judgement schemas, notation‑free)"
line_start: 63142
line_end: 63203
dependencies:
  - "A.15"
  - "A.2.1"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:6 - The six moves (judgement schemas, notation‑free)

Each move is a **thought you can justify**, expressed as `premises ⊢ conclusion`.
All moves are **context-local** and **side-effect free**: they assert knowledge; they do not modify the project entities they describe.

#### F.6:6.1 - M1 - Locate — *Fix the Context and the Template*

**Form.**
`Template τ anchored at SenseCell σ≡⟨C, ℓ⟩ ⊢ address(τ) = σ`

**Reading.** Name the Context and the exact SenseCell that gives **local meaning** to the Template.
**Note.** This forbids “floating” Roles or Statuses and prevents Context drift.

#### F.6:6.2 - M2 - Stance — *Respect DesignRunTag*

**Form.**
`stance(C)=s ∧ stance(τ)∈{s, both} ⊢ compatible_stance(τ,C)`

**Reading.** The Template’s DesignRunTag is **compatible** with its Context’s stance (design vs run).
**Note.** Guards against judging a design-mask by run-traces or judging a run-status by design-time descriptions.

#### F.6:6.3 - M3 - Qualify — *Check Holder eligibility*

**Form.**
`Holder H ∧ eligibility(τ) holds in C ⊢ eligible(H, τ @ C)`

**Reading.** Given the Template’s eligibility predicates (F.4), the Holder qualifies to be bound/assessed **in this Context**.
**Note.** Typical predicates: **type membership**, **capability present**, **scope fit**; all context‑local.

#### F.6:6.4 - M4 - Bind/Assert — *Make the Role Assignment / Status claim*

**Role assignment (behavioural mask).**
`eligible(H, τ @ C) ∧ window W ⊢ plays_role(H, τ : C) @ W`

**Status assertion (epistemic/deontic state).**
`eligible(H, τ @ C) ∧ window W ∧ S = subject_of(τ, H) ⊢ has_status(S, τ : C) @ W`

**Reading.** Assert either a **Role** binding or a **Status** about the appropriate subject (system, artefact, service), within a **Window**.
**Note.** The **subject** of a Status may differ from the Role holder (e.g., a *service* has SLO status; a *team* plays a Role).

#### F.6:6.5 - M5 - Evidence — *Shape what would make it true/false*

**Form.**
`plays_role/has_status κ in C ⊢ evidence_shape(κ) = Σ(C)`

**Reading.** From the Context’s semantics, state the **Observation/Result** pattern (KD‑CAL) that would confirm or refute the claim (**what**, **where**, **when**).
**Note.** This is not an execution plan: it is a **conceptual test** tied to the Context’s vocabulary.

#### F.6:6.6 - M6 - Conclude — *Issue a defensible verdict with confidence*

**Form.**
`evidence E fits Σ(C) ∧ invariants(τ) hold ⊢ holds(κ) with confidence γ ∈ [0,1]`

**Reading.** If observed facts match the expected evidence shape and Template invariants stand, the assignment/status claim **holds** with some confidence (cf. B.3).
**Note.** Confidence combines measurement adequacy (KD‑CAL) with any Context‑specific uncertainty; no Cross‑context boost is implied.

#### F.6:6.7 - Autonomy admission (Green‑Gate) and ledger
* **Before enactment:** If the Method step lists `requiresAutonomyBudget`, the enacting `U.RoleAssignment` **MUST** pass the **Autonomy Green‑Gate**: (i) active/enactable RSG state, (ii) budget tokens/envelope remain in the declared **Γ_time** window, (iii) all guards `pass`.
* **On enactment:** Write an **AutonomyLedgerEntry** attached to the `U.Work`, with deltas and guard verdicts.
* **On depletion:** Block further autonomy‑gated steps; emit a **DepletionNotice** (SpeechAct) and follow the `OverrideProtocolRef`.
* **SoD:** Enforce `⊥` between autonomy consumer Role and override caller Role.

