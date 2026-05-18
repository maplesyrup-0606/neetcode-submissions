# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, length):
            if not root:
                return (True, 0)
            
            """
            Get height of left sub and right sub
            """

            leftDepth, rightDepth = 0, 0
            leftBalanced, rightBalanced = False, False

            (leftBalanced, leftDepth) = dfs(root.left, 0)
            (rightBalanced, rightDepth) = dfs(root.right, 0)

            # print(root.val, leftDepth, rightDepth, leftBalanced, rightBalanced)

            if not (leftBalanced and rightBalanced) : return (False, float('inf'))
                
            """ return sub balanced AND curr-balanced """
            return ((abs(leftDepth - rightDepth) <= 1), length + 1 + max(leftDepth, rightDepth))
        
        res = dfs(root, 0)
        return res[0]