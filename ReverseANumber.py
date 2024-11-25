from typing import List
def reverseNumber(n: int) -> int: 
    rev=0
    while n>0:
        digit=n%10
        rev=digit+rev*10
        n=n//10
    return rev

"""
Problem statement
You are given a number 'n'.

Return an integer that is the reverse of ‘n’.

Note:
Reverse of ‘n’ means an integer where, the most significant digit of ‘n’ is the least significant digit of the number, the second most significant digit of ‘n’ is the second least significant digit of the number and so on.

Example:
Input: 'n' = 123
Output: 321
Explanation:
Reverse of 'n' = 123 is 321.


Sample Input 1:
34
Sample Output 1:
43
Explanation of sample output 1:
Reverse of ‘n’ = 34 is 43.

Sample Input 2:
121
Sample Output 2:
121

Expected Time Complexity:
Try to solve this in O(log(n)) 

Expected Space Complexity:
Try to solve this in O(1) 

"""