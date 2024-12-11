from solutions.HLO import hello_solution


def test_hello() -> None:
    result = hello_solution.hello("Craftsman")

    assert result == "Hello, World!"

