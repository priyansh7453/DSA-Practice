# Two sum 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the
# same element twice.
# You can return the answer in any order.
def two_sum(arr, target):
    # arr.sort()
    # left, right = 0, len(arr) - 1
    # while left < right:
    #     current_sum = arr[left] + arr[right]
    #     if current_sum == target:
    #         return [left, right]
    #     elif current_sum < target:
    #         left += 1
    #     else:
    #         right -= 1
            
    # return []  # If no solution found
    
    s = set()
    
    for i in range(len(arr)):
        com = target - arr[i]
        if com in s:
            return [arr.index(com), i]
        
        s.add(arr[i])
    return []  # If no solution found
        
# Example usage
arr = [2, 7, 5,]
target = 9
print(two_sum(arr, target))  # Output: [0, 1] (indices of elements 2 and 7)