from typing import List
def sumSubArrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1: return 0
    product = 1
    ans = left = 0
    for right, val in enumerate(nums):
        product *= val
        while product >= k:
            product /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
nums = [10,5,2,6]
k = 100
nums1 = [1,2,3]
k1 = 0
print(sumSubArrayProductLessThanK(nums, k))
print(sumSubArrayProductLessThanK(nums1, k1))