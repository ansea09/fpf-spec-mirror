---
chunk_kind: "child"
pattern_id: "A.7"
pattern_title: "Strict Distinction (Clarity Lattice)"
section_id: "A.7:14"
section_title: "Practitioner one-page review (copy-paste)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.7/A.7__016_practitioner-one-page-review-copy-paste.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.7 — Strict Distinction (Clarity Lattice)"
  - "A.7:14 — Practitioner one-page review (copy-paste)"
line_start: 21869
line_end: 21889
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "E.10"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
keywords:
  - "EntityOfConcern ≠ Description episteme"
  - "Role ≠ Work"
  - "category error"
  - "ontology"
---

### A.7:14 - Practitioner one-page review (copy-paste)

**Approval sentence template**

> “`U.RoleAssignment(holderRef=⟨system-or-acting-holon⟩, roleRef=⟨Role@Context⟩, boundedContextRef=⟨Context⟩)` is current for the work; the holder has **Capability** ⟨C⟩ to enact exact **Method** ⟨M⟩; the receiving `methodRef` resolves directly to ⟨M⟩ under its effective reference scheme; when this claim actually relies on separately admitted **MethodDescription** episteme ⟨S⟩, cite that edition separately; the holder executed **Work** ⟨W⟩ on ⟨time⟩ and cites A.10 evidence-provenance or carrier/source-currentness refs ⟨ids⟩; resources are accounted through the governing work-cost relation.”

**Six binary checks**

1. **Bare acting-subject check:** No bare “actor” token in normative core claims; canonical `U.RoleAssignment` phrasing is present when a work-facing role is current.
2. **Clear work-facing positions:** Exact Method, Capability and Work are named when current and not conflated. A MethodDescription is named only when its independently identified episteme and claims pass A.3.2 membership.
3. **Direct reference and membership:** An identifier's designation of the Method and the receiving claim's resolved `methodRef` remain distinct; neither requires a MethodDescription. Any `methodDescriptionRef` points to a separate episteme whose exact EntityOfConcern is that Method and whose claims cross the substantive way-of-doing threshold.
4. **Right Γ:** Γ\_method composes Method; Capability states a system ability/envelope under conditions; Γ\_time covers occurrences; Γ\_work accounts resources; Γ\_sys covers system properties.
5. **Episteme handled:** Epistemes do not act; carriers or source-currentness refs are listed when evidence or source use is current.
6. **Group clarity:** Acting group is a **collective system**, not a MemberOf set.

**Diagram legend stub**

* “process (domain)” ⇒ Method (design-time) / Work (run-time).
* Role column lists role values and assignment references (e.g., `CoolingCirculatorRole@Context`).
* Behaviour column shows Method and Work, not the role itself.

