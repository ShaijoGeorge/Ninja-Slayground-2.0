from typing import List
def getFrequencies(v: List[int]) -> List[int]: 
    freq = {}
    for num in v:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    min_freq = min(freq.values())
    max_freq_element = min(k for k, v in freq.items() if v == max_freq)
    min_freq_element = min(k for k, v in freq.items() if v == min_freq)
    return [max_freq_element, min_freq_element]

"""
Problem statement
Given an array 'v' of 'n' numbers.
Your task is to find and return the highest and lowest frequency elements.
If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.

Example:
Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]
Output: 1 2
Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].

Sample Input 1 :
6
1 2 3 1 1 4
Sample Output 1 :
1 2
Sample Explanation 1:
Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]
Output: 1 2
Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].

Sample Input 2 :
6
10 10 10 3 3 3
Sample Output 2 :
3 3
Sample Explanation 2:
Input: ‘n' = 6, 'v' = [10, 10, 10, 3, 3, 3]
Output: 3 3

Explanation: Since the frequency of '3' and '10' is 3. Therefore, the element with the maximum and minimum frequency is '3'.

The expected time complexity is O(n), where n is the size of the array.

"""