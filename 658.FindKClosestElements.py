from typing import List
# Using Custom Comparator
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    sorted_arr = sorted(arr, key = lambda num: abs(x-num))
    result = []
    for i in range(k):
        result.append(sorted_arr[i])
    return sorted(result)

arr = [1,2,3,4,5,6,7,8,9,10]
k = 4
x = 5
print(findClosestElements(arr, k, x))

# Using binary search
def findClosestElements1(arr: List[int], k: int, x: int) -> List[int]:
    left = 0
    right = len(arr) - k
    while left < right:
        mid = (left + right) //2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left+k]
print(findClosestElements1(arr, k, x))