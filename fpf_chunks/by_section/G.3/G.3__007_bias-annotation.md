---
chunk_kind: "child"
pattern_id: "G.3"
pattern_title: "CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
section_id: "G.3:6"
section_title: "Bias‑Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/G.3/G.3__007_bias-annotation.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "G.3 — CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates"
  - "G.3:6 — Bias‑Annotation"
line_start: 102912
line_end: 102921
dependencies:
  - "A.10"
  - "A.15.3"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CHR"
  - "B.3"
  - "B.3.4"
  - "C.16"
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.5.1"
  - "E.5.3"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.Core"
keywords:
  - "CHR Pack@CG-Frame"
  - "CHR authoring"
  - "CSLC lawfulness"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "characteristics"
  - "coordinates"
  - "edition pins"
  - "levels"
  - "scales"
  - "typed measurement"
  - "Φ/CL policy pins"
---

### G.3:6 - Bias‑Annotation

CHR authoring is where many biases become “baked in” as measurement choices. Typical risks:

* **Proxy bias:** a convenient observable substitutes for the intended construct. Mitigation: require `ObservableOf` + ReferencePlane + micro‑examples; force explicit “what is being measured” rather than relying on labels.
* **Population and protocol shift:** a characteristic’s meaning changes when the sampling regime or protocol changes. Mitigation: explicit validity windows and freshness/decay expectations; edition pins for protocol definitions; RSCR triggers on freshness/decay events and evidence surface edits.
* **Ordinal misuse bias:** ordinal ratings treated as interval/ratio by convenience. Mitigation: publish scale type + admissible transforms; legality matrix + guard macros; reject coordinate upgrades without proof hooks.
* **Cross-tradition meaning bias:** an imported expression erases its source-local meaning or makes a changed bearer, scope, window, reference plane, evidence basis, or intended use disappear. Mitigation: name those values, cite exact `F.17` cells and an `F.9` relation only when it obtains, and keep any downstream use and reliance explicit under `F.18`. Loss remains visible through the applicable `G.Core` penalty rule rather than silently altering Part F or Part G semantics.
* **Metric gaming bias (QD and evaluation):** changing descriptors/distances changes what “diverse” means. Mitigation: edition‑pin metric definitions and make role declarations explicit (wiring via `C.18 and C.19`).

