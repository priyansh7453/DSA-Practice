#print Square pattern 
def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
# Output:
square(5)