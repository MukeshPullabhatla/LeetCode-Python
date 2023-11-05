from typing import List
def findMaxConsecutiveOnesBruteForce(nums: List[int]) -> int:
    maxLength = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] == 0:
                break
            maxLength = max(maxLength, j - i + 1)
    return maxLength

# Sliding Window Approach
def findMaxConsecutiveOnesOptimum(nums: List[int]) -> int:
    maxCount = count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
    return max(maxCount, count)

nums = [1,1,0,1,1,1]
nums1 = [1,0,1,1,0,1]
print(findMaxConsecutiveOnesBruteForce(nums))
print(findMaxConsecutiveOnesBruteForce(nums1))
print(findMaxConsecutiveOnesOptimum(nums))
print(findMaxConsecutiveOnesOptimum(nums1))