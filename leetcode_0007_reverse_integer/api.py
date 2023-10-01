"""API for solving problem Reverse Integer"""

from math import ceil, floor

X_MAX = 2**31 - 1
X_MIN = -(2**31)


def _check_preconditions(x: int) -> bool:
    return X_MIN <= x <= X_MAX


def _posdiv(x: int) -> int:
    assert x >= 0
    return floor(x / 10)


def _negdiv(x: int) -> int:
    assert x <= 0
    return ceil(x / 10)


def _posmod(x: int) -> int:
    assert x >= 0
    return x % 10


def _negmod(x: int) -> int:
    assert x <= 0
    return (x % 10) - 10


def reverse_integer(x: int) -> int:
    """Solves problem Reverse Integer"""

    assert _check_preconditions(x)

    div, mod = (_posdiv, _posmod) if x > 0 else (_negdiv, _negmod)

    y = 0
    while x != 0:
        y = y * 10 + mod(x)
        x = div(x)

    return y
