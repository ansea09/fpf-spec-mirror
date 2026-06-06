---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:13"
section_title: "Anti‑Patterns & Failure Modes (what to avoid)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__014_anti-patterns-failure-modes-what-to-avoid.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:13 — Anti‑Patterns & Failure Modes (what to avoid)"
line_start: 74565
line_end: 74586
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:13 - Anti‑Patterns & Failure Modes (what to avoid)

**13.1 “Global name first.”**
Trying to coin a single global string before local understanding is mature. **Fix:** mint locally, publish MDS, then align.

**13.2 “Synonym storm.”**
Collecting many strings without stabilizing the Concept-ID. **Fix:** one Concept-ID per sense; multiple Working-Names only if they truly help didactics.

**13.3 “Process leakage into names.”**
Burying workflow or tool steps inside the MDS. **Fix:** keep process in method descriptions; keep names about sense, not procedure.

**13.4 “Member‑implies‑part.”**
Letting collection names induce part‑whole claims. **Fix:** separate names, separate MDS; don’t smuggle structure into membership.

**13.5 “Sideways dependency.”**
Defining a name by appealing to another Draft at the same dependency stratum or higher. **Fix:** depend only downward or postpone ratification.

**13.6 “Alias/Plain drift.”**
Letting a Plain label or alias accumulate extra meanings absent in the underlying row. **Fix:** periodic label review; prune metaphors that start bending sense; respect the alias budget.

**13.7 “Atlas label does substrate work.”**
Letting atlas or interpretive-view language quietly replace the base candidate set or family or decide substrate stewardship or publication policy. **Fix:** keep the base palette, front, archive, or shortlist recoverable, use atlas wording only when several declared views or qualifiers are jointly load-bearing for the naming explanation, and move substrate questions and publication questions to the pattern sections that govern those objects.
