
## https://leetcode.com/problems/time-needed-to-buy-tickets/
## Difficulty = Easy

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] = tickets[i] - 1
                    time = time + 1
                    if tickets[k] == 0:
                        break
        return time

## test
Solution().timeRequiredToBuy(tickets = [2, 3, 2], k = 2)
Solution().timeRequiredToBuy(tickets = [5, 1, 1, 1], k = 0)


## guidance
# use while to stop iteration when ticket = 0 for person k
# use break to stop iteration if ticket = 0 for person k but k is not the last person to avoid counting more
# the time complexity is O(n)
# the space complexity is O(1)
