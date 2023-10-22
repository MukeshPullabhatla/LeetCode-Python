def reverseWords(s:str)->str:
    s = s.split()
    return " ".join(s[::-1])
def reverseWords1(s:str)->str:
    n = len(s)  # Get the length of the input string
    ans = []  # Initialize a list to store the reversed words
    i = n - 1  # Start from the last character of the input string

    while i >= 0:
        if s[i] == ' ':
            i -= 1  # If the current character is a space, move to the next character
        else:
            temp = [' ']  # Initialize a temporary list with a space character
            j = i
            while j >= 0 and s[j] != ' ':
                temp.append(s[j])  # Append each character to the temporary list in reverse order
                j -= 1
            ans.extend(reversed(temp))  # Reverse the characters in the temporary list and append to the final list
            i = j  # Update the index to continue from the next word

    ans.pop()  # Remove the extra space character appended at the end

    return ''.join(ans)  # Return the reversed words as a string
s = "the sky is blue"
s1 = "  hello world  "
s2 = "a good   example"
print(reverseWords(s))
print(reverseWords(s1))
print(reverseWords(s2))
print(reverseWords1(s))
print(reverseWords1(s1))
print(reverseWords1(s2))