from typing import List
def moveZeroes(nums: List[int]) -> None:
    index = 0
    for num in nums:
        if num!=0:
            nums[index]=num
            index+=1
    while index<len(nums):
        nums[index] = 0
        index+=1
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))
nums1 = [0,1,0,2,0,3,0,4,0,5,0,6,7]
print(moveZeroes(nums1))