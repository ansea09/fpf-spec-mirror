---
chunk_kind: "child"
pattern_id: "A.16.0"
pattern_title: "Keep an Episteme's Language-State and Publication History Recoverable"
section_id: "A.16.0:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.0/A.16.0__012_sota-echoing.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.16.0 — Keep an Episteme's Language-State and Publication History Recoverable"
  - "A.16.0:11 — SoTA-Echoing"
line_start: 30811
line_end: 30824
dependencies:
  - "A.16"
  - "A.16.1"
  - "A.16.2"
  - "A.19"
  - "A.6.A"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.LS"
  - "E.10.MOVE"
  - "E.17"
  - "E.17.1"
  - "E.24.PUB"
  - "F.9"
  - "F.9.1"
keywords:
  - "LanguageStateMoveTrajectory"
  - "branch"
  - "history account"
  - "loss"
  - "next use"
  - "publication form"
  - "source edition"
---

### A.16.0:11 - SoTA-Echoing

**Practice question.** What is the lightest history that lets a later reader recover which note supplied a claim, what changed or was lost, and how that affects the next use?

The selected line retains only the source and loss relations needed by that question. [W3C PROV-DM, Recommendation of 30 April 2013, §§2.2.1.2 and 5.2.1–5.2.2](https://www.w3.org/TR/2013/REC-prov-dm-20130430/), supplies the substantive provenance distinction: derivation connects an output to what it used, can be expanded when activity details matter, and is broader than revision. **Adapt** that selective detail in §§4.0a and 4.3. A PROV derivation or revision assertion supplies no automatic C.2.1 edition relation, truth warrant or language-state position; those claims still need their own facts and rules.

The serious alternative is ordinary version history with relevant diffs and change notes. *Pro Git*, second edition, [§2.3, Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History), supplies a concrete implementation: patches expose textual changes and a graph exposes repository branches and merges. This is often sufficient and should be reused. Its limit for the present question is that a file parent or deletion does not by itself say which source claim was used, whether episteme continuity holds, or which omitted condition changes reliance.

For the same three notes in §14, both approaches can expose the missing restart window. The targeted history also makes two needed judgments explicit: S1 used S0 but failed the stated continuation rule; S2 returns directly to S0 and restores the observations and rivals needed by the diagnostic question. This requires no new incident observations. Its cost is a short semantic annotation after the same content comparison; its gain is that the next reader need not reconstruct why the capacity conclusion was withdrawn. **Reject** deriving those judgments solely from chronological adjacency or repository ancestry. When the existing change note already supplies them, §4.3 stops without another account.

The loss annotation has a separate practice basis. The *Site Reliability Workbook* (2018), [chapter 10, “Missing context” and “Key details omitted”](https://sre.google/workbook/postmortem-culture/), contrasts an inadequate incident account with one that retains the context and facts needed for learning and action. **Adopt** that action-changing-detail criterion in §4.3 and §14's restart-window loss. This is failure evidence for an unqualified summary, not a requirement to write a full postmortem or a source for FPF lineage identity. The selected history preserves an unresolved diagnostic question; it need not manufacture a settled cause or corrective action.

Reopen the choice of account when the receiving question needs an unrecorded branch, source use, lost condition or authority fact. If an existing note or diff annotation now makes all those facts recoverable, reuse it. If automated interchange becomes the actual need, compare an adequate structured provenance representation with this small human-readable account; prose alone may then cease to suffice.

