"""
Main application module containing basic arithmetic and utility functions.
"""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """
    Return the quotient of two numbers.

    Raises:
        ValueError: If division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def is_even(n: int) -> bool:
    """Return True if the number is even, False otherwise."""
    return n % 2 == 0
