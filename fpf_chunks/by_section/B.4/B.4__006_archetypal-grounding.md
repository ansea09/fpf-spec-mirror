---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__006_archetypal-grounding.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:5 — Archetypal Grounding"
line_start: 39697
line_end: 39728
dependencies:
  - "A.12"
  - "A.4"
  - "B.4.1"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "knowledge refinement"
  - "method refinement"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:5 - **Archetypal Grounding**

The Canonical Evolution Loop is universal. It applies identically to the evolution of physical systems, bodies of knowledge, and operational methods. The following sub-patterns show how the loop becomes more explicit in neighbouring patterns.

*   **B.4.1 - Observe -> Notice -> Stabilize -> Route (pre-abductive seam):**
    *   **Context:** A fleet of autonomous delivery drones (`U.System`) is in operation, and operators begin to notice that winter deliveries feel "off" before a clean anomaly statement exists.
    *   **Loop Example:**
        1.  **Operate:** The drones perform deliveries.
        2.  **Observe:** A monitoring-service System and named operator Systems perform observation Work and notice recurring cold-weather battery strain, but the evidence still has low articulation.
        3.  **Stabilize:** A named team System performs stabilization and publication Work, producing a `U.PreArticulationCuePack` that preserves the cue nucleus, the primary witness traces, and the current language-state position without pretending that a final anomaly or action record already exists.
        4.  **Route:** The same or another admitted System performs routing and publication Work, producing a `RoutedCueSet` that keeps multiple admissible continuations visible (for example, battery-chemistry investigation versus route-planning adjustment) so that endpoint patterns can take over without losing the early signal.

*   **Knowledge-instantiation slice (theory refinement loop):**
    *   **Context:** A scientific theory of protein folding (`U.Episteme`) is being used to predict structures.
    *   **Loop Example:**
        1.  **Operate:** Named researcher Systems perform theory-application Work.
        2.  **Observe:** An admitted research-lab System performs observation and publication Work, producing a finding about a new class of proteins whose structure the theory fails to predict.
        3.  **Refine:** Another admitted research-team System performs revision Work, changing the theory's design-time description by adding a term that accounts for the new protein class.
        4.  **Deploy:** The team System performs publication Work for the revised theory. Its acceptance by the journal, admission into any configured knowledge base, and later use by members of the scientific community are separate relations. **Note.** The *chart* and any CG‑frame readings derived from this episteme MUST cite the updated `MethodDescription` (per A.19.CN CC‑A19.D1‑3) to keep comparability auditable.

      **Adaptive-specialization note.** Knowledge instantiation for one declared task family **SHALL** name the prior basis being refined from, the named work-measure threshold being pursued, the adaptation budget being spent, and the freshness or provenance basis for claiming the specialization is reusable. If the refinement is claimed as one specialization step, it **SHALL** also cite the declared `TaskFamily` or `TaskSignature` anchor consumed by `C.22.1`, `G.5`, and `G.9`. This keeps the refinement legible as contextual task-family specialization rather than vague general capability growth.

*   **Method-instantiation slice (adaptive method loop):**
    *   **Context:** A field-maintenance organization uses a declared inspection-and-repair method (`U.Method`).
    *   **Loop Example:**
        1.  **Operate:** Admitted maintenance-team Systems perform maintenance Work that enacts the current Method.
        2.  **Observe:** A named reviewer System performs review Work and records that the time from fault detection to safe restoration repeatedly exceeds the allowed window.
        3.  **Refine:** Named method-maintainer Systems perform revision Work, changing the design-time `MethodDescription` by adding an earlier isolation step and a clearer classification checkpoint. Any responsibility or authority they bear is stated through a separately obtaining direct relation.
        4.  **Deploy:** A named System performs publication and release Work for the revised `MethodDescription`. Another named System may perform decision Work. State any authority or permission through its independently obtaining direct relation; the Work itself supplies neither. Keep the decision-result episteme produced by that Work separate from acceptance or admission, and assert acceptance, admission, or later use only through the direct relation and actual participants that establish it. **Note.** Method evolution MUST be recorded as `Γ_method` composition over `U.Method` (design‑time) and separated from `U.Work` (run‑time), with design-rationale references attached (per A.4/B.1.5).

      **Adaptive-specialization note.** Method instantiation for one declared task family **SHALL** name the narrower higher-fit specialist method or specialist portfolio being activated, the refinement budget being spent, the escalation or commit checkpoints, and the fallback when that method fails. If the method update is being used as evidence of specialization, the note **SHALL** keep the bearer of that specialization explicit: the holder, dyad, team, or scoped portfolio carries the claim; the method is only one selected vehicle. This keeps method evolution reviewable as bounded specialist acquisition rather than as hidden budget inflation.

