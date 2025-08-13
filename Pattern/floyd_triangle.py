# Print the floyd traingle 
def floyd_triangle(n):
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()
        
#output:
floyd_triangle(5)