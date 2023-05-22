
## https://leetcode.com/problems/remove-element/
## Difficulty = Easy

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            if nums[head] == val:
                nums[head], nums[tail] = nums[tail], nums[head]
                tail = tail - 1
            else:
                head = head + 1
        return head

## test
Solution().removeElement(nums = [3,2,2,3], val = 3)
Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)


## guidance
# record head and tail information, start from head
# swap head and tail if nums[head] equals val
# the time complexity is O(n)
# the space complexity is O(1)
