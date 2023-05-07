
## https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            nums[i+1] = nums[i+1] + nums[i]
        return nums

## test
Solution().runningSum(nums = [1,2,3,4])
Solution().runningSum(nums = [1,1,1,1,1])
Solution().runningSum(nums = [3,1,2,10,1])


## guidance
# the new value with index [i] is sum of index [i-1] plus index [i]
# the first position value doesn't need to change
# so from index [1] to traverse all index
# the time complexity is O(n)
# the space complexity is O(1)
