# Print half Pyramid of the traingle
def half_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
# Output:
half_pyramid(5)
    