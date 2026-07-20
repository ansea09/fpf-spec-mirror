---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuated Relation Occurrences"
section_id: "A.6.REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__002_problem-frame.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuated Relation Occurrences"
  - "A.6.REL:1 — Problem frame"
line_start: 10508
line_end: 10527
dependencies:
  - "A.6.0"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.18"
keywords:
---

### A.6.REL:1 - Problem frame

**Plain name.** Relation occurrence.

**Primary EntityOfConcern.** One obtaining relation occurrence of an admitted relation kind when one named receiving use needs that occurrence to remain distinguishable from another.

**Primary working reader.** An engineer who states a direct relation and needs to decide whether a named receiving use justifies exposing one occurrence's identity.

**Working concern and viewpoint.** Preserve the readable direct relation assertion while viewing occurrence identity from the named receiving use that depends on it; do not substitute an epistemic, designation, or representation-side object for the world-side relation.

**Use this when.** Use this pattern when one named receiving use needs to distinguish an obtaining relation occurrence from another occurrence of the same relation kind. A work-attribution assertion may designate one role-assignment occurrence; a reliability comparison may compare two installed-part occurrences; a dependent evaluative relation may have one actual-condition relation occurrence as a participant. Each case needs occurrence identity, not only a sentence that states the direct relation.

**First useful move.** Write the direct relation assertion with its named participants. Recover the direct governing pattern, then check that the relation obtains for those participants. In technical terms, those participants jointly satisfy the semantic predicate within the direct relation pattern's declared applicability and temporal conditions. Name the receiving use and apply its direct branch in section 4.2. If that use does not need one occurrence distinguished from another, keep the readable assertion and stop. If it does, apply the direct occurrence-identity rule before assigning an identifier, designating the occurrence in an episteme, or relying on it as a participant of another direct relation.

**What goes wrong if missed.** An epistemic, designation, or representation-side object is treated as what creates the relation it is meant to describe or designate. Repeated assignments or successive assembly episodes with the same participants then collapse into one. At the opposite extreme, every ordinary relational sentence is expanded into a relation-occurrence description episteme even though no receiving use needs that identity.

**What this buys.** Engineers can keep ordinary relation assertions readable. When a receiving use depends on exactly one occurrence, a system performing comparison or evaluation work can distinguish repetition, change, or constitution while assertions, descriptions, designations, representations, and publication occurrences retain their own identities.

**Not this pattern when.** If the wording does not yet identify the direct relation and participants, start with `A.6.P` or `A.6.RSIR`. If the only current basis is an assertion that denies the direct obtaining predicate or belongs to a forecast, scenario, counterfactual, permission, or another separately governed claim family, keep the claim episteme under `C.2.1` and its exact direct claim governor; none of those claim-side facts invents an obtaining occurrence. Only when an explicit reliance judgment is current for the declared use, keep its supported, refuted, or unresolved reliance result separately under `A.10` or the receiving evaluation; that reliance result likewise does not establish obtaining. When the direct relation owner independently establishes obtaining, A.6.REL remains available if a named receiving use needs occurrence identity. If the question concerns only the SlotSpecs of a reusable relation declaration, apply `A.6.5`. If no named receiving use depends on occurrence identity, stop at the direct relation sentence.

