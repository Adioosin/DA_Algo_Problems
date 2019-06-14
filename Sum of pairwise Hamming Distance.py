# -*- coding: utf-8 -*-
"""
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
"""

def hammingDistance(A):
    total = 0
    largest = 0
    ln = len(A)
    A = list(A)
    for i in range(0,ln):
      #b = i[0]^i[1]
      A[i] = bin(A[i])[2:]
      l = len(A[i])
      if(l>largest):
          largest = l
    for i in range(0,ln):
      l = len(A[i])
      if(l<largest):
          A[i] ='0'*(largest-l)+A[i]
    #print(A)
    for i in range(0,largest):
        x = 0
        y = 0
        for j in A:
          if(j[i]=='0'):
            x = x + 1
          else:
            y = y + 1
        total = total + 2 * x * y
    return total%1000000007
print(hammingDistance([2,4,6]))