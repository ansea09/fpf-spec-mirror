---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__004_problem.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:2 — Problem"
line_start: 73817
line_end: 73829
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:2 - Problem

Without this pattern:

1. **Local phrases become durable names.** A temporary phrase outlives its context and looks like FPF vocabulary.
2. **Source names capture FPF.** One tradition's word becomes the selected FPF name before cross-context fit is shown.
3. **Role expressions become role ontology.** `EvidenceRole`, `RequirementRole`, `AccessRole`, or `ProviderRole` is promoted without checking whether a work-facing `U.Role` exists.
4. **Role names hide assignments.** A RoleDescription label is treated as if a holder already has the role.
5. **Concept-Set rows overreach.** A row admitted for naming is reused for assignment, measurement, or structural inference.
6. **Aliases change meaning.** A prettier label is introduced but silently changes kind, scope, or use.
7. **Kernel inflation follows comfort.** A new U-kind is proposed because existing names feel awkward.
8. **Policy ids appear as strings.** A policy identifier is reused or introduced without a resolvable policy specification and decision trace.

