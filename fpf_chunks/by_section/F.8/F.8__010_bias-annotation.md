---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:8.0"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__010_bias-annotation.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:8.0 — Bias-Annotation"
line_start: 80975
line_end: 81001
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

### F.8:8.0 - Bias-Annotation

F.8 blocks minting-bias: the existence of a convenient candidate expression, suffix, title, source term, or memorable public phrase does not prove that FPF needs a new name, row, policy id, or U-kind. The decision starts from the recovered governed object, admissible use, bounded context, and direct pattern. Naming is allowed only after the smallest adequate decision target is found.

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

