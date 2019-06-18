'''
Count And Say
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A == 1:
            return '1'
        if A == 2:
            return '11'
        currstr = '11'
        for i in range(2,A):
            j = 0
            n = len(currstr)
            prev = currstr[0]
            newstr = ''
            count = 0
            #print(j,n)
            while(j<n):
                #print(prev,currstr[j])
                if(prev == currstr[j]):
                    count = count + 1
                else:
                    newstr = newstr + str(count) + '' + prev
                    count = 1
                prev = currstr[j]
                j = j + 1
            newstr = newstr + str(count) + '' + prev
            currstr = newstr
        return currstr
s = Solution()
print(s.countAndSay(5))