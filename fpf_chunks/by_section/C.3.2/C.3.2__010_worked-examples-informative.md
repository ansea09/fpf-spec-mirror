---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "KindSignature (+F) & Extension/MemberOf"
section_id: "C.3.2:9"
section_title: "Worked Examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__010_worked-examples-informative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.3.2 — KindSignature (+F) & Extension/MemberOf"
  - "C.3.2:9 — Worked Examples (informative)"
line_start: 36776
line_end: 36808
dependencies:
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
keywords:
  - "Formality F"
  - "KindSignature"
  - "MemberOf"
  - "determinism"
  - "extension"
  - "intension"
---

### C.3.2:9 - Worked Examples (informative)

#### C.3.2:9.1 - Vehicle (signature F4) and membership

**KindSignature(Vehicle)** *(F4)*:

* `hasVIN(x)` is true and parseable;
* `axles(x) ≥ 2`;
* `hasBrakeSystem(x)`;
* Standards: `registryAPI v1.4`; `Γ_time` policy: rolling 365 d for registry fields.

**`U.EntitySet(slice)`**: “records in `registryAPI v1.4` for plant `A` at build `b`, as of `Γ_time`.”
**`Extension(Vehicle, slice)`**: all records satisfying the predicates **in that `slice`**.
**Monotonicity:** `PassengerCar ⊑ Vehicle` ⇒ `Extension(PassengerCar, s) ⊆ Extension(Vehicle, s)`.

#### C.3.2:9.2 - AuthenticatedRequest (definedness & fail‑closed)

**KindSignature(AuthenticatedRequest)** *(F4)*:

* `Request` with `authHeader` present and `authSignature` valid according to `AuthStandard v2.3`;
* `Γ_time`: point in time for key validity check.

**Definedness:** `MemberOf(–, AuthenticatedRequest, slice)` is **undefined** if `AuthStandard v2.3` is **absent** in `slice` ⇒ guards **fail closed** (C3.2‑K‑07).

#### C.3.2:9.3 - Clinical cohort (low‑F signature; deterministic membership)

**KindSignature(AdultPatient)** *(F3→F4 as it hardens)*:

* `ageYears(x, Γ_time) ≥ N` (jurisdictional N varies; recorded in the Context’s signature note).
* `EntitySet(slice)`: EHR `ehr‑east v7.5` @ `Γ_time`;
* Membership deterministic if DOB present; undefined otherwise (fail closed).


