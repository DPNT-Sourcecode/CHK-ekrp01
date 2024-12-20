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
        ("AAAAABBBEE", 325),
        ("F", 10),
        ("FF", 20),
        ("FFF", 20),
        ("BEEFFF", 100),
        ("G", 20),
        ("H", 10),
        ("HHHHH", 45),
        ("HHHHHHHHHH", 80),
        ("I", 35),
        ("J", 60),
        ("K", 70),
        ("KK", 120),
        ("L", 90),
        ("M", 15),
        ("N", 40),
        ("NNNM", 120),
        ("NNNMM", 135),
        ("O", 10),
        ("P", 50),
        ("PPPPP", 200),
        ("Q", 30),
        ("QQQ", 80),
        ("R", 50),
        ("RRRQ", 150),
        ("RRRQQ", 180),
        ("RRRQQQQ", 230),
        ("S", 20),
        ("T", 20),
        ("U", 40),
        ("UUU", 120),
        ("UUUU", 120),
        ("V", 50),
        ("W", 20),
        ("X", 17),
        ("Y", 20),
        ("Z", 21),
        ("SSS", 45),
        ("STX", 45),
        ("XYZ", 45),
        ("SSSS", 65),
        ("TTTT", 65),
        ("XXXX", 62),
        ("YYYY", 65),
        ("ZZZZ", 66),
        ("ZSSTTTTXXX", 152),
    ],
)
def test_checkout(skus: str, expected: int) -> None:
    result = checkout_solution.checkout(skus)

    assert result == expected


