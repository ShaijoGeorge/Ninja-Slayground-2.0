import math
def isPrime(n:int) -> bool:
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

"""
Problem statement
A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.
You are given a number 'n'.
Find out whether 'n' is prime or not.

Example :
Input: 'n' = 5
Output: YES
Explanation: 5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.

Sample Input 1:
5
Sample Output 1:
YES
Explanation of sample input 1 :
5 is only divisible by 1 and 5. 2, 3 and 4 do not divide 5.

Sample Input 2:
6
Sample Output 2:
NO
Explanation of sample input 2 :
6 is divisible by 1, 2, 3, and 6. Therefore it is not a prime number.
Numbers having more than two factors are known as composite numbers.

Sample Input 3:
1
Sample Output 3:
NO
Explanation of sample input 3 :
1 is divisible only by 1, having only one factor. Therefore it is not a prime number.
1 is neither a prime nor a composite number.

Expected time complexity :
The expected time complexity is O(sqrt('n')).

"""