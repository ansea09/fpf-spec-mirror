---
chunk_kind: "child"
pattern_id: "A.13"
pattern_title: "The Agential Role & Agency Spectrum"
section_id: "A.13:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.13/A.13__003_problem.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "A.13 — The Agential Role & Agency Spectrum"
  - "A.13:2 — Problem"
line_start: 23069
line_end: 23077
dependencies:
  - "A.10"
  - "A.12"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "C.16"
  - "C.9"
  - "E.16"
keywords:
  - "U.SystemRoleAssignment"
  - "agency spectrum"
  - "agential participation"
  - "autonomy grading"
  - "local system-role kind"
  - "substrate-neutral autonomy"
---

### A.13:2 - Problem

If agency is treated as a monolithic, intrinsic property or a mere label, four critical failure modes emerge, undermining the rigor of FPF:

1.  **Episteme-as-Actor:** Models might incorrectly assign agency to knowledge epistemes or publications (`U.Episteme`), leading to nonsensical claims like "the specification decided to update the system." This is a direct violation of **Strict Distinction (A.7)**.
2.  **Type Inflation:** Introducing a root agent kind alongside `U.System` and `U.Episteme` would violate **Ontological Parsimony (C-5)**. The same System may qualify for an agential system-role kind and receive an assignment in one working situation but not another. The agency claim states its scope and window separately; a root type cannot express these differences.
3.  **Unfalsifiable Claims:** Without a measurable basis, "agency" becomes a subjective label. A team might call their system an "agent" for marketing purposes, but this claim has no verifiable meaning and cannot be audited, violating **Evidence Graph Referring (A.10)**.
4.  **The Binary Trap:** A simple "agent/not-agent" classification is too coarse. It fails to distinguish between a simple thermostat, a predictive cruise control system, and a strategic, self-learning robotic swarm, even though their cognitive capabilities differ by orders of magnitude.

