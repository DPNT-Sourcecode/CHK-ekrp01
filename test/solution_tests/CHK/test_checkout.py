from solutions.CHK import checkout_solution


def test_checkout() -> None:
    result = checkout_solution.checkout("A")

    assert result is None
