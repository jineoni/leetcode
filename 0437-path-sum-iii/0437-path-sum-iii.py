from collections import defaultdict

class Solution:

    def dfs(self, root, currSum, targetSum, prefix, ans):
        if not root:
            return

        currSum += root.val

        # Count paths ending at current node
        ans[0] += prefix[currSum - targetSum]

        # Add current prefix
        prefix[currSum] += 1

        # Explore left and right subtree
        self.dfs(root.left, currSum, targetSum, prefix, ans)
        self.dfs(root.right, currSum, targetSum, prefix, ans)

        # Backtrack
        prefix[currSum] -= 1


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefix = defaultdict(int)

        # Empty prefix before starting from root
        prefix[0] = 1

        ans = [0]

        self.dfs(root, 0, targetSum, prefix, ans)

        return ans[0]