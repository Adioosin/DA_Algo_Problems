#power implementation with O(logn)

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        res = 1 % d  # Cover case d == 1
        while n > 0:
            if n & 1:   # Odd?
               res = (res * x) % d
            x = x**2 % d
            n >>= 1
        return res
s = Solution()
print(s.pow(3,4,7))

