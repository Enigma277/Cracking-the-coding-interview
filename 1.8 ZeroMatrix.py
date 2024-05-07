def ZeroMatrix(mat : list[list[int]]) -> list[list[int]] :
    zeroRow = [False] * len(mat)
    zeroCol = [False] * len(mat[0])

    for i in range(len(mat)) :
        for j in range(len(mat[i])) :
            if(mat[i][j] == 0) :
                zeroCol[j] = True
                zeroRow[i] = True
    
    for i in range(len(mat)) :
        for j in range(len(mat[i])):
            if(zeroRow[i] or zeroCol[j]):
                mat[i][j] = 0
    
    return mat

#Testing our function

'''
1 2 3 4    1 0 3 0
5 0 7 8 -> 0 0 0 0
4 5 6 0    0 0 0 0
7 1 2 5    7 0 2 0 
'''
mat = [[1, 2, 3, 4], [5, 0, 7, 8], [4, 5, 6, 0], [7, 1, 2, 5]]

print(ZeroMatrix(mat))