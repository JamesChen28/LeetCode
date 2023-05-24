
## https://leetcode.com/problems/binary-tree-inorder-traversal/
## Difficulty = Easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        record = []
        if root:
            self.traverse(root, record)
        return record
        
    def traverse(self, node, record):
        if not node:
            return []
        self.traverse(node.left, record)
        record.append(node.val)
        self.traverse(node.right, record)

## test
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3
Solution().inorderTraversal(n1)

# pending
# how to create function to use root to implement?
Solution().inorderTraversal(root = [1, None, 2, 3])
Solution().inorderTraversal(root = [])
Solution().inorderTraversal(root = [1])


## guidance
# use recursive way to visit all nodes, require a linear amount of auxiliary space to record
# use one function to traverse and use another function to record the result
# the time complexity is O(n)
# the space complexity is O(n)
