# Print the numbers from 10 to 1 using recursion
def print_10_to_1(n=10):
    if n < 1:
        return
    print(n)
    print_10_to_1(n - 1)
    
# Example usage:
print_10_to_1()  # Output: 10 to 1 printed on separate lines