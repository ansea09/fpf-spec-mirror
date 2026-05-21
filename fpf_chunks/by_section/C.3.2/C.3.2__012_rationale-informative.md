---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "KindSignature (+F) & Extension/MemberOf"
section_id: "C.3.2:11"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__012_rationale-informative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.3.2 — KindSignature (+F) & Extension/MemberOf"
  - "C.3.2:11 — Rationale (informative)"
line_start: 36820
line_end: 36836
dependencies:
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
keywords:
  - "Formality F"
  - "KindSignature"
  - "MemberOf"
  - "determinism"
  - "extension"
  - "intension"
---

### C.3.2:11 - Rationale (informative)

#### C.3.2:11.1 - Why give **F** to `KindSignature`?

Because rigor in the **definition of a kind** materially affects how safely teams can quantify over it. A signature at **F4** (predicate‑like) makes membership checkable in principle; **F7+** (machine‑checked) can support proof‑carrying development. Keeping this **separate from claim‑level F** prevents “signature formalization” from inflating unrelated claims.

#### C.3.2:11.2 - Why **Extension** is not **Scope**

* **Extension** answers: *“Which entities count as `k` **in this slice**?”*
* **Scope (G)** answers: *“In which slices does **this claim** hold?”*
  Blending the two recreates the old failure mode where “more abstract wording” was treated as “wider applicability.” USM already gives the set‑algebra for G; Kind‑CAL supplies the **typed universe** the claim quantifies over.

#### C.3.2:11.3 - Why **determinism** and **fail‑closed**?

Guards must be **reproducible** and **auditable**: same `slice` ⇒ same membership result. If inputs are missing (undefinedness), the safest default is **deny** (fail closed), prompting either a richer slice or a scope/claim change.


