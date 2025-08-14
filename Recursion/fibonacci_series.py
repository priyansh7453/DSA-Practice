# Print the fabonacci series using recursion
# def fibonacci(n):
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # print(n)
    # return fibonacci(n - 1) + fibonacci(n - 2)
# Print the Fibonacci series using recursion

def print_fibonacci_series(n, a=0, b=1, count=0):
    if count >= n:
        return
    print(a, end=" ")
    print_fibonacci_series(n, b, a + b, count + 1)
    
    
# Recursive function to get nth Fibonacci number
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Function to print Fibonacci sequence
def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

# Example: print first 10 terms
n_terms = int(input("Enter number of terms: "))
print_fibonacci(n_terms)

