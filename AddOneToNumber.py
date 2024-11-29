from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    n=len(arr)
    c=1
    for i in range(n-1,-1,-1):
        if c==0:
            break
        d=arr[i]+c
        if d<10:
            arr[i]=d
            c=0
        else:
            arr[i]=0
            c=1
    if c==1:
        arr.insert(0,1)
    while len(arr)>1 and arr[0]==0:
        arr.pop(0)
    return arr

"""
Problem statement

Given a non-negative number represented as an array of digits, you have to add 1 to the number, i.e, increment the given number by one.

The digits are stored such that the most significant digit is at the starting of the array and the least significant digit is at the end of the array.

For Example
If the given array is {1,5,2}, the returned array should be {1,5,3}.

Note
Input array can contain leading zeros, but the output array should not contain any leading zeros (even if the input array contains leading zeroes).

For Example: 
If the given array is {0,2}, the returned array should be {3}.

Where Arr[i] is the i-th digit in the number.

Sample Input 1
3
3
1 2 3
2
9 9
1
4
Sample Output 1
1 2 4
1 0 0
5
Explanation For Sample Input 1
In the 1st test case, the number is 123 after adding 1 number becomes 124, hence the output will be {1,2,4}.

In the 2nd test case, the number is 99 after adding 1 number becomes 100, hence the output will be {1,0,0}.

In the 3rd test case, the number is 4 after adding 1 number becomes 5, hence the output will be {5}.


Sample Input 2
3
4
2 4 6 8 
1
0
2
0 2
Sample Output 2
2 4 6 9
1
3

"""