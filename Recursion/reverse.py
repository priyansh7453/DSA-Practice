## Reverse the number using recursion
def reverse_number(n, reversed_num=0):
    while(n!=0):
        rem = n % 10
        reversed_num = reversed_num * 10 + rem
        n = n // 10
    return reversed_num
    
print(reverse_number(123))