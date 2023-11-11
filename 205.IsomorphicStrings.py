def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    mapStoT = {}
    mapTtoS = {}
    for charInS, charInT in zip(s, t):
        if charInS in mapStoT:
            if mapStoT[charInS] != charInT:
                return False
        else:
            mapStoT[charInS] = charInT

        if charInT in mapTtoS:
            if mapTtoS[charInT] != charInS:
                return False
        else:
            mapTtoS[charInT] = charInS
    return True

s = "egg"
t = "add"
s1 = "foo"
t1 = "bar"
s2= "paper"
t2 = "title"
print(isIsomorphic(s, t))
print(isIsomorphic(s1, t1))
print(isIsomorphic(s2, t2))