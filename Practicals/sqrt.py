def sqrt(num):
    """
    Returns the square root of a number using Newton's method.
    """
    guess = num / 2  # Start with an initial guess of half the input number
    while True:
        new_guess = (guess + num / guess) / 2  # Compute the new guess
        if abs(new_guess - guess) < 0.0001:  # Check for convergence
            return new_guess
        guess = new_guess

# Example usage:
print(sqrt(16))  # Output: 4.0

