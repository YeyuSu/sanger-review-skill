# sanger-review-skill

[English](#english) | [中文](#中文)

<a id="english"></a>

## English

A Codex skill plus local Python CLI for reviewing Sanger sequencing `.ab1` reads against reference sequences.

### Features

- Parse ABI/Sanger `.ab1` base calls, quality values, and chromatogram traces.
- Compare reads against SnapGene `.dna`, FASTA, or GenBank references.
- Review target mutations or target regions with a target-first clone-picking policy.
- Generate Excel and HTML reports.
- Export chromatogram PNG files for problem reads or all reads.
- Apply manual review overrides so human chromatogram decisions are preserved in final clone calls.
- List all usable candidate clones for each sample, not only the best clone.

### Install For Codex

Copy or clone this repository, then install the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -r sanger-review ~/.codex/skills/
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse .\sanger-review $env:USERPROFILE\.codex\skills\
```

After installation, restart Codex or start a new session so the skill list is refreshed.

### Natural Language Usage

After installing the skill, you can ask Codex in plain language. Mention `$sanger-review` when you want to force this skill, or describe a Sanger/AB1 review task clearly enough for Codex to select it.

Example prompts:

```text
Use $sanger-review to review the AB1 files in reads/ against the SnapGene maps in refs/. The feature is CDS. Please list all candidate clones for each mutant and generate chromatogram PNGs for reads that need review.
```

```text
Use $sanger-review to compare my Sanger results with plasmid.gbk. Review region 149-1228, trim the first and last 100 bases, and generate an Excel report.
```

```text
Use $sanger-review for the sequencing folder F029707. The reference maps are in maps/, AB1 files are in reads/, mutation targets are in targets.csv, and the sample names are like mut3-1_T7_A01.ab1.
```

```text
Use $sanger-review to plot the chromatogram peaks for these AB1 files and help me manually inspect suspicious sites.
```

When the request is ambiguous, Codex should infer sensible defaults from filenames and available files, then ask only for missing high-impact details such as the target feature/region or filename pattern.

### Files To Prepare

Required:

- Sanger reads: one or more `.ab1` files, ideally named with sample/mutant, clone, and primer information.
- Reference sequence: SnapGene `.dna`, GenBank `.gb/.gbk`, or FASTA `.fa/.fasta` file(s).
- Target definition: either a feature name, a coordinate region such as `149-1228`, a target-site table, or reference filenames that encode expected mutations.

Recommended:

- `targets.csv` or `.xlsx` when you need mutation-level verification. Columns usually include `sample`, `name`, and either `aa_position` or `codon_start` plus expected bases/amino acids.
- A clear filename pattern, for example `mut3-1_T7_A01.ab1`, where `mut3` is the sample and `1` is the clone.
- Forward and reverse reads for each clone when available.
- `manual_overrides.csv` if you already inspected chromatograms and want to force a final call.

Example layout:

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

### Run Locally

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

### Common Options

- `--references`: reference file or directory. Supports `.dna`, `.fa/.fasta`, `.gb/.gbk`.
- `--reads`: `.ab1` file or directory.
- `--feature`: feature name in SnapGene or GenBank references.
- `--region`: coordinate range such as `149-1228`, useful for FASTA references.
- `--target-sites`: CSV/XLSX table of expected mutation or target positions.
- `--sample-regex`: regular expression for parsing sample, clone, and primer from AB1 filenames.
- `--manual-overrides`: CSV/XLSX table for human-reviewed final calls.
- `--trim-read-ends`: ignore unreliable read ends; default is `100` base calls.
- `--mode`: `target-first`, `strict`, or `differences-only`.
- `--chromatograms`: `problem`, `all`, or `none`.

### Outputs

- `sanger_review.xlsx`
- `sanger_review.html`
- `chromatograms/*.png`

The `Summary` sheet includes `candidate_clones`, so multiple usable clones can be selected for one sample.

### License

Apache-2.0

---

<a id="中文"></a>

## 中文

`sanger-review-skill` 是一个 Codex skill，也可以作为本地 Python CLI 使用，用来检查 Sanger 测序 `.ab1` 文件，并与参考序列比对，筛选可用的候选克隆。

### 功能

- 解析 ABI/Sanger `.ab1` 的 base call、质量值和原始峰图 trace。
- 支持与 SnapGene `.dna`、FASTA、GenBank 参考序列比对。
- 按目标突变位点或目标区域进行 review，默认采用“目标位点优先”的候选克隆筛选策略。
- 生成 Excel 和 HTML 报告。
- 导出问题 read 或全部 read 的峰图 PNG。
- 支持人工 review 覆盖自动判定，方便把看峰图后的结论保留在最终报告中。
- 每个样本会列出所有可用 candidate clone，而不是只列一个 best clone。

### 安装到 Codex

复制或 clone 本仓库，然后把 skill 文件夹安装到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -r sanger-review ~/.codex/skills/
```

Windows PowerShell：

```powershell
Copy-Item -Recurse .\sanger-review $env:USERPROFILE\.codex\skills\
```

安装后，重启 Codex 或开启新会话，让 skill 列表刷新。

### 自然语言调用方式

安装后，你可以直接用自然语言让 Codex 调用这个 skill。想强制使用时，在请求里写 `$sanger-review`；不写也可以，但要清楚说明你要 review Sanger/AB1 测序结果。

示例请求：

```text
使用 $sanger-review，帮我 review reads/ 里的 AB1 文件，参考图谱在 refs/，目标 feature 是 CDS。请列出每个突变体所有可用的 candidate clone，并给需要人工检查的 read 生成峰图。
```

```text
用 $sanger-review 比对我的 Sanger 测序结果和 plasmid.gbk，检查 149-1228 区域，忽略前后 100 个 base call，并生成 Excel 报告。
```

```text
用 $sanger-review 检查 F029707 测序文件夹。参考 map 在 maps/，AB1 文件在 reads/，目标突变表是 targets.csv，文件名格式类似 mut3-1_T7_A01.ab1。
```

```text
用 $sanger-review 把这些 AB1 文件的峰图导出来，帮我人工检查可疑位点。
```

如果信息不完整，Codex 会先根据文件名和目录结构推断默认值；只有缺少关键条件时才需要继续追问，比如目标 feature/区域、文件名解析规则或目标突变表。

### 需要准备的文件

必需：

- Sanger reads：一个或多个 `.ab1` 文件，文件名最好包含样本/突变体、克隆编号和引物信息。
- 参考序列：SnapGene `.dna`、GenBank `.gb/.gbk` 或 FASTA `.fa/.fasta`。
- 目标定义：可以是 feature 名称、坐标区域如 `149-1228`、目标位点表，或者在参考序列文件名中写明预期突变。

推荐：

- `targets.csv` 或 `.xlsx`：需要逐突变位点核对时使用，通常包含 `sample`、`name`，以及 `aa_position` 或 `codon_start` 等列。
- 清晰的文件名格式，例如 `mut3-1_T7_A01.ab1`，其中 `mut3` 是样本，`1` 是克隆编号。
- 每个克隆尽量提供正向和反向 reads。
- `manual_overrides.csv`：如果你已经看过峰图并希望覆盖自动判定，可以提供人工结论表。

推荐目录结构：

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

### 本地运行

安装 Python 依赖：

```bash
pip install biopython openpyxl matplotlib pyyaml
```

运行 CLI：

```bash
python sanger-review/scripts/sanger_review.py \
  --references refs/ \
  --reads reads/ \
  --feature CDS \
  --target-sites examples/minimal/targets.csv \
  --out outputs/sanger_review
```

### 常用参数

- `--references`: 参考序列文件或目录，支持 `.dna`、`.fa/.fasta`、`.gb/.gbk`。
- `--reads`: `.ab1` 文件或目录。
- `--feature`: SnapGene 或 GenBank 中的 feature 名称。
- `--region`: 坐标范围，例如 `149-1228`，适用于 FASTA 或没有 feature 注释的参考序列。
- `--target-sites`: 预期突变或目标位点 CSV/XLSX 表。
- `--sample-regex`: 用于从 AB1 文件名解析 sample、clone、primer 的正则表达式。
- `--manual-overrides`: 人工 review 后覆盖自动判定的 CSV/XLSX 表。
- `--trim-read-ends`: 忽略 read 两端不可靠 base call，默认 `100`。
- `--mode`: `target-first`、`strict` 或 `differences-only`。
- `--chromatograms`: `problem`、`all` 或 `none`。

### 输出文件

- `sanger_review.xlsx`
- `sanger_review.html`
- `chromatograms/*.png`

`Summary` sheet 中的 `candidate_clones` 会列出同一样本下所有可用克隆，方便挑选更多质粒。

### 许可证

Apache-2.0
