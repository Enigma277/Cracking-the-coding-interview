def rotate(mat : list[list[int]]) -> list[list[int]] :
    for layer in range(0, len(mat)//2) :
        first , last = layer, len(mat) - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = mat[first][first+offset]

            mat[first][first+offset] = mat[last - offset][first] #top <- left
            mat[last - offset][first] = mat[last][last-offset]   #left <- bottom
            mat[last][last-offset] = mat[first + offset][last]   #bottom <- right
            mat[first+offset][last] = top   #right <- top                                        
    
    return mat

#Testing our function
'''
1 2 3       7 4 1 
4 5 6   ->  8 5 2
7 8 9       9 6 3
'''
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(mat))