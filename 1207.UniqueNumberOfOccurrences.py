from typing import List
def uniqueOccurrences(arr: List[int]) -> bool:
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    freqSet = set(freq.values())
    return len(freq) == len(freqSet)


arr = [1,2,2,1,1,3]
arr1 = [1,2]
arr2 = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))
print(uniqueOccurrences(arr1))
print(uniqueOccurrences(arr2))