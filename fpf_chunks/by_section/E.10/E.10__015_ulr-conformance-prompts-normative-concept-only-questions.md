---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:11"
section_title: "ULR conformance prompts (normative, concept-only questions)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__015_ulr-conformance-prompts-normative-concept-only-questions.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:11 — ULR conformance prompts (normative, concept-only questions)"
line_start: 51169
line_end: 51188
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.7"
  - "B.1"
  - "B.3"
  - "E.10.SEMIO"
  - "E.5"
  - "F.18"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:11 - ULR conformance prompts *(normative, concept-only questions)*

> Use these **prompts** during review. They reference § 7 (MG-DA) and § 8 (LEX.Morph) instead of repeating them.

1. **Context prompt.** Does each potentially polysemous noun live inside a **named `U.BoundedContext`**?
2. **Layer prompt.** Is each sentence in the correct **I/D/S layer** (I: type/role; D: description/spec; run: actuals)?
3. **Token prompt.** For new/renamed tokens, is **`LEX.TokenClass`** declared and consistent with where the token appears?
4. **Head-kind prompt.** Does the **head noun** name what kind of thing the phrase is actually about (Role/Method/Service/Work/Context/Characteristic/publication form/reading/process/authority use)? A narrowing qualifier alone does **not** answer this question.
5. **Qualifier-load prompt.** If an adjective, participle, genitive, or comparative modifier is doing semantic work, has that load been restored explicitly rather than left inside the modifier alone?
6. **Comparison-basis prompt.** If the sentence compares, ranks, escalates, or downgrades something, is the comparison basis ontologically homogeneous after head-kind and qualifier restoration?
7. **Morphology prompt.** Do suffix/prefix/casing pass **LEX.Morph** gates (e.g., `…Role`, `MethodDescription`, `Work`)?
8. **Promise vs ability vs performance.** Are **Service** (promise), **Capability** (ability), and **Work** (performance) distinct?
9. **Plan vs execution.** Are **WorkPlan** windows separated from **Work** actuals?
10. **Evidence prompt.** Do documents **hold roles** and **justify**, while **systems act**?
11. **Bridge prompt.** If sameness spans Contexts, is there an explicit **Bridge** with **CL** and loss notes?
12. **Collision prompt.** Did we run full-text + Reserved-Names checks (no other meaning of this token anywhere in FPF)?
13. **Naming-procedure prompt.** If one durable reusable name is needed because no admissible existing token carries the needed meaning beyond one local repair, did we run the full **F.18 `MintNew` or `DocumentLegacy`** procedure rather than picking a label by intuition and filling a partial Name Card afterward?

**Working order for precision repair on load-bearing prose.** Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack qualifier load, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, and even then the more precise upstream reading must remain recoverable.

