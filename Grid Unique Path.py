# -*- coding: utf-8 -*-
"""
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
"""

# @param A : integer
# @param B : integer
# @return an integer
def uniquePaths(A, B):
    dp = [1 for i in range(B)] 
    for i in range(A - 1): 
        for j in range(1, B): 
            dp[j] += dp[j - 1] 
    return dp[B - 1]
print(uniquePaths(3,3))