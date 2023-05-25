
## https://leetcode.com/problems/hamming-distance/
## Difficulty = Easy

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        str_x = format(x, 'b')
        str_y = format(y, 'b')
        len_x = len(str_x)
        len_y = len(str_y)
        
        if len_x < len_y:
            str_x = '0' * (len_y - len_x) + str_x
        elif len_y < len_x:
            str_y = '0' * (len_x - len_y) + str_y
        
        count = 0
        for i in range(len(str_x)):
            if str_x[i] != str_y[i]:
                count = count + 1
        
        return count

## test
Solution().hammingDistance(x = 1, y = 4)
Solution().hammingDistance(x = 3, y = 1)


## guidance
# use format(x, 'b') or bin(x) to get binary string
# use XOR concept (x^y in python) to count different
# integer n takes log_2(n) bits to write
# the time complexity is O(log(n))
# the space complexity is O(1)
