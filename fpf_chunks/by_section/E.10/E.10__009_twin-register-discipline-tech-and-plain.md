---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:6.2"
section_title: "Twin‑Register Discipline (Tech and Plain)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__009_twin-register-discipline-tech-and-plain.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:6.2 — Twin‑Register Discipline (Tech and Plain)"
line_start: 70116
line_end: 70191
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
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

### E.10:6.2 - Twin‑Register Discipline (Tech and Plain)

**Plain twin (LEX).** A registry entry pairing the **authoritative Tech label** with a **display-only Plain label** for one governed Tech meaning in one `U.BoundedContext`: an admitted durable U-kind, C.3 `U.Kind`, Concept-Set row, imported signature symbol, or other directly governed value. Governed by **PTG (Plain Twin Governance; in the LEX registry)** and referenced by `Twin-Map ID (LEX)`. *“Plain twin” ≠ the **Plain register** (the register is where twins may be used; the twin is the 1:1 mapping).*
**Convention.** In this spec, **Plain** (capitalized) names the register; **plain twin** (lowercase) names the 1:1 mapping entry.

> **Rule R-0 (Registers).** Every Kernel and extension-pattern concept has a **Tech label** (the testable semantic token) and an optional **Plain label** (didactic synonym). The **Tech label is authoritative**; the Plain label is admitted only in expository text and maps one-to-one to the Tech meaning inside the current **Context**.

#### E.10:6.2.1 - Allowed pairs (normative table; examples)

| **Tech (authoritative)** | **Plain (didactic)**                        | **Notes and guards**                                                                           |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `U.System`               | system, machine, team                        | Bare “service” is **never** a safe Plain twin for `U.System`; treat it as an **always‑unpack** token (L‑SERV, A.6.8). Avoid “service‑instance”; prefer “system instance”, “service access point”, or “service offering” depending on facet. |
| `U.Episteme`             | body of knowledge, document, dataset, model | The pair preserves the **Carrier and Content** distinction (A.7).                                              |
| `U.Method`               | how‑to, procedure (abstract)                | Do **not** call this “process” (L‑PROC).                                                     |
| `U.MethodDescription`    | recipe, SOP, playbook, code, spec‑text      | If testable, call out **Spec** explicitly per E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use).                               |
| `U.Work`                 | run, execution, activity, job, case         | Never use “process” or “procedure” here.                                                     |
| `U.Role`                 | role, hat, mask                             | Always **context‑indexed** per D.CTX.                                                        |
| `U.PromiseContent`              | promise, offering, service offering         | Never equate to provider system or API (L‑SERV).                                             |
| `U.Capability`           | ability, capacity (within bounds)           | Separate from Role, Method, and Work; carries **envelope and measures**.                          |
| `U.Dynamics`             | law of change, model of evolution           | Not a capability or a method.                                                                |

**R‑1 (Plain first‑use).** At first use in a section, show **Tech label** and (optionally) the Plain twin: *“…a `U.Method` (the **how‑to**), described by a `U.MethodDescription` (the **recipe**) …”*
**R-2 (No unpaired Plain in CC).** Conformance Checklists use **Tech labels** only.

Domains can mint aliases inside their `U.BoundedContext` glossary; each alias maps one-to-one to a Tech label through a **SenseCell** row in the Context's **Concept-Set Table** and, when exported across Contexts, through an **Alignment Bridge** with congruence-level and loss fields.

 Make “plain twins” (reader-friendly labels) **safe by construction**, not just style. The plain twin preserves kind, scope, and reader expectations of the canonical Tech name; it is **display-only** and **context-local**.

* **Tech name (tech)** — the canonical, kernel‑conformant label used in **normative** clauses (e.g., `U.RoleAssignment`, `TransformerRole`).
* **Plain twin (plain)** — a didactic **display alias** permitted in **expository** prose and UI display contexts **inside one `U.BoundedContext`**.

> **Principle:** *Meaning lives in the Tech name; the plain twin may never move meaning.* (Locality is enforced by `U.BoundedContext` and Bridges.)

#### E.10:6.2.2 - Plain Twin Safety constraints (normative)

**CC‑TWIN‑1 - One‑to‑one and local.**
Each Tech name has **at most one** plain twin **per `U.BoundedContext`**; one plain twin points to at most one Tech name in the same Context.

**CC‑TWIN‑2 - Sense‑equivalence proof.**
A plain twin binds to the **same SenseCell** as its Tech name in that Context (F.3 and F.7). Its SenseCell notes include at least one **counterexample test** showing how the twin could be misread and why it still passes in this Context.

**CC‑TWIN‑3 - Head‑term discipline (HND).**
The plain twin preserves the **head term** of the Tech name or appends an explicit bracketed head on **first use**:

* Roles keep **“(role)”**, service-facet labels keep **“(service promise or access)”** after the direct FPF target is recovered, Methods keep **“(method)”**, Work keeps **“(work record)”**, Capability keeps **“(capability)”**.
  *Examples:*
  `TransformerRole` → “**Transformer (role)**”,
  `U.PromiseContent` → “**post-op monitoring service promise**”; service-access publication or access relation → “**service access**”,
  `U.Work` → “**work (work record)**”.

**CC‑TWIN‑4 - Kind‑consistent.**
A plain twin does not map across **Kinds** (C.3). If the twin's everyday interpretation can denote a different Kind (e.g., *Tradition* = organization, corpus, domain), it is admitted only with a bracketed head and **Context gloss** on first use (see CC-TWIN-7).

 **CC‑TWIN‑5 - Ambiguity stop‑list.**
The following base nouns are **reserved** and are not admitted as unqualified plain twins: *Tradition, service, process, function, model, system, method, standard, library, dataset, evidence, activity, task, action*.
They are allowed **only** with an explicit head per **CC‑TWIN‑3** and a **Context gloss** (CC‑TWIN‑7). *(This list MAY be extended in the registry.)*

**CC‑TWIN‑6 - No cross‑context by label.**
Plain twins are **not portable**. Reuse in another `U.BoundedContext` is admitted through a **Bridge** with CL and loss notes; names alone carry no authority.

**CC‑TWIN‑7 - First‑use gloss.**
At first occurrence in a document or screen, show a plain twin as **“Plain twin [Tech name] - Context gloss”**, e.g.:
“**Transformer (role)** \[**TransformerRole**] — *work-facing role value assigned through `U.RoleAssignment` to a system or acting holon for method-enacting work in OR\_2025*”.

**CC-TWIN-8 - Normative publication-form overread ban.**
Plain twins are not admitted in **Conformance Checklists, predicates, type signatures, or acceptance clauses**. Only Tech names are normative; Plain twins are strictly didactic.

**CC‑TWIN‑9 - Twin budget.**
**At most one** plain twin per Tech name per Context. Synonym piles are non-conformant because they create uncontrolled vocabulary sprawl (see F.14).

**CC‑TWIN‑10 - Registry entry and DRR.**
Every admitted plain twin has a **registry entry** in the LEX registry recording `tech`, `plain`, `context`, `head`, **SenseFidelity = {3,2,1,0}**, ambiguity notes, counterexamples, and DRR id. A change opens a **DRR**.

**CC‑TWIN‑11 - Tests.**
 Twin entries pass the **Twin Harness** (see F.15): *Head term*, *Kind consistency*, *SenseCell match*, *Stop-list compliance*, and *First-use gloss*.

