---
chunk_kind: "child"
pattern_id: "E.5"
pattern_title: "Four Guard‑Rails of FPF"
section_id: "E.5:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5/E.5__007_conformance-checklist.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.5 — Four Guard‑Rails of FPF"
  - "E.5:6 — Conformance Checklist"
line_start: 64635
line_end: 64645
dependencies:
  - "E.2"
  - "E.3"
  - "E.5.1"
  - "E.5.2"
  - "E.5.3"
  - "E.5.4"
keywords:
  - "GR-1 to GR-4"
  - "architecture"
  - "constraints"
  - "guardrails"
  - "rules"
  - "safety"
---

### E.5:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑GR.1** | Every new Core pattern **SHALL** cite, in its *Relations* section, the guard‑rail(s) it relies on or may affect. | Ensures traceability and deliberate rule interaction. |
| **CC‑GR.2** | Artefacts classified as Tooling or Pedagogy **MUST NOT** violate any rule in GR‑1 through GR‑4. | Keeps entropic forces outside the Conceptual Core. |
| **CC‑GR.3** | A revision to any guard‑rail pattern **REQUIRES** a Design‑Rationale Record that (a) states the reason, and (b) includes a Pillar‑impact analysis per E.3 precedence model. | Aligns evolution with higher‑level principles. |
| **CC‑GR.4** | The aggregate of guard‑rail rules **MUST** remain internally consistent and acyclic; no guard‑rail may override another without explicit precedence edges. | Preserves deterministic governance. |
| **CC‑GR.5** | Every Core pattern **MUST** anchor its primary primary EntityOfConcern or primary relation with a declared **ReferencePlane** (`world | concept | episteme`) at first mention. | Keeps Core about extensional or intensional values rather than their paperwork, and aligns with CHR:ReferencePlane. |
*All CC‑GR duties are **conceptual**. Any automated checks are **informative only** and live in Tooling/Pedagogy.*

