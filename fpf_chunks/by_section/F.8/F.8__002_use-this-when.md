---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__002_use-this-when.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:0 — Use This When"
line_start: 84275
line_end: 84307
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

### F.8:0 - Use This When

**Plain name.** Name admission decision.

Use this pattern when a project has a candidate expression and must decide whether it should stay local, reuse an existing name, become an alias, reuse a Concept-Set row, name a role-description episteme, introduce a new Concept-Set row, introduce a policy id, or become a rare U-kind candidate.

Typical moments:

- a role-like expression such as `ReviewerRole`, `AccessRole`, `EvidenceRole`, `RequirementRole`, `ProviderRole`, or "actor" appears and the project must decide whether it names a work-facing `U.Role`, a status-use relation, an evidence-use relation, an access or policy term, a relation position, or only a local phrase;
- a source tradition uses a convenient name, but the name would import one context's ontology if promoted as an FPF name;
- a Concept-Set row seems reusable, but its scope may be only naming, not substitution, role assignment, measurement, or structural inference;
- a project wants a new U-kind, policy id, role-description label, or public term because no existing name feels comfortable;
- an `E.10` repair discovers that a smoother word would still hide the current kind or relation.

**Primary EntityOfConcern.** The EntityOfConcern is one mint-or-reuse decision for one candidate expression or proposed durable name. The pattern governs the decision relation. It does not define the named U-kind, does not describe the `U.Role`, does not assign a holder, does not assert status, does not provide evidence, and does not make a publication authoritative.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, pattern author, or terminology steward deciding whether a candidate expression deserves durable FPF treatment.

**First useful move.** Recover what the candidate expression is trying to name in the current bounded context. Then choose the smallest admissible decision: local phrase, alias, local name reuse, Concept-Set row reuse, RoleDescription label, direct-pattern name, policy id, new row, or rare U-kind candidate.

**What goes wrong if missed.** A convenient label becomes a new ontology. A source word becomes global. A status, evidence, access, requirement, source, publication, or relation-position use gets named as a role. A Concept-Set row is used beyond the scope admitted by its bridge evidence. FPF then accumulates duplicate kinds where it needed a smaller decision.

**What this buys.** Teams can reuse names without growing FPF by accident. Durable names become harder to mint, but easier to trust. Role expressions become work-facing role names only when the role ontology is actually current; other expressions go to their direct patterns before any durable naming.

**Not this pattern when.**

- If the issue is ordinary phrase repair with no durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the issue is choosing a good label after the mint-or-reuse decision is already made, use `F.5` for the local name family and `F.18` for the fuller public naming protocol.
- If the issue is describing one work-facing role, use `F.4`.
- If the issue is assigning a holder to a role or attributing performed work, use `A.2.1`, `F.6`, and `A.15.1`.
- If the issue is cross-context sameness, use `F.9` and `F.7`.
- If the issue is status, evidence, source, standard, requirement, publication, assurance, gate, or decision use, use the direct pattern before naming.

