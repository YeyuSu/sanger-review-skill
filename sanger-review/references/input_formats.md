# Input formats

## Reference files

Supported reference formats:

- `.dna`: SnapGene files. Use `--feature` to select a feature by name/type, or `--region START-END`.
- `.gb`, `.gbk`, `.genbank`: GenBank files. Use `--feature` or `--region`.
- `.fa`, `.fasta`, `.fna`: FASTA files. Use `--region` when only part of the sequence should be reviewed.

Reference sample IDs default to file stems. Use `--reference-regex` with a `(?P<sample>...)` group to parse IDs from filenames.

## Read filenames

Use `--sample-regex` to parse AB1 filenames. The regex should provide named groups:

- `sample`: reference/sample ID.
- `clone`: clone or colony ID.
- `primer`: sequencing primer/read direction.

Example:

```text
S123_sample7-2_T7_A01.ab1
.*sample(?P<sample>\d+)-(?P<clone>\d+)_(?P<primer>[^_]+)_.*\.ab1$
```

## Target sites

CSV/XLSX columns:

- `sample`: reference/sample ID.
- `name`: label such as `K65E`.
- `aa_position`: amino-acid position inside the selected feature. The script checks the codon in the reference sequence.

Alternatively use nucleotide positions:

- `codon_start` or `position`: 1-based reference coordinate.
- `expected`: expected base/codon. If omitted, the reference sequence is used.

## Manual overrides

CSV/XLSX columns:

- `sample`
- `clone`
- `manual_call`: `Candidate`, `Needs review`, or `No good clone`.
- `note`

Manual overrides are meant for human chromatogram review results and supersede conservative automatic calls.
