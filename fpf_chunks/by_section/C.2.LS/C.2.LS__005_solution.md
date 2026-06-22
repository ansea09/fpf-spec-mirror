---
chunk_kind: "child"
pattern_id: "C.2.LS"
pattern_title: "U.LanguageStateFacetProfile - Thin profile bundle for language-state facets"
section_id: "C.2.LS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.LS/C.2.LS__005_solution.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "C.2.LS — U.LanguageStateFacetProfile - Thin profile bundle for language-state facets"
  - "C.2.LS:4 — Solution"
line_start: 38505
line_end: 38558
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.18"
  - "A.19"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.3"
  - "C.2.4"
  - "C.2.4-C.2.7"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "E.18"
  - "F.9.1"
keywords:
  - "anchoring"
  - "articulation"
  - "closure"
  - "facet profile"
  - "representation factors"
  - "threshold package"
---

### C.2.LS:4 - Solution
`U.LanguageStateFacetProfile` is a typed profile bundle that names the facets by which position claims in the declared language-state chart over `U.CharacteristicSpace` are published and interpreted:

- `formalityRef` -> `U.Formality` from `C.2.3`
- `articulationExplicitnessRef` -> `U.ArticulationExplicitness` from `C.2.4`
- `languageStateClosureDegreeRef` -> `U.LanguageStateClosureDegree` from `C.2.5`
- `languageStateAnchoringModeRef` -> `U.LanguageStateAnchoringMode` from `C.2.6`
- `languageStateRepresentationFactorBundleRef` -> `U.LanguageStateRepresentationFactorBundle` from `C.2.7`
- `thresholdRefs?` -> context-local threshold declarations over the governed facets
- `routeNotes?` -> informative notes that help interpret routing or reopening decisions

`C.2.LS` is therefore a **profile-bundle governing pattern**, not a characteristic governing pattern and not a trajectory governing pattern. Characteristic semantics remain with `A.18/A.19`; admissible moves remain with `A.16`; explicit transition-structure publication remains with `E.18`.

#### C.2.LS:4.0a - Kind and profile-bundle boundary

`U.LanguageStateFacetProfile` is a dependent durable profile-bundle value under the declared `U.LanguageStateSpace` and `U.CharacteristicSpace` boundary, not a root U-kind. Its identity is the explicit bundle of language-state facet refs used for position reading and threshold publication. A local dashboard, table, route note, or maturity label is a publication or interpretation over the bundle, not the bundle itself.

#### C.2.LS:4.1 - Governing boundary
`C.2.LS` governs only the profile composition and the rule that the language-state facets must remain explicit and non-collapsed. It does **not**:

- redefine `F`;
- invent a second formality progression;
- govern the scale semantics of `AE`, `CD`, `LanguageStateAnchoringMode`, or `U.LanguageStateRepresentationFactorBundle`;
- govern reopen/backoff moves;
- govern endpoint classification or bridge kinds.

#### C.2.LS:4.2 - Threshold publication discipline
Any threshold used for routing, admissible move guards, or entry into `A.6.P` shall be published on explicit named facets within the profile. Contexts shall not speak of hidden sub-levels of `F` when what matters is really articulation, closure, anchoring, or the representation-factor bundle.

#### C.2.LS:4.2.a - Local profile-reading witness
For this pattern, a published facet profile is reviewable when:

- the facet refs are explicit or explicitly inherited from an already pinned upstream publication;
- any threshold-bearing use names the facet whose threshold is being invoked;
- route notes or local overlays remain informative and visibly docked to the explicit facet bundle;
- and the profile does not smuggle move rules, bridge rules, gate state, or downstream governing-pattern semantics into the bundle record.

A polished label, one strong facet, or one memorable route note does not by itself yield an admissible profile reading. The profile remains conformant only when the named facets stay explicit and decomposable.

#### C.2.LS:4.3 - Composite readings
A language-state judgement may be composite, but the composite shall be decomposable. For example, a cue may be:

- low `AE`,
- medium `CD`,
- `AM.TraceAnchored`,
- and representation-wise mixed rather than purely symbolic.

A conforming profile makes this decomposition visible rather than hiding it under one poetic label such as "early" or "raw".

#### C.2.LS:4.4 - Corridor map note
`C.2.LS` participates in the current `Language-State & Semantic Routing Corridor`, but only as the thin governing pattern of the facet-profile bundle. Readers who need one map of the full language-state governing-pattern set should read the corridor note in `C.2.2a`.

That map does not change the governing boundary here: `C.2.LS` still does not govern cue preservation, route-bearing publication, prompt entry, or downstream endpoint use.

