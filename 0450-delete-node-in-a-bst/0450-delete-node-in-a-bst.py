# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:  
        if not root:
            return root
        
        curr = root
        if curr.val == key:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                curr.val = prev.val
                curr.left = self.deleteNode(curr.left, prev.val)
            elif curr.right:
                next = curr.right
                while next.left:
                    next = next.left
                curr.val = next.val
                curr.right = self.deleteNode(curr.right, next.val)
            else:
                curr = None
        elif curr.val > key:
            curr.left = self.deleteNode(curr.left, key)
        else:
            curr.right = self.deleteNode(curr.right, key)
        
        return curr