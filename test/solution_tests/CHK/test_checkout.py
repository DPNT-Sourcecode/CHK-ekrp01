from typing import Any

import pytest
from solutions.CHK import checkout_solution


@pytest.mark.parametrize(
    ("skus", "expected"),
    [
        ("1", -1),
        (1, -1),
        ("-", -1),
        (None, -1),
        ("A1B", -1),
    ],
)
def test_checkout_invalid(skus: Any, expected: int) -> None:
    result = checkout_solution.checkout(skus)

    assert result == -1

