# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root, subRoot):
            if not root and not subRoot: return True
            elif (root and not subRoot) or (not root and subRoot): return False
            else:
                if root.val != subRoot.val: return False
                leftSame = sameTree(root.left, subRoot.left)
                rightSame = sameTree(root.right, subRoot.right)
                return leftSame and rightSame
            
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            elif (root and not subRoot) or (not root and subRoot): return False
            else:
                same = sameTree(root, subRoot)
                if same:
                    return True
                else:
                    return same or dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)