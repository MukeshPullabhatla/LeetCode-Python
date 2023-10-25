from collections import defaultdict


def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    if k > 26: return 0
    ans = 0
    n = len(s)
    left = right = 0
    freq = [0]*26
    def getVal(ch: str)->int:
        return ord(ch) - ord('a')
    while right < n:
        freq[getVal(s[right])]+=1
        while freq[getVal(s[right])]>1:
            freq[getVal(s[left])]-=1
            left+=1
        if right - left + 1 == k:
            ans += 1
            freq[getVal(s[left])]-=1
            left+=1
        right+=1
    return ans

s = "havefunonleetcode"
k = 5
s1 = "home"
k1 = 5
print(numKLenSubstrNoRepeats(s, k))
print(numKLenSubstrNoRepeats(s1, k1))
