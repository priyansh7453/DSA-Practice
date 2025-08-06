# 🧠 When to Use What?
# ✅ Use sort() → When you want to modify the list in-place

# ✅ Use sorted() → When you want to keep the original data and get a new sorted version

list1 = ['a', 'n', 'a']
list1.sort()
print(list1)  # Output: ['a', 'a', 'n']
# ---------------------------
arr = [3, 1, 4, 2]
new_arr = sorted(arr)
print(new_arr)  # Output: [1, 2, 3, 4]
print(arr)      # Original remains: [3, 1, 4, 2]

#             <--------------------------------->

def is_anagram(s1,s2):
    if len(s1) == len(s2):
        return True
    elif sorted(s1)==sorted(s2):
        return True
    else:
        return False


s1 = "ana"
s2 = "aab"  
print(is_anagram(s1,s2))