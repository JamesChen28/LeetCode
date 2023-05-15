
## https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 1 + Solution().climbStairs(n = 1)
        if n >= 3:
            return Solution().climbStairs(n = (n-1)) + Solution().climbStairs(n = (n-2))


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = []
        for i in range(1, n+1):
            if i == 1:
                record.append(i)
                # return record[n-1]
            if i == 2:
                record.append(i)
                # return record[n-1]
            if i >= 3:
                record.append(record[i-2] + record[i-3])
        return record[n-1]

## test
Solution().climbStairs(n = 2)
Solution().climbStairs(n = 3)


## guidance
# instead using recursion method
# use dynamic list to store earlier computation data
# iterate all list data to get the fianl value
# the time complexity is O(n)
# the space complexity is O(1)
