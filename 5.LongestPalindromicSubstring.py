def longestPalindrome(s:str)->str:
    def check(i, j):
        left = i
        right = j-1
        while left<right:
            if s[left] != s[right]: return False
            left+=1
            right-=1
        return True
    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            if check(start, start + length):
                return s[start:start+length]
    return ""

# Brute Force Approach O(n2)
def longestPalindrome1(s: str)->str:
    if len(s) <= 1:
        return s
    length = 1
    string = s[0]
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if j-i+1>length and s[i:j+1] == s[i:j+1][::-1]:
                length = j-i+1
                string = s[i:j+1]
    return string

s = "babad"
s1 = "cbbd"
print(longestPalindrome(s))
print(longestPalindrome(s1))
print(longestPalindrome1(s))
print(longestPalindrome1(s1))