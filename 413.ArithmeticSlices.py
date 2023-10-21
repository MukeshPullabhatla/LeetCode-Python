from typing import List
def numberOfArithmeticSlices(nums: List[int]) -> int:
    count = 0
    curr = 0
    for i in range(2, len(nums)):
        if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
            curr+=1
            count+=curr
        else:
            curr = 0
    return count
nums = [1,2,3,4]
nums1 = [1,3,5,7,9]
nums2 = [1]
print(numberOfArithmeticSlices(nums))
print(numberOfArithmeticSlices(nums1))
print(numberOfArithmeticSlices(nums2))