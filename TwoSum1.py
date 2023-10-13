def twoSum(nums, target):
    val = {}
    for i, num in enumerate(nums):
        if num in val:
            return val[num], i
        else:
            val[target-num]=i

def twoSumBruteForce(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                return i, j

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
print(twoSumBruteForce(nums, target))