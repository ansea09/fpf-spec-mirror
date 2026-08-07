---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:9"
section_title: "Anti‑patterns & Remedies (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__010_anti-patterns-remedies-informative.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:9 — Anti‑patterns & Remedies (informative)"
line_start: 45477
line_end: 45487
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

### C.3.4:9 - Anti‑patterns & Remedies (informative)

| Anti‑pattern                                      | Why it’s wrong                         | Remedy                                                                                |
| ------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------- |
| Mask treated as a new type | Duplicates the kind and hides the declaration episteme | Keep the base kind; for a stable conceptual refinement identify another local kind and establish `U.SubkindOf` independently. |
| Hiding Scope in a masked judgment | Conflates context with candidate features | Move context predicates to USM guards; keep only direct candidate-feature predicates in `J_mask`. |
| Unregistered mask in guards                       | Non‑deterministic; un‑auditable        | Register & version the mask; fail closed otherwise.                                   |
| Cross-context use without exact bridge and adapter objects | Silently reuses source truth | Establish the KindBridge relation and bridge assertion, target declarations, and any MaskAdapter episteme; then evaluate the target `J_mask` and apply justified R penalties. |
| Mask proliferation (ten masks that mean the same) | Catalog entropy; inconsistent behavior | Consolidate declarations; for a stable conceptual distinction, separately identify a local kind and establish its obtaining `U.SubkindOf` relation. |
| Treating a mask name as a kind synonym | Hides constraints and invites misuse | Designate the exact RoleMask declaration edition and base kind separately in prose and guards. |

