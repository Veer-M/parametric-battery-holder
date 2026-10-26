import math
import pytest
from build123d import export_step, import_step
from battery_holder import build_holder, dimensions

def test_geometry_and_step_roundtrip(tmp_path):
    part = build_holder(2,2)
    width,depth = dimensions(2,2)
    assert part.is_valid
    assert len(part.solids()) == 1
    assert part.bounding_box().size.X == pytest.approx(width)
    assert part.bounding_box().size.Y == pytest.approx(depth)
    assert part.volume == pytest.approx((width*depth-4*math.pi*(18.5/2)**2)*65.5, rel=1e-6)
    path = tmp_path/'holder.step'
    assert export_step(part,str(path))
    assert import_step(str(path)).volume == pytest.approx(part.volume,rel=1e-6)

def test_bad_dimensions():
    with pytest.raises(ValueError):
        build_holder(0,2)
    with pytest.raises(ValueError):
        build_holder(pitch=18)
