# Print inverted half pyramid of the triangle using numbers
def inver_half_num(n):
    for i in range(n):
        for j in range(n - i):
            print(j + 1, end="")
        print()
# Output:
inver_half_num(5)