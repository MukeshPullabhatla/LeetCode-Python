from typing import List
def maxDistance(arrays: List[List[int]]) -> int:
    i,j = arrays[0][-1], arrays[0][0]
    mdif = float('-inf')
    for array in arrays[1::]:
        x,y = i,j
        i = max(i,array[-1])
        j = min(j,array[0])
        mdif = max(mdif,array[-1]-y)
        mdif = max(mdif, x-array[0])
    return mdif
arrays = [[1,2,3],[4,5],[1,2,3]]
print(maxDistance(arrays))