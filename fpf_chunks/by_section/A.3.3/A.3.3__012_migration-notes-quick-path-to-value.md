---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics"
section_id: "A.3.3:11"
section_title: "Migration notes (quick path to value)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__012_migration-notes-quick-path-to-value.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.3.3 — U.Dynamics"
  - "A.3.3:11 — Migration notes (quick path to value)"
line_start: 6572
line_end: 6582
dependencies:
  - "A.19"
  - "B.4"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:11 - Migration notes (quick path to value)

1. **Name the changing things.** Pick 3–7 **characteristics** that matter (physical or architectural). Declare `stateSpace` with units and ranges.
2. **Write the law you already use.** Even if it is a queueing approximation or a simple ARIMA—put it under `transitionLaw` and state assumptions under `validity`.
3. **Separate recipe from law.** Move control procedures to `Method or MethodDescription`; keep forecasting/plant equations in `U.Dynamics`.
4. **Wire evidence.** Ensure production `Work` emits the measurements needed by `observation`. Build `trace(Work, D)`.
5. **Start conformance.** Define a simple `tol` and compute `fits(D, trace, tol)` weekly. Raise issues on drift; version the model when calibrating.
6. **Link to promises (optional).** If SLOs depend on the law, reference `U.Dynamics` from `U.PromiseContent` and derive targets transparently.
7. **For KD‑CAL.** Treat belief/support as characteristics; declare a Bayesian/likelihood update in `transitionLaw`; evaluate conformance against evidence arrivals.


