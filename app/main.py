#
# def add(a, b):
#     """Return the sum of two numbers."""
#     return a + b


# def subtract(a, b):
#     """Return the difference of two numbers."""
#     return a - b


# def multiply(a, b):
#     """Return the product of two numbers."""
#     return a * b


# def divide(a, b):
#     """Return the division of two numbers. Raises ZeroDivisionError if b is zero."""
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b


# def is_even(n):
#     """Return True if n is even, else False."""
#     return n % 2 == 0


# def factorial(n):
#     """Return the factorial of n. Raises ValueError if n is negative."""
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# app/main.py

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide a by b. Returns float. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0
