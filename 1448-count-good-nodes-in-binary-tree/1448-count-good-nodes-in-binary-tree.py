# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        stack = [(root, [root.val])]

        while stack:
            curr, path = stack.pop()
            if max(path) == curr.val:
                cnt += 1
            if curr.left:
                stack.append((curr.left, path + [curr.left.val]))
            if curr.right:
                stack.append((curr.right, path + [curr.right.val]))
            
        return cnt