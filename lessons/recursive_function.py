"""In-Class, November 18, 2024."""


def factorial(n: int) -> int:
    """Calculates and returns the factorial of n."""

    if type(n) is not int or n < 0:
        raise ValueError("Invalid input!")

    if n == 0:
        return 1
    else:
        # we have already accounted for negative and nonint n's, so
        # this else case only works for integers n >= 1.
        product: int = n * factorial(n - 1)
        return product
