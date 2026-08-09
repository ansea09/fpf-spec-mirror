---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__005_solution.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:4 — Solution"
line_start: 70271
line_end: 70309
dependencies:
  - "A.6.RCD"
  - "A.6.REL"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:4 - Solution

#### E.4.PFAD:4.1 - Decide whether the architecture question is open

Ask whether choosing a framework, a thinner route, or stop will settle at least one boundary used by later authoring or review:

- a governed or intended framework edition;
- an FPF Core or other current dependency;
- initial pattern placement or a relation among those patterns that changes the architecture; or
- a publication or access consequence.

If no such boundary and receiving use are present, close the exploratory use without `E.4.PFAD` or an `E.9` DRR. If they are present, record whichever answer is selected—including access-only or stop—in one `E.9` DRR. The cheap exit and the architecture decision are alternative entry outcomes, not serial stages.

#### E.4.PFAD:4.2 - State the compact framework answer

The framework-specific part of the DRR states:

1. the intended reader, recurring problem, and bounded architecture question;
2. the selected outcome: a new or revised framework edition, a thinner publication or access route, or no new framework now;
3. the governed edition, the intended-edition boundary before realization, or that no new edition is governed;
4. the selected FPF Core dependency and only the other edition dependencies current for this answer;
5. the first patterns, their placement, and only the relation choices among them that change the selected architecture;
6. the publication or access consequence; and
7. material alternatives, accepted costs or losses, practical consequences, the first authoring action or stop, and the reopen condition.

Keep the ordinary `E.9` grounds, sources, affected loci, rationale, and consequences in the same DRR. Add source-return, naming, quality, admission, currentness, or package details only when they change this answer or a named later use requires them. Use the pattern that defines, constrains, or tests each added claim; do not make it a standing PFAD field.

#### E.4.PFAD:4.3 - State initial pattern relations directly

When an initial pattern relation changes the selected architecture, state the relation and its participants as an ordinary assertion. For example: `Pattern A frames the recurring problem; Patterns B and C specialize its reusable move for two stated situations.` Use the pattern that defines or constrains each relation function.

An optional `E.4.PFR` row may later represent these assertions for maintenance. The row neither makes the relations obtain nor becomes mandatory for the architecture answer. A generic relation catalogue is not a prerequisite for the decision.

#### E.4.PFAD:4.4 - Keep the answer, DRR, authoring, and publication distinct

The `E.9` DRR records the selected answer and rationale. A separately governed decision accepts, redirects, rejects, or reopens that answer. Later authoring realizes an accepted answer. A framework edition is the resulting maintained pattern framework, not the DRR or the authoring work. An ADR-like document, site, PDF, or other carrier publishes or projects claims about these objects; its form does not create the answer, acceptance, authoring, edition, or pattern relations.

Use `C.32.PAD` only when the question is an exact project architecture decision about a named composite project Work, and use `C.32.ADR` only to project that project decision. For an ordinary framework answer, publish the selected decision episteme or a reader-specific projection through `E.17` and `E.24.PUB`. None of these is a mandatory stage of principle-framework authoring.

