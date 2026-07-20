# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = []
        height, maxheight = 1, 1

        stack.append((root, height))
             
        while stack:
            curr, height = stack.pop()

            if curr.left:
                stack.append((curr.left, height+1))
            if curr.right:
                stack.append((curr.right, height+1))
            
            maxheight = max(maxheight, height)
        return maxheight