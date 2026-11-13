---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:17"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__019_sota-echoing.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:17 — SoTA-Echoing"
line_start: 57908
line_end: 57911
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "E.24.UK"
keywords:
---

### C.3.2:17 - SoTA-Echoing

A refusal can suffice when the receiver needs only the guard decision. If the receiver needs classification or a further action, `C.3.2:6` preserves the relevant differences: an unsuitable request yields `not-applicable` and no judgment; missing grounds for an admissible request yield `unknown`; an admissible candidate's known criterion failure yields `false`. Collapsing them into `false` would assert non-membership for a mismatch or missing grounds. Correct the request or seek missing grounds only when a further answer is needed; an adequate negative or unresolved answer can finish the work.

