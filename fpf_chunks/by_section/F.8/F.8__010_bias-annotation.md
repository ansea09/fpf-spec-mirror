---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:8.0"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__010_bias-annotation.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:8.0 — Bias-Annotation"
line_start: 92531
line_end: 92559
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

### F.8:8.0 - Bias-Annotation

F.8 blocks minting bias and record-first bias. A convenient expression, suffix, title, source term, review label, stable identifier, filled card, or memorable public phrase proves neither that FPF needs a new name nor that the named object or decision exists. Start from the exact governed value or relation, direct pattern, proposed use, effective naming ReferenceScheme, and local-sense basis. Choose the smallest adequate disposition. Treat a selected bounded-model-use Structure, decision result, NameCard, row, and publication package as separate objects only when their own direct conditions are current.

#### F.8:8.1 - Policy-Identifier Mint-or-Reuse Discipline

FPF treats policy identifiers such as `Phi(CL)`, `Phi_plane`, `Psi(CL^k)`, `Aut-Guard`, `EmitterPolicyRef`, insertion-policy identifiers, and acceptance-clause identifiers as versioned references whose meaning must be recoverable. They are not "just strings", role names, gate decisions, permissions, or policy specifications.

```text
PolicyIdentifierReference:
  PolicyIdentifier:
  PolicySpecificationRef:
  MintDecisionOccurrenceRef:
  MintDecisionResultEpistemeRef?:
  ScopeOrNamespaceRef:
```

`PolicyIdentifier` is the selected designator. `PolicySpecificationRef` resolves to the separate policy-definition episteme, pins an edition or equivalent digest when needed, and remains findable through the same publication family or an exact cited source relation; it does not identify or mint the identifier. `MintDecisionOccurrenceRef` resolves to the separate decision that introduced the identifier in the declared namespace. `MintDecisionResultEpistemeRef`, when current, resolves to a C.2.1 episteme or accepted record describing that occurrence; the record does not perform the decision.

For FPF normative policy identifiers, the durable result episteme is usually an accepted `E.9` decision record. For a local non-exported identifier, the direct gate, decision, or publication pattern may admit a smaller result episteme when local scope is explicit. In either case, the policy specification, identifier, decision occurrence, and record remain distinct.

Rules:

1. **No silent policy-identifier introduction.** A newly introduced identifier resolves both the separate `PolicySpecificationRef` and mint decision occurrence; when durable trace is needed, it also resolves the separate result episteme or record.
2. **Reuse is reference use.** Reusing an existing identifier resolves the same identifier, its policy specification, and its original mint decision; it does not restate policy semantics or silently create another decision.
3. **Gate checkability.** A gate, crossing, Bridge, assurance, or publication claim that depends on a policy identifier includes `PolicyIdentifierReference` or an equivalent resolvable structure admitted by its governing pattern.
4. **Policy authority stays with the governing pattern.** F.8 selects introduction or reuse of the identifier; it does not decide whether the policy permits Work, passes a gate, makes a relation obtain, or provides evidence.
5. **The identifier grants nothing by itself.** Name, namespace, suffix, source prestige, specification publication, or decision record grants no permission, status, equivalence, or authority beyond the exact direct policy claim.

