def findDiagonalOrder(mat):
    if not mat or not mat[0]: return []
    n, m = len(mat), len(mat[0])
    result, res = [], []
    for i in range(n+m-1):
        res.clear()
        r = 0 if i<m else i-m+1
        c = i if i<m else m-1
        while r<n and c>-1:
            res.append(mat[r][c])
            r+=1
            c-=1
        if i%2==0: result.extend(res[::-1])
        else: result.extend(res)
    return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
mat1 = [[1,2],[3,4]]
mat2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print(findDiagonalOrder(mat))
print(findDiagonalOrder(mat1))
print(findDiagonalOrder(mat2))