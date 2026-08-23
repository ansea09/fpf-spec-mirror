---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:19"
section_title: "E.10 regression cues (concept-only “diff” triggers)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__021_e-10-regression-cues-concept-only-diff-triggers.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:19 — E.10 regression cues (concept-only “diff” triggers)"
line_start: 73792
line_end: 73809
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
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
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.10.MOVE"
  - "E.10.ROLE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.17"
  - "F.18"
  - "F.19"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
---

### E.10:19 - E.10 regression cues *(concept-only “diff” triggers)*

Re-review your prose when any of these happen:

* **A source edition, effective scheme, or local meaning changes** → re-affirm any Tech-and-Plain twin mapping and first-use gloss; recheck an F.9 Bridge, use claim, reliance claim, or acceptance wording only when that exact changed value participates.
* **A system-role-kind or other kind name grows** (“and”, “plus”, or “--”) -> apply MG-DA: recover the one kind, explicit alternatives, relation, or bundle before renaming. Bare *role* first uses `E.10.ROLE`.
* **A slash, `and`, `plus`, `&`, or similar grouping mark appears in FPF-governed wording** -> classify the span before editing the mark. The trigger is the FPF-governed grouping use, not the character itself: LLM output, review text, intake notes, or draft prose often uses a slash as an unresolved alternative, an untyped bundle, or an attempt to point at a hidden kind. If the grouped words are claim-bearing heads, relation heads, kind candidates, an unresolved alternative, or an attempt to point at a hidden kind, apply MG-DA, `A.6.P`, or the selected restoration pattern: split, bundle, or recover the relation named by value and admissible use. If the mark is part of accepted notation or a conventional designation such as a source name, discipline abbreviation, established compound name, formula, ratio, fraction, unit, path-like quoted source token, title, product name, or URL, keep the notation and classify its use; do not rewrite `1/2` or similar conventional forms merely to remove the mark.
* **A “service” statement broadens scope** → use L-SERV and A.6.P:4.11a to recover the hidden subject, relation, and receiving use. Update only that recovered claim; do not apply a fixed reading list or rewrite every nearby service-related claim.
* **Recipes gain or lose steps** -> first recover the exact `U.Method`, the claim-bearing episteme, and the changed claim. Update **`U.MethodDescription`** only when that episteme has the method as its exact EntityOfConcern and passes A.3.2; a code, diagram, recipe, procedure, or document-form change remains under the pattern for that representation or publication unless claim content actually changes. Never move the change into service labels or system-role-kind names.
* **Evidence verbs creep into actor sentences** → re-apply L-rules (documents do not act).
* **A generic head or support-headed compound acquires an FPF claim or admissible use** (`comparative`, `safe`, `interactive`, `reliable`, `support`, `supported`, `supporting`, `support-looking`, and similar modifiers or heads) → restore the head kind first; then decide whether `support` states a direct subject relation or one of the common lexical alternatives, and route it as `E.10:0.2` requires before broader publication.
* **Wording about a way of doing or one of its neighboring objects changes**—for example, wording with *method*, *practice*, *technique*, *algorithm*, *program*, *proof*, *solver*, *workflow*, *process*, *procedure*, *access path*, *query plan*, *control strategy*, *method algebra*, *method graph*, or *selector calculus* → recover the method-side object or relation before rewriting. The result may be `U.Method`; an exact composition, substitution, iteration, fallback, selection, family-membership, or other direct method-side relation; an A.22-selected `MethodRelationStructure` only when a named use depends on their organization; `U.MethodDescription`; formal-substrate declaration; C.29 mathematical-lens use and correspondence; `U.Mechanism`; `U.WorkPlan`; one dated Work occurrence admitted under `U.Work`; a separate episteme about it; exact system-role assignment or relation among system-role kinds; A.1.1 `BoundedModelUseStructure`; an exact source, practice, scope, situation, discipline, or cultural-evolution label; method-family registry or selector outcome; evidence relation; or quote-only source wording. Do not replace one umbrella with another.
* **A declarative representation starts to sound imperative** (graph path, path slice, evidence-path wording, query, predicate, table, dashboard, publication face, mathematical representation, method-description representation, source-chain relation, carrier path, or FPF pattern relation `runs`, `routes`, `calls`, `dispatches`, `authorizes`, or `flows` without a recovered kind) → apply `C.2.P.DR` or the concrete pattern such as `E.18`, `A.10`, `A.19.SPR`, `E.17`, `C.29`, `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.8`, or `F.19`.
* **New token minted** → ensure `LEX.TokenClass` is declared and perform collision checks. If an enumeration is current, name its closed value set, classified kind, and classification rule; add a `CharacteristicSpace` only when the enumeration is the declared CSLC scale of one named `U.Characteristic`.
* **Suffix drift** (e.g., `…Work` on a plan) → fix via **LEX.Morph**.
* **A label is reused across local sources, practices, or schemes** → recover each local meaning. Keep them distinct unless an F.9 Bridge actually obtains between exact cells; state any proposed use and reliance separately.
* **A guarded head needs a new label** → prefer a guarded-head note first; if no admissible existing token remains for one durable reusable name, settle the value and its use, record the applicable **F.8** decision, and use **F.18** plus an **F.17** row when public publication is current.

