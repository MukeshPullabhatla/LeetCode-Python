from typing import List
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    n = len(nums1)
    m = len(nums2)
    x = []
    for i in range(0,n):
        x.append(nums1[i])
    for i in range(0,m):
        x.append(nums2[i])
    x.sort()
    k = len(x)
    if k%2==0:
        return float(x[(k-1)//2]+x[(k+1)//2])/2
    else:
        return x[k//2]

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))
nums3 = [1,2]
nums4 = [3,4]
print(findMedianSortedArrays(nums3, nums4))