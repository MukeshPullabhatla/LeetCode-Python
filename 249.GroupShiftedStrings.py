from typing import List
def groupStrings(strings: List[str]) -> List[List[str]]:
    d = {}
    for s in strings:
        t = tuple((ord(s[i + 1]) - ord(s[i]) % 26 for i in range(len(s) - 1)))
        if t in d:
            d[t].append(s)
        else:
            d[t] = [s]
    return list(d.values())
strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(groupStrings(strings))