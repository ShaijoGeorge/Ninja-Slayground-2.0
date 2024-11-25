from typing import *
def reverseArray(n: int, nums: List[int]) -> List[int]:
    return nums[::-1]
    pass

"""
Problem statement
Given an array 'arr' of size 'n'.

Return an array with all the elements placed in reverse order.

Note:
You don’t need to print anything. Just implement the given function.

Example:
Input: n = 6, arr = [5, 7, 8, 1, 6, 3]
Output: [3, 6, 1, 8, 7, 5]
Explanation: After reversing the array, it looks like this [3, 6, 1, 8, 7, 5].

Sample Input 1:
8
3 1 1 7 4 2 6 11
Sample Output 1:
11 6 2 4 7 1 1 3    
Explanation Of Sample Input 1 :
After reversing the array, it looks like this [11, 6, 2, 4, 7, 1, 1, 3].

Sample Input 2:
4
8 1 3 2
Sample Output 2:
2 3 1 8
Explanation Of Sample Input 2 :
After reversing the array, it looks like this [2, 3, 1, 8].

The expected time complexity is O(n).

"""