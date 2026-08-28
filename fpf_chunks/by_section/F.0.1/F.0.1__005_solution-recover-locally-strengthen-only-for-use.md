---
chunk_kind: "child"
pattern_id: "F.0.1"
pattern_title: "Source-Local Meaning Recovery"
section_id: "F.0.1:4"
section_title: "Solution — recover locally, strengthen only for use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.1/F.0.1__005_solution-recover-locally-strengthen-only-for-use.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.0.1 — Source-Local Meaning Recovery"
  - "F.0.1:4 — Solution — recover locally, strengthen only for use"
line_start: 91062
line_end: 91125
dependencies:
  - "E.10"
  - "E.10.D1"
  - "F.0.2"
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "actual cross-local relation"
  - "exact source and edition"
  - "local expression"
  - "optional durable address"
  - "source-local meaning"
  - "troubling word use"
---

### F.0.1:4 - Solution — recover locally, strengthen only for use

#### F.0.1:4.1 - Recover one source-local meaning

1. **Name the question.** State what answer or action can change if the expression is read differently.
2. **Identify the source.** Give the exact source and edition. A discipline or shelf label is not enough.
3. **Locate the passage.** Point to the claim, definition, example, rule, or other passage used.
4. **State the meaning plainly.** Say what the expression denotes or claims in that passage. Keep designed descriptions and performed occurrences distinct when the source does.
5. **Use the answer and stop.** Do not create a durable cell or relation unless a later receiver needs it.

The source, edition, expression, passage, and plain meaning are the ordinary minimum. A brief scoped heading may keep an already established source in view; repeated source tags are unnecessary when the reading remains unambiguous.

#### F.0.1:4.2 - Add a durable address only when it earns its cost

Create one F.17 `SchemeSenseCell <ReferenceScheme, LocalExpression, LocalSenseClaim>` only when stable reuse, a later claim, a named receiver, or an actual relation to another local sense needs an exact address. The effective ReferenceScheme keeps the source and edition recoverable; the LocalSenseClaim states the meaning rather than hiding it in a label.

State an obtaining `LocalSenseBasisRelation` only when the support relation from an exact basis episteme to that cell is itself current and supported. Identifying a source, stating that support relation, relying on it in a later use, and assuring that reliance are four different claims. Use A.10 and B.3 only for the latter questions.

When a source fixes a designed-versus-performed distinction or another time stance, put it in the local sense claim or its exact basis. Do not make an edition label or separate container stand in for the distinction.

#### F.0.1:4.3 - Relate different local meanings only when the relation is current

A shared label, close paraphrase, common superclass, table row, embedding score, or family membership does not establish identity or another relation. First recover each source-local meaning separately. Then use F.9 when a receiving use needs an actual relation between the two F.17 cells.

The F.9 result states which two cells are related, what kind of relation obtains, how its endpoints are oriented, and what relation profile makes it true. When a receiving use is current, state a separate C.2.1 claim: what action is proposed, in which direction, under which correspondence rule, how much loss it tolerates, and whether the Bridge is suitable for that use. Changing this use claim does not change the Bridge. Neither the relation nor the claim by itself permits translation, substitution, or row membership, establishes reliance or authorization, or shows that the action occurred. A chain of relations does not silently create a direct endpoint relation.

#### F.0.1:4.4 - Recover old Context-shaped artifacts only for a current reliance

An old Context Card or two-part SenseCell remains an historical episteme or representation under its original edition. Do not relabel it as a current F.17 cell.

When a current claim or action actually relies on it, recover only the values that use needs: for example, the exact source and edition, expression, source-local claim, passage, effective scheme, claim scope, or obtaining relation. If a needed value cannot be recovered, return the exact unresolved value and reopen only the dependent claim or action. Mere archival presence does not start a migration.

#### F.0.1:4.5 - Minimal conceptual objects

| Object | What it is | What it is not |
| --- | --- | --- |
| Source-backed meaning statement | A plain answer tied to one exact source passage. | A new kind, container, relation, or assurance result. |
| `SchemeSenseCell` | F.17's durable address for one expression and local sense claim under one effective ReferenceScheme. | The ordinary first result or a container of source doctrine. |
| `LocalSenseBasisRelation` | A current direct support relation from an exact basis episteme to the cell. | Automatic provenance, reliance, or assurance. |
| F.9 Bridge | An actual semantic relation between distinct recovered cells under its applicable relation profile. | A proposed use, a bounded-use claim, permission, reliance, authorization, or evidence that an action occurred. |
| Short source note | An optional readable representation of already recovered source information. | A form whose presence establishes meaning or admission. |

#### F.0.1:4.6 - Invariants

1. Every load-bearing local meaning has a recoverable source, edition, and passage.
2. A plain source-backed statement may be the complete result.
3. A `SchemeSenseCell` is created only for a named durable use and keeps scheme, expression, and claim distinct.
4. A basis relation is stated only when it obtains; reliance and assurance remain separate.
5. Different local meanings remain distinct unless an exact relation between them is established.
6. Designed and performed readings do not become identical through shared wording.
7. A changed edition, passage, or relation reopens only claims and uses that relied on the changed premise.
8. Historical artifacts remain historical; current recovery does not require corpus-wide relabelling.

#### F.0.1:4.7 - Readable reasoning moves

- **Local reading.** “This source passage uses *t* to mean *m*.”
- **Durable address.** “This receiver will reuse that reading, so record it as an F.17 cell under the effective source scheme.”
- **Basis.** “This exact source episteme supports the cell through a current `LocalSenseBasisRelation`.”
- **Cross-source relation.** “The two recovered cells stand in this stated F.9 relation under this relation profile.” When a receiving use is current: “A separate C.2.1 claim says whether that Bridge is suitable for this action, direction, correspondence rule, and tolerated loss.”
- **No transitive shortcut.** Two established relations through an intermediate meaning do not establish a direct third relation.
- **Affected-only reopening.** A changed source premise reopens the claims that used it, not every claim that cites the edition.

These are allowable conceptual moves, not storage fields, APIs, or mandatory workflow records.

