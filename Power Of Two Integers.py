# -*- coding: utf-8 -*-
"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 
"""
import math

def isPower(n):
    if (n==1)  : 
        return 1
    # Try all numbers from 2 to sqrt(n) as base 
    for x in range(2,(int)(math.sqrt(n))+1) : 
        y = 2
        p = (int)(math.pow(x, y)) 
        # Keep increasing y while power 'p' is smaller 
        # than n.  
        while (p<=n and p>0) : 
            if (p==n) : 
                return 1
              
            y = y + 1
            p = math.pow(x, y) 
    return 0
print(isPower(1024000000))