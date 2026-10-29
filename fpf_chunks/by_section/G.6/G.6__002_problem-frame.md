---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__002_problem-frame.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:1 — Problem Frame"
line_start: 129006
line_end: 129021
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.13"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "E.24.PUB"
  - "F.10"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:1 - Problem Frame

Use this pattern when a later user must cite, replay, audit or refresh a chain of established facts, such as a measurement, an acceptance judgement and a decision. Give that chain a stable address while preserving the evidence and rules for its members.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is an addressable provenance representation: one `EvidenceGraph`, its `PathId` or `PathSliceId`, and any ledger entry that makes the path replayable. G.6 governs path identity, slicing, citation and refresh of the representation. The represented facts remain governed by their subject patterns.

**First useful move.** Name the relied-on claim or bounded use, then list the exact object refs and direct relation refs needed to replay it. For every relation record its direct governor and obtaining claim. Only then draw the path. Keep an unresolved relation as a gap; do not turn it into a graph edge asserted as obtaining.

**What goes wrong if missed.** A tidy graph makes an unperformed method look like Work, a co-listed System or entity look like a participant or Work performer, a carrier look like a produced result, a measurement or verdict look like generic evidence, or a provenance edge look like the world-side relation itself.

**What this buys.** A downstream user can cite one path and recover its supporting facts, their qualifications and the direct relations that connect them. A changed premise can be traced to every dependent path within the established coverage.

**Not this pattern when.** If the required fact or relation has not been established, use its subject pattern in §4.1 first. If only one local source-to-use statement is needed, stay in A.10.

Here `path` means a path in a descriptive provenance graph, not an action route.

