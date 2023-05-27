
## https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
## Difficulty = Easy

class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_letters = set(s)
        hash_map = {}
        for v in set_letters:
            for letter in set_letters - set(v):
                if v.isupper():
                    if (v.lower() == letter) & (len(list(hash_map.values())) == 0):
                        hash_map[v] = ord(v)
                    elif (v.lower() == letter) & (len(list(hash_map.values())) > 0):
                        if (ord(v) > list(hash_map.values())[0]):
                            del hash_map[chr(list(hash_map.values())[0])]
                            hash_map[v] = ord(v)
                elif v.islower():
                    if (v.upper() == letter) & (v.upper() not in hash_map.keys()) & (len(list(hash_map.values())) == 0):
                        hash_map[v.upper()] = ord(v.upper())
                    elif (v.upper() == letter) & (v.upper() not in hash_map.keys()) & (len(list(hash_map.values())) > 0):
                        if (ord(v.upper()) > list(hash_map.values())[0]):
                            hash_map[v.upper()] = ord(v.upper())
        if len(list(hash_map.keys())) == 0:
            return ''
        else:
            return list(hash_map.keys())[0]

## test
Solution().greatestLetter(s = 'lEeTcOdE')
Solution().greatestLetter(s = 'arRAzFif')
Solution().greatestLetter(s = 'AbCdEfGhIjK')


## guidance
# use set to distinct string and use hash map to record letter and its value
# use ord(s) to compare letters order
# i don't want to use sort(), so i use two for loop to enumerate, only record the largest letter in hash map
# i think there are tow ways to improve
# first is after 'for letter in set_letters - set(v):', determine ord(letter) < hash_map.values(), then stop this letter iteration
# since smaller letter do not need to determine if the larger letter has both upper and lowwer case
# second is after 'for letter in set_letters - set(v):', determine letter.upper() in hash_map.keys(), then stop this letter iteration
# since the letter in hash_map must has its upper and lower case in the latter, this latter case  do not need to determine
# the time complexity is O(n^2), if use sort() then the time complexity is O(nlogn)
# the space complexity is O(1)
