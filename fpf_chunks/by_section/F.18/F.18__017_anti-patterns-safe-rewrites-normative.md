---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:16"
section_title: "Anti‑patterns & safe rewrites (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__017_anti-patterns-safe-rewrites-normative.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:16 — Anti‑patterns & safe rewrites (normative)"
line_start: 75608
line_end: 75639
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:16 - Anti‑patterns & safe rewrites (normative)

> Each item names a **speaking error** and a **local‑first repair**. Use this as an author’s lint pass before proposing a unified name.

| #  | Anti‑pattern (do **not** say)                           | Why it fails                                                    | Safe rewrite (how to speak)                                                                                         |
| -- | ------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| A1 | “These terms are the same **because they look alike**.” | Cross‑context **spelling** is not evidence of conceptual identity. | “We assert sameness **via a Bridge**; the loss note explains what survives across Contexts.” (F.9)                     |
| A2 | “Use the BPMN word as our Tech label.”                  | Imports BPMN’s local commitments into the unified term.         | “Choose a **neutral** Unified Tech label; cite BPMN as a **SenseCell** in the row.” (F.5, F.17 §6)                  |
| A3 | “Merge *process* (recipe) with *process* (execution).”  | Collapses **MethodDescription** with **Work**.                  | “Split the concepts: one row for **MethodDescription**, another for **Work**; align them in examples.” (F.11/F.16)  |
| A4 | “Our name encodes the process phase.”                 | Process-phase phrasing sneaks in time.                              | “Name the **concept**; show **state-space** changes in examples, not in the label.” (A-series CHR rationale)        |
| A5 | “Contextless glossary.”                                 | Violates local‑first; readers re‑globalise.                     | “Publish a **UTS** per thread; each row lists **Contexts** (Contexts+editions).” (F.17)                                |
| A6 | “We’ll fix synonyms later.”                             | Synonym sprawl grows costs.                                     | “Apply **E.10** rules now: one Tech, one Plain; retire extras via **F.13**.”                                        |
| A7 | “One mega‑row for everything service‑like.”             | Bundles distinct concepts; harms teachability.                  | “One **Concept‑Set per idea**; group with a **Block Plan** for pedagogy.” (F.17 §7)                                 |

#### F.18:16.1 - Canonical semantic unpacking for “contract” language (normative; used across FPF)

In FPF, everyday “contract” talk is treated as shorthand for a bundle of distinct roles. When precision matters (architecture, audit, compliance), authors **SHALL** avoid mapping “contract” to a single concept and instead disambiguate at least:

* **Service / promise clause (`U.PromiseContent`)** — the promised external effect + acceptance criteria (a spec/Standard), not a run (`U.Work`).
* **Utterance (`U.SpeechAct`)** — the published statement (a Description) that declares or invokes the promise content.
* **Commitment (`U.Commitment`)** — the deontic bond that binds an accountable `U.Agent` or `U.Role` to the promise content.
* **Work & evidence (`U.Work` + carriers)** — the actual enactment and the traces/metrics used to adjudicate fulfilment.

A “contract” bundle typically spans the whole A.6.B square; assign each piece explicitly to its A.6.B value:

* `L-*`: definitions/invariants of the signature (“what it means”).
* `A-*`: admissibility/entry predicates (“when it can be applied”).
* `D-*`: duties/SLAs/penalties and who is accountable (“who is bound to what”).
* `E-*`: evidence/observability claims (“how fulfilment/violation is adjudicated”).

Example 2 (§F.18:18.2) shows one naming instantiation of this unpacking.

