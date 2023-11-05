from typing import List
def findMaxConsecutiveOnesBruteForce(nums: List[int]) -> int:
    maxLength = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] == 0:
                break
            maxLength = max(maxLength, j - i + 1)
    return maxLength

nums = [1,1,0,1,1,1]
nums1 = [1,0,1,1,0,1]
print(findMaxConsecutiveOnesBruteForce(nums))
print(findMaxConsecutiveOnesBruteForce(nums1))