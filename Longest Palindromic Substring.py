# -*- coding: utf-8 -*-
"""
Longest Palindromic Substring
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        maxlen = 1
        start = 0
        low = 0
        high = 0
        for i in range(1,n):
            low = i - 1
            high = i
            while(low>=0 and high<n and A[low]==A[high]):
                if high - low + 1 > maxlen:
                    start = low
                    maxlen = high - low + 1
                low = low - 1
                high = high + 1
            low = i-1
            high = i+1
            while(low >= 0 and high<n and A[low] == A[high]):
                if(high - low + 1 > maxlen):
                    start = low
                    maxlen = high - low + 1
                low = low - 1
                high = high + 1
        return A[start:start + maxlen]
s = Solution()
print(s.longestPalindrome("abb"))