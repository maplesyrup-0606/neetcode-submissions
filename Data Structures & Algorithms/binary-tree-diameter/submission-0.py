# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            Add up max left and right depth
        """

        def depth2(root, depth):
            if not root:
                return depth
            
            leftDepth = depth2(root.left, depth + 1)
            rightDepth = depth2(root.right, depth + 1)
            return max(leftDepth, rightDepth)
        
        def dfs(root):
            if not root:
                return 0
            
            leftMaxDepth = depth2(root.left, 0)
            rigthMaxDepth = depth2(root.right, 0)

            return max(leftMaxDepth + rigthMaxDepth, dfs(root.left), dfs(root.right))
        
        return dfs(root)
        