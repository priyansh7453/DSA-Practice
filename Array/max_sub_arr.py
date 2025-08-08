# Maximum subarray 
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

def max_sub_array(nums):
    res = nums[0]
    # Maximum sum of subarray ending at current position
    maxEnding = nums[0]
    for i in range(1, len(nums)):
        # Either extend the previous subarray or start 
        # new from current element
        maxEnding = max(maxEnding + nums[i], nums[i])
        
        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)
    return res
    
    # res = nums[0]  
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, len(nums)):
    #         sum += nums[j]
    #         res = max(res, sum)
    # return res


# Example usage
nums = [2, 3, -8, 7, -1, 2, 3]
print(max_sub_array(nums))  # Output: 6 (subarray [4,-1,2,1] has the largest sum)