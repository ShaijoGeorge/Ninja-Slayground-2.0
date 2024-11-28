def read(n: int, book: [int], target: int) -> str:
    s = set()
    for p in book:
        c = target - p
        if c in s:
            return "YES"
        s.add(p)
    return "NO"

"""
Problem statement

Sam want to read exactly ‘TARGET’ number of pages.
He has an array ‘BOOK’ containing the number of pages for ‘N’ books.

Return YES/NO, if it is possible for him to read any 2 books and he can meet his ‘TARGET’ number of pages.

Example:
Input: ‘N’ = 5, ‘TARGET’ = 5
‘BOOK’ = [4, 1, 2, 3, 1] 
Output: YES
Explanation:
Sam can buy 4 pages book and 1 page book.

Sample Input 1:
5 5
4 1 2 3 1
Sample Output 1 :
YES
Explanation Of Sample Input 1:
Sam can buy 4 pages book and 1-page book.

Sample Input 2:
2 1
1 2
Sample Output 2 :
NO

Expected Time Complexity:
O( N ), Where N is the length of the array.

"""