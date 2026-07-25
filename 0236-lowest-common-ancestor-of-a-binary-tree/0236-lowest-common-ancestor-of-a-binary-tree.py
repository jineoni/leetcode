# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)