---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:11"
section_title: "E.10 conformance prompts (normative, concept-only questions)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__013_e-10-conformance-prompts-normative-concept-only-questions.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:11 — E.10 conformance prompts (normative, concept-only questions)"
line_start: 75210
line_end: 75232
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
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
4. **Head-kind prompt.** Does the head noun name what kind of thing the phrase is actually about: Role, Method, Work, Context, Characteristic, Capability, constraint claim, commitment, publication form, service-access relation, service-offer record, interpretation, `U.Transformation`, `TransformationFlowStructure`, or authority use? A narrowing qualifier alone does not answer this question.
5. **Qualifier-claim prompt.** If an adjective, participle, genitive, or comparative modifier carries a claim being made, comparison criterion, relation, or admissible-use boundary, has that use been restored explicitly rather than left inside the modifier alone?
6. **Direct relation, declaration, designation, and representation prompt.** Can a reader select exactly one `E.10:0.0a` branch from the sentence and point to its visible result? If yes, name that branch's direct owner and preserve only the objects named by that branch. If no branch fits, state the other governed object or ordinary non-use. If the sentence still mixes branches or only lists possible owners, rewrite it before applying `E.10.ARCH` or the direct governing pattern.
7. **Support interpretation prompt.** If `support`, `supported`, `supporting`, or a support-headed compound appears, first keep it unchanged when it is ordinary or quoted wording and no FPF claim relies on it. Otherwise ask whether it already states a direct subject-domain fact. If so, name the things and relation and go to that relation's owner; use `A.6.P` only when the predicate or a participant is unclear, and `A.6.RCD` only when both are clear but no owner exists. If it is not a direct subject relation, choose the matching common alternative in `E.10:0.2`, write the concrete sentence, and go straight to that alternative's owner. Thus `Test T supports claim C` reaches `A.10`, `Index I supports readers` can remain bounded reader help, and `Column C supports roof R` reaches a structural relation or a missing-governor result; none is forced into another bucket. For base, anchor, or basedness, apply `A.6.6` and state `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`. Do not mint `SupportRelation` or ask `A.6.P` to choose among the common alternatives.
8. **Comparison-basis prompt.** If the sentence compares, ranks, escalates, or downgrades something, is the comparison basis ontologically homogeneous after head-kind and qualifier restoration?
9. **Morphology prompt.** Do suffix, prefix, and casing pass **LEX.Morph** gates (e.g., `…Role`, `MethodDescription`, `Work`)?
10. **Promise, ability, access, and performance split.** Are service promise or acceptance content, service-access relation, **Capability** (ability), and **Work** (performance) distinct and governed by direct patterns?
11. **Plan and execution split.** Are a planning cue or admitted `U.WorkPlan` kept separate from one exact Work individual admitted under `U.Work`, each admitted performer `U.System`, each exact obtaining covering `RA : U.RoleAssignment`, any explicit F.6 `performedUnderAssignment(W, RA)` attribution, and the independently obtaining method, temporal, containing-system, affected-referent, binding, and resource-use relations, plus any separate assertion or description episteme that states them?
12. **Evidence prompt.** Do documents, epistemes, and publications stay in source-use, evidence-use, specification-use, or publication-use relations? When performed work is current, is the actor an admitted `U.System`, and are exact `W : U.Work`, exact obtaining `RA : U.RoleAssignment`, and `performedUnderAssignment(W, RA)` or `S performed W under RA` recoverable?
13. **Bridge prompt.** If sameness spans Contexts, is there an explicit **Bridge** with **CL** and loss notes?
14. **Collision prompt.** Were full-text and Reserved-Names checks completed, with no other meaning of this token anywhere in FPF?
15. **Naming-procedure prompt.** If one durable reusable name is needed because no admissible existing token carries the needed meaning beyond one local repair, was the governed value settled first, was the applicable **F.8** decision recorded, and were the **F.18** NameCard and any required **F.17** public term row completed rather than picking a label by intuition or filling publication apparatus around an unresolved object?
16. **Value-substitution prompt.** After the repair, can the declared reader still see the remaining admissible reader use, and did the repair preserve usability, affordability, semantic composability, governing-pattern fit, and local action guidance? If not, narrow the repair, keep ordinary wording with a recovery note with recovered kind and use, or leave the issue blocking instead of optimizing for lexical purity.

**Working order for precision repair on FPF-governed prose.** Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack the qualifier claim, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, while keeping the more precise upstream interpretation recoverable.

