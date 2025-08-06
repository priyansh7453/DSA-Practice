def get_repeated_chars(s):
    char_count = {}
    
    # Step 1: Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Collect characters that appear more than once
    repeated = {}
    for char, count in char_count.items():
        if count > 1:
            repeated[char] = count
    return repeated
# Example usage
s = "programming"
print(get_repeated_chars(s))  # Output: {'g': 2, 'm': 2, 'r': 2}