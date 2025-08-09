# Reverse the words in a string
def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    return ' '.join(reversed_words)

result = reverse_words("Hello World from OpenAI")
print(result)  # Output: "OpenAI from World Hello"
