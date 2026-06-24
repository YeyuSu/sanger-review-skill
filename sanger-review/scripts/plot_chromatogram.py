#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import importlib.util
import sys


def load_main():
    script = Path(__file__).with_name('sanger_review.py')
    spec = importlib.util.spec_from_file_location('sanger_review', script)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    parser = argparse.ArgumentParser(description='Write chromatogram PNG plots from AB1 files.')
    parser.add_argument('ab1', type=Path, nargs='+')
    parser.add_argument('--out', type=Path, default=Path('chromatograms'))
    parser.add_argument('--sample-regex', default=r'(?P<sample>.+?)[-_](?P<clone>\d+)[-_](?P<primer>[^_.]+).*\.ab1$')
    args = parser.parse_args()
    mod = load_main()
    args.out.mkdir(parents=True, exist_ok=True)
    for path in args.ab1:
        read = mod.read_ab1(path, args.sample_regex, {})
        out = mod.plot_chrom(read, args.out)
        print(out or f'Could not plot {path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
