---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__014_relations.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:12 — Relations"
line_start: 90228
line_end: 90235
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.2.6"
  - "A.22"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "U.MethodDescription"
  - "U.Structure"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:12 - Relations

- **Shares settlement with:** `E.24` through the one `E24FamilySettlementDecision` schema in `E.24:4.0a`. E.24.UK records the `UKindAdmissionResult`; E.24 records the `OnticSettlementResult`. An existing result may be reused, while a case needing both new outputs is one atomic co-decision with neither output used as prior evidence.
- **Uses for relation admission:** `A.6.REL` defines the common occurrence discipline; each relation's ClaimGraph supplies participant meanings, obtaining, applicability, and occurrence identity; and an `A.6.RCD` application may record a residual claim or a derived-or-primitive candidate with its proposed direct subject settlement. Local-claim and predicate-definition results remain claim content and do not admit a relation kind.
- **Uses for neighboring objects:** `A.6.0` defines reusable signature identity; `A.6.5` defines `SlotSpec` declarations; `C.2.1` defines admission-decision, assertion, and description episteme identity; `F.18` supplies the naming rule for selected Tech labels and designators; `C.29` defines mathematical and data-model representation use.
- **Coordinates with:** `A.22` for context-independent base `U.Structure` identity, the `BoundedModelUseStructure` membership condition, and the still-local conditional crossing-analysis rule; `A.1.1` for the bounded model-use participants and exact obtaining relations; `A.2.6` for claim-scope membership used by exact applied constraints; `C.3`, `C.3.1`, and `C.3.2` for local typed reasoning and membership judgments; `E.24.CD` for candidate detection before an E.24 ontic decision; any resulting U-kind spelling or admission pressure still requires its own E.24.UK decision, and neither pattern determines the other's disposition; `E.24.PUB` for `EpistemePublicationRelation`, publication form, and carrier distinctions; `A.3.2` for `U.MethodDescription` membership; `E.17.0` for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View` membership; `A.6.3` only for an optional viewing construction; `A.8` and `A.11` for kernel parsimony; and `E.10` for source wording that still hides the governed object.
- **Does not replace:** the rule that defines or constrains the classified individuals, their identity or membership, intended extent, and action-facing use, or the PatternID that locates that rule.

