def longestCommonPrefix(arr):
    if not arr:
        return ""
    arr.sort()
    first, last = arr[0], arr[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]
# Example usage
arr = ["flower", "flow", "flight"]
print(longestCommonPrefix(arr))  # Output: "fl"
# Example usage with an empty list
arr_empty = []
print(longestCommonPrefix(arr_empty))  # Output: ""
# Example usage with no common prefix
arr_no_prefix = ["dog", "racecar", "car"]
print(longestCommonPrefix(arr_no_prefix))  # Output: ""