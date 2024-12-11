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


@pytest.mark.parametrize(
    ("skus", "expected"),
    [
        ("", 0),
        ("A", 50),
        ("AA", 100),
        ("AAA", 130),
        ("AAAAA", 200),
        ("B", 30),
        ("BB", 45),
        ("C", 20),
        ("CC", 40),
        ("D", 15),
        ("DD", 30),
        ("ABCD", 115),
        ("AAABBCD", 210),
        ("EE", 80),
        ("BEE", 80),
        ("BBEE", 110),
        ("BBBEE", 125),
    ],
)
def test_checkout(skus: str, expected: int) -> None:
    result = checkout_solution.checkout(skus)

    assert result == expected

