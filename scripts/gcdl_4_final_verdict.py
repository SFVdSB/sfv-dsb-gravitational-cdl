#!/usr/bin/env python3
"""Consistency check for the frozen GCDL-4 classification."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
summary = json.loads((root/'results/GCDL_4_FINAL_VERDICT.json').read_text())
assert summary['formal_classification'] == 'G-C'
assert summary['conditional_dynamical_completion'] is True
assert summary['full_fp_gravity_closure'] is False
assert summary['absolute_de_bridge'] is False
assert summary['surviving_continuous_primitive_count'] == 4
assert summary['kappa_HM_is_time_dependent_switch'] is False
assert summary['particle_dump_derived'] is False
print('GCDL-4 consistency: PASS')
print(summary['formal_label'])
