---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "U.Holon, U.System, and U.Episteme"
section_id: "A.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__002_use-this-when.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.1 — U.Holon, U.System, and U.Episteme"
  - "A.1:0 — Use This When"
line_start: 1326
line_end: 1351
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.22"
  - "A.6.5"
  - "A.7"
  - "C.2.1"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.PUB"
keywords:
---

### A.1:0 - Use This When

Use this pattern when a project must say what kind of thing is under concern before it can discuss parts, boundaries, interactions, roles, work, architecture, or descriptions.

Typical moments:

- a team calls everything a "system" and then tries to ask physical questions about theories, documents, models, or descriptions;
- an episteme is treated as an acting agent that performs work or makes decisions;
- a group, organization, model, document set, machine, neural-network architecture, or research program must be treated as a whole with parts;
- a set of items is expected to act, but no boundary, part-whole relation, or acting system has been named;
- architecture or structure claims need a grounding holon before selected structures can be described.

**First useful move.** Decide whether the subject is only a `U.Entity`, a `U.Holon`, a `U.System` holon, or a `U.Episteme` holon in the current bounded context.

**What goes wrong if missed.** A theory gets ports, a document edits itself, a list becomes an acting organization, and architecture is discussed without naming the holon whose structure is being selected.

**What this buys.** FPF gets one compact root for composition: identity starts at `U.Entity`; part-whole composition starts at `U.Holon`; acting work attaches to `U.System`; claim-bearing knowledge is carried by `U.Episteme` without making it an agent.

**Not this pattern when.**

- If the current question is local vocabulary, role assignment, or meaning inside one semantic frame, use `A.1.1` and the role-governing patterns.
- If the current question is the episteme slot relation, use `C.2.1`.
- If the current question is selected structure over a holon, use `A.22`.
- If the current question is architecture of a holon in context, use `C.30`.
- If the current question is work, method, or role-method-work alignment, use `A.15` and its dependent patterns.

