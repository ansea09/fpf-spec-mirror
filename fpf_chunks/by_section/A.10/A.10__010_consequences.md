---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
section_id: "A.10:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__010_consequences.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.10 — Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph"
  - "A.10:7 — Consequences"
line_start: 20402
line_end: 20412
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:7 - Consequences

| Benefit                           | Why it matters                                                                  | Trade‑off / Mitigation                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Cross-scale reproducibility** | Any composite metric or argument can be walked back to its carriers and method. | **Overhead** of maintaining evidence-provenance entries with carrier identity and currentness fields. *Mitigation:* keep entries minimal but complete; use checklists from the pedagogical companion. |
| **DesignRunTag clarity**            | Intent (MethodDescription) is cleanly separated from execution (Work traces).          | **Discipline** needed at boundaries. *Mitigation:* MIC templates; explicit “instantiates” bridges.                                    |
| **Objective evidence**            | Separated evidence-producing work, role assignment, carrier/provenance relation, target claim, and relying context eliminate self-evidence loops. | **Reflexive systems** require explicit work and provenance separation. *Mitigation:* provide reflexive-monitoring examples with reopen triggers. |
| **Comparable numbers over time**  | Temporal coverage invariants prevent “trend” claims built on gaps.              | **Extra dating work** for older data. *Mitigation:* allow provisional labels until dating is completed.                              |
| **Safe composition of knowledge** | Evidence-provenance entries keep source publications, evidence carriers, currentness relations, and provenance relations intact as epistemes are composed, published, compiled, or used for assurance. | **Initial friction** in teams new to carrier thinking. *Mitigation:* start with the ten most important carriers per claim, then expand as needed. |
| **Feeds B.3 typed assurance claims** | Evidence relations provide evidence inputs such as `R` and `CL` only for a named typed assurance claim. | B.3 is not a generic trust or assurance score; cite the claim named by value and relying context. |

