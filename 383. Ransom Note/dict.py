
# https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        maga_note = {}
        for note in magazine:
            try:
                maga_note[note] = maga_note[note] + 1
            except:
                maga_note[note] = 1
        for note in ransomNote:
            try:
                maga_note[note] = maga_note[note] - 1
                if maga_note[note] < 0:
                    return False
            except:
                maga_note[note] = -1
                return False
        return True

## test
Solution().canConstruct(ransomNote = 'a', magazine = 'b')
Solution().canConstruct(ransomNote = 'aa', magazine = 'ab')
Solution().canConstruct(ransomNote = 'aa', magazine = 'aab')


## guidance
# save magazine characters into dictionary, if ransomnote contains the corresponding character, then minus value
# if the dictionary value becomes -1, it means some character in ransomnote is more than magazine
# the time complexity is O(m), m is the longer character
# the space complexity is O(1), actually O(k), k <= 26
