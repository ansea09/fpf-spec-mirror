---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__002_use-this-when.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:0 — Use This When"
line_start: 1547
line_end: 1580
dependencies:
  - "A.1.1"
  - "A.1.STM"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.3.4"
  - "A.6.1"
  - "B.2"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24.UK"
  - "G.11"
keywords:
---

### A.1:0 - Use This When

Use this pattern when a project must say what kind of thing is under concern before it can rely on parts, wholes, boundaries, acting systems, roles, methods, work, architecture, or descriptions.

Typical moments:

- a team calls everything a "system" and then asks physical or operational questions about theories, documents, models, dashboards, or descriptions;
- an episteme is treated as an acting agent that decides, performs work, authorizes, promises, or revises itself;
- a product, organization, machine, document family, research program, discipline, work occurrence, or model family must be treated as a whole with parts;
- a list, batch, fleet, pool, clientele, community, or supplier base is expected to act, but no acting system has been constructively recognized;
- architecture or selected-structure claims need the holon whose structure is being selected.

**Primary EntityOfConcern.** One exact `U.Entity` candidate whose actual construction may or may not satisfy the constructive recognition criterion for one already admitted holon kind.

**Primary working reader.** A practitioner or modeler who must decide whether part-whole, acting-system, or claim-bearing-holon reasoning is admissible for the exact entity under concern before relying on neighboring work, architecture, evidence, or publication claims.

**First useful move.** Name the exact `U.Entity` under concern. Then test whether its actual construction satisfies the A.1 holon-recognition criterion under an already admitted public holon kind. The kind is already admitted in the current FPF; `E.24.UK` governs the separate one-time decision to admit public U-kinds. The A.1 candidate test does not repeat that ontology decision.

When the next engineering decision depends on which exact system acts, is intended to change, carries a capability, persists, or is being considered or designated as the project system-of-interest, use `A.1.SCR` to find that proposed subject. `A.1.SCR` first checks whether a non-system subject already answers the decision; the practitioner applies the complete A.1 criterion only while the decision still depends on systemhood. After recognition, use `A.1.STM` only when the remaining problem is loss of the long dependency from project use through architecture, Work, change, and recursive builders; otherwise apply the rule that defines or tests the next claim.

**What goes wrong if missed.** A document edits itself, a theory gets ports, a list becomes an organization, a lathe that changes a workpiece is treated as its containing whole without an obtaining part-whole relation, and architecture is discussed without naming the holon whose structure is selected.

**What this buys.** FPF gets one compact part-whole foundation without turning every whole into a physical system: identity starts at `U.Entity`; part-whole treatment starts at `U.Holon`; acting work attaches to `U.System`; claim-bearing knowledge is carried by `U.Episteme`; method holonhood is governed by `U.Method`; other admitted holon kinds keep their own subject patterns.

**Not this pattern when.**

- If the current question is a selected bounded model-use relation organization, use `A.1.1`.
- If the current question is episteme identity, constitution, or neighboring-relation discipline, use `C.2.1`.
- If the current question is relation vocabulary or component, portion, aspect, and phase discipline, use `A.14`.
- If the current question is constructive part-whole grounding, use `C.13`; use `B.3.5` for Working-Model assurance grounding.
- If the current question is selected structure over a holon, use `A.22`.
- If the current question is architecture of a holon, use `C.30`.
- If the current question is transformation, method, system-role kind or assignment, work, capability, or functioning, use the subject pattern before relying on A.1.

