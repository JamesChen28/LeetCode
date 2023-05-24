
## https://leetcode.com/problems/transpose-matrix/
## Difficulty = Easy

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        
        transpose_matrix = []
        for j in range(n):
            inner_list = []
            for i in range(m):
                inner_list.append(matrix[i][j])
            transpose_matrix.append(inner_list)
            
        return transpose_matrix

## test
Solution().transpose(matrix = [[1, 2, 3],[4 ,5, 6],[7, 8, 9]])
Solution().transpose(matrix = [[1, 2, 3],[4, 5, 6]])


## guidance
# for loop column first, then for loop row, to get the transpose matrix
# the time complexity is O(mn)
# the space complexity is O(1)
