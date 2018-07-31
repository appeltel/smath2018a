from smath2018a.fib import fib


def test_fib_zero():
    assert fib(0) == 0


def test_fib_eight():
    assert fib(8) == 21
