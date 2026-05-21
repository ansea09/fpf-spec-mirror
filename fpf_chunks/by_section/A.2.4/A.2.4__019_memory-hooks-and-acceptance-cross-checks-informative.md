---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "U.EvidenceRole"
section_id: "A.2.4:18"
section_title: "Memory hooks and acceptance cross-checks (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__019_memory-hooks-and-acceptance-cross-checks-informative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.2.4 — U.EvidenceRole"
  - "A.2.4:18 — Memory hooks and acceptance cross-checks (informative)"
line_start: 3373
line_end: 3390
dependencies:
  - "A.10"
  - "A.2"
  - "B.3"
keywords:
  - "claim"
  - "episteme"
  - "evidence"
  - "justification"
  - "support"
---

### A.2.4:18 - Memory hooks and acceptance cross-checks (informative)

**Memory hook:** *“Evidence links a **document** to a **claim** in a **Context**, for a **time**, with a **trail**.”*
(document = episteme; claim = scoped thesis; Context = bounded context; time = timespan/decay; trail = provenance)

**Acceptance cross-checks before publishing a binding:**

1. **Holder**: Is it a `U.Episteme`?
2. **Context**: Is the `U.BoundedContext` declared?
3. **Claim**: Does `claimRef` resolve? Is `polarity` set?
4. **Scope**: Is `claimScope` complete? For empirical, are population/env/parameters given?
5. **Timespan**: Is it finite or fenced (formal line)?
6. **Provenance**: Is EPV anchored? Any self-evidence?
7. **Reproducibility**: For empirical, is it declared?
8. **Weight**: If scored, is the model named and inputs complete?
9. **Cross-context**: If imported, is `U.Alignment` bridge in place with CL\_min recorded?
10. **No role-of-role**: Is this role bound directly to an episteme without chaining behavioural roles?

