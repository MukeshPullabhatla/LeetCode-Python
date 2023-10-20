def kthFactor(n:int, k:int) -> int:
    res = []
    for i in range(1, n):
        if n%i==0:
            res.append(i)
    res.append(n)
    if len(res)>=k:
        return res[k-1]
    else:
        return -1
n = 12
k = 3
n1 = 7
k1 = 2
n2 = 4
k2 = 4
print(kthFactor(n, k))
print(kthFactor(n1, k1))
print(kthFactor(n2, k2))