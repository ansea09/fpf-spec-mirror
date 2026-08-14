---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__002_use-this-when.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:0 — Use This When"
line_start: 91732
line_end: 91767
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

### F.4:0 - Use This When

**Plain name.** Description of a system-role kind.

Use F.4 when a project needs a short, reusable description that makes one exact local system-role kind recognizable, teachable, and checkable. The described kind is a C.3 kind whose candidates must first be independently admitted as `U.System`. A candidate may be, for example, a person, team, organization, or non-human technical object; `SystemRole` does not mean “technical system only.”

Typical moments:

- a project has a durable kind name such as `ReviewerSystemRole`, `OperatorSystemRole`, `InspectorSystemRole`, `TransformerSystemRole`, or `ShipyardCoordinatorSystemRole`, but readers cannot recover its bounded context, contribution identity, `KindSignature`, or work-facing boundary;
- a MethodDescription names a required system-role kind, but readers cannot tell which exact local kind must classify a candidate before an assignment can be checked;
- a kind name is starting to carry assignment, capability, Method, Work, permission, responsibility, evidence, publication, or status claims that belong elsewhere; or
- source prose says that a report, standard, dataset, theorem, dashboard, publication, or requirement has a “role”, and the writer must recover whether that wording denotes a system-role kind at all.

**Primary EntityOfConcern.** A `SystemRoleKindDescription` is one `U.Episteme` constituted under C.2.1. Its exact EntityOfConcern is one local system-role kind. Its ClaimGraph names the kind's bounded context, continuing contribution identity, current `KindSignature` edition, effective `U.ReferenceScheme`, and only the neighboring relations needed by the described use. The description is not the kind, a classification judgment, assignment occurrence, holder system, capability, MethodDescription, performed Work, status-use relation, or publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, Method author, or pattern author who must help people recognize the kind while keeping kind, candidate classification, assignment, capability, Method, Work, evidence use, status use, and publication use distinct.

**First useful move.** Name the exact local system-role kind, its bounded context and contribution identity, the current `KindSignature` edition, and the shortest recognition explanation needed by the next classification, assignment, Method, Work, naming, or Bridge claim.

**What goes wrong if missed.** A description card becomes a hidden procedure, staffing record, access policy, permission badge, responsibility claim, evidence relation, status assertion, or Work log. Then one word recreates a universal role ontology and a second role-like ontology for epistemes, publications, statuses, and relation positions.

**What this buys.** A project gets a compact, readable description while operational claims remain at their direct loci. The kind stays recognizable; classification and assignment stay checkable; capability, Method, Work, evidence, status, responsibility, and publication claims stay inspectable instead of being smuggled into the name.

**Not this pattern when.**

- If the current question is whether a local system-role kind exists, how it is identified, or whether one candidate satisfies it, use A.2 with C.3 and C.3.2.
- If the current question is whether one admitted system and one exact local kind participate in an obtaining assignment, use A.2.1.
- If one assignment may satisfy one state condition during a window, use A.2.5.
- If the current question concerns admission substitution, incompatibility, qualification, a bundle, or another relation among system-role kinds, use A.2.7.
- If the current question is capability, use A.2.2.
- If it is about a Method, MethodDescription, WorkPlan, or performed Work, use A.3 or A.15 and the direct neighboring pattern.
- If an episteme is used as evidence, source, standard, requirement, publication, assurance input, status bearer, gate input, or decision input, use the direct relation. Do not classify the episteme as a system-role holder by wording.
- If only a durable name is needed, use F.18.
- If two local system-role-kind meanings must be compared across contexts or schemes, use C.3.3 and F.9.
- If bare *role* may mean a relation participant, declaration slot, representation position, ordinary wording, or another object, use E.10.ROLE and A.6.RSIR where relation recovery is needed.

