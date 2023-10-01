"""API for solving problem Reverse Integer"""

X_MAX = 2**31 - 1
X_MIN = -(2**31)


def _check_preconditions(x: int) -> bool:
    return X_MIN <= x <= X_MAX


def reverse_integer(x: int) -> int:
    """Solves problem Reverse Integer"""

    assert _check_preconditions(x)

    pass
