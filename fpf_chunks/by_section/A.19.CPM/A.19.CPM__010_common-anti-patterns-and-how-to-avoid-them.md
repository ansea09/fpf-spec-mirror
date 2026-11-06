---
chunk_kind: "child"
pattern_id: "A.19.CPM"
pattern_title: "Compare Admitted Profiles under a Declared Comparator (CPM)"
section_id: "A.19.CPM:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CPM/A.19.CPM__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "A.19.CPM — Compare Admitted Profiles under a Declared Comparator (CPM)"
  - "A.19.CPM:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 39062
line_end: 39103
dependencies:
keywords:
  - "ComparatorSet"
  - "ComparatorSpecRef"
  - "comparator"
  - "comparison"
  - "partial order"
  - "set-valued comparison outcome"
  - "tri-state admissibility (pass"
---

### A.19.CPM:8 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern: “Comparison returns a score.”**
  *Symptom:* `Compare(x,y)` returns a numeric margin or a single rank position.
  *Avoid:* keep numeric scoring in `USCM`; CPM returns relation tokens (set‑valued). If a numeric comparator is desired, it must be an explicit `ComparatorSpec` and still yields relation tokens as the kernel output.

* **Anti‑pattern: “CPM picks the winner.”**
  *Symptom:* comparison logic embeds winner selection or selected-set truncation.
  *Avoid:* CPM only compares; selection is `SelectorMechanism`, which consumes comparison outcomes and remains policy‑bound.

* **Anti-pattern: Implicit comparator choice.**
  *Symptom:* comparator choice is implicit (e.g., “we usually do lexicographic by safety then cost”), not edition‑pinned.
  *Avoid:* require an explicit `ComparatorSpecRef` from `CG-Spec.ComparatorSet`; the actual `Compare` application binds the effective edition.

* **Anti‑pattern: “GateDecision leakage.”**
  *Symptom:* the `compare` step emits or assumes GateDecision, GateLog, or DecisionLog records as part of suite closure, or uses reserved gate‑lexemes (`…Guard`) for mechanism‑level predicates.
  *Avoid:* keep `CompareEligibility` as the mechanism-level tri-state predicate and assign gate decisions to their governing pattern.

* **Anti‑pattern: “SlotKind drift.”**
  *Symptom:* renaming or re‑purposing `LeftProfileSlot`, `RightProfileSlot`, `ComparatorSpecSlot`, or `ComparisonResultSlot` across specializations or across CHR layers.
  *Avoid:* use the suite SlotKind lexicon (`A.19.CHR:4.2.1`) and keep SlotIndex as a derived projection.

* **Anti‑pattern: “Smuggling plan‑binding into CPM.”**
  *Symptom:* hard‑coding comparator editions, policy ids, or “launch values” inside the CPM intension or pattern prose.
  *Avoid:* resolve the intended editions and policies, recording them in A.15.2 on a P2W path; use A.15.3 typed filling only for independently declared positions. Establish actual Compare bindings under §4.1.

* **Anti‑pattern: “Tie‑breakers as hidden constants.”**
  *Symptom:* forced total order via untracked thresholds, epsilons, or “if equal then compare cost” logic.
  *Avoid:* make tie-break policy part of explicit comparator and acceptance policies, pin their editions, and keep their effective use in the actual `Compare` application recoverable.

* **Anti‑pattern: “Unknown coerces to outcome.”**
  *Symptom:* missing evidence treated as equal, zero, or worse, producing decisive comparisons from absent information.
  *Avoid:* tri‑state guard; fail‑closed on missing evidence; explicit failure behavior via evidence policy.

* **Anti-pattern: `ComparisonResultSlot` as a replay record.**
  *Symptom:* comparator, scope, predicate, window, evidence, or currentness fields are placed inside the set-valued output.
  *Avoid:* keep the output to relation or poset tokens; recover effective arguments from the actual operation application and direct neighboring relations.

* **Anti-pattern: Using one F.9 Bridge rule for both semantic and ReferencePlane crossings.**
  *Symptom:* an F.9 Bridge is required merely because reference schemes or planes differ; the separate C.2.1 bounded-use claim is absent; or `CL` and a bare `R_eff` penalty are treated as mandatory.
  *Avoid:* cite an obtaining F.9 Bridge and separate bounded-use claim only for the semantic branch; cite the applicable ReferencePlane relation and policy for the plane branch; state both when both facts are current. Make only actually consumed refs recoverable for the actual `Compare` application. Add `CL` only when needed. Open B.3 only for an actual named assurance claim, and use a local `R_eff` only if its declared domain model and calculation define it. Use A.2.4 for evidence-use classification and A.10 when the bounded source-to-use account must remain replayable; the direct crossing patterns establish their relations.

