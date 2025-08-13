# print inversted half pyramid of the triangle
def inver_half_pyramid(n):
    for i in range(n):
        for j in range(n - i ):
            print("*", end="")
        print()
        
# Output:
inver_half_pyramid(5)
