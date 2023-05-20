def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(gcd(24, 36))  # Output: 12
