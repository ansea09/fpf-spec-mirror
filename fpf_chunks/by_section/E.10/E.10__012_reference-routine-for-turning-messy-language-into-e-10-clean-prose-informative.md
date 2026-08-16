---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:10"
section_title: "Reference routine for turning messy language into E.10-clean prose (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__012_reference-routine-for-turning-messy-language-into-e-10-clean-prose-informative.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:10 — Reference routine for turning messy language into E.10-clean prose (informative)"
line_start: 75402
line_end: 75447
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

### E.10:10 - Reference routine for turning messy language into E.10-clean prose *(informative)*

> A pragmatic **three-pass** routine. It is subordinate to `E.10:0.2` and is used only when the selected wording problem needs register, naming, morphology, or local rewrite details. It works with plain text, diagrams, or models and uses no special tool.

#### E.10:10.1 - Pass 0 — *Pre‑flight (2 minutes per page)*

0.1 **Name only the local facts that matter here:** the exact source or practice, effective scheme, scope, model-use structure, working situation, frame, or referent when it changes interpretation or action. Do not create a generic Context card.
0.2 For every new or renamed token, **declare `LEX.TokenClass`** ∈ {KernelToken, ContextToken, DiscriminatorToken}.
0.3 Apply the **MG-DA pre-check** (anchored head noun; no metaphor heads; if an enumeration is current, name its closed value set, classified kind, and classification rule; declare a `CharacteristicSpace` only when the enumeration is the declared CSLC scale of one named `U.Characteristic`).
0.4 Perform **collision and uniqueness** checking: full-text grep plus Reserved-Names registry (see § 7). If collides -> rename or DRR deprecate.

#### E.10:10.2 - Pass 1 — *Inspect the selected span*

1.1 **Underline overloaded words** (*process, service, function, workflow, ticket, approval, spec, plan,* …).
1.2 For each, write a **one‑line intent** in Plain register (what FPF kind or relation is meant).
1.3 Mark shared labels whose local senses may differ; do not infer a relation from the label.

#### E.10:10.3 - Pass 2 — *Recover Core anchors (not substitution)*

Pass 2 is not a lexical replacement table. For each underlined word or phrase, first write one Plain-register sentence saying what the text is trying to assert or ask. Select the applicable `E.10:0.0a` branch when the use is relation-like; otherwise name the concrete object, applicable rule, admissible use, and scope. Compare the same object and claim before and after repair, then choose one disposition: keep with a guarded-head note, split into several kinds named by value, rewrite locally, record a durable naming case under `F.18`, apply the relevant pattern, or leave blocking. Name an exact predicate, assertion, `ClaimGraph`, Method, actor, assignment, or Work only when the current claim or a named later use depends on that identity. This proportional naming rule does not make a covering assignment or F.6 fact optional once performed Work is admitted. A replacement phrase is admissible only when it remains recoverable and introduces no umbrella flattening, semantic narrowing, accidental widening, declaration-participant collapse, representation-as-obtaining, or slot-as-kind substitution.

2.1 Recover underlined words through **§ 9 L‑rules** table:
 • recipe -> the exact **`U.Method`** when the wording denotes one way of doing; **`U.MethodDescription`** only for a separately identified claim-bearing episteme whose exact EntityOfConcern is that admitted method and whose claims pass A.3.2; otherwise a C.29 representation, publication form, source wording, or ordinary wording under its applicable rule
 • planned work window or dated occurrence -> a planning cue, schedule representation, or `PlanItem` content until one exact episteme passes A.15.2's present-EntityOfConcern, horizon, `PlanItem`, and substantive-coordination predicate; only then **`U.WorkPlan`**. A dated performed individual is independently admitted as a **Work occurrence under `U.Work`** only on the A.15.1 basis
 • promise -> **`U.PromiseContent`**
 • ability -> **`U.Capability`**
 • For actor or doer wording, identify the entity that acts; admit it as **`U.System`** only when A.1 passes. When performed Work is current, use A.15.1 and F.6 to identify the dated Work, performer, and assignment. Use a `...SystemRole` designation only when that classification matters.
 • document or evidence-bearing publication cue → **`Episteme`** used in an evidence-use, source-use, status-use, constraint, commitment, gate, or publication-use relation named by its evidence, source, status, constraint, commitment, gate, or publication pattern
2.2 Apply **LEX.Morph** (§ 8): compound and suffix gates such as concrete `...SystemRole` kind designations, `...Work`, `MethodDescription`, service-description episteme, service-access publication, or service-offer record labels, casing, and reserved prefixes. Bare `...Role` remains a trigger, not an accepted default form.
2.3 Pass **EntityOfConcern and Description-episteme boundary and specification-use** check: name the EntityOfConcern directly; do not type a recipe, procedure, code expression, diagram, ETL label, document form, or relation-structure description as `U.MethodDescription` by appearance. Admit only a claim-bearing episteme whose exact EntityOfConcern is one admitted `U.Method` and whose claims pass A.3.2; use Spec only where a named specification-granting gate is present. Recover actual performed facts as independently obtaining relations involving a Work occurrence, and keep run records as separate epistemes.
2.4 On first use, state the exact source or practice and effective scheme when they change meaning. Add a Tech-and-Plain twin pair in the local glossary only when a one-to-one didactic mapping is useful.
2.5 Perform one local `KindRestorationCheck` for each changed FPF-governed phrase. Write the full form below only when the repair needs a separately inspectable result; otherwise the repaired sentence and its kind-preservation check are enough. Keep any written result with the bounded repair instead of creating a second ledger:
   - `Situation`: quote the sentence and say in ordinary words why the phrase matters to its reader.
   - `Action`: write the intended sentence and select one `E.10:0.0a` branch, another concrete governed object, or explicit ordinary/quoted non-use.
   - `Before/after`: name the governed object, claim, applicable pattern contribution, admissible use, and scope on both sides; add only the distinctions required by the selected branch.
   - `Visible result and stop`: give the accepted wording, concrete result obtained by applying the selected rule, or blocker, plus the nearby case that must not be read into it. Stop when that result lets the reader return to the domain task.

Mark the disposition `preserved`, `split`, `intentionally changed`, or `blocker`. A changed phrase without this check remains an unresolved lexical finding. Cite the concrete pattern for any current relation, declaration, representation, bare-*role* recovery, exact local system-role kind or assignment, Method, Work, evidence, assurance, gate, or decision use, and state what it contributes; `E.10` detects the wording problem and does not replace that ontology.

#### E.10:10.4 - Pass 3 — *Stitch and publish*

3.1 Add **safe rewrites** for any anti‑patterns you found (use § 9.2 quick table).
3.2 If sameness or mapping between two exact local senses is being claimed, identify both senses and create their F.17 cells when stable addresses are needed. Cite an F.9 Bridge only if its direct relation actually obtains, and state direction, congruence, loss, and scope; keep use and reliance separate. Apply **A.6.9 (RPR-XCTX)** when quoted or imported wording such as “same”, “equivalent”, “align”, or “map” still hides the relation.
3.3 Publish an F.17 row or compact UTS only when readers need a durable term address. State the value it names, effective scheme, source expression, local sense, Tech and Plain designations when both exist, and warnings. The row creates no Bridge, equivalence, use, or reliance.
3.4 Log a short **DRR** when renames or aliases occur (F.13), linking to grep results that motivated the change.

