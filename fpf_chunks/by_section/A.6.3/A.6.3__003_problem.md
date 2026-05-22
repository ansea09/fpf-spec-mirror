---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — describedEntity‑preserving morphism"
section_id: "A.6.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__003_problem.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.6.3 — U.EpistemicViewing — describedEntity‑preserving morphism"
  - "A.6.3:2 — Problem"
line_start: 9796
line_end: 9821
dependencies:
  - "A.6.0"
  - "A.6.2"
  - "A.6.5"
  - "A.7"
  - "B.5.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.TGA"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotGraph"
  - "U.MultiViewDescribing"
  - "U.RelationSlotDiscipline"
  - "U.Signature"
keywords:
  - "ClaimGraph"
  - "CorrespondenceModel"
  - "Direct vs Correspondence Viewing"
  - "EpistemicViewing"
  - "RepresentationScheme"
  - "Viewpoint"
  - "describedEntity preservation"
  - "displayed fibration"
  - "episteme"
  - "optics"
  - "view"
---

### A.6.3:2 - Problem

Without a dedicated pattern for EpistemicViewing:
1. **Views vs retargetings blur.**
   Operations that *intend* to change only representation (viewing) are easily conflated with operations that change the **described entity** (retargeting). A Fourier‑style transform or a StructuralReinterpretation in E.TGA can quietly drift from “view of S” into “view of a different S′”, without declaring a `KindBridge`.

2. **“View” vs “viewpoint” vs rendered publication collapse.**
   In standards and tools, “view” is often used interchangeably to mean:
   * the **viewpoint** (specification of concerns and conformance rules),
   * the **episteme** produced under that viewpoint, and
   * the **rendered publication or carrier** (document, GUI, export, or other bearer).
     Without a clear episteme-lane notion of viewing, MVPK and E.17.0 cannot cleanly separate these lanes.

2. **No describedEntity guarantees.**
   A projection that looks like a harmless slice of a system description may in fact:
   * change `describedEntityRef` (switching to a subsystem or a function),
   * change `groundingHolonRef` (different plant or runtime),
   * or smuggle in new intensional claims.
     Without explicit invariants over C.2.1 components, “view” becomes an informal metaphor, not a reliable morphism class.

4. **Multi‑view reasoning has no core discipline.**
   Multi‑view patterns (ISO 42010 viewpoint libraries, SysML v2 view queries, TEVB, MVPK faces) need:
   * **vertical** projections over the same described entity (`α : Ep → Ref` fixed),
   * and **correspondence‑based** projections that rely on explicit cross‑episteme links.
     If each family re‑invents its own notion of “view”, consistency and tool support degrade.

