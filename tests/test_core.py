import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "sanger-review" / "scripts" / "sanger_review.py"
spec = importlib.util.spec_from_file_location("sanger_review", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def test_region_parser():
    assert mod.parse_region("10-20") == (10, 20)
    assert mod.parse_region("20:10") == (10, 20)


def test_manual_call_normalization():
    assert mod.norm_call("Candidate") == "Candidate"
    assert mod.norm_call("needs resequencing") == "Needs review"
    assert mod.norm_call("reject") == "No good clone"


def test_reference_name_targets():
    ref = mod.Ref("1", Path("sample1 K65E.fa"), "A" * 400, "sample1 K65E", 149, 400, {})
    sites = mod.targets_from_label(ref)
    assert len(sites) == 1
    assert sites[0].name == "K65E"
    assert sites[0].positions == [341, 342, 343]
