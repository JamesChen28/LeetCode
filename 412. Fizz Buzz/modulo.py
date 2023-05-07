
## https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(n):
            if (i+1) % 15 == 0:
                l.append('FizzBuzz')
            elif (i+1) % 3 == 0:
                l.append('Fizz')
            elif (i+1) % 5 == 0:
                l.append('Buzz')
            else:
                l.append(str(i+1))
        return l

## test
Solution().fizzBuzz(3)
Solution().fizzBuzz(5)
Solution().fizzBuzz(15)


## guidance
# use if/else stetement to mod 15/5/3 condition
# the time complexity is O(n)
# the space complexity is O(1)
