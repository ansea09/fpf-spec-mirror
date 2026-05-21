---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__012_conformance-checklist.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:7 — Conformance Checklist"
line_start: 49988
line_end: 50021
dependencies:
  - "E.10"
  - "E.19"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.9"
  - "F.18"
keywords:
  - "). The key words MUST"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT appear inside Definition:/Invariant:/Well-formedness constraint: blocks. When enforceable"
  - "Prevents ambiguity between obligation language and model validity"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SHALL"
  - "SHALL NOT"
  - "SHOULD"
  - "SHOULD NOT"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:7 - Conformance Checklist

**CC style (canonical).**
Conformance Checklist items are authoring checks: they test whether the pattern guidance has been applied and written correctly in a pattern or support text that claims conformance. They do not replace `Solution`, do not make the pattern a control form, and do not state deontic obligations about the modeled world. A CC clause of the form “X SHALL ...” is to be read as “In a conforming pattern or support text, X SHALL ...”.

**Preferred wording for new or edited CC items:** start with an explicit conformance subject (e.g., “Authors ...”, “Reviewers ...”, “A conforming implementation ...”, “A validator ...”). If a CC item is enforcing an admissibility predicate, it **SHOULD** cite the predicate’s identifier (from a `Definition:` / `Invariant:` / `Well-formedness constraint:` block) rather than restating the predicate as “X MUST ...”. For boundary/interface/protocol/declaration patterns, prefer A.6.B-governed claim IDs (L/A/D/E) or cite an existing Claim Register (A.6.B:7) instead of restating mixed prose.

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC-SG.0 (Heading discipline).** | Pattern and subsection headings **SHALL** follow **H-1 ... H-9** (FullId prefix, reserved punctuation, heading levels, ellipsis discipline). The Footer marker **SHALL** follow **H-9**. | Makes chunks self-contained; reduces ambiguity between author elision and retrieval truncation. |
| **CC-SG.1** | Every new pattern **SHALL** follow the section order defined in the Canonical Template (Title block -> ... -> Footer marker). | Guarantees structural comparability. |
| **CC-SG.1a (Initial live draft shape).** | The first non-empty authored version of a live pattern **SHALL** already use the canonical section frame (Title block -> Footer marker). Authors **MUST NOT** start from one pre-template opening memo and promise to backfill canonical sections later. | Prevents large late-stage structural rewrites and keeps drafting aligned with `E.8` from the first substantive pass. |
| **CC-SG.2 (Grounding required).** | Every pattern **MUST** include an *Archetypal Grounding* section. If **System** or **Episteme** grounding is inapplicable, authors **MUST** state `Not applicable` and give a one-paragraph justification. | Keeps patterns teachable and reduces “definition-only” ambiguity. |
| **CC-SG.3** | The *Bias-Annotation* section **SHALL** cite the five Principle-Taxonomy lenses and declare either “Universal” or an explicit scope limitation. | Keeps cross-disciplinary neutrality explicit (ties to Guard-Rail 4). |
| **CC-SG.4** | Deontic normative sentences **MUST** use only RFC-style keywords (see **H-8**); RFC keywords **MUST NOT** appear inside `Definition:`/`Invariant:`/`Well-formedness constraint:` blocks. When enforceable, admissibility/validity predicates **SHOULD** be referenced by id from the Conformance Checklist (rather than duplicated as “X MUST ...”). Informal deontic verbs are prohibited in normative clauses. | Prevents ambiguity between obligation language and model validity; improves auditability. |
| **CC-SG.5** | Pattern prose **SHOULD** demonstrate adherence to Style Principles **S-0 ... S-19**; reviewers are empowered to request revision when clarity or didactic quality suffers. | Embeds common narrative voice without rigid policing. |
| **CC-SG.6 (SoTA-Echo required).** | Every pattern **SHALL** include a **SoTA-Echoing** section and clearly state divergence of its Solution from SoTA with explanation of why. Architectural patterns **SHALL** satisfy the full obligations below. Definitional patterns **SHALL** carry reduced SoTA when a full comparison is not meaningful: name which current practice is adopted, adapted, or rejected for terminology work, ambiguity or sense recovery, separation between constraint and ontology, controlled-vocabulary caution, or a comparable definitional problem. Internal coherence alone is not enough. | Ensures explicit lineage, guards against vocabulary drift, and prevents definitional patterns from using internal coherence as zero SoTA. |
| **CC-SG.7 (Post-2015, multi-Tradition).** | For Architectural patterns, SoTA-Echoing **SHALL** cite >= 3 post-2015 sources across >= 2 Traditions; each item **MUST** carry adoption status (adopt/adapt/reject) with reason. | Guards against monoculture; makes intent explicit. |
| **CC-SG.8 (Bridge & CL on reuse).** | Any cross-Context or plane reuse mentioned in SoTA-Echoing **MUST** cite **Bridge id + CL** and (if planes differ) **Φ(CL)**/**Φ_plane** policy-ids; penalties **-> R_eff** only. | Safe, auditable reuse. |
| **CC-SG.9 (Lexical hygiene).** | The term **mapping** **SHALL NOT** appear in SoTA-Echoing except in the precise E.10 sense; use **alignment/Bridge/relation** instead. | Avoids overloading reserved vocabulary. |
| **CC-SG.10 (No keyword soup).** | SoTA-Echoing items **MUST** be written as sentences (not bare noun phrases); bullet lists are acceptable only with complete clauses. | Improves didactic quality and comparability. |
| **CC-SG.11 (Anti-patterns).** | Every pattern **SHALL** include a **Common Anti-Patterns and How to Avoid Them** section. It **MAY** be `Not applicable` only with a one-paragraph justification. | Makes misuse paths explicit and reduces review churn. |
| **CC-SG.12 (Boundary claim-set discipline).** | If a pattern’s subject is a boundary, interface, API, protocol, connector, SLA, or other published boundary description, it **MUST** either (a) provide an **A.6.B**-governed atomic claim set (`L-*`/`A-*`/`D-*`/`E-*`, with stable IDs), or (b) explicitly cite an existing **A.6.B Claim Register** / governed claim set that it reuses. | Pulls A.6.B into the authoring contour, prevents boundary-kind soup, and makes review more explicit and repeatable. |
| **CC-SG.13 (Didactic sufficiency).** | New patterns and substantial revisions **MUST** remain understandable without project-planning notes. When a pattern introduces a new named family, profile, or specialization, or adds a non-trivial governing-pattern-derived note, its Solution and Grounding **SHALL** carry enough supporting content: explicit governing-pattern relation, ordinary-vs-load-bearing guidance, at least one concrete source and resulting-publication slice where applicable, and visible neighboring-pattern or exact project-side FPF kind and reference cues. | Prevents skeleton-only patterns and project-context leakage. |
| **CC-SG.14 (Controlled prose, not free shorthand).** | Load-bearing prose **SHALL NOT** rely on bare relation words or planning shorthand whose governing-pattern relation is left implicit (e.g., bare “species”, “branch”, “flow”, or API-like “input/output” language). When a governing-pattern relation matters, authors **MUST** name it explicitly (`specialization under ...`, `profile governed by ...`, `overlay over ...`, etc.). | Keeps pattern prose precise and self-identifying. |
| **CC-SG.15 (Package-form and governing-pattern relation role-word discipline).** | When a pattern names a package-form or the governing-pattern relation of a family (`primary carrier`, `specialization`, `profile`, `overlay`, `family`, `bundle`, `cluster`, `suite`, `pack`, `kit`, `record`, `umbrella`), the chosen role word **MUST** match the intended ontology and **MUST NOT** be swapped for stylistic variety or left to implication. | Prevents semantic blur in pattern prose and keeps governing-pattern relations auditable. |
| **CC-SG.16 (Reader-role discipline).** | Authors **MUST** keep live pattern sections user-facing. FPF-development or package-architecture reasoning about isolation, overlay or carrier choice, freeze, merge posture, or planned evolution **MUST NOT** occupy `Problem`, `Solution`, `Consequences`, `Rationale`, or worked slices; if such placement reasoning is still needed, it **MUST** live in a separate companion note or a clearly marked informative placement note. | Keeps pattern prose aligned with its intended reader and prevents package-governance leakage into live use guidance. |
| **CC-SG.16a (Referent-index discipline in live prose).** | Live pattern sections **MUST** keep run-time/domain referents, standard-plane referents, and design-time/control-plane referents distinct. In ordinary live prose, sentence truth **MUST** depend on the governed run-time/domain object or on the pattern's declared normative claim set, not on the current draft state, author action, reviewer action, or control-plane posture. If a sentence is true only because of the current writing/review pass or text arrangement, it is design-time residue and belongs in carriers or companion notes, not in the live pattern body. | Prevents Conway/process leakage and reduces late cleanup before review or landing. |
| **CC-SG.17 (Recognition text and assurance text).** | Admission or substantial revision runs **MUST** check that a canonical pattern exposes a recognition text early enough for the intended working reader and an assurance text that carries declaration, guidance/check, modeling, and review load without silently shifting the recognition-text claim. The recognition text **MUST** expose a recognisable working situation, what goes wrong if the pattern is missed, what the pattern buys, and a clear ordinary `not this pattern when` boundary. Any load-bearing typed declaration or modeling lens **MUST** be exposed by a short user-facing statement of the governed object, early load-bearing technical terms **MUST** receive nearby pairwise plain glosses, and any `SoTA-Echoing` used as live explanatory support **MUST** state a short practitioner or manager implication plus visible linkage to the worked cases or boundary slices it disciplines. If the pattern claims universal or transdisciplinary reach, the recognition text **MUST** demonstrate that claim through at least three heterogeneous reader or domain situations, preferably using an `F.16`-style example matrix or an equally explicit alternative. | Prevents text-clean but reader-opaque patterns and keeps broad claims visible where cold readers actually enter the text. |
| **CC-SG.17a (Problem-frame recognition signature and E.11 boundary).** | Authors **SHOULD** express a pattern's concrete working situation through the pattern's `Problem frame`, not through a separate navigation block. The `Problem frame` should make recoverable the governed object or stabilized concern, what goes wrong if the pattern is missed or misread, the ordinary not-this-pattern boundary, the first admissible action-guiding move, and the result that move buys. Only when an `E.11` pattern-entry discoverability problem is live should the same recognition text add candidate-pattern, tempting-wrong-pattern, entry-load reclassification, or first admissible entry-stop cues. Cross-pattern comparison belongs in `J.4`; expanded case reading belongs in `I.2`; lexical-query support belongs under the lexical/naming patterns and support companions that already govern it. Pattern-local `Start here when`, `First output`, neighboring-pattern lists, and `Common wrong escalations and boundary transfers` blocks **SHOULD NOT** replace the action-guiding `Problem frame` and `Solution`. | Keeps working-use recognition inside the canonical pattern frame while preventing navigation/workflow language from becoming local pattern structure. |
| **CC-SG.17b (Semantic repair preserves action guidance).** | When authors edit pattern prose under `E.10.SEMIO`, the repaired recognition text **MUST** preserve or restore the first admissible action-guiding move as a remaining admissible reader move, or explicitly name the neighboring FPF pattern that now carries the live claim. When both Tech and Plain registers are live, any Plain or didactic wording **MUST** map back to the recovered Tech reading under `E.10:6.2` when it carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load. More engaging recognition wording remains admissible as ordinary Plain prose only when it does not carry such load, or as a recognition aid whose load is recoverable through the recovered Tech reading or named handoff. Type-correct but inert wording is not mature pattern prose. | Prevents semio cleanup from leaving pattern guidance inert while also preventing expressive prose from reintroducing overread. |

| **CC-SG.18 (Precision before relaxation).** | In load-bearing prose, authors **MUST NOT** leave a generic head noun or load-bearing qualifier uninterpreted when that phrase carries semantic, boundary, or authority load. A narrowing qualifier by itself does **not** restore the head kind. Authors **MUST** restore head kind first, then qualifier load, then any comparison/escalation basis before downstream claim or effect. If a later Plain, didactic, or coarsened rendering is kept, the more precise upstream reading **MUST** remain recoverable. | Prevents ambiguity from being hidden inside ordinary-looking phrases and keeps softened prose subordinate to an explicit authoritative reading. |

