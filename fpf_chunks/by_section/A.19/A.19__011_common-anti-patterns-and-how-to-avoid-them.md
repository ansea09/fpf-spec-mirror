---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__011_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 28096
line_end: 28128
dependencies:
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.ECS"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.2.5"
  - "A.3.3"
  - "A.6.5"
  - "C.16"
  - "E.18"
  - "E.2.DA"
  - "E.21"
  - "E.24"
  - "E.24.PUB"
  - "E.9.DA"
  - "G.0"
keywords:
  - "CharacteristicSpace"
  - "U.Dynamics.stateSpace"
  - "coordinatewise comparability"
  - "declared Characteristics and Scales"
  - "embedding"
  - "product"
  - "role-specific space refs stay outside A.19"
  - "state trajectories"
  - "structural overlays"
  - "subspace"
---

### A.19:7 - Common Anti-Patterns and How to Avoid Them

_The following are common modeling mistakes (“anti-patterns”) related to measurement spaces, and how to correct them:_

-   **“Same label ⇒ comparable.”**
    ✗ _Assuming_ **Ready@contextA ≥ Ready@contextB** _just because both states are called "Ready"._
  ✓ **Explicitly normalize and bridge contexts:** Define an Alignment **Bridge (B→A)** and appropriate **NormalizationMethods** for the underlying metrics. Then compare by first translating one state’s coordinates (compute **N(x)** as NCVs in the target space) and using `≼_coord` on the result.

-   **“Compare before common-space mapping.”**
    ✗ Comparing values directly across different scales, e.g. _Drift\_A = 5°C vs Drift\_B = 5°F_ as if they were the same.
  ✓ **Normalize to common units first:** e.g., apply the Fahrenheit-to-Celsius **NormalizationMethod** _m_(T_F) = (T_F - 32) × 5/9 to convert all data to °C, **then** compare the drift values. Always **normalize into one space** before comparing magnitudes.

-   **“Checklist = method sequence.”**
    ✗ Defining a state’s checklist with an implied sequence: _“State ‘Ready’ requires doing Step 1 then Step 2…”_
    ✓ **Keep checklists declarative:** A **Checklist** should represent a state of the system (a condition) – essentially **state evidence** – not a sequence of actions. If order or process matters, model that explicitly via a **MethodDescription** or by using a **Γ** (Gamma) aggregator for process logic. In other words, state = “Ready” might require conditions A and B to be true (regardless of how you got there), whereas the procedure to get ready (do Step1 then Step2) should be a separate method or playbook.

-   **“Retro-fix past assertions.”**
    ✗ Going back to edit or reinterpret old StateAssertions after changing a threshold or NormalizationMethod (e.g. “We updated the criteria, let’s ‘fix’ last quarter’s records to match”).
    ✓ **Never alter historical assertions:** **Leave history as-is.** If criteria change, issue new assertions under the new criteria going forward, and if needed, explicitly **version** the **NormalizationMethod** or **UNM** declaration or checklist. Past assertions remain valid for the old version and their time; new ones apply henceforth. This ensures auditability and avoids erasing or rewriting what was true under earlier standards.

**C.27 temporal-claim relation.**

- C.27 may flag: a rate or rate-change claim that needs base characteristic, scale and unit, time base or sampling window, transformation or finite-difference method, evidence, and admissible use.
- This pattern keeps: CharacteristicSpace coordinate discipline and the measurement-coordinate relation carried with C.16.
- Non-admissible use: derivative-like words such as velocity, acceleration, throughput, cadence, or recovery speed do not make a free characteristic, metric, or measurement template.
- Use boundary: when the interpretation governs the current claim, cite `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and the C.16 measurement or construction relation reference; C.27 does not define a parallel measurement system.

**A.19.ECS object-under-improvement evaluation construction relation.**

- A.19 defines `CharacteristicSpace` as an ontological structure: slots, characteristics, scales, value sets, overlays, and comparability boundaries.
- A.19.ECS governs the construction of one object-under-improvement evaluation `CharacteristicSpace` for an object being improved. It is used before `E.22` and `E.23` when no adequate object-under-improvement evaluation exists.
- Existing object-under-improvement evaluation patterns such as `E.21`, `E.9.DA`, `E.2.DA`, and the naming vector inside `F.18` are examples of this construction shape for object kinds under improvement. They keep their own coordinate, value-meaning, and stop-condition definitions.

