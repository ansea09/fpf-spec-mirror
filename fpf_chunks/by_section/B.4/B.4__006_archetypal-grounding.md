---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__006_archetypal-grounding.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:5 — Archetypal Grounding"
line_start: 38609
line_end: 38640
dependencies:
  - "A.12"
  - "A.15.1"
  - "A.4"
  - "B.3"
  - "B.4"
  - "B.4.1"
  - "B.5"
  - "B.5.1"
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

The phase names can be shared, but each subject branch keeps its own identity and return-to-use rule.

* **B.4.1 - Observe -> Notice -> Stabilize -> Route (optional pre-abductive route):**
  * **Context:** A fleet of autonomous delivery drones (`U.System`) is in operation, and operators begin to notice that winter deliveries feel "off" before a clean anomaly statement exists.
  * **Loop Example:**
    1. **Operate:** The drones perform deliveries.
    2. **Observe:** The monitoring service and named operators perform observation Work and find recurring cold-weather battery strain, but the cue still has low articulation.
    3. **Optional B.4.1 route inside Observe:** A named team performs stabilization Work. Under `A.16.1`, a `U.PreArticulationCuePack` preserves the cue nucleus, primary witness traces, and current language-state position without pretending that a final anomaly or action record exists; when the pack is made available for this use, name the separate publication occurrence under `E.24.PUB`. The same or another team performs routing Work. Under `B.4.1`, a `RoutedCueSet` keeps multiple continuations visible—for example, battery-chemistry investigation or route-planning adjustment; again, name its publication occurrence under `E.24.PUB` when availability matters.
    4. **Continue the loop:** The selected route enters Refine or another fitting subject pattern. Only a selected and tested change proceeds to Deploy and renewed drone operation.

* **Knowledge-instantiation slice (theory refinement loop):**
  * **Context:** A scientific theory of protein folding (`U.Episteme`) is used to predict structures.
  * **Loop Example:**
    1. **Operate:** Named researchers perform theory-application Work using the current theory episteme.
    2. **Observe:** A research lab performs observation Work. A separately identified `C.2.1` finding episteme states that the current theory fails to predict the structure of a protein class; name separately any `E.24.PUB` publication occurrence that makes this finding available.
    3. **Refine:** A research team performs revision and testing Work. A later theory episteme, identified under `C.2.1` from its changed claim content, includes a term for the new protein class. Assert an edition relation between the two theory epistemes only if that relation obtains.
    4. **Deploy:** The team performs publication Work for the later theory. The publication occurrence, journal acceptance, admission into a configured knowledge base, and later community use are separate relations. **Note.** The *chart* and any CG-frame readings derived from this episteme MUST cite the updated `MethodDescription` (per A.19.CN CC-A19.D1-3) to keep comparability auditable.

  **Adaptive-specialization note.** Knowledge instantiation for one declared task family **SHALL** name the prior basis being refined from, the named work-measure threshold being pursued, the adaptation budget being spent, and the freshness or provenance basis for claiming the specialization is reusable. If the refinement is claimed as one specialization step, it **SHALL** also cite the declared `TaskFamily` or `TaskSignature` anchor consumed by `C.22.1`, `G.5`, and `G.9`. This keeps the refinement legible as contextual task-family specialization rather than vague general capability growth.

* **Method-instantiation slice (adaptive method loop):**
  * **Context:** A field-maintenance organization uses a declared inspection-and-repair Method (`U.Method`) described by one current `U.MethodDescription`.
  * **Loop Example:**
    1. **Operate:** Maintenance teams perform dated maintenance Work that enacts the current Method.
    2. **Observe:** A reviewer performs review Work and records that the time from fault detection to safe restoration repeatedly exceeds the allowed window.
    3. **Refine:** Method maintainers perform revision and testing Work. A wording clarification can yield a later MethodDescription while the same Method remains current. Adding an earlier isolation action or changing a classification checkpoint can instead change identity-bearing Method semantics; decide under `A.3.1` whether the result is a refinement, substitute, or distinct successor Method, and use `B.1.5` if its composition changes. Then identify the MethodDescription episteme that describes the chosen Method.
    4. **Deploy:** A named publishing team performs publication or release Work for the later MethodDescription and, where needed, configuration or training Work for renewed Method use. Decision results, authority, acceptance, admission, and later Work that enacts the Method remain separate. Completed maintenance Work is never revised.

  **Adaptive-specialization note.** Method instantiation for one declared task family **SHALL** name the narrower higher-fit specialist method or specialist portfolio being activated, the refinement budget being spent, the escalation or commit checkpoints, and the fallback when that method fails. If the method update is being used as evidence of specialization, the note **SHALL** keep the bearer of that specialization explicit: the holder, dyad, team, or scoped portfolio carries the claim; the method is only one selected vehicle. This keeps method evolution reviewable as bounded specialist acquisition rather than as hidden budget inflation.

