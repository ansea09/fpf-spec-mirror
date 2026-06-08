---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping (Evidence • Standard • Requirement)"
section_id: "F.10:11"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__012_worked-examples.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.10 — Status Families Mapping (Evidence • Standard • Requirement)"
  - "F.10:11 — Worked examples"
line_start: 72654
line_end: 72720
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:11 - Worked examples

> Each example names **Contexts**, shows **StatusCells** on their native ladders, and draws **only the Bridges that F.10 allows**.

#### F.10:11.1 - Service acceptance from run‑time evidence

**Contexts.** *SOSA/SSN (2017)* — sensing; *ITIL 4 (2020)* — services; *ODRL 2.2* — deontics (optional).

**Local statuses.**

* `SOSA:Observation(uptime)` → **EvidenceStatus: Measured**, Window **July**.
* `ITIL:SLO("99.9% monthly")` → **RequirementStatus** Target = clause *SLO‑99.9*, Window **July**.
* `ITIL:Practice("Monitoring pipeline")` → **StandardStatus: Approved** (design‑time).

**Bridges.**

* **Interpretation**: `Measured(uptime@July)` **→ᴍᴇᵃ** `SLO‑99.9` (kind = ⊑, CL = 2, Loss: sampling bias, clock skew).
* **Evaluation rule** (Service pattern, local to ITIL Context): returns **Satisfied** iff *mean uptime ≥ threshold* across Window.

**Result.** We may **explain** the **Satisfied** conclusion for *SLO‑99.9\@July*; we **do not** assert StandardStatus⇒RequirementStatus. If logs later show outages, a **Violated\@July** replaces **Satisfied\@July** (mutual exclusivity + Window discipline).

#### F.10:11.2 - Safety controller: design approval vs run‑time duty

**Contexts.** *State‑space control texts* — design; *IEC 61131‑3* — run; *Norm‑CAL profile (safety layer)* — deontics.

**Local statuses.**

* `ControllerSpec(v3)` — **StandardStatus: Approved** in the **Norm‑CAL** Context.
* `PLC:Task(log@Q3)` — **EvidenceStatus: Corroborated** for *response time ≤ 50 ms*, Window **Q3**.
* `Duty("Emergency stop ≤ 100 ms")` — **RequirementStatus** clause in Norm‑CAL.

**Bridges.**

* **Interpretation**: `Corroborated(response@Q3)` **→** `Duty` check (kind = ⊑, CL = 2, Loss: sensor latency).

**Result.** The **duty** may be **Satisfied\@Q3** with explanation. *Approved spec* **alone** never yields *Satisfied*; it authorises deployment but does not prove compliance.

#### F.10:11.3 - ML model: validation vs fairness requirement

**Contexts.** *ML validation canon* — DesignRunTag hybrid; *Policy Context (fairness charter)* — deontics; *SOSA/metrics* — sensing.

**Local statuses.**

* `Model v12: cross‑val AUC=0.92` → **EvidenceStatus: Corroborated** (Windows: CV folds).
* `Policy: “Demographic parity Δ ≤ 0.1”` → **RequirementStatus** clause.
* `“Validation SOP v5”` → **StandardStatus: Approved** (governance method).

**Bridges.**

* `Measured(Δ@Aug)` **→ᴍᴇᵃ** `Policy clause` (⊑, CL = 2, Loss: sampling variance).

**Result.** **Satisfied\@Aug** (if Δ≤ 0.1 in production Window) is justifiable. Cross‑val AUC does **not** decide fairness; only **production Δ** does.

#### F.10:11.4 - Medical device log: refutation

**Contexts.** *SOSA/clinical observations*; *Regulatory profile*.

**Local statuses.**

* `Observation: adverse event` → **EvidenceStatus: Observed\@Week 34**.
* `Requirement: “No AE in first 30 days”` → **RequirementStatus** clause.

**Bridge & outcome.**

* Observation **→ Interpretation Bridge** to clause check (**kind: Interpretation**, **CL=3**).
* **Violated\@Week 34** overrides any earlier **Satisfied\@Week 34** (Weakest‑link; same Window).

