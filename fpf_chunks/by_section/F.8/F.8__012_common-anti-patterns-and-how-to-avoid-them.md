---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:9"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:9 — Common Anti-Patterns and How to Avoid Them"
line_start: 95540
line_end: 95555
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
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
  - "F.19"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "admission before naming"
  - "alias"
  - "designation"
  - "durable naming"
  - "governed value or relation"
  - "local phrase"
  - "proposed naming use"
  - "row use"
  - "subject before name"
---

### F.8:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Suffix minting | A word ending in `Role`, `Status`, `Graph`, `Map`, or `Record` becomes ontology. | Recover the governed value or relation, subject pattern, and proposed use first. |
| Evidence-role revival | `EvidenceRole` becomes a system-role-kind name family. | Recover the evidence-use relation; name it only through its subject pattern. |
| Status-system-role fusion | `ReadyReviewerRole` or `ApprovedRole` names a local system-role kind plus state. | Separate the system-role kind from the assignment-state or status-use relation. |
| Row overuse | A public naming row justifies equivalence, system-role assignment, or structural inference. | Lower use to the F.17 `AdmissibleUse` or repair the row and any needed Bridge. |
| Alias with payload | An alias changes kind, scope, occurrence identity, use, or authority. | Treat it as a different decision; use `F.5`, `F.13`, and `F.18`. |
| Source prestige minting | A standard or framework term becomes the selected FPF name by prestige. | Keep it as source wording, evidence for a local sense, or an alias until the subject and naming use are recovered and a designation is selected. |
| Review label as context | `PatternReview_2026` is used as context, Work, system-role assignment, evidence, or authority. | Recover the dated Work, plan or edition, decision-use claim, or naming ReferenceScheme needed by the assertion. |
| Decision identifier or record as decision | An identifier or filled record is treated as the decision occurrence or as creating its result. | Recover the occurrence through the decision or choice pattern, predicate, actual participants, applicability, and identity rule that establish it. If none is available, return `missing-governor`; constitute a separate C.2.1 result episteme only when needed. |
| Naming-object cascade | One expression automatically gets a cell, NameCard, row, identifier, and publication. | Apply F.14 at every gate and create only the next object whose receiving use pays for it. |
| U-kind comfort minting | A new U-kind is proposed because existing names feel awkward, and F.8 is asked to name or admit it. | Return `blockOrLowerUse`; recover the object through E.24.CD when needed, let E.24.UK settle admission, and reopen naming only for the object named by that stable result. |
| Policy identifier as magic word | An identifier is used without a separately resolvable specification, or its mint history is called accountable, cited, replayable, normative, or reusable across the local boundary without an occurrence basis. | Supply the specification for every identifier. For the stronger history claim, supply its direct occurrence basis or return `missing-governor`; a merely local non-accountable identifier does not manufacture one. |

