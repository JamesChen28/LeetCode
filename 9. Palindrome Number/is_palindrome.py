
## https://leetcode.com/problems/palindrome-number/
## Difficulty = Easy

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False
        else:
            return False

## test
Solution().isPalindrome(x = 121)
Solution().isPalindrome(x = -121)
Solution().isPalindrome(x = 10)


## guidance
# x[::-1] is the reverse string of string x
# check x[::-1] equal to x or not
# the time complexity is O(n)
# the space complexity is O(1)
