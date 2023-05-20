def find_max(numbers):
    """
    Returns the maximum number in a list of numbers.
    """
    max_num = float('-inf')  # Start with negative infinity as the maximum
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage:
numbers = [3, 5, 1, 9, 2]
print(find_max(numbers))  # Output: 9
