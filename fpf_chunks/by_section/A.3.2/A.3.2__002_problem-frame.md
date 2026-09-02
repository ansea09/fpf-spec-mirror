---
chunk_kind: "child"
pattern_id: "A.3.2"
pattern_title: "U.MethodDescription: Description Episteme for a Way of Doing"
section_id: "A.3.2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2/A.3.2__002_problem-frame.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.3.2 — U.MethodDescription: Description Episteme for a Way of Doing"
  - "A.3.2:1 — Problem frame"
line_start: 8618
line_end: 8655
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.6.1"
  - "A.6.5"
  - "B.1.5"
  - "B.3"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "F.6"
  - "F.9"
  - "U.Method"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "claim-bearing episteme"
  - "exact U.Method EntityOfConcern"
  - "method-description membership"
  - "representation versus publication versus plan versus Work"
  - "same method versus equivalent descriptions"
  - "substantive way-of-doing claim"
---

### A.3.2:1 - Problem frame

**When the reusable way is still only a candidate.** A candidate account or mined behavioural model is not a `U.MethodDescription` merely because it is coherent, executable, process-shaped, or traceable to sources. First use `A.3.1.MR` while the reusable way is still being recovered. Apply this pattern only after the account's `EntityOfConcern` has been admitted as one `U.Method`, and only when that same episteme makes a substantive claim about the Method as a way of doing.

Use this pattern when engineers need reusable claims about how one Method is carried out and must keep those claims distinct from the representation, publication, approval, plan, or actual Work through which the Method is discussed or enacted. In FPF terms, decide whether an already identified `U.Episteme` is a `U.MethodDescription`: whether its `EntityOfConcern` is one admitted `U.Method` and its claims say something substantive about that Method as a way of doing.

**Plain reading.** A method description is the knowledge object whose claims say how one identified method is done. Code, text, or a diagram may represent those claims; a publication occurrence may make an edition available; neither fact decides membership.

Recognizable working moments include:

* a maintenance team comparing a revised procedure with the method used to plan the next service window;
* a clinical team selecting a triage guideline while keeping guideline claims, approval, and patient-specific work separate;
* a production-planning team comparing scheduling-method claims while the MILP representation and solver runs change.

Use it when the working question is:

* which admitted `U.Method` is the episteme's `EntityOfConcern`;
* which claim states the method's transformation or enactment concern, applicability, precondition, effect, bound, or internal composition;
* whether anyone is proposing a use beyond membership; if so, what that use is, where it belongs, and which method claims it needs;
* which `C.29` representation corresponds to the claims, which publication occurrence makes the selected edition available, which publication form expresses it, and which `U.PresentationCarrier` bears that form—but only when the proposed use needs those distinctions;
* whether two epistemes concern the same A.3.1-identified Method and, separately, whether their claim content is equivalent for the proposed use; the later use sections carry any needed scheme correspondence, evidence-reliance, and assurance checks.

**Object being classified.** A.3.2 examines one already identified claim-bearing `U.Episteme` candidate and judges whether that same individual belongs to the dependent kind `U.MethodDescription`. For positive membership, the candidate episteme's C.2.1 `EntityOfConcern` must resolve to one admitted `U.Method`, and at least one of its claims must concern that Method as a way of doing. The Method is the internal subject of the episteme's claims, not a second candidate and not the object being classified. A.3.2 adds neither another episteme identity nor a binary description relation.

**Primary working reader.** An engineer, researcher, publisher, teacher, planner, or auditor who must identify or rely on reusable claims about a method before planning, enactment, comparison, audit, revision, publication, or teaching.

**Primary working concern.** Identify the claim-bearing episteme and its Method first. When someone proposes a further use, name that use and its subject pattern, then ask which claims the use needs and whether this edition contains them. With no proposed use, stop at membership.

**Primary viewpoint.** The practitioner selecting, comparing, or revising method descriptions while method identity and the surrounding representation and publication relations remain explicit.

**First useful move.** Name the candidate `U.Episteme`. Check two things: its C.2.1 `EntityOfConcern` is one admitted `U.Method`, and at least one claim says how that Method is done. If both hold, the same episteme is a `U.MethodDescription`; if either fails, it is not. Only then, if someone proposes a concrete further use, write that use's criterion and result as a separate subject assertion under its exact predicate, with an optional subject-pattern locator. Otherwise stop at membership; do not invent Work, a decision, or an adequacy result.

**What goes wrong if missed.** A visible file or diagram is classified by its form, a mere mention is mistaken for a description, or an episteme about a relation structure among several Methods is treated as if it described one composite Method. Planning, enactment, audit, and review then rely on the wrong object.

**What this buys.** The project can identify, compare, revise, and reuse method descriptions while keeping the described `U.Method`, `RelationSignature`, `OperationAlgebra`, C.29 representations, publication occurrences and forms, presentation carriers, work plans, work occurrences, and evidence under their own subject patterns.

**Not this pattern when.** Do not infer membership from words such as `algorithm`, `program`, `proof`, `workflow`, `process`, `procedure`, `recipe`, or `model`. Ask what the sentence actually asserts. If its `EntityOfConcern` is not an admitted `U.Method`, or it says nothing substantive about that Method as a way of doing, A.3.2 does not apply. Use the pattern for the actual Method, selected structure, formal declaration, work plan, dated Work, evidence use, or publication use instead.

