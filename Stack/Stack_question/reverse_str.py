# Reverse a string using stack in Python

str_in = "Priyansh Kushwaha"
s = []  

# Push each character to stack
for ch in str_in:
    s.append(ch)

ans = ""
while s:
    ch = s[-1]       # Top of stack
    ans += ch        # Add to answer
    s.pop()          # Remove from stack

print("answer is:", ans)
