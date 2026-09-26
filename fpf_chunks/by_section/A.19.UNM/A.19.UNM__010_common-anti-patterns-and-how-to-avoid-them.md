---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 35016
line_end: 35041
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:8 - Common Anti‑Patterns and How to Avoid Them

1) **Hidden normalization inside scoring or selection**
   Avoid by using `CN_Spec.comparability.mode` and explicit UNM use.

2) **“NCV ⇒ indicator” shortcut**
   Avoid by treating indicatorization as UINDM policy, not a byproduct of normalization.

3) **“We normalized” without declaring invariants**
   Avoid by naming the actual domain, transformation, preserved invariants and lost distinctions; supply a class or congruence claim only under its additional conditions.

4) **Reusing a normalized value after its basis changed**
   Avoid by checking the exact bearer, method and CN-Spec editions, scope/window, comparison basis, evidence, and intended use again; cite a Bridge, kind relation, or plane relation only when the new use actually relies on it.

5) **Choosing a representative implicitly**
   Avoid by either keeping quotient objects abstract or declaring `NormalizationFix`.

6) **Treating a generic mapping word as a specialized relation claim**
   State the normalization's operands, rule, invariants and loss. Test any specialized `Map` or F.9 Bridge claim separately under its defining pattern.

7) **Treating UNM outputs as comparable beyond their declared bearer, basis, scope/window, or reference plane**
   Avoid by keeping comparison local to the recorded premises. Where a conclusion depends on another source-local meaning, bearer kind, or plane, cite the exact obtaining relation and its loss; otherwise constitute a new normalization result or fail closed.

8) **Re-authoring method, basis, or evidence anchors downstream**
   Avoid by citing the exact editioned method, basis, and evidence anchors as refs; a downstream pattern neither rewrites them nor replaces them with a generic registry.

