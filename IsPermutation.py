# Given N=5, it means an original array of [1, 2, 3, 4, 5].
# I’ll give you another random array, for example [5, 2, 1, 3, 4].
# Tell me if it is a permutation of the original array. If yes, return true, else return false.
def is_permutation(orgArr, ranArr):

    element_set = set(orgArr)

    for element in ranArr:
        if element not in element_set:
            return False

    return True

# Example usage:
orgArr = [1, 2, 3, 4, 5]
ranArr = [5, 2, 1, 3, 4]

ranArr1 = [2,3,1,4]
ranArr2 = [0,3,3,4]
ranArr3 = [0,1,2,4,5,6]
# N=4, [2, 3, 1, 4] true [0, 3, 3, 4] false
# N=6, [0, 1, 2, 4, 5, 6] false

result = is_permutation(orgArr, ranArr)
result1 = is_permutation(orgArr, ranArr1)
result2 = is_permutation(orgArr, ranArr2)
result3 = is_permutation(orgArr, ranArr3)
print(result)
print(result1)
print(result2)
print(result3)