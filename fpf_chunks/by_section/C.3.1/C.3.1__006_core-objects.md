---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:4"
section_title: "Core Objects"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__006_core-objects.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:4 — Core Objects"
line_start: 45025
line_end: 45044
dependencies:
  - "A.1"
  - "A.11"
  - "A.2"
  - "A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "U.SubkindOf direct relation"
  - "assertion episteme"
  - "local kind"
  - "partial order"
  - "relation occurrence"
  - "relation-obtaining predicate"
---

### C.3.1:4 - Core Objects

| Object | Meaning | Boundary |
| --- | --- | --- |
| `U.Kind` | A kind value identified within one bounded context by a local identity basis; typed claims use `KindSignature` editions whose content names the effective `U.ReferenceScheme`. | It is not automatically a durable public FPF U-kind, and the scheme is not stored on the kind. |
| `U.SubkindOf` | The admitted direct relation kind that orders two local `U.Kind` values under one effective reference scheme. Its participants are the narrower kind and the broader kind. | It is not a predicate expression, assertion episteme, dependency, part-whole, slot-filling, construction, system-role assignment, or admission relation. |
| `SubkindOfObtains(k1, k2; RS)` | The relation-obtaining predicate: under exact reference-scheme edition `RS`, the aligned kind interpretations make every defined `true` judgment for `k1` imply `true` for `k2` over the declared candidate domain and applicable slices. | The predicate is rule content; it is not the obtaining occurrence. An unresolved required judgment leaves an assertion about obtaining unresolved rather than making the relation false. |
| `R_sub : U.SubkindOf` | One obtaining direct relation occurrence between exact narrower kind `k1` and broader kind `k2` under `RS`. | Expose an occurrence designator only when a named receiver needs to distinguish or refer to the occurrence. Participant identities plus the exact effective reference-scheme edition determine its identity. |
| subkind assertion episteme | A C.2.1 episteme whose content affirms, denies, or leaves unresolved `SubkindOfObtains(k1, k2; RS)` and cites the aligned signature editions and support used. | The assertion neither makes the relation obtain nor creates `R_sub`; a negative or unresolved assertion designates no obtaining occurrence. |
| local kind-identity criterion | The declared basis for deciding whether two kind references, including references across signature editions, designate the same local kind. | It is not the membership criterion itself. |
| `KindSignature` edition | The C.3.2 declaration episteme used to judge candidates for a kind. | It is neither the kind nor the order relation. |

#### C.3.1:4.1 - Direct `U.SubkindOf` Relation Boundary

`U.SubkindOf` is the C.3.1 direct relation kind, not the name of a claim. A readable sentence such as `CoolingPumpKind is a subkind of PumpKind in PlantScheme-7` states that the direct relation obtains for those two kind participants under the named scheme. It needs no occurrence identifier when no receiver depends on occurrence identity.

The relation obtains only when the exact effective reference-scheme edition and the compatible `KindSignature` editions make the monotonic implication hold throughout the declared candidate domain and applicable context slices. A known counterexample refutes obtaining for that alignment. Missing evidence, an unavailable dependency, an out-of-domain candidate, or another `unknown` judgment does not count as a counterexample, but it cannot by itself establish the universal obtaining predicate. `U.ContextSlice` is an input quantified by the predicate and by each C.3.2 judgment; it is neither a third relation participant nor scope stored on either kind.

When a named receiving assertion, description, or relation needs one occurrence recoverably distinguished, use `R_sub : U.SubkindOf` only after obtaining is established. Its identity is participant-determined by the exact narrower kind, broader kind, and effective reference-scheme edition. A new signature edition prompts reevaluation of obtaining but does not by itself create another occurrence when C.3.1 preserves both kind identities and the same relation continues to obtain. Any affirmative, negative, or unresolved statement about the predicate is a separate C.2.1 assertion episteme; assertion polarity, evidence, publication, or editioning never substitutes for the direct relation.

