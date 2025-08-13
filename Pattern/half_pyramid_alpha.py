# Print the half pyramid of the triangle using alphabets
def half_pyramid_alpha(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end="")
        print()
# Output:
# half_pyramid_alpha(5)

print(chr(97), end="")