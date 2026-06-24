# Calling policy

Default mode is `target-first`.

A clone is a `Candidate` when all target sites are covered and match the reference/expected sequence, and no high-quality internal mismatch or conflict is detected. Suspected indels after the final target site are reported but do not necessarily block candidate status.

A clone is `Needs review` when target sites are missing/partial, suspected indels occur before or within the target span, or the evidence is not clean enough for an automatic candidate call.

A clone is `No good clone` when target sites disagree with expectation or high-quality mismatch/conflict is detected in the reviewed region.

Use manual overrides after inspecting AB1 chromatograms. Overrides are included in reports so automatic and final calls remain traceable.
