---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:4"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__005_conformance-checklist.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:4 — Conformance Checklist"
line_start: 39621
line_end: 39633
dependencies:
  - "A.10"
  - "A.19"
  - "A.4"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "D.4"
  - "U.Episteme"
keywords:
  - "L0-L2"
  - "LA"
  - "TA"
  - "VA"
  - "assurance levels"
  - "typing"
  - "validation"
  - "verification"
---

### B.3.3:4 - **Conformance Checklist**

To ensure the integrity of the assurance calculus, the following rules are normative. A **Target of Assurance (ToA)** is any working-model element designated as a root claim (e.g., a root system requirement, safety goal, or core hypothesis).

*   **CC-B3.3.1 (L1 Anchor Mandate):** A ToA **SHALL NOT** be considered to have reached `AssuranceLevel:L1` unless it is linked to at least one evidence carrier via `verifiedBy` or `validatedBy`.
*   **CC-B3.3.2 (Concept-Bridge Mandate):** A ToA at `AssuranceLevel:L1` or higher **MUST** be supported by **Concept-Bridge Assurance**. This includes, at a minimum, that its core terms are mapped through the Domain-Concept Bridge (Pattern B.5.3) and conform to their declared schemas, slot relations, or bridge records.
*   **CC-B3.3.3 (L2 V&V Mandate):** A ToA at `AssuranceLevel:L2` **MUST** satisfy all L1 criteria. In addition, it **MUST** be supported by **Verification Assurance (VA)** with `FV ≥ threshold_FV`. For holons designated as safety-critical (e.g., `criticality ≥ SIL-2`), the ToA **MUST** also be supported by **Validation Assurance (LA)** with `EV > 0`. For non-critical holons, LA **SHOULD** be present.
    *   *Exemption Note:* Purely formal epistemes (e.g., mathematical axioms) may justify an exemption from the LA requirement, provided this is documented in the formal episteme's rationale.
*   **CC-B3.3.4 (Concept-Bridge Completeness):** For any mechanism used in a model at `AssuranceLevel:L1` or higher, its load-bearing local terms, slots, and governed values **MUST** be mapped to their declared FPF kinds, relations, characteristics, method values, work values, publication-use relations, or evidence-use relations via the Domain-Concept Bridge (Pattern B.5.3).
*   **CC-B3.3.5 (Scope Separation):** Assurance claims **MUST** maintain a strict separation between `design-time` and `run-time` scopes (Pattern A.4). An assurance tuple for a `MethodDescription` (design-time) SHALL NOT be conflated with one for its corresponding `Work`/`Trace` (run-time). The Evidence Graph Ref (`verifiedBy`, `validatedBy`) must point to evidence carriers or records with the appropriate scope.
* **CC-B3.3.6 (CT2R‑LOG Handshake):** If a ToA depends on **structural** claims, those claims **SHALL** be published as **Working‑Model** relations and, when used to justify `L2`, **SHALL** declare `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.(sum|set|slice)` (see B.3.5 and C.13).
* **CC-B3.3.7 (Downward‑Only Dependence):** Assurance publications or records (Mapping, Logical, Constructive, and Evidence) **SHALL NOT** impose vocabulary or layout back onto the Working‑Model surface (E.14).

