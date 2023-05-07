
# https://leetcode.com/problems/richest-customer-wealth/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_number = 0
        sum_i = 0
        for account in accounts:
            sum_i = sum(account)
            if sum_i > max_number:
                max_number = sum_i
        return max_number

## test
Solution().maximumWealth([[1,2,3],[3,2,1]])
Solution().maximumWealth([[1,5],[7,3],[3,5]])
Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]])


## guidance
# sum each account, if sum is larger than max number, then substitute the max number
# the time complexity is O(n x m)
# the space complexity is O(1)
