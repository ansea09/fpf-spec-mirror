---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__002_intent-applicability.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:1 — Intent & applicability"
line_start: 64114
line_end: 64132
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:1 - Intent & applicability

**Intent.** Provide a **conceptual discipline** for relating **SenseCells** from **different Contexts (U.BoundedContext)**. A **Bridge** states *what kind* of relationship holds, *how far* it holds (via **CL: Congruence Level**), and *what is lost* during the translation. Bridges **support carefully scoped reuse** (e.g., a Concept-Set row) while **rejecting silent equivalence**.

**Applicability.** Use **whenever** an author needs to **read across Contexts**—to reuse a familiar label, to connect design-time and run-time notions, to compare two standards’ terms, or to justify a row in the Concept-Set table. This pattern is **not** storage, enactment protocol, or governance; it codifies **thinking moves**.

**Non-goals.** No global meaning; no `PublicationSurface` semantics; no editor roles. Bridges are **semantic relations between local senses**, not transport chains, not processes.
**Governed object in plain terms.** One bridge card relating two `SenseCells` across different `U.BoundedContext`s; not a transport chain, not a workflow, and not one global meaning layer.
**Governing move in plain terms.** Declare relation kind, direction, `CL`, and loss between local senses so cross-context reading stays inspectable without collapsing them into silent equivalence.
**Primary working reader.** The primary working reader is an author, checker, or practitioner preparing one bridge card, one comparative mapping note, or one concept-set row that depends on cross-context reading without pretending the contexts have already collapsed.
**Use this when.** Use this pattern when two local senses from different contexts need one explicit bridge card before a team can admissibly reuse a label, justify a row, or compare the cases without pretending the senses are equivalent or substitutable.
**Start here when.** The same term, role, quality, or status label appears in more than one context and the team is about to treat that overlap as if it were already equivalence, safe substitution, or structure-preserving reuse.
**What goes wrong if missed.** Teams fall back to shared labels, string-equals shortcuts, or informal analogies, then quietly smuggle equivalence, substitution, or structure across contexts without publishing relation kind, `CL`, or loss.
**What this buys.** One explicit bridge discipline that lets a team reuse names, compare contexts, and publish bounded cross-context support without losing track of direction, loss, and the limits of admissible substitution.
**Not this pattern when.** Not this pattern when the case is still only a coarsened source-pinned rendering with no bridge claim yet, or when the real job is storage, enactment, governance, or one single local context rather than explicit cross-context alignment.

**Boundary to controlled coarsening.** This pattern is also the explicit boundary pattern when a simplified or coarsened cross-context rendering starts to imply equivalence, substitution, projection, or interoperability scope. If the case is still only a coarsened source-pinned rendering for narrower use, keep it with that rendering's own source tether, non-admissible-use line, and reopen condition, using `A.6.3.CSC Controlled Semantic Coarsening` when that narrower-use card is primary. A lighter cross-context note may support informal orientation talk, but that is not a formal `F.9` `Naming-only` row. Any bridge, substitution, row, or interoperability claim must reopen the source-bearing episteme or source publication needed for bridge support before a Bridge Card may be published under `F.9`.
**Recognition vs assurance note.** Read **Intent**, **Applicability**, **Non-goals**, and the `A.6.3.CSC` neighbor boundary above as the ordinary recognition block. Read Bridge kinds, `CL`, conformance, and Relations below as assurance blocks that tighten the same bridge-card claim; they do not widen the pattern into transport, workflow, or one global meaning layer.

