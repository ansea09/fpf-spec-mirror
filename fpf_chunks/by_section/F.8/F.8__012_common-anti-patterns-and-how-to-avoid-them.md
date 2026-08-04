---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:9"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:9 — Common Anti-Patterns and How to Avoid Them"
line_start: 92024
line_end: 92039
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
  - "C.2.1"
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

### F.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Suffix minting | A word ending in `Role`, `Status`, `Graph`, `Map`, or `Record` becomes ontology. | Recover the exact governed value or relation, direct owner, and proposed use first. |
| Evidence role revival | `EvidenceRole` becomes a role-name family. | Recover the exact evidence-use relation; name it only through its direct owner. |
| Status-role fusion | `ReadyReviewerRole` or `ApprovedRole` names a role plus state. | Separate the work-facing role from the state or status-use relation. |
| Row overuse | A public naming row justifies equivalence, role assignment, or structural inference. | Lower use to the exact F.17 `AdmissibleUse` or repair the row and any required Bridge. |
| Alias with payload | An alias changes kind, scope, occurrence identity, use, or authority. | Treat it as a different decision; use `F.5`, `F.13`, and `F.18`. |
| Source prestige minting | A standard or framework term becomes the selected FPF name by prestige. | Keep it as source wording, evidence for a local sense, or an alias until exact recovery and selection pass. |
| Review label as context | `PatternReview_2026` is used as context, Work, role assignment, evidence, or authority. | Recover the exact dated Work or plan/edition, decision-use claim, or effective ReferenceScheme needed by the actual assertion. |
| Decision record as decision | A filled record is treated as performing a mint decision or creating its result. | Identify the decision occurrence through its direct owner; constitute a separate C.2.1 result episteme only when needed. |
| Naming-object cascade | One expression automatically gets a cell, NameCard, row, identifier, and publication. | Apply F.14 at every gate and create only the next object whose receiving use pays for it. |
| U-kind comfort minting | A new U-kind is proposed because existing names feel awkward. | Attempt reduction to local phrase, existing designation, alias, direct-pattern name, admitted row, existing relation, or existing U-kind; use `E.24.UK` before admission. |
| Policy identifier as magic word | An identifier is used without a separately resolvable specification or mint decision. | Supply the exact references or lower the claim. |

