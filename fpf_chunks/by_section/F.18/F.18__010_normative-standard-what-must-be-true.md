---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:9"
section_title: "Normative Standard (what must be true)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__010_normative-standard-what-must-be-true.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:9 — Normative Standard (what must be true)"
line_start: 74017
line_end: 74062
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:9 - Normative Standard (what must be true)

> This section is binding. It specifies the publication Standard for unification-oriented names in the Unification Suite (Part F), with **local-first authority**, **bounded context clarity**, and **one-way unification** through declared dependency strata. It complements, and does not replace, the structural and epistemic Standards elsewhere in FPF.

**9.1 Local authority & stewardship context.**
Every unification name has a **single stewardship Bounded Context**: exactly one *Bounded Context* that authors and stewards it. That stewardship Context is responsible for the definition, examples, and lineage of the name. Cross-context reuse happens by **bridges**, not by relocating the stewardship Context.

**9.2 Minimum definitional payload.**
A published name MUST ship with a human-readable **Minimal Definitional Statement (MDS)** that states the intended sense in the stewardship context, and a **Didactic Subtitle** (≤ 12 words) that signals its pragmatic use. The MDS must be free of process slang and implementation jargon.

**9.3 Row ID plus labels.**
For each adopted name, the stewardship Context supplies:
* a **Row ID** (the opaque UTS identifier — the **identity anchor**), and
* two **labels**: a **Unified Tech** label (for Core prose) and a **Plain** label (for teaching).
  Both labels refer to the same underlying sense; **Plain** may simplify terms, not premises.

**9.4 One-way dependency strata.**
Each dependency stratum depends only on already-admitted lower strata: a name in stratum *n* can rely on names admitted in strata ≤ *n*, never sideways or upwards. Cycles are prohibited. If a dependency is not yet admitted at the required stratum, the new name remains Draft or Pilot.

**9.5 Local‑first before reuse.**
Teams MUST first **identify and stabilize the local sense** (within their Bounded Context). **Within the stewardship Context**, reuse existing **Concept-Set rows** where they fit (§4.2 **P1**). **Across contexts**, reuse occurs via **Alignment Bridges** that map the local sense to an existing sense elsewhere without collapsing the local stewardship Context.

**9.6 Sense, not string.**
Publication concerns **sense** (intended meaning in context), not the literal string. Synonyms are allowed as **Plain** labels or **aliases** only if they point to the same **Row ID** and pass the conformance checks in §15 (“CC‑F18”). Strings must not be treated as identity.

**9.7 Relation-kind discipline (structural vs epistemic).**
If the public name expresses a **structural relation**, its intended sense **MUST** be backed by *exactly one Constructive trace* in the structural calculus (Compose-CAL) and **SHALL** declare `validationMode=axiomatic` (see E.14). If the name expresses an **epistemic relation**, Constructive backing is optional; **declare** `validationMode ∈ {inferential, postulate}` and use **Logical/Mapping** and/or **Empirical Validation** as appropriate. **Do not mix relation kinds** inside a single name. *(Do not use “Tier-1/2”; formality is expressed via F per C.2.3.)*

**9.8 Member vs Component.**
Names that describe collection membership MUST NOT be used to imply part‑whole structure, and vice versa. If both aspects are needed, publish two names with their own MDS and an explicit bridge.

**9.9 Name-lineage states.**
A name travels through **Idea → Draft → Pilot → Ratified → Deprecated**. Transitions require explicit human review gates. Ratified names carry a clear stewardship contact and date.

**9.10 Anti‑duplication duty.**
Before ratification, the stewardship Context MUST perform a **near-neighbor review**: identify adjacent names, record the decision to align, merge, or keep separate, and publish the rationale in the name’s record.

**9.11 Local clarity over global neatness.**
When in doubt, prefer **local intelligibility** for practitioners over global symmetry. Global neatness can be achieved later via bridges; loss of local sense is hard to repair.

**9.12 No imported tool terms in Core names.**
Names and their MDS must not carry terms whose only meaning is tied to operating tools or pipelines. If such terms are unavoidable in pedagogy, confine them to Working-Names and examples with disclaimers.

**9.13 Human‑only conformance.**
Conformance for this protocol is judged by trained human reviewers using the author and reviewer checklists in §14 and the conformance criteria in §15 (“CC‑F18”). Automated heuristics, if any exist in an organization, have no standing in the Core.

