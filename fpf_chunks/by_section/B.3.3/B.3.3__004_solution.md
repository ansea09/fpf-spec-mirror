---
chunk_kind: "child"
pattern_id: "B.3.3"
pattern_title: "Assurance Subtypes & Levels"
section_id: "B.3.3:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.3/B.3.3__004_solution.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "B.3.3 — Assurance Subtypes & Levels"
  - "B.3.3:3 — Solution"
line_start: 32748
line_end: 32780
dependencies:
  - "A.10"
  - "A.4"
  - "B.3"
  - "B.3.1"
  - "B.4"
  - "D.4"
keywords:
  - "L0-L2"
  - "LA"
  - "TA"
  - "VA"
  - "assurance levels"
  - "typing"
  - "validation"
  - "verification"
---

### B.3.3:3 - **Solution**

FPF establishes a formal Standard that links three distinct **Assurance Subtypes** to three computable **Assurance Levels**. An assurance target's level is not assigned manually by an author; it is **derived automatically** by its anchored evidence. This creates a transparent and falsifiable system for tracking an assurance target's progression from a speculative idea to a robust, reliable holon.

#### B.3.3:3.1 - Assurance Subtypes: The Three Pillars of Trust

These three subtypes categorize the kind of question an assurance activity answers, ensuring a balanced approach to building confidence.

| Subtype | Code | Core Question | Links to Epistemic Score | Manager's View: What It Prevents |
| :--- | :--- | :--- | :--- | :--- |
| **Typing Assurance** | TA | “Does the assurance target faithfully represent its intended concept?” | **CL** (Congruence Level) | **Miscommunication & Integration Failures.** TA ensures that when a requirement says "Sensor," the design model's "Sensor" component is the same conceptual thing. This activity directly improves the Congruence Level (CL) of the integration *edges* between assurance targets. |
| **Verification Assurance**| VA | “Is the holon logically correct under its stated assumptions?” | **FV** (Formal Verifiability)| **"It Works on Paper" Errors.** VA catches design flaws, logical inconsistencies, and specification errors before a single line of code is written or a physical part is machined. It ensures the blueprint is sound. |
| **Validation Assurance**| LA | “Does the holon work correctly in the real world?” | **EV** (Empirical Validability)| **"Works in the Lab, Fails in the Field" Surprises.** LA confirms that the holon performs as expected under real or simulated operational conditions, accounting for noise, unexpected inputs, and environmental factors. |

#### B.3.3:3.2 - Computed Assurance Levels: Evidence-support progression

An assurance target's level is computed based on the evidence it has accumulated. This creates a declared progression for increasing trust without treating assurance as a generic ladder.

| Level | Name | How It Is Computed |
| :--- | :--- | :--- |
| **Level 0** | **Unsubstantiated** | No `verifiedBy` or `validatedBy` evidence is present. The assurance target is a claim or an idea. |
| **Level 1** | **Substantiated** | At least one `verifiedBy` or `validatedBy` link to an evidence carrier exists, and the assurance target is supported by Typing Assurance (TA). |
| **Level 2** | **Axiomatic** | The assurance target is `verifiedBy` either a proof **or** a **Compose‑CAL (Γₘ) constructive narrative** that the author has linked from the Working‑Model via `tv:groundedBy` (CT2R‑LOG). Its FormalVerifiabilityScore (FV) meets or exceeds a pre‑defined threshold. Additionally, if the holon is designated as safety‑critical, it **MUST** also be supported by **Validation Assurance (LA)**. For non‑critical holons, LA is recommended (`SHOULD`). |

> **Didactic Note for Managers: What 'Level 1' Really Means**
>
> Think of moving from Level 0 to Level 1 as the first step toward professional seriousness.
>
> *   **Level 0** is an idea on a whiteboard. It has potential, but no receipts.
> *   **Level 1** means you have **at least one receipt**. You have anchored the idea to something concrete: a passing test, a formal sketch, a simulation result. It's no longer just an opinion.
>
> Crucially, Level 1 also demands **Typing Assurance (TA)**. This sounds technical, but its business impact is simple: **it means you've named your terms correctly and consistently**. You've used the Role-Projection Bridge (Pattern B.5) to ensure that the "Sensor" in your requirements document is the same "Sensor" in your architectural diagram. This basic alignment work is what prevents costly integration failures and endless meetings where teams talk past each other. Good typing is the foundation of clear communication, and at Level 1, FPF makes it mandatory.

