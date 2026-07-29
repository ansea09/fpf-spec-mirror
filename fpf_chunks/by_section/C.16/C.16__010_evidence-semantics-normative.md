---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:7"
section_title: "Evidence Semantics (Normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__010_evidence-semantics-normative.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:7 — Evidence Semantics (Normative)"
line_start: 47069
line_end: 47081
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:7 - Evidence Semantics (Normative)

#### C.16:7.1 - What an Evidence Stub is (and is not)

**Definition.** `U.EvidenceStub` is a **conceptual pointer** that ties a **measure** to the **grounds** sufficient for independent checking (observations, arguments, admissible transformations). It is not the run log, not the evidence carrier, and not the characteristic itself. This keeps **EntityOfConcern and Description-episteme boundary and specification use** distinct per E.10.D2 and the Clarity Lattice.

**Rule Σ‑1.** Whether evidence is **required** is a **property of the metric template**; if required, each `U.Measure` **SHALL** include an `U.EvidenceStub`.
**Rule Σ‑2.** Evidence composition is **commutative, associative, idempotent** at the concept level (sets/multisets of grounds); combining grounds can never *reduce* what is knowable about the measure’s warrant.
**Rule Σ‑3.** *Soundness minimum:* there exists a conceptual chain linking **bearer → Characteristic → Scale and Unit → admissible method or episteme**. (No “free‑floating numbers”.)
**Rule Σ‑4.** Any declared *agreement* construct used as evidence (e.g., dual readings, panels) **SHALL** respect the template’s scale type (per A.18) (e.g., order‑based concordance for ordinal; tolerance‑based agreement for interval or ratio).
**Note (boundary).** CG‑frame evidence thresholds (e.g., “minimal evidence” gates used by selection, scoring, or comparison mechanisms) are governed by their FPF patterns or specification records. C.16 defines only the EvidenceStub semantics that such gates may cite.
*Source references:* MM‑CHR units and evidence notion; Strict Distinction and the separation of objects from their descriptions and specifications.

