# Find Occurrences of an Element in a List
def count_occurrences(arr, element):
    count = 0
    
    # for i in range(len(arr)):
    #     if arr[i] == element:
    #         count += 1   
    # return count
    
    for i in arr:   
        if i == element:
            count += 1
            
    return count

# Example usage

arr = [1, 2, 2, 3, 4, 2, 5]
element = 2
print(count_occurrences(arr, element))  # Output: 3
