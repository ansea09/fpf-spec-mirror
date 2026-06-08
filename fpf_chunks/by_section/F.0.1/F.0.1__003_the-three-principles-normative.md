---
chunk_kind: "child"
pattern_id: "F.0.1"
pattern_title: "Contextual Lexicon Principles"
section_id: "F.0.1:2"
section_title: "The Three Principles (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.1/F.0.1__003_the-three-principles-normative.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.0.1 — Contextual Lexicon Principles"
  - "F.0.1:2 — The Three Principles (normative)"
line_start: 68977
line_end: 69027
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.4"
  - "A.7"
  - "A.8"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "U.BoundedContext"
  - "bridge"
  - "congruence"
  - "context"
  - "lexicon"
  - "local meaning"
  - "semantic boundary"
---

### F.0.1:2 - The Three Principles (normative)

#### F.0.1:2.1 - P‑S - **Source Localisation Principle** — *Speak with the Context.*

**Rule.** Every term in a normative FPF publication unit **MUST** be bound to a **specific `U.BoundedContext`** (its “Context of meaning”). The binding is explicit in text, notation, or table headers (e.g., **process (BPMN 2.0)**).

**Implications.**

* No free‑floating “global terms”.
* A finite **Context Map** (see **F.1**) is chosen **before** naming work starts.
* If a source intrinsically fixes time stance, the **DesignRunTag** is carried by the Context (C‑7).

**Reasoning move (conceptual).**
`Context(C) ∧ says(C, term t) ⊢ usable(t@C)`

**Illustration (Enactment line).**
`activity @ PROV‑O (run)` vs `task @ IEC 61131‑3 (run)` vs `process @ BPMN 2.0 (design)`.

#### F.0.1:2.2 - P‑L - **Local Meaning Principle** — *Meaning lives inside the Context.*

**Rule.** The **intended sense** of a term is established **inside its Context** as a **SenseCell**: a small, reconstructible unit of local meaning with **Tech/Plain labels** and a concise gloss. SenseCells are **lexical only** (C‑6): no behaviours, no deontics, no equations.

**Implications.**

* SenseCells are **Context‑scoped**; they do **not** cross Contexts.
* Minimal generality (G‑1) and contextual specification (G‑2) govern naming inside the Context.
* **Intra‑Context clustering** of raw mentions precedes any Cross‑context act (see **F.3**).

**Reasoning move (conceptual).**
`usable(t@C) ∧ fits(gloss, C) ⊢ SenseCell⟨t@C⟩`

**Illustration (KD‑CAL).**
`observation @ SOSA/SSN`: Tech “observation”, Plain “measurement act”; gloss “Result‑bearing act applying a Procedure…”.

#### F.0.1:2.3 - P‑B - **Explicit Bridge Principle** — *across Contexts, only with a bridge.*

**Rule.** Any relation between terms from **different** Contexts **MUST** be stated as an **Alignment Bridge** (see **F.9**): a named mapping between **SenseCell⟨-⟩** items with a declared **relation kind** (e.g., *overlaps*, *broader‑than*, *near‑equivalent*) and a **Congruence Level (CL)** for trust calculus (B.3).

**Implications.**

* No by‑name identity across Contexts; **string equality ≠ sense equality**.
* Bridges carry **loss/fit notes** and are auditable; they can be revised by edition.
* Concept‑Sets (F.7) are built **from bridged cells**, not from lexical strings.
* When the prose wording uses umbrella sameness/alignment tokens (“same/equivalent/align/map/…”), treat it as an RPR trigger and repair it via **A.6.9 (RPR‑XCTX)** before granting any naming or substitution licence.

**Reasoning move (conceptual).**
`SenseCell⟨x@A⟩ ↔⟨rel, CL⟩ SenseCell⟨y@B⟩ ⊢ translatable(x@A, y@B, rel, CL)`

**Illustration (Sys‑CAL × Enactment).**
`actuation @ CTRL‑Text` ↔⟨near‑equiv, CL=2⟩ `control‑output @ IEC 61131‑3`.

