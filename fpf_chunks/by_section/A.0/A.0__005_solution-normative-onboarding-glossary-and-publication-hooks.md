---
chunk_kind: "child"
pattern_id: "A.0"
pattern_title: "Generative Search Onboarding Glossary (NQD & E/E‑LOG)"
section_id: "A.0:4"
section_title: "Solution - Normative onboarding glossary and publication hooks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.0/A.0__005_solution-normative-onboarding-glossary-and-publication-hooks.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.0 — Generative Search Onboarding Glossary (NQD & E/E‑LOG)"
  - "A.0:4 — Solution - Normative onboarding glossary and publication hooks"
line_start: 2335
line_end: 2375
dependencies:
  - "A.19"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.19.SOURCE-SET-SPACE-SUBSTRATE"
  - "A.5"
  - "B.5"
  - "B.5.2.1"
  - "C.17"
  - "C.17-C.19"
  - "C.19"
  - "E.10"
  - "E.2"
  - "E.7"
  - "E.8"
  - "F.17"
  - "G.12"
  - "G.5"
  - "G.9"
  - "G.9-G.12"
  - "U.EpistemeRef"
keywords:
  - "& queries. novelty"
  - "BLP"
  - "CL^plane"
  - "DeclaredSubstrateInterpretiveView"
  - "OutcomeSpaceRef"
  - "ParetoOnly default"
  - "ReferencePlane"
  - "SearchSpaceRef"
  - "TypedSetViews"
  - "comparability"
  - "declared set result"
  - "explore/exploit (E/E-LOG)"
  - "explore/exploit (E/E‑LOG)"
  - "illumination map (report‑only telemetry)"
  - "novelty"
  - "parity run"
  - "quality-diversity (NQD)"
  - "quality‑diversity (NQD)"
  - "scale-probe"
  - "typed portfolio publication"
---

### A.0:4 - Solution - Normative onboarding glossary and publication hooks



#### A.0:4.1 - Plain one‑liners (normative on‑ramp; formal anchors in C.17–C.19)


| Term                      | Plain definition (on‑ramp)                                                                                                                                   | See        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **Novelty (N)**           | How unlike the known set a candidate is in your declared **CharacteristicSpace**. Use the declared `DescriptorMapRef` and `DistanceDefRef`, with no ad-hoc normalisation. | C.17, C.18 |
| **Use‑Value (U / ValueGain)** | What the candidate helps you achieve now under your **CG‑Frame**; tie to acceptance/tests; **publish units, scale kind, polarity, ReferencePlane**.                   | C.17, C.18 |
| **Constraint‑Fit (C)**    | *Satisfies must‑constraints (Resource/Risk/Ethics)*; legality via **CG‑Spec**; **unknowns propagate** (never coerce to zero).                                | C.18, G.4  |
| **Diversity_P (declared retained set)** | Coverage or dispersion of the declared retained set under a named measurement policy; declare **ReferencePlane**. Its change on adding one candidate is **DeltaDiversity_P**. | C.17, C.18 |
| **E/E‑LOG**               | *Named, versioned **explore↔exploit** policy*; governs when to widen space vs refine candidates; **policy‑id is published**.                                   | C.19       |
| **ReferencePlane**        | *Where a value lives:* **world** (system), **concept** (definition), **episteme** (about a claim). For a plane relation, retain its source/target planes and basis. Cite **CL^plane** for a used or required calibration and the **Φ_plane** policy and loss model for a used or required loss calculation; any numerical assurance penalty requires an applicable B.3 model. | F.9, G.Core:4.2.3 |
| **Scale Variables (S)** | Ordered settings such as iteration budget, data exposure or resolution. For a scale claim, identify which settings vary, the tasks, the response of interest and the range examined. | C.18.1 |
| **Scale Elasticity (χ)** | A supported response class (*rising*, *knee*, *flat* or *declining*) over the tested settings, or a wider range when a model or bound justifies the extension. Leave the class open when evidence is insufficient. | C.18.1 |
| **BLP (Bitter‑Lesson Preference)** | A preference supported by a comparable, uncertainty-qualified scale comparison; begin with a **cheap scale-claim probe**. **No scale claim yet** or **no scale-based preference** are valid results. A local generality policy is a separate declared basis. | C.19.1, C.24 |
| **Iso‑Scale Parity** | A comparison of candidates at matched resource settings under a justified common basis. To assess change with scale, compare responses at distinct settings. A knee needs at least three ordered settings along one coordinate or specified path, with evidence for the change in slope. | G.9, C.18.1 |

*(Use **LEX‑BUNDLE** for the applicable measurement and scope terminology.)*



#### A.0:4.2 - Publication & telemetry duties (where these terms **show up**)


1. **UTS surface (Part F).** When a **UTS row describes a generator, selector, typed portfolio publication, or set-return publication surface**, it **MUST** surface each glossary value or policy used by the declared operation or independently required by the receiving use. Type each reported value's applicable **units, scale, polarity and ReferencePlane** under **MM‑CHR** and **CG‑Spec**, and cite its defining basis, including `DescriptorMapRef` and `DistanceDefRef` when used or required. *(Row schema: F.17; shipping via G.10.)*
2. **Parity & edition pins (Part G).** When QD/OEE is in scope, **pin the editions and policies used by the operation or required by its receiving use**, including `DescriptorMapRef.edition`, `DistanceDefRef.edition`, the `CharacteristicSpaceRef` with its separate `characteristicSpaceDescriptionRef: U.EpistemeRef` under A.19:5.1.1.1 and `TransferRulesRef.edition` where applicable; record `PathSliceId` when required by that use. **G.9** supplies the pin requirements for a parity use. Treat **illumination/coverage as report‑only telemetry**; publish an **Illumination Map** where G‑kit mandates parity records. For an empirical claim about how performance changes with scale, declare **S** and use comparison evidence at distinct settings. Reuse an applicable **scale‑probe**. A theoretical prediction states the assumptions and range that support it. **Dominance policy defaults to `ParetoOnly`;** including illumination in dominance **MUST** cite a CAL policy‑id.
3. **Ground generative claims (E.7/E.8).** An architectural pattern claiming generative behaviour **MUST** show which action or conclusion requires the generative claim, who generated or selected the alternatives where this matters, and which conditions and glossary distinctions warrant the conclusion. Use a system or episteme illustration when it reveals a condition of that claim.



#### A.0:4.3 - Putting the glossary to use

1) **Recover the decision before choosing the table.** Who will use the result, by when and with what authority? If they need one workable option, an existing candidate with established fitness may finish the job (C.38). A request for the best option also needs a comparison over the allowed alternatives. If the order calls for new candidates, generate them. For a decision left to the recipient, preserve the alternatives they can identify and use in time. Distinguish who set the goal, proposed the candidates and chose the criteria. When designing the search, make and justify the choices left open. When applying a supplied rule, credit those choices to whoever made them.
2) **Work out which choices have to fit together.** Several recipients may choose independently, need the same option, or need every member of a combination. Compare whole combinations when a shared resource or condition affects their suitability. For one feasible combination, exhibit it or establish its existence as the request requires. To promise support for every allowed joint choice, establish a way for the participants to meet every such request. At each commitment the plan assigns an authorised action to each participant on the information that participant has. It must work in every situation still compatible with that information. The plan can branch on a distinction that reaches the participant in time. A declaration of agreed members needs the agreement. A report of actual use needs evidence of the work.
3) **Choose what to compare or count.** Start with the candidates the commission allows, including ones beyond the current table. When designing a comparison, hold your proposed readings fixed and vary a permitted use or shared condition. If the recipient would have to act differently or give a different justification, retain that distinction or establish how the recipient can learn it in time. Group cases when the same answer and grounds hold (C.39.SA:4). State the eligible population, the question of quality, the admissible units and scales (**CG‑Frame**) and the **ReferencePlane**. Choose the **Q components** or **DescriptorMap** coordinates used by this operation and retain their meanings and applicable editions. Occupied cells describe a retained archive. A claim about which regions were tested needs evidence of the tests, including rejected candidates when they count. To report all nondominated answers, establish completeness for the requested population and distinguish objective values, one realization of each value, and all qualifying candidate identities (C.18:4.4).
4) **Use the method for the requested result.** C.11 governs a local choice. C.18 supplies an archive or front. Use C.19 and record the **E/E‑LOG policy‑id** when the search needs explore/exploit control. Use **G.5** for method-family dispatch or to declare a selected set on an established basis. Keep any consumed `Front` or `Archive` identifiable as the source. Return `Shortlist` or `RankedShortlist` for retained alternatives and `JointUseSet` when all named members are included for one use. A G.5 handoff, abstention or escalation carries its own grounds.
5) **Deliver what the recipient can use.** Keep references to the criteria, evidence and editions used for the result (basis pins). To compare runs on common terms, also record the editions and policies that G.9 requires for that comparison (parity pins). Publish when the receiving use calls for publication, with the applicable **PathIds/PathSliceId**. Add a UTS row for a named governed value when F.17's independent naming and reuse conditions hold. An **Illumination Map** remains **report‑only telemetry** by default.

