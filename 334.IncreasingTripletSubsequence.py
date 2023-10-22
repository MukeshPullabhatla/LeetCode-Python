from typing import List
def increasingTriplet(nums: List[int]) -> bool:
    first = second = float('inf')
    for num in nums:
        if num<=first:
            first = num
        elif num<=second:
            second = num
        else:
            return True
    return False
nums = [1,2,3,4,5]
nums1 = [5,4,3,2,1]
nums2 = [2,1,5,0,4,6]
print(increasingTriplet(nums))
print(increasingTriplet(nums1))
print(increasingTriplet(nums2))