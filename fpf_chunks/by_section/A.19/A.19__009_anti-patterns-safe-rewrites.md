---
chunk_kind: "child"
pattern_id: "A.19"
pattern_title: "CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
section_id: "A.19:7"
section_title: "Anti‑patterns → safe rewrites"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19/A.19__009_anti-patterns-safe-rewrites.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.19 — CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)"
  - "A.19:7 — Anti‑patterns → safe rewrites"
line_start: 23326
line_end: 23353
dependencies:
  - "A.17"
  - "A.18"
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.2.5"
  - "A.3.3"
  - "C.16"
  - "E.18"
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

### A.19:7 - Anti‑patterns → safe rewrites

_The following are common modeling mistakes (“anti-patterns”) related to measurement spaces, and how to correct them:_

-   **“Same label ⇒ comparable.”**
    ✗ _Assuming_ **Ready@contextA ≥ Ready@contextB** _just because both states are called "Ready"._
  ✓ **Explicitly normalize and bridge contexts:** Define an Alignment **Bridge (B→A)** and appropriate **NormalizationMethods** for the underlying metrics. Then compare by first translating one state’s coordinates (compute **N(x)** as NCVs in the target space) and using `≼_coord` on the result.

-   **“Compare before landing.”**
    ✗ Comparing values directly across different scales, e.g. _Drift\_A = 5°C vs Drift\_B = 5°F_ as if they were the same.
  ✓ **Normalize to common units first:** e.g., apply the Fahrenheit‑to‑Celsius **NormalizationMethod** _m_(T_F) = (T_F − 32) × 5/9 to convert all data to °C, **then** compare the drift values. Always **normalize into one space** before comparing magnitudes.

-   **“Checklist = workflow.”**
    ✗ Defining a state’s checklist with an implied sequence: _“State ‘Ready’ requires doing Step 1 then Step 2…”_
    ✓ **Keep checklists declarative:** A **Checklist** should represent a state of the system (a condition) – essentially **state evidence** – not a sequence of actions. If order or process matters, model that explicitly via a **MethodDescription** or by using a **Γ** (Gamma) aggregator for process logic. In other words, state = “Ready” might require conditions A and B to be true (regardless of how you got there), whereas the procedure to get ready (do Step1 then Step2) should be a separate method or playbook.

-   **“Retro-fix past assertions.”**
    ✗ Going back to edit or reinterpret old StateAssertions after changing a threshold or NormalizationMethod (e.g. “We updated the criteria, let’s ‘fix’ last quarter’s records to match”).
    ✓ **Never alter historical assertions:** **Leave history as‑is.** If criteria change, issue new assertions under the new criteria going forward, and if needed, explicitly **version** the **NormalizationMethod/UNM** or checklist. Past assertions remain valid for the old version and their time; new ones apply henceforth. This ensures auditability and avoids erasing or rewriting what was true under earlier standards.


**C.27 temporal-claim relation.**

- C.27 may flag: a rate/rate-change claim that needs base characteristic, scale/unit, time base or sampling window, transformation/finite-difference method, evidence, and admissible use.
- This pattern keeps: CharacteristicSpace coordinate discipline and the measurement/coordinate relation carried with C.16.
- Non-admissible use: derivative-like words such as velocity, acceleration, throughput, cadence, or recovery speed do not make a free characteristic, metric, or measurement template.
- Exit: when the reading is load-bearing, cite `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and `C16RouteRef`; C.27 does not define a parallel measurement system.

