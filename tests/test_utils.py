import pytest
from src.utils import add, subtract


# ---------- Partner A tests ----------
@pytest.mark.parametrize("nums,expected", [
    (tuple(), 0),                # empty -> 0
    ((5,), 5),                   # single -> itself
    ((1, 2, 3), 6),              # normal ints
    ((-1, 1, 10), 10),           # negatives + positives
    ((1.5, 2.5, 3.0), 7.0),      # floats
])
def test_add(nums, expected):
    assert add(*nums) == expected


@pytest.mark.parametrize("nums,expected", [
    (tuple(), 0),                # empty -> 0
    ((5,), 5),                   # single -> itself
    ((10, 3), 7),                # two args
    ((10, 3, 2), 5),             # multiple args
    ((0, 1, 2, 3), -6),          # result negative
    ((10.5, 0.5), 10.0),         # floats
])
def test_subtract(nums, expected):
    assert subtract(*nums) == expected


# ---------- Partner B placeholder (skip-safe) ----------
# These will run automatically once Partner B adds multiply/divide.
try:
    from src.utils import divide
    HAS_DIVIDE = True
except Exception:
    HAS_DIVIDE = False


@pytest.mark.skipif(not HAS_DIVIDE, reason="Partner B's divide() not implemented yet")
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
