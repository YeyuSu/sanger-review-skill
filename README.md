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

`sanger-review-skill` 是一个 Codex skill，同时也可以作为本地 Python CLI 使用，用于查看 Sanger 测序 `.ab1` 文件，并与参考序列进行比对和候选克隆筛选。

### 功能

- 解析 ABI/Sanger `.ab1` 的 base call、质量值和原始峰图 trace。
- 支持与 SnapGene `.dna`、FASTA、GenBank 参考序列比对。
- 按目标突变位点或目标区域进行 review，默认采用“目标位点优先”的候选克隆筛选策略。
- 生成 Excel 和 HTML 报告。
- 导出问题 read 或全部 read 的峰图 PNG。
- 支持人工 review 覆盖自动判定，方便把人工看峰图后的结论保留在最终报告中。
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
