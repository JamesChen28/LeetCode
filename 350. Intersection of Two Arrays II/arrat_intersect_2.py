
## https://leetcode.com/problems/intersection-of-two-arrays-ii/
## Difficulty = Easy

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        for number in nums2:
            if number in nums1:
                inter.append(number)
                nums1.remove(number)
        return inter

## test
Solution().intersect(nums1 = [1, 2, 2, 1], nums2 = [2, 2])
Solution().intersect(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4])


## guidance
# without considering nums1 and nums2 size, take arbitrary list as base data, W.L.O.G, say nums2
# if number in nums2 appears in nums1, then add this number to final list and remove this number from nums1
# the time complexity is O(m+n)
# the space complexity is O(1)
