---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality-Read Question Framing"
section_id: "E.22:5"
section_title: "Archetypal grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__006_archetypal-grounding.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "E.22 — Improvement-Oriented Quality-Read Question Framing"
  - "E.22:5 — Archetypal grounding"
line_start: 68873
line_end: 68890
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:5 - Archetypal grounding

**Show, pattern floor read.** A requester says, "Review this E.21 pattern." The frame is missing. `E.22` defaults to `floorRead`: the reviewer checks whether active E.21 coordinates meet the declared floor and returns blockers or admissible stop. The reviewer is not obligated to propose every plausible edit toward `5`.

**Show, exceptional improvement read.** A requester says, "This pattern already has all active E.21 coordinates at `4`; propose non-dominated edits that could raise each one toward `5` without damaging ordinary use." The frame selects `exceptionalImprovementRead` plus `paretoTradeoffRead`. The reviewer must answer per active coordinate and must name protected trade-offs.

**Show, DRR adequacy read.** A requester says, "Can this DRR carry pattern drafting?" The object-under-improvement evaluation is `E.9.DA`, not `E.21`. If the requester wants maximum DRR strength, the frame must say `exceptionalImprovementRead` over the active `E.9.DA` coordinates. Otherwise the default question is only whether the `DRR` meets the declared drafting floor.

**Show, engineering work-result quality read.** A requester says, "Raise this interface design review toward exceptional." The object version under quality read is the named interface design version. The object-under-improvement evaluation is the declared design-quality characteristic space, `C.25` quality bundle, local rubric, or other exact review profile, not `E.21` unless the object is an FPF pattern. `E.22` asks whether the read is floor-only, exceptional-improvement, trade-off, open-question, absorption, candidate-proposal, or a declared combination.

**Show, architecture-quality read.** A requester says, "Review this architecture description and suggest improvements." The object-under-improvement evaluation must be named: for example an architecture-quality rubric, characteristic space, `C.25` quality bundle, or exact architecture review profile. `E.22` prevents the request from silently mixing a blocker check, exceptional improvement, ATAM-like trade-off discovery, and open-question discovery.

**Show, OEE/NQD read.** A requester asks, "Is this generated set good enough to keep exploring from, and what candidate changes should we consider next?" The frame must first name the object version under quality read: one candidate, `Front`, `Q-Front`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, parity report, refresh report, or declared transduction result. It then names the object-under-improvement evaluation: for example `C.17` for candidate characteristics, `C.18` for archive and front semantics, `C.19` for pool policy, `G.5` for selected-set publication, `G.9` for parity, or `G.11` for refresh. `E.22` frames the read purpose and the candidate improvement proposal rule: expected quality movement, protected trade-off, closure test, and neighbour exit for each proposal row. If the useful result is a bounded proposal portfolio, selection by NQD, front or archive placement, selected-set publication, parity, and refresh remain with the governing patterns. `E.22` does not turn illumination telemetry, a public shortlist, or a proposed candidate change into one scalar quality result.

**Show, absorption read.** An external review returns fifty suggestions. A checklist tracks them one by one, but `E.22` requires one additional quality impact result: which coordinates actually improved, which stayed floor-only, which trade-offs were introduced, and which suggestions were outside the object-under-improvement evaluation.

**Near miss, all-to-five prompt.** "Raise all coordinates to exceptional" is incomplete. It lacks protected trade-offs and an open-question classification rule. The repaired frame asks for non-dominated improvements toward exceptional expression where feasible and rejects edits that damage declared usability, affordability, locality, corpus ecology, neighbour fit, or another active protected quality.

