---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__007_worked-slices.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:5 — Worked Slices"
line_start: 60279
line_end: 60302
dependencies:
  - "A.1.CSD"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.43"
keywords:
  - "candidate configuration S1"
  - "constraints"
  - "current configuration S0"
  - "finite change"
  - "interactions"
  - "marginal contribution"
  - "option effects"
  - "result and resource vectors"
  - "transition"
  - "uncertainty"
---

### C.11.CRC:5 - Worked Slices

#### C.11.CRC:5.1 - Flood-pump modernization

Station `FPS7-C19` currently supports bounded discharge use. Compare two ways of operating it over the coming service interval. In `S0` the station continues with its existing diagnostics and scheduled maintenance. In the proposed `S1` it uses an additional bearing-temperature sensor. The change `Δ` includes placement, cabling, controller changes, access for maintenance, calibration and operating procedure. Both forecasts use the same loading scenarios. Neither forecast establishes that the sensor has been installed.

Result coordinates include discharge continuity, failure detection, maintenance access, recoverability, and evidence continuity. Resource coordinates include outage time and maintenance burden plus the resource costs of installation work, calibration, and observation.

Two gaps affect this proposal. Establish whether the proposed location can be reached during an allowed maintenance window. To assess earlier warning, compare the proposed signal with the existing diagnostics under the loads where their indications might differ. A load observation alone cannot establish access. Price each attainable check against the choice it can change (C.11.DUA). If access is impossible at this location, compare a feasible placement or retain the current configuration.

#### C.11.CRC:5.2 - Capability-development programme

For the same later assignment, compare continuing with the present programme and normally available support against adding the proposed practice. Include prerequisites, practice time, the support provider's time and work displaced elsewhere, and the expected time to competent use. Determine what the participant did and what an assistant supplied. A jointly completed artifact can meet the immediate need. To judge a gain in the participant's capability, compare earlier performance with performance on a later comparable task under the support conditions promised for later work. Transfer, retention and detection of critical errors need observations suited to those claims.

#### C.11.CRC:5.3 - Operations constraint intervention

Suppose each unit of output requires both stages of a production line and each stage can process ten units in the period. With continuously divisible output and no other binding constraints, the model maximizes throughput `q` subject to `q ≤ a` and `q ≤ b`, where `a` and `b` are the two capacities. The optimum is `min(a,b)`. Each station by itself bounds the possible throughput. At `a = b = 10` both bounds equal the feasible optimum, and an optimizer can assign dual weights `(1,0)` or `(0,1)`. Raising only the first capacity leaves the optimum at ten, even for an arbitrarily small increase. The unchanged second capacity supplies the decisive bound. Raising both capacities to eleven gives eleven. The value of the coordinated change can therefore exceed the sum of the gains from making each change alone.

A shadow price established for the proposed direction is useful within its range of validity. For a machine purchase, compare the attainable configurations over the decision period, including staffing, maintenance, setup, downstream capacity, energy and resilience where they affect the answer.

#### C.11.CRC:5.4 - Capital allocation

Compare the portfolio over the decision horizon with and without the proposed project. If it would displace another investment, include what that investment would have produced in the feasible alternative. Compare shared resources, cannibalization, risk concentration, financing constraints, staging, irreversibility and information available before later commitments. Corporate Finance supplies the NPV, real-options, scenario and portfolio Methods. Return the finite comparison to that practice or to C.11 when it informs a local choice.

