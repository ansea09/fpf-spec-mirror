---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:11"
section_title: "Application Guidance (how to apply, step by step)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__012_application-guidance-how-to-apply-step-by-step.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:11 — Application Guidance (how to apply, step by step)"
line_start: 75416
line_end: 75472
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

### F.18:11 - Application Guidance (how to apply, step by step)

**11.1 Prepare (30–60 min).**

* Clarify **your Bounded Context** and audience.
* Collect 2–3 typical user stories that require the name.
* Scan near‑neighbors in adjacent contexts (see §14.2 Reviewer checklist).

**11.2 Mint locally.**

* Write the **MDS** in plain language, one paragraph.
* Draft a **Didactic Subtitle** (≤ 12 words): “what this name buys you.”
* Decide whether the intended **relation kind** is **structural** or **epistemic** (do not mix), and declare `validationMode`.

**11.3 Choose labels.**

* **Unified Tech label**: concise, morphology‑stable, neutral; avoid metaphor.
* **Plain label**: approachable phrasing for non‑specialists.
* **How to choose**: pick both **from a small NQD‑frontier** (see §4.2 P1 (candidate set), P2(read-through)): diversify by tradition, novelty/familiarity, and lexical form; record discarded contenders and rationale on the Card.

**11.4 Place in the dependency stratum.**

* Verify all dependencies are at the same dependency stratum or below.
* If a dependency is still Draft/Pilot, keep this name at most Pilot.

**11.5 Align, don’t erase.**

* Where overlap exists with another context, propose an **alignment bridge**.
* Keep your stewardship Context; record the mapping and any known divergence in reading.

**11.5a Test the replacement candidate against umbrella drift.**

* Before replacing an overloaded head, apply the `E.10:0.2` replacement-candidate anti-umbrella rule. Then run the candidate head through the same local-first naming test: primary `EntityOfConcern`, receiving FPF pattern, carried admissible move, kind named by value/ref or local field, relation or claim record when live, neighboring exclusions, and example fit.
* Do not approve a candidate merely because it avoids the old bad word. The replacement is acceptable only when the FPF kind named by value or local field is defined by value and the current use names its boundaries.
* If the candidate still hides several possible kinds, keep a candidate-set note and do not mint, rename, or land the term yet.

**11.5b Keep interpretive-view labels subordinate to the base candidate set or family.**

* When a naming pass talks about one palette, front, archive, shortlist, or candidate set, keep that base candidate set or family recoverable on the Name Card.
* Use thinner interpretive-view wording when the pressure is local comparison across candidate labels, sense-seeds, rejected candidates, or guarded-head notes.
* Use atlas wording only when the naming explanation truly depends on several declared views, spaces, mappings, or distortion qualifiers being visible together, for example one cited `OutcomeMapRef` plus a `BridgeDistortionNote`.
* Those cited spaces or qualifiers stay naming-side reuse of already-declared substrate qualifiers; they do not let naming passages mint one new source-to-outcome relation or one new publication-use relation locally.
* A guarded-head note remains naming governance: it can explain why one head word misleads across admissible readings, but it does not decide substrate stewardship or publication policy.

**11.6 Publish and steward.**

* Publish the name with MDS, subtitle, dependency stratum, stewardship contact, examples.
* Schedule a **first refresh**: when should the stewardship Context examine usage and drift?

**11.7 Deprecate gracefully.**

* If the sense is superseded, publish **Deprecation Notes**: what to use instead, and why. Keep old Working-Names visible long enough to allow safe migration.

**11.8 The “Friday test.”**

* On a busy Friday, could a competent colleague apply the name correctly using only the MDS, subtitle, and two examples? If not, refine before ratification: it is too overloaded with meanings to be helpful.

