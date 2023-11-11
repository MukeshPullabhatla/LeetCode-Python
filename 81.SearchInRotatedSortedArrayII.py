from typing import List
def search(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[left] == nums[mid]:
            left += 1
            continue
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
    return False
nums = [2,5,6,0,0,1,2]
target = 0
nums1 = [1,0,1,1,1]
target1 = 0
print(search(nums, target))
print(search(nums1, target1))