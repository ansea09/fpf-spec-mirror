---
chunk_kind: "child"
pattern_id: "E.5.1"
pattern_title: "DevOps Lexical Firewall"
section_id: "E.5.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.1/E.5.1__005_solution.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.5.1 — DevOps Lexical Firewall"
  - "E.5.1:4 — Solution"
line_start: 101638
line_end: 101658
dependencies:
  - "E.5"
keywords:
---

### E.5.1:4 - Solution
Apply the **Lexical Firewall** to the subject the text governs:

1. **Keep abstract definitions independent of incidental machinery.**
   A Core definition **SHALL NOT** make an unrelated tool, file format, command or deployment arrangement necessary to identify or use its conceptual subject. Describe that subject directly. Place the implementation in Tooling.

2. **Retain the syntax needed to test conformance of a concrete subject.**
   When a rule governs a publication form, protocol or grammar, it **MAY** state the exact syntax needed to apply that subject's conformance condition. Name the subject and its edition or use boundary. The exception applies only where replacing the syntax with a conceptual alias would remove an operative condition.

   A heading marker in a heading grammar qualifies. An unrelated build command does not. Calling executable code a grammar example supplies no exception.

3. **Keep executable teaching in its teaching or Tooling source.**
   A Core concept needing a runnable illustration cites the teaching or Tooling artifact by conceptual name. Runnable teaching programs, concrete execution paths and commands remain there. A subject-defining syntax fragment under item 2 is not a runnable illustration merely because it appears in a code span or block.

   Mathematical expressions follow E.5.2: explain their interpretation, operation and prerequisites, with semantic mapping when compared or translated.

4. **Use aliases where they preserve the rule.**
   An incidental technical term can be defined in a Tooling Glossary and cited by conceptual alias. Preserve necessary spelling under item 2 when the concrete subject's condition would otherwise become untestable.

*Non‑normative automation.* Machine checks **MAY** exist in Tooling. They are advisory and **MUST NOT** be imported into the Core.

