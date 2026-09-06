---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Use-Bounded Representation Selection and Co-Use"
section_id: "C.37:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__003_problem.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.37 — Use-Bounded Representation Selection and Co-Use"
  - "C.37:2 — Problem"
line_start: 67963
line_end: 67976
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.22"
  - "A.6.3.RT"
  - "C.11"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
keywords:
---

### C.37:2 - Problem

Representations are useful because they foreground different things. A workflow diagram may expose order while hiding effort. A work plan may expose intended timing while saying nothing about actual performance. A work record may expose an observed breakdown while saying nothing about whether a proposed change will repair it. A graph may support traversal or calculation while omitting distinctions needed by a receiving decision.

The practical question is therefore not “which representation is best?” It is “which exact candidate result may this receiver use for this action, for which claim, under which limits, and what direct result makes that use available?”

Five recurrent shortcuts make the answer unsafe:

1. **Object shortcut.** A label such as *diagram*, *view*, *model*, *graph*, or *record* substitutes for the direct result that identifies the candidate and its subject-side claim.
2. **Classification shortcut.** An A.2.4 intended first evidence-use classification is treated as evidence sufficiency or permission.
3. **Provenance shortcut.** A source path, current carrier, or authentic publication is treated as a positive `RelianceDisposition` or receiving result.
4. **Decision shortcut.** A selected row is treated as the choice, authorization, permission, or gate result without the direct receiving pattern.
5. **Composition shortcut.** Several rows are treated as a collection, structure, integrated view, world model, or graph merely because one receiver reads them together.

