---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:4"
section_title: "Solution — One‑Way, Acyclic Imports"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__005_solution-one-way-acyclic-imports.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:4 — Solution — One‑Way, Acyclic Imports"
line_start: 102464
line_end: 102486
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:4 - Solution — One‑Way, Acyclic Imports
Read a dependency arrow from the member that needs content for a stated use to the member that supplies it. The **strict partial order** on distinct families constrains the permitted direction of cross-family imports. The actual imports connect particular members. A family may have several permitted suppliers and need only one for the work at hand.

**`imports` expresses dependency. Specialisation is a separate relation (normative).** When an artefact exposes an `imports : [...]` list (e.g., `SignatureManifest.imports` in A.6.0), treat each dependency claim in the list as an edge of its `imports` graph. The graph MUST be **acyclic** (a DAG) and MUST respect the declared direction.

`imports` MUST NOT be used to encode *specialisation* (e.g., `⊑` / `⊑⁺` between mechanisms). Specialisation relations and any specialisation-chain claims are declared separately under their defining rules. For mechanism declarations, apply A.6.1:4.8 to the comparison claim. Use C.29 when a separate mathematical-representation choice, transfer or reliance question remains.

**Permitted suppliers for Core, Tooling and Pedagogy**

| Family of the receiving member | That member may import directly from members of these families |
| --- | --- |
| Conceptual Core | Conceptual Core |
| Tooling Reference | Tooling Reference, Conceptual Core |
| Pedagogical Companion | Pedagogical Companion, Tooling Reference, Conceptual Core |

Each row lists permitted suppliers. Use the ones needed for the member’s stated work. A guide can take a definition directly from Core. An intermediary is needed when its contribution is required for that use.

The acyclicity rule applies within each family as well as across families. Before adding an import, follow the existing imports from the proposed supplier. If a path reaches the receiving member, the new import would close a cycle. Keep Core meanings independent of Tooling, Pedagogy and domain or local frameworks (E.10 V-1, E.4). Linters and other executable checks of Core conformance belong in Tooling. Core states the conditions they check. For Core, DPF and LPF editions, apply the edition rules in E.4.PFR:3.4. An LPF may depend directly on a DPF, and either may depend directly on Core. E.4.DPF also permits a DPF to rely on a contribution from another DPF when it fits the receiving use. The discipline to which a Method belongs, the order of chapters and the level of abstraction of a model each need their own grounds (E.4:4.2.2, B.5.MR).

**Extending the order.** Classify a proposed tool or teaching publication by the use it supplies. It can join an existing family under that family's rules. For a genuinely new family, use E.4.PFAD and E.9 to decide both who may supply it and who may import from it. Under the current extension rule, place it on the receiving side of at least one existing family. Follow the proposed directions through the existing order. Reject a loop even if nobody has yet exercised any of the permissions. Specify any change in what existing families may obtain from one another and seek the amendment needed before an existing prohibition can change. Families without a direct or transitive ordering relation can remain incomparable. A permitted direction need not yet have an actual import. A proposal outside the extension rule requires a change to that rule before admission.

**When a needed import would be forbidden**, keep the contingent claim with the family that can warrant it. If Core readers need a transdisciplinary rule, supply the rule and grounds they can use independently. A guide can receive credit for the discovery. Copying a guide's convention leaves Core dependent on that convention whenever the argument still requires it. If two members would have to import one another, look for a common definition they can both use from a permitted supplier. Where two definitions must be given together, consider one defining account and check its imports. Printing two mutually dependent members in one file leaves their cycle intact.

