
## https://leetcode.com/problems/two-sum/
## Difficulty = Easy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hash = {}
        for i in range(n):
            num1 = nums[i]
            num2 = target - num1
            if num2 in hash:
                return [hash[num2], i]
            hash[num1] = i

## test
Solution().twoSum(nums = [2,7,11,15], target = 9)
Solution().twoSum(nums = [3,2,4], target = 6)
Solution().twoSum(nums = [3,3], target = 6)


## guidance
# n1 + n2 = target <=> n2 = target - n1
# use hash table to store n1 and its index information
# if target - n1 in hash table, then target - n1 is the solution
# the time complexity is O(n)
# the space complexity is O(n)
