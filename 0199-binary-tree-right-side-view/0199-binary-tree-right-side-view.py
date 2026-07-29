from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        rightSide = []
        while queue:
            curr, height = queue.popleft()
            if not queue or height != queue[0][1]:
                rightSide.append(curr.val)
            if curr.left:
                queue.append((curr.left, height+1))
            if curr.right:
                queue.append((curr.right, height+1))
        return rightSide