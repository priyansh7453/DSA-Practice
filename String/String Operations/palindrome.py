## palindrome = "madam"

def is_palindrome(s):
    # return s == s[::-1]
    
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
        # return True   
    return True
# Example usage
s = "madam"
print(is_palindrome(s))  # Output: True

