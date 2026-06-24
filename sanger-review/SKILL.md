---
name: sanger-review
description: Review Sanger sequencing AB1 chromatograms against reference sequences and call candidate clones. Use when Codex needs to parse .ab1 files, compare reads to SnapGene .dna, FASTA, or GenBank references, inspect target mutations or regions, generate chromatogram PNGs, produce Excel/HTML reports, and apply manual review overrides for clone picking.
---

# Sanger Review

Use this skill to review Sanger `.ab1` reads against reference sequences and identify usable candidate clones.

## Quick start

```bash
python path/to/sanger-review/scripts/sanger_review.py \
  --references refs/ \
  --reads reads/ \
  --feature CDS \
  --target-sites targets.csv \
  --out outputs/sanger_review
```

For SnapGene maps with mutation names in filenames:

```bash
python path/to/sanger-review/scripts/sanger_review.py \
  --references refs/ \
  --reads reads/ \
  --feature MyFeature \
  --reference-regex "(?P<sample>\\d+)" \
  --sample-regex "mut(?P<sample>\\d+)-(?P<clone>\\d+)_(?P<primer>[^_]+)" \
  --targets-from-reference-names
```

## Inputs

- References: `.dna`, `.fa/.fasta`, `.gb/.gbk` files or a directory.
- Reads: `.ab1` files or a directory.
- Target sites: optional CSV/XLSX with `sample`, `name`, and either `aa_position` or `codon_start`.
- Manual overrides: optional CSV/XLSX with `sample`, `clone`, `manual_call`, `note`.

See `references/input_formats.md` for column details.

## Calling policy

Default mode is `target-first`:

- `Candidate`: target sites match and no blocking mismatch/conflict is detected, or manual review confirms the clone.
- `Needs review`: target sites are missing/partial or suspected indels require chromatogram inspection.
- `No good clone`: target sites disagree or high-quality internal mismatch/conflict is detected.

Use `--mode strict` for full target-region agreement, or `--mode differences-only` to avoid clone calls.

Manual overrides supersede conservative automatic warnings and are kept in the report as `manual_override` and `manual_note`.

## Outputs

- `sanger_review.xlsx`: `Summary`, `CloneReview`, `TargetSites`, `ProblemSites`, `Reads`.
- `sanger_review.html`: browser-readable summary.
- `chromatograms/`: AB1 peak plots for problem reads or all reads.

`Summary.candidate_clones` lists all usable clone IDs, not only the best clone.
