
## https://leetcode.com/problems/reshape-the-matrix/
## Difficulty = Easy

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        
        matrix_new = [[0] * c for i in range(r)]    
        row = 0
        col = 0
        for i in range(m):
            for j in range(n):
                if col == c:
                    row = row + 1
                    col = 0
                matrix_new[row][col] = mat[i][j]
                col = col + 1
        return matrix_new

## test
Solution().matrixReshape(mat = [[1, 2],[3, 4]], r = 1, c = 4)
Solution().matrixReshape(mat = [[1, 2],[3, 4]], r = 2, c = 4)


## guidance
# use row and col counters to record position in the for loop
# the time complexity is O(mnn)
# the space complexity is O(1)
