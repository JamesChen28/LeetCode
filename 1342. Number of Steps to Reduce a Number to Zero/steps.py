
## https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while num !=0 :
            if num == 1:
                num = num - 1
                step = step + 1
            elif num % 2 == 0:
                num = num / 2
                step = step + 1
            else:
                num = num - 1
                step = step + 1
        return step
    
## test
Solution().numberOfSteps(14)
Solution().numberOfSteps(8)
Solution().numberOfSteps(123)


## guidance
# use while to break when num = 0
# the time complexity is O(logn)
# the space complexity is O(1)
