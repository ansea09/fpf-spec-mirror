---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:13"
section_title: "Author’s pocket guide (carry‑in‑mind rules)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__014_author-s-pocket-guide-carry-in-mind-rules.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:13 — Author’s pocket guide (carry‑in‑mind rules)"
line_start: 56900
line_end: 56914
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

### E.10.D2:13 - Author’s pocket guide (carry‑in‑mind rules)

> **Use these as thinking cues, not as paperwork.** Each cue is a one‑breath test you can apply while writing.

1. **Name the Context.** Write “*Role (ITIL4)*”, “*Method (Essence‑language)*”, “*Execution (PROV)*”. Never speak global words.
2. **Pick the described entity and lane.** Am I talking about an **intension** (Role/Method/Service), a **Description/Spec**, an **Evaluation**, or a **Carrier**? Keep one described entity and one lane per sentence.
3. **Prefer –Description.** Use **`…Description`** by default. Switch to **`…Spec`** only after the **Spec‑gate** (testable invariants + harness + F‑mode).
4. **Characterised by…** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, never *“Role **contains** its states”*.
5. **Window every verdict.** An Evaluation must read “*X ∈ State\@context **in** W*”. No naked, timeless verdicts.
6. **Status ≠ state.** Role **states** live in `U.RSG`; Evidence/Requirement **statuses** classify **knowledge units**. Do not mix.
7. **Bridge later.** If two Contexts “feel the same”, write the itch down and leave it for **F.9 Bridge**.
8. **Two registers.** Every Description/Spec has **Tech** and **Plain** labels; prefer the shortest tech term that matches the invariants.
9. **Carrier humility.** Files and records are **Carriers** of Descriptions/Specs; they don’t *equal* the thing you reason about.
10. **Spec = test.** If you can’t point to a harness that would falsify it, it isn’t a **Spec** yet.

