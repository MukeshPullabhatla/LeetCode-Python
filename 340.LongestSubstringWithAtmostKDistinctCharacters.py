from collections import defaultdict


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    if n<k: return n
    left, right = 0, 0
    maxLength = k
    m = defaultdict()
    while right<n:
        m[s[right]] = right
        right += 1
        if len(m)>k:
            i = min(m.values())
            del m[s[i]]
            left = i+1
        maxLength = max(maxLength, right-left)
    return maxLength
s = "eceba"
k = 2
s1 = "aa"
k1 = 1
print(lengthOfLongestSubstringKDistinct(s, k))
print(lengthOfLongestSubstringKDistinct(s1, k1))