---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:10"
section_title: "Migration playbook — turning messy language into ULR‑clean prose (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__013_migration-playbook-turning-messy-language-into-ulr-clean-prose-informative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:10 — Migration playbook — turning messy language into ULR‑clean prose (informative)"
line_start: 59992
line_end: 60031
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.22"
  - "E.23"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:10 - Migration playbook — turning messy language into ULR‑clean prose *(informative)*

> A pragmatic **three‑pass** routine. Works with plain text, diagrams, or models; no tools required.

#### E.10:10.1 - Pass 0 — *Pre‑flight (2 minutes per page)*

0.1 **Name the Context card** you’re writing in (title, edition, scope note).
0.2 For every new or renamed token, **declare `LEX.TokenClass`** ∈ {KernelToken, ContextToken, DiscriminatorToken}.
0.3 Run **MG-DA pre‑check** (anchored head noun; no metaphor heads; if enum → declare its **CharacteristicSpace**).
0.4 Run **collision/uniqueness**: full‑text grep + Reserved‑Names registry (see § 7). If collides → rename or DRR deprecate.

#### E.10:10.2 - Pass 1 — *Harvest in the Context*

1.1 **Underline overloaded words** (*process, service, function, workflow, ticket, approval, spec, plan,* …).
1.2 For each, write a **one‑line intent** in Plain register (what FPF kind or relation is meant).
1.3 Mark any cross‑Context reuse candidates.

#### E.10:10.3 - Pass 2 — *Recover Core anchors (not substitution)*

Pass 2 is not a lexical replacement table. For each underlined word or phrase, first record the pre-repair object kind, relation or claim kind, slot or use-position, admissible use, and scope. Then choose one disposition: keep with a guarded-head note, split into several kinds named by value, rewrite locally, send to `F.18` for durable naming, send to the governing pattern, or leave blocking. A replacement phrase is admissible only after the post-repair kind, relation or claim kind, slot or use-position, admissible use, and scope are recoverable and no umbrella flattening, semantic narrowing, accidental widening, or slot-as-kind substitution has occurred.

2.1 Recover underlined words through **§ 9 L‑rules** table:
 • recipe → **`U.Method` / `U.MethodDescription`**
 • scheduled run → **`U.Work` / `U.WorkPlan`**
 • promise → **`U.PromiseContent`**
 • ability → **`U.Capability`**
 • actor‑mask → **`…Role / RoleAssignment`**
 • document or evidence-bearing publication cue → **`Episteme`** with **`EvidenceRole` or `RequirementRole`**
2.2 Apply **LEX.Morph** (§ 8): suffix gates (`…Role/…Work/MethodDescription/Service`), casing, reserved prefixes.
2.3 Pass **EntityOfConcern and Description-episteme boundary and specification-use** check: the EntityOfConcern named directly; recipes/docs as Description epistemes; Spec only where the specification-granting gate is present; actuals as run records.
2.4 Attach **Context tags** on first use; set **twin labels** (Tech/Plain) in the local Glossary.
2.5 Record a local `KindRestorationCheck` for every changed FPF-governed phrase: pre-repair kind/relation/slot-or-use-position/use/scope, post-repair kind/relation/slot-or-use-position/use/scope, and preserved/split/intentionally changed/blocker disposition. A changed word without this check remains an unresolved lexical finding. If a relation, signature, field, mathematical-lens, role, method, work, evidence, assurance, gate, or decision use-position is live, cite the governing pattern for that position; `E.10` detects the wording-use problem and does not replace the selected ontology.

#### E.10:10.4 - Pass 3 — *Stitch & publish*

3.1 Add **safe rewrites** for any anti‑patterns you found (use § 9.2 quick table).
3.2 If sameness is needed across Contexts, create a **Bridge** (F.9) with explicit `kind/dir/CL/Loss/scope` (apply **A.6.9 (RPR‑XCTX)** when quoted or imported source wording uses umbrella “same/equivalent/align/map/…” language).
3.3 Publish a one‑page **UTS** (F.17) for the Context (columns: Context, Tech label, Plain label, Kernel anchor, Warnings).
3.4 Log a short **DRR** when renames/aliases occur (F.13), linking to grep results that motivated the change.

