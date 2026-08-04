---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__002_use-this-when.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:0 — Use This When"
line_start: 91645
line_end: 91677
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

### F.8:0 - Use This When

**Plain name.** Name admission decision.

Use this pattern when a project has one candidate expression, has independently recovered the exact governed value or relation that the expression might designate, knows that value's direct governing pattern, and must choose the smallest naming disposition for one proposed use. The expression may stay local, reuse an existing designation, become an alias, reuse a direct-pattern name or an admitted Unified Term Sheet row, name a RoleDescription episteme, open a durable naming settlement, introduce a policy identifier, propose a new public row, or remain only a rare U-kind candidate.

Typical moments:

- a role-like expression such as `ReviewerRole`, `AccessRole`, `EvidenceRole`, `RequirementRole`, `ProviderRole`, or "actor" appears and the project must decide whether it designates a work-facing `U.Role`, a status-use relation, an evidence-use relation, an access or policy value, a relation position, or only a local phrase;
- a source tradition supplies a convenient name, but its local sense would import that tradition's ontology if promoted as an FPF designation;
- an F.17 row seems reusable, but its admitted use may be only naming rather than substitution, role assignment, measurement, or structural inference;
- a project wants a new U-kind, policy identifier, RoleDescription label, NameCard, or public term row because no existing expression feels comfortable; or
- an `E.10` repair discovers that a smoother word would still hide the current kind or relation.

**Primary working object.** The working object is one mint-or-reuse decision occurrence concerning one candidate expression, one independently governed value or relation, and one proposed naming use. If another claim needs to cite that occurrence, identify it through the direct decision or work owner. A separately constituted C.2.1 decision-result episteme may describe the occurrence, and a displayed record may designate that episteme; neither the episteme nor its record performs the decision. F.8 introduces no generic decision kind.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, pattern author, or terminology steward deciding whether a candidate expression deserves durable FPF treatment.

**First useful move.** Write four things before judging the wording: the candidate expression, the exact governed value or relation already recovered under its direct pattern, that direct pattern, and one proposed use. Then apply F.14 and try, in order, a local phrase, an existing designation, an alias, a current direct-pattern name, and an admitted F.17 row. Create no `SchemeSenseCell`, NameCard, row, policy identifier, or U-kind candidate until every lighter sufficient disposition has failed.

**What goes wrong if missed.** A convenient label becomes new ontology. A source word becomes global. A status, evidence, access, requirement, source, publication, or relation-position use gets named as a role. A public row is used beyond its admitted scope. A review label is treated as a context object, performed Work, role assignment, evidence use, or authority. FPF then accumulates duplicate kinds and naming records where it needed a smaller decision.

**What this buys.** Teams can reuse names without growing FPF by accident. Durable names become harder to mint but easier to trust. Role expressions become work-facing role names only when the role ontology is independently current; other expressions return to their direct patterns before naming. The effective naming ReferenceScheme and exact local-sense basis stay visible without inventing a universal context object.

**Not this pattern when.**

- If the issue is ordinary phrase repair with no durable name, use `E.10`, `E.10.ARCH`, `A.6.P`, or the direct governing pattern.
- If the issue is choosing labels after the mint-or-reuse disposition is already settled, use `F.5` for the local name family and `F.18` for the fuller durable naming settlement.
- If the issue is describing one work-facing role, use `F.4`.
- If the issue is assigning a holder to a role or attributing performed work, use `A.2.1`, `F.6`, and `A.15.1`.
- If the issue is an actual relation between two different local-sense projections, use `F.9`; use `F.17` only when a public, Core-facing, durable, or cross-local row is current.
- If the issue is status, evidence, source, standard, requirement, publication, assurance, gate, decision, policy use, method, work, or another subject claim, use its direct pattern before naming.

