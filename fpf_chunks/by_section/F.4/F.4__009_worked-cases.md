---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:7"
section_title: "Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__009_worked-cases.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:7 — Worked Cases"
line_start: 91330
line_end: 91363
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "C.3.2"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.5"
  - "F.9"
keywords:
  - "classification criterion"
  - "description episteme"
  - "effective scheme"
  - "local kind"
  - "non-inference boundary"
  - "system-role-kind description"
---

### F.4:7 - Worked Cases

#### F.4:7.1 - Pump Inspector System Role

`PumpInspectorSystemRoleKindDescription` is a C.2.1 episteme whose EntityOfConcern is `PumpInspectorSystemRole@PlantAMaintenance`. Its contribution identity is supplying the pump-condition inspection judgment used before a Plant A maintenance decision. The description names `PlantA-PumpInspector-KindSignature-v4` and `Plant-A-Maintenance-Scheme`. Under that signature, a candidate counts only when it is already admitted as a `U.System` and two Plant A domain claims obtain: the reading predicate says that this System obtains readings for the named pump and declared condition characteristics in the applicable inspection situation; the judgment predicate says that this System returns the named pre-maintenance judgment from those readings. Each predicate declaration supplies participant meanings and applicability, and the current case supplies the satisfying facts. Use `A.6.F` only if source wording first hides those claims behind *function*; it establishes neither predicate. If either predicate or its case facts cannot be recovered, record the exact A.6.RCD `missing-governor` or missing-information result instead of classifying the candidate. A maintenance technician, inspection robot, or service team is only an example until those same conditions are checked.

The description says the kind concerns pump-condition inspection and does not itself denote repair. It may cite pump-inspection capability conditions or an inspection Method when a receiving Work claim needs them. Its boundary says that an inspection report is an episteme used through evaluation, evidence, source, or publication relations, not a system-role holder.

The description makes `PumpInspectorSystemRole` recognizable. It does not say that Robot-7 satisfies the kind, has an assignment, is capable of inspecting, has permission or readiness to inspect, enacted a Method, or performed Work. Those claims use C.3.2, A.2.1, A.2.2, A.2.8.PER, A.15, and the applicable evaluation or evidence relations.

#### F.4:7.2 - Reviewer System Role and Review Report

`ReviewerSystemRoleKindDescription` may describe `ReviewerSystemRole@PatternReview-2026`, the local kind identified by the contribution of supplying a reasoned pattern-review judgment against the declared scales. Under `PatternReview-2026-Reviewer-KindSignature-v2`, a candidate counts only when it is already admitted as a `U.System` and two review-domain claims obtain: the comparison predicate says that this System compares the named pattern claims with each selected scale in the applicable review situation; the result predicate says that it returns the named reasoned judgment with the assessed values or defects. Each declaration supplies participant meanings and applicability, and the current case supplies the satisfying facts. `A.6.F` is used only to unpack still-ambiguous function wording and establishes neither claim. If a predicate is missing, record the A.6.RCD `missing-governor`; if case facts are missing, record the corresponding unresolved result. This condition can be checked without asserting that any review appointment or dated review Work already exists.

Alice's classification under that kind, any review appointment she holds, any dated review Work she performs, and any report used as evidence remain four separate claims. This compact description names none of their occurrence identities.

Use:

- A.2 with C.3 for the local kind and direct classification;
- F.4 for the description episteme;
- A.2.1 when a particular review assignment must be identified;
- A.15.1 and F.6 when a particular dated review Work occurrence and the assignment under which it was performed must be identified; and
- A.10, B.3, G.6, or another direct relation for the report's evidence or assurance use.

The report is not a system-role holder and does not acquire an “evidence role.”

#### F.4:7.3 - Standard Used as a Specification or Source

The sentence “Standard S has the architecture-standard role in this Work” is unsafe if it classifies the standard episteme as a system-role holder. Rewrite the actual claim: the exact edition of Standard S is used as a specification, external rule, premise, or source for named claims. A standard may constrain or support a claim through that direct relation. No system-role kind or assignment is needed unless a separately admitted system really satisfies and is assigned to one.

#### F.4:7.4 - Access Role Is Not Automatically a System Role

RBAC *role* often names a permission grouping. If the current claim concerns permission or access standing, use the direct policy, deontic, access, or status relation. Treat a local access term as a system-role kind only when its own C.3 identity and criterion are current and a receiving Work claim actually needs that classification. Even then, permission and assignment remain separate.

