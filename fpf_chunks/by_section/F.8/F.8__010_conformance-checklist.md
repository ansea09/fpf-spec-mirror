---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:8"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__010_conformance-checklist.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:8 — Conformance Checklist"
line_start: 74368
line_end: 74406
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

### F.8:8 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-F8-01` | Candidate expression, bounded context, proposed use, and recovered kind or relation are named. |
| `CC-F8-02` | Mixed role, status, evidence, source, requirement, method, work, measurement, or structure uses are split. |
| `CC-F8-03` | A local existing sense is reused before proposing a row or `U.Type`. |
| `CC-F8-04` | Role expressions become durable role names only after `U.Role` and RoleDescription ontology are recovered. |
| `CC-F8-05` | Assignment and performed-work claims use `A.2.1`, `F.6`, and `A.15.1`, not naming. |
| `CC-F8-06` | Status, evidence, access, source, requirement, publication, assurance, gate, decision, and relation-position names go to direct governing patterns. |
| `CC-F8-07` | Concept-Set row reuse stays within the row's admitted use. |
| `CC-F8-08` | Aliases preserve meaning and carry lineage when durable. |
| `CC-F8-09` | New `U.Type` candidates cite cross-family recurrence, irreducibility, and accepted decision record. |
| `CC-F8-10` | Policy ids carry `PolicyIdRef` discipline when introduced or reused. |
| `CC-F8-11` | The decision states what overread is not admitted and what condition reopens the decision. |

#### F.8:8.1 - Policy-Id Mint-or-Reuse Discipline

FPF treats policy ids such as `Phi(CL)`, `Phi_plane`, `Psi(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, insertion-policy ids, and acceptance-clause ids as versioned identifiers whose meaning must be recoverable. They are not "just strings", role names, or gate decisions.

```text
PolicyIdRef:
  PolicyId:
  PolicySpecRef:
  MintDecisionRef?:
  ScopeOrNamespaceRef:
```

`PolicySpecRef` is a resolvable reference to the policy definition. It identifies the policy id, pins an edition or equivalent digest when needed, and can be found from the same publication family or cited source relation.

`MintDecisionRef` is a resolvable reference to the decision that introduced the policy id in the declared namespace. For FPF normative policy ids this is usually an accepted `E.9` decision record. For local non-exported policy ids, the governing gate, decision, or publication pattern may admit a smaller decision record when the local scope is explicit.

Rules:

1. **No silent policy-id introduction.** A newly introduced policy id carries both `PolicySpecRef` and `MintDecisionRef`.
2. **Reuse is reference use.** Reusing an existing policy id cites `PolicySpecRef`; it does not restate policy semantics as if a new policy had been introduced.
3. **Gate checkability.** A gate, crossing, bridge, assurance, or publication claim that depends on policy ids includes `PolicyIdRef` or an equivalent resolvable structure admitted by its governing pattern.
4. **Policy authority stays with the governing pattern.** F.8 decides introduction or reuse of the identifier; it does not decide whether the policy permits work, passes a gate, or gives evidence.

