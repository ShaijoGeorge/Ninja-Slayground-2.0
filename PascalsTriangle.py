from collections import *
from math import *

def printPascal(n:int):
    triangle=[]
    for i in range(n):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return triangle

"""
Problem statement
You are given an integer N. Your task is to return a 2-D ArrayList containing the pascal’s triangle till the row N.

A Pascal's triangle is a triangular array constructed by summing adjacent elements in preceding rows. Pascal's triangle contains the values of the binomial coefficient. For example in the figure below.

img alt="Array"
        src="https://images.app.goo.gl/PQUqe2vrc2xEzUYQ8" width="540"/>

For example, given integer N= 4 then you have to print.

1  
1 1 
1 2 1 
1 3 3 1

Here for the third row, you will see that the second element is the summation of the above two-row elements i.e. 2=1+1, and similarly for row three 3 = 1+2 and 3 = 1+2.

Sample Input 1 :
3
1
2
3
Sample Output 1 :
1
1 
1 1 
1 
1 1 
1 2 1 
Explanation of The Sample Input 1:
For the first test case:
The given integer N = 1 you have to print the triangle till row 1 so you just have to output 1.

For the second test case:
The given integer N = 2 you have to print the triangle till row 2 so you have to output 
1
1 1

For the third test case
The given integer N = 3 you have to print the triangle till row 3 so you have to output 
1
1 1
1 2 1
Sample Input 2 :
3
4
5
6
Sample Output 2 :
1 
1 1 
1 2 1
1 3 3 1 
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1
1 5 10 10 5 1

"""