"""
Problem statement:
Programming languages have some conditional / decision-making statements that execute when some specific condition is fulfilled.

Switch-case is one of the ways to implement them.

In a menu-driven program, the user is given a set of choices of things to do (the menu) and then is asked to select a menu item.

There are 2 choices in the menu:
Choice 1 is to find the area of a circle having radius 'r'.
Choice 2 is to find the area of a rectangle having dimensions 'l' and 'b'.

You are given the choice 'ch' and an array 'a'.

If ‘ch’ is 1, ‘a’ contains a single number ‘r’. If ‘ch’ is 2, ‘a’ contains 2 numbers, ‘l’ and ‘b’.

Consider the choice and print the appropriate area.

Example :
Input: ‘ch’ = 2 and ‘a’ = [3, 2]
Output: area = 6
Explanation: Since the choice ‘ch’ is 2, we have to print the area of the rectangle having ‘l’ = 3 and ‘b’ = 2, which is 6.


Sample Input 1:
2
3 2

Sample Output 1:
6.00000

Explanation of sample input 1 :
Since the choice ‘ch’ is 2, we have to print the area of the rectangle having ‘l’ = 3 and ‘b’ = 2, which is 6.


Sample Input 2:
1
3

Sample Output 2:
28.27433

Explanation of sample input 2 :
Since the choice ‘ch’ is 1, we have to print the area of the circle having ‘r’ = 3, which is approximately 28.274333882308138. Rounded off to 5 decimal places, we get 28.27433.

Expected time complexity :
The expected time complexity is O(1).

Constraints :
1 <= ‘ch’ <= 2
1 <= ‘r’ <= 100
1 <= ‘l’, ‘b’ <= 100

Time limit: 1 second

"""

from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    def circleArea():
        r=a[0]
        area=math.pi*r*r
        return "{0:.5f}".format(area)
    def rectangleArea():
        l=a[0]
        b=a[1]
        area=l*b
        return "{0:.5f}".format(area)
    switch={
        1:circleArea,
        2:rectangleArea
    }
    return switch.get(ch)()