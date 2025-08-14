# print the 1 to 10 number by without loop
def print_1_to_10(n=0):
    if n >= 10:
        return
    print(n)
    print_1_to_10(n + 1)
    
# Example usage:
print_1_to_10()  # Output: 1 to 10 printed on separate lines