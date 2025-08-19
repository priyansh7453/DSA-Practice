# Python Code to swap two numbers using arithmetic operators

# if __name__ == "__main__":
# 	a = 2
# 	b = 3
# 	print("a =", a, " b =", b)
    
# 	a = a + b
# 	b = a - b
# 	a = a - b
    
# 	print("a =", a, " b =", b)

def swap_without_thirdvar(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
# Test the function
if __name__ == "__main__":
    a = 2
    b = 3
    print("Before swap: a =", a, "b =", b)
    
    a, b = swap_without_thirdvar(a, b)
    
    print("After swap: a =", a, "b =", b)