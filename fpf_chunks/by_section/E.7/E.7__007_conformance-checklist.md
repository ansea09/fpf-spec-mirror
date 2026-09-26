---
chunk_kind: "child"
pattern_id: "E.7"
pattern_title: "Archetypal Grounding: Explain Rules of FPF Architectural Patterns through Cases"
section_id: "E.7:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.7/E.7__007_conformance-checklist.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "E.7 — Archetypal Grounding: Explain Rules of FPF Architectural Patterns through Cases"
  - "E.7:6 — Conformance Checklist"
line_start: 82221
line_end: 82229
dependencies:
  - "E.5.4"
  - "E.6"
  - "E.8"
keywords:
---

### E.7:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑AG.1** | Every architectural pattern **SHALL** contain a section headed *“Archetypal Grounding”* under E.8's heading rules. | Keeps grounding findable across all Parts. |
| **CC‑AG.2** | The Archetypal Grounding section **MUST** illustrate the rule with both `U.System` and `U.Episteme` when it applies to both. A single-substrate rule follows CC‑AG.3. | Makes the claimed application and scope inspectable. |
| **CC‑AG.3** | If a rule intentionally applies to only one substrate, the subsection **SHALL** state the scope limitation and justify it against the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Epist` (epistemological and ontological), `Prag`, `Did`). | Prevents silent bias; links to Bias‑Audit guard‑rail. |
| **CC‑AG.4** | Patterns lacking a compliant Archetypal Grounding subsection **MAY NOT** progress to “Accepted” status. | Enforces discipline without referring to workflow mechanics. |

