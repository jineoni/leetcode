# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return (-1, -1)
        
        left_child = self.dfs(root.left)
        right_child = self.dfs(root.right)
        my_left = 1 + left_child[1]
        my_right = 1+ right_child[0]

        self.maximum = max(self.maximum, my_left, my_right)

        return (my_left, my_right)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        self.dfs(root)

        return self.maximum