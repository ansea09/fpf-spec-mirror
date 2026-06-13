---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__008_conformance-checklist.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:6 — Conformance Checklist"
line_start: 70827
line_end: 70846
dependencies:
  - "A.15"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "C.3"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "E.21"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.24:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E24-1` | The authoring decision names the primary `EntityOfConcern`, bounded context, and current claim before proposing a durable ontic. |
| `CC-E24-2` | Existing governing patterns are checked by value before a new ontic is selected. |
| `CC-E24-3` | A durable ontic publishes stable identity criteria and says what does and does not change identity. |
| `CC-E24-4` | A durable `onticSlotRelation` names SlotKinds, ValueKinds, RefKinds, relation set, species or record forms, non-slot components, and description/publication boundary. |
| `CC-E24-5` | The decision declares the selected `ontic` components by value: `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `onticSlotRelation`, selected `ontologicalNeighborhood`, pattern nest, and dependent-pattern obligations, without treating any of them as synonyms. |
| `CC-E24-5a` | The pattern keeps ontic root identity, type-level `onticSlotRelation`, filled value assignment or ordinary-use core, description episteme/publication, and neighboring relation references distinct; a filled core or neighbor list is not treated as a second ontology. |
| `CC-E24-6` | Draft-only loci are marked non-governing until a current pattern or accepted stub carries named conformance gaps. |
| `CC-E24-7` | A local use frame is explicitly non-`U.*`, non-ontic, and points typed values to their governing patterns. |
| `CC-E24-8` | The selected name passes `F.18`; the name does not hide a second ontology or one umbrella for several kinds. |
| `CC-E24-8a` | Durable `U.*` names, reusable SlotKind heads, species or record-form names, public ids, Core-facing heads, and cross-context labels use `F.18`; `F.17 UTS` / Name Card material is opened only when that name becomes public, Core-facing, or cross-context, and never replaces the `A.6.5` / `SlotSpec` slot relation. |
| `CC-E24-9` | Pattern-quality and DRR-adequacy checks stay in `E.21` and `E.9.DA`; they are not copied as user-facing ontic or subject-matter content. |
| `CC-E24-10` | Dependent patterns state how they rely on the head ontic or local use frame without duplicating the whole slot relation. |
| `CC-E24-11` | Slot-position labels, including role-like labels, method-like labels, mechanism-like labels, temporal labels, source labels, and publication labels, do not create alternate ontology; `U.Role` is not a SlotKind, SlotKind is not a role, and role participation uses a slot-disciplined `U.RoleAssignment` only when the A.2/A.15 role-governing patterns govern the case. |
| `CC-E24-12` | Ontic slot talk uses slot-language (`onticSlotRelation`, `SlotSpec`, `SlotKind`, `ValueKind`, `RefKind`, slot discipline, slot/relation boundary); `interface` is used only when a governing boundary, module, signature, mechanism, or architecture pattern makes interface meaning current. |
| `CC-E24-13` | Source-ontology annotation is proportional: load-bearing kind, slot, relation, admissible-use, and governing-pattern differences are recovered, while stable domain prose is not expanded into type labels. |

