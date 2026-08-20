---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Lexical Authoring & Evolution Protocol  (LEX‑AUTH)"
section_id: "E.15:4"
section_title: "Solution — A governed evolutionary authoring method with a publishable LEX‑AUTH Trace (LAT)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__005_solution-a-governed-evolutionary-authoring-method-with-a-publishable-lex-auth-trace-lat.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "E.15 — Lexical Authoring & Evolution Protocol  (LEX‑AUTH)"
  - "E.15:4 — Solution — A governed evolutionary authoring method with a publishable LEX‑AUTH Trace (LAT)"
line_start: 79081
line_end: 79175
dependencies:
  - "A.10"
  - "B.3"
  - "B.4"
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.9"
  - "F.15"
keywords:
  - "LAT"
  - "delta-classes"
  - "evolution protocol"
  - "lexical authoring"
---

### E.15:4 - Solution — A *governed evolutionary* authoring method with a publishable **LEX‑AUTH Trace (LAT)**

LEX‑AUTH defines **how** a pattern is **proposed, varied, selected, validated, and merged**, with artifacts and evidence fit to the FPF kernel.

#### E.15:4.1 - Method (design‑time choreography)

**Stage A — Frame and Scope (Question, Intended Use, Objectives, Invariants)**
**Historical record recovery.** Keep an old LAT, Context Card, and the claims it represents immutable under their original edition. When a current use relies on one, recover only the exact source and edition, effective `ReferenceScheme`, local claim, `ClaimScope`, and any method, model, criterion, or other subject-defined value that the use actually needs. Author a successor only from evidence. If an exact needed value cannot be recovered, return that value as unresolved; do not fill it from a card label or a newer edition. Reopen only the claims or actions that depended on the changed or missing value. An edition-number change alone does not reopen unrelated use.

1. **Frame** the exact pattern and edition, receiving question and intended use, applicable `ClaimScope`, and the selected scheme, source, model-use structure, or subject-specific situation only when it changes the work. Cite the applicable guardrails in **E.5.***, and state objectives for the change, such as clearer language, wider useful application, or lower assurance cost.
2. **Declare the Delta‑Class** (see §4.3) and **impact radius** (dependent patterns, bridges, tests).
3. **Fix acceptance targets** (see §4.4 Quality & SoTA metrics).

**Stage B — Generate candidates (SoTA + NQD)**
4. **Harvest SoTA** inputs (standards, rival patterns, lived domain idioms) and **bind** them as evidence through evidence-use relations with **claim/claim‑scope/timespan** and polarity (empirical vs deductive lines).
5. **Generate candidate variants** using **NQD‑CAL** engines (Novelty/Quality/Diversity) with an **E/E policy** (explore↔exploit governor) to populate a **Pareto front** of pattern phrasings/structures. *(No single shot; multiple candidate clauses compete.)*

**Stage C — Shape & Align (Structure, Bridges, USM)**
6. **Shape** top candidates into the standard **pattern template** (Problem frame → Problem → Forces → Solution → CC → Consequences → Rationale), obeying **LEX‑BUNDLE** (no tooling jargon; twin registers allowed).
7. **Relate local meanings only when needed.** Recover the exact source-local claims first. When the candidate actually relies on a relation between distinct F.17 cells, use F.9 to state that relation, its admitted use, and its loss or limits. A source import or shared word alone creates no Bridge.
8. **Type scopes** with **USM (A.2.6)**: keep **ClaimScope (G)** distinct from **WorkScope**; no “applicability/envelope” smuggling.

**Stage D — Validate & Decide (Assurance, Tests, DRR)**
9. **Run the harness**: update **SCR/RSCR** (F.15), lint lexical rules (E.10), run **Γ‑consistency** and **RSG/SoD** checks where relevant.
10. **Score** candidates on **Quality & SoTA metrics** (§4.4) and **assurance deltas** (Δ⟨F,G,R⟩).
11. Record a **DRR** (E.9) with *options considered*, *trade‑offs*, chosen candidate, *blast‑radius*.
12. **Merge** the winner; version pattern **SemVer** by Delta‑Class.

**Stage E — Publish & Monitor**
13. Publish the **LEX‑AUTH Trace (LAT)** (§4.2) as the separate authoring/evidence record for the change.

14. Schedule **evidence refresh** windows and an **evolution watchpoint** (B.4 loop): when metrics or SoTA inputs decay, reopen Stage B.

#### E.15:4.2 - The **LEX‑AUTH Trace (LAT)** — what it is and why it matters

A LAT is **not** “we ran a script.” It is a **structured episteme** that lets others **reproduce quality gains** and **re‑run** the search when SoTA shifts.

**LAT minimal contents (publish with the pattern):**

1. **Pattern and use identity** (pattern id and edition, intended use, `ClaimScope`, selected scheme or source, and any model-use structure that materially changes the use, plus SemVer and Delta-Class).
2. **Objective vector** (what we tried to improve: clarity, universality, assurance cost, etc.).
3. **SoTA pack** (sources bound through evidence-use relations with claim/scope/time and polarity).
4. **NQD settings** (emitters/lenses, diversity characteristics) + **E/E policy** used.
5. **Candidate set** (top K variants with NQD scores + short deltas from baseline).
6. **Cross-local relation account** (each actually consumed F.9 relation between distinct F.17 cells, with admitted use and loss notes; ordinary source imports need no fictitious Bridge).
7. **Assurance delta** (Δ⟨F,G,R⟩ from baseline; penalties from CL applied).
8. **Harness results** (checks passed/failed, test diffs).
9. **DRR link** (decision rationale id).
10. **Refresh policy** (evidence decay windows and triggers).

**Uses of the LAT:**
*Reproducibility* (re-run B-stages as SoTA changes), *assurance* (explicit impact on `F`, `G`, and `R`), *portfolio health* (diversity and coverage), *teaching* (didactic before-and-after), and *cross-local honesty* (no relation inferred from shared wording or source import).
Publish the pattern with its **DRR**, and publish the **LAT** as the separate authoring/evidence record for the change. The LAT carries the reproducible authoring trace and cites the DRR as the governing decision record. The DRR remains complete without LAT citations; it may summarize already-available decisive evidence by value when that evidence materially shaped the content choice. If later LAT or refresh evidence motivates a reopened or revised choice, carry that evidence into the successor DRR or other admissible decision record rather than retrofitting the accepted DRR.

**Example of a LAT‑stub**
```
LAT:
  pattern: F.15, basis: FPF/Core@<edition>, intended-use: <named use>, claim-scope: <scope>, semver: x.y+1, delta-class: Δ-2
  objectives: {clarity↑, universality↑, assurance-cost↓}
  SoTA-pack: {OpenAlex 2025‑Q3, SPECTER2‑23, DPP‑2019, MAP‑Elites‑2015+}
  NQD-settings: {CharacteristicSpace: domain‑family × …, grid: CVT@k=16}
  candidates: K=4 (wording of RSCR‑F04 & gates)
  bridge-ledger: none (intra‑canon refs only)
  assurance‑delta: ΔF=+, ΔG=+, ΔR=+ (after CL‑penalties=0)
  harness: LEX‑BUNDLE lint pass; F‑suite pass; Γ‑consistency ok
  DRR-id: DRR‑2025‑09‑DFCM‑roll‑in
  refresh: {source-cut-policy: <policy-id>@<edition>, reopen-on: [receiving question or use, relied source edition, known rival explanation, action-changing counterexample, transfer boundary]}
```

#### E.15:4.3 - What counts as “changed the pattern as a whole” — **Delta‑Classes & versioning**

Classify the intended change **before** work starts (declare it in the DRR framing; echo it in the LAT or evidence record when one is used):

* **Δ‑0 Lexical polish** — wording/ordering only; **no** change to CC or semantics. → *Patch* (x.y.**z**+1).
* **Δ‑1 Didactic restructure** — narrative/layout; **unchanged** Conformance Checklist (CC). → *Minor* (**x.y**+1.0).
* **Δ‑2 Normative refinement** — CC tightened/clarified; *semantics preserved* by test equivalence. → *Minor* (**x.y**+1.0) + **RSCR** required.
* **Δ‑3 Semantic change** — CC **adds/removes** requirements; downstream requirements shift. → *Major* (**x**+1.0.0) + **impact review** + **bridges refresh**.

> **Definition of “pattern changed as a whole”:** any **Δ‑2/Δ‑3** change (i.e., the **normative surface** or **semantics** changed) counts as a pattern change in the canonical corpus and triggers harness & bridge reviews.

#### E.15:4.4 - Quality & SoTA metrics (selection lenses)

**Mandatory lenses** (declare in LAT; higher is better unless noted):

* **Clarity** (readability; plain‑register score from didactic rubric).
* **Universality** (C‑1): *≥3 heterogeneous domains* anchored in the Archetypal section.
* **Lexical discipline** (E.10): 0 violations (DevOps lexicon, process/function conflations).
* **Assurance delta**: ΔF (formality), ΔG (scope clarity), ΔR (reliability after CL penalties).
* **Cross-local relation integrity**: when an actual F.9 relation between distinct local senses is consumed, name the relation, admitted use, loss notes, and applicable CL policy; penalties route to `R` only under B.3 and F.9, and the policy id is recorded in LAT.
* **Test conformance**: F‑suite pass; RSCR clean.
* **Exploration health** (NQD): diversity coverage > threshold; no premature convergence.
* **Didactic economy**: length vs density ratio within band; “Tell‑Show‑Show” present.

**Optional lenses** (selected for the subject and intended use): *ethical and separation-of-duties guard strength; cross-scale roll-up integrity; aggregation proofs present;* etc.

