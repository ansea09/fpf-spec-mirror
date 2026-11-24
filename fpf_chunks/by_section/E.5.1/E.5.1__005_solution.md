---
chunk_kind: "child"
pattern_id: "E.5.1"
pattern_title: "DevOps Lexical Firewall"
section_id: "E.5.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.1/E.5.1__005_solution.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "E.5.1 — DevOps Lexical Firewall"
  - "E.5.1:4 — Solution"
line_start: 102593
line_end: 102613
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

   E.8 H-2 specifies the characters that separate a heading identifier from its title. An editor can explain the separator in prose. To decide whether a submitted heading conforms, inspect the characters in that heading. A correct explanation of the rule can accompany a heading that fails it. An unrelated build command belongs with the tool that uses it.

3. **Keep executable teaching in its teaching or Tooling source.**
   A Core concept needing a runnable illustration cites the teaching or Tooling artifact by conceptual name. Runnable teaching programs, concrete execution paths and commands remain there. A subject-defining syntax fragment under item 2 is not a runnable illustration merely because it appears in a code span or block.

   Mathematical expressions follow E.5.2: explain their interpretation, operation and prerequisites, with semantic mapping when compared or translated.

4. **Use aliases where they preserve the rule.**
   An incidental technical term can be defined in a Tooling Glossary and cited by conceptual alias. Preserve necessary spelling under item 2 when the concrete subject's condition would otherwise become untestable.

*Checking an instance.* A Tooling check that reads the exact characters of a submitted heading can establish whether its separator satisfies H-2. Finding a technical word can locate a possible dependency. To decide whether the definition actually depends on that tool, examine its meaning under the Core rule. Acceptance follows the authority and conditions of the governing practice. The executable check **MUST** remain outside Core.

