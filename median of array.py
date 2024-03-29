# -*- coding: utf-8 -*-
"""
Median of Array
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            A,B,n,m = B,A,m,n
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin<=imax:
            i = (imax + imin) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0  and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_left = B[j-1]
                elif j == 0: max_left = A[i-1]
                else:
                    max_left = max(A[i-1],B[j-1])
                if (m+n)%2 == 1:
                    return max_left
                if i == m: max_right = B[j]
                elif j == n: max_right = A[i]
                else:
                    max_right = min(B[j],A[i])
                return (max_left+max_right)/2.0
s = Solution()
s.findMedianSortedArrays([1,4,5],[2,3])