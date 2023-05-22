
## https://leetcode.com/problems/merge-sorted-array/
## Difficulty = Easy

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if (m == 0) & (nums1[m] == 0):
                nums1[m+n-1] = nums2[n-1]
                n = n-1
            if (nums1[m-1] <= nums2[n-1]) & (m >= 1):
                nums1[m+n-1] = nums2[n-1]
                n = n-1
            if (nums1[m-1] > nums2[n-1]) & (m >= 1):
                nums1[m+n-1], nums1[m-1] = nums1[m-1], nums1[m+n-1]
                m = m-1
        return nums1

## test
Solution().merge(nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3)
Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0)
Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)


## guidance
# compare nums1 and nums2 from the last elements, move the larger element to the last of nums1
# use len(nums2) = n to control while condition, if n becomes 0 means all elements in nums2 are sorted in nums1
# len(nums1) = m = 0 and nums1[0] = 0 is the special case, just move nums2[0] to nums1[0]
# the time complexity is O(m+n)
# the space complexity is O(1)
