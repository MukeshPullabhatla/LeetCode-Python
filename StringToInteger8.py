def myAtoi(s:str) -> int:
    value, state, pos, sign = 0, 0, 0, 1
    if len(s) == 0:
        return 0
    while pos<len(s):
        curr_char = s[pos]
        if state == 0:
            if curr_char == " ":
                state = 0
            elif curr_char == "+" or curr_char == "-":
                state = 1
                sign = 1 if curr_char == "+" else -1
            elif curr_char.isdigit():
                state = 2
                value = value * 10 + int(curr_char)
            else:
                return 0
        elif state == 1:
            if curr_char.isdigit():
                state = 2
                value = value * 10 + int(curr_char)
            else: return 0
        elif state == 2:
            if curr_char.isdigit():
                state = 2
                value = value * 10 + int(curr_char)
            else:
                break
        else:
            return 0
        pos += 1
    value = sign*value
    value = min(value, 2**31-1)
    value = max(-(2**31), value)

    return value
s = "42"
s1 = "-42"
s2 = "4193 with words"
print(myAtoi(s))
print(myAtoi(s1))
print(myAtoi(s2))