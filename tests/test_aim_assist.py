import pytest
from gameplay import aim_assist as mod

CASES = [
    ("fov", 'm.in_fov(10.0, 30.0) is True'),
    ("fov_out", 'm.in_fov(20.0, 30.0) is False'),
    ("sens", 'm.sensitivity_norm(2.0, 1.0) == approx(2.0)'),
    ("hysteresis", 'm.switch_hysteresis(2.0, 1.0, 0.5) is True'),
    ("no_hysteresis", 'm.switch_hysteresis(1.2, 1.0, 0.5) is False'),
    ("occlusion", 'm.occlusion_ok(True) is True'),
    ("device", 'm.device_scale("gamepad") == approx(1.0)'),
    ("lag", 'm.lag_target(10.0, 8.0) == approx(8.0)'),
    ("aspect", 'm.aspect_scale(1920, 1080) == approx(1.7778, rel=1e-3)'),
    ("threat", 'm.threat_priority(2.0, 4.0) == approx(2.0)'),
    ("recoil", 'm.recoil_separate(1.0, 0.5) == approx(0.5)'),
    ("death", 'm.release_on_death(False) is True'),
    ("frame", 'm.frame_independent(0.5, 2.0) == approx(1.0)'),
    ("soft", 'm.soft_lock(0.0, 1.0, 0.5) == approx(0.5)'),
    ("return", 'm.return_smooth(0.0, 1.0, 0.5) == approx(0.5)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
