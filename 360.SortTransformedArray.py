from typing import List
def sortTransformedArray(nums: List[int], a: int, b: int, c: int) -> List[int]:
    arr = []
    for i in range(len(nums)):
        x = 0
        x = (a*nums[i]*nums[i])+(b*nums[i])+c
        arr.append(x)
    return sorted(arr)

nums = [-4,-2,2,4]
a = 1
b = 3
c = 5
nums1 = [-4,-2,2,4]
a1 = -1
b1 = 3
c1 = 5
print(sortTransformedArray(nums, a, b, c))
print(sortTransformedArray(nums1, a1, b1, c1))