def linear_search(arr, x):
    """
    Perform a linear search on the input list arr to find the value x.
    If x is found in arr, return its index. Otherwise, return -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50]
x = 30
index = linear_search(arr, x)
if index == -1:
    print(f"{x} not found in list")
else:
    print(f"{x} found at index {index}")
