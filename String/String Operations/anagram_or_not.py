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

def is_anagram(st1,st2):
    s1 = st1.lower()
    s2 = st2.lower()
    if len(s1) == len(s2):
        if sorted(s1)==sorted(s2):
            return True
        else:
            return False


s1 = "anA"
s2 = "aaN"  
print(is_anagram(s1,s2))