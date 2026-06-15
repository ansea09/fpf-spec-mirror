---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__002_intent.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:1 — Intent"
line_start: 45333
line_end: 45354
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:1 - Intent

Operationalise No-Free-Lunch discipline in selection by making every run-time decision against a **typed TaskSignature (S2)**, not a paragraph. A problem reaches `C.22` when its problem-side representation is stable enough for a selector-facing typed attachment record; a task or work target is ready for selection only when that attachment can be made to a declared `TaskKind`, task family, or work target without pre-binding a method. Method absence, method contestability, or method-family ambiguity is a common practical cue for this transition, but it is not the ontology of problemhood. The signature is the **smallest CHR-typed set** sufficient to drive **Eligibility -> Acceptance -> policy-governed selection** without inadmissible arithmetic or silent coercions; crossings are reviewable (Bridge+CL -> **R_eff only**).

#### C.22:1.1 - Term split used in this pattern

- `TaskSignature` attachment means attaching one typed problem record to one declared task family or work target; it does **not** pre-bind a method.
- `ScopeSlice(G)` means the claim-bounding scope cut over `EntityOfConcernRef` and scope; it is not an evidence-path slice and not a baseline-set slice.
- `threshold` is not one undifferentiated family here:
  - articulation and closure thresholds stay with cue or prompt governing patterns such as `B.4.1` and `B.5.2.0`
  - acceptance-gate thresholds stay with `G.4`
  - the work-measure threshold target used in specialization claims is only the declared success mark for the current task family or work target
#### C.22:1.2 - ProblemCard@Context relation

`ProblemCard@Context` is the `C.22.2`-problem-side record-side record shape for stabilizing one context-bound problem representation before downstream Principles-to-Work (P2W).

A `ProblemCard@Context` record can be used to prepare `ProblemProfile`, `TaskKind`, or candidate `TaskSignature` material for later use. Binding to one `TaskSignature` is admissible only when the downstream selector-facing object is ready. If several downstream signatures remain plausible, keep them as candidate signatures rather than binding one chosen `TaskSignature`.

This relation does not move problem-card fields into `TaskSignature`. `TaskSignature` remains the minimal `C.22` attachment record for eligibility, acceptance, and selection. `ProblemCard@Context` remains the reviewable problem-side record that carries the reason this problem, in this context, can proceed to P2W, characterization, comparison, search, refresh, retirement, or another governing pattern.

The corresponding claims are governed by their named governing patterns.

