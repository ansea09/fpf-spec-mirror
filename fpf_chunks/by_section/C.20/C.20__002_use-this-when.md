---
chunk_kind: "child"
pattern_id: "C.20"
pattern_title: "Composition of U.Discipline (Discipline-CAL)"
section_id: "C.20:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.20/C.20__002_use-this-when.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.20 — Composition of U.Discipline (Discipline-CAL)"
  - "C.20:0 — Use This When"
line_start: 65095
line_end: 65130
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19.CPM"
  - "A.22"
  - "A.3.1"
  - "A.6.REL"
  - "B.1.5"
  - "B.2"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.20"
  - "C.21"
  - "E.24.UK"
  - "F.9"
  - "G.5"
keywords:
---

### C.20:0 - Use This When

Use this pattern to establish what makes an existing field a discipline, to design the connection between knowledge and practice in a proposed field, or to maintain that connection as the field changes. Begin with the work the discipline is meant to sustain. Practitioners may be producing something, investigating a phenomenon, or keeping an activity effective over time. What must they understand to do that work, and how can the results of their work test or improve that understanding?

Typical moments include:

- comparing rival traditions without letting a shared label, Bridge or comparison table merge them;
- reusing a practice across semantic localities while preserving local meanings, direction, tolerated loss and field boundaries;
- testing whether a Method, theory, standard or subdiscipline is a constituent rather than merely used, cited, registered or taught in the field;
- determining continuity while a canon, standard or accepted practice changes, and identifying another whole when the reidentification rule fails;
- using an applied, multidisciplinary or transdisciplinary classification under its stated criterion.

**Primary EntityOfConcern.** One exact `U.Entity` candidate being tested for recognition as `U.Discipline`. The candidate is recoverable before the classification result.

**First useful move.** What does the proposed field enable practitioners to do or explain? Start with a problem the field is meant to address. Trace the knowledge that guides how practitioners address it and the reusable practice through which results can challenge that knowledge. This gives you candidates for both kinds of contribution. A field may also use a result supplied from outside. To distinguish the two, establish which contribution the field's own practice requires or currently realizes as an admitted alternative and how it connects to the others. For recognition of the discipline, test the exact candidate and its independently identified parts under section 4.1. A narrower question about one use can be settled by the grounds for that use.

**What goes wrong if missed.** A field name starts doing the work of a canon, method repertoire, institution, bridge, comparison policy, and maturity score at once. The reader may then treat a card or graph as establishing parts, or treat changes to a journal, standard, method list, or dashboard as establishing a new discipline. Cross-locality reuse can also look valid after local meanings, evidence lanes, or comparison rules have drifted.

**What this buys.** A practitioner can say what the discipline is made of, how the parts form one practice-and-knowledge whole, what remains the same through change, and which surrounding objects are merely used by discipline work. That makes comparison, transport, stewardship, and edition work inspectable without reducing the field to a document list or domain label.

**Not this pattern when.**

- Use domain or catalogue work for a subject-area label.
- Use the effective `ReferenceScheme`, `ClaimScope`, and F.17 local-sense row for one local meaning.
- Use F.9 only when a semantic relation is claimed between two exact F.17 `SchemeSenseCell` values from different semantic contexts and its predicate obtains.
- Use C.2.1 and its publication or source-use patterns for one theory, standard, canon item, or their exact episteme edition.
- Use C.3, C.2.1, and direct historical or provenance relations for a school, variant, lineage, or classification.
- Use A.3.1 and B.1.5 for a Method or composite Method.
- Use A.15.1 for dated Work.
- Use A.22 for a selected relation organization.
- Use A.19.CPM for an actual comparison.
- Use C.21 for field-health characteristics.
- Use E.24.PUB for publication.

Use C.20 when determining, explaining, or relying on whether one exact field-level candidate has the required construction and continuity. The result may be `true`, `false` or `unknown`. Missing constructive facts leave the discipline claim unknown; they do not establish that the candidate is only a collection. Continue with the separately supported objects or collection when those suffice.

