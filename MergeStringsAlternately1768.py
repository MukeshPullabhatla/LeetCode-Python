def mergeAlternately(word1, word2) -> str:
    word = ""
    i = 0
    while i<len(word1) or i<len(word2):
        if i<len(word1):
            word += word1[i]
        if i<len(word2):
            word += word2[i]
        i+=1
    return word

word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))
