
## https://leetcode.com/problems/divisor-game/
## Difficulty = Easy

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def strategy(self, n):
            x = 1
            if (x > 0) & (x < n) & (n % x == 0):
                n = n - x
            return n
        
        A = 0
        while n > 1:
            n = strategy(self, n)
            if A == 0:
                A = 1
            elif A == 1:
                A = 0
        return bool(A)

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = True
        return dp[n]

## test
Solution().divisorGame(n = 2)
Solution().divisorGame(n = 3)


## guidance
# for simplicity, use strategy x = 1 to test
# for optimal strategy, use dynamic programming to record Alice can win or not from n = 1 to large number
# actually if n = 2, then Alice can always win, since Alice can select x = 1
# so when n = 2k (k is any interger), Alice always select x = 1, make new n = 2k - 1
# either Bob select any number, x must be odd, which make new n = 2m (m is any integer)
# therefore, this game result is based on n is odd or even (i.e. n % 2 = 0 or 1)
# n is even (i.e. n % 2 == 0), 
# the time complexity is O()
# the space complexity is O()
