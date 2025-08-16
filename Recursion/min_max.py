# find the min and max of a list using recursion
def find_min_max(arr, n, min_val=float('inf'), max_val=float('-inf  ')):
    if n == 0:
        return min_val, max_val
    
    if arr[n - 1] < min_val:
        min_val = arr[n - 1]
    
    if arr[n - 1] > max_val:
        max_val = arr[n - 1]
    
    return find_min_max(arr, n - 1, min_val, max_val)

print(find_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5], 9))  # Output: (1, 9)