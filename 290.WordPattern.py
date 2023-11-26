def wordPattern(pattern: str, s: str) -> bool:
    map_char = {}
    map_word = {}

    words = s.split(' ')
    if len(words) != len(pattern):
        return False
    for c, w in zip(pattern, words):
        if c not in map_char:
            if w in map_word:
                return False
            else:
                map_char[c] = w
                map_word[w] = c
        else:
            if map_char[c] != w:
                return False
    return True
pattern = "abba"
s = "dog cat cat dog"
pattern1 = "abba"
s1 = "dog cat cat fish"
pattern2 = "aaaa"
s2 = "dog cat cat dog"
print(wordPattern(pattern, s))
print(wordPattern(pattern1, s1))
print(wordPattern(pattern2, s2))