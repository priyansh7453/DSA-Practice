# Print the number of sum of digit using  recursion
# def sum_of_digit(n):
#     sum = 0
#     while(n > 0):
#         rem = n % 10
#         sum += rem
#         n = n // 10
#     return sum
# print(sum_of_digit(3331))  # Output: 10

def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(n // 10)

# Example usage:
print(sum_of_digit(3331))  # Output: 10