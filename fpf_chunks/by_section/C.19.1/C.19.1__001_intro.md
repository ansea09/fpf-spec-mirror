---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__001_intro.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:intro — Intro"
line_start: 50402
line_end: 50439
dependencies:
  - "A.0"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.23"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP‑waiver"
  - "Scale‑Audit"
  - "alpha and delta tolerances"
  - "general-solution preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
---

## C.19.1 - Bitter‑Lesson Preference (BLP)

**One-screen purpose (manager-first).**
State the empirical Bitter Lesson narrowly: in search, learning, planning, and related computational work, general methods able to use increasing compute or data have often displaced hand-engineered special cases. Treat that history as a comparison pressure, not as proof about every bearer. A project may declare an analogous preference for a module, platform, organization design, evidence arrangement, or other bearer only as a separate local policy, with a scale predicate, objective vector, comparison basis, and evidence form appropriate to that bearer. Safety, cost, admissibility, uncertainty, and non-dominance remain visible; the word `general` creates no preference by itself.
**Builds on.** C.19 (E and E‑LOG), C.24 (Agent‑Tools‑CAL; **ATC‑2**), B.3 (Assurance), E.3 (Precedence), E.5 (Guard‑Rails).
**Coordinates with.** G.5 (Selector), G.8 (SoS‑LOG Bundles), G.9 (Parity), G.11 (Refresh‑Telemetry), A.0 (On‑Ramp).
**Keywords.** general-solution preference; scale‑amenability; **BLP‑waiver**; iso‑scale parity; **Scale‑Audit**; slope vector; **alpha and delta tolerances**.

**Use this when.**
Use `C.19.1` when a current choice or policy makes a real scale claim: a narrower special-purpose approach is preferred over a general alternative, or a general approach is preferred because its measured performance is expected to improve across a declared scale window. For search, learning, planning, and agent substrates, the empirical Bitter Lesson can supply the motivating line. For a module relation, platform, organization design, evidence-bearing episteme or work arrangement, or selected structure, state explicitly that the move is a local analogy or policy rather than an empirical Bitter-Lesson result.

The pattern governs only that scale-based comparison, preference, or waiver. It neither proves architecture adequacy nor turns a bearer label into a holon kind. If the project is merely using a bounded specialization and makes no scale advantage or durable generality claim, keep the use local under the bearer's direct pattern and stop here.

When `E.23` compares a general adaptive loop with a specialized cycle or direct repair, use `C.19.1` only if the decision relies on scale advantage or a declared generality policy. The `E.23` loop still names the object under improvement, evaluation, cost and risk account, protected trade-offs, and stop or switch condition.

#### C.19.1:0.1 - What Goes Wrong If Missed

A team treats "more agentic", "more automated", "more specialized", or "works on this benchmark" as proof that one bearer should displace a more general scale-amenable bearer. Another team repeats the opposite error: it invokes the Bitter Lesson as permission to ignore safety, cost, task-family fit, or a narrow heuristic that actually wins inside the declared scale window. In both cases, the selector loses parity, waiver, and scale-window discipline.

#### C.19.1:0.2 - What This Buys

The practitioner gets a cheap first probe before an expensive audit. It distinguishes a supported scale comparison, a declared local analogy or policy, a bounded use with no scale claim yet, and a high-stakes claim that justifies a fuller `Scale-Audit`. When comparison proceeds, task family, scale window, parity, uncertainty, cost, safety, and waiver remain explicit.

#### C.19.1:0.3 - Not This Pattern When

Do not use `C.19.1` to prove that an architecture candidate is adequate, declare a selected-set result, make that result available to an audience, run the improvement loop, plan or perform work, or claim a gate decision. Apply the pattern that defines and tests the current question: `C.30` or `C.32` for architecture adequacy and synthesis, `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence and audience availability, `E.23` for object-version improvement, the A.15 family for work, and `A.21` for gate decisions.

#### C.19.1:0.4 - First Output

Run one cheap scale-claim probe before selecting any `Scale-Audit`. In a short note, name the two bearer candidates and their direct patterns, the task family or receiving use, the proposed scale predicate, objective vector, comparison basis, feasible evidence form, safety boundary, and stakes. Return one of four results:

- `no scale claim yet`: use the bounded candidate under its direct pattern; no BLP preference or waiver follows;
- `local analogy or policy`: identify the non-computational bearer family, policy edition, and bearer-appropriate evidence still needed;
- `bounded scale comparison`: state the smallest parity and uncertainty method adequate for this use;
- `full Scale-Audit selected`: state why the claim, stakes, feasible evidence, and receiving use justify the added work.

A `BLP-waiver` is needed only when an actual declared generality preference would otherwise decide the use.

