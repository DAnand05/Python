def power(base, exponent):
    """
    Returns the result of raising a base to a given exponent.
    """
    result = 1
    for i in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    else:
        return result

# Example usage:
print(power(2, 3))  # Output: 8
print(power(5, -2))  # Output: 0.04

'''
base=int(input("Enter the base: "))
exp=int(input("Enter the exponent: "))

res=1
for i in range(abs(exp))
    res*=base
if exp < 0:
    print(1/res)
else:
    print(res)
'''