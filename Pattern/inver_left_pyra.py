# Print Left aligned inverted pyramid of the triangle
def invert_left_pyramid(n):
    for i in range(n):
        # Loop for spaces
        for j in range(i):
            print(" ", end="")
        # Loop for stars
        for j in range(n - i):
            print("*", end="")
        # Move to the next line
        print() 
# Output:
invert_left_pyramid(5)