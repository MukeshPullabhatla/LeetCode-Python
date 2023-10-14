# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once.
#
# Return the single element that appears only once.

from collections import Counter

def singleNonDuplicate(nums):
    res = Counter(nums)
    for key, value in res.items():
        if value == 1:
            return key
# Time Complexity:
#
# Creating the Counter object using Counter(nums) takes O(n) time, where n is the length of the input list nums.
# This is because it iterates through the entire list to count the occurrences of each element.
# The subsequent loop through the elements in the Counter object takes O(n) time as well,
# as it iterates through the unique elements in the list (which can be at most n/2 unique elements,
# given that there's only one non-duplicate element).
# Inside the loop, checking if value == 1 is a constant-time operation because the values in the Counter object are already computed.
# So, the overall time complexity of this program is O(n).
#
# Space Complexity:
#
# The primary space usage comes from the Counter object, which stores the counts of unique elements in the nums list. In the worst case, where there are n/2 unique elements (all duplicates except for one), the space complexity is O(n/2), which simplifies to O(n).
# In summary, the time complexity of the program is O(n), and the space complexity is O(n).


#To achieve O(logn) time complexity for finding the single non-duplicate element in a sorted array,
#you can use binary search.
def singleNonDuplicatesOptimum(nums):
    left, right = 0, len(nums)-1

    while left<right:
        mid = left + (right-left) // 2
        if mid%2 == 1:
            mid -= 1
        if nums[mid] == nums[mid+1]:
            left = mid+2
        else:
            right = mid
    return nums[left]

# we perform a binary search on the even indices of the array.
# The key idea is to always keep the mid index as an even number and compare nums[mid]
# with nums[mid + 1. If they are equal, it means the single non-duplicate element
# is on the right side, so we update the left pointer. If they are not equal,
# it means the single non-duplicate element is on the left side, so we update the right pointer.
#
# This algorithm has a time complexity of O(log n) because with each iteration,
# the size of the search space is effectively halved

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))

nums1 = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums1))
print(singleNonDuplicatesOptimum(nums1))
