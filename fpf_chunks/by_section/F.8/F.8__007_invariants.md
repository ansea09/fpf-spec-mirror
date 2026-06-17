---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__007_invariants.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:5 — Invariants"
line_start: 74261
line_end: 74273
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
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:5 - Invariants

1. **Kind before name.** The candidate's recovered kind or relation comes before the label decision.
2. **One decision, one current use.** Mixed uses are split into separate decisions.
3. **Local before cross-context.** Reuse local sense labels before proposing cross-context rows or new `U.Types`.
4. **Aliases are meaning-preserving.** An alias cannot change kind, scope, use, or authority.
5. **Role names are work-facing.** A role name or RoleDescription label must point to a work-facing `U.Role`; status, evidence, access, source, publication, requirement, assurance, gate, decision, and relation-position uses are direct-pattern names.
6. **Role assignment is not naming.** A name does not assign a holder or prove performed work.
7. **Rows do not exceed their admitted use.** F.8 may reuse a row only at the use declared by `F.7` and admitted by `F.9`.
8. **New `U.Type` candidates are rare.** Cross-family recurrence and irreducibility are necessary; an accepted decision record governs the change.
9. **Policy ids are resolvable.** A policy id needs a policy specification reference and, when introduced, a mint decision reference.
10. **Source labels are not semantic authority.** A source term can be evidence for a local sense or alias, not automatic FPF vocabulary.

