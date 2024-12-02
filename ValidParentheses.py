def isValidParenthesis(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

"""
Problem statement

You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .

Return true if the given string 'S' is balanced, else return false.

For example:
'S' = "{}()".

There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
So the 'S' is Balanced.

Sample Input 1 :
[()]{}{[()()]()}
Sample Output 1 :
Balanced
Explanation Of the Sample Input 1 :
There is always an opening brace before a closing brace i.e. '{' before '}', '(' before '), '[' before ']'.
So the 'S' is Balanced.

Sample Input 2 :
[[}[
Sample Output 2 :
Not Balanced

"""