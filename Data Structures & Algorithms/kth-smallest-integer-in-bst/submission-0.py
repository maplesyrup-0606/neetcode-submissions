# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # inorder traversal
        def inorder(root, res):
            if not root:
                return
            
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
    
        ret = []
        inorder(root, ret)
        return ret[k - 1]
# def inOrder(node, res):
#     if node is None:
#         return

#     # Traverse the left subtree first
#     inOrder(node.left, res)

#     # Visit the current node
#     res.append(node.data)

#     # Traverse the right subtree last
#     inOrder(node.right, res)
