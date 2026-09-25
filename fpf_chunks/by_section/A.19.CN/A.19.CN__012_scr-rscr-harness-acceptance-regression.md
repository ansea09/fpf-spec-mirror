---
chunk_kind: "child"
pattern_id: "A.19.CN"
pattern_title: "CN-frame: Specify and Maintain Comparability and Normalization"
section_id: "A.19.CN:11"
section_title: "SCR / RSCR Harness (acceptance & regression)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CN/A.19.CN__012_scr-rscr-harness-acceptance-regression.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.19.CN — CN-frame: Specify and Maintain Comparability and Normalization"
  - "A.19.CN:11 — SCR / RSCR Harness (acceptance & regression)"
line_start: 33967
line_end: 33989
dependencies:
  - "A.19"
  - "A.6.1"
  - "C.16"
  - "F.9"
  - "G.0"
keywords:
  - "CL/loss notes"
  - "CN-Spec"
  - "CN-frame"
  - "RSG admission hooks"
  - "SCR/RSCR harness"
  - "WLNK discipline"
  - "bridges"
  - "chart"
  - "comparability modes"
  - "conformance checklist"
  - "indicator policy refs"
  - "normalization refs"
  - "registry"
  - "Γ-fold governance"
---

### A.19.CN:11 - SCR / RSCR Harness (acceptance & regression)

> **These are concept‑level checks; notation‑agnostic.**

#### A.19.CN:11.1 - **SCR — Acceptance (first introduction)**

* **SCR‑A19.4‑S01 (Completeness).** CN-Spec has every applicable mandatory value. Each cs_basis position declares its Scale and value meanings, Unit when that Scale has one, and the comparison's polarity or target rule, including no preferred direction when appropriate. The chart names its reference state and coordinate patch; measured values cite their C.16 measurement method/protocol, while evaluated or otherwise ascribed values cite the rule and basis that establish them, as required by CC-A19.D1-2 and CC-A19.D1-3.
* **SCR‑A19.4‑S02 (Normalization clarity).** `normalization` cites the UNM mechanism (`UNM_id?`) and provides the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used). If instances are referenced in assurance logs, their evidence/backing and validity constraints are handled by the governing evidence pattern (C.16), not by A.19.CN.
* **SCR‑A19.4‑S03 (Comparability test).** Provide one worked example showing **coordinatewise** or **normalization‑based** comparison end‑to‑end (with Evidence Graph Ref).
* **SCR‑A19.4‑S04 (Γ‑fold audit).** The aggregation rule states the intended result, law and applicability basis, with only the required property claims; the reviewer reconstructs the result on a toy set under that model.
* **SCR‑A19.4‑S05 (Required certification).** Identify the exact receiving claim/control and relied-on CN-Spec edition or admission basis. If independent certification is required, check the actual certifier against authoring/material-selection history, then the independently applicable authority and examination conditions. Replay both successive same-holder assignments and overlapping different-holder assignments. If certification is not required, keep the adequate comparison explicitly uncertified.
* **SCR‑A19.4‑S06 (bearer and anchors surfaced).** For each CN-Spec characteristic used in the worked example, cite its bearer, Characteristic and Scale editions, reference/comparison basis, scope/window, and the A.10 evidence anchors that support the reading.

#### A.19.CN:11.2 - **RSCR — Regression (on change)**

* **RSCR‑A19.4‑R01 (UNM edit).** When `normalization` changes, flag every comparison and Bridge-use claim that cites that normalization for affected-only reassessment, then rerun the corresponding worked comparisons.
* **RSCR‑A19.4‑R02 (Slot surgery/Basis surgery).** Adding/removing/renaming slot/basis requires a **new edition**; old data remain valid **for their edition**.
* **RSCR‑A19.4‑R03 (Chart drift).** Updating measurement protocol bumps edition; **historic Work** keeps old edition link.
* **RSCR‑A19.4‑R04 (Fold change).** Any change to `Γ_fold` invalidates cached roll‑ups; re‑compute or mark as superseded.
* **RSCR‑A19.4‑R05 (Bridge health).** After either endpoint's scheme, claim, or edition changes, revalidate the Bridge direction, correspondence, and loss before relying on it again; reopen only the claims that use it.
* **RSCR‑A19.4‑R06 (Deprecation rule).** On deprecating a CN‑frame, Registry lists its successor; bridges re‑targeted or retired.
* **RSCR‑A19.4‑R07 (Certification basis).** A change to the relied-on basis, relevant participation history or applicable control reopens only the certification and receiving conclusions it can change. A registry display change alone does not.

