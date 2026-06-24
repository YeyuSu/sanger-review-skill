---
name: sanger-review
description: Review Sanger sequencing AB1 chromatograms against reference sequences and call candidate clones. Use when Codex needs to parse .ab1 files, compare reads to SnapGene .dna, FASTA, or GenBank references, inspect target mutations or regions, generate chromatogram PNGs, produce Excel/HTML reports, and apply manual review overrides for clone picking.
---

# Sanger Review

Use this skill to review Sanger `.ab1` reads against reference sequences and identify usable candidate clones.

## Natural language use

When the user asks in natural language, translate the request into a CLI run and report review artifacts. Typical prompts include:

- "Use $sanger-review to review AB1 files in `reads/` against SnapGene maps in `refs/`; the feature is `CDS`; list all candidate clones."
- "Compare my Sanger results with `plasmid.gbk`, review region `149-1228`, trim the first and last 100 base calls, and generate an Excel report."
- "The sequencing folder is `F029707`; maps are in `maps/`; AB1 files are in `reads/`; target mutations are in `targets.csv`; filename style is `mut3-1_T7_A01.ab1`."
- "Plot chromatograms for these `.ab1` files so suspicious sites can be manually inspected."

If a request is incomplete, infer from available files first. Ask only when a required high-impact input is missing, especially the reference file, reads folder, target feature/region, target-site table, or filename parsing pattern.

## Files users should prepare

Required inputs:

- Sanger reads: `.ab1` files, preferably named with sample/mutant, clone, and primer information.
- Reference sequence: SnapGene `.dna`, GenBank `.gb/.gbk`, or FASTA `.fa/.fasta`.
- Target definition: one of `--feature`, `--region`, `--target-sites`, or mutation names encoded in reference filenames with `--targets-from-reference-names`.

Useful optional inputs:

- `targets.csv` or `.xlsx`: expected mutation/target positions with `sample`, `name`, and either `aa_position` or `codon_start`.
- `manual_overrides.csv` or `.xlsx`: columns `sample`, `clone`, `manual_call`, and `note` for human-reviewed calls.
- A filename regex if sample/clone/primer cannot be inferred from names.
- Sequencing metadata from the vendor, when available.

Example project layout:

```text
project/
  refs/
    mut3.dna
    mut4.dna
  reads/
    mut3-1_T7_A01.ab1
    mut3-1_T7term_A02.ab1
    mut3-2_T7_A03.ab1
  targets.csv
  manual_overrides.csv
```

## Workflow

1. Locate reference files and `.ab1` reads from the user request or current workspace.
2. Determine the target review scope using `--feature`, `--region`, `--target-sites`, or `--targets-from-reference-names`.
3. Choose or infer `--sample-regex` so sample and clone IDs are parsed correctly. Prefer listing all passing clones over choosing only one best clone.
4. Run `scripts/sanger_review.py` with `--trim-read-ends 100` unless the user specifies a different end-trimming rule.
5. Generate chromatograms with `--chromatograms problem` by default, or `all` when the user asks to inspect peaks broadly.
6. Summarize `Summary.candidate_clones`, blocking differences, manual overrides, and report paths.

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
