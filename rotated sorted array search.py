# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0
"""

class Solution:
    def binSearch(self,A,n):
        start = 0
        end = len(A) - 1
        while(start<= end):
            mid = (start + end) // 2
            if(A[mid] == n):
                return mid
            elif(A[mid]>=n):
                end = mid - 1
            else:
                start = mid + 1
        return -1
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        sortedA = list(A[:])
        sortedA.sort()
        a = self.binSearch(sortedA,B)
        if(a == -1):
            return -1
        diff = self.binSearch(sortedA,A[0])
        return (a - diff)%len(A)
s = Solution()
print(s.search([4,5,6,7,0,1,2],4))