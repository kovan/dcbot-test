class Calculator:
    """A simple calculator."""

    def add(self, a, b):
        """Calculates the nth Fibonacci number.

        Args:
            n: A non-negative integer representing the position in the Fibonacci sequence.

        Returns:
            An integer representing the nth Fibonacci number.

        Raises:
            None
        """
        return a + b

    def subtract(self, a, b):
        """Determine whether a given number is prime.

        Args:
            n: An integer to check for primality.

        Returns:
            A boolean value indicating whether the number is prime (True) or not (False).

        Raises:
            TypeError: If n is not an integer.
        """
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers.

        Args:
            a: The first number to multiply.
            b: The second number to multiply.

        Returns:
            The product of a and b.
        """

        """Divides two numbers.

        Args:
            a: The dividend.
            b: The divisor.

        Returns:
            The quotient of a divided by b.

        Raises:
            ValueError: If b is zero.
        """

        """Calculates the nth Fibonacci number.

        Args:
            n: The position in the Fibonacci sequence.

        Returns:
            The nth Fibonacci number.
        """

        """Check if a number is prime.

        Args:
            n: The number to check.

        Returns:
            True if n is a prime number, False otherwise.
        """
        return a * b

    def divide(self, a, b):
        """Divides two numbers.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float: The result of dividing a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def fibonacci(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    """Calculates the factorial of a non-negative integer using recursion.

    Args:
        n: A non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n as an integer.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n <= 1:
        return 1
    return n * factorial(n - 1)