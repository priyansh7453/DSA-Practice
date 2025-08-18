def solve(s, x):
    # base case
    if not s:
        s.append(x)
        return
    
    num = s.pop()
    
    # recursive call
    solve(s, x)
    
    s.append(num)

def push_at_bottom(my_stack, x):
    solve(my_stack, x)
    return my_stack


# Example usage:
stack = [1, 2, 3, 4]  # top is at the end of the list
print("Original stack:", stack)

push_at_bottom(stack, 100)
print("Stack after pushing 0 at bottom:", stack)
