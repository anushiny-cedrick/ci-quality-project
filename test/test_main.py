#

import pytest
from app.main import add, subtract, multiply, divide, is_even, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(5, 0)


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
