"""API for solving problem Reverse Integer"""

X_MAX = 2**31 - 1
X_MIN = -(2**31)


def _check_preconditions(x: int) -> bool:
    return X_MIN <= x <= X_MAX


def reverse_integer(x: int) -> int:
    """Solves problem Reverse Integer"""

    assert _check_preconditions(x)

    sign = 1 if x == abs(x) else -1
    x = abs(x)

    y = 0
    while x > 0:
        y = y * 10 + (x % 10)
        x = x // 10

    return sign * y
