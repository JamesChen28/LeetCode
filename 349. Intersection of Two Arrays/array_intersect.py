
## https://leetcode.com/problems/intersection-of-two-arrays/
## Difficulty = Easy

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)

## test
Solution().intersection(nums1 = [1, 2, 2, 1], nums2 = [2, 2])
Solution().intersection(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4])


## guidance
# use set() to distinct values in nums
# the time complexity is O(mn)
# the space complexity is O(m+n)
