---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:13"
section_title: "Acceptance Tests (SCR/RSCR stubs)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__014_acceptance-tests-scr-rscr-stubs.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:13 — Acceptance Tests (SCR/RSCR stubs)"
line_start: 76399
line_end: 76415
dependencies:
  - "A.2.1"
  - "A.4"
  - "A.7"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "U.BoundedContext"
  - "anchor"
  - "context"
  - "domain"
  - "frame"
---

### E.10.D1:13 - Acceptance Tests (SCR/RSCR stubs)

**SCR — Static discipline checks**

* **SCR‑DCTX‑S01.** No occurrence of the token **anchor** in normative sections.
* **SCR‑DCTX‑S02.** All formal uses of “Context” resolve to **`U.BoundedContext`**.
* **SCR‑DCTX‑S03.** Pattern headers contain **Problem Frame** instead of “Context”.
* **SCR‑DCTX‑S04.** All semantic references use the forms in Sec. 5.
* **SCR‑DCTX‑S05.** No “domain context” strings; Domain appears only as family metadata.
* **SCR‑DCTX‑S06.** No is‑a or containment relations between contexts outside **F.9**.

**RSCR — Regression discipline checks**

* **RSCR‑DCTX‑E01.** Adding a new family or edition does not introduce “domain context” or context hierarchies.
* **RSCR‑DCTX‑E02.** Refactors of F.1/F.2/F.7/F.9 do not re‑introduce “anchor”.
* **RSCR‑DCTX‑E03.** Multilingual updates follow D‑CTX‑7 (split/merge rationale recorded informatively).

