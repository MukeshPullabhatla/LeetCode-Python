from typing import List
def arrayRankTransform(arr: List[int]) -> List[int]:
    d = {}
    nums = sorted(set(arr))
    for i in range(len(nums)):
        d[nums[i]] = i + 1
    for i in range(len(arr)):
        arr[i] = d[arr[i]]
    return arr

arr = [40,10,20,30]
arr1 = [100,100,100]
arr2 = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr))
print(arrayRankTransform(arr1))
print(arrayRankTransform(arr2))