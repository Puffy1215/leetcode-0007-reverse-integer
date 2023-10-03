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


def _posstep(x: int, y: int) -> tuple[int, int]:
    if y > X_MAX // 10:
        return 0, 0
    y = y * 10

    m = _posmod(x)
    if X_MAX - y < m:
        return 0, 0

    y = y + m
    x = _posdiv(x)

    return x, y


def _negstep(x: int, y: int) -> tuple[int, int]:
    if y < (X_MIN + 9) // 10:
        return 0, 0
    y = y * 10

    m = _negmod(x)
    if y - X_MIN < m:
        return 0, 0

    y = y + m
    x = _negdiv(x)

    return x, y


def reverse_integer(x: int) -> int:
    """Solves problem Reverse Integer"""

    assert _check_preconditions(x)

    step = _posstep if x > 0 else _negstep

    y = 0
    while x != 0:
        x, y = step(x, y)

    return y
