from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2): return False
    word1Map = {}
    word2Map = {}
    for c in word1:
        word1Map[c] = word1Map.get(c, 0) + 1
    for c in word2:
        word2Map[c] = word2Map.get(c, 0) + 1
    if set(word1Map.keys()) != set(word2Map.keys()): return False
    word1Frequency = sorted(word1Map.values())
    word2Frequency = sorted(word2Map.values())
    return word1Frequency == word2Frequency
def closeStrings1(word1: str, word2: str) -> bool:
    w1 = Counter(word1)
    w2 = Counter(word2)
    n1 = Counter([v for v in w1.values()])
    n2 = Counter([v for v in w2.values()])
    return w1 == w2 or (n1 == n2 and set(word1) == set(word2))

word1 = "abc"
word2 = "bca"
word3 = "a"
word4 = "aa"
word5 = "cabbba"
word6 = "abbccc"
print(closeStrings(word1, word2))
print(closeStrings(word3, word4))
print(closeStrings(word5, word6))
print(closeStrings1(word1, word2))
print(closeStrings1(word3, word4))
print(closeStrings1(word5, word6))
