# find two array is equal or not
def two_array_equal(arr1, arr2):    
    if len(arr1) != len(arr2):
        return False
    # for i in range(len(arr1)):
    #     if arr1[i] != arr2[i]:
    #         return False
    # return True
    
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if sorted(arr1) == sorted(arr2):
        return True
    return False

# Example usage
arr1 = [1, 2, 3, 4, 10]
arr2 = [1, 4, 10, 2, 3]
print(two_array_equal(arr1, arr2))  # Output: True
