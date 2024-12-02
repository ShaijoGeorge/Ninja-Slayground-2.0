from typing import List
def lowerBound(arr: List[int], n: int, x: int) -> int:
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid   
    return left

"""
Problem statement

You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.

Note:
1. For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'.If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.
2. Try to do this in O(log(n)).

Example:
Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0
Output: 0
Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

Sample Input 1:
6
1 2 2 3 3 5
0
Sample Output 1:
0
Explanation Of Sample Input 1 :
Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

Sample Input 2:
6
1 2 2 3 3 5
2
Sample Output 2:
1

Sample Input 3:
6
1 2 2 3 3 5
7
Sample Output 3:
6

"""