---
chunk_kind: "child"
pattern_id: "E.14"
pattern_title: "Human‑Centric Working‑Model"
section_id: "E.14:8"
section_title: "Conformance Checklist (normative; author‑facing duties for thought and prose)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.14/E.14__011_conformance-checklist-normative-author-facing-duties-for-thought-and-prose.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.14 — Human‑Centric Working‑Model"
  - "E.14:8 — Conformance Checklist (normative; author‑facing duties for thought and prose)"
line_start: 70529
line_end: 70587
dependencies:
  - "B.3.5"
  - "C.13"
  - "C.2.3"
  - "E.10"
  - "E.7"
  - "E.8"
keywords:
  - "assurance layers"
  - "grounding"
  - "human-centric"
  - "publication surface"
  - "working model"
---

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical publication face for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC-E14-2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working-Model to the appropriate assurance shoulder (**Mapping, Logical, Constructive, or Empirical**) and **SHALL NOT** impose vocabulary back onto the Working-Model. | Maintain relation-family separation and cognitive economy. |
| **CC‑E14‑3 (Stance declaration).**         | For any claim where assurance matters, the author **SHALL** declare `validationMode` (*postulate / inferential / axiomatic*).                                                    | Make assurance intent explicit and readable.                  |
| **CC-E14-4 (No order/time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part-whole; keep them adjacent in their own relation families.                                           | Prevent layer leakage and category errors.                    |
| **CC‑E14‑5 (Collection ≠ Composition).**   | Authors **SHALL** keep **membership** claims distinct from **component** claims; no implicit upgrade from collection to assembly.                                                | Guard extensional identity and reader expectations.           |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back-defining Working-Model terms by their assurance publications or records; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support staged formality without overloading early drafts.  |
|**CC-E14-10 (Structural grounding handshake).** | For **structural** edges on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.sum|set|slice` (see **Compose-CAL** and **CT2R-LOG**). Exactly **one** Γₘ trace is permitted per edge (CI rule alignment). | Aligns E.14 with CT2R-LOG and Compose-CAL; ensures extensional identity. |
| **CC‑E14‑11 (Empirical bindings).**        | When `validationMode=postulate` (or when adding real-world confirmation), authors **SHALL** bind evidence through an evidence-use relation in a declared `U.BoundedContext`, with an explicit target claim, scope, **timespan**, and provenance anchors. | Aligns with Evidence Graph Referring and empirical ageing policies. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model publications **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable publications). Assurance publications or records **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids obsolete “tiers/modes”. |
| **CC‑E14‑13 (Light records, not thin prose).** | Authors **SHALL NOT** use the Working‑Model-first stance as a reason to strip problem framing, rationale, or worked slices out of the pattern text. Ordinary use may stay light, but readers **MUST** still be able to understand the pattern without nearby project notes. | Keeps human-facing economy from collapsing into under-explained prose. |
| **CC‑E14‑14 (Recognition text before assurance text).** | When a pattern claims a Working‑Model or other human-facing benefit, authors **SHALL** keep recognition-first working text distinct from the heavier assurance text. The assurance text **MAY** refine and justify the working text, but it **SHALL NOT** silently change the recognition-text claim. If the pattern claims broad or transdisciplinary reach, the working text **SHOULD** show heterogeneous situations early, preferably through an `F.16`-style example matrix or an equally explicit alternative. | Keeps Working‑Model-first drafting from collapsing into either thin prose or late-only universality. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Assembly from parts → “Component Of”**
   A pump skid is agreed to be nothing over and above its pump, frame, reservoir, and valve set considered together. Because the whole is conceptually *constructed* from those parts, the team may safely speak of each part as *Component Of* the skid. The justification is the construction itself: if any listed part were removed, the very same skid would no longer exist as that whole. This keeps identity extensional and makes the engineer-facing label (“Component Of”) truthful rather than conventional.

2. **Parallel elements gathered → “Member Of”**
   A test rig has four identical cartridges used in parallel. The rig treats them as a conceptual *gathering*; membership is fixed by inclusion in that gathering, not by sequence or timing. Speaking of each cartridge as *Member Of* the rig’s cartridge bank is then licensed by the same gathering act. Engineers can keep saying “member,” while architects know the warrant is the underlying construction of the bank as a collection, not an accidental tagging.

3. **Focused facet carved → “Aspect Of”**
   When the team talks about the *thermal envelope* of a reactor, they are not multiplying entities; they are taking the already‑agreed reactor and conceptually *carving out* its thermal facet for focused reasoning. Calling that carve‑out an *Aspect Of* the reactor is justified because the aspect owes its identity to the parent and the chosen facet, and nothing else. This licenses disciplined talk about “boundary,” “interface,” or “envelope” without mistaking them for independent systems.

> **Notes across the examples**
> • Everyday labels (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; their truth is grounded by prior constructional choices.
> • Structural links draw on **Constructive** grounding; **epistemic links**—like “Representation Of” or “Usage Of”—may instead rely on **Empirical Validation** (evidence-use relations) or **Logical** grounding appropriate to the claim.

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **Single dial for containment.** Teams can ask one plain question, “what is inside what?”, and trust that all structural talk reduces to shared constructional choices rather than ad-hoc relation lists. Ontologists keep rigorous warrants without overloading day-to-day readers.
* **Extensional identity by default.** Wholes are the wholes they are because of the parts gathered; collections are the collections they are because of their members; aspects inherit identity from their parent and facet. This prevents silent drift when labels change.
* **Layer harmony.** Engineer-facing labels live at the same level as other relation names, while their warrants live one step below, keeping human language clean and the generative basis auditable.

**What to watch**

* **Discipline for structural relation kinds.** A structural link that lacks a constructional warrant is conceptually unsafe. Conversely, forcing epistemic links to pretend they are structural over-physicalises knowledge claims; for those, evidence or argument is the right currency.
* **Author workload moves, not grows.** Day-to-day model authors stay with working labels; specification authors carry the responsibility for ensuring every structural statement really follows from a sum, a gathering, or a carve-out. This is a conscious shift of complexity away from operations and into the pattern's foundation.

**Invariants you must preserve**

* **Parsimony of constructors.** Build wholes by summing parts; build banks by gathering elements; focus facets by carving aspects. Do not invent extra generative acts for parallelism or time‑slicing; those concerns belong to other conceptual services.
* **Two-relation-kind justification.** Structural talk rides on construction; epistemic talk rides on evidence or proof. Keep the boundary sharp so that downstream reasoning (about reliability, compliance, or policy) remains clear.

**Known consequences**

* **Stable queries, fewer surprises.** Because working labels are backed by shared constructions, teams from different disciplines can interoperate without renegotiating meanings at hand-off.
* **Audit trail without jargon.** Reviewers can trace every structural claim to a prior constructional choice, while everyday collaborators keep using familiar relation names.

