---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:4"
section_title: "Solution — One‑Way, Acyclic Imports"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__005_solution-one-way-acyclic-imports.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:4 — Solution — One‑Way, Acyclic Imports"
line_start: 101847
line_end: 101867
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:4 - Solution — One‑Way, Acyclic Imports
Define a strict **partial order** over FPF ecosystem families. Imports between families point only **upward** in stability. Also protect the direction of meaning flow under **E.10 V-1**: **no Core semantics** may derive from Tooling or Pedagogy. The Conceptual Core excludes linters and machine checking.

**`imports` expresses dependency. Specialisation is a separate relation (normative).** When an artefact exposes an `imports : [...]` list (e.g., `SignatureManifest.imports` in A.6.0), treat each dependency claim in the list as an edge of its `imports` graph. The graph MUST be **acyclic** (a DAG) and MUST respect the declared direction.

`imports` MUST NOT be used to encode *specialisation* (e.g., `⊑` / `⊑⁺` between mechanisms). Specialisation relations and any specialisation-chain claims are declared separately under their defining rules. For mechanism declarations, apply A.6.1:4.8 to the comparison claim. Use C.29 when a separate mathematical-representation choice, transfer or reliance question remains.

Pedagogical Companion  ⟶  Tooling Reference  ⟶  Conceptual Core

1. **Allowed edges**
   Dependencies between families **MAY** point **only upward** (toward greater semantic
   stability). Cycles are forbidden.

2. **No downward import**
   Conceptual Core patterns **SHALL NOT** import Tooling Reference or Pedagogical Companion family members.
   Tooling Reference family members **SHALL NOT** import Pedagogical Companion family members.

3. **Future layers**
   Any new family is inserted below an existing one or becomes part of
   the Tooling or Pedagogy strata. The ordering extends accordingly.

