from solutions.HLO import hello_solution


def test_hello() -> None:
    result = hello_solution.hello("John")

    assert result == "Hello, John!"
