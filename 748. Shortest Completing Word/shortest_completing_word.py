
## https://leetcode.com/problems/shortest-completing-word/
## Difficulty = Easy

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # use hash_plate dict to store licensePlate information
        hash_plate = {}
        for letter in licensePlate.replace(' ', '').lower():
            if letter in hash_plate.keys():
                hash_plate[letter] = hash_plate[letter] + 1
            else:
                hash_plate[letter] = 1
        # use len_list to store each word length
        # use count_list to store each word valid count consistent to hash_plate
        # use count_map to store count_list distribution
        len_list = []
        count_list = []
        count_map = {}
        for k in range(len(words)):
            hash_word = hash_plate.copy()
            count = 0
            len_list.append(len(words[k]))
            for i, v in enumerate(words[k]):
                if v in hash_word.keys():
                    if hash_word[v] > 0:
                        count = count + 1
                        hash_word[v] = hash_word[v] - 1
            count_list.append(count)
            if count not in count_map:
                count_map[count] = 1
            else:
                count_map[count] = count_map[count] + 1
        # use sub_len_list to store each word length when its valid count is max
        sub_len_list = [len_list[i] for i in range(len(count_list)) if count_list[i] == max(count_list)]
        if count_map[max(count_list)] > 1:
            for j in range(len(count_list)):
                if count_list[j] == max(count_list):
                    if len_list[j] == min(sub_len_list):
                        return(words[j])
        else:
            for j in range(len(count_list)):
                if count_list[j] == max(count_list):
                    return(words[j])

## test
Solution().shortestCompletingWord(licensePlate = '1s3 PSt', words = ['step', 'steps', 'stripe', 'stepple'])
Solution().shortestCompletingWord(licensePlate = '1s3 456', words = ['looks', 'pest', 'stew', 'show'])


## guidance
# store licensePlate and words information respectively
# based on rule, find the shortest word with the max appeared letters
# the time complexity is O(26*n) = O(n), n is number of words
# the space complexity is O(26) = O(1)
