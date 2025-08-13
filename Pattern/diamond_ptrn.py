# Print the Diamond pattern
def diamond(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    
    for i in range(1,n):
        # Loop for spaces
        for j in range(i):
            print(" ", end="")
        # Loop for stars
        for j in range(2 * (n - i) - 1):
            print("*", end="")
        # Move to the next line
        print()
        
# Output:
diamond(5)