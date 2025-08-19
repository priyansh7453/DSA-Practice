def insert_at_bottom(s, element):
    # base case
    if not s:
        s.append(element)
        return
    
    num = s.pop()
    
    # recursive call
    insert_at_bottom(s, element)
    
    s.append(num)

def reverse_stack(stack):
    # base case
    if not stack:
        return
    
    num = stack.pop()
    
    # recursive call
    reverse_stack(stack)
    
    insert_at_bottom(stack, num)

# Example usage:
stack = [1, 2, 3, 4]  # top is at the end of the list
print("Original stack:", stack)

reverse_stack(stack)
print("Stack after reversal:", stack)
