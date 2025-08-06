def count_vowels_and_consonants(str):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in str:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
            
    return vowel_count, consonant_count

# Example usage
str = "Hello, World!"
vowel_count, consonant_count = count_vowels_and_consonants(str)
print("Vowel Count:", vowel_count)
print("Consonant Count:", consonant_count)
            

# print(str.isalpha())  # Output: True
# print(str.isdigit())  # Output: False
# print(str.isalnum())  # Output: True

