def is_valid_parenthesis(expression):
    stack = []
    
    for ch in expression:
        # If opening bracket, push to stack
        if ch in ['(', '{', '[']:
            stack.append(ch)
        else:
            # For closing bracket
            if stack:
                top = stack[-1]
                if (ch == ')' and top == '(') or (ch == '}' and top == '{') or (ch == ']' and top == '['):
                    stack.pop()
                else:
                    return False
            else:
                return False

    # If stack is empty at the end, parentheses are balanced
    return len(stack) == 0

# Example usage:
# expr = "{(a+b)*[c-d]}"
expr = "{{[()]}}"
print(is_valid_parenthesis(expr))  # Output: True

expr2 = "{(a+b]*[c-d)}"
print(is_valid_parenthesis(expr2))  # Output: False
