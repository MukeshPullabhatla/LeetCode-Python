from typing import List
def maximumGap(nums: List[int]) -> int:
    if len(nums) < 2: return 0
    nums = sorted(nums)
    maxDiff = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        maxDiff = max(maxDiff, diff)
    return maxDiff
nums = [3,6,9,1]
nums1 = [10]
print(maximumGap(nums))
print(maximumGap(nums1))