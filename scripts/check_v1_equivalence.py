"""Verify every original metric against the preserved, unmodified v1 code."""
from pathlib import Path
import sys
import types
import zipfile
import math
ROOT=Path(__file__).resolve().parents[1]
with zipfile.ZipFile(ROOT/"archive/v1/PS1-Qingyue.zip") as z:
    source=z.read("companion/src/strategic_reporting.py").decode()
v1=types.ModuleType("preserved_v1")
sys.modules[v1.__name__]=v1
exec(compile(source,"preserved-v1/strategic_reporting.py","exec"),v1.__dict__)
sys.path.insert(0,str(ROOT/"companion/src"))
import strategic_reporting as v2
for condition in ("none","strategic","verified","high_lie_cost"):
    for seed in range(30):
        old=v1.run_once(v1.Config(condition=condition),seed)
        new=v2.run_once(v2.Config(condition=condition),seed)
        for key,value in old.items():
            assert new[key]==value or (math.isnan(value) and math.isnan(new[key])),(condition,seed,key)
print("PASS: all seven original metrics match v1 exactly for 120 full-length runs (four conditions x 30 seeds).")
