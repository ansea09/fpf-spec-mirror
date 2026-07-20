---
chunk_kind: "child"
pattern_id: "A.6.C"
pattern_title: "Contract Unpacking for Boundaries"
section_id: "A.6.C:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.C/A.6.C__001_intro.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.C — Contract Unpacking for Boundaries"
  - "A.6.C:intro — Intro"
line_start: 10167
line_end: 10177
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.8"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "E.10"
  - "E.17"
  - "F.12"
  - "F.18"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "(RFC 2119 + RFC 8174)"
  - "A as predicates (“is admissible iff…”)"
  - "Boundary Norm Square (L/A/D/E)"
  - "MVPK faces “no new semantics”"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SLA/guarantee claim classification"
  - "accountable commitment vs exact permission result"
  - "and E as observable/evidenced properties. If a BCP‑14 keyword or synonym appears in an L/A/E claim"
  - "and OPTIONAL"
  - "as a disciplined modality family"
  - "contract bundle unpacking"
  - "exercise"
  - "finding"
  - "in L/A/E claims"
  - "including common synonyms such as SHALL"
  - "non-violation"
  - "permission projections cite the corresponding D- and exact A.2.8.PER grant"
  - "phrase L as definitions or invariants (“is defined as…”"
  - "promise content ≠ work"
  - "promise-act/utterance separation"
  - "the face is non-conformant until rewritten without the BCP‑14 keyword or moved out of the face"
  - "the sentence MUST be rewritten to remove the keyword or moved out of the face"
  - "“holds iff…”)"
---

## A.6.C — Contract Unpacking for Boundaries

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)
> **Placement:** Part A → **A.6 Signature Stack & Boundary Discipline**
> **Builds on:** A.6 (stack + classification intent), **A.6.B** (L/A/D/E), **A.6.8 (RPR‑SERV)** (service‑cluster polysemy unpacking), **A.7** (EntityOfConcern, Description episteme, and carrier separation), **A.2.3** (`U.PromiseContent`), **A.2.8** (`U.Commitment`), **A.2.8.PER** (strong/weak permission, exercise, and conflict), **A.2.9** (`U.SpeechAct`), **A.15.1** (`U.Work`), **A.10** and **B.3** (evidence and assurance use), E.10 (`L-SERV` and `LEX-BUNDLE`), E.17 (MVPK “no new semantics” faces), F.12 (service acceptance and evidence discipline)
> **Naming boundary:** **F.18** may provide durable names for recovered terms when naming is current; it does not govern the promise-content, speech-act, commitment, permission, work, evidence, or boundary ontology.
> **Mint or reuse (terminology):** Reuses “contract”, “SLA”, and “guarantee” as Plain-level boundary shorthand; mints **Contract Bundle** as an unpacking lens (not a new entity kind), plus optional register columns (`bundleId`, `bundlePart`, and `faceRefs`). **NQD-front seeds (informative):** contract packet, agreement bundle, boundary bundle (chosen: *Contract Bundle* for low collision with existing “bundle” terms).
> **Purpose (one line):** Prevent “contract soup” and agency misattribution by unpacking contract-language into distinct promise-content, utterance package, commitment or permission under separate direct owners, performed work, and carrier-referenced evidence as adjudication basis, then classifying each part into the Boundary Norm Square.

