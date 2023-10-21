from typing import List
def containsNearByDuplicate(nums: List[int], k: int)->bool:
    val = {}
    for i, num in enumerate(nums):
        if num in val and abs(i-val[num])<=k:
            return True
        else:
            val[num] = i
    return False

nums = [1,2,3,1]
k = 3
nums1 = [1,0,1,1]
k1 = 1
nums2 = [1,2,3,1,2,3]
k2 = 2
print(containsNearByDuplicate(nums, k))
print(containsNearByDuplicate(nums1, k1))
print(containsNearByDuplicate(nums2, k2))