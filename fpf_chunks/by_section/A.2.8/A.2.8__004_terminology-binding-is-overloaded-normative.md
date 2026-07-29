---
chunk_kind: "child"
pattern_id: "A.2.8"
pattern_title: "U.Commitment (Deontic Commitment Object)"
section_id: "A.2.8:0.1"
section_title: "Terminology: “binding” is overloaded (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8/A.2.8__004_terminology-binding-is-overloaded-normative.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "A.2.8 — U.Commitment (Deontic Commitment Object)"
  - "A.2.8:0.1 — Terminology: “binding” is overloaded (normative)"
line_start: 5686
line_end: 5693
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.2.6"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "A.7"
  - "E.8"
  - "U.PromiseContent"
  - "U.Work"
keywords:
  - ") but makes the structure explicit"
  - "BCP‑14 (RFC 2119/8174)"
  - "adjudication hooks"
  - "are cues for the modality field after the deontic relation is recovered"
  - "by themselves"
  - "commitment"
  - "deontics"
  - "evidenceRefs"
  - "modality normalization"
  - "obligation"
  - "prohibition"
  - "recommendation-as-duty"
  - "scope and validity window"
  - "they are not the governed object of this pattern"
---

### A.2.8:0.1 - Terminology: “binding” is overloaded (normative)

The word family “bind/binding” is used throughout FPF for **technical binding** (name/slot binding, parameter binding, etc.). This pattern introduces a narrower lexical constraint: **do not use “binding” as the Tech-level term for deontic governance relations.** Use **commitment** and model it as `U.Commitment`. If source wording uses “binding contract/promise” rhetoric, rewrite it into explicit `U.Commitment` fields (`subject`, `modality`, `scope/window`, `referents`, and—when auditable—`adjudication`).

This pattern therefore treats **commitment** as the canonical Tech-level term and uses `U.Commitment` as the kernel object.

If source wording uses “binding” rhetoric (e.g., “binding contract”, “legally binding promise”), treat it as Plain-level phrasing that must be recovered into explicit `U.Commitment` fields (`subject`, `modality`, `scope/window`, `referents`, and, when auditable, `adjudication`). Deontic keywords are cues for the modality field after the deontic relation is recovered; they are not the governed object of this pattern.

