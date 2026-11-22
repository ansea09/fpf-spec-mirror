---
chunk_kind: "parent"
pattern_id: "E.6"
pattern_title: "Didactic Architecture of the FPF Specification"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/E.6.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "E.6 — Didactic Architecture of the FPF Specification"
line_start: 102966
line_end: 103048
dependencies:
  - "E.2"
keywords:
---

## E.6 - Didactic Architecture of the FPF Specification

> **Status:** Stable

### E.6:1 - Problem frame
Use this pattern when arranging the specification's explanation and practical entry. Readers differ in at least two respects:

* **Disciplinary background** — for example, systems engineering, knowledge science or ethics.
* **Preparation** — some readers need help seeing a relation in use. Others can enter through the definition or operation that answers their question.

### E.6:2 - Problem
The publication needs an explanatory order in which readers can find the grounds needed for later claims. A practical question may require entry into a later Part. Document order must not become a compulsory workflow.


### E.6:3 - Forces

| Force | Tension |
|-------|---------|
| **Cognitive Load** | Formal detail supplies grounds for later reasoning, but too much detail at the outset can obscure the opening explanation. |
| **Conceptual Integrity** | A general account must preserve the distinctions its reader needs. A concrete case can reveal one of them while supplying a choice that the reader needs to learn to make. |
| **Didactic order vs practical entry** | The order of Parts is stable, while a first practical route that fits the reader’s question may cross Parts. |

### E.6:4 - Solution — Order the explanation and keep practical entry separate

#### E.6:4.0 - Document order is distinct from first-practical entry

The document's macro-order organizes explanation. It does not prescribe one practical workflow. Apply `E.11.PFP` to the compact opening and navigation.

After the Table of Contents, the Readme offers recognizable working questions and direct entries. The Architectural Reference explains the whole pattern language, its cross-cutting ideas, connections and architectural choices, including introductory explanation.

Choose the opening from the reader’s question. What are they trying to understand, do or construct? Which whole, constituent or relation is the question about, and what must the model let them distinguish? Begin where the reader can obtain the first grounds or perform the first operation they need. Follow its contribution to the promised result across Parts when necessary. E.11 helps when several plausible entries would lead to different work.

Keep the main explanatory sequence recoverable:

1. **Readme and Architectural Reference.** The Readme helps a reader find a first useful result. The Architectural Reference explains the connected language and its rationale. Its introductory System and Episteme stories build intuition before the kernel exposition.
2. **Part A — Kernel Architecture.** Introduce the holonic ontology and acting-side externalization in A.12.
3. **Part B — Trans-disciplinary Reasoning.** Explain the reasoning moves and their grounds for the kinds of things each question concerns. Use E.7 to show how the reasoning applies.
4. **Part C — Kernel Extension Specifications.** Develop the calculi and extension patterns whose questions use those foundations.
5. **Part D — Multi-scale Ethics and Conflict Optimization.** Introduce the reflective ethical and conflict questions with the needed holonic distinctions available.
6. **Part E — Constitution and Authoring Guides.** Place framework governance and contributor guidance after the principal kernel and reasoning exposition so an ordinary first use need not begin with authoring rules.
7. **Part F — Unification Suite.** Keep concept-set, sense and system-role unification methods in their own Part. Reach them directly when the question calls for them.
8. **Part G — Discipline SoTA Patterns Kit.** Keep the discipline source-synthesis, comparison and refresh methods in their own Part.

Part H remains reserved. Examples and extended explanations belong with the pattern whose contribution they explain. Tooling guides and executable examples follow their separate family and lexical rules.

This publication order does not require readers to traverse every Part. Practical entries return to the pattern needed by the reader’s question.

### E.6:5 - Archetypal Grounding (System / Episteme)

Consider a reader who wants to understand how a whole can depend on its constituents. The two reading paths below show how an introductory account, a definition and an application can contribute to that question. The physical arrangement and the grounds for a synthesis require different relations among constituents. A reader who needs only the criterion for one kind can enter at its definition.

| Place in the publication | First sight of `U.System` | First sight of `U.Episteme` |
|-----------------|---------------------------|-----------------------------|
| Architectural Reference | Coffee‑machine story (pump as system). | Meta‑analysis story (study bundle as episteme). |
| Part A | Formal definition states the System criterion and applicable boundary conditions. | Formal definition states the Episteme criterion. F‑G‑R coordinates characterize a claim under the C.2.2 profile. |
| Part B, worked applications | B.1.2:5.1: identify pump-skid parts and external relations for an aggregation decision. | B.1.3:5.1: synthesize a study bundle into a bounded guidance statement. |

### E.6:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑DA.1** | Each Part **SHALL** open with a one-paragraph situational introduction before formal text. |
| **CC‑DA.2** | Every architectural pattern **MUST** ground its rule under E.7 in the practitioner's question, the kinds of things it concerns and the relation that warrants the answer. |
| **CC‑DA.3** | Governance patterns (**Part E**) **SHALL NOT** appear before the Kernel in the main document flow. |
| **CC‑DA.4** | Navigation aids **SHALL** distinguish document order from first-practical entry guidance. First-entry pattern-comparison guidance and expanded entry-disambiguation cases are informative and MAY cross Parts without implying a universal process history. |

### E.6:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Readers can choose introductory explanation or direct entry to the pattern they need. | Authors must maintain the explanation and entry guidance under E.8. |
| Grounding can be read beside the claims it explains. | The Architectural Reference's introductory examples evolve when new archetypes are added. Their change is handled through the relevant architecture decision. |

### E.6:8 - Rationale
A reader needs grounds for using the rule in the work at hand. A direct demonstration can establish them. A contrasting application earns its place when it reveals a condition that the first leaves open. The document order and E.7 make those grounds accessible while practical entries can cross Parts. This serves **P‑2 Didactic Primacy** and **P‑1 Cognitive Elegance**.

### E.6:9 - Relations
* **Depends on:** `pat:constitution/guard‑rails` (GR-1 governs implementation detail and necessary subject syntax).
* **Constrains:** Placement of Parts, patterns, and their explanatory examples.
* **Instantiates pillars:** P‑1, P‑2

### E.6:End

