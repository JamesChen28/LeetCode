
## https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
## Difficulty = Easy

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str 
        :rtype: int
        """
        hash_chars = {}
        for char in chars:
            if char not in hash_chars.keys():
                hash_chars[char] = 1
            else:
                hash_chars[char] = hash_chars[char] + 1
        good = 0
        for i in range(len(words)):
            hash_chars_copy = hash_chars.copy()
            word_good = 0
            for word in words[i]:
                if word not in hash_chars_copy.keys():
                    break
                if (word in hash_chars_copy.keys()) & (hash_chars_copy[word] == 0):
                    break
                if (word in hash_chars_copy.keys()) & (hash_chars_copy[word] > 0):
                    hash_chars_copy[word] = hash_chars_copy[word] - 1
                word_good = word_good + 1
            if word_good == len(words[i]):
                good = good + word_good
        return good

## test
Solution().countCharacters(words = ['cat', 'bt', 'hat', 'tree'], chars = 'atach')
Solution().countCharacters(words = ['hello', 'world', 'leetcode'], chars = 'welldonehoneyr')


## guidance
# use hash table to store chars' information
# examine words' characters respectively to check whether characters are all in hash table
# use break to ignore for loop when character is not in hash table or character's count is more than hash table
# the time complexity is O(n)
# the space complexity is O(1)
