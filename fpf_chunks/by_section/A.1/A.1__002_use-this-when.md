---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Recognize a Whole with Parts (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__002_use-this-when.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "A.1 — Recognize a Whole with Parts (U.Holon and Admitted Holon Kinds)"
  - "A.1:0 — Use This When"
line_start: 2561
line_end: 2599
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

Use this pattern when a decision depends on whether an entity is a whole with parts, an acting System, or a claim-bearing holon.

Typical moments:

- physical or operational abilities are being attributed to a theory or document merely because it is called a system;
- an episteme is treated as an acting agent that decides, performs work, authorizes, promises, or revises itself;
- a proposed whole needs an account of its constituents and construction;
- a collection is expected to act, but no acting system has been constructively recognized;
- architecture or selected-structure claims need the holon whose structure is being selected.

**Primary EntityOfConcern.** A `U.Entity` candidate whose actual construction may or may not satisfy the constructive recognition criterion for an already admitted holon kind.

**Primary working reader.** A practitioner or modeler who must decide whether part-whole, acting-system, or claim-bearing-holon reasoning is admissible for that entity before relying on neighboring work, architecture, evidence, or publication claims.

**First useful move.** Identify the entity and ask which conclusion the receiving work needs. To recognize an existing whole, test its construction under an already admitted public holon kind using §4.2. A necessary condition that fails, or required conditions that cannot hold together, can settle that test. If the decision requires positive recognition and the available grounds leave it open, identify what prevents reliance. `E.24.UK` governs the separate decision to admit a public U-kind.

When the next decision depends on which System acts, is intended to change, carries a capability, persists, or is being considered or designated as the project system-of-interest, use `A.1.SCR` to find that proposed subject. `A.1.SCR` first checks whether a non-system subject already answers the decision; apply the complete A.1 criterion only while the decision still depends on systemhood.

Once the proposed or observed focus is current, use `A.1.CSD` when the next question is which other Systems may undergo relevant changes and omitting one could change a named decision or investigation. That branch discovers candidate bearers and qualified consequence claims; it does not repeat recognition of the focus or settle causality, evaluation, or choice.

Use `A.1.STM` when the project needs a connected account. Start with the use to create, sustain or end and what the recipients must still be able to do. This can identify a system sought for future use before any candidate exists. For an existing product it can identify the functioning, changes and contributions needed to keep it usable or to withdraw it under the agreed conditions. Apply actual-system recognition where a claim relies on an existing holder.


**What goes wrong if missed.** A claim attributes revision Work to a document, gives a theory physical ports, or treats a list as an organization. A lathe that changes a workpiece is treated as its containing whole without an obtaining part-whole relation. An architecture claim lacks the holon whose structure is selected.

**What this buys.** FPF gets one compact part-whole foundation without turning every whole into a physical system: identity starts at `U.Entity`; part-whole treatment starts at `U.Holon`; acting work attaches to `U.System`; claim-bearing knowledge is carried by `U.Episteme`; method holonhood is governed by `U.Method`; other admitted holon kinds keep their own subject patterns.

**Not this pattern when.**

- If the current question is a selected bounded model-use relation organization, use `A.1.1`.
- If the current question is episteme identity, constitution, or neighboring-relation discipline, use `C.2.1`.
- If the current question is relation vocabulary or component, portion, aspect, and phase discipline, use `A.14`.
- If the current question is constructive part-whole grounding, use `C.13`; use `B.3.5` for Working-Model assurance grounding.
- If the current question is selected structure over a holon, use `A.22`.
- If the current question is architecture of a holon, use `C.30`.
- If the current question is transformation, method, system-role kind or assignment, work, capability, or functioning, use the subject pattern before relying on A.1.

