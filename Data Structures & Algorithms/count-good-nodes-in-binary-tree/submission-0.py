# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
            when reaching a certain node, we check the maximum on that path and check
            and update max on the way
        """

        def dfs(root, maxSoFar):
            if not root:
                return 0
            else:
                good = root.val >= maxSoFar
                ret = 0
                if good:
                    ret = 1
                newMax = max(maxSoFar, root.val)
                return ret + dfs(root.left, newMax) + dfs(root.right, newMax)
        return dfs(root, float('-inf'))