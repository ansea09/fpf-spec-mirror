---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes"
section_id: "B.2:5"
section_title: "Promotion Record & proof obligations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__006_promotion-record-proof-obligations-normative.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "B.2 — Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes"
  - "B.2:5 — Promotion Record & proof obligations (normative)"
line_start: 30642
line_end: 30693
dependencies:
  - "A.1"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.x"
  - "B.2.x"
  - "B.3"
  - "B.4"
keywords:
  - "MHT"
  - "emergence"
  - "meta-system"
  - "new whole"
  - "synergy"
  - "system of systems"
---

### B.2:5 - Promotion Record & proof obligations (normative)

To declare an MHT you MUST create a **Promotion Record** that makes identity, boundary, objective, supervision, and context shifts explicit. This record extends the general proof kit in **B.1.1**.

#### B.2:5.1 - Promotion Record — minimal fields

```
MHT.PromotionRecord
  id:                unique identifier
  eventType:         one of {Fusion | Fission | PhasePromotion | Role‑Lift | ContextReframe}
  transformer:       U.TransformerRole (who/what enacted the transition)
  identityStance:    one of {4D | 3D+1}
  preConfig:
    nodes:           list of holons (ids, kinds) involved before MHT
    edges:           list of relations & their types (A.14), including CL on integration edges
    Γflavour:        active Γ-flavour(s) prior to MHT
    assurance:       Assurance tuples for relevant claims before MHT (B.3)
    boundedContext:  name or description (vocabulary/units/policy) before MHT
  triggers:
    BOSC:            {B? O? S? C?} with measurements and evidence carriers
    A?               Agency-CHR grade & context (A.13)
    T?               Γ\_time phase boundary details (coverage, carrier identity/continuation)
    X?               context mapping summary (old↔new)
  postHolon (H⁺):
    boundary:        explicit BIC or equivalent boundary statement (B.1.2)
    objective:       objective(s) and evaluation basis for H⁺
    supervision:     supervisory/feedback structure present in H⁺ (if any)
    Γflavour:        Γ-flavour(s) intended for H⁺
    assurance:       initial Assurance(H⁺, C | K, S) with F/G/R & CL baselines
    boundedContext:  new context; mapping to previous (with CL for mappings)
  identityMapping:
    4D:              continuity/cut specification (precursors→H⁺ tube start)
    3D+1:            predecessor(s) and creation event; any PhaseOf segments preserved
  notes:
    alternativesConsidered:   why not modelled as non‑MHT Γ improvement
    EvidenceGraphRef:          references to measurements, specs, interface Standards, tests
    orderTimeRefs:            OrderSpec/TimeWindow if Γ\_ctx/Γ\_time material
```

#### B.2:5.2 - Proof obligations specific to MHT

* **MHT‑BOSC‑EVD.** For each selected trigger (B/O/S/C/A/T/X), attach the evidence carriers that evidence it (e.g., boundary Standard for **B**, policy/regulation objective text for **O**, controller‑plant diagram for **S**, capability measurement vs WLNK bound for **C**, Agency‑CHR record for **A**, phase coverage & carrier identity for **T**, context mapping & unit schemes for **X**).

* **MHT‑NO‑EVADE.** Show that the observed improvement cannot be explained by **within‑Γ** moves alone: improved parts (MONO), raised congruence CL, corrected order (Γ\_ctx), or richer phase coverage (Γ\_time). If any of those suffice, **MHT is not justified**.

* **MHT‑ASS‑REBAS.** Provide **before/after** assurance tuples (B.3) for the same typed claim(s) or justify claim changes; do not fuse design-time and run-time scopes.

* **MHT‑IDENT.** State identity stance (4D or 3D+1) and the identity mapping (continuation vs new identity). Mixing stances in the same record is forbidden.

* **MHT‑CTX‑MAP.** For **ContextReframe**, list the concept/unit/terminology mappings and their CL levels; record the **new CL baseline** for future aggregations.


