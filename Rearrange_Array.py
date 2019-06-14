# -*- coding: utf-8 -*-
'''Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]'''

# @param A : list of integers
def hd(A):
  n = len(A)
  for i in range(0,n):
      A[i] = A[i] + (A[A[i]]%n)*n
  for i in range(0,n):
      A[i] = A[i]/n
  return A
print(hd([ 6, 4, 3, 2, 5, 1, 7, 0 ]))