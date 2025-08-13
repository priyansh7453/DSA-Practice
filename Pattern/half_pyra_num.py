# print the half pyramid of the triangle using numbers
def half_pyramid_num(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        print()
        
        
# Output:
half_pyramid_num(5)