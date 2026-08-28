---
chunk_kind: "child"
pattern_id: "F.19"
pattern_title: "Ontology-First Plain Technical Rewriting"
section_id: "F.19:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/F.19/F.19__013_sota-echoing.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "F.19 — Ontology-First Plain Technical Rewriting"
  - "F.19:11 — SoTA-Echoing"
line_start: 98911
line_end: 98923
dependencies:
  - "A.19.SPR"
  - "A.6.P"
  - "A.7"
  - "C.16.P"
  - "C.2.P"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "F.18"
  - "I.2"
keywords:
---

### F.19:11 - SoTA-Echoing

`SoTA` here means the best current contribution to the stated practice question, not the newest or most formal publication. The comparison below is current to 2026-08-19; a source's official status does not by itself make it SoTA.

| Practice question | Exact source and status | Selected payload and limit | Source-use decision, receiving locus, qualification, and reopen |
|---|---|---|---|
| How should ordinary technical prose help its intended reader act without being "dumbed down"? | ISO 24495-1:2023, *Plain language — Part 1: Governing principles and guidelines*, current published foundation (`https://www.iso.org/standard/78907.html`); Digital.gov, *Principles of plain language* and *Writing for understanding*, current living US-government practice guide (`https://digital.gov/guides/plain-language/principles`, `https://digital.gov/guides/plain-language/writing`), checked 2026-08-19. | Declare the reader and task; put the usable object and action first; organize for finding, understanding, and use; keep terms the intended reader needs. Neither source defines FPF ontology or requires expert prose to use general-public vocabulary. | **Adapt — reason:** these moves improve F.19's ordinary path without changing its semantic boundary. **Receiving loci:** F.19:0 first useful move; F.19:4 steps 1 and 5; `CC-F19-9` and `CC-F19-12`. **Qualification/currentness:** current standard and current practice guide, not FPF semantic authority. **Reopen:** a new edition changes a used principle, or cold-reader evidence shows that these moves no longer support the declared use. |
| How should plain prose address readers outside the author's specialty while retaining scientific content? | ISO 24495-3:2026, *Plain language — Part 3: Science writing*, Edition 1, current published standard (`https://www.iso.org/standard/86938.html`). | It extends the reader-sensitive principles of Part 1 to science writing for people with different backgrounds and interests. It expressly does not govern specialist scientific writing, and it supplies no test for FPF kinds or terms. | **Adapt — reason:** the cross-specialty reader boundary sharpens the cold-reader check without authorizing loss of technical content. **Receiving loci:** F.19:4 step 5 and `CC-F19-12`. **Qualification/currentness:** current for plain science communication, not proof that a specialist FPF distinction is dispensable. **Reopen:** the standard changes materially, or an F.19 case needs a different expert-to-expert boundary. |
| When is controlled technical language worth its added restriction and maintenance cost? | ASD-STE100, *Simplified Technical English: Standard for Technical Documentation*, Issue 9 (2025-01-15), current issue (`https://www.asd-ste100.org/`). | Its controlled vocabulary and writing rules reduce lexical and syntactic ambiguity in multilingual, safety-sensitive maintenance documentation. That setting does not show that a controlled dictionary, one-word/one-meaning rule, or compliance apparatus improves ordinary FPF prose. | **Reject as the default FPF language; adapt only as a comparison probe — reason:** F.19's cheap ordinary path remains better unless a declared high-risk multilingual use shows otherwise at comparable effort. **Receiving loci:** F.19:4 step 5 and `CC-F19-9`/`CC-F19-12`; no controlled-language machinery is imported. **Qualification/currentness:** current controlled-language practice with an aerospace-maintenance origin. **Reopen:** an F.19 case demonstrates that bounded restrictions outperform the ordinary path for its declared reader and risk. |
| What action-guiding detail must survive when the prose tells someone what to do? | IEC/IEEE 82079-1:2019, *Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements*, Edition 2, published and marked for revision (`https://www.iso.org/standard/71620.html`). | It distinguishes step-by-step instructions within information for use and treats usable instructions as purpose- and user-sensitive. Its full information-management process, competency scheme, and evaluation apparatus are much broader than a bounded F.19 rewrite. | **Adapt the action-preservation branch; reject the surrounding documentation process — reason:** sequence, condition, quantity, warning, and stop detail improve the worked case and checks, while the larger apparatus does not improve them at comparable effort. **Receiving loci:** F.19:4 step 5, `ActionGuidingClaimDetails`, the operational-detail case, and `CC-F19-9`/`CC-F19-10`/`CC-F19-14`. **Qualification/currentness:** current published product-information reference, already marked for revision. **Reopen:** its successor changes a used principle, or an F.19 case requires a further action detail. |
| Can legally constrained prose become clearer without losing controlled terms or obligations? | ISO 24495-2:2025, *Plain language — Part 2: Legal communication*, current published standard (`https://www.iso.org/standard/85774.html`); US SEC, *A Plain English Handbook: How to Create Clear SEC Disclosure Documents* (1998; SEC page 1999), retained lineage (`https://www.sec.gov/about/reports-publications/newsextrahandbook`). | The current standard shows that reader access can coexist with nuanced concepts, required structures, rights, and obligations. The SEC handbook is lineage for concrete, direct presentation. Neither source makes legal drafting or disclosure compliance part of ordinary FPF authoring. | **Adapt the meaning-preservation lesson; reject legal-process transfer — reason:** the branch supports necessary terms without importing a legal-document method. **Receiving loci:** F.19:4 step 5 and the plain-language-drift and synonym-churn boundaries. **Qualification/currentness:** ISO 24495-2 is current legal-communication guidance; the SEC handbook is lineage only. **Reopen:** F.19 acquires a legal-use case, or a later source changes the retained lesson. |
| What prevents a plain rewrite from changing an FPF claim while removing apparatus? | Current FPF patterns `E.8`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, `A.6.P`, and `E.21`, internal governing dependencies. | They recover the actual word, head, role- or function-shaped claim, relation, name, use, and quality loss before the sentence is shortened. They are not external evidence that F.19 is SoTA. | **Adopt as internal dependencies — reason:** they define, constrain, or test the meaning that F.19 must preserve. **Receiving loci:** F.19:4 steps 2–5, the result form, conformance checks, and Relations. **Qualification/currentness:** current FPF dependencies, kept thin rather than copied here. **Reopen:** a dependency changes a distinction or check used by F.19. |

