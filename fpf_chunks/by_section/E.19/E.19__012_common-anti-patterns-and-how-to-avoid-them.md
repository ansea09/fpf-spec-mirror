---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review & Refresh Profiles"
section_id: "E.19:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.19 — Pattern Quality Gates: Review & Refresh Profiles"
  - "E.19:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 59769
line_end: 59796
dependencies:
  - "A.6.P"
  - "E.10"
  - "E.10.SEMIO"
  - "E.8"
  - "E.9"
  - "F.18"
keywords:
  - "(see H-8)"
  - "MUST NOT modify modeled‑world entities (e.g"
  - "and (if needed) reference them from CC items"
  - "inside the predicate)"
  - "where a non-deontic Invariant: predicate is required)"
  - "“Earth”"
  - "“RoleAssignment”"
  - "“Role”"
  - "“holon”) — express those as Invariant: / Well‑formedness constraint: predicates instead"
---

### E.19:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------- |
| **Governed-object drift** | The draft appears to govern one thing in the opening, another in the declaration block, and a third in the examples or neighbouring-pattern or support-companion guidance. | Review cannot tell whether the pattern governs a `PublicationUnit`, a reading move, a work-result record, or a whole process, so later naming and boundary decisions become unstable. | Stabilise one governed object early, keep its head kind explicit, and mark note, sheet, UI, rendering, or process labels as either examples of that object or separate neighbouring entities rather than stylistic substitutes. |
| **Role-clean but pragmatically foggy** | The draft is addressed to the right reader in principle, but cold working readers still cannot recognise the situation, practical payoff, governed object, or first useful move early enough. | The run passes role hygiene while still failing pragmatic fit and first-minute usability. | Pull a recognisable working situation upward, add one minimally viable worked case, make the practical payoff explicit in nearby user-facing prose, expose the governed object and any minimal modeling lens in plain terms, add plain glosses for early claim-bearing terms, and require `SoTA-Echoing` rows that carry live claim force or explanatory work to name the practitioner or manager implication plus the case they discipline. |
| **Architecture-clean but domain-thin** | The text is internally well placed in the package, but the governed object, narrowed branch, or practical payoff are justified mainly through package architecture while the problem-owning domain, practice, or SoTA appears late or decoratively. | The pattern passes internal architecture checks while drifting away from the domain whose work it claims to improve. | Pull the problem-owning domain moment into the recognition text, make the narrowed branch and governed object answerable to the relevant domain or practice, and require load-bearing `SoTA-Echoing` to discipline the practical cases rather than merely bless them after the fact. |
| **Type-correct but inert semio cleanup** | An `E.10.SEMIO` pass removes the overread and restores kind language, but the recognition text no longer tells the reader why the distinction matters, what move remains, where the live claim moved, or how a Plain recognition line maps back to the recovered Tech reading when both registers are live. | The review accepts typed wording while losing action guidance. | Return the draft to same-boundary repair: restore a remaining admissible reader move, name the neighboring FPF handoff, repair the Tech-to-Plain mapping, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete. |
| **Expressive overread rebound after semio cleanup** | The pass makes the text more engaging after cleanup, but the added Plain or didactic force carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load not recoverable from the Tech reading or named handoff. | The review mistakes readability for recovered semantic force. | Rewrite the expressive line as ordinary recognition aid, recover its load through the Tech fields under `E.10:6.2`, name the neighboring FPF handoff that carries the live claim, or demote the phrase to reduced-use cue, quote-only wording, blocked transfer, or rewrite incomplete. |
| **Verdict-only review** | The run ends with “pass/fail” and prose complaints, but no precise findings-first repair direction. | Raises editorial cost; reduces repeatability. | Require one findings-first run record plus concrete remediation direction; do not rely on direct patch text as the primary review output. |
| **Single giant checklist** | Review becomes a long, unfocused ritual that few complete. | Increases cost; reduces fit and rigor in practice. | Use a minimal baseline plus triggered profiles. |
| **Template-only compliance** | All headings exist, but obligations are vague and untestable. | Looks uniform; fails enforceability and auditability. | Enforce normative clause hygiene and CC/Solution coherence. |
| **SoTA name-dropping** | SoTA-Echoing is a list of buzzwords with no stance. | Breaks evidence lineage; invites monoculture. | Require adopt/adapt/reject with reasons per item. |
| **Terminology drift by “synonym”** | Authors swap kernel terms for nicer-sounding words. | Increases ambiguity; harms cross-pattern composability. | Apply PCP-TERM and require explicit mini-definitions on first use. |
| **Form-only review** | Review time goes to formatting and micro-edits while the normative content, terms, Bridges, modularity, slot discipline and SoTA stance are barely checked. | Raises editorial cost without raising semantic trust. | Use the triage rule: treat load-bearing sections as depth targets and keep mechanical cleanup subordinate to semantic correction. |
| **Checklist-clean but content-wrong** | The named profiles, lexical checks, and conformance rows are marked complete, but the repaired text no longer solves the stated problem, sends a live claim to the wrong locus, creates shadow authority, loses a support relation, or adds needless apparatus. | Review accepts a locally tidy pattern while weakening the actual `FPF` guidance. | Apply substantive solution and locus adequacy: name local content questions, check the actual problem and neighboring loci, ask what became worse, and widen the declared boundary by value when the fix belongs outside the first target. |
| **Architecturally right, didactically thin** | The family is admissible, but readers still need project notes to understand what the pattern really governs. | Trust in the monolith depends on external context rather than the pattern text. | Add the missing problem frame, worked slices, local definitions, and exact neighboring-pattern or exact project-side FPF kind and reference guidance before admission. |
| **Scenario-name grounding** | Grounding names a situation but does not show what the source and resulting publication actually look like. | Readers cannot tell why the case stays in the family or where it leaves the family. | Add concrete source and resulting-publication slices, especially for transform families and easy boundary confusions. |
| **Generic-head underspecification** | A load-bearing phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the run leaves that head uninterpreted. | Review discusses the sentence before the object kind is even stable. | Restore the head kind first in pattern-local terms before accepting or comparing the sentence. |
| **Qualifier-smuggled semantic load** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the run treats the phrase as already precise. | The review blesses apparent precision without recovering the actual semantic load. | Unpack the qualifier into explicit semantic load, comparison basis, or downstream-use boundary before acceptance. |
| **Mixed comparison basis** | One sentence compares or ranks publication-form, carrier, process, authority-reference, or project-record values on one comparison basis. | The sentence remains ontologically incoherent even after local wording is polished. | Restore head kind, then qualifier semantic load, then rewrite the comparison through a homogeneous semantic-load, threshold, or named receiving-pattern/source-relation basis. |
| **Sentence-level shorthand drift** | A few innocent-looking words (“species”, “branch”, “flow”, “input/output”) quietly carry the semantic load. | Review passes while key relations remain implicit or wrong. | Inspect load-bearing sentences one by one and replace shorthand with explicit governing-pattern relations and package relations or publication language. |
| **Package-form, governing-pattern relation, and package-relation drift** | The text slides between `family`, `bundle`, `cluster`, `profile`, `overlay`, `suite`, `kit`, or `record` without showing that the ontology changed. | Reviews miss governing-pattern or authority-reference blur because each local sentence still sounds plausible. | Require one intended role word, check governing-pattern relation and package relation explicitly, and treat stylistic noun-swapping as a semantic defect. |
| **Reader-role leakage** | Live sections explain why the pattern was isolated, what landing form is safest, or why merge/freeze is premature. | Review accepts a package memo disguised as a user pattern. | Move package-development reasoning to companions; rewrite live sections in terms of what the user may do, must avoid, and which exact neighboring FPF pattern or named project-side FPF kind and reference governs the release, policy, assurance, gate, action-selection, or adjudication case. |
| **Support object by inertia** | A companion note, profile, check sheet, support row, or review harness remains attached to a pattern family after the pattern body already carries the usable guidance, but the text does not say what real breakage returns if that support object is absent. | Support material becomes permanent local folklore, hidden authority, or reader cost without a corresponding use gain. | State the support question, governing source, support-only use, real breakage if absent, and demotion or deletion condition; otherwise fold the useful example into the pattern or demote the object. |


