##Remove Duplicate element from string
def remove_duplicates(s):
    ans = ""
    
    for char  in s:
        if char not in ans:
            ans += char
    return ans

# Test the function
print(remove_duplicates("Ankussshhhhh"))  # Output: "Ankush"
    
    