from typing import List
def findMaxConsecutiveOnesBruteForce(nums: List[int]) -> int:
    maxLength = 0
    for left in range(len(nums)):
        num_zeros = 0
        for right in range(left, len(nums)):
            if num_zeros == 2:
                break
            if nums[right] == 0:
                num_zeros += 1
            if num_zeros <= 1:
                maxLength = max(maxLength, right - left + 1)
    return maxLength

# Sliding Window Approach
def findMaxConsecutiveOnesOptimum(nums: List[int]) -> int:
    maxLength = 0
    left, right = 0, 0
    zeroes = 0
    while right < len(nums):
        if nums[right] == 0:
            zeroes += 1
        while zeroes == 2:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        maxLength = max(maxLength, right - left + 1)
        right += 1
    return maxLength

nums = [1,0,1,1,0]
nums1 = [1,0,1,1,0,1]
print(findMaxConsecutiveOnesBruteForce(nums))
print(findMaxConsecutiveOnesBruteForce(nums1))
print(findMaxConsecutiveOnesOptimum(nums))
print(findMaxConsecutiveOnesOptimum(nums1))