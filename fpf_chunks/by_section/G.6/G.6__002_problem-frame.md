---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__002_problem-frame.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:1 — Problem Frame"
line_start: 103792
line_end: 103816
dependencies:
  - "A.10"
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

Use this pattern when a later user must cite, replay, audit, or refresh a path through several already established objects and relations rather than repeat their complete source account.

Use it when the working question is:

* which admitted dated Work occurrences and A.13-qualified actual performer Systems must remain addressable, together with already-established F.6 attribution refs only when the selected path expressly consumes precise assignment-bound attribution, and any local system-role kind or assignment identifier that the path separately uses;
* which direct participation or binding facts, produced entities, domain results, result epistemes, outcomes, source publications, carriers, and provenance relations must remain addressable;
* which exact direct relations connect those objects, which pattern defines or constrains each relation, and whether each relation is already established as obtaining;
* which bounded context, reference plane, time window, bridge, edition, policy, source-currentness result, or reliance boundary limits the cited path;
* which downstream work and exact use relation may cite the path; and
* what stronger conclusion, assurance, permission, acceptance, gate passage, or decision the path does not carry.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is an addressable provenance representation: one `EvidenceGraph`, its `PathId` or `PathSliceId`, and any ledger entry that makes the path replayable. G.6 governs path identity, slicing, citation, and local refresh. It does not create the represented work, participation, production, result, episteme, outcome, source, currentness, reliance, or representation correspondence.

**First useful move.** Name the relied-on claim or bounded use, then list the exact object refs and direct relation refs needed to replay it. For every relation record its direct governor and obtaining claim. Only then draw the path. Keep an unresolved relation as a gap; do not turn it into a graph edge asserted as obtaining.

**What goes wrong if missed.** A tidy graph makes an unperformed method look like Work, a co-listed System or entity look like a participant or Work performer, a carrier look like a produced result, a measurement or verdict look like generic evidence, or a provenance edge look like the world-side relation itself.

**What this buys.** Downstream work can cite one stable path while a reviewer can still recover the exact work, participants, products, subject results, result epistemes, sources, direct relations, currentness, and bounded use that the path represents.

**Not this pattern when.** Use `A.2.4` for the first evidence-use or status-use classification, `A.10` for source recovery and bounded reliance, `A.15.1` and `F.6` for performed Work and its attribution, `A.2.1` only when an assignment occurrence itself is current, `A.6.1` for actual operation bindings, `A.15.PROD` when production or inception is current, the exact domain pattern for its local result, `C.2.1` for the result episteme, `G.11` for currentness, `C.29` for representation correspondence, and `B.3` for assurance. If only one local source-to-use statement is needed, stay in A.10.

Here `path` means a path in a descriptive provenance graph. It is not an action route, method, workflow, transformation flow, universal evidence relation, or generic work-result relation.

