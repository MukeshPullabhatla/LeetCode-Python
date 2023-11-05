from typing import List
def longestOnesBruteForce(nums: List[int], k: int) -> int:
    maxLength = 0
    for i in range(len(nums)):
        zeroes = 0
        for j in range(i, len(nums)):
            if zeroes == k + 1:
                break
            if nums[j] == 0:
                zeroes += 1
            if zeroes <= k:
                maxLength = max(maxLength, j - i + 1)
    return maxLength

# Sliding Window Approach
def longestOnesOptimum(nums: List[int], k: int) -> int:
    maxLength = 0
    i, j = 0, 0
    zeroes = 0
    while j < len(nums):
        if nums[j] == 0:
            zeroes += 1
        while zeroes == k + 1:
            if nums[i] == 0:
                zeroes -= 1
            i += 1
        maxLength = max(maxLength, j - i + 1)
        j += 1
    return maxLength

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
nums1 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k1 = 3
print(longestOnesBruteForce(nums, k))
print(longestOnesBruteForce(nums1, k1))
print(longestOnesOptimum(nums, k))
print(longestOnesOptimum(nums1, k1))