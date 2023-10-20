def removeKdigits(num: str, k: int) -> str:
    stack = list()
    for n in num:
        while stack and k and stack[-1]>n:
            stack.pop()
            k-=1
        if stack or n is not '0':
            stack.append(n)
    if k:
        stack = stack[0:-k]
    return ''.join(stack) or '0'
num = "1432219"
k = 3
num1 = "10200"
k1 = 1
num2 = "10"
k2 = 2
print(removeKdigits(num, k))
print(removeKdigits(num1, k1))
print(removeKdigits(num2, k2))