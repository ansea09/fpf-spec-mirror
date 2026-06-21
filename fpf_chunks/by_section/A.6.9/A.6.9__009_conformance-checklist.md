---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
section_id: "A.6.9:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__009_conformance-checklist.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.6.9 — Cross-Context Sameness Disambiguation - Repairing cross-context \"same\", \"equivalent\", and \"align\" via explicit Bridges (RPR-XCTX)"
  - "A.6.9:7 — Conformance Checklist"
line_start: 18035
line_end: 18054
dependencies:
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.3.3"
  - "E.10"
  - "E.10.D1"
  - "E.10.U9"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "CL"
  - "SenseCells"
  - "alignment"
  - "bridge"
  - "cross-context sameness"
  - "direction"
  - "loss notes"
  - "mapping"
  - "substitution licence"
  - "weakest-link"
---

### A.6.9:7 - Conformance Checklist

A document or boundary statement conforms to A.6.9 iff:

* **CC‑A.6.9‑0 (UTS/LEX trigger coverage).** The local lexicon treats umbrella‑sameness tokens as RPR triggers and points authors to Bridge‑explicit rewrites.
* **CC‑A.6.9‑1 (No standalone umbrella predicate).** Cross‑Context umbrella tokens SHALL NOT be used as standalone cross‑Context predicates unless either:
  * (a) the paragraph includes an explicit Bridge reference (BridgeId or inline Bridge Card), or
  * (b) the statement is explicitly marked as non‑licensing explanatory prose (“no Bridge licence; do not substitute; do not justify rows”).
* **CC‑A.6.9‑2 (SenseCell endpoints).** Every such claim names endpoints as `σ@Context` (edition‑pinned where relevant), not as strings or system names.
* **CC‑A.6.9‑3 (Direction explicitness).** `dir` is stated on every Bridge. If `kind` is non‑symmetric, any inverse use without redeclaration is non‑conformant.
* **CC‑A.6.9‑4 (Licence separation).** If the intent is explanation only, authors SHALL either (a) declare `scope = Explanation‑only` on a Bridge, or (b) use explicit non‑licensing prose (no Bridge licence). If the intent is naming compatibility, authors SHALL declare a Bridge with `scope = Naming‑only`. In all cases, the text SHALL NOT invite substitution unless a substitution‑eligible Bridge exists.
* **CC‑A.6.9‑5 (Substitution thresholds).** Any statement that implies substitution MUST be backed by a substitution‑eligible Bridge (`kind∈{≈,⊑,⊒}`, `CL≥2`, same `senseFamily`, stance‑compatible), with Loss notes and a counter‑example discipline.
* **CC‑A.6.9‑6 (Weakest‑link respect).** Any Concept‑Set row or composed claim that depends on multiple Bridges MUST bound its scope and `CL` by the weakest participating Bridge.
* **CC‑A.6.9‑7 (Loss visibility).** Loss notes are present and **non‑empty**. `Loss: none` is permitted only for `CL=3` with cited invariants; `Loss: n/a` is permitted for `kind=⊥`. Loss must be consistent with the allowed scope.
* **CC‑A.6.9‑8 (Change narration).** Changes to cross‑Context fit are narrated using the change‑class lexicon (`declare`, `withdraw`, `adjustCL`, `rescope`, and related verbs) rather than umbrella verbs.
* **CC‑A.6.9‑9 (Kind and scope admissibility).** Any Bridge used to justify cross‑Context sameness satisfies the admissibility constraints INV‑XCTX‑KS‑1 … INV‑XCTX‑KS‑5: no overlap-to-substitution, no disjoint or interpretation rows, substitution is directional, and Type-structure only under `≈` + `CL=3` + invariants.
* **CC‑A.6.9‑10 (Registry reference hygiene).** If a BridgeId or policy or edition id is cited, it is treated as a **registry reference** (existence and edition pinning), not as a semantic symbol exported by signatures.
* **CC‑A.6.9‑11 (Edition basis).** In decision or publication lanes, any Bridge used to justify Naming-only, substitution, or Type-structure SHALL state `Γ_time` (edition pins or “as-of” basis). If `Γ_time` cannot be stated, the claim MUST remain Explanation-only and MUST NOT justify rows or substitution.
* **CC‑A.6.9‑12 (Facet honesty).** If the correspondence holds only on a subset of facets, the author SHALL either (a) refine endpoints into the facet SenseCells (preferred) or (b) declare `facetSpan` explicitly, with `Loss` consistent with that facet span. Whole‑cell Bridges MUST NOT be used to smuggle facet‑only correspondences.

