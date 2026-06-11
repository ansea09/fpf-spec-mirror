---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:6"
section_title: "Method Interface Standard (MIC) — template & examples"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__007_method-interface-standard-mic-template-examples.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:6 — Method Interface Standard (MIC) — template & examples"
line_start: 30368
line_end: 30422
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.3.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
keywords:
  - "concurrent"
  - "method composition"
  - "plan vs run"
  - "sequential"
  - "workflow"
---

### B.1.5:6 - Method Interface Standard (MIC) — template & examples

#### B.1.5:6.1 - MIC template (normative content)

```
Method Interface Standard (MIC)
  name:                human-readable identifier
  version:             semantic label of this MIC
  orderSpecHash:       hash(OrderSpec σ + step signatures)
  externalInteractions:
    - id:              external op name
      mode:            {Promote | Forward | Encapsulate}
      signature:       state/action types (typed interface)
      preconditions:   predicates that must hold at call
      postconditions:  predicates guaranteed on return
      qosEnvelope:     optional envelope (throughput, latency, quality)
  invariants:
    - textual/logical invariants preserved by the method
  notes:
    - rationale for Promote/Forward/Encapsulate choices
```

#### B.1.5:6.2 - MIC excerpts (didactic)

* **Manufacturing method MIC excerpt**

  ```
  externalInteractions:
    - id: Start
      mode: Promote
      signature: Start(): Promise<BatchId>
      preconditions: LineReady & MaterialsAvailable
      postconditions: BatchId issued
    - id: PrimerMixingPort
      mode: Encapsulate
  invariants:
    - FunctionalTest.Pass implies TorqueTolerance ≤ δ
  ```

* **Evidence method MIC excerpt**

  ```
  externalInteractions:
    - id: Submit
      mode: Promote
      signature: Submit(): Promise<SubmissionId>
      preconditions: ManuscriptReady & SCRComplete
      postconditions: DOI assigned on accept
    - id: CrossValidate.Folds
      mode: Forward
      signature: Folds(k: Int): Report
  invariants:
    - Report.metrics computed on held-out data only
  ```

