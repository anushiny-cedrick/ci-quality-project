"""
Calculator utility module.

Provides basic arithmetic operations with input validation.
"""

from typing import Union

Number = Union[int, float]


def _validate_numbers(a: Number, b: Number) -> None:
    """
    Validate that inputs are numbers.

    :param a: First number
    :param b: Second number
    :raises TypeError: If inputs are not numeric
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric values")


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    _validate_numbers(a, b)
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of two numbers."""
    _validate_numbers(a, b)
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    _validate_numbers(a, b)
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Return the division of two numbers.

    :raises ValueError: If division by zero is attempted
    """
    _validate_numbers(a, b)
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def is_even(number: int) -> bool:
    """
    Check if a number is even.

    :param number: Integer to check
    :return: True if even, False otherwise
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0
