---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:4"
section_title: "Solution — Terms, operator family, invariant Standard, core rules"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__005_solution-terms-operator-family-invariant-standard-core-rules.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:4 — Solution — Terms, operator family, invariant Standard, core rules"
line_start: 29640
line_end: 29763
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "C.2"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:4 - Solution — **Terms, operator family, invariant Standard, core rules**

#### B.1.3:4.1 - Terms (didactic recap)

* **U.Episteme** — a knowledge holon. Internally read it as an `EpistemeSlotGraph`: `EntityOfConcernSlot` for what it is about, `ClaimGraphSlot` or theory/model structure for what it claims, `GroundingHolonSlot` where grounding is live, and SCR/RSCR carrier references for text, code, figures, or datasets.
* **Evidence/Provenance Graph** — edges like **evidences**, **derivesFrom**, **usesMethod**, **isMeasuredBy** with anchors (A.10).
* **Mapping edge** — a typed relation between conceptual vocabularies (e.g., ontology alignment, unit conversion) with a **CL** score (0…3/4 per A.15/B.3 convention).
* **SCR** — a `U.SCR` that lists all symbol carriers included in the aggregate; **never dropped**.
* **Bounded context** — a modelling Standard (vocabulary/units/policy). Crossing it requires **Context Reframe** (B.2) or explicit mappings with CL.

> **Didactic reminders.**
> • Knowledge does **not** “act.” Transformers (A.12) **use** knowledge.
> • **MemberOf** creates **collections**; it is not a semantic argument link. Use **ConstituentOf** for logical/evidential composition.
> • **PhaseOf** is for **versions** of the same episteme; if identity, boundary, or context re‑anchor, declare **MHT**.

#### B.1.3:4.2 - The operator family (companion flavours)

To keep **design vs run** clean (A.15), Γ\_epist has two companion flavours that share the same algebra but serve different moments:

1. **Synthesis (design‑time)** — fold epistemes into a **draft aggregate**

```
Γ_epist^synth : ( D_know : DependencyGraph< U.Episteme >,
                  T      : U.TransformerRole ) → U.Episteme
```

* **Domain.** `D_know` uses **ConstituentOf**, **UsageOf/ReferenceTo**, **evidences/derivesFrom**, optional **MemberOf** for collections.
 * **Result.** A **composite episteme** whose Object/Concept/Symbol components are assembled; **provenance and SCR are preserved**; F/G/R/CL are provisionally computed for later assurance.   **Gating:** at **M‑mode** only tuple placeholders are required; numeric scoring may be omitted (**\[M‑0/M‑1]**). At **F‑mode** the tuple **MUST** be computable in‑Context (**\[F‑\*,L1+]**).  # [M/F]

2. **Compile (run‑time)** — produce the **released artifact** in a bounded context

```
Γ_epist^compile : ( E_synth : U.Episteme,
                    Ctx     : BoundedContext,
                    T       : U.TransformerRole ) → U.Episteme
```

* **Domain.** A synthesized episteme and a **target context** (journal, standard, program spec).
* **Result.** A **context‑anchored** episteme (e.g., published paper/spec) whose **mappings to the context vocabulary** are explicit and carry **CL**; assurance will reference this context baseline (B.3).

**Relationship to Γ\_ctx / Γ\_time.**
If the knowledge fold explicitly depends on **argument order** (e.g., derivation), the internal fold uses **Γ\_ctx** for the sequence. If a **temporal storyline** (updates, retractions) is important, use **Γ\_time** to slice versions; **Γ\_epist** then composes the **current slice**. If composition yields **new explanatory closure** beyond WLNK/CL, declare **MHT** (B.2).

#### B.1.3:4.3 - Invariant Standard (how the Quintet applies; **math by level**)

* **IDEM (Idempotence).** Folding a single episteme returns itself; no accidental “upgrade.”
* **COMM/LOC (Local commutativity / locality).** For **independent** subgraphs (no logical/evidential dependency), fold order/location is irrelevant; when dependencies exist, **Γ\_ctx** controls order explicitly.
* **WLNK (Weakest‑link bound).** Aggregate **Reliability (R)** is bounded by the **weakest supported link** along any justification path, **after** considering the **lowest CL** on mappings used by that path.
* **MONO (Monotonicity).** Strengthening a part (raising **R** with valid evidence or raising **CL** on a needed mapping) cannot lower aggregate **R**. Adding **contradictory** evidence is **not** an improvement; it triggers conflict handling (below), not MONO.

2. **Reliability fold.** Along any support spine, **R\_raw = min\_i R\_i**; apply congruence penalty Φ(CL\_min) → **R\_eff = max(0, R\_raw − Φ(CL\_min))**.  *No averaging; weakest‑link.*
   **Math by level:**
   – **\[M‑0/M‑1]** allow **ordinal** comparisons only (no arithmetic on R); Φ may be stated qualitatively (“low/med/high”).
   – **\[M‑2/L1]** require numeric Φ table (default in §4.4) and reproducibility tag on empirical edges.
   – **\[F‑\*,L1/L2]** require formal derivability of the fold rules from LOG‑CAL; constructive mode annotates `proof.kind=constructive`.  # [M/F]

#### B.1.3:4.4 - Core rules for epistemic aggregation (design‑time synthesis)

When computing **Γ\_epist^synth(D\_know, T)**:

1. **Provenance preservation.**
   The **provenance/evidence graph** is **unioned with de‑duplication**; every claim in the aggregate remains traceable to its sources and methods. No source, method, or dataset that supports a retained claim may be dropped.

2. **SCR construction.**
   Build a **U.SCR** that lists all symbol carriers (texts, code, figures, datasets) that materially participate in the aggregate. Provenance nodes must be mappable to SCR entries.

3. **Object alignment.**
   Determine a **common Object** via domain taxonomy (e.g., **least common ancestor**) or create a `U.CompositeEntity` with explicit **mappings**. Record **CL** for each mapping; **do not** silently merge homonyms.

4. **Concept integration with CL penalty.**
   Compute provisional **F/G/R** of the aggregate:

   * **F\_eff** = min(F\_i) (formality is as strong as the least formal constituent actually used).
   * **G\_eff** = function of coverage; typically **monotone** in included scope, capped by weakest definitional fit.
   * **R\_eff** = min over justification paths of { R\_i along the path } **penalized** by the lowest **CL** used by that path: `R_eff := max(0, min_path( min_claimR(path) − Φ(CL_min(path)) ))`, where **Φ** is the normative penalty function defined below.
      If a mapping with **CL < threshold** is essential to a path, mark the claim **provisional**.
 5. **Normative Penalty Function Φ (v1.0)**
The penalty function `Φ` quantifies the loss of reliability due to poor conceptual alignment between parts.

| Congruence Level `CL_min` | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Penalty Φ(CL_min)** | 1.5 | 1.0 | 0.5 | 0.0 |

*A domain profile **MAY** provide an alternative table but **MUST** preserve monotonic decrease (a lower `CL` cannot have a smaller penalty). The default values are derived from empirical fits in KD-CAL Bench 0.3.*

 6. **Conflict detection (no averaging).**
    Detect contradictions (e.g., `p` and `¬p` with overlapping scope). Do **not** average. Either (i) **separate** by context or scope (bounded contexts; Γ\_time slices), (ii) mark **provisional** with explicit conflict edges, or (iii) if resolution yields **new closure**, consider **MHT**.

7. **Handling of Axiomatic vs. Postulative Epistemes**
   In alignment with ADR-028, the computation of `R_eff` depends on the episteme's declared `mode`.

*   For an input episteme `E_i` with **`mode: axiomatic`**, empirical `R` is N/A; take `R_i_eff = F_i`. **Tag:** `line=formal`.  # [F‑\*]
*   For **`mode: postulative`**, use declared `R_i` with decay; **Tag:** `line=empirical`.  # [M‑1/M‑2/F]
*   The aggregate `E_eff` **MUST** also declare a mode. If all inputs are `axiomatic`, the output is `axiomatic`. If any input is `postulative`, the output **MUST** be `postulative`.
*   **Constructive note.** Under **F‑constructive**, equivalence claims use **isomorphism/equivalence** in the chosen UF library; **CL=2** means proof‑reconstructed alignment, not mere model‑theoretic appeal.  # [F‑constructive]

7. **Order‑aware arguments (optional).**
   If the argument requires premise ordering, embed a **Γ\_ctx** fold inside Γ\_epist; record the **OrderSpec** for reproducibility (NC‑1..3).
   **Gating:** OrderSpec is **recommended** at **M‑1** and **required** at **M‑2/F**.  # [M‑1→F]

8. **No costs here.**
   Any compute/collection effort is **Γ\_work**; attach references but do not mix costs into epistemic aggregation.

#### B.1.3:4.5 - Core rules for compilation (run‑time context anchoring)

When computing **Γ\_epist^compile(E\_synth, Ctx, T)**:

1. **Context bindings.**  # [M‑1+]
   Map all operative concepts/units/claims into **Ctx**; record mappings and their **CL**. If the rebase changes boundary/objective of the episteme (e.g., from descriptive compendium to explanatory theory with commitments), **declare Context Reframe (MHT)** per B.2.

2. **Assurance baseline (gated).**
   Recalculate the **assurance tuple** (B.3) **in Ctx**: F and R may change with formalization and mapping penalties; G is re‑expressed in Ctx’s scope.
   **Gating:**
* **\[M‑0]** narrative justification only;
* **\[M‑1]** qualitative tuples allowed;
* **\[M‑2/L1]** numeric tuple required;
* **\[F‑*/L2]** tuple **and** proof obligations on weight/penalty model selection.  # [M/F]

3. **Release SCR.**
 Produce RSCR with carrier hashes; at **L2** require independent re‑hash verification.  # [M‑1/L2]

4. **Order/time hooks.**
   If the compiled artifact includes an internal derivation, carry the **OrderSpec**; if it codifies a specific **time slice** of evolving knowledge, link back to the **Γ\_time** slice used.

