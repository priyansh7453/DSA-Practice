# delete the middle element of a stack
def solve(input_stack, count, size):
    # base case
    if count == size // 2:
        input_stack.pop()
        return
    
    num = input_stack.pop()
    
    # recursive call
    solve(input_stack, count + 1, size)
    
    input_stack.append(num)


def delete_middle(input_stack):
    size = len(input_stack)
    solve(input_stack, 0, size)


# Example usage:
stack = [1, 2, 3, 4, 5]  # bottom -> top : 1 is bottom, 5 is top
print("Original stack:", stack)

delete_middle(stack)

print("Stack after deleting middle element:", stack)
