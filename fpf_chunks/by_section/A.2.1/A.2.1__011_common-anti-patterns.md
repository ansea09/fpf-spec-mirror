---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.SystemRoleAssignment - Contextual System-Role Assignment"
section_id: "A.2.1:9"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__011_common-anti-patterns.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.2.1 — U.SystemRoleAssignment - Contextual System-Role Assignment"
  - "A.2.1:9 — Common Anti-Patterns"
line_start: 3701
line_end: 3713
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.3.3"
  - "F.6"
  - "F.9"
keywords:
  - "assignment predicate"
  - "direct assignment species"
  - "holder System"
  - "identity"
  - "maximal interval"
  - "performedUnderAssignment"
  - "system-role kind"
---

### A.2.1:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `Alice is reviewer`, used as assignment identity | It names neither species nor occurrence. | Recover the direct species and the obtaining occurrence needed by the receiver. |
| One universal binary assignment relation over `U.Kind` | It admits arbitrary kinds and hides stronger participant laws. | Use one exact local assigned-kind domain in every direct species. |
| Generic assignment plus appointment occurrence | One world-side episode receives two competing identities. | Make the appointment species a subtype of `U.SystemRoleAssignment`; use its holder projection. |
| One assignment row reused for every shift | Storage identity collapses repeated occurrences. | Distinguish maximal uninterrupted predicate-true intervals. |
| Assignment proves Work | Holding is confused with dated performance. | Use A.13 to identify each actual performer and A.15.1 to admit the Work independently. Add F.6 only if the current use also needs the exact assignment under which that Work was performed; a missing or failed check leaves the Work intact. |
| Durable `RoleEnactment` object | It duplicates Work and attribution. | Use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. Add the exact assignment and F.6 only if the current use must also say under which assignment the Work was performed; do not mint a duplicate occurrence. |
| Report holds a system-role assignment | An episteme is made a holder by usefulness. | Use its direct evidence, result, source-use, or publication relation. |
| Optional `ContextSlot` everywhere | Unrelated locality, scope, structure, and locus meanings collapse. | Recover the denoted object and declare it only when a direct species truly depends on it. |

