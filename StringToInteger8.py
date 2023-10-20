def myAtoi(s:str) -> int:
    value, state, position, sign = 0, 0, 0, 1
    if len(s) == 0: return 0
    while position<len(s):
        current_character = s[position]
        if state == 0:
            if current_character == " ":
                state = 0
            elif current_character == "+" or current_character == "-":
                state = 1
                sign = 1 if current_character == "+" else -1
            elif current_character.isdigit():
                state = 2
                value = value * 10 + int(current_character)
            else:
                return 0
        elif state == 1:
            if current_character.isdigit():
                state = 2
                value = value * 10 + int(current_character)
            else:
                return 0
        elif state == 2:
            if current_character.isdigit():
                state = 2
                value = value * 10 + int(current_character)
            else:
                break
        else:
            return 0
        position += 1

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