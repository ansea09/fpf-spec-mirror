---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__002_problem-frame.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:1 — Problem Frame"
line_start: 81720
line_end: 81741
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.21"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "E.18"
  - "E.18.2"
  - "E.24"
  - "E.5.2"
  - "F.10"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:1 - Problem Frame

Use this pattern when a claim, admission result, assurance result, selector result, maturity transition, benchmark result, or refresh decision needs a citable evidence-provenance path rather than a local evidence-use statement.

Use it when the working question is:

* which evidence-use relations, source records, work occurrences, method descriptions, proof checks, measurements, status-use relations, or causal-use references make the claim traceable;
* that the evidence relation is a graph path in a declared provenance graph, while actual work and transformation-flow claims remain governed by `A.15.1` and `E.18`;
* which time window, bounded context, reference plane, bridge, edition, policy, or source-currentness relation changes the admissible use;
* which downstream selector record, assurance record, release package, benchmark record, audit record, or refresh record may cite the evidence path without copying the whole evidence table;
* what stronger downstream use is not carried by the evidence path and which direct pattern governs that use.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is addressable evidence provenance: an `EvidenceGraph`, its graph-path addresses `PathId` and `PathSliceId`, and the provenance ledger entries that make those paths replayable. The pattern governs addressable provenance. It does not create `U.EvidenceRole`, does not make an episteme hold a work-facing role, and does not replace `A.10`, `A.2.4`, `B.3`, `C.28`, or `F.10`.

**First useful move.** Write the smallest `PathCitationRecord`: claim or use, `EvidenceGraphRef`, graph path, bounded context, downstream citation use or evidence-use relation, time window, source or provenance constraints, bridge or edition refs when current, and `NotCarried`.

**What goes wrong if missed.** Evidence is summarized as a story, badge, confidence phrase, benchmark score, proof label, or dashboard tile; downstream users cannot find which sources and checks carried the claim; context crossings are hidden; refresh becomes a global rerun instead of a local path update.

**What this buys.** A selector, auditor, assurance user, benchmark consumer, or refresh process can cite one stable path and later replay exactly the sources, relations, windows, and constraints that made the claim admissible.

**Not this pattern when.** If only one episteme is being used as evidence or status before a full path is needed, use `A.2.4`. If the current question is ordinary evidence relation and source-currentness without Part-G path addressing, use `A.10`. If the claim is assurance, use `B.3`. If the claim is causal use, use `C.28`. If the question is status-family mapping, use `F.10`. If the question is publication, view, source-use, explanation-use, or specification-use, use `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, or `E.10.D2`. If the question is performed work, use `A.15.1`.

