---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__002_use-this-when.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:0 — Use This When"
line_start: 1329
line_end: 1356
dependencies:
  - "A.1.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.UK"
keywords:
---

### A.1:0 - Use This When

Use this pattern when a project must say what kind of thing is under concern before it can rely on parts, wholes, boundaries, acting systems, roles, methods, work, architecture, or descriptions.

Typical moments:

- a team calls everything a "system" and then asks physical or operational questions about theories, documents, models, dashboards, or descriptions;
- an episteme is treated as an acting agent that decides, performs work, authorizes, promises, or revises itself;
- a product, organization, machine, document family, research program, bounded context, discipline, work occurrence, or model family must be treated as a whole with parts;
- a list, batch, fleet, pool, clientele, community, or supplier base is expected to act, but no acting system has been admitted;
- architecture or selected-structure claims need the holon whose structure is being selected.

**First useful move.** Name the `U.Entity` under concern. Then decide whether the current claim also admits it as `U.Holon`, and whether a direct governing pattern admits a more specific holon kind such as `U.System`, `U.Episteme`, `U.Method`, `U.Work`, `U.BoundedContext`, or `U.Discipline`.

**What goes wrong if missed.** A document edits itself, a theory gets ports, a list becomes an organization, a lathe becomes the super-holon of the workpiece it changes, and architecture is discussed without naming the holon whose structure is selected.

**What this buys.** FPF gets one compact part-whole foundation without turning every whole into a physical system: identity starts at `U.Entity`; part-whole treatment starts at `U.Holon`; acting work attaches to `U.System`; claim-bearing knowledge is carried by `U.Episteme`; method holonhood is governed by `U.Method`; other admitted holon kinds keep their own governing patterns.

**Not this pattern when.**

- If the current question is local vocabulary, local invariant, role taxonomy, or meaning inside one semantic frame, use `A.1.1`.
- If the current question is episteme slot discipline, use `C.2.1`.
- If the current question is relation vocabulary or component, portion, aspect, and phase discipline, use `A.14`.
- If the current question is constructive part-whole grounding, use `C.13`; use `B.3.5` for Working-Model assurance grounding.
- If the current question is selected structure over a holon, use `A.22`.
- If the current question is architecture of a holon in context, use `C.30`.
- If the current question is transformation, method, role, work, capability, or functioning, use the direct governing pattern before relying on A.1.

