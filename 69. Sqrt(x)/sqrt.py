
## https://leetcode.com/problems/sqrtx/
## Difficulty = Easy

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left = int('1' + '0' * (len(str(x)) // 2 - 1))
        right = x
        while left < right:
            mid = left + (right-left) // 2
            if mid == x/mid:
                return mid
            elif (mid < x/mid) & ((mid + 1) > x/(mid + 1)):
                return mid
            elif mid < x/mid:
                left = mid + 1
            else:
                right = mid
        return left

## test
Solution().mySqrt(x = 4)
Solution().mySqrt(x = 8)
Solution().mySqrt(x = 2147395599)


## guidance
# sqrare root of n-digits number is (n/2 - 1) to (n/2) digit
# set left and right pointers to compress square root range (binary search)
# use x/mid instead mid*mid to avoid runtime error
# the time complexity is O(logn)
# the space complexity is O(1)
