# Sort the stack 

def sorted_insert(stack, num):
    # Base case: stack empty or num greater than the top, just push
    if not stack or stack[-1] < num:
        stack.append(num)
        return

    n = stack.pop()
    # Recursive call
    sorted_insert(stack, num)
    stack.append(n)

def sort_stack(stack):
    # Base case: if stack is empty, return
    if not stack:
        return

    num = stack.pop()
    # Recursive call
    sort_stack(stack)
    sorted_insert(stack, num)

# Example usage:
stack = [5, 3, 2, -4, 1]  # top is at rightmost
print("Original stack:", stack)
sort_stack(stack)
print("Sorted stack (top at right):", stack)
