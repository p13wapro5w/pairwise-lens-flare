import pytest
from render import lens_flare as mod

CASES = [
    ("project_mid", "m.project_light((1.0, 2.0), (2.0, 4.0)) == approx((0.5, 0.5))"),
    ("project_zero", "m.project_light((0.0, 0.0), (2.0, 4.0)) == approx((0.0, 0.0))"),
    ("occlusion_two", "m.occlusion_count([1, 1, 0]) == 2"),
    ("occlusion_none", "m.occlusion_count([0, 0]) == 0"),
    ("ghost_six", "m.ghost_count(1.0) == 6"),
    ("intensity_six", "m.flare_intensity(2.0, 3.0) == approx(6.0)"),
    ("threshold_high", "m.highlight_threshold(2.0, 1.0) == approx(1.0)"),
    ("threshold_low", "m.highlight_threshold(0.5, 1.0) == approx(0.0)"),
    ("transmission_half", "m.transmission(0.5) == approx(0.5)"),
    ("fov_same", "m.update_fov(60.0) == approx(60.0)"),
    ("flares_sum", "sum(m.normalize_flares([2.0, 2.0])) == approx(1.0)"),
    ("flares_half", "m.normalize_flares([2.0, 2.0])[0] == approx(0.5)"),
    ("ui_excluded", "m.exclude_ui(True) is False"),
    ("stereo_left", "m.stereo_shift(0) == approx(0.0)"),
    ("stereo_right", "m.stereo_shift(1) == approx(0.5)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
