# Reverse the String 
def reverse_string(s):
    # return s[::-1]
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
        print(char,end="")
        print("----")
        print(reversed_s,end="")
        
    return reversed_s



# Test the function
print(reverse_string("Ankush"))  
