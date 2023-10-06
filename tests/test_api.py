"""Tests API for solving problem Reverse Integer"""

import pytest

from leetcode_0007_reverse_integer import api


@pytest.mark.parametrize(
    ["result", "x"],
    (
        [321, 123],
        [-321, -123],
        [21, 120],
        [0, api.X_MAX],
        [0, api.X_MIN],
    ),
)
def test_reverse_integer(result: int, x: int) -> None:
    """Tests solution for problem Reverse Integer"""

    assert api.reverse_integer(x) == result
