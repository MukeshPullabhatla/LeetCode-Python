from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1]*n
    pre = 1
    post = 1
    for i in range(n): #i = 3
        res[i]*=pre # 1 1 2 6
        pre*=nums[i] # pre = 24
        res[n-i-1]*=post # 24 12 4 1
        post*=nums[n-i-1] # 96

    return res
nums = [1,2,3,4]
nums1 = [-1,1,0,-3,3]
print(productExceptSelf(nums))
print(productExceptSelf(nums1))