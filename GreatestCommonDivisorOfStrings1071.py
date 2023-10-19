from math import gcd
def gcdOfStrings1(str1, str2):
    if str1+str2!=str2+str1: return ""
    return str1[:gcd(len(str1), len(str2))]
str1 = "ABCABC"
str2 = "ABC"
str3 = "ABABAB"
str4 = "ABAB"
str5 = "LEET"
str6 = "CODE"
print(gcdOfStrings1(str1, str2))
print(gcdOfStrings1(str3, str4))
print(gcdOfStrings1(str5, str6))
