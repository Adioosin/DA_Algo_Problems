# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:45:39 2019

@author: ednisai
"""

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(A)
        if(n==1):
            return d[A]
        prev = A[-1]
        total = 0
        for i in range(n-1,-1,-1):
            #print(A[i])
            if d[prev]>d[A[i]]:
                total = total - d[A[i]]
            else:
                total = total + d[A[i]]
            prev = A[i]
        return total
s = Solution()
print(s.romanToInt('MDCCCIV'))