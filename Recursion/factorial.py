# Factorial of the number using recursion
def factorial(n):
    if n ==  0 or n == 1:
        return 1
    chotti_problem = factorial(n - 1)
    badi_problem = n * chotti_problem        
    return badi_problem
    # return n * factorial(n - 1)


# Example usage:
print(factorial(5))  # Output: 120