---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:11"
section_title: "E.10 conformance prompts (normative, concept-only questions)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__014_e-10-conformance-prompts-normative-concept-only-questions.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:11 — E.10 conformance prompts (normative, concept-only questions)"
line_start: 68969
line_end: 68991
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
keywords:
---

### E.10:11 - E.10 conformance prompts *(normative, concept-only questions)*

> Use these **prompts** during review. They reference § 7 (MG-DA) and § 8 (LEX.Morph) instead of repeating them.

1. **Context prompt.** Is each potentially polysemous noun interpreted inside a **named `U.BoundedContext`**?
2. **EntityOfConcern and Description-episteme boundary and specification-use prompt.** Does each sentence use the correct boundary (the EntityOfConcern named directly; Description-episteme use for descriptions; specification use only where a direct gate pattern grants it; run: actuals)?
3. **Token prompt.** For new or renamed tokens, is **`LEX.TokenClass`** declared and consistent with where the token appears?
4. **Head-kind prompt.** Does the **head noun** name what kind of thing the phrase is actually about: Role, Method, Work, Context, Characteristic, Capability, Requirement, publication form, service-access relation, service-offer record, interpretation, process, or authority use? A narrowing qualifier alone does **not** answer this question.
5. **Qualifier-claim prompt.** If an adjective, participle, genitive, or comparative modifier carries a claim being made, comparison criterion, relation, or admissible-use boundary, has that use been restored explicitly rather than left inside the modifier alone?
6. **Slot, relation-position, and use-relation prompt.** If the sentence names an object through a relation slot, signature slot, schema field, mathematical-lens relation position, use relation, or another FPF-governed position, are the object kind, position name, reference mode when required, admissible use, and governing pattern recoverable? If not, apply `E.10.ARCH` or the governing pattern before rewriting.
7. **Support-like interpretation prompt.** If `support`, `supported`, `supporting`, or a support-headed compound has FPF-governed use, apply `E.10:0.2` first and then use `A.6.P` support-like interpretation discrimination instead of a synonym swap. If the selected interpretation is base, anchor, or basedness, apply `A.6.6` and state `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`. If no interpretation can be selected, do not use support wording for reliance, publication, gate, decision, assurance, work, architecture, pattern-quality, or cross-context reuse.
8. **Comparison-basis prompt.** If the sentence compares, ranks, escalates, or downgrades something, is the comparison basis ontologically homogeneous after head-kind and qualifier restoration?
9. **Morphology prompt.** Do suffix, prefix, and casing pass **LEX.Morph** gates (e.g., `…Role`, `MethodDescription`, `Work`)?
10. **Promise, ability, access, and performance split.** Are service promise or acceptance content, service-access relation, **Capability** (ability), and **Work** (performance) distinct and governed by direct patterns?
11. **Plan and execution split.** Are **WorkPlan** windows separated from **Work** actuals?
12. **Evidence prompt.** Do documents, epistemes, and publications stay in source-use, evidence-use, specification-use, or publication-use relations, while systems or acting holons hold work-facing role assignments and act?
13. **Bridge prompt.** If sameness spans Contexts, is there an explicit **Bridge** with **CL** and loss notes?
13. **Collision prompt.** Were full-text and Reserved-Names checks completed, with no other meaning of this token anywhere in FPF?
14. **Naming-procedure prompt.** If one durable reusable name is needed because no admissible existing token carries the needed meaning beyond one local repair, was the full **F.18 `MintNew` or `DocumentLegacy`** procedure completed rather than picking a label by intuition and filling a partial Name Card afterward?
15. **Value-substitution prompt.** After the repair, can the declared reader still see the remaining admissible reader use, and did the repair preserve usability, affordability, semantic composability, governing-pattern fit, and local action guidance? If not, narrow the repair, keep ordinary wording with a recovery note with recovered kind and use, or leave the issue blocking instead of optimizing for lexical purity.

**Working order for precision repair on FPF-governed prose.** Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack the qualifier claim, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, and even then the more precise upstream interpretation must remain recoverable.

