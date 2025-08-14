# Print the power of 2 using recursion
def power_of_2(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 1
    chotti_problem = power_of_2(n - 1)
    badi_problem = 2 * chotti_problem
    # return 2 * power_of_2(n - 1)
    return badi_problem
# Example usage:
print(power_of_2(5))  # Output: 32