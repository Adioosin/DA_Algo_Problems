# -*- coding: utf-8 -*-
"""
The given number is power of two or not
"""

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A==1:
            return 0
        if(A and (not(A & (A - 1))) ):
            return 1
        else:
            return 0
s = Solution()
print(s.power('512'))