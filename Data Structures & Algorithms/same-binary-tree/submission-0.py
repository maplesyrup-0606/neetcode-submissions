# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def double_dfs(left, right):
            if not left and not right:
                return True
            elif (left and not right) or (not left and right):
                return False
            else:
                if left.val != right.val:
                    return False
                
                return double_dfs(left.left, right.left) and double_dfs(left.right, right.right)
            
        return double_dfs(p, q)