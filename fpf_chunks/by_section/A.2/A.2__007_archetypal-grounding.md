---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__007_archetypal-grounding.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:5 — Archetypal Grounding"
line_start: 2847
line_end: 2892
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:5 - Archetypal Grounding

#### A.2:5.1 - Pump in a Cooling Loop

Plant operation relies on a current assignment. The four values under `participantDesignations` designate the direct relation participants; `assignmentInterval` is assertion content describing the currently known extent of the uninterrupted occurrence.

```text
RoleAssignmentAssertion@PumpUnit3:
  participantDesignations:
    HolderSystemSlot: PumpUnit-3
    RoleValueSlot: CoolingCirculatorRole
    RoleTaxonomyEpistemeSlot: PlantOperationsRoleTaxonomy-2026
    EffectiveReferenceSchemeSlot: Plant-A-Operations-Scheme
  assignmentInterval: [2026-06-01, open]
```

`PumpUnit-3` is the holder system. `PlantOperationsRoleTaxonomy-2026` contains the role-vocabulary claims, and `CoolingCirculatorRole` is interpreted under `Plant-A-Operations-Scheme`. Plant A is an actual plant system and work locus, not a context slot. No selected model-use structure is needed because none changes interpretation of this assignment.

The world-side assignment occurrence continues only while its predicate obtains without interruption for the same four participants. Closing the open assertion interval later refines the same description when continuity holds; the declared interval neither makes the relation obtain nor becomes a fifth participant.

The assignment does not prove that the pump can circulate coolant throughout every operating region, that circulation work occurred, or that a maintenance method was followed. Those claims use `A.2.2`, `A.15.1`, and the applicable method, transformation, measurement, and evidence relations.

#### A.2:5.2 - A Standard Used in Design Work

An engineering team uses the RFC 9110 publication while designing an HTTP service. Keep three claims separate:

1. `DesignTeam-2` holds `ProtocolDesignerRole` under `EngineeringRoles-2026`, interpreted through `HTTP-Design-Scheme`, during one current uninterrupted assignment episode.
2. The RFC publication is the source episteme in a source-use relation whose receiving use is the HTTP-semantics constraint set in the team's design method description.
3. The dated design work is performed by `DesignTeam-2` and may produce a method description or system description.

The team uses the publication as the named source for those constraints. The publication neither holds the design role nor performs the work.

#### A.2:5.3 - The Same Label under Two Role Taxonomies

An editorial team and a safety-assurance team both use `ReviewerRole`. Their role-taxonomy epistemes contain different admission, independence, evidence, and completion claims, each interpreted under its effective reference scheme. The shared label establishes neither one role meaning nor a Bridge.

Suppose a staffing dashboard proposes `u-reviewer-display`: show assignments from both taxonomies in one `Reviewer` column. First recover the exact F.17 sense cells and establish the exact obtaining F.9 Bridge between them. Then state a separate affirmative C.2.1 assertion about that Bridge: direction `d-safety-to-editorial-display`; rule `r-preserve-reviewer-differences`, which keeps each taxonomy's admission, independence, evidence, and completion claims in separate fields; and tolerance `t-shared-label-only`, which permits the shared display label but no assignment, eligibility, capability, substitution, or performed-work inference. Its effective reference scheme interprets those designations.

For this ordinary display use, the exact current A.10 evidence-provenance graph relation and `RelianceDisposition=pass` support only `u-reviewer-display`. They do not justify putting a safety-assurance reviewer into an editorial assignment. That substitution would be another bounded-use assertion with its own direction, rule, tolerance, polarity, and reliance. If an assurance claim is being made or B.3's material-reliance threshold is met, first ask whether a current positive B.3 assurance claim exists: only one that carries the same use with a sufficient minimum reliance safety assurance record supports it; otherwise an explicit no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked disposition stops or narrows the use.

A Bridge Card may package the Bridge, bounded-use assertion, evidence, and disposition, but neither the card nor the Bridge alone establishes use suitability, assigns either role, or proves that dashboard or substitution work occurred. Any actual assignment, comparison, or work remains under its direct owner. If an independently selected DDD-style model-use structure changes one receiving interpretation, designate it in that receiving assertion or use. A genuinely structure-dependent relation species requires its own direct pattern, required structure participant, stronger predicate, and occurrence-identity rule; it is not an optional extension of a generic role relation.

#### A.2:5.4 - Relation Participant Slot Named Role

An external relation notation may label one participant as `role`. In FPF the declaration first recovers one participant SlotKind and its SlotSpec. The ValueKind is `U.Role` only when the filler is genuinely an enactment-facing role value. Otherwise the ValueKind remains the direct kind of the actual participant. The external label alone creates neither a `U.Role` value nor a `U.RoleAssignment`; an admitted system holds a role only through the separately obtaining assignment relation.

