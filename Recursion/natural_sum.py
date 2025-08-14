# print the sum of natural numbers from 1 to n using recursion
def natural_sum(n):
    if n <= 0:
        return 0
    return n + natural_sum(n - 1)


# Example usage:
print(natural_sum(10))  # Output: 55
