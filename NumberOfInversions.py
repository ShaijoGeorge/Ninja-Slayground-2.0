from typing import List
def numberOfInversions(a: List[int], n: int) -> int:
    def merge_sort_and_count(arr, temp, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        inversions = merge_sort_and_count(arr, temp, left, mid)
        inversions += merge_sort_and_count(arr, temp, mid + 1, right)
        inversions += merge_and_count(arr, temp, left, mid, right)
        return inversions
    def merge_and_count(arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        inversions = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inversions += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]
        return inversions
    temp = [0] * n
    return merge_sort_and_count(a, temp, 0, n - 1)

"""
Problem statement
There is an integer array ‘A’ of size ‘N’.
Number of inversions in an array can be defined as the number of pairs of ‘i’, ‘j’ such that ‘i’ < ‘j’ and ‘A[i]’ > ‘A[j]’.
You must return the number of inversions in the array.
For example,
Input:
A = [5, 3, 2, 1, 4], N = 5
Output:
7
Explanation: 
The pairs satisfying the condition for inversion are (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), and (3, 4). 
The number of inversions in the array is 7.

Sample Input 1:
4
4 3 2 1
Sample Output 1:
6
Explanation Of Sample Input 1:
Input:
A = [4, 3, 2, 1], N = 4
Output:
6
Explanation: 
The pairs satisfying the condition for inversion are (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), and (3, 4).    
The number of inversions in the array is 6.

Sample Input 2:
5
1 20 6 4 5
Sample Output 2:
5

"""