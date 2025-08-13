# # print the inverted pyramid of the triangle 
# def invert_pyramid(n):
#     for i in range(n):
#         for j in range(n - i - 1):
#             print(" ", end="")
#         for j in range(2 * i + 1):
#             print("*", end="")
#         print()
# # Output:
# invert_pyramid(5)

def invert_pyramid(n):
    for i in range(n):
        # Loop for spaces
        for j in range(i):
            print(" ", end="")
        # Loop for stars
        for j in range(2 * (n - i) - 1):
            print("*", end="")
        # Move to the next line
        print()
# Output:
invert_pyramid(5)
