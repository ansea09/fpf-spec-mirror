---
chunk_kind: "child"
pattern_id: "E.15"
pattern_title: "Pattern Change, Edition Continuity, and Impact Analysis"
section_id: "E.15:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.15/E.15__008_conformance-checklist.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "E.15 — Pattern Change, Edition Continuity, and Impact Analysis"
  - "E.15:7 — Conformance Checklist"
line_start: 113340
line_end: 113354
dependencies:
  - "C.18"
  - "C.19"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.8"
  - "E.9"
  - "F.0.1"
  - "F.1"
  - "F.15"
  - "F.9"
keywords:
---

### E.15:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-E15-1 (Exact change basis).** | A conforming use **MUST** identify the change question, receiving use and predecessor. A claim about the actual difference or continuity **MUST** identify the exact predecessor and candidate editions. A design in development identifies the change sought and which choices remain open. | Makes continuity replayable without a universal context record. |
| **CC-E15-2 (Actual delta first).** | Delta-Class **MUST** follow comparison of actual effects on recognition, inputs, actions, conditions, results, norms, ontology, consumers, and assurance; a label, version number, edit operator, or line count **MUST NOT** decide it. | Prevents small semantic changes and large harmless rewrites from being misclassified. |
| **CC-E15-3 (Proportional route).** | An understood direct repair **MUST NOT** be forced through multiple-candidate generation, aggregate scoring, a SoTA harvest, or a new trace record. Alternative comparison **MUST** be used only when materially plausible alternatives or a consequential current-source choice remain. | Keeps ordinary changes cheap without deleting the stronger branch. |
| **CC-E15-4 (Actual affected reach).** | Identify each in-scope use whose action, interpretation, condition, result, check or public reference depends on the changed premise. For an impact assessment, distinguish a required change awaiting its maintainer from a dependency still unknown. For an implementation claim, establish which affected uses were repaired and verified and what remains unresolved. Mentions and declared links alone do not establish a dependency. | Keeps the claimed repair and the assessment of its reach verifiable. |
| **CC-E15-5 (Independent predecessor preservation).** | A material rewrite **MUST** be checked against an independently derived inventory of predecessor functions and uses. Every intentional change, move, or retirement **MUST** be named by its successor decision; the author’s preservation map alone **MUST NOT** be accepted as proof that the inventory is complete. | Prevents compression or restructuring from silently deleting ideas. |
| **CC-E15-6 (Valid selection).** | Hard constraints **MUST** remain separate from multi-scale qualities. When a candidate is selected, it **MUST** be non-dominated for the stated use and protected trade-offs. A comparison can return several supported alternatives. An undeclared aggregate score **MUST NOT** choose among them. | Makes “better” a replayable use-relative claim. |
| **CC-E15-7 (Record economy and object separation).** | The change account **MUST** reuse the receiving workflow's governed records by reference. A new episteme or publication **MUST NOT** be inferred solely from a form, file, self-log, or the fact that authoring occurred. | Avoids duplicate records and false work evidence. |
| **CC-E15-8 (Proportionate verification).** | Checks **MUST** be selected from the actual change and claimed conclusion. After material formal or ontological repair, the whole changed pattern **MUST** receive a precise-plain-language and practitioner-use read in addition to focused semantic checks. | Prevents locally exact repairs from making the pattern unusable. |
| **CC-E15-9 (Edition continuity).** | Historical editions **MUST** remain recoverable, and only affected premises or consumers **MUST** reopen. Publication, acceptance, registration, and landing **MUST NOT** be inferred from E.15 completion. | Separates semantic continuity from later lifecycle decisions. |
| **CC-E15-10 (Problem-specific SoTA).** | When external or internal SoTA changes the repair, the account **MUST** compare serious current alternatives at comparable application effort and state the adopted, adapted, or rejected contribution at the receiving locus. Source popularity, age, official status, or tool availability **MUST NOT** substitute for that decision. | Keeps research load-bearing and bounded. |

