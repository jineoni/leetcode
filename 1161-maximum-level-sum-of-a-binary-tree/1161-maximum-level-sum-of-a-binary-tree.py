from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        sums = []
        while queue:
            nodeNums = len(queue)
            currSum = 0
            for _ in range(nodeNums):
                curr = queue.popleft()
                currSum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            sums.append(currSum)
        return sums.index(max(sums)) + 1