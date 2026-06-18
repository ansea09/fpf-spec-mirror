---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "External Transformer & Reflexive Split"
section_id: "A.12:4.1"
section_title: "The Principle of the External Transformer"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__006_the-principle-of-the-external-transformer.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.12 — External Transformer & Reflexive Split"
  - "A.12:4.1 — The Principle of the External Transformer"
line_start: 19804
line_end: 19822
dependencies:
  - "A.3"
  - "B.2.5"
  - "U.Interaction"
keywords:
  - "agency"
  - "causality"
  - "control loop"
  - "external agent"
  - "self-modification"
---

### A.12:4.1 - The Principle of the External Transformer

Every transformation in FPF is a `U.Work` event that is the result of an **Agent** acting upon a **Target**.

*   **The acting-side assignment:** the acting side is a `U.RoleAssignment` with `holderRef` naming a `U.System` or admitted acting holon, `roleRef=TransformerRole@Context`, and `boundedContextRef` naming the context. This is the causal/work side, not a compact holder-role shorthand.
*   **The Target:** The target is the `U.Holon` being changed. This can be another `U.System` or the **symbol carrier** of a `U.Episteme`.
*   **The Boundary:** The agent and the target are always separated by a `U.Boundary` and interact through a `U.Interaction`.

**Crucial Rule:** The `holder` of the Agent's `U.RoleAssignment` **cannot** be the same holon instance as the Target.
> `holder(Agent) ≠ Target`

This simple inequality is the core of the externalization principle. It constitutionally forbids self-magic.

#### A.12:4.1.1 - Reflexivity vs cross‑reference (normative note)

FPF distinguishes **reflexive transformation** from **episteme‑level reference**.
*Reflexive* cases (e.g., “self‑calibration”) MUST be modeled by the **Reflexive Split** (Regulator→Regulated) and remain within the **world** ReferencePlane.
When a claim **refers to** another claim/episteme, model it with **epistemeAbout(x,y)** and set **ReferencePlane(x)=episteme**. Such references **do not perform transformations** and **MUST NOT** be used to bypass the external‑agent rule. Evaluation of chains of episteme‑about relations MUST remain **acyclic within a single evaluation chain**; otherwise, abstain and request a split or external evidence.

