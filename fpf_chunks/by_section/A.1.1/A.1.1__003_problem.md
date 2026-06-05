---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__003_problem.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:2 — Problem"
line_start: 1335
line_end: 1343
dependencies:
  - "A.1"
  - "A.2.1"
  - "D.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "U.Boundary"
  - "U.BoundedContext"
  - "U.Holon"
keywords:
  - "DDD"
  - "context"
  - "domain"
  - "glossary"
  - "invariants"
  - "local meaning"
  - "semantic boundary"
---

### A.1.1:2 - Problem

Absent an explicit, first-class semantic frame:

1. **Ambiguity becomes structural debt.** Integrations silently overwrite meanings (“process” becomes “procedure”; “role” becomes “permission”), and the resulting model cannot be audited.
2. **Pluralism looks like contradiction.** Two valid perspectives appear mutually exclusive because the frame of reference is implicit (e.g., Pluto as `PlanetRole` vs `DwarfPlanetRole`).
3. **Roles lose semantic footing.** A `U.Role` without a declared frame degenerates into a global label, violating the kernel’s insistence that roles are contextual masks (A.2, A.2.1).
4. **Local rules leak globally.** Team- or theory-specific invariants are mistaken for universal laws, producing incoherent cross-domain reasoning.

