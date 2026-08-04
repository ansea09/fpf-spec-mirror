---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:8"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__010_consequences.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:8 — Consequences"
line_start: 6097
line_end: 6104
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.5"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:8 - Consequences

**Benefits.** A system applying a method can reuse role relations without hiding its admission predicate. Safety and governance checks can state separation conditions exactly. Joint work can distinguish role-set membership from holder allocation. Role qualification remains semantic and does not become system taxonomy. Relation assertions can stay readable until a receiving use needs explicit occurrence identity.

**Costs.** A consequence-bearing use must write the predicate that an informal hierarchy or bundle name previously concealed. Repeated relations may need temporal extent or another direct identity discriminator. Existing policy tables and organization charts may need a separate assertion layer and explicit links to the selected occurrences they describe.

**Limits.** This pattern ends at the selected role relation and its structure. A.2.1 establishes actual assignments, A.2.2 and A.2.5 establish capability and current role state, A.15 establishes performed work, evidence patterns establish support, and the receiving pattern governs the final admission outcome. Storage and visualization remain implementation and lens choices.

