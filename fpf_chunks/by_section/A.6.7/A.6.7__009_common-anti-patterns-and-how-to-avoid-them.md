---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Description of a set of distinct mechanisms"
section_id: "A.6.7:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.7 — MechSuiteDescription — Description of a set of distinct mechanisms"
  - "A.6.7:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 15912
line_end: 15933
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.TGA"
  - "G.10"
  - "G.5"
  - "U.Mechanism.Intension"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

### A.6.7:8 - Common Anti-Patterns and How to Avoid Them

1. **Anti-pattern: “Family-as-suite”.**
   Using `MechFamilyDescription` to list multiple distinct mechanisms.
   **Fix:** use `MechSuiteDescription` for “many mechanisms”, and keep `MechFamilyDescription` for “many realizations of one mechanism”.

2. **Anti-pattern: “Pack-as-suite”.**
   Naming/using the suite as a `Pack`.
   **Fix:** reserve `Pack` for publication/shipping bundling; use `Suite` for mechanism bundles.

3. **Anti-pattern: “Suite contains legality tables”.**
   Duplicating CG‑Spec or embedding CL/Φ/Ψ tables in suite obligations.
   **Fix:** publish pins and references only; keep legality content in `…Spec` and policy registries; keep crossing realization in E.TGA/gate surfaces.

4. **Anti-pattern: “Suite is a hidden gate”.**
   Introducing thresholds, `block`, or `DecisionLog` in the suite.
   **Fix:** suite declares guard formats and required pins; the gate issues decisions.

5. **Anti-pattern: “Implicit calls”.**
   A protocol implies “normalize happens somewhere” without explicit member and pin visibility.
   **Fix:** protocols enumerate steps and required pins; E.TGA `Uses` edges remain explicit.

