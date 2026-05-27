---
chunk_kind: "child"
pattern_id: "E.21"
pattern_title: "FPF Pattern Quality Characteristic Space"
section_id: "E.21:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.21/E.21__002_problem-frame.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.21 — FPF Pattern Quality Characteristic Space"
  - "E.21:1 — Problem frame"
line_start: 64152
line_end: 64175
dependencies:
  - "A.17-A.19"
  - "A.6.P"
  - "A.6.Q"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "E.11"
  - "E.17.AUD"
  - "E.19"
  - "E.8"
  - "F.18"
  - "J.4"
keywords:
  - "Goodhart/proxy substitution"
  - "Pareto/front comparison"
  - "PatternQualityCharacteristicSpace"
  - "PatternQualityQBundle"
  - "activation-normalized coordinates"
  - "and admissibility predicates are not written as duties"
  - "bounded non-use"
  - "coordinate evidence"
  - "definitions"
  - "eligibility filters"
  - "first move"
  - "invariants"
  - "pattern quality"
  - "state agent obligations only"
  - "stop condition"
  - "typing rules"
---

### E.21:1 - Problem frame

Use `E.21` when you are evaluating one FPF pattern version and need to know whether improvement can stop without relying on taste, a single quality score, or template compliance alone. The governed object is the scoped pattern-quality claim; the target text being read is one authored FPF pattern body in one declared use and reader scope.

Use it especially when a pattern already has the `E.8` skeleton and may even pass an `E.19` review, but authors still disagree about whether the pattern is recognisable, action-guiding, ontologically precise, SoTA-bearing, proportionate in apparatus, and safe to compose with neighbours.

**Not this pattern when.** Use `E.8` to write the pattern body. Use `E.19` to run admission or refresh review profiles. Use `C.16`, `A.17`, `A.18`, and `A.19` when the live problem is measurement legality, Characteristic/Scale discipline, or declaring a general `CharacteristicSpace`. Use `C.25` when the live problem is an arbitrary engineering quality family rather than FPF pattern quality. Use `F.18` when the live problem is durable naming. Not this pattern when the live question is whether a user correctly applied an FPF pattern in a project case. `E.21` reads the quality of the pattern text for a declared reader/use/scope. Pattern-application quality belongs to the receiving project-side or publication-side pattern that governs the actual case: evidence, assurance, gate, work, decision, publication, action invitation, method, or bridge use as applicable.

**First useful move.** The architectural first move of `E.21` is not "run quality control". It is to recover the target pattern's first admissible action-guiding move for the declared reader/use/window. Start with the ordinary first-pass slice of `PatternQualityQBundle`: name `PatternVersionRef`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`, then inspect the target pattern's `Problem frame` and `Solution` for one first admissible action-guiding move for that working reader.

If that first move is absent, unrecoverable, or only present in the Conformance Checklist, close the first-pass read as `repairBeforeUse` for the declared use, or as `admissibleWithNarrowerUse` when the pattern can still serve an expert-only or support-only scope. Do not require a full coordinate comparison before this result.

Create the fuller `PatternQualityQBundle` only when the first-pass slice survives, when several candidate edits are being compared, or when admission, refresh, high-assurance reuse, or contested neighbour authority is live.

**What goes wrong if missed.** Pattern improvement collapses into a single "quality score", a reviewer preference, or a heading checklist. That hides hard blockers such as undefined vocabulary, shadow authority, decorative SoTA, ordinal arithmetic, missing first move, or neighbour breakage.

**What this buys.** `E.21` gives authors one typed quality space for FPF patterns: hard eligibility filters first, multi-characteristic coordinates second, Pareto/front reasoning for candidate improvements, and an explicit stop condition that does not scalarize.

`E.21` is the quality-characteristic receiving pattern for claims of the form "this pattern version is sufficiently good for this use, readership, and scope." It normalizes such claims into a scoped bundle; it does not run the review process or take over authoring, measurement, naming, project evidence, assurance, gate, release, or work authority from neighbouring FPF patterns.

**Governed object in plain terms.** The governed object is the pattern-quality claim for one FPF pattern version under one declared use and reader scope.

**Primary working reader.** The first reader is an FPF author, reviewer, or steward deciding whether to keep improving a pattern version. The downstream reader is the practitioner or manager who must use the pattern as action guidance.

