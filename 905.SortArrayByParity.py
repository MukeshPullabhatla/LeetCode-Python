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
# Second Approach
def sortArrayByParitySecond(nums):
    even, odd = [], []
    for i in range(len(nums)):
        if nums[i]%2==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    return even+odd

# Optimal Approach
def sortArrayByParityOptimal(nums):
    left, right = 0, len(nums)-1
    while left<right:
        if nums[left]%2==1 and nums[right]%2==0:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left]%2==0:
            left+=1
        if nums[right]%2==1:
            right-=1
    return nums

nums = [3,1,2,4]
nums1 = [0]
print(sortArrayByParity(nums))
print(sortArrayByParity(nums1))
print(sortArrayByParitySecond(nums))
print(sortArrayByParitySecond(nums1))
print(sortArrayByParityOptimal(nums))
print(sortArrayByParityOptimal(nums1))