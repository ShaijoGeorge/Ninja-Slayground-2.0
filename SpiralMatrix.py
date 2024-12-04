from typing import List
def spiralMatrix(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    res=[]
    t,b=0,len(matrix)-1
    l,r=0,len(matrix[0])-1
    while t<=b and l<=r:
        res.extend(matrix[t][l:r+1])
        t+=1
        for i in range(t,b+1):
            res.append(matrix[i][r])
        r-=1
        if t<=b:
            res.extend(matrix[b][l:r+1][::-1])
            b-=1
        if l<=r:
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1    
    return res

"""
Problem statement
You are given a 2D matrix ‘MATRIX’ of ‘N’*’M’ dimension. You have to return the spiral traversal of the matrix.

Example:
Input:
MATRIX = [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60] ]
Output:
1 3 5 7 20 60 34 30 23 10 11 16
Explanation: Starting from the element in the first row and the first column, traverse from left to right (1 3 5 7), then top to bottom (20 60), then right to left (34 30 23), then bottom to up (10) and then left to right (11 16).

Sample Input 1:
3 3
1 3 7
10 12 15
19 20 21
Sample Output 1:
1 3 7 15 21 20 19 10 12
Explanation Of Sample Input 1:

Input:
MATRIX = [ [1, 3, 7], [10, 12, 15], [19, 20, 21] ], 
Output:
1 3 7 15 21 20 19 10 12
Explanation: Starting from the element in the first row and the first column, traverse from left to right (1 3 7), then top to bottom (15 21), then right to the left (20 19), then bottom to up (10) and then left to right (12).

Sample Input 2:
4 4
1 5 9 13
14 15 16 17
19 20 21 50
59 60 71 80
Sample Output 2:
1 5 9 13 17 50 80 71 60 59 19 14 15 16 21 20

"""