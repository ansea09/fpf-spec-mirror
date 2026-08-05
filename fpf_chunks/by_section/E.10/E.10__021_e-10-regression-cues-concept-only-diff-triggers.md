---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:19"
section_title: "E.10 regression cues (concept-only “diff” triggers)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__021_e-10-regression-cues-concept-only-diff-triggers.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:19 — E.10 regression cues (concept-only “diff” triggers)"
line_start: 75317
line_end: 75334
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

### E.10:19 - E.10 regression cues *(concept-only “diff” triggers)*

Re-review your prose when any of these happen:

* **Context edition** changes → re-affirm twin labels, Bridges, and acceptance wording.
* **A role or kind name grows** (“and”, “plus”, or “--”) -> apply MG-DA: split or bundle (A.2).
* **A slash, `and`, `plus`, `&`, or similar grouping mark appears in FPF-governed wording** -> classify the span before editing the mark. The trigger is the FPF-governed grouping use, not the character itself: LLM output, review text, intake notes, or draft prose often uses a slash as an unresolved alternative, an untyped bundle, or an attempt to point at a hidden kind. If the grouped words are claim-bearing heads, relation heads, kind candidates, an unresolved alternative, or an attempt to point at a hidden kind, apply MG-DA, `A.6.P`, or the selected restoration pattern: split, bundle, or recover the relation named by value and admissible use. If the mark is part of accepted notation or a conventional designation such as a source name, discipline abbreviation, established compound name, formula, ratio, fraction, unit, path-like quoted source token, title, product name, or URL, keep the notation and classify its use; do not rewrite `1/2` or similar conventional forms merely to remove the mark.
* **A “service” statement broadens scope** → use L-SERV and A.6.P:4.11a to recover the exact hidden subject, relation, and receiving use. Update only the claim whose direct owner says it changed; do not apply a fixed reading list or rewrite every nearby service-related claim.
* **Recipes gain or lose steps** -> first recover the exact `U.Method`, the claim-bearing episteme, and the changed claim. Update **`U.MethodDescription`** only when that episteme has the method as its exact EntityOfConcern and passes A.3.2; a code, diagram, recipe, procedure, or document-form change remains under its representation or publication owner unless claim content actually changes. Never move the change into service labels or `Role` names.
* **Evidence verbs creep into actor sentences** → re-apply L-rules (documents do not act).
* **A generic head or support-headed compound acquires an FPF claim or admissible use** (`comparative`, `safe`, `interactive`, `reliable`, `support`, `supported`, `supporting`, `support-looking`, and similar modifiers or heads) → restore the head kind first; then decide whether `support` states a direct subject relation or one of the common lexical alternatives, and route it as `E.10:0.2` requires before broader publication.
* **Method, practice, technique, algorithm, program, proof, solver, workflow, process, procedure, access path, query plan, control-strategy, method-algebra, method-graph, or selector-calculus wording changes** -> recover the governed method-side object or direct relation before rewriting: `U.Method`, `MethodRelationStructure@BoundedContext`, `U.MethodDescription`, formal-substrate declaration, C.29 mathematical-lens use and correspondence, `U.Mechanism`, `U.WorkPlan`, one dated Work occurrence admitted under `U.Work`, a separate episteme about it, role assignment or role relation, bounded context, discipline or cultural-evolution source label, method-family registry or selector outcome, evidence relation, or quote-only source wording. Do not replace one umbrella with another.
* **A declarative representation starts to sound imperative** (graph path, path slice, evidence-path wording, query, predicate, table, dashboard, publication face, mathematical representation, method-description representation, source-chain relation, carrier path, or FPF pattern relation "runs", "routes", "calls", "dispatches", "authorizes", or "flows" without a recovered kind) → apply `C.2.P.DR` or the direct governing pattern such as `E.18`, `A.10`, `A.19.SPR`, `E.17`, `C.29`, `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.8`, or `F.19`.
* **New token minted** → ensure `LEX.TokenClass` is declared and perform collision checks. If an enumeration is current, name its closed value set, classified kind, and direct owner; add a `CharacteristicSpace` only when the enumeration is the declared CSLC scale of one exact named `U.Characteristic`.
* **Suffix drift** (e.g., `…Work` on a plan) → fix via **LEX.Morph**.
* **Cross-Context reuse by label** appears -> use a **Bridge** (F.9) or split senses.
* **A guarded head needs a new label** → prefer a guarded-head note first; if no admissible existing token remains for one durable reusable name, settle the governed value, record the applicable **F.8** decision, and use **F.18** plus an **F.17** row when public publication is current.

