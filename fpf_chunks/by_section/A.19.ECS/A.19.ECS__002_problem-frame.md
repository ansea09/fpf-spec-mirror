---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__002_problem-frame.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:1 — Problem frame"
line_start: 23353
line_end: 23374
dependencies:
  - "A.17-A.19"
  - "C.16"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8.ECSPF"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### A.19.ECS:1 - Problem frame

Use `A.19.ECS` when an object version is to be improved or judged, but the evaluation that says what "better" means is not yet available, not yet explicit, or not yet adequate for the object.

`A.19` says how a `CharacteristicSpace` is structured: declared characteristics, declared scales, slots, value sets, declared coordinate groups, and no hidden normalization or aggregation. `A.19.ECS` says how to make such a `CharacteristicSpace` for the evaluated object, so that an evaluation can later evaluate that object and `E.23` can run an improvement loop without inventing values.

The ordinary output is an evaluation characteristic-space specification: a grouped set of characteristics, scales, value meanings, evidence-basis rules, missingness rules, result-row shape, calibration points, coordinate-specific evidence payloads, protected trade-offs, status meanings, and stop or reopen conditions for one evaluated object kind and use scope.

**Not this pattern when.** If a suitable evaluation already exists, cite it and use `E.22` for question framing or `E.23` for repeated improvement. Use `A.17`, `A.18`, and `C.16` when the live problem is one characteristic, one scale, or measurement legality. Use `C.16.P` first when candidate coordinate wording still hides whether the use under repair is a characteristic, scale, coordinate, score, metric label, quality-term repair, or governing-pattern relation. Use `A.19` when the live problem is the structure of `CharacteristicSpace` itself. Use `C.25` when the evaluated EntityOfConcern is a composite engineering quality family that already fits Q-Bundle form. Use `F.18` when the live problem is durable naming. Use `E.21`, `E.9.DA`, or `E.2.DA` when the evaluated EntityOfConcern is respectively one FPF pattern version, one `DRR`, or one FPF-level Pillar-adequacy evaluated EntityOfConcern.

**First useful move.** State the sentence: "good as what kind of object, for which use, against which contrast cases?" Then name the evaluated object kind, the use scope, and at least three contrast cases: one admissible evaluated object, one below-floor evaluated object, and one outside-declared-object-kind boundary case that should return to evaluation selection before the evaluation is opened or receive an explicit object-kind-fit defect/value when that evaluation has already been invoked.

**Existing-evaluation boundary.** If the answer is "use this existing evaluation" and the evaluated object kind, use scope, floor, protected trade-offs, and stop meanings are already recoverable, do not construct a new `CharacteristicSpace`.

**What goes wrong if missed.** A team says "improve this" and then chooses convenient scores. A scale set appears from nowhere. Chairs, coal plants, nuclear plants, and FPF patterns all get compared on coordinates that do not distinguish the evaluated object kind. One visible value improves while the intended use gets worse. A review can say "better" but cannot say which object property changed, what trade-off was protected, or why improvement may stop.

**What this buys.** `A.19.ECS` gives improvement work a way to create the missing evaluation before the loop starts. It keeps `E.23` universal and simple: `E.23` changes the object and asks an evaluation to re-evaluate it; `A.19.ECS` helps build that evaluation when none is yet adequate.

**Primary EntityOfConcern in plain terms.** The primary EntityOfConcern is the construction of one evaluation `CharacteristicSpace` for one evaluated object kind and declared use.

**Primary working reader.** The first reader is the engineer, analyst, pattern author, reviewer, steward, or method designer who must define what counts as improvement for an evaluated object before running an improvement loop.

