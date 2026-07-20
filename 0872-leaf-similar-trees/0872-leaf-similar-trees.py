# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getSeq(self, stack, seq):
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            if not curr.right and not curr.left:
                seq.append(curr.val)
        return seq

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1, seq2 = [], []
        stack1, stack2 = [root1], [root2]
        self.getSeq(stack1, seq1)
        self.getSeq(stack2, seq2)

        if seq1 == seq2:
            return True
        else:
            return False

        