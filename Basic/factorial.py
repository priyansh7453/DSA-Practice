# factorial of the number n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage
n = 6
print(factorial(n))  # Output: 120