def sortArrayByParity(nums):
    if len(nums)<=1:
        return nums
    res = []
    for i, num in enumerate(nums):
        if num%2==0:
            res.append(num)
    for i, num in enumerate(nums):
        if num%2!=0:
            res.append(num)
    return res

nums = [3,1,2,4]
nums1 = [0]
print(sortArrayByParity(nums))
print(sortArrayByParity(nums1))