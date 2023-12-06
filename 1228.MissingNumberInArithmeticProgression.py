from typing import List
def missingNumber1(arr: List[int]) -> int:
    n = len(arr)
    first = arr[0]
    last = arr[-1]
    sume = 0
    for i in range(n):
        sume += arr[i]
    return ((first + last) * (n + 1)) // 2 - sume
    # return ((first + last) * (n + 1)) // 2 - sum(arr)
def missingNumber1(arr: List[int]) -> int:
    n = len(arr)
    diff = (arr[n-1] - arr[0]) // n
    first = 0
    last = n - 1
    while first < last:
        mid = (first + last) // 2
        if arr[mid] == arr[0] + mid * diff:
            first = mid + 1
        else:
            last = mid
    return arr[0] + diff * first
arr = [5,7,11,13]
arr1 = [15,13,12]
print(missingNumber1(arr))
print(missingNumber1(arr1))
print(missingNumber1(arr))
print(missingNumber1(arr1))