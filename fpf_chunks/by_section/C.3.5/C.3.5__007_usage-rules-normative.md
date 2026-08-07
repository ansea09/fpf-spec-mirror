---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:6"
section_title: "Usage rules (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__007_usage-rules-normative.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:6 — Usage rules (normative)"
line_start: 45653
line_end: 45664
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.4"
  - "C.3.A"
keywords:
  - "K0-K3"
  - "KindAT"
  - "assurance planning"
  - "declaration planning"
  - "editorial facet"
---

### C.3.5:6 - Usage rules (normative)

**AT-01 (Facet, not Characteristic).** KindAT SHALL be treated as a Facet per MM-CHR. It has no algebra or threshold and MUST NOT appear in guard predicates or composition math.

**AT-02 (Placement).** If recorded, KindAT SHALL characterize one exact local `U.Kind` under an effective reference scheme. A catalog row may represent that assignment. KindAT MUST NOT be attached to a claim, capability, `KindSignature` episteme, candidate, judgment, or extension as a substitute for its own governor.

**AT-03 (No F–G–R effect).** Editors SHALL NOT imply that a higher KindAT widens G, raises the signature episteme's F, increases R, or changes a classification value. Any such sentence MUST name the actual declaration, scope, evidence, or receiving-use change.

**AT-04 (Bridge neutrality).** Neither an obtaining KindBridge relation nor its bridge-assertion episteme computes or alters KindAT. The assertion may record an informative anchor comparison, but `CL^k` remains a separate assessment of the admitted bridge use from demonstrated signature/order preservation and loss.

**AT-05 (Catalog representation).** When a context uses KindAT, its catalog SHOULD identify the local kind and effective reference scheme and reference, rather than collapse, the current `KindSignature` edition, obtaining subkind relations, RoleMask declaration editions, KindBridge occurrences/assertions, and optional extension representations. Absence of a tag means “not set”, not K0.

