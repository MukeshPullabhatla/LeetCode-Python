# As per problem statement: You must write an algorithm with O(log n) runtime Complexity
from typing import List
def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
nums = [4,5,6,7,0,1,2]
target = 0
nums1 = [5,1,3]
target1 = 0
print(search(nums, target))
print(search(nums1, target1))