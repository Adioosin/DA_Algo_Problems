# -*- coding: utf-8 -*-
"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""

# @param A : string
# @return an integer
def fact(n):
    return 1 if n==0 or n==1 else n * fact(n-1)

def findRank(A):
    #l = A.split()
    #l.sort()
    rank = 1
    n = len(A)
    for i in range(0,n-1):
        count = 0
        for j in range(i+1,n):
            if(A[j]<A[i]):
                count = count +1
        rank = rank + count * fact(n-i-1)
    return rank%1000003

print(findRank('HELO'))