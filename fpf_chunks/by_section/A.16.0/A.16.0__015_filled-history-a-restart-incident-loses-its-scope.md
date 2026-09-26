---
chunk_kind: "child"
pattern_id: "A.16.0"
pattern_title: "Keep an Episteme's Language-State and Publication History Recoverable"
section_id: "A.16.0:14"
section_title: "Filled history: a restart incident loses its scope"
source_path: "FPF-Spec.md"
output_path: "by_section/A.16.0/A.16.0__015_filled-history-a-restart-incident-loses-its-scope.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "A.16.0 — Keep an Episteme's Language-State and Publication History Recoverable"
  - "A.16.0:14 — Filled history: a restart incident loses its scope"
line_start: 30853
line_end: 30868
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

### A.16.0:14 - Filled history: a restart incident loses its scope

This constructed incident concerns `CheckoutSystem-17`. All three notes below use `Incident17Scheme`, which fixes the System name, trace identifiers and time interpretation. History account H17 has source episteme S0 as its EntityOfConcern; the notes it describes have the checkout System as theirs.

The local incident-edition rule permits a note to continue S0 only if it actually uses S0, retains that System and scheme, preserves the reported observation window and observations, and explicitly marks any changed diagnosis or next question. It allows a diagnosis to be withdrawn or a question added; a scope-dropping summary fails the continuation condition. This is the applicable C.2.1 rule for this example, not a rule inferred from the filenames.

| Entry and source use | Content and position needed here | History result and receiving action |
|---|---|---|
| S0, the initial incident note, grounded in trace T17 | Three timeouts occurred during 09:00–09:02 after restart; the 09:04 request succeeded. Cold-cache startup and database-pool startup remain rival explanations. The named observations and rivals support `ValueSet(AE)={AE2}` and `ValueSet(CD)={CD2}` using the C.2.4/.5 starter anchors. | Preserve the time window, later success and both rivals for the diagnostic question. The note establishes no permanent capacity shortage. |
| S1, a briefing composed from S0 | “Checkout is permanently undersized; add replicas.” The explicit claim/action supports AE3; the selected capacity route is CD3. It omits both the restart window and the later success, and drops the rival explanations. | S1 has changed claim content and fails the stated edition-continuity rule. Record that failed continuation claim rather than silently linking it as the next valid edition. Its polish and closure establish no stronger warrant. |
| S2, a corrected note composed directly from S0 after S1's loss is found | Retains both observations and rivals; adds “Which explanation accounts for the restart-only timeouts, and what observation would distinguish them?” It withdraws the permanent-shortage conclusion. Its explicit diagnostic structure gives `ValueSet(AE)={AE3}`; restored rivals give `ValueSet(CD)={CD2}`. | C.2.1 continuation from S0 to S2 obtains: distinct content, actual source use, same System/scheme, retained observations and an explicitly changed question satisfy the stated rule. Do not infer continuation from S1. |

The A.16 `reopen` guard is met for the earlier capacity-route commitment: recovering S0 reveals the lost scope and unsupported elimination of rivals. The local next-use rule requires at least AE2, both named rivals and the observation window to be recoverable; it permits a return to B.5.2.0's diagnostic-question entry, not authorization to add replicas. S2 meets that guard. The receiving practitioner can now frame the discriminating inquiry while withholding the permanent-capacity conclusion. Any additional measurement is prospective Work under its own rule.

This short history is needed because the loss occurred between notes and changes how the later action proposal may be used. If the same facts and return were already recoverable in one adequate local move note, §4.3 would stop there. No successor publication, fork, responsibility transfer or history-of-H17 is required for this result.

