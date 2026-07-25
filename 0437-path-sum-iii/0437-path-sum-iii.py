# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]
        cnt = 0
        while stack:
            curr, path = stack.pop()
            path2 = path.copy()
            while path2:
                pathSum = sum(path2)
                if pathSum == targetSum:
                    cnt += 1
                path2.pop(0)
            if curr.left:
                stack.append((curr.left, path + [curr.left.val]))
            if curr.right:
                stack.append((curr.right, path + [curr.right.val]))
        return cnt