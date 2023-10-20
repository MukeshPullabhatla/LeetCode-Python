# 1st approach
def reverse(x):
    flag = -1 if x<0 else 1
    s = str(abs(x))
    x = int(s[::-1])
    return x*flag if x<2**31 else 0
# 2nd approach
def reverse1(x):
    flag = -1 if x<0 else 1
    x = abs(x)
    res = 0
    while x>0:
        digit = x % 10
        res = res * 10 + digit
        x //= 10
    return res * flag
x = 123
x1 = -123
x2 = 120
print(reverse(x))
print(reverse(x1))
print(reverse(x2))
print(reverse1(x))
print(reverse1(x1))
print(reverse1(x2))