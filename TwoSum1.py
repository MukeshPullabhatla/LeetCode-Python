def twoSum(nums, target):
    val = {}
    for i, num in enumerate(nums):
        if num in val:
            return val[num], i
        else:
            val[target-num]=i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))