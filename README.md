# sanger-review-skill

A Codex skill plus local Python CLI for reviewing Sanger sequencing `.ab1` reads against reference sequences.

It supports:

- ABI/Sanger `.ab1` base calls, quality values, and chromatogram traces.
- SnapGene `.dna`, FASTA, and GenBank references.
- Target-first clone review for mutation confirmation.
- Excel and HTML reports.
- Chromatogram PNG output.
- Manual review overrides for final candidate clone calls.

## Install for Codex

Copy or clone this repository, then install the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -r sanger-review ~/.codex/skills/
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse .\sanger-review $env:USERPROFILE\.codex\skills\
```

## Run locally

Install Python dependencies:

```bash
pip install biopython openpyxl matplotlib pyyaml
```

Run the CLI:

```bash
python sanger-review/scripts/sanger_review.py \
  --references refs/ \
  --reads reads/ \
  --feature CDS \
  --target-sites examples/minimal/targets.csv \
  --out outputs/sanger_review
```

## Outputs

- `sanger_review.xlsx`
- `sanger_review.html`
- `chromatograms/*.png`

The `Summary` sheet includes `candidate_clones`, so multiple usable clones can be picked for one sample.

## License

MIT
